#!/usr/bin/env python3
"""Genuine LLM fuzzy-unification with a certificate-bounded hallucination guarantee.

This experiment converts reviewer MAJOR #2 -- "Mode-P 'fuzzy unification' was circular
memorized-table recall (confidence exactly 1.0 on every kinship cell)" -- into a REAL
contribution.  We construct GENUINELY-fuzzy LLM reads from EXISTING gold in two labeled
settings, and show that a training-free abstain-on-collapse CERTIFICATE bounds the
hallucination cost of feeding those fuzzy reads into a sound symbolic closure engine.

SETTING 1  -- VAGUE / OUT-OF-TABLE SPATIAL RCC-8 (SpaRP-PS1, art_f-ofxduZjwSM):
    A KNOWN RCC-8 relation between two regions is rendered with a VAGUE preposition
    ("near", "touching", "around", "inside", "overlapping") that has NO single RCC-8
    answer.  A real LLM (google/gemini-3.1-flash-lite, temp 0) MUST emit a CALIBRATED
    sub-1.0 disjunction over the 8 base relations.  We measure CALIBRATION (ECE +
    reliability) and show the confidences are genuinely <1.0 and reasonably calibrated.

SETTING 2  -- AMBIGUOUS / PARAPHRASED KINSHIP (CLUTRR, art_HS7-lxhZnU9m):
    An atomic kinship fact is replaced by an informal/under-specified term ("guardian",
    "descendant", "family elder", "sibling-figure", "relative by marriage") that maps to
    a TYPE-DISJUNCTION.  Same calibration measurement.

In BOTH settings the fuzzy disjunction + the OTHER exact-table constituent reads are fed
into the existing closure engines (qcn.algebras RCC-8 / a disjunctive-seed kinship
forward-union closure).  The OUTPUT CONTRACT is:

    |D_query| == 1  -> COMMIT the singleton              (covered)
    |D_query| == 0  -> Mode-B COLLAPSE  (gold-free certificate flags an UNSOUND read)
    |D_query| >  1  -> ABSTAIN          (non-singleton, disjunction preserved)

This is measured as a RISK-COVERAGE tradeoff vs (a) a commit-the-argmax baseline that
ignores the disjunction (point estimate, always answers) and (b) an abstain-always
baseline.  The KEY invariant (proved by construction and asserted): when every
contributing fuzzy read is SOUND (gold in the emitted set), confident-wrong == 0
(read-soundness-conditional zero-FP).  Auditable trace-graphs flag every LLM-resolved
fuzzy step (with its <1.0 confidence) distinctly from exact-table steps.

STAGE 4 contrasts the calibrated sub-1.0 fuzzy reads with the memorized Mode-P
(frac_conf_1p0 ~= 1.0); STAGE 5 re-runs the reads on deepseek-v3.2 (cross-family
sensitivity).  Output: method_out.json in the aii exp_gen_sol_out schema.
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

from dataio import load_clutrr
from kinship import Kinship, query_modeA, forward_closure, derivation_trace
from llm import OpenRouterClient
from qcn.algebras import load_algebras, RCC8_BASE
from stats import clustered_bootstrap_ci, mean_ci

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #
SEED = 20260617
MODEL = "google/gemini-3.1-flash-lite"
FALLBACKS = ["deepseek/deepseek-v3.2", "google/gemini-3-flash-preview"]
SENS_MODEL = "deepseek/deepseek-v3.2"            # cross-family sensitivity reader
TEMPERATURE = 0.0
BUDGET_HARD = 9.0
BUDGET_SOFT = 2.0
CONCURRENCY = 12

WORKDIR = Path(__file__).resolve().parent
CACHE_DIR = WORKDIR / "cache"
RESULTS_DIR = WORKDIR / "results"
LOG_DIR = WORKDIR / "logs"
for _d in (CACHE_DIR, RESULTS_DIR, LOG_DIR):
    _d.mkdir(exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(LOG_DIR / "run.log"), rotation="30 MB", level="DEBUG")

# Dependency data paths -------------------------------------------------------
SPATIAL_FULL = Path(
    "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/"
    "gen_art/gen_art_dataset_1/full_data_out.json")
SPATIAL_MINI = SPATIAL_FULL.parent / "mini_data_out.json"
MODEP_PRIOR = Path(
    "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/"
    "gen_art/gen_art_experiment_2/method_out.json")

# RCC-8 legend given to the LLM (semantics, NOT the composition table) --------
RCC8_GLOSS = {
    "DC": "disconnected (the regions do not touch at all)",
    "EC": "externally connected (their boundaries touch but interiors do not overlap)",
    "PO": "partial overlap (interiors overlap but neither contains the other)",
    "EQ": "equal (exactly the same region)",
    "TPP": "tangential proper part (A is inside B and touches B's boundary)",
    "NTPP": "non-tangential proper part (A is strictly inside B, not touching B's boundary)",
    "TPPi": "has tangential proper part (B is inside A and touches A's boundary)",
    "NTPPi": "has non-tangential proper part (B is strictly inside A, not touching boundary)",
}
# qualreas canonical uppercase -> algebra base codes
_RCC8_NORM = {"DC": "DC", "EC": "EC", "PO": "PO", "EQ": "EQ", "TPP": "TPP",
              "NTPP": "NTPP", "TPPI": "TPPi", "NTPPI": "NTPPi",
              "TPPi": "TPPi", "NTPPi": "NTPPi"}


def norm_rcc8(code: str):
    return _RCC8_NORM.get(str(code).strip(), None)


# =====================================================================
# VAGUE / AMBIGUOUS TERM MAPS  (the fair lossy renderings; gold in admissible
# by construction so the soundness target is gold-in-emitted-set)
# =====================================================================
# SPATIAL: a vague preposition -> the RCC-8 base relations it is consistent with.
VAGUE_RCC8 = {
    "near":        ["DC", "EC"],
    "touching":    ["EC", "PO", "TPP", "TPPi"],
    "around":      ["TPPi", "NTPPi", "EC"],
    "inside":      ["TPP", "NTPP"],
    "overlapping": ["PO", "TPP", "TPPi"],
}
# a short natural phrase for each vague term (used in the rendered sentence)
VAGUE_PHRASE = {
    "near": "near", "touching": "touching", "around": "around",
    "inside": "inside", "overlapping": "overlapping with",
}

# KINSHIP: an informal/under-specified family term -> the base TYPES it could mean.
AMBIG_KIN = {
    "guardian":            ["inv-child", "inv-grand"],                       # parent or grandparent
    "descendant":          ["child", "grand"],                              # child or grandchild
    "family elder":        ["inv-child", "inv-grand", "inv-un"],            # parent/grandparent/aunt-uncle
    "sibling-figure":      ["sibling", "sibling-in-law"],                   # blood- or in-law sibling
    "relative by marriage": ["SO", "in-law", "inv-in-law", "sibling-in-law"],  # spouse or an in-law
    "younger relative":    ["child", "grand", "un"],                        # child/grandchild/nephew-niece
}
KIN_GLOSS = {
    "child": "A's son or daughter", "inv-child": "A's father or mother (a parent of A)",
    "SO": "A's spouse (husband or wife)", "sibling": "A's brother or sister",
    "grand": "A's grandson or granddaughter (a grandchild of A)",
    "inv-grand": "A's grandfather or grandmother (a grandparent of A)",
    "in-law": "A's son-in-law or daughter-in-law (a child-in-law of A)",
    "inv-in-law": "A's father-in-law or mother-in-law (a parent-in-law of A)",
    "sibling-in-law": "A's brother-in-law or sister-in-law",
    "un": "A's nephew or niece", "inv-un": "A's uncle or aunt",
}


def _stable_hash(*parts) -> int:
    return int(hashlib.md5("|".join(str(p) for p in parts).encode()).hexdigest(), 16)


def _assign_term(term_map: dict, gold_code, *hash_parts):
    """Deterministically assign an eligible vague/ambiguous term to an edge whose true
    relation is `gold_code` (eligible = gold in the term's admissible set)."""
    eligible = [t for t, adm in term_map.items() if gold_code in adm]
    if not eligible:
        return None
    return eligible[_stable_hash(*hash_parts) % len(eligible)]


# =====================================================================
# ROBUST FUZZY-READ PARSING  (JSON {"relations":[{"rel":CODE,"p":FLOAT},...]})
# =====================================================================
def _first_json_block(txt: str):
    for op, cl in (("{", "}"), ("[", "]")):
        start = txt.find(op)
        if start < 0:
            continue
        depth = 0
        for i in range(start, len(txt)):
            if txt[i] == op:
                depth += 1
            elif txt[i] == cl:
                depth -= 1
                if depth == 0:
                    return txt[start:i + 1]
    return None


def parse_fuzzy_read(content: str, vocab: list, syn: dict | None = None):
    """Parse an LLM fuzzy read into (S_pred:frozenset, conf:dict, raw_max_p:float|None,
    parse_fail:bool).

    * S_pred = emitted set of canonical codes (p>0, or all listed if no p field);
    * conf[code] = calibrated probability in [0,1] (uniform 1/|S| fallback if no p given);
    * raw_max_p = the MAX raw probability the model returned (None if it gave no p) --
      used for frac_conf_1p0 (memorized-recall detector);
    * empty / unparseable -> universe + parse_fail=True (SOUND but uninformative)."""
    syn = syn or {}
    canon = {v.lower(): v for v in vocab}
    universe = frozenset(vocab)
    if not content or not content.strip():
        return universe, {v: 1.0 / len(vocab) for v in vocab}, None, True
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
    items = []
    if isinstance(obj, dict):
        rels = obj.get("relations", obj.get("relation", obj.get("possible", [])))
        if isinstance(rels, dict):
            rels = [{"rel": k, "p": v} for k, v in rels.items()]
        if isinstance(rels, list):
            items = rels
    elif isinstance(obj, list):
        items = obj

    def _map(rel):
        rl = str(rel).strip().lower()
        if rl in canon:
            return canon[rl]
        if rl in syn:
            return syn[rl]
        # tolerate small variants ('tpp-i', 'tpp_i')
        rl2 = rl.replace("-", "").replace("_", "").replace(" ", "")
        for k, v in canon.items():
            if k.replace("-", "").replace("_", "") == rl2:
                return v
        for k, v in syn.items():
            if k.replace("-", "").replace("_", "").replace(" ", "") == rl2:
                return v
        return None

    conf_raw = {}
    raw_ps = []
    for it in items:
        if isinstance(it, dict):
            rel = it.get("rel", it.get("relation", it.get("r", it.get("type", it.get("label")))))
            p = it.get("p", it.get("prob", it.get("probability", it.get("confidence", None))))
        else:
            rel, p = it, None
        c = _map(rel)
        if c is None:
            continue
        if p is not None:
            try:
                p = float(p)
                raw_ps.append(p)
            except Exception:
                p = None
        conf_raw[c] = p if (p is not None) else conf_raw.get(c)

    # regex fallback over raw symbols if JSON yielded nothing
    if not conf_raw and obj is None:
        low = txt.lower()
        for v in sorted(vocab, key=len, reverse=True):
            if re.search(r"(?<![a-z])" + re.escape(v.lower()) + r"(?![a-z])", low):
                conf_raw[v] = None
    if not conf_raw:
        return universe, {v: 1.0 / len(vocab) for v in vocab}, (max(raw_ps) if raw_ps else None), True

    S = frozenset(c for c, p in conf_raw.items() if (p is None or p > 0.0))
    if not S:                                   # all p==0 -> uninformative
        S = frozenset(conf_raw.keys())
    # confidence map: clamp given p; uniform fallback when the model gave none
    any_p = any(p is not None for p in conf_raw.values())
    conf = {}
    for c in S:
        p = conf_raw.get(c)
        if p is None:
            conf[c] = (1.0 / len(S)) if any_p else (1.0 / len(S))
        else:
            conf[c] = max(0.0, min(1.0, p))
    raw_max_p = max(raw_ps) if raw_ps else None
    return S, conf, raw_max_p, False


# =====================================================================
# READ ELICITATION  (one read per distinct vague/ambiguous TERM, temp 0, cached;
# the SHA-256 cache + term-level dedup means only ~6 billed calls per setting)
# =====================================================================
def _spatial_read_item(term: str):
    legend = "; ".join(f"{k} = {v}" for k, v in RCC8_GLOSS.items())
    sys_p = (
        "You are a qualitative spatial reasoning expert. Two regions A and B can stand in "
        "exactly one of the 8 RCC-8 base relations: " + legend + ". A natural-language "
        "spatial phrase is often IMPRECISE and consistent with SEVERAL of these base "
        "relations. Given an imprecise phrase, return the COMPLETE set of RCC-8 base "
        "relations that are POSSIBLE, each with a CALIBRATED probability in [0,1] reflecting "
        "how likely it is the TRUE relation (probabilities need NOT sum to 1; do not force a "
        "single answer when the phrase is genuinely ambiguous). Output ONLY JSON "
        '{"relations":[{"rel":CODE,"p":FLOAT}, ...]} using the exact codes above.')
    usr = (f'Two regions A and B are described only as: "A is {VAGUE_PHRASE[term]} B." '
           "This phrasing is imprecise. List every RCC-8 base relation that is possible "
           "between A and B, each with a calibrated probability.")
    return {"id": f"spatial::{term}", "system": sys_p, "user": usr, "max_tokens": 320}


def _kin_read_item(term: str):
    legend = "; ".join(f"{k} = {v}" for k, v in KIN_GLOSS.items())
    sys_p = (
        "You are a kinship-relation reasoning expert. The allowed SPECIFIC relation TYPES "
        "(B's relation to A) are: " + legend + ". An informal or under-specified family "
        "term can map to SEVERAL of these specific types. Given such a term, return EVERY "
        "specific relation TYPE that B could be to A, each with a CALIBRATED probability in "
        "[0,1] (probabilities need NOT sum to 1; do not force a single answer when the term "
        "is genuinely ambiguous). Output ONLY JSON "
        '{"relations":[{"rel":TYPE,"p":FLOAT}, ...]} using the exact type codes above.')
    usr = (f'B is A\'s "{term}". This term is informal and under-specified. List every '
           "specific kinship relation type B could be to A, each with a calibrated probability.")
    return {"id": f"kin::{term}", "system": sys_p, "user": usr, "max_tokens": 320}


# kinship synonym net (model may answer with words instead of type codes)
KIN_SYN = {
    "parent": "inv-child", "father": "inv-child", "mother": "inv-child",
    "son": "child", "daughter": "child", "kid": "child",
    "grandparent": "inv-grand", "grandfather": "inv-grand", "grandmother": "inv-grand",
    "grandchild": "grand", "grandson": "grand", "granddaughter": "grand",
    "spouse": "SO", "husband": "SO", "wife": "SO", "partner": "SO",
    "brother": "sibling", "sister": "sibling",
    "uncle": "inv-un", "aunt": "inv-un", "nephew": "un", "niece": "un",
    "child-in-law": "in-law", "son-in-law": "in-law", "daughter-in-law": "in-law",
    "parent-in-law": "inv-in-law", "father-in-law": "inv-in-law", "mother-in-law": "inv-in-law",
    "sibling in law": "sibling-in-law", "brother-in-law": "sibling-in-law",
    "sister-in-law": "sibling-in-law",
}


def adm_read(adm: list):
    """Symbolic stand-in read (--no-llm): the admissible set itself with uniform p."""
    S = frozenset(adm)
    return {"S_pred": S, "conf": {c: 1.0 / len(S) for c in S}, "raw_max_p": None,
            "parse_fail": False, "content": "ADM(no-llm)"}


def elicit_reads(client, term_map: dict, setting: str, no_llm: bool, vocab: list,
                 syn: dict | None = None) -> dict:
    """Return {term: read} where read = {S_pred, conf, raw_max_p, parse_fail, content}."""
    if no_llm:
        return {t: adm_read(adm) for t, adm in term_map.items()}
    builder = _spatial_read_item if setting == "spatial" else _kin_read_item
    items = [builder(t) for t in term_map]
    res = asyncio.run(client.run_batch(items))
    reads = {}
    for t in term_map:
        payload = res.get(f"{setting}::{t}", {"content": ""})
        S, conf, raw_max_p, pf = parse_fuzzy_read(payload.get("content", ""), vocab, syn)
        if pf:
            client.n_parse_fail += 1
        reads[t] = {"S_pred": S, "conf": conf, "raw_max_p": raw_max_p,
                    "parse_fail": pf, "content": (payload.get("content") or "")[:600]}
        logger.info(f"[read] {setting}:{t:>20s} -> {sorted(S)}  "
                    f"max_p={raw_max_p}  parse_fail={pf}")
    return reads


# =====================================================================
# CALIBRATION  (ECE + reliability diagram; two views per the plan)
# =====================================================================
def compute_ece(pairs, n_bins: int = 10):
    """pairs: list of (confidence, correct{0,1}).  Returns (ece, reliability_points, n)."""
    pairs = [(float(c), float(y)) for c, y in pairs if c is not None]
    n = len(pairs)
    if n == 0:
        return None, [], 0
    bins = [[] for _ in range(n_bins)]
    for c, y in pairs:
        idx = min(n_bins - 1, max(0, int(c * n_bins)))
        bins[idx].append((c, y))
    ece = 0.0
    rel = []
    for bi, b in enumerate(bins):
        lo, hi = bi / n_bins, (bi + 1) / n_bins
        if not b:
            rel.append({"bin_lo": lo, "bin_hi": hi, "mean_conf": None,
                        "mean_acc": None, "count": 0})
            continue
        mc = float(np.mean([c for c, _ in b]))
        ma = float(np.mean([y for _, y in b]))
        ece += (len(b) / n) * abs(ma - mc)
        rel.append({"bin_lo": lo, "bin_hi": hi, "mean_conf": mc, "mean_acc": ma,
                    "count": len(b)})
    return float(ece), rel, n


def score_reads(edge_records, vocab):
    """edge_records: [{gold, term, S_pred, conf, raw_max_p, parse_fail, doc_id}].
    Returns the calibration block + per-edge scored rows (for clustering/bootstrap)."""
    universe = frozenset(vocab)
    cand_pairs = []     # view (a): per (edge, candidate) -> (p(rel), rel==gold)
    top1_pairs = []     # view (b): per edge -> (top1_conf, top1==gold)
    scored = []
    for r in edge_records:
        gold = r["gold"]
        S = r["S_pred"]
        conf = r["conf"]
        sound = gold in S
        breadth = len(S)
        over_u = (S == universe)
        # top-1 (argmax p); ties broken by canonical order
        if conf:
            top1 = max(sorted(S, key=lambda c: vocab.index(c)), key=lambda c: conf.get(c, 0.0))
            top1_conf = conf.get(top1, 0.0)
        else:
            top1, top1_conf = None, 0.0
        top1_correct = (top1 == gold)
        for c in S:
            cand_pairs.append((conf.get(c, 0.0), 1.0 if c == gold else 0.0))
        if top1 is not None:
            top1_pairs.append((top1_conf, 1.0 if top1_correct else 0.0))
        scored.append({**r, "sound": sound, "breadth": breadth, "over_universe": over_u,
                       "top1": top1, "top1_conf": top1_conf, "top1_correct": top1_correct,
                       "conf_at_1p0": (r["raw_max_p"] == 1.0)})
    ece_cand, rel_cand, n_cand = compute_ece(cand_pairs)
    ece_top1, rel_top1, n_top1 = compute_ece(top1_pairs)
    n = len(scored)
    block = {
        "n_reads": n,
        "soundness_rate": float(np.mean([s["sound"] for s in scored])) if n else None,
        "mean_breadth": float(np.mean([s["breadth"] for s in scored])) if n else None,
        "frac_over_universe": float(np.mean([s["over_universe"] for s in scored])) if n else None,
        "frac_at_conf_1p0": float(np.mean([1.0 if s["conf_at_1p0"] else 0.0 for s in scored])) if n else None,
        "mean_top1_conf": float(np.mean([s["top1_conf"] for s in scored])) if n else None,
        "top1_accuracy": float(np.mean([s["top1_correct"] for s in scored])) if n else None,
        "n_parse_fail": int(sum(1 for s in scored if s["parse_fail"])),
        "ECE_per_candidate": ece_cand, "n_candidate_pairs": n_cand,
        "reliability_per_candidate": rel_cand,
        "ECE_top1": ece_top1, "n_top1": n_top1, "reliability_top1": rel_top1,
    }
    return block, scored


# =====================================================================
# SETTING 1 : SPATIAL  -- load, per-edge reads, certificate closure
# =====================================================================
def load_spatial(mini: bool = False):
    """Load SpaRP-PS1 rows; build per-scene directed RCC-8 sub-graph + query metadata."""
    path = SPATIAL_MINI if mini else SPATIAL_FULL
    d = json.loads(Path(path).read_text())
    ds = [x for x in d["datasets"] if x["dataset"] == "SpaRP-PS1"]
    if not ds:
        raise ValueError("SpaRP-PS1 not present in spatial dataset")
    rows = []
    A = load_algebras()["rcc8"]
    for ex in ds[0]["examples"]:
        out = json.loads(ex["output"])
        adj = defaultdict(dict)     # u -> {v: code}  (directed, with converses)
        stated = []                 # [(u,v,code)] non-root single-canonical rcc8 edges
        for e in out["edges"]:
            if e.get("is_root_edge"):
                continue
            if e.get("algebra") != "rcc8":
                continue
            canon = e.get("canonical") or []
            if len(canon) != 1:
                continue
            code = norm_rcc8(canon[0])
            if code is None:
                continue
            u, v = e["src"], e["dst"]
            if u == "-1" or v == "-1":
                continue
            stated.append((u, v, code))
            adj[u][v] = code
            adj[v].setdefault(u, A.conv(code))   # do not overwrite a stated converse
        q = out["query_edge"]
        gold = norm_rcc8((q.get("gold_canonical") or [None])[0]) if q.get("gold_canonical") else None
        rows.append({
            "doc_id": ex["metadata_doc_id"], "input": ex["input"],
            "adj": {u: dict(d2) for u, d2 in adj.items()}, "stated": stated,
            "qsrc": q["src"], "qdst": q["dst"], "gold": gold,
            "gold_algebra": q.get("gold_algebra"),
            "deduction_required": bool(q.get("deduction_required")),
            "multipath_bite": bool(q.get("genuine_multipath_with_bite")),
            "multipath_bite_tight": bool(q.get("genuine_multipath_with_bite_tight")),
            "hop_length": q.get("hop_length"),
            "num_edge_disjoint_paths": q.get("num_edge_disjoint_paths"),
        })
    logger.info(f"[spatial] loaded {len(rows)} SpaRP-PS1 rows")
    return rows, A


def rcc8_simple_paths(adj: dict, src, dst, max_len: int = 4, max_paths: int = 8):
    """Up to `max_paths` simple directed paths src..dst (<= max_len edges) over the RCC-8
    sub-graph. Returns lists of edge tuples [(u,v,code), ...], shortest first."""
    if src not in adj or dst not in adj:
        return []
    out = []
    stack = [(src, [src], [])]
    while stack and len(out) < max_paths * 6:
        node, nodes_on, edges_on = stack.pop()
        if len(edges_on) > max_len:
            continue
        for nb, code in sorted(adj.get(node, {}).items()):
            if nb == dst:
                out.append(edges_on + [(node, nb, code)])
            elif nb not in nodes_on and len(edges_on) + 1 < max_len:
                stack.append((nb, nodes_on + [nb], edges_on + [(node, nb, code)]))
    out.sort(key=len)
    seen, uniq = set(), []
    for p in out:
        k = tuple((u, v) for u, v, _ in p)
        if k not in seen:
            seen.add(k)
            uniq.append(p)
    return uniq[:max_paths]


def compose_path_sets(A, set_list):
    """Iterated composition of a sequence of disjunctive labels (frozensets)."""
    if not set_list:
        return frozenset([A.identity])
    acc = frozenset(set_list[0])
    for s in set_list[1:]:
        acc = A.compose_sets(acc, s)
        if acc == A.universe:
            break
    return acc


def _representative(A, s):
    """Deterministic singleton representative of a set, in canonical algebra order."""
    for r in A.base:
        if r in s:
            return r
    return None


def spatial_collect_edges(rows, A, cap: int | None):
    """Per-edge calibration records: sample renderable stated RCC-8 edges, stratified by
    gold code, assign a vague term, attach (filled later by the term read)."""
    by_code = defaultdict(list)
    for row in rows:
        seen = set()
        for (u, v, code) in row["stated"]:
            if (u, v) in seen:
                continue
            seen.add((u, v))
            term = _assign_term(VAGUE_RCC8, code, row["doc_id"], u, v)
            if term is None:
                continue
            by_code[code].append({"doc_id": row["doc_id"], "src": u, "dst": v,
                                  "gold": code, "term": term})
    # stratified, round-robin across codes, deterministic
    for c in by_code:
        by_code[c].sort(key=lambda r: (r["doc_id"], r["src"], r["dst"]))
    edges = []
    codes = sorted(by_code)
    idx = {c: 0 for c in codes}
    remaining = sum(len(v) for v in by_code.values())
    while remaining > 0 and (cap is None or len(edges) < cap):
        progressed = False
        for c in codes:
            if idx[c] < len(by_code[c]):
                edges.append(by_code[c][idx[c]])
                idx[c] += 1
                remaining -= 1
                progressed = True
                if cap is not None and len(edges) >= cap:
                    break
        if not progressed:
            break
    return edges


def spatial_certificate_pool(rows, A, reads, cap: int | None):
    """End-to-end certificate-bounded closure on deduction-required RCC-8 queries.
    Returns (pool_records, kept, dropped_cross_algebra, n_multipath)."""
    pool = []
    dropped = 0
    n_multi = 0
    cand = [r for r in rows if r["deduction_required"] and r["gold_algebra"] == "rcc8"
            and r["gold"] is not None]
    cand.sort(key=lambda r: r["doc_id"])
    for row in cand:
        if cap is not None and len(pool) >= cap:
            break
        paths = rcc8_simple_paths(row["adj"], row["qsrc"], row["qdst"], max_len=4, max_paths=8)
        paths = [p for p in paths if len(p) >= 2 or len(paths) == 1]  # need composition
        paths = [p for p in paths if len(p) >= 2]                      # at least one 2+ edge path
        if not paths:
            dropped += 1
            continue
        # choose ONE renderable fuzzy edge per path (deterministic), attach its term read
        fuzzy_choice = {}
        ok = True
        for pi, path in enumerate(paths):
            renderable = [j for j, (u, v, code) in enumerate(path)
                          if _assign_term(VAGUE_RCC8, code, row["doc_id"], u, v, pi) is not None]
            if not renderable:
                ok = False
                break
            j = renderable[_stable_hash(row["doc_id"], row["qsrc"], row["qdst"], pi) % len(renderable)]
            u, v, code = path[j]
            term = _assign_term(VAGUE_RCC8, code, row["doc_id"], u, v, pi)
            fuzzy_choice[pi] = (j, term, code)
        if not ok:
            dropped += 1
            continue
        if len(paths) >= 2:
            n_multi += 1

        # ---- certificate (sound disjunction) ----
        inter = A.universe
        all_sound = True
        fuzzy_used = []
        per_path_sets = []
        for pi, path in enumerate(paths):
            j, term, code = fuzzy_choice[pi]
            S_read = reads[term]["S_pred"]
            if code not in S_read:
                all_sound = False
            fuzzy_used.append({"path": pi, "edge": [path[j][0], path[j][1]], "term": term,
                               "gold_code": code, "emitted": sorted(S_read),
                               "sound": code in S_read})
            set_list = [frozenset(S_read) if k == j else frozenset([c])
                        for k, (uu, vv, c) in enumerate(path)]
            comp = compose_path_sets(A, set_list)
            per_path_sets.append(comp)
            inter = inter & comp
        Dq = inter
        if len(Dq) == 1:
            cert_decision = "COMMIT"
            cert_pred = _representative(A, Dq)
        elif len(Dq) == 0:
            cert_decision = "COLLAPSE"
            cert_pred = None
        else:
            cert_decision = "ABSTAIN"
            cert_pred = None
        cert_correct = (cert_decision == "COMMIT" and cert_pred == row["gold"])

        # ---- commit_argmax (ignore disjunction: point estimate, always answer) ----
        inter_a = A.universe
        for pi, path in enumerate(paths):
            j, term, code = fuzzy_choice[pi]
            conf = reads[term]["conf"]
            S_read = reads[term]["S_pred"]
            top1 = max(sorted(S_read, key=lambda c: A.base.index(c)),
                       key=lambda c: conf.get(c, 0.0)) if S_read else code
            set_list = [frozenset([top1]) if k == j else frozenset([c])
                        for k, (uu, vv, c) in enumerate(path)]
            inter_a = inter_a & compose_path_sets(A, set_list)
        if inter_a:
            argmax_pred = _representative(A, inter_a)
        else:
            # contradiction under the point estimate: still forced to answer
            uni = frozenset().union(*per_path_sets) if per_path_sets else A.universe
            argmax_pred = _representative(A, uni) or row["gold"]
        argmax_correct = (argmax_pred == row["gold"])

        pool.append({
            "doc_id": row["doc_id"], "qsrc": row["qsrc"], "qdst": row["qdst"],
            "gold": row["gold"], "n_paths": len(paths),
            "multipath": len(paths) >= 2, "multipath_bite_tight": row["multipath_bite_tight"],
            "hop_length": row["hop_length"], "all_reads_sound": all_sound,
            "fuzzy_used": fuzzy_used, "Dquery": sorted(Dq),
            "cert_decision": cert_decision, "cert_pred": cert_pred, "cert_correct": cert_correct,
            "argmax_pred": argmax_pred, "argmax_correct": argmax_correct,
            "paths": [[[u, v, c] for (u, v, c) in p] for p in paths],
        })
    return pool, len(pool), dropped, n_multi


# =====================================================================
# SETTING 2 : KINSHIP  -- disjunctive-seed forward closure
# =====================================================================
def _atomics_to_edges(atomic_facts):
    return [{"a": f["source_name"], "b": f["target_name"], "type": f["relation_type"]}
            for f in atomic_facts]


def seeded_forward_closure(kin: Kinship, seed_pairs):
    """Forward least-fixpoint UNION derivation with DISJUNCTIVE seeds.
    seed_pairs: list of (a, b, typeset).  Identical fixpoint to kinship.forward_closure
    but every directed pair may be seeded with a SET of types (singletons except the one
    fuzzy edge, which is seeded with the LLM's emitted disjunction)."""
    from collections import deque
    D = defaultdict(set)
    nbrs = defaultdict(set)

    def add(a, b, t):
        if t not in D[(a, b)]:
            D[(a, b)].add(t)
            nbrs[a].add(b)

    for (a, b, ts) in seed_pairs:
        if a == b:
            continue
        for t in ts:
            if t not in kin.base:
                continue
            add(a, b, t)
            add(b, a, kin.conv_type(t))
    Q = deque(D.keys())
    inq = set(D.keys())

    def push(p):
        if p not in inq:
            inq.add(p)
            Q.append(p)

    def emit(a, c, t3):
        grew = False
        if t3 not in D[(a, c)]:
            D[(a, c)].add(t3)
            nbrs[a].add(c)
            grew = True
        ct3 = kin.conv_type(t3)
        if ct3 not in D[(c, a)]:
            D[(c, a)].add(ct3)
            nbrs[c].add(a)
        if grew:
            push((a, c))
            push((c, a))

    while Q:
        (a, b) = Q.popleft()
        inq.discard((a, b))
        tab = list(D[(a, b)])
        for c in list(nbrs[b]):
            if c == a:
                continue
            for t1 in tab:
                for t2 in list(D[(b, c)]):
                    t3 = kin.compose_types(t1, t2)
                    if t3 is not None:
                        emit(a, c, t3)
        for z in list(nbrs[a]):
            if z == b:
                continue
            for t1 in list(D[(z, a)]):
                for t2 in tab:
                    t3 = kin.compose_types(t1, t2)
                    if t3 is not None:
                        emit(z, b, t3)
    return D


def kin_collect_edges(gen_rows, kin, cap: int | None):
    """Per-edge calibration records over CLUTRR atomic facts: renderable atomic edges
    (true type in some ambiguous term's admissible set), one record per (doc, edge)."""
    by_type = defaultdict(list)
    for ex in gen_rows:
        if ex["metadata_noise_type"] != "none":
            continue
        for f in ex["metadata_atomic_facts"]:
            t = f["relation_type"]
            term = _assign_term(AMBIG_KIN, t, ex["metadata_doc_id"], f["source_name"], f["target_name"])
            if term is None:
                continue
            by_type[t].append({"doc_id": ex["metadata_doc_id"], "src": f["source_name"],
                               "dst": f["target_name"], "gold": t, "term": term})
    for t in by_type:
        by_type[t].sort(key=lambda r: (r["doc_id"], r["src"], r["dst"]))
    edges, types = [], sorted(by_type)
    idx = {t: 0 for t in types}
    remaining = sum(len(v) for v in by_type.values())
    while remaining > 0 and (cap is None or len(edges) < cap):
        progressed = False
        for t in types:
            if idx[t] < len(by_type[t]):
                edges.append(by_type[t][idx[t]])
                idx[t] += 1
                remaining -= 1
                progressed = True
                if cap is not None and len(edges) >= cap:
                    break
        if not progressed:
            break
    return edges


def kin_certificate_pool(gen_rows, kin, reads, cap: int | None):
    """End-to-end disjunctive-seed closure on clean multi-hop kinship queries."""
    pool = []
    dropped_unclean = 0
    rows = [e for e in gen_rows if e["metadata_noise_type"] == "none"
            and e["metadata_fold"] == "test" and e["metadata_hop_count"] >= 2]
    rows.sort(key=lambda e: e["metadata_doc_id"])
    for ex in rows:
        if cap is not None and len(pool) >= cap:
            break
        q = ex["metadata_query"]
        qsrc, qtgt = q["source_name"], q["target_name"]
        gold_surface = q["relation"]
        gtgt = ex["metadata_genders"].get(qtgt, "male")
        edges = _atomics_to_edges(ex["metadata_atomic_facts"])
        # gold-clean gate: singleton-closure must recover gold (excludes table artifacts)
        base = query_modeA(kin, edges, qsrc, qtgt)
        if not base["singleton"]:
            dropped_unclean += 1
            continue
        gold_type = base["answer_type"]
        if kin.surface(gold_type, gtgt) != gold_surface:
            dropped_unclean += 1
            continue
        # pick ONE renderable atomic edge on the chain
        renderable = [(i, e) for i, e in enumerate(edges)
                      if _assign_term(AMBIG_KIN, e["type"], ex["metadata_doc_id"], e["a"], e["b"]) is not None]
        if not renderable:
            continue
        fi, fe = renderable[_stable_hash(ex["metadata_doc_id"], qsrc, qtgt) % len(renderable)]
        term = _assign_term(AMBIG_KIN, fe["type"], ex["metadata_doc_id"], fe["a"], fe["b"])
        edge_gold = fe["type"]
        S_read = reads[term]["S_pred"]
        sound = edge_gold in S_read

        # ---- certificate (disjunctive seed) ----
        seed = []
        for i, e in enumerate(edges):
            ts = S_read if i == fi else frozenset([e["type"]])
            seed.append((e["a"], e["b"], ts))
        D = seeded_forward_closure(kin, seed)
        Dq = D.get((qsrc, qtgt), set())
        if len(Dq) == 1:
            cert_decision = "COMMIT"
            ctype = next(iter(Dq))
            cert_pred = kin.surface(ctype, gtgt)
        elif len(Dq) == 0:
            cert_decision = "COLLAPSE"
            cert_pred = None
        else:
            cert_decision = "ABSTAIN"
            cert_pred = None
        cert_correct = (cert_decision == "COMMIT" and cert_pred == gold_surface)

        # ---- commit_argmax (point estimate, always answer) ----
        conf = reads[term]["conf"]
        top1 = max(sorted(S_read, key=lambda c: kin.base.index(c)),
                   key=lambda c: conf.get(c, 0.0)) if S_read else edge_gold
        seed_a = [(e["a"], e["b"], (frozenset([top1]) if i == fi else frozenset([e["type"]])))
                  for i, e in enumerate(edges)]
        Da = seeded_forward_closure(kin, seed_a).get((qsrc, qtgt), set())
        if Da:
            atype = sorted(Da, key=lambda t: kin.base.index(t))[0]
            argmax_pred = kin.surface(atype, gtgt)
        else:
            argmax_pred = kin.surface(top1, gtgt)     # forced to answer
        argmax_correct = (argmax_pred == gold_surface)

        pool.append({
            "doc_id": ex["metadata_doc_id"], "qsrc": qsrc, "qtgt": qtgt,
            "gold": gold_surface, "gold_type": gold_type, "hop": ex["metadata_hop_count"],
            "fuzzy_edge": [fe["a"], fe["b"]], "fuzzy_term": term, "fuzzy_gold_type": edge_gold,
            "emitted": sorted(S_read), "all_reads_sound": sound,
            "Dquery": sorted(Dq), "cert_decision": cert_decision, "cert_pred": cert_pred,
            "cert_correct": cert_correct, "argmax_pred": argmax_pred,
            "argmax_correct": argmax_correct, "story": ex["input"], "_edges": edges,
        })
    logger.info(f"[kin] certificate pool={len(pool)} dropped_unclean={dropped_unclean}")
    return pool, dropped_unclean


# =====================================================================
# RISK-COVERAGE METRICS  (certificate vs commit_argmax vs abstain_always)
# =====================================================================
def risk_coverage(pool):
    """Three methods on the SAME pool. Output contract decisions already attached."""
    n = len(pool)
    if n == 0:
        return {"n_pool": 0}

    def _summ(decisions, preds, corrects):
        committed = [i for i in range(n) if decisions[i] == "COMMIT"]
        wrong = [i for i in committed if not corrects[i]]
        cov = len(committed) / n
        acc = (sum(corrects[i] for i in committed) / len(committed)) if committed else None
        return {"coverage": cov, "n_committed": len(committed),
                "acc_among_answered": acc, "confident_wrong_rate": len(wrong) / n,
                "n_confident_wrong": len(wrong)}

    cert = _summ([p["cert_decision"] for p in pool],
                 [p["cert_pred"] for p in pool], [p["cert_correct"] for p in pool])
    # commit_argmax ALWAYS commits (coverage 1.0)
    argmax = {"coverage": 1.0, "n_committed": n,
              "acc_among_answered": float(np.mean([p["argmax_correct"] for p in pool])),
              "confident_wrong_rate": float(np.mean([0.0 if p["argmax_correct"] else 1.0 for p in pool])),
              "n_confident_wrong": int(sum(0 if p["argmax_correct"] else 1 for p in pool))}
    abstain = {"coverage": 0.0, "n_committed": 0, "acc_among_answered": None,
               "confident_wrong_rate": 0.0, "n_confident_wrong": 0}

    # certificate_caught_fraction: of UNSOUND-read queries, frac NOT confidently-wrong
    unsound = [p for p in pool if not p["all_reads_sound"]]
    cert_wrong_unsound = [p for p in unsound if p["cert_decision"] == "COMMIT" and not p["cert_correct"]]
    caught = [p for p in unsound if not (p["cert_decision"] == "COMMIT" and not p["cert_correct"])]
    collapse_or_abstain = [p for p in unsound if p["cert_decision"] in ("COLLAPSE", "ABSTAIN")]
    # ZERO-FP CHECK: on the all-sound subset the certificate must never be confident-wrong
    sound_pool = [p for p in pool if p["all_reads_sound"]]
    zero_fp_viol = [p for p in sound_pool if p["cert_decision"] == "COMMIT" and not p["cert_correct"]]

    return {
        "n_pool": n,
        "certificate": cert, "commit_argmax": argmax, "abstain_always": abstain,
        "recovered_coverage_cert_vs_abstain": cert["coverage"],
        "confident_wrong_reduction_cert_vs_argmax":
            argmax["confident_wrong_rate"] - cert["confident_wrong_rate"],
        "n_unsound_reads": len(unsound),
        "n_silent_wrong_missed_by_cert": len(cert_wrong_unsound),
        "certificate_caught_fraction": (len(caught) / len(unsound)) if unsound else None,
        "unsound_collapse_or_abstain_fraction":
            (len(collapse_or_abstain) / len(unsound)) if unsound else None,
        "n_sound_reads": len(sound_pool),
        "zero_fp_holds": (len(zero_fp_viol) == 0),
        "n_zero_fp_violations": len(zero_fp_viol),
        "cert_decision_breakdown": {
            d: sum(1 for p in pool if p["cert_decision"] == d)
            for d in ("COMMIT", "ABSTAIN", "COLLAPSE")},
    }


# =====================================================================
# STAGE 4 : CALIBRATION CONTRAST vs MEMORIZED MODE-P
# =====================================================================
def calibration_contrast(spatial_cal, kin_cal):
    block = {"note": (
        "Mode-P (iter-4) was MEMORIZED-CALCULUS atomic-rule recall: the LLM was asked to "
        "compose two EXACT kinship cells, which it knows by heart (16/16 cells correct at "
        "confidence EXACTLY 1.0). That is table recall, NOT fuzzy unification. THIS "
        "experiment is the genuine fuzzy case: vague/ambiguous reads with no single answer, "
        "where the LLM emits calibrated sub-1.0 disjunctions.")}
    try:
        prior = json.loads(MODEP_PRIOR.read_text())
        pc = (prior.get("metadata", {}).get("llm_resolved_step_accuracy", {})
              .get("mode_P", {}).get("per_cell", {}))
        confs = [v.get("confidence") for v in pc.values() if v.get("confidence") is not None]
        if confs:
            block["modeP_memorized"] = {
                "n": len(confs),
                "frac_conf_1p0": float(np.mean([1.0 if c == 1.0 else 0.0 for c in confs])),
                "mean_conf": float(np.mean(confs)),
                "exact_match_acc": prior["metadata"]["llm_resolved_step_accuracy"]["mode_P"].get("exact_match_acc"),
                "source": str(MODEP_PRIOR),
            }
    except Exception as e:
        logger.warning(f"could not load Mode-P prior: {e}")
        block["modeP_memorized"] = {"error": str(e)}
    if spatial_cal:
        block["setting1_spatial_fuzzy"] = {
            "n": spatial_cal["n_reads"], "frac_conf_1p0": spatial_cal["frac_at_conf_1p0"],
            "mean_top1_conf": spatial_cal["mean_top1_conf"],
            "ECE_per_candidate": spatial_cal["ECE_per_candidate"],
            "ECE_top1": spatial_cal["ECE_top1"], "soundness_rate": spatial_cal["soundness_rate"]}
    if kin_cal:
        block["setting2_kinship_fuzzy"] = {
            "n": kin_cal["n_reads"], "frac_conf_1p0": kin_cal["frac_at_conf_1p0"],
            "mean_top1_conf": kin_cal["mean_top1_conf"],
            "ECE_per_candidate": kin_cal["ECE_per_candidate"],
            "ECE_top1": kin_cal["ECE_top1"], "soundness_rate": kin_cal["soundness_rate"]}
    return block


# =====================================================================
# STAGE 6 : FLAGGED TRACE-GRAPHS
# =====================================================================
def spatial_traces(pool, A, n=6):
    """Worked spatial traces: each path's composition tagged exact_table vs llm_fuzzy."""
    traces = []
    # ensure >=1 unsound-caught example is included
    unsound = [p for p in pool if not p["all_reads_sound"]]
    ordered = unsound[:2] + [p for p in pool if p["all_reads_sound"]]
    for p in ordered[:n]:
        steps = []
        for pi, path in enumerate(p["paths"]):
            fu = next((f for f in p["fuzzy_used"] if f["path"] == pi), None)
            fuzzy_edge = tuple(fu["edge"]) if fu else None
            for (u, v, c) in path:
                is_fuzzy = (fuzzy_edge == (u, v))
                step = {"path": pi, "src": u, "dst": v,
                        "source": "llm_fuzzy" if is_fuzzy else "exact_table",
                        "exact_relation": c}
                if is_fuzzy:
                    step["vague_term"] = fu["term"]
                    step["emitted_disjunction"] = fu["emitted"]
                    step["gold_retained"] = fu["sound"]
                steps.append(step)
        traces.append({
            "setting": "spatial", "doc_id": p["doc_id"], "query": [p["qsrc"], p["qdst"]],
            "gold": p["gold"], "n_paths": p["n_paths"], "Dquery": p["Dquery"],
            "all_reads_sound": p["all_reads_sound"], "certificate_decision": p["cert_decision"],
            "certificate_answer": p["cert_pred"], "correct": p["cert_correct"],
            "commit_argmax_answer": p["argmax_pred"], "trace": steps,
            "caught_unsound": (not p["all_reads_sound"]
                               and p["cert_decision"] in ("COLLAPSE", "ABSTAIN")),
            "silent_wrong_missed": (not p["all_reads_sound"]
                                    and p["cert_decision"] == "COMMIT" and not p["cert_correct"]),
        })
    return traces


def kin_traces(pool, kin, n=6):
    """Worked kinship traces: derivation steps tagged exact_table vs llm_fuzzy."""
    traces = []
    unsound = [p for p in pool if not p["all_reads_sound"]]
    ordered = unsound[:2] + [p for p in pool if p["all_reads_sound"]]
    seen = set()
    for p in ordered:
        if p["doc_id"] in seen:
            continue
        seen.add(p["doc_id"])
        if len(traces) >= n:
            break
        edges = p["_edges"]
        fe = tuple(p["fuzzy_edge"])
        # show the singleton-seed gold derivation (the proof skeleton) for auditability
        steps = []
        for st in derivation_trace(kin, edges, p["qsrc"], p["qtgt"]):
            src_is_fuzzy = ((st["a"], st["b"]) == fe or (st["b"], st["a"]) == fe)
            steps.append({"a": st["a"], "b": st["b"], "c": st["c"], "t1": st["t1"],
                          "t2": st["t2"], "t3": st["t3"],
                          "source": "llm_fuzzy" if src_is_fuzzy else "exact_table"})
        traces.append({
            "setting": "kinship", "doc_id": p["doc_id"], "query": [p["qsrc"], p["qtgt"]],
            "gold": p["gold"], "fuzzy_edge": p["fuzzy_edge"], "vague_term": p["fuzzy_term"],
            "emitted_disjunction": p["emitted"], "gold_type_retained": p["all_reads_sound"],
            "Dquery": p["Dquery"], "certificate_decision": p["cert_decision"],
            "certificate_answer": p["cert_pred"], "correct": p["cert_correct"],
            "commit_argmax_answer": p["argmax_pred"], "story": p["story"][:900],
            "proof_skeleton": steps,
            "caught_unsound": (not p["all_reads_sound"]
                               and p["cert_decision"] in ("COLLAPSE", "ABSTAIN")),
            "silent_wrong_missed": (not p["all_reads_sound"]
                                    and p["cert_decision"] == "COMMIT" and not p["cert_correct"]),
        })
    return traces


# =====================================================================
# STAGE 7 : bootstrap CIs (doc-clustered)
# =====================================================================
def _doc_vals(scored, key_doc, val_fn):
    d = defaultdict(list)
    for r in scored:
        d[r[key_doc]].append(1.0 if val_fn(r) else 0.0)
    return d


def paired_diff_ci(pool, fn_a, fn_b, B=2000, seed=SEED, alpha=0.05):
    """Doc-clustered paired bootstrap CI for mean(fn_a) - mean(fn_b) over the pool."""
    if not pool:
        return {"diff": None, "ci95": [None, None], "n": 0}
    by_doc = defaultdict(list)
    for p in pool:
        by_doc[p["doc_id"]].append((1.0 if fn_a(p) else 0.0, 1.0 if fn_b(p) else 0.0))
    docs = list(by_doc)
    rng = np.random.default_rng(seed)
    a_all = np.array([x for d in docs for x, _ in by_doc[d]])
    b_all = np.array([y for d in docs for _, y in by_doc[d]])
    point = float(a_all.mean() - b_all.mean())
    diffs = []
    nd = len(docs)
    for _ in range(B):
        pick = rng.integers(0, nd, nd)
        a = np.concatenate([[x for x, _ in by_doc[docs[i]]] for i in pick])
        b = np.concatenate([[y for _, y in by_doc[docs[i]]] for i in pick])
        diffs.append(a.mean() - b.mean())
    lo, hi = np.quantile(diffs, [alpha / 2, 1 - alpha / 2])
    return {"diff": point, "ci95": [float(lo), float(hi)], "n": len(a_all), "n_docs": nd}


# =====================================================================
# SYMBOLIC SELF-TESTS  (T1/T2; $0)
# =====================================================================
def run_symbolic_tests(rows, A, kin, gen_rows):
    """T1: spatial 2-hop exact path composition contains gold; kinship gold-clean chains
    recover gold. T2: disjunctive seed contains gold (zero-FP) and an unsound seed never
    yields a falsely-correct singleton."""
    report = {}
    # T1a spatial: exact path composition must be SOUND (contain gold) on dedR rcc8 queries
    n = n_ok = 0
    for row in rows:
        if not (row["deduction_required"] and row["gold_algebra"] == "rcc8" and row["gold"]):
            continue
        paths = rcc8_simple_paths(row["adj"], row["qsrc"], row["qdst"], max_len=4)
        paths = [p for p in paths if len(p) >= 2]
        if not paths:
            continue
        inter = A.universe
        for path in paths:
            inter = inter & compose_path_sets(A, [frozenset([c]) for (_, _, c) in path])
        n += 1
        if row["gold"] in inter:
            n_ok += 1
        if n >= 200:
            break
    report["T1a_spatial_exact_path_soundness"] = {"n": n, "sound": n_ok,
                                                  "rate": (n_ok / n if n else None)}
    assert n == 0 or n_ok / n >= 0.95, f"spatial exact-path soundness too low: {n_ok}/{n}"

    # T1b kinship: gold-clean chains recover gold singleton
    n = n_ok = 0
    for ex in gen_rows:
        if ex["metadata_noise_type"] != "none" or ex["metadata_hop_count"] < 2:
            continue
        q = ex["metadata_query"]
        edges = _atomics_to_edges(ex["metadata_atomic_facts"])
        res = query_modeA(kin, edges, q["source_name"], q["target_name"])
        if res["singleton"]:
            n += 1
            gt = ex["metadata_genders"].get(q["target_name"], "male")
            if kin.surface(res["answer_type"], gt) == q["relation"]:
                n_ok += 1
        if n >= 200:
            break
    report["T1b_kinship_goldclean_recovery"] = {"n": n, "correct": n_ok,
                                               "rate": (n_ok / n if n else None)}
    assert n == 0 or n_ok / n >= 0.95, f"kinship gold-clean recovery too low: {n_ok}/{n}"

    # T2 disjunctive seed unit test (kinship): pick a clean 2-hop chain
    sample = None
    for ex in gen_rows:
        if ex["metadata_noise_type"] == "none" and ex["metadata_hop_count"] == 2:
            edges = _atomics_to_edges(ex["metadata_atomic_facts"])
            q = ex["metadata_query"]
            r = query_modeA(kin, edges, q["source_name"], q["target_name"])
            if r["singleton"] and len(edges) == 2:
                sample = (ex, edges, q, r["answer_type"])
                break
    if sample:
        ex, edges, q, gold_t = sample
        e0 = edges[0]
        # sound disjunction containing gold -> result CONTAINS gold (zero-FP)
        wrong = [t for t in kin.base if t != e0["type"]][:2]
        S_sound = frozenset([e0["type"]] + wrong)
        seed = [(e0["a"], e0["b"], S_sound)] + [(e["a"], e["b"], frozenset([e["type"]])) for e in edges[1:]]
        Dq = seeded_forward_closure(kin, seed).get((q["source_name"], q["target_name"]), set())
        sound_ok = gold_t in Dq
        # UNSOUND disjunction dropping gold -> must NOT yield the gold singleton
        S_unsound = frozenset(wrong) if wrong else frozenset(["sibling"])
        seed_u = [(e0["a"], e0["b"], S_unsound)] + [(e["a"], e["b"], frozenset([e["type"]])) for e in edges[1:]]
        Du = seeded_forward_closure(kin, seed_u).get((q["source_name"], q["target_name"]), set())
        unsound_safe = not (len(Du) == 1 and next(iter(Du)) == gold_t)
        report["T2_disjunctive_seed"] = {"sound_contains_gold": bool(sound_ok),
                                         "unsound_not_falsely_correct": bool(unsound_safe),
                                         "sound_Dq": sorted(Dq), "unsound_Dq": sorted(Du),
                                         "gold_type": gold_t}
        assert sound_ok, "T2: sound disjunctive seed dropped gold"
        assert unsound_safe, "T2: unsound seed produced a falsely-correct singleton"
    logger.info(f"[symbolic-tests] {json.dumps(report, default=str)[:500]}")
    return report


# =====================================================================
# OUTPUT ASSEMBLY
# =====================================================================
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


def build_spatial_examples(scored, pool):
    exs = []
    for r in scored:
        exs.append({
            "input": f'Region {r["src"]} is {VAGUE_PHRASE.get(r["term"], r["term"])} region {r["dst"]}.',
            "output": json.dumps({"gold": r["gold"], "emitted": sorted(r["S_pred"]),
                                  "confidences": {k: round(v, 4) for k, v in r["conf"].items()},
                                  "sound": r["sound"], "top1": r["top1"]}),
            "predict_top1": r["top1"] or "NONE",
            "metadata_record_kind": "edge_read", "metadata_doc_id": r["doc_id"],
            "metadata_vague_term": r["term"], "metadata_gold": r["gold"],
            "metadata_sound": r["sound"], "metadata_breadth": r["breadth"],
            "metadata_top1_conf": round(r["top1_conf"], 4),
            "metadata_top1_correct": r["top1_correct"], "metadata_parse_fail": r["parse_fail"],
        })
    for p in pool:
        exs.append({
            "input": f'RCC-8 query: relation of region {p["qsrc"]} to {p["qdst"]} via '
                     f'{p["n_paths"]} path(s) with one vague edge per path.',
            "output": json.dumps({"gold": p["gold"], "Dquery": p["Dquery"],
                                  "certificate_decision": p["cert_decision"],
                                  "all_reads_sound": p["all_reads_sound"]}),
            "predict_certificate": p["cert_pred"] if p["cert_decision"] == "COMMIT" else p["cert_decision"],
            "predict_commit_argmax": p["argmax_pred"],
            "predict_abstain_always": "ABSTAIN",
            "metadata_record_kind": "query", "metadata_doc_id": p["doc_id"],
            "metadata_gold": p["gold"], "metadata_n_paths": p["n_paths"],
            "metadata_multipath": p["multipath"], "metadata_all_reads_sound": p["all_reads_sound"],
            "metadata_cert_decision": p["cert_decision"], "metadata_cert_correct": p["cert_correct"],
            "metadata_argmax_correct": p["argmax_correct"],
        })
    return exs


def build_kin_examples(scored, pool, kin):
    exs = []
    for r in scored:
        exs.append({
            "input": f'{r["dst"]} is {r["src"]}\'s {r["term"]}.',
            "output": json.dumps({"gold_type": r["gold"], "emitted": sorted(r["S_pred"]),
                                  "confidences": {k: round(v, 4) for k, v in r["conf"].items()},
                                  "sound": r["sound"], "top1": r["top1"]}),
            "predict_top1": r["top1"] or "NONE",
            "metadata_record_kind": "edge_read", "metadata_doc_id": r["doc_id"],
            "metadata_ambiguous_term": r["term"], "metadata_gold_type": r["gold"],
            "metadata_sound": r["sound"], "metadata_breadth": r["breadth"],
            "metadata_top1_conf": round(r["top1_conf"], 4),
            "metadata_top1_correct": r["top1_correct"], "metadata_parse_fail": r["parse_fail"],
        })
    for p in pool:
        exs.append({
            "input": p["story"][:2600],
            "output": json.dumps({"gold": p["gold"], "Dquery": p["Dquery"],
                                  "certificate_decision": p["cert_decision"],
                                  "all_reads_sound": p["all_reads_sound"]}),
            "predict_certificate": p["cert_pred"] if p["cert_decision"] == "COMMIT" else p["cert_decision"],
            "predict_commit_argmax": p["argmax_pred"],
            "predict_abstain_always": "ABSTAIN",
            "metadata_record_kind": "query", "metadata_doc_id": p["doc_id"],
            "metadata_qsrc": p["qsrc"], "metadata_qtgt": p["qtgt"], "metadata_hop": p["hop"],
            "metadata_gold": p["gold"], "metadata_ambiguous_term": p["fuzzy_term"],
            "metadata_all_reads_sound": p["all_reads_sound"],
            "metadata_cert_decision": p["cert_decision"], "metadata_cert_correct": p["cert_correct"],
            "metadata_argmax_correct": p["argmax_correct"],
        })
    return exs


def make_verdict(spatial_cal, kin_cal, spatial_rc, kin_rc, contrast, cis):
    """Genuine fuzzy-unification adds net-faithful coverage with certificate-bounded
    hallucination IFF: cert coverage>0 AND cert acc high AND cert confident_wrong strictly
    < commit_argmax (CI-separated) AND confidences genuinely <1.0 (frac_conf_1p0 << Mode-P)
    AND reasonably calibrated (ECE small)."""
    def _per_setting(cal, rc, ci):
        if not rc or rc.get("n_pool", 0) == 0:
            return {"label": "NO_POOL"}
        cert = rc["certificate"]
        arg = rc["commit_argmax"]
        cw_diff = ci.get("confident_wrong_diff", {}) if ci else {}
        ci_sep = (cw_diff.get("ci95", [None, None])[0] is not None
                  and cw_diff["ci95"][0] > 0)   # argmax_cw - cert_cw > 0 CI excludes 0
        genuinely_fuzzy = (cal and cal["frac_at_conf_1p0"] is not None
                           and cal["frac_at_conf_1p0"] < 0.5)
        calibrated = (cal and cal["ECE_per_candidate"] is not None
                      and cal["ECE_per_candidate"] < 0.20)
        if cert["coverage"] > 0 and (cert["acc_among_answered"] or 0) >= 0.8 \
                and cert["confident_wrong_rate"] < arg["confident_wrong_rate"] and ci_sep \
                and genuinely_fuzzy:
            label = "YES"
        elif cert["coverage"] == 0 and genuinely_fuzzy:
            label = "READ_INFORMATIVENESS_LIMIT"   # FB1: high-recall but bite-free
        elif cert["confident_wrong_rate"] < arg["confident_wrong_rate"] and genuinely_fuzzy:
            label = "MARGINAL"
        else:
            label = "NO"
        return {"label": label, "cert_coverage": cert["coverage"],
                "cert_acc_among_answered": cert["acc_among_answered"],
                "cert_confident_wrong": cert["confident_wrong_rate"],
                "argmax_confident_wrong": arg["confident_wrong_rate"],
                "cw_reduction_ci_excludes_0": ci_sep, "genuinely_fuzzy": genuinely_fuzzy,
                "calibrated_ece_lt_0p2": calibrated, "zero_fp_holds": rc.get("zero_fp_holds")}
    return {
        "spatial": _per_setting(spatial_cal, spatial_rc, cis.get("spatial")),
        "kinship": _per_setting(kin_cal, kin_rc, cis.get("kinship")),
        "modeP_was_memorized_not_fuzzy": (
            contrast.get("modeP_memorized", {}).get("frac_conf_1p0") == 1.0),
        "summary": _verdict_summary(spatial_cal, kin_cal, spatial_rc, kin_rc, contrast),
    }


def _verdict_summary(scal, kcal, src, krc, contrast):
    parts = []
    mp = contrast.get("modeP_memorized", {})
    if mp.get("frac_conf_1p0") is not None:
        parts.append(
            f"the memorized Mode-P emitted confidence EXACTLY 1.0 on {int(mp.get('frac_conf_1p0')*100)}% "
            f"of cells (mean_conf={mp.get('mean_conf')}), i.e. table recall not fuzzy unification")
    for name, cal in (("spatial RCC-8", scal), ("kinship", kcal)):
        if cal:
            parts.append(
                f"on genuinely-vague {name} reads the LLM emits calibrated disjunctions "
                f"(frac_conf_1p0={cal['frac_at_conf_1p0']:.2f}, mean_breadth={cal['mean_breadth']:.2f}, "
                f"soundness={cal['soundness_rate']:.2f}, ECE_cand={cal['ECE_per_candidate']}, "
                f"ECE_top1={cal['ECE_top1']})")
    for name, rc in (("spatial", src), ("kinship", krc)):
        if rc and rc.get("n_pool"):
            cert = rc["certificate"]
            arg = rc["commit_argmax"]
            parts.append(
                f"the {name} certificate covers {cert['coverage']:.2f} at "
                f"acc={cert['acc_among_answered']} with confident-wrong {cert['confident_wrong_rate']:.3f} "
                f"vs commit-argmax {arg['confident_wrong_rate']:.3f} "
                f"(caught {rc.get('certificate_caught_fraction')} of unsound reads; "
                f"zero-FP on sound reads={rc.get('zero_fp_holds')})")
    return ". ".join(parts) + "." if parts else "no-LLM symbolic validation only."


# =====================================================================
# MAIN
# =====================================================================
@logger.catch(reraise=True)
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mini", action="store_true", help="tiny smoke run")
    ap.add_argument("--no-llm", action="store_true", help="symbolic-only validation ($0)")
    ap.add_argument("--max-per-setting", type=int, default=400,
                    help="cap per-edge calibration reads AND certificate-pool queries per setting")
    ap.add_argument("--sens-cap", type=int, default=150, help="cross-family sensitivity subsample")
    ap.add_argument("--load-cap", type=int, default=0,
                    help="if>0, only load this many source rows per dataset (scaling tests)")
    args = ap.parse_args()
    t0 = time.time()

    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key and not args.no_llm:
        logger.error("OPENROUTER_API_KEY missing; use --no-llm for symbolic-only validation")
        sys.exit(2)

    client = OpenRouterClient(api_key=api_key, model=MODEL, fallbacks=FALLBACKS,
                              cache_dir=CACHE_DIR, temperature=TEMPERATURE,
                              budget_hard=BUDGET_HARD, budget_soft=BUDGET_SOFT,
                              concurrency=CONCURRENCY, max_tokens=320)
    sens_client = OpenRouterClient(api_key=api_key, model=SENS_MODEL, fallbacks=[],
                                   cache_dir=CACHE_DIR, temperature=TEMPERATURE,
                                   budget_hard=BUDGET_HARD, budget_soft=BUDGET_SOFT,
                                   concurrency=CONCURRENCY, max_tokens=320)

    # ---- LOAD ----
    spatial_rows, A = load_spatial(mini=args.mini)
    gen_rows, _disc, comp = load_clutrr(mini=args.mini)
    kin = Kinship(comp)
    if args.load_cap > 0:
        spatial_rows = spatial_rows[:args.load_cap]
        gen_rows = gen_rows[:args.load_cap]
    logger.info(f"loaded spatial={len(spatial_rows)} clutrr_gen={len(gen_rows)}")

    # ---- SYMBOLIC SELF-TESTS (always; $0) ----
    sym_tests = run_symbolic_tests(spatial_rows, A, kin, gen_rows)

    cap = 3 if args.mini else args.max_per_setting

    # ---- READS (term-level, cached) ----
    spatial_reads = elicit_reads(client, VAGUE_RCC8, "spatial", args.no_llm, RCC8_BASE)
    kin_reads = elicit_reads(client, AMBIG_KIN, "kin", args.no_llm, kin.base, KIN_SYN)

    # ---- SETTING 1 : SPATIAL ----
    s_edges = spatial_collect_edges(spatial_rows, A, cap=cap)
    for r in s_edges:
        rd = spatial_reads[r["term"]]
        r.update({"S_pred": rd["S_pred"], "conf": rd["conf"], "raw_max_p": rd["raw_max_p"],
                  "parse_fail": rd["parse_fail"]})
    spatial_cal, spatial_scored = score_reads(s_edges, RCC8_BASE)
    spatial_pool, s_kept, s_dropped, s_multi = spatial_certificate_pool(
        spatial_rows, A, spatial_reads, cap=cap)
    spatial_rc = risk_coverage(spatial_pool)
    logger.info(f"[spatial] cal soundness={spatial_cal['soundness_rate']} "
                f"breadth={spatial_cal['mean_breadth']} ECE_cand={spatial_cal['ECE_per_candidate']}; "
                f"pool n={s_kept} (multipath={s_multi}) cert={spatial_rc.get('certificate')}")

    # ---- SETTING 2 : KINSHIP ----
    k_edges = kin_collect_edges(gen_rows, kin, cap=cap)
    for r in k_edges:
        rd = kin_reads[r["term"]]
        r.update({"S_pred": rd["S_pred"], "conf": rd["conf"], "raw_max_p": rd["raw_max_p"],
                  "parse_fail": rd["parse_fail"]})
    kin_cal, kin_scored = score_reads(k_edges, kin.base)
    kin_pool, k_dropped = kin_certificate_pool(gen_rows, kin, kin_reads, cap=cap)
    kin_rc = risk_coverage(kin_pool)
    logger.info(f"[kin] cal soundness={kin_cal['soundness_rate']} "
                f"breadth={kin_cal['mean_breadth']} ECE_cand={kin_cal['ECE_per_candidate']}; "
                f"pool n={len(kin_pool)} cert={kin_rc.get('certificate')}")

    # ---- STAGE 4 : CALIBRATION CONTRAST ----
    contrast = calibration_contrast(spatial_cal, kin_cal)

    # ---- STAGE 5 : CROSS-FAMILY SENSITIVITY (deepseek) ----
    sensitivity = {"model": SENS_MODEL}
    if not args.no_llm and not args.mini:
        scap = args.sens_cap
        sp_reads_d = elicit_reads(sens_client, VAGUE_RCC8, "spatial", False, RCC8_BASE)
        kin_reads_d = elicit_reads(sens_client, AMBIG_KIN, "kin", False, kin.base, KIN_SYN)
        se = spatial_collect_edges(spatial_rows, A, cap=scap)
        for r in se:
            rd = sp_reads_d[r["term"]]
            r.update({"S_pred": rd["S_pred"], "conf": rd["conf"], "raw_max_p": rd["raw_max_p"],
                      "parse_fail": rd["parse_fail"]})
        scal_d, _ = score_reads(se, RCC8_BASE)
        ke = kin_collect_edges(gen_rows, kin, cap=scap)
        for r in ke:
            rd = kin_reads_d[r["term"]]
            r.update({"S_pred": rd["S_pred"], "conf": rd["conf"], "raw_max_p": rd["raw_max_p"],
                      "parse_fail": rd["parse_fail"]})
        kcal_d, _ = score_reads(ke, kin.base)
        sensitivity["spatial"] = {k: scal_d[k] for k in
                                  ("n_reads", "soundness_rate", "mean_breadth",
                                   "frac_at_conf_1p0", "ECE_per_candidate", "ECE_top1")}
        sensitivity["kinship"] = {k: kcal_d[k] for k in
                                  ("n_reads", "soundness_rate", "mean_breadth",
                                   "frac_at_conf_1p0", "ECE_per_candidate", "ECE_top1")}
        sensitivity["budget_usd"] = sens_client.stats()["cumulative_usd"]
    else:
        sensitivity["note"] = "skipped (--no-llm or --mini)"

    # ---- STAGE 6 : TRACES ----
    traces = {"spatial": spatial_traces(spatial_pool, A), "kinship": kin_traces(kin_pool, kin)}

    # ---- STAGE 7 : BOOTSTRAP CIs ----
    cis = {"spatial": {}, "kinship": {}}
    for name, scored, pool in (("spatial", spatial_scored, spatial_pool),
                               ("kinship", kin_scored, kin_pool)):
        if scored:
            cis[name]["soundness_rate"] = clustered_bootstrap_ci(
                _doc_vals(scored, "doc_id", lambda r: r["sound"]))
            cis[name]["top1_accuracy"] = clustered_bootstrap_ci(
                _doc_vals(scored, "doc_id", lambda r: r["top1_correct"]))
        if pool:
            cis[name]["confident_wrong_diff"] = paired_diff_ci(
                pool,
                lambda p: (not p["argmax_correct"]),                                   # argmax confident-wrong
                lambda p: (p["cert_decision"] == "COMMIT" and not p["cert_correct"]))   # cert confident-wrong
            cis[name]["certificate_coverage"] = clustered_bootstrap_ci(
                _doc_vals(pool, "doc_id", lambda p: p["cert_decision"] == "COMMIT"))

    verdict = make_verdict(spatial_cal, kin_cal, spatial_rc, kin_rc, contrast, cis)

    # ---- ASSEMBLE OUTPUT ----
    spatial_examples = build_spatial_examples(spatial_scored, spatial_pool)
    kin_examples = build_kin_examples(kin_scored, kin_pool, kin)
    if not spatial_examples:
        spatial_examples = [{"input": "no-data", "output": "EMPTY", "metadata_note": "empty"}]
    if not kin_examples:
        kin_examples = [{"input": "no-data", "output": "EMPTY", "metadata_note": "empty"}]

    metadata = {
        "method_name": "Genuine LLM fuzzy-unification with a certificate-bounded hallucination guarantee",
        "tag": "REAL-LLM-FUZZY-READ",
        "scope_statement": (
            "Two GENUINELY-fuzzy read settings constructed from existing gold: vague/out-of-table "
            "spatial RCC-8 (SpaRP-PS1) and ambiguous/paraphrased kinship (CLUTRR). The LLM emits a "
            "CALIBRATED sub-1.0 disjunction; an abstain-on-collapse CERTIFICATE bounds the "
            "hallucination cost when that disjunction is fed into the sound closure engine. This is "
            "the honest replacement for the circular memorized Mode-P (confidence exactly 1.0)."),
        "reader_model": MODEL, "model_fallbacks": FALLBACKS, "sens_model": SENS_MODEL,
        "temperature": TEMPERATURE, "seed": SEED,
        "vague_term_maps": {"spatial_rcc8": VAGUE_RCC8, "kinship_types": AMBIG_KIN},
        "symbolic_self_tests": sym_tests,
        # Setting 1
        "setting1_spatial_calibration": spatial_cal,
        "setting1_spatial_risk_coverage": spatial_rc,
        "setting1_spatial_pool_provenance": {
            "n_kept": s_kept, "n_dropped_no_rcc8_path": s_dropped, "n_multipath": s_multi,
            "n_calibration_edges": len(spatial_scored)},
        # Setting 2
        "setting2_kinship_calibration": kin_cal,
        "setting2_kinship_risk_coverage": kin_rc,
        "setting2_kinship_pool_provenance": {
            "n_kept": len(kin_pool), "n_dropped_unclean": k_dropped,
            "n_calibration_edges": len(kin_scored)},
        # Stage 4-7
        "calibration_contrast_vs_modeP": contrast,
        "cross_family_sensitivity": sensitivity,
        "flagged_fuzzy_step_traces": traces,
        "bootstrap_cis": cis,
        "honesty_caveats": [
            "the vague/ambiguous TERM is the unit of fuzziness: reads are term-conditioned "
            "(temp 0, sha256-cached), so ~6 distinct reads per setting drive hundreds of "
            "per-edge calibration records; the empirical gold mix per term is the calibration target",
            "SpaRP-PS1 uses SYMBOLIC region ids (char_spans=[]) and templated text -- the vague "
            "rendering is a minimal stand-alone sentence (the gold RCC-8 relation is the construction target)",
            "CLUTRR is a templated kinship benchmark (max 871 chars), not natural long-form text",
            "soundness = gold IN the emitted set; an UNSOUND read is the silent-wrong-narrowing "
            "failure mode that the certificate is designed to catch (collapse/abstain)",
            "the read-soundness-conditional zero-FP invariant is asserted on the all-sound subset, "
            "NOT an unconditional guarantee -- an unsound read can still slip a wrong singleton "
            "through (reported as certificate_caught_fraction < 1)",
            "Mode-P contrast is loaded from the iter-4 method_out.json (memorized recall, conf 1.0)",
        ],
        "budget": client.stats(),
        "verdict": verdict,
        "runtime_sec": round(time.time() - t0, 1),
    }

    datasets = [
        {"dataset": "spatial_fuzzy_rcc8", "examples": spatial_examples},
        {"dataset": "kinship_fuzzy_paraphrase", "examples": kin_examples},
    ]
    out = {"metadata": metadata, "datasets": datasets}

    # honest TOTAL spend across the whole disk cache
    total_cache_spend = 0.0
    n_cache_calls = 0
    for cf in CACHE_DIR.glob("*.json"):
        try:
            c = json.loads(cf.read_text()).get("cost", 0.0) or 0.0
            total_cache_spend += float(c)
            n_cache_calls += 1
        except Exception:
            continue
    out["metadata"]["budget"]["sens_budget"] = sens_client.stats()
    out["metadata"]["budget"]["total_api_spend_all_runs_usd"] = round(total_cache_spend, 6)
    out["metadata"]["budget"]["n_cached_calls_on_disk"] = n_cache_calls
    out["metadata"]["budget"]["note"] = (
        "cumulative_usd is THIS invocation's marginal cost (0 when cache-served); "
        "total_api_spend_all_runs_usd is the real money spent to build the sha256 cache.")

    out_path = WORKDIR / "method_out.json"
    out_path.write_text(json.dumps(out, default=_json_default, ensure_ascii=False))
    total = client.cost + sens_client.cost
    logger.info(f"wrote {out_path} ({out_path.stat().st_size/1e6:.2f} MB); "
                f"marginal cost=${total:.4f}; runtime={time.time()-t0:.1f}s")
    logger.info(f"VERDICT: {verdict['summary']}")
    assert total < BUDGET_HARD, f"budget exceeded: ${total}"
    gc.collect()


if __name__ == "__main__":
    main()
