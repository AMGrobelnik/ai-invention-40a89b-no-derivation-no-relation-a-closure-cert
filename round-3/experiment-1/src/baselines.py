#!/usr/bin/env python3
"""Symbolic predictions + the matched-coverage / risk-coverage analysis machinery.

* predict_symbolic     -- Mode-A (forward-closure) and naive single-pass predictions
                          from the EXTRACTED atomic edges, with graded confidence and
                          a surface answer realized with the GOLD target gender
                          (entity grounding / gender is NOT the contribution).
* atomic_pr            -- direction-aware typed atomic-extraction precision/recall/F1
                          vs gold edges, with doc-clustered CI + hop/noise breakdown.
* doc_clustered_paired_gap -- paired bootstrap of selective-accuracy gap RESAMPLING
                          DOCUMENTS (the matched-coverage showdown statistic).
* risk_coverage_curve  -- full confident-wrong-rate (and selective-accuracy) vs coverage.
* matched_coverage_point / present_selective -- scalar operating-point comparisons.
"""
from __future__ import annotations

from collections import defaultdict

import numpy as np

from kinship import query_modeA, query_naive
from stats import matched_coverage_mask, selective_accuracy


# --------------------------------------------------------------------------- #
# Symbolic predictions
# --------------------------------------------------------------------------- #
def predict_symbolic(kin, edges, qsrc, qtgt, genders) -> dict:
    """Return Mode-A and naive predictions as {surface, conf, named, answer_type, info}.

    conf is graded so coverage can be swept: singleton->1.0 ; conflict(|D|>1)->1/|D| ;
    no_path->0.0. A non-singleton Mode-A ABSTAINS (named=False) -- but we still record a
    forced representative surface so a risk-coverage sweep can push coverage above c*."""
    g = genders.get(qtgt, "male")
    a = query_modeA(kin, edges, qsrc, qtgt)
    if a["singleton"]:
        a_pred = {"surface": kin.surface(a["answer_type"], g), "conf": 1.0, "named": True,
                  "answer_type": a["answer_type"], "info": "singleton"}
    elif a["no_path"]:
        a_pred = {"surface": "no-relation", "conf": 0.0, "named": False,
                  "answer_type": None, "info": "no_path"}
    else:  # conflict |D|>1
        rep = a["answer_type"]
        a_pred = {"surface": kin.surface(rep, g), "conf": 1.0 / max(2, a["n_derivations"]),
                  "named": False, "answer_type": rep, "info": f"conflict:{kin.label(a['types'])}"}

    n = query_naive(kin, edges, qsrc, qtgt)
    if n["singleton"]:
        n_pred = {"surface": kin.surface(n["answer_type"], g), "conf": 1.0, "named": True,
                  "answer_type": n["answer_type"], "info": "singleton"}
    elif n["no_path"]:
        n_pred = {"surface": "no-relation", "conf": 0.0, "named": False,
                  "answer_type": None, "info": "no_path"}
    else:
        rep = n["answer_type"]
        n_pred = {"surface": kin.surface(rep, g), "conf": 1.0 / max(2, n["n_derivations"]),
                  "named": False, "answer_type": rep, "info": "conflict"}
    return {"modeA": a_pred, "naive": n_pred,
            "modeA_raw": a, "naive_raw": n}


# --------------------------------------------------------------------------- #
# (i) Atomic-extraction precision / recall (direction- and type-aware)
# --------------------------------------------------------------------------- #
def _norm_name(x):
    return str(x).strip().lower()


def story_atomic_pr(extracted_edges: list[dict], gold_edges: list[dict]) -> dict:
    """Direction-aware typed match of (a,type,b). Returns counts for this story."""
    gold = set()
    for e in gold_edges:
        gold.add((_norm_name(e["a"]), e["type"], _norm_name(e["b"])))
    pred = set()
    for e in extracted_edges:
        pred.add((_norm_name(e["a"]), e["type"], _norm_name(e["b"])))
    tp = len(pred & gold)
    n_pred = len(pred)
    n_gold = len(gold)
    return {"tp": tp, "n_pred": n_pred, "n_gold": n_gold}


def aggregate_atomic_pr(per_story: list[dict], doc_ids: list, hops: list, noises: list,
                        B: int = 1000, seed: int = 20260617) -> dict:
    """Micro P/R/F1 over all stories + doc-clustered bootstrap CI on F1, plus per-hop
    and per-noise_type breakdowns (micro). per_story[i] = story_atomic_pr output."""
    tp = sum(s["tp"] for s in per_story)
    np_ = sum(s["n_pred"] for s in per_story)
    ng = sum(s["n_gold"] for s in per_story)
    prec = tp / np_ if np_ else 0.0
    rec = tp / ng if ng else 0.0
    f1 = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0

    # doc-clustered bootstrap of micro precision / recall / f1
    by_doc = defaultdict(list)
    for i, d in enumerate(doc_ids):
        by_doc[d].append(i)
    docs = list(by_doc)
    rng = np.random.default_rng(seed)
    tps = np.array([s["tp"] for s in per_story], float)
    nps = np.array([s["n_pred"] for s in per_story], float)
    ngs = np.array([s["n_gold"] for s in per_story], float)
    boot_p, boot_r, boot_f = [], [], []
    nd = len(docs)
    for _ in range(B):
        pick = rng.integers(0, nd, nd)
        idx = np.concatenate([by_doc[docs[i]] for i in pick]) if nd else np.array([], int)
        if len(idx) == 0:
            continue
        t = tps[idx].sum(); p_ = nps[idx].sum(); gg = ngs[idx].sum()
        pp = t / p_ if p_ else 0.0
        rr = t / gg if gg else 0.0
        ff = (2 * pp * rr / (pp + rr)) if (pp + rr) else 0.0
        boot_p.append(pp); boot_r.append(rr); boot_f.append(ff)

    def ci(b):
        if len(b) < 10:
            return [float("nan"), float("nan")]
        lo, hi = np.quantile(np.array(b), [0.025, 0.975])
        return [float(lo), float(hi)]

    # breakdowns
    def breakdown(keys):
        agg = defaultdict(lambda: [0, 0, 0])
        for s, k in zip(per_story, keys):
            agg[k][0] += s["tp"]; agg[k][1] += s["n_pred"]; agg[k][2] += s["n_gold"]
        out = {}
        for k, (t, p_, gg) in sorted(agg.items(), key=lambda kv: str(kv[0])):
            pp = t / p_ if p_ else 0.0
            rr = t / gg if gg else 0.0
            ff = (2 * pp * rr / (pp + rr)) if (pp + rr) else 0.0
            out[str(k)] = {"precision": round(pp, 4), "recall": round(rr, 4),
                           "f1": round(ff, 4), "tp": t, "n_pred": p_, "n_gold": gg}
        return out

    return {"precision": round(prec, 4), "recall": round(rec, 4), "f1": round(f1, 4),
            "tp": tp, "n_pred": np_, "n_gold": ng, "n_stories": len(per_story),
            "precision_ci": ci(boot_p), "recall_ci": ci(boot_r), "f1_ci": ci(boot_f),
            "by_hop": breakdown(hops), "by_noise_type": breakdown(noises)}


# --------------------------------------------------------------------------- #
# Per-query correctness helpers (uniform over present & absent queries)
# --------------------------------------------------------------------------- #
def coverage_confidence(named: bool, conf: float) -> float:
    """Confidence used for COVERAGE ranking: an ABSTENTION is never 'covered', so its
    coverage-confidence is -1 (below any real [0,1] confidence). This prevents a method's
    confident *abstentions* from filling the coverage budget ahead of its lower-ranked
    *named* answers -- coverage counts only relations the method actually emits."""
    return float(conf) if named else -1.0


def query_correct(named: bool, surface, gold_surface: str, is_absent: bool) -> bool:
    """Correct = (named AND surface==gold) for present queries; (NOT named) for absent."""
    if is_absent:
        return not named
    return bool(named and surface == gold_surface)


def confident_wrong(named: bool, surface, gold_surface: str, is_absent: bool) -> bool:
    """A named answer that disagrees with gold (for absent, ANY named answer is wrong)."""
    if not named:
        return False
    if is_absent:
        return True
    return surface != gold_surface


# --------------------------------------------------------------------------- #
# Matched-coverage selective accuracy (doc-clustered paired bootstrap)
# --------------------------------------------------------------------------- #
def doc_clustered_paired_gap(correct_a, mask_a, correct_b, mask_b, doc_ids,
                             B: int = 2000, seed: int = 20260617, alpha: float = 0.05) -> dict:
    """Paired bootstrap of selacc(A)-selacc(B) at FIXED masks, RESAMPLING DOCUMENTS.

    correct_*: 0/1 arrays over queries; mask_*: bool covered-sets (fixed on full sample)."""
    correct_a = np.asarray(correct_a, float); correct_b = np.asarray(correct_b, float)
    mask_a = np.asarray(mask_a, bool); mask_b = np.asarray(mask_b, bool)
    sa = selective_accuracy(correct_a, mask_a)
    sb = selective_accuracy(correct_b, mask_b)
    point = (sa - sb) if (sa == sa and sb == sb) else float("nan")
    by_doc = defaultdict(list)
    for i, d in enumerate(doc_ids):
        by_doc[d].append(i)
    docs = list(by_doc)
    nd = len(docs)
    rng = np.random.default_rng(seed)
    gaps = []
    for _ in range(B):
        pick = rng.integers(0, nd, nd)
        idx = np.concatenate([by_doc[docs[i]] for i in pick]) if nd else np.array([], int)
        if len(idx) == 0:
            continue
        sai = selective_accuracy(correct_a[idx], mask_a[idx])
        sbi = selective_accuracy(correct_b[idx], mask_b[idx])
        if sai == sai and sbi == sbi:
            gaps.append(sai - sbi)
    gaps = np.array(gaps, float)
    if len(gaps) < 10:
        return {"gap": point, "ci95": [float("nan"), float("nan")], "p_one_sided": float("nan"),
                "selacc_a": sa, "selacc_b": sb, "cov_a": float(mask_a.mean()),
                "cov_b": float(mask_b.mean()), "n_boot": int(len(gaps))}
    lo, hi = np.quantile(gaps, [alpha / 2, 1 - alpha / 2])
    p_one = float(np.mean(gaps <= 0.0))
    p_one = max(p_one, 1.0 / (len(gaps) + 1))  # honest floor: p<1/B, never exactly 0
    return {"gap": float(point), "ci95": [float(lo), float(hi)], "p_one_sided": p_one,
            "selacc_a": float(sa), "selacc_b": float(sb),
            "cov_a": float(mask_a.mean()), "cov_b": float(mask_b.mean()),
            "n_boot": int(len(gaps))}


def matched_coverage_showdown(records: list[dict], ref: str = "modeA",
                              baselines=("naive", "raw", "sc", "pot", "off"),
                              present_only: bool = True) -> dict:
    """At the REFERENCE method's natural coverage c*, threshold every baseline to c* and
    compute selective accuracy + doc-clustered paired gap. Present queries only by default
    (the deduction showdown). Returns leaderboard + per-baseline gap dicts."""
    recs = [r for r in records if (not present_only) or (not r["is_absent"])]
    if not recs:
        return {}
    doc_ids = [r["doc_id"] for r in recs]
    methods = [ref] + [b for b in baselines]
    # coverage-confidence (abstentions ranked below any named answer) + correctness arrays
    conf = {m: np.array([coverage_confidence(r[m]["named"], r[m]["conf"]) for r in recs], float)
            for m in methods}
    named = {m: np.array([r[m]["named"] for r in recs], bool) for m in methods}
    correct = {m: np.array([query_correct(r[m]["named"], r[m]["surface"],
                                          r["gold_surface"], r["is_absent"]) for r in recs], float)
               for m in methods}
    # reference covered set = where it NAMES a relation
    mask_ref = named[ref]
    cstar = float(mask_ref.mean())
    selacc_ref = selective_accuracy(correct[ref], mask_ref)
    leaderboard = {ref: {"coverage": cstar, "selective_accuracy": _r(selacc_ref),
                         "n_covered": int(mask_ref.sum())}}
    gaps = {}
    for b in baselines:
        # threshold baseline b to coverage c* by ranking on its confidence
        mask_b = matched_coverage_mask(conf[b], cstar)
        selacc_b = selective_accuracy(correct[b], mask_b)
        leaderboard[b] = {"coverage_matched": float(mask_b.mean()),
                          "natural_coverage": float(named[b].mean()),
                          "selective_accuracy": _r(selacc_b),
                          "n_covered": int(mask_b.sum())}
        gaps[b] = doc_clustered_paired_gap(correct[ref], mask_ref, correct[b], mask_b, doc_ids)
    return {"c_star": cstar, "ref": ref, "leaderboard": leaderboard, "gaps": gaps,
            "n_queries": len(recs)}


# --------------------------------------------------------------------------- #
# Accuracy / coverage vs chain length
# --------------------------------------------------------------------------- #
def accuracy_vs_hop(records: list[dict], methods=("modeA", "naive", "raw", "sc", "pot"),
                    present_only: bool = True) -> dict:
    recs = [r for r in records if (not present_only) or (not r["is_absent"])]
    by_hop = defaultdict(list)
    for r in recs:
        by_hop[r["hop"]].append(r)
    out = {}
    for hop in sorted(by_hop):
        rs = by_hop[hop]
        row = {"n": len(rs)}
        for m in methods:
            named = np.array([x[m]["named"] for x in rs], bool)
            corr = np.array([query_correct(x[m]["named"], x[m]["surface"],
                                           x["gold_surface"], x["is_absent"]) for x in rs], float)
            cov = float(named.mean())
            sel = float(corr[named].sum() / named.sum()) if named.sum() else float("nan")
            row[m] = {"coverage": _r(cov), "selective_accuracy": _r(sel)}
        # full-minus-naive coverage gap (the iteration signal)
        cov_full = row["modeA"]["coverage"]
        cov_naive = row["naive"]["coverage"]
        row["full_minus_naive_coverage_gap"] = _r((cov_full or 0) - (cov_naive or 0))
        out[str(hop)] = row
    return out


# --------------------------------------------------------------------------- #
# (iv) Risk-coverage curves + the H2 absent-relation operating point
# --------------------------------------------------------------------------- #
def risk_coverage_curve(records: list[dict], method: str, n_points: int = 21) -> dict:
    """Sweep confidence threshold; report (coverage, confident_wrong_rate_over_pool,
    selective_accuracy_over_present) at each operating point. coverage = fraction of the
    POOL that the method NAMES with conf>=tau."""
    N = len(records)
    if N == 0:
        return {"points": [], "n_pool": 0}
    rows = []
    for r in records:
        p = r[method]
        cw = confident_wrong(p["named"], p["surface"], r["gold_surface"], r["is_absent"])
        corr = query_correct(p["named"], p["surface"], r["gold_surface"], r["is_absent"])
        rows.append((p["conf"], bool(p["named"]), bool(cw), bool(corr), r["is_absent"]))
    taus = sorted({x[0] for x in rows} | {0.0, 1.0001}, reverse=True)
    pts = []
    for tau in taus:
        sel = [x for x in rows if x[1] and x[0] >= tau]   # named & conf>=tau
        n_named = len(sel)
        coverage = n_named / N
        cw_rate = sum(1 for x in sel if x[2]) / N
        present_named = [x for x in sel if not x[4]]
        sel_acc = (sum(1 for x in present_named if x[3]) / len(present_named)
                   if present_named else float("nan"))
        pts.append({"tau": _r(tau if tau <= 1 else 1.0), "coverage": _r(coverage),
                    "confident_wrong_rate": _r(cw_rate), "abstention": _r(1 - coverage),
                    "selective_accuracy_present": _r(sel_acc)})
    # thin to n_points by coverage
    pts = _thin_by_coverage(pts, n_points)
    return {"points": pts, "n_pool": N}


def _thin_by_coverage(pts, n_points):
    if len(pts) <= n_points:
        return pts
    # keep evenly spaced by coverage
    targets = np.linspace(0, 1, n_points)
    kept = []
    used = set()
    for t in targets:
        best = min(range(len(pts)), key=lambda i: abs(pts[i]["coverage"] - t))
        if best not in used:
            used.add(best); kept.append(pts[best])
    kept.sort(key=lambda p: p["coverage"])
    return kept


def absent_h2(records: list[dict], ref: str = "modeA", compare="raw",
              others=("sc", "pot", "naive")) -> dict:
    """Pre-registered H2 on the ABSENT pool: at MATCHED coverage = the compare method's
    natural named-rate, Mode-A confident-wrong rate must be >= 0.20 lower (doc-clustered
    bootstrap CI excluding 0). Reports the operating point for every method."""
    recs = [r for r in records if r["is_absent"]]
    if not recs:
        return {"n_absent": 0}
    doc_ids = [r["doc_id"] for r in recs]
    methods = [ref, compare] + list(others)
    conf = {m: np.array([coverage_confidence(r[m]["named"], r[m]["conf"]) for r in recs], float)
            for m in methods}
    cw = {m: np.array([confident_wrong(r[m]["named"], r[m]["surface"],
                                       r["gold_surface"], True) for r in recs], float)
          for m in methods}
    named = {m: np.array([r[m]["named"] for r in recs], bool) for m in methods}
    c_match = float(named[compare].mean())  # raw-LLM natural answer rate on absent pool
    # operating points at matched coverage c_match (rank-based)
    def cw_rate_at(m, c):
        mask = matched_coverage_mask(conf[m], c)
        return float((cw[m] * mask).sum() / len(recs)), mask
    ref_rate, mask_ref = cw_rate_at(ref, c_match)
    cmp_rate, mask_cmp = cw_rate_at(compare, c_match)
    # doc-clustered bootstrap of (compare_cw - ref_cw) at matched coverage (fixed masks)
    by_doc = defaultdict(list)
    for i, d in enumerate(doc_ids):
        by_doc[d].append(i)
    docs = list(by_doc); nd = len(docs)
    rng = np.random.default_rng(20260617)
    diffs = []
    cwc = cw[compare]; cwr = cw[ref]
    for _ in range(2000):
        pick = rng.integers(0, nd, nd)
        idx = np.concatenate([by_doc[docs[i]] for i in pick])
        n = len(idx)
        d_cmp = float((cwc[idx] * mask_cmp[idx]).sum() / n)
        d_ref = float((cwr[idx] * mask_ref[idx]).sum() / n)
        diffs.append(d_cmp - d_ref)
    diffs = np.array(diffs, float)
    lo, hi = np.quantile(diffs, [0.025, 0.975])
    point = cmp_rate - ref_rate
    p_one = float(np.mean(diffs <= 0.0))
    p_one = max(p_one, 1.0 / (len(diffs) + 1))  # honest floor: p<1/B, never exactly 0
    natural = {m: {"natural_named_rate": float(named[m].mean()),
                   "natural_confident_wrong_rate": float(cw[m].mean())} for m in methods}
    matched = {}
    for m in methods:
        rate, _ = cw_rate_at(m, c_match)
        matched[m] = {"confident_wrong_rate_at_matched_cov": _r(rate)}
    return {"n_absent": len(recs), "matched_coverage": _r(c_match),
            "ref": ref, "compare": compare,
            "confident_wrong_reduction": _r(point), "ci95": [_r(lo), _r(hi)],
            "p_one_sided": _r(p_one), "meets_0.20_bar": bool(point >= 0.20 and lo > 0.0),
            "ci_excludes_0": bool(lo > 0.0),
            "natural_operating_points": natural, "matched_operating_points": matched}


def _r(x, nd=4):
    try:
        if x != x:
            return float("nan")
        return round(float(x), nd)
    except (TypeError, ValueError):
        return x
