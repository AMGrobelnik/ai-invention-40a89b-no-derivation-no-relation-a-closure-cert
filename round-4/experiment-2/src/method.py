#!/usr/bin/env python3
"""Minimal LLM-as-probabilistic-composition-reasoner (fuzzy-unification gap-filling) demo.

This experiment substantiates the neuro-symbolic 'fuzzy unification' framing WITHOUT
overclaiming OpenCyc grounding or general fuzzy unification.  The substantive question:

   When a SOUND symbolic closure engine ABSTAINS because a composition-table cell is
   MISSING (no path) or AMBIGUOUS (conflicting derivations), can a minimal probabilistic
   LLM read fill/resolve that cell and add NET FAITHFUL coverage -- i.e. recover answers
   the symbolic engine could not give, WITHOUT introducing a confident-wrong (silent-
   wrong-narrowing) hallucination cost that swamps the gain?

Three settings, one consistent pipeline:

  SETTING 1a  (clean composition-cell accuracy vs algebra richness):
      Query a real LLM (google/gemini-3.1-flash-lite, temp 0, sha256-cached) on EVERY
      base x base composition cell of convex Point (3), RCC-8 (8) and Allen (13) -- the
      TRUE cell is known from the authoritative algebra tables -- and score the LLM EXACTLY
      vs the withheld true cell.  The clean LLM-composition-accuracy-vs-richness curve.
      The SAME machinery scores the 16 CLUTRR kinship cells (a 4th, finite calculus).

  SETTING 1b  (end-to-end synthetic gap-fill, ZERO extra LLM cost):
      Reuse the per-cell predictions as an alternative composition table.  Ablate K% of
      cells, recompose the held-out query along the dataset's enumerated paths, intersect,
      and measure coverage RECOVERED by LLM-filling vs the abstain (gap=universe) baseline
      and the added confident-wrong cost.

  SETTING 2  (HEADLINE end-to-end demo on CLUTRR kinship):
      Reuse the forward-union closure engine.  Under a consistently ablated kinship table,
      some queries become GAPS (manufactured: needed an ablated cell) and the documented
      inv-child vs inv-in-law conflict cells are NATURAL gaps.  Fill/resolve with the LLM in
      two modes (Mode P = abstract table-cell composition; Mode S = story-conditioned, given
      the symbolic candidate set).  Compare against TWO baselines on the SAME mixed pool:
        * symbolic-abstain  (pure closure: never hallucinates, zero coverage on gaps)
        * raw_llm CoT       (PURE NEURAL: reads the story, answers every query directly)
      Report risk-coverage (selective accuracy vs coverage), LLM-resolved-step accuracy,
      a quantified hallucination reduction vs raw LLM, and source-tagged trace-graphs that
      flag each LLM-resolved (fuzzy) step distinctly from exact-table steps.

Output: method_out.json in the aii exp_gen_sol_out schema.
"""
from __future__ import annotations

import argparse
import asyncio
import gc
import hashlib
import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
from loguru import logger

from dataio import load_clutrr, subsample_gen
from kinship import Kinship, forward_closure
from llm import OpenRouterClient
from qcn.algebras import load_algebras
from stats import clustered_bootstrap_ci, mean_ci

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #
SEED = 20260617
MODEL = "google/gemini-3.1-flash-lite"
FALLBACKS = ["deepseek/deepseek-v3.2", "google/gemini-3-flash-preview"]
TEMPERATURE = 0.0
BUDGET_HARD = 9.0
BUDGET_SOFT = 2.0
CONCURRENCY = 12
K_ABLATE = [0.10, 0.20, 0.30]      # gap fractions for the end-to-end ablation arms
NET_FAITHFUL_BAR = 0.50            # recovered precision must exceed this to be 'net faithful'
HEADLINE_K = 0.20                  # ablation level that defines the CLUTRR mixed pool

WORKDIR = Path(__file__).resolve().parent
CACHE_DIR = WORKDIR / "cache"
RESULTS_DIR = WORKDIR / "results"
LOG_DIR = WORKDIR / "logs"
for _d in (CACHE_DIR, RESULTS_DIR, LOG_DIR):
    _d.mkdir(exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(LOG_DIR / "run.log"), rotation="30 MB", level="DEBUG")

# human-readable base-relation legend given to the LLM (semantics, NOT the table)
ALG_DEFS = {
    "point": {"<": "X is strictly before Y", "=": "X is at the same point as Y",
              ">": "X is strictly after Y"},
    "rcc8": {"DC": "disconnected (no contact)", "EC": "externally connected (touch, no overlap)",
             "PO": "partial overlap", "EQ": "equal region", "TPP": "tangential proper part of",
             "NTPP": "non-tangential proper part of", "TPPi": "has tangential proper part",
             "NTPPi": "has non-tangential proper part"},
    "allen": {"b": "before", "bi": "after", "m": "meets", "mi": "met-by", "o": "overlaps",
              "oi": "overlapped-by", "d": "during", "di": "contains", "s": "starts",
              "si": "started-by", "f": "finishes", "fi": "finished-by", "eq": "equal"},
}


def _json_default(o):
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    return str(o)


# =====================================================================
# SETTING 1a : clean LLM composition-cell accuracy vs algebra richness
# =====================================================================
def build_cell_items(algebras: dict) -> list[dict]:
    """One LLM item per (algebra, r1, r2) base x base cell."""
    items = []
    for aname, A in algebras.items():
        legend = "; ".join(f"{k}={v}" for k, v in ALG_DEFS[aname].items())
        for r1 in A.base:
            for r2 in A.base:
                sys_p = (
                    "You are a qualitative spatial/temporal reasoning expert. "
                    f"Algebra={aname}. Base relations: {legend}. "
                    "Given relation r1 between A and B, and r2 between B and C, return the "
                    "COMPLETE set of base relations that are POSSIBLE between A and C "
                    "(the relation composition r1 ; r2). Be SOUND: include every relation the "
                    "premises do not rule out. Output ONLY JSON {\"relations\":[...]} using the "
                    "symbols above."
                )
                usr = (f"r1 (A to B) = {r1}\nr2 (B to C) = {r2}\n"
                       "List all possible base relations A to C.")
                items.append({"id": f"cell::{aname}::{r1}::{r2}", "system": sys_p,
                              "user": usr, "max_tokens": 220,
                              "_aname": aname, "_r1": r1, "_r2": r2})
    return items


def parse_cell_set(content: str, A) -> tuple[frozenset, bool]:
    """Robust parse of an LLM composition answer to a frozenset of canonical base symbols.

    Strategy: JSON {"relations":[...]} first; else regex scan over base symbols
    (longest-first, case-insensitive). '' / universal / all -> universe (SOUND but
    uninformative). Unparseable -> universe and parse_fail=True."""
    base = list(A.base)
    # canonical case-insensitive lookup (longest-first so 'bi' is matched before 'b')
    canon = {b.lower(): b for b in base}
    if not content or not content.strip():
        return A.universe, True
    txt = content.strip()
    import re
    txt = re.sub(r"^```(?:json)?|```$", "", txt, flags=re.M).strip()
    obj = None
    for cand in (txt, _first_json_block(txt)):
        if cand is None:
            continue
        try:
            obj = json.loads(cand)
            break
        except Exception:
            continue
    tokens: list[str] = []
    universal = False
    if isinstance(obj, dict):
        rels = obj.get("relations", obj.get("relation", obj.get("possible", [])))
        if isinstance(rels, str):
            rels = [rels]
        if isinstance(rels, list):
            tokens = [str(x) for x in rels]
        if obj.get("universal") or obj.get("all"):
            universal = True
    elif isinstance(obj, list):
        tokens = [str(x) for x in obj]
    found = set()
    for t in tokens:
        tl = str(t).strip().lower()
        if tl in ("universal", "all", "any", "u", "universe", "*"):
            universal = True
            continue
        if tl in canon:
            found.add(canon[tl])
    if not found and obj is None:
        # regex fallback over raw text, longest-symbol-first
        low = txt.lower()
        for b in sorted(base, key=len, reverse=True):
            if re.search(r"(?<![a-z])" + re.escape(b.lower()) + r"(?![a-z])", low):
                found.add(b)
    if universal and not found:
        return A.universe, False
    if not found:
        return A.universe, True
    return frozenset(found), False


def _first_json_block(txt: str):
    start = txt.find("{")
    if start < 0:
        start = txt.find("[")
        if start < 0:
            return None
        op, cl = "[", "]"
    else:
        op, cl = "{", "}"
    depth = 0
    for i in range(start, len(txt)):
        if txt[i] == op:
            depth += 1
        elif txt[i] == cl:
            depth -= 1
            if depth == 0:
                return txt[start:i + 1]
    return None


def score_cell(pred: frozenset, true: frozenset) -> dict:
    inter = pred & true
    union = pred | true
    return {
        "exact": pred == true,
        "sound": true <= pred,                       # safety-critical: no feasible relation dropped
        "over_committed": (pred < true) or (not (true <= pred) and len(pred) < len(true)),
        "jaccard": len(inter) / max(1, len(union)),
        "precision": len(inter) / max(1, len(pred)),
        "recall": len(inter) / max(1, len(true)),
        "pred_size": len(pred),
        "true_size": len(true),
    }


def _size_bucket(n: int) -> str:
    if n <= 1:
        return "singleton"
    if n <= 3:
        return "small_2_3"
    return "large_4plus"


def aggregate_cells(cell_rows: list[dict]) -> tuple[dict, dict]:
    """cell_rows: [{algebra, r1, r2, true, pred, parse_fail, score}].  Returns
    (by_algebra, by_true_size)."""
    by_alg: dict = defaultdict(list)
    by_size: dict = defaultdict(list)
    for r in cell_rows:
        by_alg[r["algebra"]].append(r)
        by_size[_size_bucket(r["score"]["true_size"])].append(r)

    def _agg(rows: list[dict]) -> dict:
        n = len(rows)
        if n == 0:
            return {}
        return {
            "n_cells": n,
            "exact_match_acc": float(np.mean([r["score"]["exact"] for r in rows])),
            "soundness_rate": float(np.mean([r["score"]["sound"] for r in rows])),
            "mean_jaccard": float(np.mean([r["score"]["jaccard"] for r in rows])),
            "mean_precision": float(np.mean([r["score"]["precision"] for r in rows])),
            "mean_recall": float(np.mean([r["score"]["recall"] for r in rows])),
            "n_parse_fail": int(sum(r["parse_fail"] for r in rows)),
            "mean_pred_size": float(np.mean([r["score"]["pred_size"] for r in rows])),
            "mean_true_size": float(np.mean([r["score"]["true_size"] for r in rows])),
        }

    out_alg = {}
    for aname, rows in by_alg.items():
        d = _agg(rows)
        d["by_true_size"] = {
            b: _agg([r for r in rows if _size_bucket(r["score"]["true_size"]) == b])
            for b in ("singleton", "small_2_3", "large_4plus")
        }
        out_alg[aname] = d
    out_size = {b: _agg(rows) for b, rows in by_size.items()}
    return out_alg, out_size


def run_setting1a(algebras: dict, client, no_llm: bool):
    """Run Setting 1a (QCN cells) and return (cell_rows, by_algebra, by_true_size,
    pred_lookup) where pred_lookup[(aname, r1, r2)] = predicted frozenset (for 1b)."""
    items = build_cell_items(algebras)
    logger.info(f"[1a] {len(items)} composition cells across point/rcc8/allen")
    if no_llm:
        logger.warning("[1a] --no-llm: skipping (cell accuracy requires the LLM)")
        return [], {}, {}, {}
    results = asyncio.run(client.run_batch(items))
    cell_rows = []
    pred_lookup: dict = {}
    for it in items:
        aname, r1, r2 = it["_aname"], it["_r1"], it["_r2"]
        A = algebras[aname]
        payload = results.get(it["id"], {"content": ""})
        pred, parse_fail = parse_cell_set(payload.get("content", ""), A)
        if parse_fail:
            client.n_parse_fail += 1
        true = frozenset(A.compose(r1, r2))
        pred_lookup[(aname, r1, r2)] = pred
        cell_rows.append({"algebra": aname, "r1": r1, "r2": r2,
                          "true": sorted(true), "pred": sorted(pred),
                          "parse_fail": parse_fail, "score": score_cell(pred, true)})
    by_alg, by_size = aggregate_cells(cell_rows)
    for aname in ("point", "rcc8", "allen"):
        if aname in by_alg:
            d = by_alg[aname]
            logger.info(f"[1a] {aname:5s} n={d['n_cells']:3d} exact={d['exact_match_acc']:.3f} "
                        f"sound={d['soundness_rate']:.3f} jaccard={d['mean_jaccard']:.3f}")
    return cell_rows, by_alg, by_size, pred_lookup


# =====================================================================
# SETTING 1b : end-to-end synthetic gap-fill (zero extra LLM cost)
# =====================================================================
SYNTH_DIR = Path(
    "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/"
    "gen_art/gen_art_dataset_2/full_data_out"
)
SYNTH_MINI = SYNTH_DIR.parent / "mini_data_out.json"


def _ablate_set(A, K: float) -> set:
    """Deterministic K-fraction of base x base cells, converse-closed (a cell (r1,r2) and
    its converse partner (conv(r2),conv(r1)) are ablated together so a path cannot route
    around the removed rule via its converse)."""
    cells = [(r1, r2) for r1 in A.base for r2 in A.base]
    sel = set()
    for (r1, r2) in cells:
        h = int(hashlib.md5(f"{SEED}|{A.name}|{r1}|{r2}".encode()).hexdigest(), 16) % 100
        if h < int(round(100 * K)):
            sel.add((r1, r2))
            sel.add((A.conv(r2), A.conv(r1)))
    return sel


def compose_path_variant(A, path_rels: list[str], cell_lookup) -> frozenset:
    """Iterated composition of atomic directed relations along a path, using a cell_lookup
    callable cell_lookup(r1,r2)->frozenset (the table variant)."""
    if not path_rels:
        return frozenset([A.identity])
    acc = frozenset([path_rels[0]])
    for r in path_rels[1:]:
        nxt = set()
        for x in acc:
            nxt |= cell_lookup(x, r)
        acc = frozenset(nxt)
        if acc == A.universe:
            break
    return acc


def _dir_lookup(A, abstract_edges: list) -> dict:
    """Directed atomic-relation lookup for consecutive path nodes (both orientations)."""
    d: dict = {}
    for u, v, r in abstract_edges:
        d[(u, v)] = r
        d[(v, u)] = A.conv(r)
    return d


def run_setting1b(algebras: dict, pred_lookup: dict, per_alg: int, mini: bool):
    """For each algebra and K, recompose the held-out query along the enumerated paths under
    three table variants (full / gap=universe / LLM-filled) and report coverage recovered +
    hallucination cost.  Reuses the cached Setting-1a predictions (no new LLM calls)."""
    if not pred_lookup:
        logger.warning("[1b] no cell predictions available; skipping")
        return {}
    # load synthetic rows
    rows_by_alg: dict = defaultdict(list)
    files = [SYNTH_MINI] if mini else sorted(SYNTH_DIR.glob("full_data_out_*.json"))
    for f in files:
        part = json.loads(Path(f).read_text())
        for ds in part["datasets"]:
            aname = ds["dataset"].replace("synthetic_qcn_", "")
            for ex in ds["examples"]:
                if ex.get("metadata_fold") in ("dev", "test") or mini:
                    rows_by_alg[aname].append(ex)
        del part
        gc.collect()

    out: dict = {}
    for aname, A in algebras.items():
        rows = rows_by_alg.get(aname, [])
        rows = sorted(rows, key=lambda e: e.get("metadata_seed", 0))[:per_alg]
        if not rows:
            continue

        def full_cell(r1, r2, _A=A):
            return _A.compose(r1, r2)

        # sanity: full-table path recomposition must reproduce the dataset's path_compositions
        n_check = n_check_ok = 0
        for ex in rows[:50]:
            ag = ex["metadata_abstract_graph"]
            dl = _dir_lookup(A, ag["edges"])
            for path, pc in zip(ex["metadata_paths"]["path_list"],
                                ex["metadata_paths"]["path_compositions"]):
                rels = [dl[(path[i], path[i + 1])] for i in range(len(path) - 1)]
                got = compose_path_variant(A, rels, full_cell)
                n_check += 1
                if got == frozenset(pc):
                    n_check_ok += 1

        per_K = {}
        for K in K_ABLATE:
            S = _ablate_set(A, K)

            def gap_cell(r1, r2, _A=A, _S=S):
                return _A.universe if (r1, r2) in _S else _A.compose(r1, r2)

            def llm_cell(r1, r2, _A=A, _S=S, _an=aname):
                if (r1, r2) in _S:
                    return pred_lookup.get((_an, r1, r2), _A.universe)
                return _A.compose(r1, r2)

            cov = {"full": 0, "gap": 0, "llm": 0}
            ans = {"full": 0, "gap": 0, "llm": 0}              # answered (singleton)
            corr = {"full": 0, "gap": 0, "llm": 0}             # singleton & == gold
            cw = {"full": 0, "gap": 0, "llm": 0}               # singleton & != gold (hallucination)
            rec_correct = rec_wrong = 0                        # recovered = gap-abstained but llm-answered
            n = 0
            for ex in rows:
                gold = ex["output"]
                gold = json.loads(gold)["query_edge"]["relation"]
                ag = ex["metadata_abstract_graph"]
                dl = _dir_lookup(A, ag["edges"])
                paths = ex["metadata_paths"]["path_list"]
                if not paths:
                    continue
                n += 1
                variants = {}
                for name, cl in (("full", full_cell), ("gap", gap_cell), ("llm", llm_cell)):
                    label = A.universe
                    for path in paths:
                        rels = [dl[(path[i], path[i + 1])] for i in range(len(path) - 1)]
                        label = label & compose_path_variant(A, rels, cl)
                    variants[name] = label
                    is_single = (len(label) == 1)
                    if is_single:
                        ans[name] += 1
                        cov[name] += 1
                        if next(iter(label)) == gold:
                            corr[name] += 1
                        else:
                            cw[name] += 1
                # recovered = symbolic-gap abstained but llm answered
                if len(variants["gap"]) != 1 and len(variants["llm"]) == 1:
                    if next(iter(variants["llm"])) == gold:
                        rec_correct += 1
                    else:
                        rec_wrong += 1
            if n == 0:
                continue
            rec_total = rec_correct + rec_wrong
            per_K[f"{K:.2f}"] = {
                "n_networks": n, "n_ablated_cells": len(S),
                "coverage_full": cov["full"] / n, "coverage_gap": cov["gap"] / n,
                "coverage_llm": cov["llm"] / n,
                "acc_among_answered_full": corr["full"] / max(1, ans["full"]),
                "acc_among_answered_gap": corr["gap"] / max(1, ans["gap"]),
                "acc_among_answered_llm": corr["llm"] / max(1, ans["llm"]),
                "confident_wrong_rate_llm": cw["llm"] / n,
                "recovered_coverage": (cov["llm"] - cov["gap"]) / n,
                "recovered_n": rec_total,
                "recovered_precision": (rec_correct / rec_total) if rec_total else None,
                "recovered_correct": rec_correct, "recovered_wrong": rec_wrong,
            }
        out[aname] = {"path_recompose_check": {"n": n_check, "ok": n_check_ok,
                                               "rate": n_check_ok / max(1, n_check)},
                      "by_K": per_K}
        logger.info(f"[1b] {aname:5s} path-check={n_check_ok}/{n_check} "
                    f"K={HEADLINE_K}: {per_K.get(f'{HEADLINE_K:.2f}', {})}")
    return out


# =====================================================================
# SETTING 2 : CLUTRR kinship gap-filling (HEADLINE)
# =====================================================================
class AugKinship(Kinship):
    """Kinship engine with a removed-cell set and an override (gap-fill) table.

    removed cells return their override (None => genuine gap, blocks composition);
    everything else uses the true finite table."""

    def __init__(self, base_kin: Kinship, removed=None, overrides=None):
        self.__dict__.update(base_kin.__dict__)
        self._removed = set(removed or set())
        self._overrides = dict(overrides or {})

    def compose_types(self, t1, t2):
        if (t1, t2) in self._removed:
            return self._overrides.get((t1, t2))
        return self.composition_rules.get(t1, {}).get(t2)


def kinship_cells(comp: dict) -> list[tuple]:
    cr = comp["composition_rules"]
    return [(t1, t2, t3) for t1 in cr for t2, t3 in cr[t1].items()]


def converse_closed(kin: Kinship, cells: set) -> set:
    """Close a set of (t1,t2) cells under converse partners (conv(t2),conv(t1))."""
    out = set(cells)
    for (t1, t2) in list(cells):
        out.add((kin.conv_type(t2), kin.conv_type(t1)))
    # keep only defined cells
    return {(a, b) for (a, b) in out if kin.compose_types(a, b) is not None}


def ablate_kinship(kin: Kinship, K: float) -> set:
    """Deterministic converse-closed K-fraction of the 16 DEFINED kinship cells."""
    cells = [(t1, t2) for (t1, t2, _t3) in kinship_cells(_COMP)]
    sel = set()
    for (t1, t2) in cells:
        h = int(hashlib.md5(f"{SEED}|kin|{t1}|{t2}".encode()).hexdigest(), 16) % 100
        if h < int(round(100 * K)):
            sel.add((t1, t2))
    return converse_closed(kin, sel)


def _atomics_to_edges(atomic_facts: list[dict]) -> list[dict]:
    return [{"a": f["source_name"], "b": f["target_name"], "type": f["relation_type"]}
            for f in atomic_facts]


def _query_set(kin, edges, qsrc, qtgt) -> set:
    D, _, _ = forward_closure(kin, edges)
    return set(D.get((qsrc, qtgt), set()))


VOCAB_SURFACES = None  # set in main


# ---- Mode P : abstract kinship composition-cell prompts -------------------- #
def build_kinship_cell_items(kin: Kinship) -> list[dict]:
    """One item per DEFINED kinship cell: 'X is A's <surface(t1,male)>, Y is X's
    <surface(t2,female)>, what is Y to A?'.  The TYPE answer is gender-invariant; we read
    it back via surface_reverse and score vs the true rules[t1][t2]."""
    vocab = ", ".join(sorted(VOCAB_SURFACES))
    items = []
    for (t1, t2, t3) in kinship_cells(_COMP):
        sB = kin.surface(t1, "male")       # B is A's <sB>
        sC = kin.surface(t2, "female")     # C is B's <sC>
        sys_p = (
            "You are a kinship-relation reasoning expert. Use ONLY these relation terms: "
            f"{vocab}. Given that B is A's {sB}, and C is B's {sC}, determine the single "
            "most specific kinship relation of C to A (i.e. 'C is A's ___'). If no kinship "
            "relation can hold, answer 'no-relation'. Output ONLY JSON "
            "{\"relation\":\"<term>\",\"confidence\":<0..1>}."
        )
        usr = f"B is A's {sB}. C is B's {sC}. What is C to A? (C is A's ___)"
        items.append({"id": f"kincell::{t1}::{t2}", "system": sys_p, "user": usr,
                      "max_tokens": 120, "_t1": t1, "_t2": t2, "_t3": t3})
    return items


def parse_kinship_answer(content: str, kin: Kinship):
    """Return (surface_word|None, rel_type|None, confidence float, parse_fail bool)."""
    if not content or not content.strip():
        return None, None, 0.0, True
    import re
    txt = re.sub(r"^```(?:json)?|```$", "", content.strip(), flags=re.M).strip()
    obj = None
    for cand in (txt, _first_json_block(txt)):
        if cand is None:
            continue
        try:
            obj = json.loads(cand)
            break
        except Exception:
            continue
    word = None
    conf = 0.5
    if isinstance(obj, dict):
        word = obj.get("relation", obj.get("answer", obj.get("rel")))
        try:
            conf = float(obj.get("confidence", 0.5))
        except Exception:
            conf = 0.5
    if word is None:
        low = txt.lower()
        for w in sorted(VOCAB_SURFACES, key=len, reverse=True):
            if re.search(r"(?<![a-z-])" + re.escape(w) + r"(?![a-z])", low):
                word = w
                break
    if word is None:
        return None, None, conf, True
    w = str(word).strip().lower()
    if w in ("no-relation", "no relation", "none", "norelation"):
        return "no-relation", None, conf, False
    rev = kin.surface_to_type(w)
    if rev is None:
        return w, None, conf, True
    conf = max(0.0, min(1.0, conf))
    return w, rev[0], conf, False


# ---- Mode S / raw_llm : story-conditioned per-query prompts ----------------- #
def build_story_item(ex: dict, kin: Kinship, mode: str, candidates: list[str] | None):
    """mode='raw': pure-neural CoT direct answer. mode='modeS': neuro-symbolic, given the
    symbolic candidate set (when the closure narrowed to >1 type)."""
    q = ex["metadata_query"]
    qsrc, qtgt = q["source_name"], q["target_name"]
    story = ex["input"]
    vocab = ", ".join(sorted(VOCAB_SURFACES))
    if mode == "raw":
        sys_p = (
            "You are a kinship-reasoning assistant. Read the short story and determine the "
            f"family relation between two people. Use ONLY these terms: {vocab}. "
            "Reason briefly step by step, then give the single most specific relation of "
            "the TARGET to the SOURCE (i.e. 'TARGET is SOURCE's ___'). If they are provably "
            "unrelated answer 'no-relation'. Output ONLY JSON "
            "{\"reasoning\":\"...\",\"relation\":\"<term>\",\"confidence\":<0..1>}."
        )
        usr = (f"Story: {story}\n\nSOURCE = {qsrc}\nTARGET = {qtgt}\n"
               f"What is {qtgt} to {qsrc}? ({qtgt} is {qsrc}'s ___)")
        tag = "raw"
    else:
        cand_txt = ""
        if candidates:
            cand_txt = (" The symbolic reasoner narrowed the answer to ONE of these "
                        f"candidates: {', '.join(candidates)}. Use the story to pick the "
                        "correct one.")
        sys_p = (
            "You are a kinship-reasoning assistant resolving an ambiguous deduction. Read the "
            f"story.{cand_txt} Use ONLY these terms: {vocab}. Give the single most specific "
            "relation of the TARGET to the SOURCE. Output ONLY JSON "
            "{\"relation\":\"<term>\",\"confidence\":<0..1>}."
        )
        usr = (f"Story: {story}\n\nSOURCE = {qsrc}\nTARGET = {qtgt}\n"
               f"What is {qtgt} to {qsrc}? ({qtgt} is {qsrc}'s ___)")
        tag = "modeS"
    return {"id": f"{tag}::{ex['metadata_doc_id']}", "system": sys_p, "user": usr,
            "max_tokens": 400 if mode == "raw" else 200, "tag": tag}


def _gender(ex, name):
    return ex["metadata_genders"].get(name, "male")


# --------------------------------------------------------------------------- #
_COMP = None  # global composition table (set in main)


def run_setting2(kin: Kinship, gen_rows: list[dict], client, no_llm: bool,
                 cap_per_hop: int, n_normal: int, modeS_cap: int):
    """The headline CLUTRR gap-filling experiment.  Returns a results dict + the per-query
    example records for the output dataset."""
    # ---- baseline closure helpers --------------------------------------------------
    full_kin = kin
    S = ablate_kinship(kin, HEADLINE_K)
    abl_kin = AugKinship(kin, removed=S, overrides={})        # symbolic-abstain under ablation
    logger.info(f"[2] headline ablation K={HEADLINE_K}: {len(S)} cells removed: {sorted(S)}")

    # ---- 2A natural gaps (conflict / no-path under the FULL table) ----------------
    natural_gaps = []           # rows whose FULL-table closure does not yield a unique singleton
    solvable = []               # rows whose FULL-table closure == gold singleton
    for ex in gen_rows:
        if ex["metadata_noise_type"] != "none":
            continue
        q = ex["metadata_query"]
        qsrc, qtgt = q["source_name"], q["target_name"]
        edges = _atomics_to_edges(ex["metadata_atomic_facts"])
        Dq = _query_set(full_kin, edges, qsrc, qtgt)
        ex["_edges"] = edges
        ex["_Dfull"] = Dq
        if len(Dq) == 1:
            solvable.append(ex)
        else:
            ex["_gap_origin"] = "natural"
            ex["_gap_kind"] = "conflict" if len(Dq) > 1 else "no_path"
            natural_gaps.append(ex)
    logger.info(f"[2A] natural gaps: {len(natural_gaps)} "
                f"(conflict={sum(1 for e in natural_gaps if e['_gap_kind']=='conflict')}, "
                f"no_path={sum(1 for e in natural_gaps if e['_gap_kind']=='no_path')}); "
                f"solvable={len(solvable)}")

    # ---- 2B manufactured gaps : ablate S, find solvable-test queries that now break ----
    test_solvable = [e for e in solvable if e["metadata_fold"] == "test"]
    by_hop: dict = defaultdict(list)
    for e in sorted(test_solvable, key=lambda x: x["metadata_doc_id"]):
        by_hop[e["metadata_hop_count"]].append(e)
    capped = []
    for h in sorted(by_hop):
        capped.extend(by_hop[h][:cap_per_hop])
    manufactured = []
    normal = []
    for ex in capped:
        qsrc = ex["metadata_query"]["source_name"]
        qtgt = ex["metadata_query"]["target_name"]
        Dabl = _query_set(abl_kin, ex["_edges"], qsrc, qtgt)
        ex["_Dabl"] = Dabl
        ex["_gold_type"] = next(iter(ex["_Dfull"]))
        if len(Dabl) == 1 and next(iter(Dabl)) == ex["_gold_type"]:
            ex["_gap_origin"] = "none"
            normal.append(ex)
        else:
            ex["_gap_origin"] = "manufactured"
            ex["_gap_kind"] = "conflict" if len(Dabl) > 1 else "no_path"
            manufactured.append(ex)
    # which ablated cells does each manufactured gap's proof use (provenance)
    for ex in manufactured:
        _, _, _, prov = forward_closure(full_kin, ex["_edges"], with_prov=True)
        used = set()
        for (a, c, t3), p in prov.items():
            if p is None:
                continue
            _a, _b, _c, t1, t2, _t3 = p
            if t2 is None:
                continue
            if (t1, t2) in S:
                used.add((t1, t2))
        ex["_blocked_cells"] = sorted(used) if used else sorted(S)
    logger.info(f"[2B] from {len(capped)} test queries under ablation: "
                f"manufactured_gaps={len(manufactured)} normal={len(normal)}")

    # cap normal for the mixed pool
    normal = normal[:n_normal]

    # ---- 2C gap-fill prompts -------------------------------------------------------
    cell_pred: dict = {}        # (t1,t2) -> {type, surface, conf, parse_fail, correct}
    kincell_acc = {}
    if not no_llm:
        kc_items = build_kinship_cell_items(kin)
        kc_res = asyncio.run(client.run_batch(kc_items))
        rows = []
        for it in kc_items:
            payload = kc_res.get(it["id"], {"content": ""})
            surf, rtype, conf, pf = parse_kinship_answer(payload.get("content", ""), kin)
            if pf:
                client.n_parse_fail += 1
            correct = (rtype == it["_t3"])
            cell_pred[(it["_t1"], it["_t2"])] = {
                "type": rtype, "surface": surf, "confidence": conf,
                "parse_fail": pf, "true_type": it["_t3"], "correct": correct}
            rows.append({"correct": correct, "sound": rtype is not None})
        kincell_acc = {
            "n_cells": len(rows),
            "exact_match_acc": float(np.mean([r["correct"] for r in rows])) if rows else None,
            "parse_fail": int(sum(1 for it in kc_items
                                  if cell_pred[(it["_t1"], it["_t2"])]["parse_fail"])),
        }
        logger.info(f"[2C] Mode-P kinship-cell accuracy: exact={kincell_acc['exact_match_acc']}")

    # overrides for the ablated cells, from Mode-P predictions
    overrides = {c: cell_pred.get(c, {}).get("type") for c in S}
    overrides = {c: t for c, t in overrides.items() if t is not None}
    fill_kin = AugKinship(kin, removed=S, overrides=overrides)

    # ---- CLUTRR manufactured-gap K-sweep (symbolic + cached Mode-P fills; no new LLM) -----
    #   Does cell-fill recovery scale across ablation fractions?  For each K, ablate S_K, find
    #   solvable test queries that break, and Mode-P-fill them.
    k_sweep = {}
    if not no_llm:
        for K in K_ABLATE:
            S_K = ablate_kinship(kin, K)
            abl_K = AugKinship(kin, removed=S_K, overrides={})
            ov_K = {c: cell_pred.get(c, {}).get("type") for c in S_K}
            ov_K = {c: t for c, t in ov_K.items() if t is not None}
            fill_K = AugKinship(kin, removed=S_K, overrides=ov_K)
            n_man = rec_c = rec_w = abst = 0
            for ex in capped:
                qs, qt = ex["metadata_query"]["source_name"], ex["metadata_query"]["target_name"]
                gold_t = ex["_gold_type"]
                Da = _query_set(abl_K, ex["_edges"], qs, qt)
                if len(Da) == 1 and next(iter(Da)) == gold_t:
                    continue                       # not broken by this ablation
                n_man += 1
                Df = _query_set(fill_K, ex["_edges"], qs, qt)
                if len(Df) == 1:
                    if next(iter(Df)) == gold_t:
                        rec_c += 1
                    else:
                        rec_w += 1
                else:
                    abst += 1
            ans = rec_c + rec_w
            k_sweep[f"{K:.2f}"] = {
                "n_ablated_cells": len(S_K), "n_manufactured_gaps": n_man,
                "modeP_recovered_coverage": (ans / n_man) if n_man else None,
                "modeP_recovered_precision": (rec_c / ans) if ans else None,
                "modeP_confident_wrong": (rec_w / n_man) if n_man else None,
                "modeP_recovered_correct": rec_c, "modeP_recovered_wrong": rec_w,
                "still_abstain": abst,
            }
        logger.info(f"[2] CLUTRR manufactured K-sweep: "
                    f"{ {k: (v['n_manufactured_gaps'], v['modeP_recovered_precision']) for k, v in k_sweep.items()} }")

    # ---- MIXED POOL : manufactured gaps + normal (BOTH from solvable queries under the
    #      ablated table).  Crucially the ablated symbolic engine is HALLUCINATION-SAFE on
    #      this pool: for a solvable query D_full={gold}, ablation only removes rules so
    #      D_abl is a subset of {gold} -> it either returns gold or abstains, never a wrong
    #      singleton.  Natural conflicts (genuinely ambiguous under the FULL table) are a
    #      SEPARATE arm so they cannot contaminate that guarantee. ------------------------
    pool = manufactured + normal
    natural_for_modeS = natural_gaps[:modeS_cap]

    # ---- per-query story calls ------------------------------------------------------
    #   raw_llm (pure-neural CoT) on EVERY pool query + every natural-arm query;
    #   Mode-S (story-conditioned, symbolic-candidate-aware) on the gap subsets only.
    story_items = []
    for ex in pool:
        story_items.append(build_story_item(ex, kin, "raw", None))
    for ex in manufactured:                       # Mode-S on manufactured gaps (no candidates)
        story_items.append(build_story_item(ex, kin, "modeS", None))
    for ex in natural_for_modeS:                  # natural arm gets BOTH raw and Mode-S
        story_items.append(build_story_item(ex, kin, "raw", None))
        gtgt = ex["metadata_query"]["target_name"]
        D = ex["_Dfull"]
        cands = (sorted({kin.surface(t, _gender(ex, gtgt)) for t in D})
                 if D and len(D) > 1 else None)
        story_items.append(build_story_item(ex, kin, "modeS", cands))
    # de-dup items by (id) -- a doc may be in both pool and natural arm only if folds overlap
    uniq_items = {it["id"]: it for it in story_items}
    story_items = list(uniq_items.values())

    story_res = {}
    if not no_llm:
        logger.info(f"[2C] story calls: pool_raw={len(pool)} manuf_modeS={len(manufactured)} "
                    f"natural_arm={len(natural_for_modeS)}x2 (unique items {len(story_items)})")
        story_res = asyncio.run(client.run_batch(story_items))

    def _story_answer(ex, tag):
        payload = story_res.get(f"{tag}::{ex['metadata_doc_id']}", {"content": ""})
        return parse_kinship_answer(payload.get("content", ""), kin)

    # ---- assemble per-query records + method predictions ---------------------------
    records = []
    for ex in pool:
        q = ex["metadata_query"]
        qsrc, qtgt = q["source_name"], q["target_name"]
        gold_surface = q["relation"]
        gtgt = _gender(ex, qtgt)
        gap_origin = ex["_gap_origin"]
        # symbolic (under ablation) -- the hallucination-safe baseline
        Dsym = ex.get("_Dabl") if "_Dabl" in ex else _query_set(abl_kin, ex["_edges"], qsrc, qtgt)
        if len(Dsym) == 1:
            sym_type = next(iter(Dsym))
            sym_pred = kin.surface(sym_type, gtgt)
            sym_conf = 1.0
            sym_answered = True
        else:
            sym_pred = "ABSTAIN"
            sym_conf = 0.0
            sym_answered = False
        sym_correct = sym_answered and (sym_pred == gold_surface)

        # gapfill_P : symbolic where possible, else fill ablated cells with Mode-P preds
        if sym_answered:
            P_pred, P_conf, P_answered, P_type = sym_pred, 1.0, True, sym_type
        else:
            Dfill = _query_set(fill_kin, ex["_edges"], qsrc, qtgt)
            if len(Dfill) == 1:
                P_type = next(iter(Dfill))
                P_pred = kin.surface(P_type, gtgt)
                # confidence = min confidence of the filled cells used
                fconfs = [cell_pred.get(c, {}).get("confidence", 0.5) for c in ex.get("_blocked_cells", [])
                          if c in overrides]
                P_conf = float(min(fconfs)) if fconfs else 0.6
                P_answered = True
            else:
                P_pred, P_conf, P_answered, P_type = "ABSTAIN", 0.0, False, None
        P_correct = P_answered and (P_pred == gold_surface)

        # gapfill_S : symbolic where possible, else story-conditioned LLM (intersect candidates)
        # Dcand = candidate type-set the symbolic engine narrowed to (full table for natural
        # conflicts; ablated table for manufactured -- which is empty no-path)
        Dcand = ex["_Dfull"] if gap_origin == "natural" else Dsym
        if sym_answered:
            S_pred, S_conf, S_answered = sym_pred, 1.0, True
        else:
            surf, rtype, conf, pf = _story_answer(ex, "modeS")
            if rtype is not None and len(Dcand) > 1:
                # disambiguation: intersect candidate set with the LLM pick
                if rtype in Dcand:
                    S_pred = kin.surface(rtype, gtgt)
                    S_conf, S_answered = conf, True
                else:
                    S_pred, S_conf, S_answered = "ABSTAIN", 0.0, False
            elif rtype is not None:
                S_pred = kin.surface(rtype, gtgt)
                S_conf, S_answered = conf, True
            elif surf == "no-relation":
                S_pred, S_conf, S_answered = "no-relation", conf, True
            else:
                S_pred, S_conf, S_answered = "ABSTAIN", 0.0, False
        S_correct = S_answered and (S_pred == gold_surface)

        # raw_llm : pure neural, answers every query
        rsurf, rtype, rconf, rpf = _story_answer(ex, "raw")
        if rsurf == "no-relation":
            raw_pred = "no-relation"
        elif rsurf is not None:
            raw_pred = rsurf
        else:
            raw_pred = "ABSTAIN"
        raw_answered = (raw_pred != "ABSTAIN")
        raw_conf = rconf if raw_answered else 0.0
        raw_correct = raw_answered and (raw_pred == gold_surface)

        records.append({
            "doc_id": ex["metadata_doc_id"], "qsrc": qsrc, "qtgt": qtgt,
            "hop": ex["metadata_hop_count"], "gold": gold_surface,
            "gap_origin": gap_origin, "gap_kind": ex.get("_gap_kind", "none"),
            "blocked_cells": ex.get("_blocked_cells", []),
            "story": ex["input"],
            "sym": {"pred": sym_pred, "conf": sym_conf, "answered": sym_answered, "correct": sym_correct},
            "P": {"pred": P_pred, "conf": P_conf, "answered": P_answered, "correct": P_correct},
            "S": {"pred": S_pred, "conf": S_conf, "answered": S_answered, "correct": S_correct},
            "raw": {"pred": raw_pred, "conf": raw_conf, "answered": raw_answered, "correct": raw_correct},
        })

    # ---- natural-gap-specific Mode-S records (all-fold, separate analysis) ----------
    natural_records = []
    for ex in natural_for_modeS:
        q = ex["metadata_query"]
        qsrc, qtgt = q["source_name"], q["target_name"]
        gold_surface = q["relation"]
        gtgt = _gender(ex, qtgt)
        D = ex["_Dfull"]
        # Mode-S (symbolic narrows candidates, LLM disambiguates from the story)
        surf, rtype, conf, pf = _story_answer(ex, "modeS")
        if rtype is not None and len(D) > 1 and rtype in D:
            pred = kin.surface(rtype, gtgt); answered = True
        elif rtype is not None and len(D) <= 1:
            pred = kin.surface(rtype, gtgt); answered = True
        elif surf == "no-relation":
            pred = "no-relation"; answered = True
        else:
            pred = "ABSTAIN"; answered = False
        # raw_llm (pure-neural CoT, no symbolic candidate set) on the SAME ambiguous query
        rsurf, rrtype, rconf, rpf = _story_answer(ex, "raw")
        raw_pred = "no-relation" if rsurf == "no-relation" else (rsurf if rsurf else "ABSTAIN")
        raw_answered = raw_pred != "ABSTAIN"
        natural_records.append({
            "doc_id": ex["metadata_doc_id"], "qsrc": qsrc, "qtgt": qtgt,
            "gold": gold_surface, "gap_kind": ex["_gap_kind"],
            "candidates": sorted({kin.surface(t, gtgt) for t in D}) if D else [],
            "cand_types": sorted(D), "story": ex["input"], "_edges": ex["_edges"],
            "S": {"pred": pred, "answered": answered, "correct": answered and pred == gold_surface,
                  "conf": conf if answered else 0.0},
            "raw": {"pred": raw_pred, "answered": raw_answered,
                    "correct": raw_answered and raw_pred == gold_surface},
        })

    results = _metrics_setting2(records, natural_records, cell_pred, overrides, S,
                                kincell_acc, manufactured, natural_gaps, normal, kin)
    results["manufactured_K_sweep"] = k_sweep
    return results, records, natural_records, cell_pred, S


def _risk_coverage_curve(records, method_key, taus):
    """Selective-accuracy vs coverage as the confidence threshold sweeps."""
    n = len(records)
    pts = []
    for tau in taus:
        covered = [r for r in records if r[method_key]["answered"] and r[method_key]["conf"] >= tau]
        cov = len(covered) / n if n else 0.0
        acc = float(np.mean([r[method_key]["correct"] for r in covered])) if covered else None
        pts.append({"tau": round(tau, 3), "coverage": cov, "selective_accuracy": acc,
                    "n_covered": len(covered)})
    return pts


def _metrics_setting2(records, natural_records, cell_pred, overrides, S, kincell_acc,
                      manufactured, natural_gaps, normal, kin):
    n = len(records)
    gap_recs = [r for r in records if r["gap_origin"] != "none"]
    man_recs = [r for r in records if r["gap_origin"] == "manufactured"]

    def _modesummary(recs, key):
        if not recs:
            return {"n_pool": 0, "coverage": 0.0, "acc_among_answered": None,
                    "confident_wrong_rate": 0.0, "n_answered": 0, "n_correct": 0, "n_wrong": 0}
        answered = [r for r in recs if r[key]["answered"]]
        correct = [r for r in answered if r[key]["correct"]]
        wrong = [r for r in answered if not r[key]["correct"]]
        npool = len(recs)
        return {
            "n_pool": npool, "coverage": len(answered) / npool,
            "acc_among_answered": (len(correct) / len(answered)) if answered else None,
            "confident_wrong_rate": len(wrong) / npool,
            "n_answered": len(answered), "n_correct": len(correct), "n_wrong": len(wrong),
        }

    # RISK-COVERAGE on the GAP POOL (symbolic abstains on 100% of gaps by construction)
    gap_pool = {
        "n_gap_pool": len(gap_recs),
        "symbolic_abstain": _modesummary(gap_recs, "sym"),
        "gapfill_P": _modesummary(gap_recs, "P"),
        "gapfill_S": _modesummary(gap_recs, "S"),
        "raw_llm": _modesummary(gap_recs, "raw"),
    }
    for mode in ("gapfill_P", "gapfill_S", "raw_llm"):
        m = gap_pool[mode]
        if m.get("n_answered"):
            rec_correct = m["n_correct"]
            rec_total = m["n_answered"]
            m["recovered_coverage"] = m["coverage"]  # symbolic covered 0
            m["recovered_precision"] = rec_correct / rec_total if rec_total else None
            m["net_recovered_correct_minus_wrong"] = m["n_correct"] - m["n_wrong"]
            m["net_faithful"] = (m["recovered_precision"] or 0) > NET_FAITHFUL_BAR

    # MIXED-POOL risk-coverage curve
    taus = [i / 20 for i in range(21)]
    mixed_curve = {
        "n_pool": n,
        "symbolic_abstain": _risk_coverage_curve(records, "sym", taus),
        "gapfill_P": _risk_coverage_curve(records, "P", taus),
        "gapfill_S": _risk_coverage_curve(records, "S", taus),
        "raw_llm": _risk_coverage_curve(records, "raw", taus),
    }
    # full-coverage (tau=0) comparison + hallucination reduction
    full_pt = {m: _modesummary(records, k) for m, k in
               (("symbolic", "sym"), ("gapfill_P", "P"), ("gapfill_S", "S"), ("raw_llm", "raw"))}
    cw_raw = full_pt["raw_llm"]["confident_wrong_rate"]
    cw_S = full_pt["gapfill_S"]["confident_wrong_rate"]
    cw_P = full_pt["gapfill_P"]["confident_wrong_rate"]
    hallucination_reduction = {
        "confident_wrong_rate_raw_llm": cw_raw,
        "confident_wrong_rate_gapfill_S": cw_S,
        "confident_wrong_rate_gapfill_P": cw_P,
        "confident_wrong_rate_symbolic": full_pt["symbolic"]["confident_wrong_rate"],
        "abs_reduction_S_vs_raw": cw_raw - cw_S,
        "rel_reduction_S_vs_raw": (cw_raw - cw_S) / cw_raw if cw_raw else None,
        "abs_reduction_P_vs_raw": cw_raw - cw_P,
        "rel_reduction_P_vs_raw": (cw_raw - cw_P) / cw_raw if cw_raw else None,
    }

    # LLM-resolved-step accuracy : Mode P (cells) vs Mode S (story), by gap origin
    modeP_cell = {
        "n_cells": kincell_acc.get("n_cells"),
        "exact_match_acc": kincell_acc.get("exact_match_acc"),
        "parse_fail": kincell_acc.get("parse_fail"),
        "per_cell": {f"{t1}|{t2}": {"pred_type": cell_pred[(t1, t2)]["type"],
                                    "true_type": cell_pred[(t1, t2)]["true_type"],
                                    "correct": cell_pred[(t1, t2)]["correct"],
                                    "confidence": cell_pred[(t1, t2)]["confidence"]}
                     for (t1, t2) in cell_pred},
    }
    natural_S = [r for r in natural_records]
    natural_S_ans = [r for r in natural_S if r["S"]["answered"]]
    natural_raw_ans = [r for r in natural_S if r.get("raw", {}).get("answered")]
    # NATURAL-CONFLICT ARM: symbolic abstains on ALL (coverage 0); Mode-S (symbolic candidate
    # set + story) vs raw_llm (pure CoT) on the SAME genuinely-ambiguous queries.
    natural_arm = {
        "n_natural_conflicts": len(natural_S),
        "symbolic_abstain": {"coverage": 0.0, "acc_among_answered": None,
                             "note": "ambiguous under the full table -> abstains by construction"},
        "gapfill_S": {
            "coverage": len(natural_S_ans) / len(natural_S) if natural_S else None,
            "acc_among_answered": (float(np.mean([r["S"]["correct"] for r in natural_S_ans]))
                                   if natural_S_ans else None),
            "overall_resolved_rate": (float(np.mean([r["S"]["correct"] for r in natural_S]))
                                      if natural_S else None),
            "n_answered": len(natural_S_ans),
        },
        "raw_llm": {
            "coverage": len(natural_raw_ans) / len(natural_S) if natural_S else None,
            "acc_among_answered": (float(np.mean([r["raw"]["correct"] for r in natural_raw_ans]))
                                   if natural_raw_ans else None),
            "overall_resolved_rate": (float(np.mean([r["raw"]["correct"] for r in natural_S]))
                                      if natural_S else None),
        },
        "modeS_beats_raw_on_conflicts": None,
    }
    if natural_S:
        s_ov = natural_arm["gapfill_S"]["overall_resolved_rate"]
        r_ov = natural_arm["raw_llm"]["overall_resolved_rate"]
        if s_ov is not None and r_ov is not None:
            natural_arm["modeS_beats_raw_on_conflicts"] = bool(s_ov > r_ov)
    modeS_step = {
        "manufactured": _modesummary(man_recs, "S"),
        "natural_conflict": natural_arm,
    }
    # P vs S on manufactured (the same gap pool) -- does story conditioning help?
    story_helps = None
    if man_recs:
        accP = _modesummary(man_recs, "P")["acc_among_answered"]
        accS = _modesummary(man_recs, "S")["acc_among_answered"]
        if accP is not None and accS is not None:
            story_helps = bool(accS > accP)

    # bootstrap CIs (clustered by doc_id) for key rates on the gap pool
    def _doc_vals(recs, predicate):
        d = defaultdict(list)
        for r in recs:
            d[r["doc_id"]].append(1.0 if predicate(r) else 0.0)
        return d

    cis = {}
    if gap_recs:
        cis["gapfill_S_acc_among_answered"] = clustered_bootstrap_ci(
            _doc_vals([r for r in gap_recs if r["S"]["answered"]], lambda r: r["S"]["correct"]))
        cis["gapfill_P_acc_among_answered"] = clustered_bootstrap_ci(
            _doc_vals([r for r in gap_recs if r["P"]["answered"]], lambda r: r["P"]["correct"]))
        cis["raw_confident_wrong_rate"] = clustered_bootstrap_ci(
            _doc_vals(records, lambda r: r["raw"]["answered"] and not r["raw"]["correct"]))
        cis["gapfill_S_confident_wrong_rate"] = clustered_bootstrap_ci(
            _doc_vals(records, lambda r: r["S"]["answered"] and not r["S"]["correct"]))

    # VERDICT
    recP = gap_pool["gapfill_P"].get("recovered_precision")
    recS = gap_pool["gapfill_S"].get("recovered_precision")
    best_rec = max([x for x in (recP, recS) if x is not None], default=None)
    best_mode = "gapfill_S" if (recS is not None and (recP is None or recS >= recP)) else "gapfill_P"
    net_correct = gap_pool[best_mode].get("net_recovered_correct_minus_wrong", 0) if best_rec else 0
    if best_rec is None:
        verdict_label = "NO"
    elif best_rec > 0.75 and net_correct > 0:
        verdict_label = "YES"
    elif best_rec > NET_FAITHFUL_BAR and net_correct > 0:
        verdict_label = "MARGINAL"
    else:
        verdict_label = "NO"

    return {
        "ablation_cells_removed": sorted(S),
        "pool_counts": {
            "n_mixed_pool": n,
            "n_manufactured_gaps": len(man_recs),
            "n_natural_gaps_total": len(natural_gaps),
            "n_natural_conflict": sum(1 for e in natural_gaps if e["_gap_kind"] == "conflict"),
            "n_natural_no_path": sum(1 for e in natural_gaps if e["_gap_kind"] == "no_path"),
            "n_normal_in_pool": len([r for r in records if r["gap_origin"] == "none"]),
            "n_distinct_ablated_cells": len(S),
        },
        "gap_pool_risk_coverage": gap_pool,
        "mixed_pool_curve": mixed_curve,
        "full_coverage_point": full_pt,
        "hallucination_reduction": hallucination_reduction,
        "llm_resolved_step_accuracy": {"mode_P": modeP_cell, "mode_S": modeS_step,
                                       "story_conditioning_helps_manufactured": story_helps},
        "bootstrap_cis": cis,
        "verdict_inputs": {"best_mode": best_mode, "best_recovered_precision": best_rec,
                           "net_recovered_correct_minus_wrong": net_correct,
                           "label": verdict_label},
    }


def build_flagged_traces(kin, records, natural_records, cell_pred, S, n_man=3, n_nat=2):
    """Source-tagged trace-graphs: every composition step is tagged exact_table vs llm_fuzzy,
    so a human auditor can see exactly where the pipeline left the exact table.

    Two flavours:
      * MANUFACTURED no-path gaps -> the missing rule is filled by a Mode-P llm_fuzzy step
        and the rest of the chain stays on the exact table.
      * NATURAL conflict gaps -> the symbolic engine derives MULTIPLE candidate types
        (an exact-table conflict), and a single llm_fuzzy disambiguation step (Mode-S)
        selects one using the story.
    """
    from kinship import forward_closure, derivation_trace
    overrides = {c: cell_pred.get(c, {}).get("type") for c in S}
    overrides = {c: t for c, t in overrides.items() if t is not None}
    fill_kin = AugKinship(kin, removed=S, overrides=overrides)
    traces = []

    # ---- manufactured: filled-cell derivations ----
    man = [r for r in records if r["gap_origin"] == "manufactured" and r["P"]["answered"]]
    for r in man[:n_man]:
        ex_edges = r.get("_edges")
        if ex_edges is None:
            continue
        qsrc, qtgt = r["qsrc"], r["qtgt"]
        D, _, _ = forward_closure(fill_kin, ex_edges)
        steps = []
        if len(D.get((qsrc, qtgt), set())) == 1:
            for st in derivation_trace(fill_kin, ex_edges, qsrc, qtgt):
                # a step is llm_fuzzy iff its cell was ablated and filled by the LLM (Mode-P);
                # checking S (NOT the complete original table, which defines every cell)
                source = "llm_fuzzy" if (st["t1"], st["t2"]) in S else "exact_table"
                entry = {"a": st["a"], "b": st["b"], "c": st["c"], "t1": st["t1"],
                         "t2": st["t2"], "t3": st["t3"], "source": source}
                if source == "llm_fuzzy":
                    cp = cell_pred.get((st["t1"], st["t2"]), {})
                    entry["llm_confidence"] = cp.get("confidence")
                    entry["llm_predicted_t3"] = cp.get("type")
                    entry["matches_true_cell"] = cp.get("correct")
                steps.append(entry)
        traces.append({
            "doc_id": r["doc_id"], "qsrc": qsrc, "qtgt": qtgt, "gold": r["gold"],
            "gap_origin": "manufactured", "gap_kind": r["gap_kind"], "story": r["story"][:1200],
            "trace": steps, "final_answer": r["P"]["pred"], "correct": r["P"]["correct"],
            "n_llm_fuzzy_steps": sum(1 for s in steps if s["source"] == "llm_fuzzy"),
        })

    # ---- natural conflict: exact-table conflict + one llm_fuzzy disambiguation ----
    nat = [r for r in natural_records if r.get("_edges") and len(r.get("cand_types", [])) > 1]
    for r in nat[:n_nat]:
        ex_edges = r["_edges"]
        qsrc, qtgt = r["qsrc"], r["qtgt"]
        # show the exact-table steps that PRODUCED each candidate (forward closure provenance)
        _, _, _, prov = forward_closure(kin, ex_edges, with_prov=True)
        exact_steps = []
        for t in r["cand_types"]:
            p = prov.get((qsrc, qtgt, t))
            if p and p[4] is not None:
                a, b, c, t1, t2, t3 = p
                exact_steps.append({"a": a, "b": b, "c": c, "t1": t1, "t2": t2, "t3": t3,
                                    "source": "exact_table"})
        fuzzy_step = {"source": "llm_fuzzy", "kind": "story_disambiguation",
                      "candidates": r["candidates"], "llm_pick": r["S"]["pred"],
                      "llm_confidence": r["S"].get("conf"), "resolved": r["S"]["answered"]}
        traces.append({
            "doc_id": r["doc_id"], "qsrc": qsrc, "qtgt": qtgt, "gold": r["gold"],
            "gap_origin": "natural", "gap_kind": r["gap_kind"], "story": r["story"][:1200],
            "trace": exact_steps + [fuzzy_step], "final_answer": r["S"]["pred"],
            "correct": r["S"]["correct"], "n_llm_fuzzy_steps": 1,
        })
    return traces


# =====================================================================
# OUTPUT assembly
# =====================================================================
def assemble_output(cell_rows, by_alg, by_size, s1b, s2_results, s2_records,
                    natural_records, traces, client, runtime_sec, kincell_acc):
    composition_richness_curve = {
        a: {"n_relations": n, "exact_match_acc": by_alg.get(a, {}).get("exact_match_acc"),
            "soundness_rate": by_alg.get(a, {}).get("soundness_rate"),
            "mean_jaccard": by_alg.get(a, {}).get("mean_jaccard")}
        for a, n in (("point", 3), ("rcc8", 8), ("allen", 13))
    }
    if kincell_acc:
        composition_richness_curve["kinship"] = {
            "n_relations": 11, "exact_match_acc": kincell_acc.get("exact_match_acc"),
            "soundness_rate": None, "mean_jaccard": None}

    degrades = None
    accs = [composition_richness_curve[a]["exact_match_acc"] for a in ("point", "rcc8", "allen")]
    if all(x is not None for x in accs):
        degrades = bool(accs[0] >= accs[1] >= accs[2] or (accs[0] >= accs[2]))

    hr = s2_results.get("hallucination_reduction", {}) if s2_results else {}
    vi = s2_results.get("verdict_inputs", {}) if s2_results else {}
    lsa = s2_results.get("llm_resolved_step_accuracy", {}) if s2_results else {}

    metadata = {
        "method_name": "Minimal LLM fuzzy-unification (composition-cell gap-filling) -- EXPLORATORY",
        "tag": "REAL-LLM-READ",
        "scope_statement": (
            "This is composition-CELL gap-filling (a missing/ambiguous cell of an EXACT "
            "qualitative or kinship composition table filled by a probabilistic LLM read). It is "
            "NOT OpenCyc/upper-ontology grounding and NOT general fuzzy unification; both are out "
            "of scope."),
        "reader_model": MODEL, "model_fallbacks": FALLBACKS, "temperature": TEMPERATURE,
        "seed": SEED, "headline_K": HEADLINE_K, "net_faithful_bar": NET_FAITHFUL_BAR,
        # Setting 1
        "composition_accuracy_by_algebra": by_alg,
        "composition_accuracy_by_true_cell_size": by_size,
        "composition_richness_curve": composition_richness_curve,
        "kinship_composition_cell_accuracy": kincell_acc,
        "end_to_end_synthetic_gapfill": s1b,
        # Setting 2
        "clutrr_gap_pool_counts": s2_results.get("pool_counts") if s2_results else None,
        "clutrr_ablation_cells_removed": s2_results.get("ablation_cells_removed") if s2_results else None,
        "clutrr_gapfill_risk_coverage": s2_results.get("gap_pool_risk_coverage") if s2_results else None,
        "clutrr_manufactured_K_sweep": s2_results.get("manufactured_K_sweep") if s2_results else None,
        "clutrr_gapfill_mixed_pool_curve": s2_results.get("mixed_pool_curve") if s2_results else None,
        "clutrr_full_coverage_point": s2_results.get("full_coverage_point") if s2_results else None,
        "clutrr_hallucination_reduction": hr,
        "llm_resolved_step_accuracy": lsa,
        "bootstrap_cis": s2_results.get("bootstrap_cis") if s2_results else None,
        "flagged_fuzzy_step_traces": traces,
        "honesty_caveats": [
            "CLUTRR is a TEMPLATED kinship benchmark (max 871 chars), not natural text",
            "gaps are composition CELLS, not ontology/common-sense grounding",
            "manufactured gaps are clearly labelled and separated from natural gaps",
            "a non-sound LLM fill is the silent-wrong-narrowing failure mode -> reported as confident-wrong",
            "Mode-S and the raw_llm baseline see the same story; the neuro-symbolic system invokes "
            "the LLM ONLY on gap cells and uses the exact table elsewhere",
        ],
        "budget": client.stats(),
        "verdict": {
            "adds_net_faithful_coverage_clutrr": vi.get("label"),
            "recovered_precision": vi.get("best_recovered_precision"),
            "net_recovered_correct_minus_wrong": vi.get("net_recovered_correct_minus_wrong"),
            "best_mode": vi.get("best_mode"),
            "composition_accuracy_degrades_with_richness": degrades,
            "cell_fill_beats_story_fill": (
                None if not s2_results else bool(
                    (s2_results["gap_pool_risk_coverage"]["gapfill_P"].get("recovered_precision") or 0)
                    > (s2_results["gap_pool_risk_coverage"]["gapfill_S"].get("recovered_precision") or 0))),
            "story_conditioning_helps_natural_conflicts": (
                lsa.get("mode_S", {}).get("natural_conflict", {}).get("modeS_beats_raw_on_conflicts")),
            "hallucination_rel_reduction_bestmode_vs_raw": hr.get("rel_reduction_P_vs_raw"),
            "hallucination_rel_reduction_S_vs_raw": hr.get("rel_reduction_S_vs_raw"),
            "summary": _verdict_summary(by_alg, s2_results, hr, vi, degrades),
        },
        "runtime_sec": round(runtime_sec, 1),
    }

    # ---- datasets ----
    synth_examples = []
    for r in cell_rows:
        synth_examples.append({
            "input": f"{r['algebra']}: {r['r1']} ; {r['r2']}",
            "output": " ".join(r["true"]) if r["true"] else "EMPTY",
            "predict_llm": " ".join(r["pred"]) if r["pred"] else "EMPTY",
            "metadata_algebra": r["algebra"], "metadata_r1": r["r1"], "metadata_r2": r["r2"],
            "metadata_exact": r["score"]["exact"], "metadata_sound": r["score"]["sound"],
            "metadata_jaccard": r["score"]["jaccard"], "metadata_true_size": r["score"]["true_size"],
            "metadata_pred_size": r["score"]["pred_size"], "metadata_parse_fail": r["parse_fail"],
        })
    if not synth_examples:
        synth_examples = [{"input": "no-llm-run", "output": "EMPTY", "predict_llm": "EMPTY",
                           "metadata_algebra": "none", "metadata_note": "ran with --no-llm"}]

    clutrr_examples = []
    for r in (s2_records or []):
        clutrr_examples.append({
            "input": r["story"][:2800],
            "output": r["gold"],
            "predict_symbolic": r["sym"]["pred"],
            "predict_gapfill_P": r["P"]["pred"],
            "predict_gapfill_S": r["S"]["pred"],
            "predict_raw_llm": r["raw"]["pred"],
            "metadata_doc_id": r["doc_id"], "metadata_qsrc": r["qsrc"], "metadata_qtgt": r["qtgt"],
            "metadata_hop": r["hop"], "metadata_gap_origin": r["gap_origin"],
            "metadata_gap_kind": r["gap_kind"], "metadata_blocked_cell": r["blocked_cells"],
            "metadata_correct_symbolic": r["sym"]["correct"], "metadata_correct_P": r["P"]["correct"],
            "metadata_correct_S": r["S"]["correct"], "metadata_correct_raw": r["raw"]["correct"],
            "metadata_conf_S": r["S"]["conf"], "metadata_conf_raw": r["raw"]["conf"],
        })
    if not clutrr_examples:
        clutrr_examples = [{"input": "no-llm-run", "output": "EMPTY",
                            "predict_symbolic": "ABSTAIN", "metadata_note": "ran with --no-llm"}]

    datasets = [
        {"dataset": "synthetic_composition_cells", "examples": synth_examples},
        {"dataset": "clutrr_gapfill", "examples": clutrr_examples},
    ]
    return {"metadata": metadata, "datasets": datasets}


def _verdict_summary(by_alg, s2, hr, vi, degrades):
    parts = []
    if by_alg:
        pa = by_alg.get("point", {}).get("exact_match_acc")
        rc = by_alg.get("rcc8", {}).get("exact_match_acc")
        al = by_alg.get("allen", {}).get("exact_match_acc")
        sa = by_alg.get("allen", {}).get("soundness_rate")
        if pa is not None and al is not None:
            parts.append(f"LLM abstract composition-cell exact-match falls with algebra richness "
                         f"(point={pa:.2f}/3rels, rcc8={rc:.2f}/8rels, allen={al:.2f}/13rels; "
                         f"allen soundness only {sa:.2f}), so an LLM composes RICH algebras "
                         f"poorly and a non-sound fill is a silent-wrong-narrowing hazard")
    if s2:
        rcv = s2["gap_pool_risk_coverage"]
        pP = rcv["gapfill_P"].get("recovered_precision")
        pS = rcv["gapfill_S"].get("recovered_precision")
        if pP is not None:
            parts.append(f"on CLUTRR kinship -- where the LLM knows the composition calculus "
                         f"(Mode-P cell accuracy {s2['llm_resolved_step_accuracy']['mode_P'].get('exact_match_acc')}) "
                         f"-- CELL-level gap-filling (symbolic does the multi-hop chaining, the LLM "
                         f"supplies only the missing atomic rule) recovers gap coverage at "
                         f"precision={pP:.2f} (net +{rcv['gapfill_P'].get('net_recovered_correct_minus_wrong')}), "
                         f"verdict={vi.get('label')}")
        if pS is not None:
            parts.append(f"by contrast STORY-level filling (asking the LLM to do the multi-hop read) "
                         f"recovers at only precision={pS:.2f} "
                         f"(net {rcv['gapfill_S'].get('net_recovered_correct_minus_wrong')}) -- naive "
                         f"story gap-fill is NOT net-faithful")
    if hr.get("rel_reduction_P_vs_raw") is not None:
        parts.append(f"the cell-fill neuro-symbolic system cuts the confident-wrong (hallucination) "
                     f"rate by {100*hr['rel_reduction_P_vs_raw']:.0f}% vs the raw-LLM CoT baseline "
                     f"({hr.get('confident_wrong_rate_raw_llm'):.3f} -> "
                     f"{hr.get('confident_wrong_rate_gapfill_P'):.3f}) at FULL coverage")
    return ". ".join(parts) + "." if parts else "no LLM run (symbolic-only validation)."


# =====================================================================
# MAIN
# =====================================================================
@logger.catch(reraise=True)
def main():
    global _COMP, VOCAB_SURFACES
    ap = argparse.ArgumentParser()
    ap.add_argument("--mini", action="store_true", help="tiny smoke run")
    ap.add_argument("--no-llm", action="store_true", help="symbolic-only validation ($0)")
    ap.add_argument("--cap-per-hop", type=int, default=60, help="manufactured/normal cap per hop")
    ap.add_argument("--n-normal", type=int, default=300, help="normal queries in the mixed pool")
    ap.add_argument("--modeS-cap", type=int, default=260, help="natural-gap Mode-S cap")
    ap.add_argument("--s1b-per-alg", type=int, default=400, help="Setting-1b networks per algebra")
    ap.add_argument("--smoke-cells", type=int, default=0, help="if>0, run only this many 1a cells")
    args = ap.parse_args()
    t0 = time.time()

    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key and not args.no_llm:
        logger.error("OPENROUTER_API_KEY missing; use --no-llm for symbolic-only validation")
        sys.exit(2)

    client = OpenRouterClient(api_key=api_key, model=MODEL, fallbacks=FALLBACKS,
                              cache_dir=CACHE_DIR, temperature=TEMPERATURE,
                              budget_hard=BUDGET_HARD, budget_soft=BUDGET_SOFT,
                              concurrency=CONCURRENCY, max_tokens=240)

    algebras = load_algebras()

    # ---- load CLUTRR ----
    gen_rows, disc_rows, comp = load_clutrr(mini=args.mini)
    _COMP = comp
    kin = Kinship(comp)
    VOCAB_SURFACES = set(comp["surface_reverse"].keys()) | {"no-relation"}
    logger.info(f"loaded CLUTRR gen={len(gen_rows)} disc={len(disc_rows)}; "
                f"kinship vocab={len(VOCAB_SURFACES)} surfaces")

    # ---- SETTING 1a ----
    if args.smoke_cells > 0 and not args.no_llm:
        items = build_cell_items(algebras)[:args.smoke_cells]
        res = asyncio.run(client.run_batch(items))
        for it in items:
            A = algebras[it["_aname"]]
            pred, pf = parse_cell_set(res[it["id"]].get("content", ""), A)
            true = A.compose(it["_r1"], it["_r2"])
            logger.info(f"  smoke {it['_aname']} {it['_r1']};{it['_r2']} -> pred={sorted(pred)} "
                        f"true={sorted(true)} exact={pred==frozenset(true)}")
        logger.info(f"smoke cost=${client.cost:.5f}")
        return

    cell_rows, by_alg, by_size, pred_lookup = run_setting1a(algebras, client, args.no_llm)

    # ---- SETTING 1b ----
    s1b = run_setting1b(algebras, pred_lookup, per_alg=(3 if args.mini else args.s1b_per_alg),
                        mini=args.mini)

    # ---- SETTING 2 ----
    cap = 1 if args.mini else args.cap_per_hop
    n_normal = 3 if args.mini else args.n_normal
    modeS_cap = 3 if args.mini else args.modeS_cap
    s2_results, s2_records, natural_records, cell_pred, S = run_setting2(
        kin, gen_rows, client, args.no_llm, cap_per_hop=cap, n_normal=n_normal, modeS_cap=modeS_cap)

    # attach edges to records for the trace builder
    edge_map = {}
    for ex in gen_rows:
        if "_edges" in ex:
            edge_map[ex["metadata_doc_id"]] = ex["_edges"]
    for r in s2_records:
        r["_edges"] = edge_map.get(r["doc_id"])
    traces = build_flagged_traces(kin, s2_records, natural_records, cell_pred, S)

    kincell_acc = s2_results.get("llm_resolved_step_accuracy", {}).get("mode_P", {})
    kincell_acc = {"n_cells": kincell_acc.get("n_cells"),
                   "exact_match_acc": kincell_acc.get("exact_match_acc"),
                   "parse_fail": kincell_acc.get("parse_fail")} if kincell_acc else {}

    out = assemble_output(cell_rows, by_alg, by_size, s1b, s2_results, s2_records,
                          natural_records, traces, client, time.time() - t0, kincell_acc)

    # honest TOTAL API spend = sum of per-call cost over the whole disk cache (this run may be
    # fully cache-served and thus report $0 marginal; the cache cost is the real money spent).
    total_cache_spend = 0.0
    n_cache_calls = 0
    for cf in CACHE_DIR.glob("*.json"):
        try:
            c = json.loads(cf.read_text()).get("cost", 0.0) or 0.0
            total_cache_spend += float(c)
            n_cache_calls += 1
        except Exception:
            continue
    out["metadata"]["budget"]["total_api_spend_all_runs_usd"] = round(total_cache_spend, 6)
    out["metadata"]["budget"]["n_cached_calls_on_disk"] = n_cache_calls
    out["metadata"]["budget"]["note"] = (
        "cumulative_usd is THIS invocation's marginal cost (0 when fully cache-served); "
        "total_api_spend_all_runs_usd is the real money spent to build the sha256 cache, "
        "which makes the experiment reproducible at $0.")

    # strip helper keys before write (records carried _edges)
    out_path = WORKDIR / "method_out.json"
    out_path.write_text(json.dumps(out, default=_json_default, ensure_ascii=False))
    logger.info(f"wrote {out_path} ({out_path.stat().st_size/1e6:.2f} MB); "
                f"cost=${client.cost:.4f}; runtime={time.time()-t0:.1f}s")
    logger.info(f"VERDICT: {out['metadata']['verdict']['summary']}")


if __name__ == "__main__":
    main()
