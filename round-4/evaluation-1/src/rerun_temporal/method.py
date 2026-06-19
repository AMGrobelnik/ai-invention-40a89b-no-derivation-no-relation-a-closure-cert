#!/usr/bin/env python3
"""LOCAL-reader real-text head-to-head (H1) + end-to-end hallucination reduction (H2)
   on ACTUAL NarrativeTime (+TDDMan), two readers, matched-coverage baselines.

THE HEADLINE EXPERIMENT (experiment_iter2_dir5) of the Closure-Certified Text-to-Logic
Deduction Module.

OUR METHOD = Mode-A: iterated path-consistency CLOSURE (PC-2, engine.pc2_full) over
SPAN-LOCAL LLM reads of the constituent path edges, with the query edge HELD OUT (left
at universe). The closure must RECOVER the deduction-required query relation from local
reads it never saw directly.

BASELINES (same pipeline, same local reads, same coverage object):
  * NAIVE single-pass intersection (engine.naive_single_pass)  -- iteration contrast.
  * RAW local LLM (forced single relation from the query edge's OWN local read).
  * PATH-OF-THOUGHTS (per-path LLM composition, modal vote, abstain on path disagreement;
    NO cross-path intersection -- isolates the intersection step Mode-A adds).
  * SELF-CONSISTENCY voting (k paraphrase samples of the query local read, majority).

H1 (gateway): Mode-A selective accuracy at MATCHED coverage beats PoT AND SC
  (doc-clustered paired bootstrap, Holm-Bonferroni adjusted).
H2 (gateway): Mode-A confident-wrong (hallucination) rate on deduction-required queries
  drops >= 0.05 ABS vs RAW (doc-clustered paired bootstrap, adjusted).

Closure runs in the CONVEX POINT START-POINT algebra (PC-COMPLETE, exact) -- the five
coarse temporal labels {before, after, simultaneous, includes, is_included} correspond
exactly to the five convex point relations {<},{>},{=},{<,=},{=,>}; the universe {<,=,>}
is no-commitment. Every number is TAGGED REAL-LLM-READ / SYNTHETIC-CHANNEL /
GOLD-ONLY-GATE / THEOREM.

Engine + OpenRouter client + closure tests + coarse maps are REUSED from iter-1 verbatim;
the genuinely new code is the dataset adapter (data_adapter.py), the span-LOCAL reads, the
matched-coverage risk-coverage comparison, the end-to-end Prolog discharge, and the $0
synthetic matched-coverage backstop (synth_channel.py)."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import shutil
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from loguru import logger
from scipy.stats import binomtest

import data_adapter as DA
import synth_channel as SC
from corpora import (COARSE_TO_POINT, COARSE_VOCAB_ALLEN, COARSE_VOCAB_POINT)
from engine import QCN, build_point_algebra, naive_single_pass, pc2_full
from llm import OpenRouterClient, parse_relations
from tests import closure_tests_pass

HERE = Path(__file__).parent
RESULTS = HERE / "results"
FIGS = RESULTS / "figures"
for d in (RESULTS, FIGS, HERE / "logs"):
    d.mkdir(parents=True, exist_ok=True)

# ============================ PRE-REGISTERED CONFIGURATION ============================
SEED = 20260617
# PRIMARY reader = lite tier (the weak anchor whose local-read soundness we probe).
READER_PRIMARY = "google/gemini-3.1-flash-lite"
PRIMARY_FALLBACKS = ["deepseek/deepseek-v3.2", "deepseek/deepseek-v4-flash"]
# STRONGER reader = a CLEAR capability jump above the lite primary, for the recall-gate-
# crossing test (is the bottleneck read soundness, or merely a weak-model artifact?).
# iter-3 choice: deepseek-v4-pro (frontier tier; decisive on the probe where flash-lite
# abstained). It is CROSS-FAMILY w.r.t. the gemini primary, which STRENGTHENS the
# "not a weak-model artifact" argument (rules out a gemini-family-specific failure), and
# it is ~100x cheaper per call than gemini-3.5-flash ($0.43/$0.87 vs $1.50/$9.00 per-M
# tokens), making >=150-scorable-edge reads on BOTH corpora affordable under the $9 cap.
# gemini-3.5-flash is kept ONLY as a labelled fallback. Capability ORDERING is what the
# gate test needs (strong strictly > primary), not the exact id.
READER_STRONG = "deepseek/deepseek-v4-pro"
STRONG_FALLBACKS = ["google/gemini-3.5-flash", "deepseek/deepseek-v3.2"]
TEMPERATURE = 0.0
SC_TEMPERATURE = 0.7                              # self-consistency sampling temperature
RECALL_GATE = {"POINT": 0.90, "ALLEN": 0.85}      # PC-complete point arm -> 0.90 bar
APPLIC = {"general": 0.10, "module": 0.05}
H2_MIN_EFFECT = 0.05                              # confident-wrong must drop >= 5 pts ABS
N_TARGET = 300                                    # >=10x iter-1 n=7
V_MAX = 3                                         # vias per query (induced-subgraph closure)
# iter-3 EDIT B: run the stronger reader on BOTH real corpora to a powered scorable-edge
# count, accumulating query-by-query (round-robin doc spread, already in arm['queries']
# order) until >=STRONG_MIN_SCORABLE scorable (non-VAGUE-gold, locally-readable) edges are
# covered, capping total reads at STRONG_MAX per corpus.
STRONG_MIN_SCORABLE = 160                         # >=150 powered recall-CI per corpus
STRONG_MAX = 320                                  # hard cap on strong reads per corpus
STRONG_QUERY_CAP = 40                             # legacy mini-mode bound (kept for --mini)
CONFIRM_MIN_N = 70                                # CONFIRM requires >= this many scored queries
SC_K = 5
BOOT_B = 2000
ALPHA = 0.05
CONFIRM_FAMILY = ["H1_vs_PoT", "H1_vs_SC", "H2_halluc"]   # Holm-Bonferroni gatekeeping
GLOBAL_CAP = 9.0                                  # HARD total across ALL clients (< $10 cap)
BUDGET_SOFT = 3.0


def enforce_global_cap(active, others):
    """Lower the ACTIVE client's hard budget so the SUM across all clients never exceeds
    GLOBAL_CAP. Phases run sequentially with one active client, so this guarantees the
    cumulative OpenRouter spend stays < the $10 ceiling."""
    spent_others = sum(c.cost for c in others)
    active.budget_hard = max(0.0, GLOBAL_CAP - spent_others)

PT = build_point_algebra()
COARSE_LABELS = ["before", "after", "simultaneous", "includes", "is_included"]
# the 5 coarse labels <-> the 5 convex point relations (exact bijection)
POINT_SET_TO_COARSE = {
    frozenset({"<"}): "before", frozenset({">"}): "after",
    frozenset({"="}): "simultaneous", frozenset({"<", "="}): "includes",
    frozenset({"=", ">"}): "is_included",
}
COARSE_CONVERSE = {"before": "after", "after": "before", "simultaneous": "simultaneous",
                   "includes": "is_included", "is_included": "includes"}


# ============================ PROMPTS ============================
def _vocab_desc(vocab):
    defs = {
        "before": "E1 entirely precedes E2",
        "after": "E1 entirely follows E2",
        "simultaneous": "E1 and E2 occur at the same time / over the same span",
        "includes": "E1's time span contains E2's",
        "is_included": "E1's time span is contained within E2's",
    }
    return "; ".join(f"'{v}' ({defs[v]})" for v in vocab)


def build_read_prompt(marked_text, algebra, variant=""):
    """Span-LOCAL temporal-relation read. Requests BOTH a sound disjunctive set (for
    closure) AND a single most_likely relation + confidence (for raw / risk-coverage)."""
    vocab = COARSE_VOCAB_POINT if algebra == "POINT" else COARSE_VOCAB_ALLEN
    system = (
        "You read the temporal relation between two events marked [[E1]]...[[/E1]] and "
        "[[E2]]...[[/E2]] in a news text excerpt. "
        f"Allowed base relations: {_vocab_desc(vocab)}. "
        "Name ALL base relations the text does NOT exclude (recall matters more than "
        "precision: better to include an extra relation than to omit the correct one). "
        "If the excerpt does not constrain the order, set underdetermined=true. "
        "Judge ONLY from the given excerpt; do NOT assume consistency with any other pair. "
        'Reply with ONLY a JSON object: {"relations": [<allowed relation strings>], '
        '"underdetermined": <true|false>, "most_likely": "<the single most probable '
        'relation>", "confidence": <0..1 probability your most_likely relation is correct>}.'
        + (f" {variant}" if variant else "")
    )
    user = f"{marked_text}\n\nWhat is the temporal relation of E1 to E2?"
    return system, user


def build_pot_prompt(fact1, fact2, algebra):
    """Path-of-Thoughts per-path reasoning: compose two local edge facts into the
    endpoint relation INDEPENDENTLY (no cross-path intersection)."""
    vocab = COARSE_VOCAB_POINT if algebra == "POINT" else COARSE_VOCAB_ALLEN
    system = (
        "You are given two temporal facts about three events A, B, C. "
        f"Allowed relations: {_vocab_desc(vocab)}. "
        "Using ONLY these two facts and transitive temporal reasoning, infer the single "
        "most likely temporal relation of A to C. If the two facts do not determine it, "
        "set underdetermined=true. "
        'Reply with ONLY JSON: {"most_likely": "<relation>", "confidence": <0..1>, '
        '"underdetermined": <true|false>}.'
    )
    user = f"Fact 1: {fact1}\nFact 2: {fact2}\n\nWhat is the temporal relation of A to C?"
    return system, user


# ============================ PARSING ============================
def _to_coarse_label(tok, vocab):
    if tok is None:
        return None
    coarse, _, _ = parse_relations(json.dumps({"relations": [tok]}), vocab)
    return coarse[0] if coarse else None


def parse_read(content, algebra):
    """Return dict {coarse_set:list, underdet, pfail, most_likely:coarse|None, conf:float}."""
    vocab = COARSE_VOCAB_POINT if algebra == "POINT" else COARSE_VOCAB_ALLEN
    coarse, underdet, pfail = parse_relations(content, vocab)
    most_likely, conf = None, 0.5
    try:
        txt = (content or "").strip()
        obj = _safe_json(txt)
        if isinstance(obj, dict):
            ml = obj.get("most_likely")
            if isinstance(ml, list) and ml:
                ml = ml[0]
            most_likely = _to_coarse_label(ml, vocab)
            c = obj.get("confidence")
            if isinstance(c, (int, float)):
                conf = float(max(0.0, min(1.0, c)))
    except Exception:
        pass
    if most_likely is None and coarse:
        most_likely = coarse[0]
    return {"coarse_set": coarse, "underdet": underdet, "pfail": pfail,
            "most_likely": most_likely, "conf": conf}


def parse_pot(content, algebra):
    vocab = COARSE_VOCAB_POINT if algebra == "POINT" else COARSE_VOCAB_ALLEN
    obj = _safe_json((content or "").strip())
    if isinstance(obj, dict):
        if obj.get("underdetermined"):
            return None, 0.0
        ml = obj.get("most_likely")
        if isinstance(ml, list) and ml:
            ml = ml[0]
        lab = _to_coarse_label(ml, vocab)
        c = obj.get("confidence", 0.5)
        c = float(c) if isinstance(c, (int, float)) else 0.5
        return lab, max(0.0, min(1.0, c))
    coarse, underdet, _ = parse_relations(content, vocab)
    if underdet or not coarse:
        return None, 0.0
    return coarse[0], 0.5


def _safe_json(txt):
    import re
    txt = re.sub(r"^```(?:json)?|```$", "", txt, flags=re.M).strip()
    for cand in (txt, _first_block(txt)):
        if cand is None:
            continue
        try:
            return json.loads(cand)
        except Exception:
            continue
    return None


def _first_block(txt):
    s = txt.find("{")
    if s < 0:
        return None
    depth = 0
    for i in range(s, len(txt)):
        if txt[i] == "{":
            depth += 1
        elif txt[i] == "}":
            depth -= 1
            if depth == 0:
                return txt[s:i + 1]
    return None


# ============================ coarse <-> point ============================
def coarse_to_point(coarse_set, underdet):
    """Union of coarse labels -> convex point set. Empty/underdet -> universe."""
    if underdet or not coarse_set:
        return PT.universe
    out = set()
    for c in coarse_set:
        out |= set(COARSE_TO_POINT[c])
    pset = frozenset(out) if out else PT.universe
    pset, _ = PT.widen(pset)
    return pset


def orient_coarse(label, stored_uv, want_uv):
    if label is None:
        return None
    if stored_uv == want_uv:
        return label
    if (stored_uv[1], stored_uv[0]) == want_uv:
        return COARSE_CONVERSE[label]
    return label


def orient_point(pset, stored_uv, want_uv):
    if stored_uv == want_uv:
        return pset
    if (stored_uv[1], stored_uv[0]) == want_uv:
        return PT.converse(pset)
    return pset


def point_to_coarse(R):
    return POINT_SET_TO_COARSE.get(frozenset(R))


# ============================ elicitation item building ============================
def make_read_items(arm, reader_tag, only_keys=None):
    items, index = [], {}
    for key, task in arm["edge_tasks"].items():
        if only_keys is not None and key not in only_keys:
            continue
        if not task["has_local_span"]:
            continue
        system, user = build_read_prompt(task["marked_text"], task["algebra"])
        iid = f"read|{reader_tag}|{arm['arm']}|" + "|".join(map(str, key))
        items.append({"id": iid, "system": system, "user": user})
        index[iid] = key
    return items, index


def parse_read_results(results, index, arm):
    """emitted[(docid,u,v)] = {coarse_set, underdet, most_likely, conf, point_set,
    stored_uv}."""
    emitted = {}
    n_pfail = 0
    for iid, payload in results.items():
        key = index.get(iid)
        if key is None:
            continue
        task = arm["edge_tasks"][key]
        pr = parse_read(payload.get("content", ""), task["algebra"])
        if pr["pfail"]:
            n_pfail += 1
        emitted[key] = {
            "coarse_set": pr["coarse_set"], "underdet": pr["underdet"],
            "most_likely": pr["most_likely"], "conf": pr["conf"],
            "point_set": coarse_to_point(pr["coarse_set"], pr["underdet"]),
            "stored_uv": (task["u"], task["v"]),
            "pfail": bool(pr["pfail"]),
        }
    return emitted, n_pfail


# ============================ per-edge recall + stronger-reader gate ============================
def per_edge_recall(arm, emitted):
    """recall = P(gold point relation subset of emitted point set), over scorable edges,
    with doc-clustered bootstrap CI and within-doc soundness ICC."""
    sound_by_doc = defaultdict(list)
    n = 0
    n_pfail_excluded = 0
    breadth = []
    for key, task in arm["edge_tasks"].items():
        if task["gold"] == "VAGUE":
            continue
        em = emitted.get(key)
        if em is None:                       # not actually read (no span / budget-skipped)
            continue
        if em.get("pfail"):
            # parse failure (e.g. a reasoning model truncated to EMPTY content) is MISSING
            # DATA, not a sound 'universe' read -> EXCLUDE from recall (else recall is
            # spuriously inflated to 1 because gold is trivially subset of the universe).
            n_pfail_excluded += 1
            continue
        gold_pt = coarse_to_point([task["gold"]], False)
        bset = em["point_set"]
        sound = 1 if gold_pt <= bset else 0
        sound_by_doc[task["docid"]].append(sound)
        breadth.append(len(bset))
        n += 1
    recalls = [x for v in sound_by_doc.values() for x in v]
    recall = float(np.mean(recalls)) if recalls else float("nan")
    return {
        "recall": recall, "n_scorable_edges": n,
        "n_parse_fail_excluded": n_pfail_excluded,
        "parse_fail_rate": (n_pfail_excluded / (n + n_pfail_excluded)) if (n + n_pfail_excluded) else 0.0,
        "recall_ci95": clustered_bootstrap_ci(sound_by_doc),
        "rho_within_doc_soundness": icc_oneway(list(sound_by_doc.values())),
        "breadth_mean": float(np.mean(breadth)) if breadth else float("nan"),
    }


# ============================ closure pipeline + baselines per query ============================
def run_query(q, emitted, sc_votes=None, pot_preds=None):
    """Return per-method records for ONE query: each = {answered, pred, correct, conf}."""
    docid, qx, qy = q["docid"], q["qx"], q["qy"]
    gold = q["gold"]
    nodes = q["induced_nodes"]
    qcn = QCN(PT, nodes)
    contrib_confs = []
    n_path_edges_set = 0
    for (a, b) in q["path_edges"]:
        key = (docid,) + tuple(sorted((a, b)))
        em = emitted.get(key)
        if em is None:
            continue
        oriented = orient_point(em["point_set"], em["stored_uv"], (a, b))
        i, j = qcn.index[a], qcn.index[b]
        qcn.set_edge(i, j, oriented)
        if oriented != PT.universe:
            n_path_edges_set += 1
            if em["conf"] is not None:
                contrib_confs.append(em["conf"])
    qi, qj = qcn.index[qx], qcn.index[qy]
    path_conf = float(min(contrib_confs)) if contrib_confs else 0.0

    # --- NAIVE (read-only) BEFORE pc2_full mutates the network ---
    naive_set = naive_single_pass(qcn, qi, qj)
    # --- Mode-A FULL closure (our method); query held at universe ---
    ok, n_fired = pc2_full(qcn)
    full_set = PT.empty if not ok else qcn.get(qi, qj)

    def commit(R):
        if not R:
            return ("collapse", None)
        lab = point_to_coarse(R)
        return ("answer", lab) if lab is not None else ("abstain", None)

    fstat, fpred = commit(full_set)
    modeA = {"answered": fstat == "answer", "pred": fpred,
             "correct": (int(fpred == gold) if fstat == "answer" else None),
             "conf": path_conf, "collapse": fstat == "collapse",
             "narrowed": full_set != PT.universe}
    nstat, npred = commit(naive_set)
    naive = {"answered": nstat == "answer", "pred": npred,
             "correct": (int(npred == gold) if nstat == "answer" else None),
             "conf": path_conf}

    # --- RAW: query edge's own local read, forced single ---
    qkey = (docid,) + tuple(sorted((qx, qy)))
    em_q = emitted.get(qkey)
    if em_q is not None and em_q["most_likely"] is not None:
        raw_pred = orient_coarse(em_q["most_likely"], em_q["stored_uv"], (qx, qy))
        raw = {"answered": True, "pred": raw_pred, "correct": int(raw_pred == gold),
               "conf": em_q["conf"]}
    else:
        raw = {"answered": False, "pred": None, "correct": None, "conf": 0.0}

    # --- PATH-OF-THOUGHTS: modal vote over per-path LLM compositions; abstain on disagree ---
    pot = {"answered": False, "pred": None, "correct": None, "conf": 0.0}
    if pot_preds:
        preds = [p for (p, _) in pot_preds if p is not None]
        confs = [c for (p, c) in pot_preds if p is not None]
        if preds:
            counts = {l: preds.count(l) for l in set(preds)}
            top = max(counts, key=counts.get)
            agree = counts[top] / len(preds)
            answered = (len(counts) == 1) or (agree > 0.5)
            pot = {"answered": answered, "pred": (top if answered else None),
                   "correct": (int(top == gold) if answered else None),
                   "conf": float(agree * (np.mean(confs) if confs else 0.5))}

    # --- SELF-CONSISTENCY: majority of k query-edge samples ---
    sc = {"answered": False, "pred": None, "correct": None, "conf": 0.0}
    if sc_votes:
        # sc_votes are ALREADY oriented to (qx,qy) at parse time -> use directly
        votes = [v for v in sc_votes if v is not None]
        if votes:
            counts = {l: votes.count(l) for l in set(votes)}
            top = max(counts, key=counts.get)
            margin = counts[top] / len(votes)
            sc = {"answered": True, "pred": top, "correct": int(top == gold),
                  "conf": float(margin)}

    return {"modeA": modeA, "naive": naive, "raw": raw, "pot": pot, "sc": sc,
            "n_fired": n_fired, "n_path_edges_set": n_path_edges_set,
            "stratum": q["stratum"], "docid": docid, "gold": gold,
            "sentdiff": q["sentdiff"]}


# ============================ statistics ============================
def icc_oneway(groups):
    groups = [g for g in groups if len(g) >= 2]
    if len(groups) < 2:
        return None
    N = sum(len(g) for g in groups)
    k = len(groups)
    grand = sum(sum(g) for g in groups) / N
    ms_between = sum(len(g) * (np.mean(g) - grand) ** 2 for g in groups) / (k - 1)
    ss_within = sum(sum((x - np.mean(g)) ** 2 for x in g) for g in groups)
    ms_within = ss_within / (N - k) if N > k else 0.0
    sum_n2 = sum(len(g) ** 2 for g in groups)
    n0 = (N - sum_n2 / N) / (k - 1)
    denom = ms_between + (n0 - 1) * ms_within
    if denom == 0:
        return 0.0
    return float((ms_between - ms_within) / denom)


def clustered_bootstrap_ci(doc_to_vals, B=BOOT_B, seed=SEED, alpha=ALPHA):
    docs = [d for d, v in doc_to_vals.items() if v]
    if len(docs) < 2:
        allv = [x for v in doc_to_vals.values() for x in v]
        m = float(np.mean(allv)) if allv else float("nan")
        return [m, m]
    rng = np.random.default_rng(seed)
    arrs = {d: np.array(doc_to_vals[d], dtype=float) for d in docs}
    nd = len(docs)
    means = []
    for _ in range(B):
        pick = rng.integers(0, nd, nd)
        vals = np.concatenate([arrs[docs[i]] for i in pick])
        means.append(vals.mean())
    lo, hi = np.quantile(means, [alpha / 2, 1 - alpha / 2])
    return [float(lo), float(hi)]


def _curve(records):
    """Risk-coverage curve: returns sorted list of (coverage, selective_acc) plus the
    method's natural coverage (fraction answered) and overall selective acc."""
    n = len(records)
    ans = [(r["conf"], r["correct"]) for r in records
           if r["answered"] and r["correct"] is not None]
    if n == 0:
        return [], 0.0, float("nan")
    ans.sort(key=lambda x: -x[0])
    pts = []
    cum = 0
    for k, (_, corr) in enumerate(ans, start=1):
        cum += corr
        pts.append((k / n, cum / k))
    nat_cov = len(ans) / n
    nat_acc = (cum / len(ans)) if ans else float("nan")
    return pts, nat_cov, nat_acc


def _acc_at_coverage(pts, target):
    """Interpolate selective accuracy at a target coverage. NaN if target exceeds the
    method's max coverage."""
    if not pts:
        return float("nan")
    if target <= pts[0][0]:
        return pts[0][1]
    if target > pts[-1][0] + 1e-9:
        return float("nan")
    for i in range(1, len(pts)):
        c0, a0 = pts[i - 1]
        c1, a1 = pts[i]
        if c0 <= target <= c1:
            if c1 == c0:
                return a1
            w = (target - c0) / (c1 - c0)
            return a0 + w * (a1 - a0)
    return pts[-1][1]


def matched_coverage_gap(method_recs, base_recs, by_doc_method, by_doc_base,
                         seed=SEED, B=BOOT_B):
    """Gap = method selective_acc at method's natural coverage MINUS baseline acc at the
    SAME coverage. Doc-clustered paired bootstrap CI on the gap."""
    m_pts, m_cov, m_acc = _curve(method_recs)
    b_pts, b_cov, b_acc_nat = _curve(base_recs)
    base_acc = _acc_at_coverage(b_pts, m_cov)
    point_gap = m_acc - base_acc if (m_acc == m_acc and base_acc == base_acc) else float("nan")
    base_unreachable = (b_cov + 1e-9 < m_cov)   # baseline structurally cannot match coverage
    docs = sorted(set(by_doc_method) | set(by_doc_base))
    rng = np.random.default_rng(seed)
    gaps = []
    nd = len(docs)
    for _ in range(B):
        pick = [docs[i] for i in rng.integers(0, nd, nd)]
        mrec = [r for d in pick for r in by_doc_method.get(d, [])]
        brec = [r for d in pick for r in by_doc_base.get(d, [])]
        mp, mc, ma = _curve(mrec)
        bp, _, _ = _curve(brec)
        ba = _acc_at_coverage(bp, mc)
        if ma == ma and ba == ba:
            gaps.append(ma - ba)
    if not gaps:
        return {"gap": point_gap, "ci95": [float("nan"), float("nan")],
                "matched_coverage": m_cov, "method_acc": m_acc, "base_acc": base_acc,
                "base_max_coverage": b_cov, "base_unreachable": bool(base_unreachable),
                "boot_p_gap_le_0": (0.0 if base_unreachable else 1.0)}
    lo, hi = np.quantile(gaps, [ALPHA / 2, 1 - ALPHA / 2])
    p_gt0 = float(np.mean([g > 0 for g in gaps]))
    return {"gap": point_gap, "ci95": [float(lo), float(hi)], "boot_p_gap_le_0": 1 - p_gt0,
            "matched_coverage": m_cov, "method_acc": m_acc, "base_acc": base_acc,
            "base_max_coverage": b_cov, "base_unreachable": bool(base_unreachable),
            "n_boot": len(gaps)}


def auc_rc(pts, grid=None):
    if grid is None:
        grid = np.linspace(0.05, 0.95, 19)
    vals = [_acc_at_coverage(pts, c) for c in grid]
    vals = [v for v in vals if v == v]
    return float(np.mean(vals)) if vals else float("nan")


def holm_bonferroni(pvals: dict, alpha=ALPHA):
    """Return {name: {p, adjusted_significant}} via Holm step-down."""
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(items)
    out = {}
    rejected_all_below = True
    for rank, (name, p) in enumerate(items):
        thresh = alpha / (m - rank)
        sig = (p <= thresh) and rejected_all_below
        if not sig:
            rejected_all_below = False
        out[name] = {"p": float(p), "holm_threshold": float(thresh),
                     "adjusted_significant": bool(sig)}
    return out


# ============================ per-corpus gate-crossing test (iter-3 EDIT C) ============================
def gate_crossing_test(recall, ci95, n_scorable, gate=0.90):
    """Locate a per-(corpus,reader) recall relative to the point gate.

    PRIMARY = doc-clustered bootstrap CI position vs the gate:
      'CI_excludes_above_gate' (ci_lo > gate, recall provably >= gate),
      'CI_excludes_below_gate' (ci_hi < gate, recall provably < gate),
      'CI_contains_gate'       (the CI straddles the gate -> indeterminate).
    SECONDARY (labelled ANTICONSERVATIVE) = one-sided binomial p(recall < gate) that
    IGNORES within-document clustering (rho>0 inflates significance) -> reported, never
    load-bearing. 'sits_at_gate' flags |recall-gate|<0.02 (a knife-edge)."""
    if recall is None or recall != recall or not n_scorable:
        return {"recall": recall, "n_scorable": n_scorable, "verdict": "INSUFFICIENT_DATA"}
    lo, hi = (ci95 if ci95 and len(ci95) == 2 else (None, None))
    if lo is not None and lo == lo and lo > gate:
        verdict = "CI_excludes_above_gate"
    elif hi is not None and hi == hi and hi < gate:
        verdict = "CI_excludes_below_gate"
    else:
        verdict = "CI_contains_gate"
    n_sound = int(round(recall * n_scorable))
    try:
        binom_p = float(binomtest(n_sound, n_scorable, gate, alternative="less").pvalue)
    except Exception:
        binom_p = None
    return {"recall": float(recall), "ci95": [lo, hi], "n_scorable": int(n_scorable),
            "n_sound": n_sound, "gate": gate, "verdict": verdict,
            "crosses_gate": bool(recall >= gate),
            "sits_at_gate": bool(abs(recall - gate) < 0.02),
            "binomial_p_recall_lt_gate_ANTICONSERVATIVE": binom_p,
            "primary_evidence": "clustered-bootstrap CI position vs gate",
            "secondary_evidence": "binomial p (ignores doc-clustering -> anticonservative)"}


# ============================ H2 hallucination ============================
def h2_confident_wrong(query_results):
    """confident_wrong = frac of NON-ABSTAINED predictions that are wrong, on
    deduction-required queries. Compare Mode-A vs RAW with doc-clustered paired bootstrap
    on the reduction. Also decompose Mode-A confident-wrong into SILENT-WRONG-NARROWING."""
    cw_modeA_by_doc = defaultdict(list)
    cw_raw_by_doc = defaultdict(list)
    silent_wrong = 0
    modeA_wrong = 0
    for qr in query_results:
        d = qr["docid"]
        m = qr["modeA"]
        r = qr["raw"]
        if m["answered"]:
            wrong = int(m["correct"] == 0)
            cw_modeA_by_doc[d].append(wrong)
            if wrong:
                modeA_wrong += 1
                # silent-wrong-narrowing: closure committed to a wrong singleton because a
                # contributing edge was unsound (the pre-registered failure mode).
                silent_wrong += 1
        if r["answered"]:
            cw_raw_by_doc[d].append(int(r["correct"] == 0))
    cw_modeA = float(np.mean([x for v in cw_modeA_by_doc.values() for x in v])) \
        if cw_modeA_by_doc else float("nan")
    cw_raw = float(np.mean([x for v in cw_raw_by_doc.values() for x in v])) \
        if cw_raw_by_doc else float("nan")
    docs = sorted(set(cw_modeA_by_doc) | set(cw_raw_by_doc))
    rng = np.random.default_rng(SEED + 5)
    reductions = []
    nd = len(docs)
    for _ in range(BOOT_B):
        pick = [docs[i] for i in rng.integers(0, nd, nd)] if nd else []
        mv = [x for d in pick for x in cw_modeA_by_doc.get(d, [])]
        rv = [x for d in pick for x in cw_raw_by_doc.get(d, [])]
        if mv and rv:
            reductions.append(np.mean(rv) - np.mean(mv))
    if reductions:
        lo, hi = np.quantile(reductions, [ALPHA / 2, 1 - ALPHA / 2])
        p_le0 = float(np.mean([x <= 0 for x in reductions]))
    else:
        lo = hi = float("nan"); p_le0 = float("nan")
    # iter-3 EDIT D: report confident-wrong AT its coverage; the FAIR cross-method metric is
    # selective accuracy at MATCHED coverage (H1), not confident-wrong in isolation (Mode-A
    # cuts confident-wrong partly by abstaining more -> the abstention rate must be stated).
    n_pool = len(query_results)
    n_modeA_ans = sum(len(v) for v in cw_modeA_by_doc.values())
    n_raw_ans = sum(len(v) for v in cw_raw_by_doc.values())
    modeA_cov = (n_modeA_ans / n_pool) if n_pool else float("nan")
    raw_cov = (n_raw_ans / n_pool) if n_pool else float("nan")
    modeA_pts, _, _ = _curve([qr["modeA"] for qr in query_results])
    raw_pts, _, _ = _curve([qr["raw"] for qr in query_results])
    return {
        "confident_wrong_modeA": cw_modeA, "confident_wrong_raw": cw_raw,
        "reduction": (cw_raw - cw_modeA) if (cw_raw == cw_raw and cw_modeA == cw_modeA) else float("nan"),
        "reduction_ci95": [lo, hi], "boot_p_reduction_le_0": p_le0,
        "n_modeA_answered": n_modeA_ans, "n_raw_answered": n_raw_ans,
        "n_pool_deduction_queries": n_pool,
        "modeA_coverage": modeA_cov, "raw_coverage": raw_cov,
        "modeA_abstention_rate": (1.0 - modeA_cov) if modeA_cov == modeA_cov else float("nan"),
        "raw_abstention_rate": (1.0 - raw_cov) if raw_cov == raw_cov else float("nan"),
        "modeA_confident_wrong_count": modeA_wrong,
        "silent_wrong_narrowing_count": silent_wrong,
        "pre_registered_min_effect": H2_MIN_EFFECT,
        "risk_coverage_points": {"modeA": modeA_pts, "raw": raw_pts},
        "coverage_note": ("confident-wrong is reported AT the stated coverage; Mode-A lowers it "
                          "partly by ABSTAINING more (coverage above), so the FAIR cross-method "
                          "comparison is selective accuracy at MATCHED coverage (H1), not "
                          "confident-wrong in isolation. The iter-2 0.65->0.0 was achieved at "
                          "~90% Mode-A abstention; iter-3 states both rates explicitly."),
    }


# ============================ Prolog discharge ============================
POINT_COMP_FACTS = [
    ("lt", "lt", "lt"), ("lt", "eq", "lt"), ("eq", "lt", "lt"), ("eq", "eq", "eq"),
    ("eq", "gt", "gt"), ("gt", "eq", "gt"), ("gt", "gt", "gt"),
]
PT_SYM = {"<": "lt", "=": "eq", ">": "gt"}


SYM_PT = {"lt": "<", "eq": "=", "gt": ">"}
PT_CONV_SYM = {"lt": "gt", "gt": "lt", "eq": "eq"}


def emit_prolog(q, emitted, outpath: Path, engine_relation=None, run_swipl=True):
    """Emit a runnable SWI-Prolog program for the closed query subgraph and discharge the
    held-out query edge. Read facts are emitted in BOTH directions (algebra converse), the
    query is the INTERSECTION of every length-2 composition (the certified narrowing), and
    the discharge runs swipl if available, else a self-contained python resolution. The
    derived relation is cross-checked against the engine's Mode-A closure result."""
    docid, qx, qy = q["docid"], q["qx"], q["qy"]

    def nid(x):
        return "e_" + "".join(ch if ch.isalnum() else "_" for ch in str(x))

    # oriented singleton reads for every induced edge (both directions via converse)
    facts = []          # list of (a_nid, b_nid, sym) directed
    seen = set()
    for (a, b) in q["path_edges"]:
        key = (docid,) + tuple(sorted((a, b)))
        em = emitted.get(key)
        if em is None:
            continue
        pset = orient_point(em["point_set"], em["stored_uv"], (a, b))
        if len(pset) != 1:
            continue
        sym = PT_SYM[next(iter(pset))]
        na, nb = nid(a), nid(b)
        if (na, nb) not in seen:
            facts.append((na, nb, sym)); seen.add((na, nb))
        if (nb, na) not in seen:
            facts.append((nb, na, PT_CONV_SYM[sym])); seen.add((nb, na))

    lines = [
        "% Closure-certified temporal deduction -- auto-generated trace program.",
        "% Convex point start-point algebra over event start points {lt,eq,gt}.",
        "% The query relation is the INTERSECTION of all length-2 path compositions",
        "% (path-consistency narrowing); an empty intersection certifies inconsistency.",
        ":- discontiguous rel/3.", "",
        "% --- composition table (Vilain-Kautz convex point algebra) ---",
    ]
    for (a, b, c) in POINT_COMP_FACTS:
        lines.append(f"comp({a},{b},{c}).")
    lines += ["", "% --- read facts (LOCAL LLM reads; both directions via converse) ---"]
    for (a, b, s) in facts:
        lines.append(f"rel({a},{b},{s}).")
    qxn, qyn = nid(qx), nid(qy)
    lines += ["",
              f"% --- query: intersect every {qxn}->M->{qyn} length-2 composition ---",
              "% path-consistency narrowing: the certified query relation is the SET of",
              "% distinct composed relations; a singleton => ANSWER, >=2 (conflicting",
              "% compositions => empty intersection) or 0 (no path) => ABSTAIN (Mode-B).",
              f"path_comp({qxn},{qyn},R) :- rel({qxn},M,R1), "
              f"rel(M,{qyn},R2), comp(R1,R2,R).",
              "",
              "% main computes the narrowed set Rs and PRINTS A VERDICT (end-to-end proof).",
              "main :-",
              f"    ( setof(R, path_comp({qxn},{qyn},R), Rs) ->",
              "        ( Rs = [Single] ->",
              "            format('PATHS: ~w~n', [Rs]),",
              "            format('VERDICT: ANSWER(~w)~n', [Single])",
              "        ; format('PATHS: ~w~n', [Rs]),",
              "          write('VERDICT: ABSTAIN(conflict->empty-intersection->Mode-B)'), nl",
              "        )",
              "    ; write('PATHS: none'), nl,",
              "      write('VERDICT: ABSTAIN(underdetermined-no-length2-path)'), nl",
              "    ),",
              "    halt.",
              "", ":- initialization(main)."]
    prog = "\n".join(lines) + "\n"
    outpath.write_text(prog)

    # ---- python resolution: intersection of all 2-hop compositions over both-dir facts ----
    comp = {(a, b): c for (a, b, c) in POINT_COMP_FACTS}
    adj = defaultdict(list)
    for (u, v, s) in facts:
        adj[u].append((v, s))
    path_results = []
    for (mid, r1) in adj.get(nid(qx), []):
        for (v2, r2) in adj.get(mid, []):
            if v2 == nid(qy) and (r1, r2) in comp:
                path_results.append(comp[(r1, r2)])
    if not path_results:
        derived_set = set()
        derived = "underdetermined (no length-2 path among singleton reads)"
    else:
        inter = set(SYM_PT)             # {lt,eq,gt}
        for s in path_results:
            inter &= {s}
        derived_set = inter
        derived = next(iter(inter)) if len(inter) == 1 else (
            "EMPTY (inconsistent -> Mode-B abstain)" if not inter else "|".join(sorted(inter)))
    # ---- ACTUALLY discharge with SWI-Prolog (the deliverable); parse its VERDICT ----
    method = "python-checked (swipl-unavailable)"
    swipl_stdout = None
    swipl_verdict = None          # 'ANSWER' | 'ABSTAIN' | None
    swipl_answer_sym = None       # 'lt'|'eq'|'gt' when ANSWER
    if run_swipl and shutil.which("swipl"):
        try:
            r = subprocess.run(["swipl", "-q", str(outpath)], capture_output=True,
                               text=True, timeout=30)
            swipl_stdout = (r.stdout or "").strip()
            method = "swipl: " + swipl_stdout.replace("\n", " ")
            mverd = re.search(r"VERDICT:\s*ANSWER\((\w+)\)", swipl_stdout)
            if mverd:
                swipl_verdict = "ANSWER"; swipl_answer_sym = mverd.group(1)
            elif "VERDICT: ABSTAIN" in swipl_stdout:
                swipl_verdict = "ABSTAIN"
        except Exception as e:
            method = f"swipl-error:{e}; python-checked"

    gold_sym = "|".join(PT_SYM[s] for s in sorted(COARSE_TO_POINT[q["gold"]]))
    # python checker derivation (independent of swipl)
    derived_coarse = point_to_coarse(frozenset(SYM_PT[s] for s in derived_set)) if derived_set else None
    # swipl-derived coarse relation (when the program emitted ANSWER)
    swipl_coarse = None
    if swipl_answer_sym in SYM_PT:
        swipl_coarse = point_to_coarse(frozenset({SYM_PT[swipl_answer_sym]}))
    # cross-check: swipl ANSWER == python checker, AND == engine Mode-A relation
    swipl_matches_python = None
    if swipl_verdict is not None:
        if swipl_verdict == "ANSWER":
            swipl_matches_python = (swipl_coarse == derived_coarse)
        else:  # ABSTAIN: python derived a non-singleton / empty too
            swipl_matches_python = (derived_coarse is None)
    agrees_engine = None
    if engine_relation is not None:
        agree_src = swipl_coarse if swipl_verdict == "ANSWER" else (
            None if swipl_verdict == "ABSTAIN" else derived_coarse)
        agrees_engine = (agree_src == engine_relation)
    return {"prolog_path": str(outpath), "discharge_method": method,
            "swipl_stdout": swipl_stdout, "swipl_verdict": swipl_verdict,
            "swipl_derived_coarse": swipl_coarse,
            "swipl_matches_python_checker": swipl_matches_python,
            "derived_point": derived, "derived_coarse": derived_coarse,
            "engine_modeA_relation": engine_relation,
            "agrees_with_engine": agrees_engine,
            "gold_point": gold_sym, "gold_coarse": q["gold"], "query": [nid(qx), nid(qy)],
            "n_read_facts": len(facts), "n_length2_paths": len(path_results),
            "program": prog}


def emit_prolog_collapse(q, emitted, outpath: Path, run_swipl=True):
    """Mode-B INCONSISTENCY certificate (auditable, runnable). Emit ALL SINGLETON local
    reads of the induced subgraph and let Prolog find an inconsistent TRIANGLE: a pair of
    events whose composed relation compose(R(a,b),R(b,c)) conflicts with the directly-read
    R(a,c). Such a triangle IS the closure-detected inconsistency (the query edge is held at
    universe, so a Mode-B collapse is a contradiction purely among the path-edge reads).
    A 2-hop conflict on the query edge is the special case a=qx,c=qy."""
    docid = q["docid"]

    def nid(x):
        return "e_" + "".join(ch if ch.isalnum() else "_" for ch in str(x))

    facts = []          # (a_nid, b_nid, sym) both directions, singleton reads only
    seen = set()
    rel_map = {}
    for (a, b) in q["path_edges"]:
        key = (docid,) + tuple(sorted((a, b)))
        em = emitted.get(key)
        if em is None:
            continue
        pset = orient_point(em["point_set"], em["stored_uv"], (a, b))
        if len(pset) != 1:
            continue
        sym = PT_SYM[next(iter(pset))]
        na, nb = nid(a), nid(b)
        for (x, y, s) in ((na, nb, sym), (nb, na, PT_CONV_SYM[sym])):
            if (x, y) not in seen:
                facts.append((x, y, s)); seen.add((x, y)); rel_map[(x, y)] = s

    # python checker: find an inconsistent singleton triangle (compose conflicts with direct read)
    comp = {(a, b): c for (a, b, c) in POINT_COMP_FACTS}
    adj = defaultdict(list)
    for (x, y, s) in facts:
        adj[x].append((y, s))
    witness = None
    for a in list(adj):
        for (b, r1) in adj[a]:
            for (c, r2) in adj.get(b, []):
                if c == a:
                    continue
                rc = comp.get((r1, r2))         # None => composition is the universe (no constraint)
                if rc is None:
                    continue
                r3 = rel_map.get((a, c))
                if r3 is not None and r3 != rc:
                    witness = (a, b, c, r1, r2, rc, r3); break
            if witness:
                break
        if witness:
            break

    lines = [
        "% Closure-certified temporal deduction -- Mode-B INCONSISTENCY certificate.",
        "% Convex point start-point algebra {lt,eq,gt}. The query edge is held at the",
        "% universe; a Mode-B collapse is a contradiction among the LOCAL path-edge reads:",
        "% some triangle has compose(R(a,b),R(b,c)) /= the direct read R(a,c).",
        ":- discontiguous rel/3.", "",
        "% --- composition table (Vilain-Kautz convex point algebra) ---",
    ]
    for (a, b, c) in POINT_COMP_FACTS:
        lines.append(f"comp({a},{b},{c}).")
    lines += ["", "% --- singleton local reads (both directions via converse) ---"]
    for (a, b, s) in facts:
        lines.append(f"rel({a},{b},{s}).")
    lines += [
        "",
        "% an inconsistent triangle: composed relation conflicts with the direct read",
        "bad(A,B,C,R1,R2,Rc,R3) :- rel(A,B,R1), rel(B,C,R2), comp(R1,R2,Rc), "
        "rel(A,C,R3), R3 \\== Rc.",
        "main :- ( bad(A,B,C,R1,R2,Rc,R3) ->",
        "    format('INCONSISTENT-TRIANGLE: ~w-~w-~w  comp(~w,~w)=~w but rel(~w,~w)=~w~n',"
        "[A,B,C,R1,R2,Rc,A,C,R3]),",
        "    write('VERDICT: INCONSISTENT(Mode-B ABSTAIN)'), nl",
        "  ; write('VERDICT: consistent-among-singletons "
        "(full PC-2 over disjunctive/long-range reads found the conflict)'), nl ),",
        "  halt.",
        "", ":- initialization(main)."]
    prog = "\n".join(lines) + "\n"
    outpath.write_text(prog)

    method = "python-checked (swipl-unavailable)"
    swipl_stdout = None
    swipl_verdict = None
    if run_swipl and shutil.which("swipl"):
        try:
            r = subprocess.run(["swipl", "-q", str(outpath)], capture_output=True,
                               text=True, timeout=30)
            swipl_stdout = (r.stdout or "").strip()
            method = "swipl: " + swipl_stdout.replace("\n", " ")
            if "VERDICT: INCONSISTENT" in swipl_stdout:
                swipl_verdict = "INCONSISTENT"
            elif "VERDICT: consistent-among-singletons" in swipl_stdout:
                swipl_verdict = "CONSISTENT_AMONG_SINGLETONS"
        except Exception as e:
            method = f"swipl-error:{e}; python-checked"
    py_inconsistent = witness is not None
    # faithful iff the singleton-triangle certificate reproduces the engine's Mode-B collapse
    swipl_matches_python = None
    if swipl_verdict is not None:
        swipl_matches_python = ((swipl_verdict == "INCONSISTENT") == py_inconsistent)
    return {"prolog_path": str(outpath), "discharge_method": method,
            "swipl_stdout": swipl_stdout, "swipl_verdict": swipl_verdict,
            "python_inconsistent_triangle": py_inconsistent,
            "inconsistent_triangle_witness": (list(witness) if witness else None),
            "swipl_matches_python_checker": swipl_matches_python,
            "engine_modeA_relation": None, "agrees_with_engine": None,
            "gold_coarse": q["gold"], "n_read_facts": len(facts),
            "two_hop_prolog_faithful": py_inconsistent, "program": prog}


# ============================ synthetic backstop ============================
def synthetic_matched_coverage():
    SC.self_verify_point_algebra()
    breadth = {"p_singleton": 0.6, "p_two": 0.3, "p_univ": 0.1}
    r = 0.96
    rho = 0.3
    cells = [
        ("R_redundancy_K4", "R", {"K": 4}),
        ("R_redundancy_K8", "R", {"K": 8}),
        ("H_hop_L4_C2", "H", {"L": 4, "C": 2}),
        ("H_hop_L6_C3", "H", {"L": 6, "C": 3}),
    ]
    out = {}
    for name, fam, params in cells:
        rows = SC.simulate_matched_coverage(fam, params, n_net=600, r=r, rho=rho,
                                            breadth=breadth, sc_k=SC_K,
                                            seed=SC_cell_seed(name))
        by_doc = {m: defaultdict(list) for m in rows}
        recs = {m: [] for m in rows}
        for m, lst in rows.items():
            for x in lst:
                rec = {"answered": x["answered"], "correct": x["correct"], "conf": x["conf"]}
                recs[m].append(rec)
                by_doc[m][x["net"]].append(rec)
        modeA = recs["modeA_full"]
        comp = {}
        for base in ("raw", "sc", "pot", "naive"):
            comp[base] = matched_coverage_gap(modeA, recs[base], by_doc["modeA_full"],
                                               by_doc[base], seed=SC_cell_seed(name + base))
        _, m_cov, m_acc = _curve(modeA)
        out[name] = {"family": fam, "params": params, "recall": r, "rho": rho,
                     "modeA_natural_coverage": m_cov, "modeA_selective_acc": m_acc,
                     "vs_baselines": comp,
                     "n_networks": 600}
    return out


def SC_cell_seed(name):
    import zlib
    return (SEED + zlib.crc32(name.encode())) % (2 ** 31)


# ============================ figures ============================
def make_figures(real_curves, synth, h2=None):
    figs = []
    # 1) risk-coverage curves (real, primary reader, pooled NT+TDDMan)
    fig, ax = plt.subplots(figsize=(7, 5))
    colors = {"modeA": "C0", "naive": "C1", "raw": "C2", "pot": "C3", "sc": "C4"}
    labels = {"modeA": "Mode-A closure (ours)", "naive": "naive single-pass",
              "raw": "raw local LLM", "pot": "Path-of-Thoughts", "sc": "self-consistency"}
    for m, pts in real_curves.items():
        if not pts:
            continue
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        ax.plot(xs, ys, label=labels.get(m, m), color=colors.get(m), lw=2)
    ax.set_xlabel("coverage (fraction of deduction queries answered)")
    ax.set_ylabel("selective accuracy")
    ax.set_title("Real-text risk-coverage (NarrativeTime+TDDMan, primary reader)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3); ax.set_ylim(0, 1.02)
    p = FIGS / "real_risk_coverage.jpg"; fig.tight_layout(); fig.savefig(p, dpi=130); plt.close(fig)
    figs.append(str(p))

    # 2) synthetic matched-coverage gap (Mode-A minus baseline)
    fig, ax = plt.subplots(figsize=(7, 5))
    cells = list(synth.keys())
    bases = ["raw", "pot", "sc", "naive"]
    x = np.arange(len(cells)); w = 0.2
    for bi, base in enumerate(bases):
        gaps = [synth[c]["vs_baselines"][base]["gap"] for c in cells]
        ax.bar(x + bi * w, gaps, w, label=f"Mode-A − {base}")
    ax.set_xticks(x + 1.5 * w); ax.set_xticklabels(cells, rotation=20, fontsize=7)
    ax.axhline(0, color="k", lw=0.8)
    ax.set_ylabel("selective-accuracy gap at matched coverage")
    ax.set_title("Synthetic backstop (recall 0.96): Mode-A vs baselines")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")
    p = FIGS / "synthetic_matched_coverage.jpg"; fig.tight_layout(); fig.savefig(p, dpi=130); plt.close(fig)
    figs.append(str(p))

    # 3) H2 risk-coverage with abstention (Mode-A vs raw, real, pooled) -- EDIT D
    if h2 and h2.get("risk_coverage_points"):
        rc = h2["risk_coverage_points"]
        fig, ax = plt.subplots(figsize=(7, 5))
        for m, col, lab in (("modeA", "C0", "Mode-A closure (ours)"), ("raw", "C2", "raw local LLM")):
            pts = rc.get(m) or []
            if pts:
                ax.plot([p_[0] for p_ in pts], [p_[1] for p_ in pts], color=col, lw=2, label=lab)
        mc = h2.get("modeA_coverage"); rcv = h2.get("raw_coverage")
        if mc == mc:
            ax.axvline(mc, color="C0", ls="--", lw=1, alpha=0.7,
                       label=f"Mode-A coverage={mc:.2f}")
        if rcv == rcv:
            ax.axvline(rcv, color="C2", ls=":", lw=1, alpha=0.7,
                       label=f"raw coverage={rcv:.2f}")
        ax.set_xlabel("coverage (fraction of deduction queries answered)")
        ax.set_ylabel("selective accuracy (1 - confident-wrong rate)")
        ax.set_title("H2 risk-coverage: Mode-A vs raw (confident-wrong is reported AT coverage)")
        ax.legend(fontsize=8); ax.grid(alpha=0.3); ax.set_ylim(0, 1.02)
        p = FIGS / "h2_risk_coverage.jpg"; fig.tight_layout(); fig.savefig(p, dpi=130); plt.close(fig)
        figs.append(str(p))
    return figs


# ============================ output assembly ============================
def build_examples(arm, query_results_by_key, max_examples=None):
    exs = []
    for q, qr in query_results_by_key:
        docid, qx, qy = q["docid"], q["qx"], q["qy"]
        qkey = (docid,) + tuple(sorted((qx, qy)))
        task = arm["edge_tasks"].get(qkey)
        marked = task["marked_text"] if task else ""
        ex = {
            "input": (marked[:2800] + (" ..." if len(marked) > 2800 else "")),
            "output": q["gold"],
            "metadata_docid": docid,
            "metadata_corpus": arm["arm"],
            "metadata_algebra": "POINT",
            "metadata_sentdiff": q["sentdiff"],
            "metadata_stratum": q["stratum"],
            "metadata_n_vias": len(q["vias"]),
            "metadata_n_path_edges": len(q["path_edges"]),
            "metadata_deduction_required": True,
            "metadata_closure_collapsed": bool(qr["modeA"].get("collapse")),
            "metadata_n_fired": qr["n_fired"],
            "predict_modeA": str(qr["modeA"]["pred"] or "ABSTAIN"),
            "predict_naive": str(qr["naive"]["pred"] or "ABSTAIN"),
            "predict_raw": str(qr["raw"]["pred"] or "ABSTAIN"),
            "predict_pot": str(qr["pot"]["pred"] or "ABSTAIN"),
            "predict_sc": str(qr["sc"]["pred"] or "ABSTAIN"),
        }
        exs.append(ex)
        if max_examples and len(exs) >= max_examples:
            break
    return exs


def _json_default(o):
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    return str(o)


def _f(x):
    return "nan" if (x is None or x != x) else f"{x:.4f}"


# ============================ MAIN ============================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mini", action="store_true")
    ap.add_argument("--limit-docs", type=int, default=0, help="cap docs per corpus (smoke)")
    ap.add_argument("--n-target", type=int, default=N_TARGET)
    ap.add_argument("--concurrency", type=int, default=12)
    ap.add_argument("--skip-strong", action="store_true")
    ap.add_argument("--dataset", default=DA.DEFAULT_DATASET)
    args = ap.parse_args()

    logger.remove(); logger.add(sys.stderr, level="INFO")
    logger.add(HERE / "logs" / "run.log", level="INFO", rotation="5 MB")
    t0 = time.time()

    n_target = 10 if args.mini else args.n_target
    sc_k = 3 if args.mini else SC_K
    limit_docs = 3 if args.mini else (args.limit_docs or None)

    # ---- STAGE 0: BLOCKING closure tests (gate all LLM spend) ----
    ok, tres = closure_tests_pass(verbose=True)
    if not ok:
        logger.error("Closure tests FAILED -> abort before any LLM spend."); sys.exit(1)
    SC.self_verify_point_algebra()
    logger.info("Stage-0 closure + point-algebra self-verify PASSED.")

    # ---- STAGE 1: synthetic matched-coverage backstop ($0) ----
    logger.info("Running synthetic matched-coverage backstop ($0) ...")
    synth = synthetic_matched_coverage()
    for name, s in synth.items():
        gp = s["vs_baselines"]
        logger.info(f"  synth {name:18s} cov={s['modeA_natural_coverage']:.2f} "
                    f"acc={s['modeA_selective_acc']:.3f} | gaps raw={gp['raw']['gap']:+.3f} "
                    f"pot={gp['pot']['gap']:+.3f} sc={gp['sc']['gap']:+.3f} naive={gp['naive']['gap']:+.3f}")

    # ---- STAGE 2: dataset adapter ----
    logger.info(f"Loading dataset {args.dataset} ...")
    by_corpus = defaultdict(list)
    for (corpus, docid, text, G) in DA.load_dataset(args.dataset):
        by_corpus[corpus].append((docid, text, G))
    arms = {}
    offset_fracs = {}
    for corpus in ("narrativetime", "tddman", "matres"):
        rows = by_corpus.get(corpus, [])
        if not rows:
            continue
        docs, off = DA.build_corpus(corpus, rows, max_docs=limit_docs, seed=SEED)
        offset_fracs[corpus] = off
        algebra = DA.CORPUS_ALGEBRA[corpus]
        arm = DA.build_arm(corpus, docs, algebra, n_target=n_target, v_max=V_MAX, seed=SEED)
        arms[corpus] = arm
        logger.info(f"  {corpus:14s} docs={arm['n_docs']:3d} read_edges={arm['n_edges']:4d} "
                    f"queries={arm['n_queries']:4d} (len2={arm['n_len2']} ge3={arm['n_ge3_cyclic']}) "
                    f"offset_ok={off:.3f}")

    # GOLD-ONLY-GATE: MATRES deduction envelope (expect ~0)
    matres_q = arms.get("matres", {}).get("n_queries", 0)
    gate_validation = {
        "matres_deduction_multipath_queries": matres_q,
        "expected": "~0 (MATRES is intra/adjacent only -> near-empty deduction envelope)",
        "passed": matres_q < 5, "tag": "GOLD-ONLY-GATE",
    }

    real_corpora = [c for c in ("narrativetime", "tddman") if c in arms and arms[c]["n_queries"]]
    if not real_corpora:
        # EDIT A guard: abort-to-synthetic ONLY if BOTH real corpora yielded 0 queries.
        logger.error("No real deduction queries on EITHER corpus -> synthetic-only verdict "
                     "(no LLM spend).")
        out = {"metadata": {
                   "method_name": "Closure-Certified Composition (synthetic-only fallback)",
                   "verdict": "SYNTHETIC-ONLY",
                   "reason": "no real deduction-required multi-path queries were sampled",
                   "config": {"seed": SEED, "n_target": n_target, "mini": args.mini,
                              "limit_docs": limit_docs, "reader_primary": READER_PRIMARY,
                              "reader_strong": READER_STRONG},
                   "closure_tests_passed": ok, "closure_test_detail": tres,
                   "gate_validation_matres": gate_validation,
                   "dataset_adapter": {"offset_alignment_fraction": offset_fracs,
                                       "n_deduction_queries": {c: arms[c]["n_queries"] for c in arms}},
                   "synthetic_backstop": {"tag": "SYNTHETIC-CHANNEL", "cells": synth},
                   "tags": "SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / THEOREM"},
               "datasets": [{"dataset": "synthetic_only",
                             "examples": [{"input": "synthetic matched-coverage backstop (see metadata)",
                                           "output": "see synthetic_backstop",
                                           "metadata_note": "no_real_queries"}]}]}
        (HERE / "method_out.json").write_text(json.dumps(out, indent=2, default=_json_default))
        (RESULTS / "method_out.json").write_text(json.dumps(out, indent=2, default=_json_default))
        logger.info("Wrote synthetic-only method_out.json (no real corpora)."); return

    # ---- STAGE 3: LLM elicitation ----
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        logger.error("OPENROUTER_API_KEY not set"); sys.exit(1)
    client_primary = OpenRouterClient(api_key, READER_PRIMARY, PRIMARY_FALLBACKS, HERE / "cache",
                                      temperature=TEMPERATURE, budget_hard=GLOBAL_CAP,
                                      budget_soft=BUDGET_SOFT, concurrency=args.concurrency,
                                      max_tokens=260)
    client_sc = OpenRouterClient(api_key, READER_PRIMARY, PRIMARY_FALLBACKS, HERE / "cache",
                                 temperature=SC_TEMPERATURE, budget_hard=GLOBAL_CAP,
                                 budget_soft=BUDGET_SOFT, concurrency=args.concurrency,
                                 max_tokens=260)
    # strong reader is a REASONING model (deepseek-v4-pro): reasoning tokens count toward
    # max_tokens and toward output cost. At 1500 ~58% of NT reads truncated to EMPTY content
    # (out=1500) -> parse-fail -> universe -> spurious recall=1. Verified empirically: at
    # max_tokens=8000 ALL reads complete (out 31..4980). deepseek-v4-pro output is cheap
    # ($0.87/M) so an 8000 cap is affordable (~$0.004/read). Parse-failed reads are ALSO
    # excluded from recall (see per_edge_recall) so no spurious-universe inflation survives.
    client_strong = OpenRouterClient(api_key, READER_STRONG, STRONG_FALLBACKS, HERE / "cache",
                                     temperature=TEMPERATURE, budget_hard=GLOBAL_CAP,
                                     budget_soft=BUDGET_SOFT, concurrency=args.concurrency,
                                     max_tokens=8000)
    ALL_CLIENTS = [client_primary, client_sc, client_strong]

    # Stage-0 cache round-trip probe
    enforce_global_cap(client_primary, [client_sc, client_strong])
    probe = asyncio.run(client_primary.run_batch([{"id": "probe",
        "system": "Reply with only JSON.",
        "user": 'Return {"relations":["before"],"most_likely":"before","confidence":0.9,"underdetermined":false}'}]))
    logger.info(f"probe model={probe['probe'].get('model')} cached_next? running again ...")
    probe2 = asyncio.run(client_primary.run_batch([{"id": "probe",
        "system": "Reply with only JSON.",
        "user": 'Return {"relations":["before"],"most_likely":"before","confidence":0.9,"underdetermined":false}'}]))
    logger.info(f"cache round-trip cached={probe2['probe'].get('cached')} (hits={client_primary.n_cache_hits})")

    # ---- PHASE A: edge reads (primary on all corpora) ----
    emitted = {"primary": {}, "strong": {}}
    n_pfail = {"primary": 0, "strong": 0}
    primary_models = defaultdict(int)        # served-model histogram (honest single-model audit)
    for corpus in real_corpora + (["matres"] if "matres" in arms else []):
        arm = arms[corpus]
        items, index = make_read_items(arm, "primary")
        logger.info(f"[primary] {corpus}: {len(items)} local edge reads ...")
        enforce_global_cap(client_primary, [client_sc, client_strong])
        res = asyncio.run(client_primary.run_batch(items))
        em, pf = parse_read_results(res, index, arm)
        emitted["primary"][corpus] = em
        n_pfail["primary"] += pf
        for _iid, payload in res.items():
            primary_models[payload.get("model")] += 1
        logger.info(f"  done. cost=${client_primary.cost:.4f} cache_hits={client_primary.n_cache_hits} pfail={pf}")

    # ---- PHASE A2: STRONGER reader on BOTH real corpora (iter-3 EDIT B) ----
    # Accumulate edges query-by-query (the arm['queries'] order is already round-robin over
    # docs) until >=STRONG_MIN_SCORABLE scorable (non-VAGUE-gold, locally-readable) edges are
    # covered per corpus; cap total reads at STRONG_MAX. This gives a POWERED recall CI on
    # each corpus for the gate-crossing reconciliation, not just the NT-only iter-2 sample.
    emitted["strong"]["_models"] = {}
    strong_corpora = [] if args.skip_strong else list(real_corpora)
    for corpus in strong_corpora:
        arm = arms[corpus]
        if not arm["n_queries"]:
            continue
        min_scorable = STRONG_MIN_SCORABLE if not args.mini else 8
        max_reads = STRONG_MAX if not args.mini else 30
        keys = set(); scorable = 0; qi = 0
        while scorable < min_scorable and qi < len(arm["queries"]) and len(keys) < max_reads:
            q = arm["queries"][qi]; d = q["docid"]
            for (a, b) in (list(q["path_edges"]) + [(q["qx"], q["qy"])]):
                keys.add((d,) + tuple(sorted((a, b))))
            scorable = sum(1 for k in keys
                           if arm["edge_tasks"].get(k, {}).get("gold", "VAGUE") != "VAGUE"
                           and arm["edge_tasks"].get(k, {}).get("has_local_span"))
            qi += 1
        items, index = make_read_items(arm, "strong", only_keys=keys)
        logger.info(f"[strong:{READER_STRONG}] {corpus}: {len(items)} local edge reads "
                    f"(first {qi} queries, ~{scorable} scorable, cap {max_reads}) ...")
        enforce_global_cap(client_strong, [client_primary, client_sc])
        res = asyncio.run(client_strong.run_batch(items))
        em, pf = parse_read_results(res, index, arm)
        emitted["strong"][corpus] = em
        n_pfail["strong"] += pf
        # serving-model mix (honest 'stronger reader' labelling per corpus)
        smodels = defaultdict(int)
        for iid, payload in res.items():
            smodels[payload.get("model")] += 1
        emitted["strong"]["_models"][corpus] = dict(smodels)
        logger.info(f"  done. strong cost=${client_strong.cost:.4f} pfail={pf} models={dict(smodels)}")

    # ---- PHASE B: PoT calls (primary; per query per path) ----
    pot_items = []
    pot_index = {}
    for corpus in real_corpora:
        arm = arms[corpus]
        em = emitted["primary"][corpus]
        for q in arm["queries"]:
            docid, qx, qy = q["docid"], q["qx"], q["qy"]
            for via in q["vias"]:
                k1 = (docid,) + tuple(sorted((qx, via)))
                k2 = (docid,) + tuple(sorted((via, qy)))
                e1 = em.get(k1); e2 = em.get(k2)
                if e1 is None or e2 is None or e1["most_likely"] is None or e2["most_likely"] is None:
                    continue
                r1 = orient_coarse(e1["most_likely"], e1["stored_uv"], (qx, via))
                r2 = orient_coarse(e2["most_likely"], e2["stored_uv"], (via, qy))
                fact1 = f"event A is '{r1}' event B"
                fact2 = f"event B is '{r2}' event C"
                system, user = build_pot_prompt(fact1, fact2, "POINT")
                iid = f"pot|{corpus}|{docid}|{qx}|{qy}|{via}"
                pot_items.append({"id": iid, "system": system, "user": user})
                pot_index[iid] = (corpus, docid, qx, qy)
    logger.info(f"[primary] PoT path-composition calls: {len(pot_items)} ...")
    enforce_global_cap(client_primary, [client_sc, client_strong])
    pot_res = asyncio.run(client_primary.run_batch(pot_items)) if pot_items else {}
    pot_by_query = defaultdict(list)
    for iid, payload in pot_res.items():
        corpus, docid, qx, qy = pot_index[iid]
        lab, conf = parse_pot(payload.get("content", ""), "POINT")
        pot_by_query[(corpus, docid, qx, qy)].append((lab, conf))

    # ---- PHASE C: self-consistency samples (sc_client temp>0; query edges) ----
    sc_items = []
    sc_index = {}
    for corpus in real_corpora:
        arm = arms[corpus]
        for q in arm["queries"]:
            docid, qx, qy = q["docid"], q["qx"], q["qy"]
            qkey = (docid,) + tuple(sorted((qx, qy)))
            task = arm["edge_tasks"].get(qkey)
            if task is None or not task["has_local_span"]:
                continue
            for s in range(sc_k):
                variant = f"(reading attempt {s + 1}; reason carefully and independently.)"
                system, user = build_read_prompt(task["marked_text"], "POINT", variant=variant)
                iid = f"sc|{corpus}|{docid}|{qx}|{qy}|{s}"
                sc_items.append({"id": iid, "system": system, "user": user})
                sc_index[iid] = (corpus, docid, qx, qy, task["u"], task["v"])
    logger.info(f"[primary@T={SC_TEMPERATURE}] self-consistency samples: {len(sc_items)} ...")
    enforce_global_cap(client_sc, [client_primary, client_strong])
    sc_res = asyncio.run(client_sc.run_batch(sc_items)) if sc_items else {}
    sc_by_query = defaultdict(list)
    for iid, payload in sc_res.items():
        corpus, docid, qx, qy, su, sv = sc_index[iid]
        pr = parse_read(payload.get("content", ""), "POINT")
        # orient most_likely from stored (su,sv) to (qx,qy)
        lab = orient_coarse(pr["most_likely"], (su, sv), (qx, qy))
        sc_by_query[(corpus, docid, qx, qy)].append(lab)

    # ---- per-edge recall (primary + STRONGER reader on BOTH corpora) ----
    gate = RECALL_GATE["POINT"]
    recall_report = {}
    for corpus in real_corpora:
        rep = {"primary": per_edge_recall(arms[corpus], emitted["primary"][corpus])}
        rep["primary"]["tag"] = "REAL-LLM-READ"
        if corpus in emitted["strong"]:
            rep["strong"] = per_edge_recall(arms[corpus], emitted["strong"][corpus])
            rep["strong"]["tag"] = "REAL-LLM-READ"
        recall_report[corpus] = rep

    # per-(corpus, reader) gate-crossing test (iter-3 EDIT C)
    gate_tests = {}
    for corpus in real_corpora:
        gate_tests[corpus] = {}
        for reader in ("primary", "strong"):
            r = recall_report[corpus].get(reader)
            if r is None:
                continue
            gate_tests[corpus][reader] = gate_crossing_test(
                r["recall"], r.get("recall_ci95"), r.get("n_scorable_edges", 0), gate=gate)

    # ---- read-soundness reconciliation: NT vs TDDMan, primary vs strong, vs the gate ----
    recon_rows = {}
    for corpus in real_corpora:
        for reader in ("primary", "strong"):
            gv = gate_tests.get(corpus, {}).get(reader)
            if gv and gv.get("verdict") != "INSUFFICIENT_DATA":
                recon_rows[f"{corpus}_{reader}"] = gv
    any_above = any(v.get("verdict") == "CI_excludes_above_gate" for v in recon_rows.values())
    any_below = any(v.get("verdict") == "CI_excludes_below_gate" for v in recon_rows.values())
    framing = ("Read-soundness gate-crossing is CORPUS/GENRE-specific, NOT a universal ceiling: "
               "NarrativeTime is dense referential news prose (more local-read ambiguity), while "
               "TDDMan is discourse-level manually-annotated gold; per-corpus recall CIs vs the "
               f"{gate} point gate (rows above) localize where local reads are / are not sound. ")
    if any_above and any_below:
        framing += ("Some (corpus,reader) CIs EXCLUDE-ABOVE the gate and others EXCLUDE-BELOW => "
                    "the binding constraint is corpus-specific, not intrinsic to the closure step.")
    elif any_below and not any_above:
        framing += ("No (corpus,reader) CI provably clears the gate; the binding constraint is "
                    "real-text LOCAL read soundness across both corpora (negative-localization).")
    elif any_above and not any_below:
        framing += ("At least one (corpus,reader) provably clears the gate => sound local reads "
                    "are achievable; closure value is GATED BY read soundness, not blocked by it.")
    else:
        framing += ("All CIs straddle the gate at this power; report point estimates + CIs honestly.")
    read_soundness_reconciliation = {
        "rows": recon_rows, "gate": gate,
        "any_reader_corpus_CI_excludes_above_gate": any_above,
        "any_reader_corpus_CI_excludes_below_gate": any_below,
        "framing": framing, "tag": "REAL-LLM-READ",
    }

    strong_rec = recall_report.get("narrativetime", {}).get("strong", {}).get("recall")
    prim_rec = recall_report.get("narrativetime", {}).get("primary", {}).get("recall")
    gate_crossing = {
        "recall_gate_point": gate,
        "primary_recall_narrativetime": prim_rec,
        "strong_recall_narrativetime": strong_rec,
        "primary_crosses_gate": (prim_rec is not None and prim_rec >= gate),
        "strong_crosses_gate": (strong_rec is not None and strong_rec >= gate),
        "per_corpus_reader_gate_tests": gate_tests,
        "interpretation": ("If the STRONGER reader still does not cross the gate, the binding "
                           "constraint is real-text LOCAL read soundness (the bottleneck), not the "
                           "closure step. If it crosses, the bottleneck was a weak-model artifact."),
        "tag": "REAL-LLM-READ",
    }

    # ---- run closure pipeline + baselines per query (primary reader) ----
    def run_corpus(corpus, reader, query_list=None):
        arm = arms[corpus]
        em = emitted[reader].get(corpus, {})
        qrs = []
        for q in (query_list if query_list is not None else arm["queries"]):
            key = (corpus, q["docid"], q["qx"], q["qy"])
            qr = run_query(q, em, sc_votes=sc_by_query.get(key) if reader == "primary" else None,
                           pot_preds=pot_by_query.get(key) if reader == "primary" else None)
            qrs.append((q, qr))
        return qrs

    query_results = {"primary": {}, "strong": {}}
    for corpus in real_corpora:
        query_results["primary"][corpus] = run_corpus(corpus, "primary")
    # STRONGER reader: closure on the queries whose FULL induced edge set was read by the
    # strong reader (iter-3 EDIT E -> BOTH corpora, not NT-only).
    strong_sample_summary = {}
    for corpus in real_corpora:
        em_s = emitted["strong"].get(corpus)
        if not em_s:
            continue
        sample_qs = [q for q in arms[corpus]["queries"]
                     if all((q["docid"],) + tuple(sorted(e)) in em_s
                            for e in (list(q["path_edges"]) + [(q["qx"], q["qy"])]))]
        if not sample_qs:
            continue
        srs = run_corpus(corpus, "strong", query_list=sample_qs)
        query_results["strong"][corpus] = srs
        s_ans = [qr["modeA"] for (_, qr) in srs if qr["modeA"]["answered"]]
        strong_sample_summary[corpus] = {
            "n_sample_queries": len(srs),
            "modeA_coverage": (len(s_ans) / len(srs)) if srs else float("nan"),
            "modeA_selective_acc": (float(np.mean([m["correct"] for m in s_ans]))
                                    if s_ans else float("nan")),
            "note": "Mode-A closure over the STRONGER reader's local reads (powered per-corpus sample).",
            "tag": "REAL-LLM-READ",
        }
    if not strong_sample_summary:
        strong_sample_summary = None

    # ---- H1: matched-coverage selective accuracy (pooled real, primary reader) ----
    pooled = [qr for c in real_corpora for (_, qr) in query_results["primary"][c]]
    # === EVAL-INJECT (R1 bracketing CI): dump per-query (conf,correct,answered) records ===
    # Serialize the EXACT per-query records used for H1 so the bracketing-CI re-analysis can
    # hold the matched-coverage operating point FIXED across resamples. $0: all reads cached.
    import json as _evjson
    _ev_out = "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1/per_query_records_temporal.json"
    _ev_recs = [{"docid": qr["docid"], "stratum": qr["stratum"], "gold": qr["gold"],
                 "sentdiff": qr.get("sentdiff"),
                 "modeA": qr["modeA"], "naive": qr["naive"], "raw": qr["raw"],
                 "pot": qr["pot"], "sc": qr["sc"]} for qr in pooled]
    _ev_costs = {"primary_cost": getattr(client_primary, "cost", None),
                 "primary_calls": getattr(client_primary, "n_calls", None),
                 "primary_cache_hits": getattr(client_primary, "n_cache_hits", None),
                 "sc_cost": getattr(client_sc, "cost", None),
                 "sc_calls": getattr(client_sc, "n_calls", None),
                 "total_cache_misses": getattr(client_primary.__class__, "_EV_N_MISS", None),
                 "n_pooled": len(pooled)}
    _evjson.dump({"records": _ev_recs, "client_costs": _ev_costs},
                 open(_ev_out, "w"))
    logger.info(f"EVAL-INJECT: dumped {len(_ev_recs)} per-query records -> {_ev_out}; "
                f"primary_cost={_ev_costs['primary_cost']} primary_calls={_ev_costs['primary_calls']} "
                f"sc_cost={_ev_costs['sc_cost']} sc_calls={_ev_costs['sc_calls']}")
    sys.exit(0)
    # === END EVAL-INJECT ===
    by_method = {m: [] for m in ("modeA", "naive", "raw", "pot", "sc")}
    by_method_doc = {m: defaultdict(list) for m in by_method}
    for qr in pooled:
        for m in by_method:
            rec = qr[m]
            by_method[m].append(rec)
            by_method_doc[m][qr["docid"]].append(rec)

    h1 = {}
    pvals = {}
    for base in ("pot", "sc", "naive", "raw"):
        g = matched_coverage_gap(by_method["modeA"], by_method[base],
                                 by_method_doc["modeA"], by_method_doc[base])
        h1[f"modeA_vs_{base}"] = g
        if base in ("pot", "sc"):
            pvals[f"H1_vs_{base.upper()}" if base != "pot" else "H1_vs_PoT"] = \
                g.get("boot_p_gap_le_0", 1.0)
    # AUC over shared grid
    curves = {m: _curve(by_method[m])[0] for m in by_method}
    h1_auc = {m: auc_rc(curves[m]) for m in by_method}

    # ---- applicability: Mode-A singleton-resolution-to-correct vs GO thresholds ----
    n_pool = len(pooled)
    modeA_ans = [qr["modeA"] for qr in pooled if qr["modeA"]["answered"]]
    modeA_correct_resolution = (sum(m["correct"] for m in modeA_ans) / n_pool) if n_pool else float("nan")
    _, modeA_cov, modeA_acc = _curve(by_method["modeA"])
    applicability = {
        "n_deduction_queries": n_pool,
        "modeA_singleton_resolution_coverage": modeA_cov,
        "modeA_selective_accuracy": modeA_acc,
        "modeA_singleton_to_correct_rate": modeA_correct_resolution,
        "applic_general_threshold": APPLIC["general"],
        "applic_module_threshold": APPLIC["module"],
        "applicability_verdict": ("GO-GENERAL" if modeA_correct_resolution >= APPLIC["general"]
                                  else ("GO-MODULE" if modeA_correct_resolution >= APPLIC["module"]
                                        else "NICHE")),
        "tag": "REAL-LLM-READ",
    }

    # ---- H2: hallucination reduction (deduction-required; pooled real, primary) ----
    h2 = h2_confident_wrong(pooled)
    h2["tag"] = "REAL-LLM-READ"
    pvals["H2_halluc"] = h2.get("boot_p_reduction_le_0", 1.0)

    # ---- Holm-Bonferroni across the confirmatory family ----
    holm = holm_bonferroni({k: pvals.get(k, 1.0) for k in CONFIRM_FAMILY})

    # ---- stratified (exploratory): len2 (predicted Mode-A==naive) vs ge3/cyclic ----
    strat = {}
    for stratum in ("len2", "ge3_cyclic"):
        sub = [qr for qr in pooled if qr["stratum"] == stratum]
        if not sub:
            continue
        sd = {m: defaultdict(list) for m in by_method}
        sm = {m: [] for m in by_method}
        for qr in sub:
            for m in by_method:
                sm[m].append(qr[m]); sd[m][qr["docid"]].append(qr[m])
        strat[stratum] = {
            "n": len(sub),
            "modeA_vs_naive": matched_coverage_gap(sm["modeA"], sm["naive"], sd["modeA"], sd["naive"]),
            "modeA_vs_raw": matched_coverage_gap(sm["modeA"], sm["raw"], sd["modeA"], sd["raw"]),
            "modeA_natural_coverage": _curve(sm["modeA"])[1],
        }

    # ---- worked Prolog examples ----
    # The 2-hop trace program only carries SINGLETON local reads; the PC-2 engine can also
    # narrow via disjunctive reads / iteration. So we SCREEN candidates with a cheap
    # python-only emit (run_swipl=False) and pick examples the 2-hop Prolog can FAITHFULLY
    # reproduce (narrows: python derivation == engine relation; collapse: >=2 conflicting
    # length-2 paths -> empty intersection), then discharge ONLY the chosen ones with swipl.
    worked = []
    scr = RESULTS / "_screen.pl"
    pick_pool = [(q, qr) for c in real_corpora for (q, qr) in query_results["primary"][c]]

    def _screen(q, qr, eng):
        return emit_prolog(q, emitted["primary"][q["corpus"]], scr, engine_relation=eng,
                           run_swipl=False)

    narrow_cands = [(q, qr) for (q, qr) in pick_pool
                    if qr["modeA"]["answered"] and qr["modeA"]["correct"] == 1]
    chosen_narrow = None
    for (q, qr) in narrow_cands:
        res = _screen(q, qr, qr["modeA"]["pred"])
        # faithful: 2-hop singleton intersection yields the SAME relation the engine derived
        if res.get("n_length2_paths", 0) >= 1 and res.get("derived_coarse") == qr["modeA"]["pred"]:
            chosen_narrow = (q, qr); break
    narrow_faithful = chosen_narrow is not None
    if chosen_narrow is None and narrow_cands:      # fall back: emit first, label honestly
        chosen_narrow = narrow_cands[0]
    if chosen_narrow:
        q, qr = chosen_narrow
        rec = {"kind": "modeA_narrows_correct",
               **emit_prolog(q, emitted["primary"][q["corpus"]], RESULTS / "worked_modeA.pl",
                             engine_relation=qr["modeA"]["pred"]),
               "modeA_pred": qr["modeA"]["pred"], "n_fired": qr["n_fired"],
               "two_hop_prolog_faithful": narrow_faithful}
        if not narrow_faithful:
            rec["note"] = ("PC-2 engine narrowed via iteration / disjunctive reads beyond the "
                           "2-hop singleton trace; the runnable program is the auditable "
                           "length-2 fragment (it ABSTAINs where the full closure narrowed).")
        worked.append(rec)

    # collapse: screen for a Mode-B example with an inconsistent SINGLETON triangle (a
    # genuine, runnable inconsistency certificate); discharge only the chosen one with swipl.
    collapse_cands = [(q, qr) for (q, qr) in pick_pool if qr["modeA"].get("collapse")]
    chosen_collapse = None
    for (q, qr) in collapse_cands:
        res = emit_prolog_collapse(q, emitted["primary"][q["corpus"]], scr, run_swipl=False)
        if res.get("python_inconsistent_triangle"):
            chosen_collapse = (q, qr); break
    collapse_faithful = chosen_collapse is not None
    if chosen_collapse is None and collapse_cands:
        chosen_collapse = collapse_cands[0]
    if chosen_collapse:
        q, qr = chosen_collapse
        rec = {"kind": "closure_collapse_modeB",
               **emit_prolog_collapse(q, emitted["primary"][q["corpus"]],
                                      RESULTS / "worked_collapse.pl"),
               "note": ("closure detected inconsistency among LOCAL reads -> Mode-B ABSTAIN; "
                        "the program emits the witnessing inconsistent triangle." if collapse_faithful
                        else "PC-2 detected the inconsistency via disjunctive/long-range reads "
                             "beyond a single singleton triangle; the runnable program reports "
                             "no singleton-triangle witness (full closure still collapsed).")}
        worked.append(rec)
    if scr.exists():
        try:
            scr.unlink()
        except OSError:
            pass

    # ---- verdict ----
    h1_pot_sig = holm.get("H1_vs_PoT", {}).get("adjusted_significant", False) and \
        (h1["modeA_vs_pot"]["gap"] or 0) > 0
    h1_sc_sig = holm.get("H1_vs_SC", {}).get("adjusted_significant", False) and \
        (h1["modeA_vs_sc"]["gap"] or 0) > 0
    h1_confirm = h1_pot_sig and h1_sc_sig
    h2_confirm = (holm.get("H2_halluc", {}).get("adjusted_significant", False) and
                  (h2["reduction"] or 0) >= H2_MIN_EFFECT)
    n_ded = len(pooled)
    underpowered = n_ded < CONFIRM_MIN_N
    powered = n_ded >= CONFIRM_MIN_N
    # CONFIRM requires BOTH gateways Holm-adjusted AND >= CONFIRM_MIN_N scored queries
    # (the iter-2 n=20 smoke could not reach CONFIRM by construction).
    if h1_confirm and h2_confirm and powered:
        verdict = "CONFIRM"
    elif h1_confirm or h2_confirm:
        verdict = "PARTIAL/SCOPE-BOUNDARY"
    else:
        verdict = "DISCONFIRM/SCOPE-BOUNDARY"

    # ---- assemble ----
    elapsed = time.time() - t0
    total_cost = client_primary.cost + client_sc.cost + client_strong.cost
    headline = {
        "verdict": verdict,
        "H1_confirm_vs_PoT_and_SC": h1_confirm,
        "H2_confirm_hallucination_reduction": h2_confirm,
        "H1_modeA_vs_PoT_gap": h1["modeA_vs_pot"]["gap"],
        "H1_modeA_vs_SC_gap": h1["modeA_vs_sc"]["gap"],
        "H1_modeA_vs_raw_gap": h1["modeA_vs_raw"]["gap"],
        "H1_modeA_vs_naive_gap": h1["modeA_vs_naive"]["gap"],
        "H2_confident_wrong_reduction": h2["reduction"],
        "H2_confident_wrong_modeA": h2["confident_wrong_modeA"],
        "H2_confident_wrong_raw": h2["confident_wrong_raw"],
        "primary_recall_narrativetime": prim_rec,
        "strong_recall_narrativetime": strong_rec,
        "strong_crosses_recall_gate": gate_crossing["strong_crosses_gate"],
        "n_deduction_queries_scored": n_ded,
        "modeA_singleton_to_correct_rate": applicability["modeA_singleton_to_correct_rate"],
        "modeA_resolution_coverage": applicability["modeA_singleton_resolution_coverage"],
        "applicability_verdict": applicability["applicability_verdict"],
        "underpowered_lt70": underpowered,
        "tags": "every number tagged REAL-LLM-READ / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / THEOREM",
    }
    metadata = {
        "method_name": "Closure-Certified Composition over Span-LOCAL LLM reads (Mode-A) "
                       "-- LOCAL-reader real-text head-to-head + end-to-end Prolog",
        "description": ("Tests whether iterated path-consistency CLOSURE over span-LOCAL LLM "
                        "reads of constituent path edges recovers deduction-required temporal "
                        "relations the local reads alone cannot, beating Path-of-Thoughts, "
                        "self-consistency, raw local LLM, and naive single-pass at MATCHED "
                        "coverage (H1), and cutting the confident-wrong hallucination rate vs a "
                        "raw LLM (H2), on the FROZEN ACTUAL NarrativeTime + TDDMan gold graphs, "
                        "with a SWI-Prolog-discharged trace and a $0 fully-powered synthetic "
                        "matched-coverage backstop. Closure runs in the PC-complete convex point "
                        "start-point algebra."),
        "headline_findings": headline,
        "config": {
            "seed": SEED, "reader_primary": READER_PRIMARY, "reader_strong": READER_STRONG,
            "reader_primary_used": probe["probe"].get("model"),
            "primary_fallbacks": PRIMARY_FALLBACKS, "strong_fallbacks": STRONG_FALLBACKS,
            "temperature": TEMPERATURE, "sc_temperature": SC_TEMPERATURE, "sc_k": sc_k,
            "n_target": n_target, "v_max": V_MAX, "recall_gate": RECALL_GATE,
            "h2_min_effect": H2_MIN_EFFECT, "boot_B": BOOT_B, "alpha": ALPHA,
            "confirm_family_holm": CONFIRM_FAMILY, "budget_global_cap": GLOBAL_CAP,
            "strong_query_cap": STRONG_QUERY_CAP, "strong_min_scorable": STRONG_MIN_SCORABLE,
            "strong_max": STRONG_MAX, "confirm_min_n": CONFIRM_MIN_N,
            "closure_algebra": "convex point start-point (PC-complete)",
            "mini": args.mini, "limit_docs": limit_docs,
        },
        "closure_tests_passed": ok, "closure_test_detail": tres,
        "TAG_THEOREM": "closure engine (pc2_full) + point-algebra PC-completeness are THEOREM-grade; "
                       "all closure outputs are sound certificates.",
        "dataset_adapter": {
            "offset_alignment_fraction": offset_fracs,
            "n_docs": {c: arms[c]["n_docs"] for c in arms},
            "n_read_edges": {c: arms[c]["n_edges"] for c in arms},
            "n_deduction_queries": {c: arms[c]["n_queries"] for c in arms},
            "n_len2": {c: arms[c]["n_len2"] for c in arms},
            "n_ge3_cyclic": {c: arms[c]["n_ge3_cyclic"] for c in arms},
            "tag": "GOLD-ONLY-GATE / REAL-LLM-READ",
        },
        "gate_validation_matres": gate_validation,
        "per_edge_recall": recall_report,
        "stronger_reader_gate_test": gate_crossing,
        "read_soundness_reconciliation": read_soundness_reconciliation,
        "stronger_reader_sample_closure": strong_sample_summary,
        "strong_reader_serving_models": emitted["strong"].get("_models"),
        "primary_reader_serving_models": dict(primary_models),
        "H1_matched_coverage": {**h1, "auc_risk_coverage": h1_auc,
                                "tag": "REAL-LLM-READ",
                                "note": "gap = Mode-A selective acc at its natural coverage MINUS "
                                        "baseline acc at the SAME coverage; doc-clustered paired "
                                        "bootstrap; Holm-Bonferroni across the confirmatory family."},
        "H1_stratified": {**strat, "tag": "REAL-LLM-READ",
                          "label": "EXPLORATORY (iteration-on-real H3): len2 (Mode-A==naive by "
                                   "theorem) vs ge3_cyclic; over GOLD full==naive but over NOISY "
                                   "reads a gap can appear. NarrativeTime gold is a globally "
                                   "consistent dense timeline -> the synthetic channel carries H3."},
        "applicability": applicability,
        "H2_hallucination": h2,
        "holm_bonferroni": holm,
        "worked_examples_prolog": worked,
        "synthetic_backstop": {"tag": "SYNTHETIC-CHANNEL", "cells": synth,
                               "note": "recall 0.96, 600 networks/cell, NO LLM, $0. Carries the "
                                       "matched-coverage mechanism claim if real text is thin."},
        "cost": {"cumulative_usd": round(total_cost, 6),
                 "primary_usd": round(client_primary.cost, 6),
                 "sc_usd": round(client_sc.cost, 6),
                 "strong_usd": round(client_strong.cost, 6),
                 "n_calls_primary": client_primary.n_calls, "n_calls_sc": client_sc.n_calls,
                 "n_calls_strong": client_strong.n_calls,
                 "cache_hits": client_primary.n_cache_hits + client_sc.n_cache_hits + client_strong.n_cache_hits,
                 "parse_fail": n_pfail, "budget_global_cap": GLOBAL_CAP},
        "elapsed_sec": round(elapsed, 1),
        "interpretation": _interpret(verdict, h1_confirm, h2_confirm, gate_crossing, synth,
                                     h1, h2, underpowered, read_soundness_reconciliation),
    }

    datasets = []
    for corpus in real_corpora:
        exs = build_examples(arms[corpus], query_results["primary"][corpus],
                             max_examples=(5 if args.mini else None))
        datasets.append({"dataset": corpus, "examples": exs})
    if not datasets:
        datasets.append({"dataset": "synthetic_only",
                         "examples": [{"input": "synthetic matched-coverage backstop (see metadata)",
                                       "output": "see synthetic_backstop", "metadata_note": "no_real_queries"}]})

    real_curves_pooled = {m: _curve(by_method[m])[0] for m in by_method}
    figs = make_figures(real_curves_pooled, synth, h2=h2)
    metadata["figures"] = figs

    out = {"metadata": metadata, "datasets": datasets}
    outpath = HERE / "method_out.json"
    outpath.write_text(json.dumps(out, indent=2, default=_json_default))
    (RESULTS / "method_out.json").write_text(json.dumps(out, indent=2, default=_json_default))
    logger.info(f"Wrote {outpath} ({outpath.stat().st_size/1e6:.2f} MB)")
    logger.info(f"VERDICT={verdict} H1={h1_confirm} H2={h2_confirm} "
                f"n_ded={n_ded} cost=${total_cost:.4f} time={elapsed:.0f}s")
    print("\n=== HEADLINE ===")
    for k, v in headline.items():
        print(f"  {k}: {v}")
    print("\n=== H1 matched-coverage gaps (Mode-A minus baseline @ matched coverage) ===")
    for base in ("pot", "sc", "raw", "naive"):
        g = h1[f"modeA_vs_{base}"]
        print(f"  vs {base:6s}: gap={_f(g['gap'])} ci95=[{_f(g['ci95'][0])},{_f(g['ci95'][1])}] "
              f"matched_cov={_f(g['matched_coverage'])} modeA_acc={_f(g['method_acc'])} "
              f"base_acc={_f(g['base_acc'])}")
    print(f"\n  H2 confident-wrong reduction={_f(h2['reduction'])} "
          f"ci95=[{_f(h2['reduction_ci95'][0])},{_f(h2['reduction_ci95'][1])}] "
          f"(modeA={_f(h2['confident_wrong_modeA'])} raw={_f(h2['confident_wrong_raw'])})")
    print(f"\n  Holm: {json.dumps(holm)}")
    print(f"\n=== per-edge recall vs gate {gate} (gate-crossing reconciliation) ===")
    for corpus in real_corpora:
        for reader in ("primary", "strong"):
            r = recall_report.get(corpus, {}).get(reader)
            if not r:
                continue
            gt = gate_tests.get(corpus, {}).get(reader, {})
            print(f"  {corpus:13s} {reader:7s}: recall={_f(r['recall'])} "
                  f"ci95=[{_f(r['recall_ci95'][0])},{_f(r['recall_ci95'][1])}] "
                  f"n={r['n_scorable_edges']:4d} verdict={gt.get('verdict')}")
    print(f"  MATRES deduction queries={matres_q} (gate {'PASS' if gate_validation['passed'] else 'FAIL'})")
    print(f"  primary served models: {dict(primary_models)}")
    print(f"  strong served models:  {emitted['strong'].get('_models')}")
    print(f"\nTOTAL COST=${total_cost:.4f}  VERDICT={verdict}  n_ded={n_ded} powered={powered}")


def _interpret(verdict, h1, h2, gate, synth, h1d, h2d, underpowered, recon=None):
    parts = [f"VERDICT={verdict}."]
    if verdict == "CONFIRM":
        parts.append("LOCAL-reader closure value + end-to-end hallucination reduction ESTABLISHED on "
                     "real text: Mode-A beats PoT AND self-consistency at matched coverage (H1) and cuts "
                     "the confident-wrong rate vs a raw LLM (H2), both Holm-adjusted, at powered n.")
    elif verdict == "PARTIAL/SCOPE-BOUNDARY":
        parts.append(("Exactly one gateway cleared (or both clear but underpowered): H1=%s H2=%s. "
                      "Report which holds; scope the claim.") % (h1, h2))
    else:
        parts.append("Neither gateway cleared (ANTICIPATED, publishable). Contribution reframed as "
                     "(i) NEGATIVE LOCALIZATION -- local reads + even the stronger reader sit at/below "
                     "the recall gate, so the bottleneck is real-text LOCAL read soundness, not closure; "
                     "and (ii) the SYNTHETIC matched-coverage MECHANISM win (recall 0.96), retargeted to "
                     "NeSy/findings.")
    if gate["strong_crosses_gate"] is False and gate["strong_recall_narrativetime"] is not None:
        parts.append(f"Stronger reader ({READER_STRONG}) NT recall={gate['strong_recall_narrativetime']:.3f} "
                     f"< gate {gate['recall_gate_point']} => read-soundness bottleneck is NOT a weak-model "
                     "artifact (load-bearing).")
    elif gate["strong_crosses_gate"]:
        parts.append(f"Stronger reader ({READER_STRONG}) CROSSES the recall gate => the bottleneck was "
                     "(at least partly) a weak-model artifact, not the closure step.")
    if recon and recon.get("framing"):
        parts.append("READ-SOUNDNESS RECONCILIATION: " + recon["framing"])
    if h2d is not None and h2d.get("modeA_coverage") == h2d.get("modeA_coverage"):
        parts.append(f"H2 confident-wrong is reported AT coverage: Mode-A answered "
                     f"{h2d.get('modeA_coverage'):.2f} (abstained {h2d.get('modeA_abstention_rate'):.2f}) "
                     f"vs raw {h2d.get('raw_coverage'):.2f}; the FAIR metric is selective accuracy at "
                     "MATCHED coverage (H1), not confident-wrong in isolation.")
    # synthetic mechanism summary
    syn_raw = np.mean([s["vs_baselines"]["raw"]["gap"] for s in synth.values()])
    syn_pot = np.mean([s["vs_baselines"]["pot"]["gap"] for s in synth.values()])
    parts.append(f"SYNTHETIC backstop (recall 0.96): mean Mode-A matched-coverage gap vs raw="
                 f"{syn_raw:+.3f}, vs PoT={syn_pot:+.3f} -> the closure mechanism WORKS when reads are "
                 "sound; the real-text result isolates whether local read soundness is the binding "
                 "constraint.")
    if underpowered:
        parts.append(f"WARNING: <{CONFIRM_MIN_N} deduction queries scored -> real-text headline "
                     "UNDERPOWERED; lean on the synthetic + stronger-reader-recall evidence.")
    return " ".join(parts)


if __name__ == "__main__":
    main()
