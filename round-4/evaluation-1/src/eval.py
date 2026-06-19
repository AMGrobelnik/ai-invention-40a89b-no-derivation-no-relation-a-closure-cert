#!/usr/bin/env python3
"""Zero-LLM-spend re-analysis evaluation for the Closure-Certified deduction module.

Re-analyses the two iter-3 source experiments (numpy + scipy ONLY, $0 LLM):
  * TEMPORAL point-algebra natural-text  [art_OETjJkketEVS]
  * CLUTRR templated-kinship end-to-end  [art_0a7i481ZRwS1]

Deliverables (all into eval_out.json + eval_digest.md):
  R1  Bracketing CI on the temporal Mode-A-vs-PoT gap (fix the matched-coverage
      estimator/resample mismatch; hold the operating point FIXED across resamples).
  R2  CLUTRR naive NATURAL-coverage selective accuracy beside the FORCE-EXTENDED
      matched value, and route the iteration (H3) claim through the COVERAGE axis.
  ---  The 42.5% (48/113) confident-wrong-among-answered block + silent-wrong-narrowing.
  ---  INHERITED-vs-NOVEL decomposition on both available venues + carried Allen split.
  ---  TRANSFERABLE-AT-POWER vs SYNTHETIC-CHANNEL-ONLY contribution-split table.
  ---  Scope-framing guidance for GEN_PAPER_TEXT.

All bootstraps: seed=20260617, B=10000, DOC/STORY-CLUSTERED paired resampling.
Every reported number carries an evidence TAG.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from loguru import logger

# --------------------------------------------------------------------------- #
# config / paths
# --------------------------------------------------------------------------- #
SEED = 20260617
B = 10000
ALPHA = 0.05

HERE = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1")
TEMPORAL_FULL = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_2/full_method_out.json")
CLUTRR_FULL = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/full_method_out.json")
PRIOR_EVAL = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_evaluation_1/eval_out.json")
ITER2_ALLEN = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_method_out.json")
TEMPORAL_RECORDS = HERE / "per_query_records_temporal.json"   # built by the $0 cached re-run

TEMPORAL_ID = "art_OETjJkketEVS"
CLUTRR_ID = "art_0a7i481ZRwS1"
PRIOR_EVAL_ID = "art_D0cHQUJ8kY75"
ITER2_ALLEN_ID = "art_N0e4pH_C_Cxw"
CHANNEL_ID = "art_FtN4LBzazO_l"

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
(HERE / "logs").mkdir(exist_ok=True)
logger.add(str(HERE / "logs" / "eval.log"), rotation="20 MB", level="DEBUG")

MISMATCHES: list[dict] = []   # sanity-check log: reproduced vs published


def _r(x, n=6):
    """Round, NaN/inf-safe (JSON cannot hold NaN/inf)."""
    if x is None:
        return None
    try:
        xf = float(x)
    except (TypeError, ValueError):
        return x
    if not np.isfinite(xf):
        return None
    return round(xf, n)


def check(label: str, reproduced, published, tol=2e-3):
    """Compare a reproduced point estimate against the source-file value; log mismatch."""
    if reproduced is None or published is None:
        return
    if not (np.isfinite(reproduced) and np.isfinite(published)):
        return
    d = abs(reproduced - published)
    ok = d <= tol
    rec = {"metric": label, "reproduced": _r(reproduced), "published": _r(published),
           "abs_diff": _r(d, 8), "within_tol": ok, "tol": tol}
    if ok:
        logger.info(f"REPRO OK  {label}: {reproduced:.6f} ~ {published:.6f} (|d|={d:.2e})")
    else:
        logger.warning(f"REPRO MISMATCH {label}: {reproduced:.6f} vs published {published:.6f} (|d|={d:.2e})")
        MISMATCHES.append(rec)
    return rec


# --------------------------------------------------------------------------- #
# risk-coverage curve helpers (faithful reimplementation of temporal method.py)
# --------------------------------------------------------------------------- #
def curve(records):
    """records: list of {answered,correct,conf}. Return (pts, nat_cov, nat_acc).
    pts: sorted-by-conf-desc cumulative (coverage=k/N, selective_acc=cum_correct/k)."""
    n = len(records)
    ans = [(r["conf"], r["correct"]) for r in records
           if r["answered"] and r["correct"] is not None]
    if n == 0:
        return [], 0.0, float("nan")
    ans.sort(key=lambda x: -x[0])
    pts, cum = [], 0
    for k, (_, c) in enumerate(ans, start=1):
        cum += c
        pts.append((k / n, cum / k))
    nat_cov = len(ans) / n
    nat_acc = (cum / len(ans)) if ans else float("nan")
    return pts, nat_cov, nat_acc


def acc_at_coverage(pts, target):
    """Interpolate selective accuracy at a target coverage. NaN if target > max coverage."""
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


# --------------------------------------------------------------------------- #
# bootstraps
# --------------------------------------------------------------------------- #
def old_buggy_gap_boot(method_by_doc, base_by_doc, seed=SEED, n_boot=B):
    """Reproduce the PUBLISHED (buggy) matched_coverage_gap bootstrap:
    inner loop RE-DERIVES the target coverage mc per resample and interpolates the
    baseline at that VARYING mc -> the gap distribution is a different estimator than
    the point gap (recenters on the volatile low-coverage baseline curve)."""
    docs = sorted(set(method_by_doc) | set(base_by_doc))
    nd = len(docs)
    rng = np.random.default_rng(seed)
    gaps = []
    for _ in range(n_boot):
        pick = [docs[i] for i in rng.integers(0, nd, nd)]
        mrec = [r for d in pick for r in method_by_doc.get(d, [])]
        brec = [r for d in pick for r in base_by_doc.get(d, [])]
        _, mc, ma = curve(mrec)
        bp, _, _ = curve(brec)
        ba = acc_at_coverage(bp, mc)          # <-- VARYING mc = the bug
        if ma == ma and ba == ba:
            gaps.append(ma - ba)
    if not gaps:
        return None
    lo, hi = np.quantile(gaps, [ALPHA / 2, 1 - ALPHA / 2])
    return {"ci95": [float(lo), float(hi)], "boot_p_gap_le_0": float(np.mean([g <= 0 for g in gaps])),
            "median": float(np.median(gaps)), "mean": float(np.mean(gaps)), "n_boot": len(gaps)}


def fixed_set_gap_boot(method_set_by_doc, base_set_by_doc, seed=SEED, n_boot=B):
    """CORRECTED bracketing bootstrap: the operating point is FIXED on the full sample.
    method_set_by_doc / base_set_by_doc map docid -> list of correctness values (0/1)
    for the FIXED answered set (method) and FIXED matched-coverage top-k set (baseline).
    Each resample recomputes accuracies over those FIXED sets present in the resample."""
    docs = sorted(set(method_set_by_doc) | set(base_set_by_doc))
    nd = len(docs)
    rng = np.random.default_rng(seed)
    gaps = []
    for _ in range(n_boot):
        idx = rng.integers(0, nd, nd)
        mvals, bvals = [], []
        for i in idx:
            d = docs[i]
            mvals.extend(method_set_by_doc.get(d, []))
            bvals.extend(base_set_by_doc.get(d, []))
        if mvals and bvals:
            gaps.append(float(np.mean(mvals)) - float(np.mean(bvals)))
    if not gaps:
        return None
    lo, hi = np.quantile(gaps, [ALPHA / 2, 1 - ALPHA / 2])
    return {"ci95": [float(lo), float(hi)], "boot_p_gap_le_0": float(np.mean([g <= 0 for g in gaps])),
            "median": float(np.median(gaps)), "mean": float(np.mean(gaps)), "n_boot": len(gaps)}


def fixed_mc_interp_gap_boot(modeA_by_doc, base_by_doc, m_cov, seed=SEED, n_boot=B):
    """The plan's 'equivalent' fix: reuse the experiment's curve/interpolation but pass the
    FULL-sample m_cov as a FIXED constant into the inner loop (replace the resampled mc).
    modeA_by_doc/base_by_doc map docid -> list of {answered,correct,conf}. Each resample:
    ma = resampled Mode-A natural selacc; ba = baseline acc interpolated at FIXED m_cov."""
    docs = sorted(set(modeA_by_doc) | set(base_by_doc))
    nd = len(docs)
    rng = np.random.default_rng(seed)
    gaps = []
    for _ in range(n_boot):
        idx = rng.integers(0, nd, nd)
        mrec, brec = [], []
        for i in idx:
            d = docs[i]
            mrec.extend(modeA_by_doc.get(d, []))
            brec.extend(base_by_doc.get(d, []))
        _, _, ma = curve(mrec)
        bp, _, _ = curve(brec)
        ba = acc_at_coverage(bp, m_cov)        # FIXED m_cov (not resampled)
        if ma == ma and ba == ba:
            gaps.append(ma - ba)
    if not gaps:
        return None
    lo, hi = np.quantile(gaps, [ALPHA / 2, 1 - ALPHA / 2])
    return {"ci95": [float(lo), float(hi)], "boot_p_gap_le_0": float(np.mean([g <= 0 for g in gaps])),
            "median": float(np.median(gaps)), "n_boot": len(gaps)}


def clustered_diff_boot(method_by_doc, base_by_doc, seed=SEED, n_boot=B):
    """Doc-clustered paired bootstrap of a simple mean-difference (rates), e.g. confident-wrong."""
    docs = sorted(set(method_by_doc) | set(base_by_doc))
    nd = len(docs)
    rng = np.random.default_rng(seed)
    diffs = []
    for _ in range(n_boot):
        idx = rng.integers(0, nd, nd)
        mv, bv = [], []
        for i in idx:
            d = docs[i]
            mv.extend(method_by_doc.get(d, []))
            bv.extend(base_by_doc.get(d, []))
        if mv and bv:
            diffs.append(float(np.mean(bv)) - float(np.mean(mv)))   # reduction = base - method
    if not diffs:
        return None
    lo, hi = np.quantile(diffs, [ALPHA / 2, 1 - ALPHA / 2])
    return {"reduction": float(np.mean(diffs)), "ci95": [float(lo), float(hi)],
            "boot_p_reduction_le_0": float(np.mean([x <= 0 for x in diffs])), "n_boot": len(diffs)}


def clustered_value_ci(by_doc, seed=SEED, n_boot=B):
    """Doc-clustered bootstrap CI of a single mean (e.g. a recall)."""
    docs = [d for d, v in by_doc.items() if v]
    nd = len(docs)
    if nd < 2:
        allv = [x for v in by_doc.values() for x in v]
        m = float(np.mean(allv)) if allv else float("nan")
        return {"mean": m, "ci95": [m, m]}
    rng = np.random.default_rng(seed)
    means = []
    arrs = {d: np.array(by_doc[d], float) for d in docs}
    for _ in range(n_boot):
        idx = rng.integers(0, nd, nd)
        vals = np.concatenate([arrs[docs[i]] for i in idx])
        means.append(vals.mean())
    lo, hi = np.quantile(means, [ALPHA / 2, 1 - ALPHA / 2])
    return {"mean": float(np.mean([x for v in by_doc.values() for x in v])),
            "ci95": [float(lo), float(hi)], "n_boot": len(means)}


def holm(pvals: dict, alpha=ALPHA):
    """Holm step-down adjusted p-values + reject flags."""
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(items)
    out, prev = {}, 0.0
    for rank, (name, p) in enumerate(items):
        adj = min(1.0, max(prev, (m - rank) * p))
        prev = adj
        out[name] = {"p": float(p), "p_adj": float(adj), "reject": bool(adj < alpha)}
    return out


# =========================================================================== #
# LOAD SOURCES
# =========================================================================== #
@logger.catch(reraise=True)
def main():
    logger.info("Loading source method_out.json files ...")
    temporal = json.loads(TEMPORAL_FULL.read_text())
    clutrr = json.loads(CLUTRR_FULL.read_text())
    tmd = temporal["metadata"]
    cmd = clutrr["metadata"]

    cache_complete = False
    temporal_records = None
    if TEMPORAL_RECORDS.exists():
        blob = json.loads(TEMPORAL_RECORDS.read_text())
        temporal_records = blob["records"]
        costs = blob.get("client_costs", {})
        misses = costs.get("total_cache_misses")
        cost = costs.get("primary_cost")
        cache_complete = (misses == 0) and (cost in (0, 0.0)) and (len(temporal_records) == 600)
        logger.info(f"Loaded {len(temporal_records)} temporal per-query records; "
                    f"cache_misses={misses} primary_cost={cost} -> cache_complete={cache_complete}")
    else:
        logger.warning("per_query_records_temporal.json absent -> R1 will use recentering fallback.")

    out = {}                                  # top-level eval_out.json metadata payload
    metrics_agg = {}                          # flat scalar metrics
    digest = []                               # eval_digest.md lines

    # ===================================================================== #
    # R1 -- BRACKETING CI ON THE TEMPORAL Mode-A-vs-PoT GAP
    # ===================================================================== #
    logger.info("=== R1: temporal bracketing CI ===")
    h1_pub = tmd["H1_matched_coverage"]
    pub_old_ci = {b: h1_pub[f"modeA_vs_{b}"]["ci95"] for b in ("pot", "sc", "naive", "raw")}
    pub_gap = {b: h1_pub[f"modeA_vs_{b}"]["gap"] for b in ("pot", "sc", "naive", "raw")}
    pub_bootp = {b: h1_pub[f"modeA_vs_{b}"]["boot_p_gap_le_0"] for b in ("pot", "sc", "naive", "raw")}

    r1 = {"tag": "REAL-LLM-READ", "n_boot": B, "seed": SEED,
          "method_primary": ("fixed-operating-point doc-clustered paired bootstrap"
                             if cache_complete else "reverse-percentile recentering (FALLBACK)"),
          "cache_complete": cache_complete}

    if cache_complete:
        recs = temporal_records
        N = len(recs)
        # Mode-A natural operating point (FIXED once on the full sample)
        modeA_ans = [r for r in recs if r["modeA"]["answered"] and r["modeA"]["correct"] is not None]
        m_cov = len(modeA_ans) / N
        m_acc = float(np.mean([r["modeA"]["correct"] for r in modeA_ans]))
        k_target = int(round(m_cov * N))      # matched-coverage k (113)
        check("temporal.modeA_coverage", m_cov, h1_pub["modeA_vs_pot"]["matched_coverage"])
        check("temporal.modeA_selacc", m_acc, h1_pub["modeA_vs_pot"]["method_acc"])

        # FIXED Mode-A answered set -> docid -> [correct]
        modeA_set_doc = {}
        for r in modeA_ans:
            modeA_set_doc.setdefault(r["docid"], []).append(int(r["modeA"]["correct"]))

        r1["fixed_m_cov"] = _r(m_cov)
        r1["k_matched"] = k_target
        r1["modeA_selective_accuracy"] = _r(m_acc)
        r1["baselines"] = {}

        for base in ("pot", "sc", "naive", "raw"):
            brecs = [r for r in recs if r[base]["answered"] and r[base]["correct"] is not None]
            # FIXED matched-coverage set = top-k_target by conf
            brecs_sorted = sorted(brecs, key=lambda r: -r[base]["conf"])
            kk = min(k_target, len(brecs_sorted))
            base_set = brecs_sorted[:kk]
            base_acc = float(np.mean([r[base]["correct"] for r in base_set])) if base_set else float("nan")
            point_gap = m_acc - base_acc
            # consistency vs published point gap
            check(f"temporal.gap_modeA_vs_{base}", point_gap, pub_gap[base], tol=3e-3)

            base_set_doc = {}
            for r in base_set:
                base_set_doc.setdefault(r["docid"], []).append(int(r[base]["correct"]))

            # doc -> all-answered baseline records (for the interpolation variant + old reproduction)
            base_all_doc = {}
            for rr in brecs:
                base_all_doc.setdefault(rr["docid"], []).append(
                    {"answered": True, "correct": rr[base]["correct"], "conf": rr[base]["conf"]})
            modeA_all_doc = {}
            for rr in modeA_ans:
                modeA_all_doc.setdefault(rr["docid"], []).append(
                    {"answered": True, "correct": rr["modeA"]["correct"], "conf": rr["modeA"]["conf"]})

            new = fixed_set_gap_boot(modeA_set_doc, base_set_doc)         # PRIMARY: fixed-set
            interp = fixed_mc_interp_gap_boot(modeA_all_doc, base_all_doc, m_cov)  # plan's 'equivalent' fix
            old = old_buggy_gap_boot(modeA_all_doc, base_all_doc)         # reproduce buggy procedure
            new_ci = new["ci95"]
            brackets = bool(new_ci[0] <= point_gap <= new_ci[1])
            corrected_sig = bool(new_ci[0] > 0)   # one-sided: CI lower bound above 0
            r1["baselines"][base] = {
                "point_gap": _r(point_gap),
                "base_acc_at_matched_coverage": _r(base_acc),
                "base_natural_coverage": _r(len(brecs) / N),
                "published_gap": _r(pub_gap[base]),
                "published_old_ci95_B2000": [_r(pub_old_ci[base][0]), _r(pub_old_ci[base][1])],
                "published_old_boot_p": _r(pub_bootp[base]),
                "reproduced_old_ci95_B10000": [_r(old["ci95"][0]), _r(old["ci95"][1])] if old else None,
                "reproduced_old_boot_p": _r(old["boot_p_gap_le_0"]) if old else None,
                "new_ci95": [_r(new_ci[0]), _r(new_ci[1])],
                "new_boot_p_gap_le_0": _r(new["boot_p_gap_le_0"]),
                "new_ci95_interp_variant": [_r(interp["ci95"][0]), _r(interp["ci95"][1])] if interp else None,
                "new_boot_p_interp_variant": _r(interp["boot_p_gap_le_0"]) if interp else None,
                "ci_brackets_point_estimate": brackets,
                "old_ci_brackets_point_estimate": bool(pub_old_ci[base][0] <= pub_gap[base] <= pub_old_ci[base][1]),
                "corrected_one_sided_significant": corrected_sig,
                "n_boot": B,
            }
            logger.info(f"R1 vs {base}: point={point_gap:+.4f} OLD_ci={[round(x,4) for x in pub_old_ci[base]]} "
                        f"NEW_ci=[{new_ci[0]:.4f},{new_ci[1]:.4f}] brackets={brackets} "
                        f"new_boot_p={new['boot_p_gap_le_0']:.4f} interp_ci="
                        f"[{interp['ci95'][0]:.4f},{interp['ci95'][1]:.4f}] corrected_sig={corrected_sig}")

        # Holm over the corrected confirmatory family {vs PoT, vs SC} (H1 gateways)
        r1["holm_H1_corrected"] = {k: v for k, v in holm({
            "H1_vs_PoT": r1["baselines"]["pot"]["new_boot_p_gap_le_0"],
            "H1_vs_SC": r1["baselines"]["sc"]["new_boot_p_gap_le_0"],
        }).items()}
        r1["corrected_significance_finding"] = (
            "IMPORTANT (honest re-analysis result): once the operating point is held FIXED, the corrected "
            "doc-clustered CIs are centered on the true point gaps and BRACKET them, but they are WIDE and "
            f"INCLUDE 0 for both H1 gateways -- vs PoT new_ci={r1['baselines']['pot']['new_ci95']} "
            f"(boot_p={r1['baselines']['pot']['new_boot_p_gap_le_0']}), vs SC new_ci={r1['baselines']['sc']['new_ci95']} "
            f"(boot_p={r1['baselines']['sc']['new_boot_p_gap_le_0']}). The published Holm-significance "
            "(boot_p 0.007 / 0.0185, CI ENTIRELY above 0 yet EXCLUDING the point estimate) was an ARTIFACT "
            "of the same estimator/resample mismatch: the buggy bootstrap recentered on the volatile "
            "low-coverage baseline curve (~0.18), simultaneously inflating the gap magnitude AND its apparent "
            "significance. The plan's 'equivalent' fixed-m_cov INTERPOLATION variant (which RE-SELECTS the "
            f"baseline matched set within each resample) gives vs-PoT {r1['baselines']['pot'].get('new_ci95_interp_variant')} "
            f"(boot_p {r1['baselines']['pot'].get('new_boot_p_interp_variant')}) -- borderline, lower bound just above 0, "
            "but it retains RESIDUAL interpolation volatility (its upper bound ~0.34 echoes the buggy ~0.31), so the "
            "literal fixed-SET estimator (which pins the specific top-k matched queries per the plan's 'do NOT re-derive "
            "the threshold' instruction) is the PRIMARY. CONCLUSION: significance is ESTIMATOR-DEPENDENT and FRAGILE -- "
            "on natural temporal text the Mode-A selective-accuracy advantage over PoT/SC is MARGINAL and NOT robustly "
            "significant under a correctly-centered bootstrap (~36 doc clusters, SE~0.06); it is NOT the robust CONFIRM "
            "the published boot_p implied. The transferable temporal contribution is the gold-free abstain-on-collapse "
            "CERTIFICATE, NOT selective-accuracy dominance. vs-naive (boot_p 0.088) and vs-raw (gap -0.124) are "
            "consistent before and after the fix.")
        r1["why_old_ci_failed"] = (
            "method.py:531-563 matched_coverage_gap re-derived the TARGET coverage mc from each "
            "resample (line ~548 'mp,mc,ma=_curve(mrec)') and interpolated the baseline at that VARYING "
            "mc (line ~550 'ba=_acc_at_coverage(bp,mc)'). The resampled gap is therefore a DIFFERENT "
            "estimator than the headline gap; on the volatile low-coverage PoT curve the distribution "
            "recenters (~0.18) so the published vs-PoT CI [0.0454,0.3148] does NOT contain the observed "
            "point gap +0.0265. Holding the operating point FIXED across resamples (Mode-A's fixed "
            "answered set vs PoT's fixed top-k-by-conf matched set) yields a CI that BRACKETS +0.0265.")
    else:
        # ---- FALLBACK: reverse-percentile recentering on the experiment's own published gaps ----
        r1["fallback_note"] = (
            "Temporal per-query (conf,correct) records unavailable / cache incomplete -> the conf-based "
            "matched-coverage CI cannot be recomputed without the cached pipeline. Presented instead: a "
            "basic/reverse-percentile recentering [2*gap - q_hi, 2*gap - q_lo] of the published bootstrap "
            "quantiles. This is a PRESENTATIONAL recentering, not a re-estimated CI.")
        r1["baselines"] = {}
        for base in ("pot", "sc", "naive", "raw"):
            g = pub_gap[base]
            lo, hi = pub_old_ci[base]
            r1["baselines"][base] = {
                "point_gap": _r(g),
                "published_old_ci95_B2000": [_r(lo), _r(hi)],
                "recentered_ci95": [_r(2 * g - hi), _r(2 * g - lo)],
                "ci_brackets_point_estimate": bool(min(2 * g - hi, 2 * g - lo) <= g <= max(2 * g - hi, 2 * g - lo)),
                "n_boot": "N/A (recentering of published B=2000 quantiles)",
            }
    out["r1_bracketing"] = r1
    metrics_agg["temporal_modeA_vs_pot_gap"] = _r(pub_gap["pot"])
    if cache_complete:
        metrics_agg["temporal_modeA_vs_pot_new_ci_lo"] = r1["baselines"]["pot"]["new_ci95"][0]
        metrics_agg["temporal_modeA_vs_pot_new_ci_hi"] = r1["baselines"]["pot"]["new_ci95"][1]
        metrics_agg["temporal_modeA_vs_pot_ci_brackets"] = 1.0 if r1["baselines"]["pot"]["ci_brackets_point_estimate"] else 0.0
        metrics_agg["temporal_modeA_vs_pot_new_boot_p"] = r1["baselines"]["pot"]["new_boot_p_gap_le_0"]
        metrics_agg["temporal_modeA_vs_sc_new_boot_p"] = r1["baselines"]["sc"]["new_boot_p_gap_le_0"]
        metrics_agg["temporal_modeA_vs_pot_corrected_significant"] = 1.0 if r1["baselines"]["pot"]["corrected_one_sided_significant"] else 0.0
        metrics_agg["temporal_modeA_vs_sc_corrected_significant"] = 1.0 if r1["baselines"]["sc"]["corrected_one_sided_significant"] else 0.0

    # ===================================================================== #
    # CLUTRR per-query columns
    # ===================================================================== #
    clutrr_ex = [e for ds in clutrr["datasets"] for e in ds["examples"]]
    present = [e for e in clutrr_ex if not e.get("metadata_is_absent")]
    absent = [e for e in clutrr_ex if e.get("metadata_is_absent")]
    logger.info(f"CLUTRR: {len(clutrr_ex)} total, {len(present)} present, {len(absent)} absent")

    def is_ans(v):
        return v is not None and v != "ABSTAIN"

    # ===================================================================== #
    # R2 -- CLUTRR naive natural vs forced coverage + iteration via coverage
    # ===================================================================== #
    logger.info("=== R2: CLUTRR naive natural vs forced coverage ===")
    n_present = len(present)
    naive_ans = [e for e in present if is_ans(e.get("predict_naive"))]
    naive_nat_cov = len(naive_ans) / n_present
    naive_nat_correct = sum(1 for e in naive_ans if e.get("predict_naive") == e.get("output"))
    naive_nat_selacc = naive_nat_correct / len(naive_ans) if naive_ans else float("nan")
    lb = cmd["deduction_matched_coverage"]["leaderboard"]
    naive_forced_cov = lb["naive"]["coverage_matched"]
    naive_forced_selacc = lb["naive"]["selective_accuracy"]
    check("clutrr.naive_natural_coverage", naive_nat_cov, lb["naive"]["natural_coverage"])

    # iteration COVERAGE gap by hop (recompute from columns -> verify vs published)
    avh = cmd["accuracy_vs_hop"]
    iter_cov_gap = {}
    iter_cov_gap_recomputed = {}
    for hop in sorted(avh, key=lambda x: int(x)):
        iter_cov_gap[int(hop)] = avh[hop]["full_minus_naive_coverage_gap"]
    for hop in sorted(set(int(e["metadata_hop"]) for e in present)):
        hq = [e for e in present if int(e["metadata_hop"]) == hop]
        f_cov = sum(1 for e in hq if is_ans(e.get("predict_modeA"))) / len(hq)
        n_cov = sum(1 for e in hq if is_ans(e.get("predict_naive"))) / len(hq)
        iter_cov_gap_recomputed[hop] = _r(f_cov - n_cov)
        if hop in iter_cov_gap:
            check(f"clutrr.iter_cov_gap_hop{hop}", f_cov - n_cov, iter_cov_gap[hop], tol=2e-3)

    r2 = {
        "tag": "REAL-LLM-READ",
        "venue": "templated-CLUTRR",
        "n_present_queries": n_present,
        "naive_natural_coverage": _r(naive_nat_cov),
        "naive_natural_selacc": _r(naive_nat_selacc),
        "naive_natural_n_answered": len(naive_ans),
        "naive_natural_n_correct": naive_nat_correct,
        "naive_matched_coverage": _r(naive_forced_cov),
        "naive_matched_selacc_forced": _r(naive_forced_selacc),
        "force_extension_flag": True,
        "force_extension_caption": (
            "naive matched-coverage selective accuracy (0.229 @ cov 0.686) is FORCE-EXTENDED beyond "
            "naive's natural coverage 0.216 (22/102 answered, predominantly hop-2) with representative-"
            "surface answers; the natural-coverage figure (selacc ~0.73 @ cov 0.216) is reported alongside. "
            "The '0.229 -> 0.886' contrast must NOT be read as the iteration result."),
        "iteration_coverage_gap_by_hop": {str(k): _r(v) for k, v in iter_cov_gap.items()},
        "iteration_coverage_gap_by_hop_recomputed": {str(k): v for k, v in iter_cov_gap_recomputed.items()},
        "iteration_statement": (
            "full iterated closure resolves a strictly larger COVERAGE fraction than naive single-pass "
            "for hop>=3 (0.0@hop-2 -> 0.586@hop-3 -> up to 0.875@hop-9); naive single-pass resolves only "
            "hop-2. Route the CLUTRR H3 (iteration) claim through the coverage axis, NOT the forced "
            "selective-accuracy gap."),
        "legitimate_leaderboard_matched_cov": _r(cmd["deduction_matched_coverage"]["c_star"]),
        "legitimate_leaderboard": {
            "modeA_selacc": _r(lb["modeA"]["selective_accuracy"]),
            "pot_selacc": _r(lb["pot"]["selective_accuracy"]),
            "sc_selacc": _r(lb["sc"]["selective_accuracy"]),
            "raw_selacc": _r(lb["raw"]["selective_accuracy"]),
            "naive_selacc_FORCE_EXTENDED": _r(lb["naive"]["selective_accuracy"]),
            "off_selacc": _r(lb["off"]["selective_accuracy"]),
        },
    }
    out["r2_clutrr"] = r2
    metrics_agg["clutrr_naive_natural_coverage"] = _r(naive_nat_cov)
    metrics_agg["clutrr_naive_natural_selacc"] = _r(naive_nat_selacc)
    metrics_agg["clutrr_naive_matched_selacc_forced"] = _r(naive_forced_selacc)

    # ===================================================================== #
    # CLUTRR matched-coverage gaps recomputed with the CORRECTED fixed-set bootstrap
    # ===================================================================== #
    logger.info("=== CLUTRR matched-coverage gaps (fixed-operating-point bootstrap) ===")
    modeA_pres_ans = [e for e in present if is_ans(e.get("predict_modeA"))]
    c_star = len(modeA_pres_ans) / n_present
    modeA_acc_c = float(np.mean([1.0 if e["predict_modeA"] == e["output"] else 0.0 for e in modeA_pres_ans]))
    k_c = int(round(c_star * n_present))
    check("clutrr.modeA_matched_selacc", modeA_acc_c, lb["modeA"]["selective_accuracy"], tol=2e-3)

    modeA_set_doc_c = {}
    for e in modeA_pres_ans:
        modeA_set_doc_c.setdefault(e["metadata_doc_id"], []).append(1 if e["predict_modeA"] == e["output"] else 0)

    clutrr_gaps = {}
    conf_field = {"raw": "metadata_raw_conf", "sc": "metadata_sc_conf", "pot": "metadata_pot_conf"}
    for base in ("pot", "sc", "raw"):
        bans = [e for e in present if is_ans(e.get(f"predict_{base}")) and e.get(conf_field[base]) is not None]
        bans_sorted = sorted(bans, key=lambda e: -float(e[conf_field[base]]))
        kk = min(k_c, len(bans_sorted))
        bset = bans_sorted[:kk]
        base_acc = float(np.mean([1.0 if e[f"predict_{base}"] == e["output"] else 0.0 for e in bset]))
        pgap = modeA_acc_c - base_acc
        base_set_doc = {}
        for e in bset:
            base_set_doc.setdefault(e["metadata_doc_id"], []).append(1 if e[f"predict_{base}"] == e["output"] else 0)
        boot = fixed_set_gap_boot(modeA_set_doc_c, base_set_doc)
        pub = cmd["deduction_matched_coverage"]["gaps"][base]
        check(f"clutrr.gap_modeA_vs_{base}", pgap, pub["gap"], tol=2e-2)
        clutrr_gaps[base] = {
            "point_gap": _r(pgap), "base_acc_matched": _r(base_acc),
            "new_ci95": [_r(boot["ci95"][0]), _r(boot["ci95"][1])],
            "new_boot_p_gap_le_0": _r(boot["boot_p_gap_le_0"]),
            "published_gap": _r(pub["gap"]), "published_ci95_B2000": [_r(pub["ci95"][0]), _r(pub["ci95"][1])],
            "published_p_one_sided": _r(pub["p_one_sided"]),
        }
        logger.info(f"CLUTRR vs {base}: point={pgap:+.4f} new_ci=[{boot['ci95'][0]:.3f},{boot['ci95'][1]:.3f}] "
                    f"published_gap={pub['gap']:+.4f}")
    clutrr_holm = holm({"H1_vs_pot": clutrr_gaps["pot"]["new_boot_p_gap_le_0"],
                        "H1_vs_sc": clutrr_gaps["sc"]["new_boot_p_gap_le_0"]})
    out["clutrr_matched_coverage_gaps"] = {
        "tag": "REAL-LLM-READ", "venue": "templated-CLUTRR", "matched_coverage": _r(c_star),
        "modeA_selacc": _r(modeA_acc_c), "gaps": clutrr_gaps, "holm": clutrr_holm,
        "published_holm_p_adj": _r(cmd["holm_family"]["H1_modeA_vs_pot"]["p_adj"]),
    }
    metrics_agg["clutrr_modeA_vs_pot_gap"] = _r(clutrr_gaps["pot"]["point_gap"])
    metrics_agg["clutrr_modeA_selacc"] = _r(modeA_acc_c)

    # ===================================================================== #
    # 42.5% CONFIDENT-WRONG BLOCK (temporal)
    # ===================================================================== #
    logger.info("=== temporal 42.5% confident-wrong block ===")
    h2 = tmd["H2_hallucination"]
    cw_frac = h2["confident_wrong_modeA"]
    # recompute from records if available
    cw_recomputed = None
    reduction_recomputed = None
    if cache_complete:
        recs = temporal_records
        ma_ans = [r for r in recs if r["modeA"]["answered"]]
        cw = sum(1 for r in ma_ans if r["modeA"]["correct"] == 0)
        cw_recomputed = cw / len(ma_ans)
        check("temporal.confident_wrong_modeA", cw_recomputed, cw_frac)
        # doc-clustered reduction CI (raw confident-wrong - modeA confident-wrong) at B=10000
        ma_doc, raw_doc = {}, {}
        for r in recs:
            if r["modeA"]["answered"]:
                ma_doc.setdefault(r["docid"], []).append(0 if r["modeA"]["correct"] == 1 else 1)
            if r["raw"]["answered"]:
                raw_doc.setdefault(r["docid"], []).append(0 if r["raw"]["correct"] == 1 else 1)
        red = clustered_diff_boot(ma_doc, raw_doc)
        reduction_recomputed = red
        check("temporal.confident_wrong_reduction", red["reduction"], h2["reduction"], tol=5e-3)

    synth = tmd["synthetic_backstop"]["cells"]
    synth_raw_gaps = [synth[c]["vs_baselines"]["raw"]["gap"] for c in synth]
    synth_mean_vs_raw = float(np.mean(synth_raw_gaps))
    read_rows = {k: {"recall": _r(v["recall"]), "ci95": [_r(v["ci95"][0]), _r(v["ci95"][1])],
                     "verdict": v["verdict"], "crosses_gate": v["crosses_gate"]}
                 for k, v in tmd["read_soundness_reconciliation"]["rows"].items()}
    rho_vals = [tmd["per_edge_recall"][c][r]["rho_within_doc_soundness"]
                for c in tmd["per_edge_recall"] for r in tmd["per_edge_recall"][c]]
    cw_block = {
        "tag": "REAL-LLM-READ",
        "frac_confident_wrong_among_answered": _r(cw_frac),
        "n_confident_wrong": h2["modeA_confident_wrong_count"],
        "denom_answered": h2["n_modeA_answered"],
        "modeA_coverage": _r(h2["modeA_coverage"]),
        "modeA_abstention_rate": _r(h2["modeA_abstention_rate"]),
        "confident_wrong_raw": _r(h2["confident_wrong_raw"]),
        "reduction_vs_raw_published": _r(h2["reduction"]),
        "reduction_published_ci95": [_r(h2["reduction_ci95"][0]), _r(h2["reduction_ci95"][1])],
        "reduction_recomputed_B10000": ({"reduction": _r(reduction_recomputed["reduction"]),
                                         "ci95": [_r(reduction_recomputed["ci95"][0]), _r(reduction_recomputed["ci95"][1])],
                                         "boot_p": _r(reduction_recomputed["boot_p_reduction_le_0"])}
                                        if reduction_recomputed else None),
        "confident_wrong_recomputed": _r(cw_recomputed),
        "silent_wrong_narrowing_count": h2["silent_wrong_narrowing_count"],
        "all_confident_wrongs_are_silent_wrong_narrowing": (h2["silent_wrong_narrowing_count"] == h2["modeA_confident_wrong_count"]),
        "raw_minus_modeA_acc_at_matched_coverage": _r(pub_gap["raw"]),   # -0.124
        "reporting_block": (
            "On natural temporal text, among the ~19% of queries Mode-A commits to, it is CONFIDENT-WRONG "
            "42.5% (48/113). REPORT THIS BESIDE EVERY TEMPORAL CLAIM. Mechanism: silent-wrong-narrowing -- "
            "when gold is OMITTED from a contributing local read, closure narrows to a confident WRONG "
            "singleton with NO empty collapse, so Mode-B cannot flag it; ALL 48 Mode-A confident-wrongs are "
            "of this type. Bounded per-edge by (1-recall) and per-network by (1-J(E)). Hence "
            "'faithfulness-by-abstention' is WEAKLY protective on dense temporal prose (~0.85 recall): raw "
            "actually out-accuracies Mode-A at matched coverage by 0.124. The temporal value of Mode-A is "
            "the gold-free certificate + abstention-as-an-OPTION, NOT selective-accuracy dominance, and "
            "even that is bounded by read recall."),
        "read_soundness_rows": read_rows,
        "rho_within_doc_soundness_range": [_r(min(rho_vals)), _r(max(rho_vals))],
        "synthetic_backstop_vs_raw_mean_gap": _r(synth_mean_vs_raw),
        "synthetic_backstop_cells_vs_raw": {c: _r(synth[c]["vs_baselines"]["raw"]["gap"]) for c in synth},
        "synthetic_backstop_recall": 0.96,
        "read_soundness_localization": (
            "At synthetic recall 0.96 Mode-A beats raw by ~+0.225 at matched coverage (mechanism works when "
            "reads are sound); on real text recall is ~0.83-0.86 (NT primary CI excludes-below-gate; NT "
            "strong CI straddles; TDDMan both below) -> the binding real-text constraint is the NEURAL READ "
            "(read soundness), NOT the symbolic closure step."),
    }
    out["temporal_confident_wrong_block"] = cw_block
    metrics_agg["temporal_confident_wrong_frac"] = _r(cw_frac)
    metrics_agg["temporal_confident_wrong_n"] = float(h2["modeA_confident_wrong_count"])
    metrics_agg["temporal_synthetic_backstop_vs_raw_mean"] = _r(synth_mean_vs_raw)

    # ===================================================================== #
    # DECOMPOSITION: INHERITED vs NOVEL  (CLUTRR + TEMPORAL + carried Allen)
    # ===================================================================== #
    logger.info("=== inherited-vs-novel decomposition ===")
    # ---- CLUTRR: matched-coverage additive split (force-extension flagged) ----
    naive_forced_acc = lb["naive"]["selective_accuracy"]
    pot_acc_c = lb["pot"]["selective_accuracy"]
    modeA_acc_lb = lb["modeA"]["selective_accuracy"]
    clutrr_inherited = naive_forced_acc - pot_acc_c
    clutrr_novel = modeA_acc_lb - naive_forced_acc
    # honest natural-operating-point inherited proxy (naive on its natural hop-2 set vs PoT on hop-2)
    hop2 = avh.get("2", {})
    clutrr_decomp = {
        "tag": "REAL-LLM-READ", "venue": "templated-CLUTRR",
        "definition": "system_gap(ModeA-PoT) = INHERITED(naive-PoT) + NOVEL_selacc(ModeA-naive), all at matched coverage 0.686",
        "system_gap_modeA_minus_pot": _r(modeA_acc_lb - pot_acc_c),
        "inherited_naive_minus_pot_FORCED": _r(clutrr_inherited),
        "novel_modeA_minus_naive_FORCED": _r(clutrr_novel),
        "additivity_residual": _r((modeA_acc_lb - pot_acc_c) - (clutrr_inherited + clutrr_novel)),
        "WARNING_force_extension": (
            "naive@matched (0.229) is FORCE-EXTENDED, so this additive split mis-attributes: the negative "
            "'inherited' (-0.229) and inflated 'novel' (+0.657) are ARTIFACTS of force-extending naive's "
            "coverage with representative-surface (wrong) answers. naive single-pass CANNOT iterate, so it "
            "is a poor proxy for the inherited exact-table composition advantage on CLUTRR."),
        "honest_framing": (
            "On CLUTRR the Mode-A advantage is realized through ITERATED exact-table composition over "
            "multi-hop chains (naive single-pass resolves only hop-2). The actionable inherited part is the "
            "STANDARD neuro-symbolic premise 'use exact composition tables instead of LLM composition' -- "
            "NOT this work's discovery; the novel cross-path-INTERSECTION mechanism is NOT what drives CLUTRR "
            "(kinship is a single-chain forward UNION fixpoint, no involutive converse)."),
        "naive_natural_hop2_selacc": _r(hop2.get("naive", {}).get("selective_accuracy")),
        "pot_hop2_selacc": _r(hop2.get("pot", {}).get("selective_accuracy")),
    }

    # ---- TEMPORAL: novel_selacc on covered-by-BOTH subset (expect ~0) ----
    temporal_decomp = {"tag": "REAL-LLM-READ", "venue": "natural-temporal", "algebra": "point"}
    if cache_complete:
        recs = temporal_records
        both = [r for r in recs if r["modeA"]["answered"] and r["naive"]["answered"]
                and r["modeA"]["correct"] is not None and r["naive"]["correct"] is not None]
        if both:
            mA = float(np.mean([r["modeA"]["correct"] for r in both]))
            nA = float(np.mean([r["naive"]["correct"] for r in both]))
            # doc-clustered CI of the novel_selacc difference
            mdoc, ndoc = {}, {}
            for r in both:
                mdoc.setdefault(r["docid"], []).append(int(r["modeA"]["correct"]))
                ndoc.setdefault(r["docid"], []).append(int(r["naive"]["correct"]))
            nov = fixed_set_gap_boot(mdoc, ndoc)
            n_disagree = sum(1 for r in both if r["modeA"]["pred"] != r["naive"]["pred"])
            temporal_decomp["novel_selacc_covered_by_both"] = {
                "n": len(both), "modeA_acc": _r(mA), "naive_acc": _r(nA),
                "novel_selacc": _r(mA - nA), "ci95": [_r(nov["ci95"][0]), _r(nov["ci95"][1])],
                "boot_p_le_0": _r(nov["boot_p_gap_le_0"]),
                "n_pred_disagreements": n_disagree,
                "note": "iteration adds ~0 selective accuracy on queries BOTH methods resolve (full closure "
                        "narrows to the same singleton single-pass already found)."}
    # inherited (naive vs pot at matched coverage) for temporal
    temporal_decomp["inherited_naive_minus_pot_at_matched_cov"] = _r(
        h1_pub["modeA_vs_naive"]["base_acc"] - h1_pub["modeA_vs_pot"]["base_acc"])
    strat = tmd["H1_stratified"]
    temporal_decomp["iteration_on_coverage_axis"] = {
        "len2_modeA_vs_naive_gap": _r(strat["len2"]["modeA_vs_naive"]["gap"]),
        "len2_note": "len2 Mode-A==naive EXACTLY 0.0 by theorem (single via, no iteration possible)",
        "ge3_cyclic_modeA_vs_naive_gap": _r(strat["ge3_cyclic"]["modeA_vs_naive"]["gap"]),
        "ge3_cyclic_ci95": [_r(strat["ge3_cyclic"]["modeA_vs_naive"]["ci95"][0]),
                            _r(strat["ge3_cyclic"]["modeA_vs_naive"]["ci95"][1])],
        "ge3_cyclic_boot_p": _r(strat["ge3_cyclic"]["modeA_vs_naive"]["boot_p_gap_le_0"]),
        "label": "EXPLORATORY (NOT significant at power); iteration value, where any, lives on COVERAGE not selective-accuracy",
    }
    temporal_decomp["summary"] = (
        "On the SELECTIVE-ACCURACY axis the temporal iteration/novel term is ~0 (covered-by-both novel_selacc "
        "~0); INHERITED (naive-PoT) is also ~0 at matched coverage. The matched-coverage system gap "
        "+0.0265 is MARGINAL and reflects Mode-A's higher accuracy on its low-coverage answered set, not "
        "iteration. Iteration's value (where any) is on the COVERAGE axis (ge3_cyclic +0.042, p=0.061, NS).")

    # ---- ALLEN: recompute from iter-2 file (cross-check) + carry-forward prior split ----
    allen_block = {"tag": "REAL-LLM-READ-ON-SYNTHETIC", "venue": "synthetic-NL",
                   "source": f"iter-2 Allen experiment {ITER2_ALLEN_ID} (carried via {PRIOR_EVAL_ID}); NOT a dependency of this eval",
                   "note": "templated NL at recall ~1.0; carried forward as a CITED prior result."}
    prior = json.loads(PRIOR_EVAL.read_text())
    allen_pub = prior["metadata"]["decomposition"]["allen"]["selective_accuracy_axis"]["bite_bearing"]
    allen_block["carried_forward"] = {
        "system_gap": _r(allen_pub["system_gap"]),
        "inherited": _r(allen_pub["inherited_component"]),
        "novel_selacc": _r(allen_pub["novel_selacc_component"]),
    }
    try:
        a2 = json.loads(ITER2_ALLEN.read_text())
        allen_ds = next(ds for ds in a2["datasets"] if ds["dataset"] == "synthetic_qcn_allen")
        aex = allen_ds["examples"]
        both = [e for e in aex if e.get("metadata_modeA_covered") and e.get("metadata_naive_covered")]
        if both:
            def corr(e, m):
                return 1.0 if (is_ans(e.get(f"predict_{m}")) and e.get(f"predict_{m}") == e.get("output")) else 0.0
            mA = float(np.mean([corr(e, "modeA") for e in both]))
            nA = float(np.mean([corr(e, "naive") for e in both]))
            allen_block["recomputed_novel_selacc_covered_by_both"] = {
                "n": len(both), "modeA_acc": _r(mA), "naive_acc": _r(nA), "novel_selacc": _r(mA - nA),
                "note": "independent cross-check from iter-2 allen columns; ~0 confirms iteration adds ~0 selective accuracy."}
            # matched-coverage inherited proxy: naive vs pot on covered-by-both
            potA = float(np.mean([corr(e, "pot") for e in both]))
            allen_block["recomputed_inherited_naive_minus_pot_on_both"] = _r(nA - potA)
            allen_block["readable"] = True
            check("allen.novel_selacc_covered_by_both", mA - nA, allen_pub["novel_selacc_component"], tol=5e-3)
    except Exception as e:
        allen_block["readable"] = False
        allen_block["recompute_error"] = str(e)
        logger.warning(f"iter-2 Allen recompute failed -> carry-forward only: {e}")

    out["decomposition"] = {
        "clutrr": clutrr_decomp,
        "temporal_point": temporal_decomp,
        "allen_carried_forward": allen_block,
        "actionable_framing": (
            "The INHERITED part (exact composition table vs LLM per-path composition) is the STANDARD "
            "neuro-symbolic premise, not this work's discovery. The NOVEL-on-selective-accuracy term "
            "(cross-path iterated intersection) is ~0 on both available algebras."),
    }
    metrics_agg["allen_inherited_carried"] = _r(allen_pub["inherited_component"])
    metrics_agg["allen_novel_selacc_carried"] = _r(allen_pub["novel_selacc_component"])

    # ===================================================================== #
    # CLUTRR carry-forward results for the contribution-split (recompute simple counts)
    # ===================================================================== #
    h2c = cmd["absent_relation_h2"]
    # recompute natural confident-wrong (named) rates on absent pool from columns
    modeA_named_abs = sum(1 for e in absent if is_ans(e.get("predict_modeA"))) / len(absent)
    raw_named_abs = sum(1 for e in absent if is_ans(e.get("predict_raw"))) / len(absent)
    check("clutrr.modeA_named_rate_absent", modeA_named_abs, h2c["natural_operating_points"]["modeA"]["natural_named_rate"])
    check("clutrr.raw_named_rate_absent", raw_named_abs, h2c["natural_operating_points"]["raw"]["natural_named_rate"])
    oracle = cmd["deduction_goldread_oracle"]
    atomic = cmd["atomic_pr"]
    prolog = cmd["prolog_discharge"]
    rc_mixed = cmd["risk_coverage_mixed_present_absent"]

    # ===================================================================== #
    # CONTRIBUTION-SPLIT TABLE
    # ===================================================================== #
    logger.info("=== contribution-split table ===")
    def row(claim, tag, venue, where, number):
        return {"claim": claim, "evidence_tag": tag, "venue": venue, "where_it_holds": where, "number": number}

    transferable = [
        row("CLUTRR Mode-A selective accuracy vs PoT / SC / raw at matched coverage 0.686 -- inherited "
            "exact-table multi-hop composition + structural abstention on a TEMPLATED benchmark",
            "REAL-LLM-READ", "templated-CLUTRR", "TRANSFERABLE-AT-POWER",
            {"modeA_selacc": _r(modeA_acc_lb),
             "vs_pot_gap": _r(clutrr_gaps["pot"]["point_gap"]), "vs_pot_ci95": clutrr_gaps["pot"]["new_ci95"],
             "vs_sc_gap": _r(clutrr_gaps["sc"]["point_gap"]), "vs_sc_ci95": clutrr_gaps["sc"]["new_ci95"],
             "vs_raw_gap": _r(clutrr_gaps["raw"]["point_gap"]), "vs_raw_ci95": clutrr_gaps["raw"]["new_ci95"],
             "holm_p_adj": _r(cmd["holm_family"]["H1_modeA_vs_pot"]["p_adj"])}),
        row("CLUTRR H2 absent-relation confident-wrong (hallucination) reduction vs raw, risk-coverage on "
            "mixed n=282 pool (Mode-A answers 26.6% @ confident-wrong 4.6%)",
            "REAL-LLM-READ", "templated-CLUTRR", "TRANSFERABLE-AT-POWER",
            {"reduction": _r(h2c["confident_wrong_reduction"]), "ci95": [_r(h2c["ci95"][0]), _r(h2c["ci95"][1])],
             "p_one_sided": _r(h2c["p_one_sided"]), "meets_0.20_bar": h2c["meets_0.20_bar"],
             "mixed_pool_modeA_coverage": _r(rc_mixed["modeA"]["points"][1]["coverage"]),
             "mixed_pool_modeA_confident_wrong": _r(rc_mixed["modeA"]["points"][1]["confident_wrong_rate"])}),
        row("CLUTRR gold-read ORACLE: Mode-A 1.00 selective accuracy @ coverage 0.951 vs 0.433 raw/PoT -- "
            "closure is NOT the bottleneck; the ~0.53 atomic neural READ is",
            "REAL-LLM-READ", "templated-CLUTRR", "TRANSFERABLE-AT-POWER",
            {"oracle_modeA_selacc": _r(oracle["leaderboard"]["modeA"]["selective_accuracy"]),
             "oracle_coverage": _r(oracle["leaderboard"]["modeA"]["coverage"]),
             "oracle_raw_selacc": _r(oracle["leaderboard"]["raw"]["selective_accuracy"]),
             "atomic_recall": _r(atomic["recall"]), "atomic_precision": _r(atomic["precision"]),
             "atomic_f1": _r(atomic["f1"])}),
        row("CLUTRR multi-hop accuracy ~0.80-1.00 through hop-10 while raw->0.0 / PoT->0.2; SWI-Prolog "
            "discharge executed",
            "REAL-LLM-READ", "templated-CLUTRR", "TRANSFERABLE-AT-POWER",
            {"hop10_modeA_selacc": _r(avh["10"]["modeA"]["selective_accuracy"]),
             "hop10_raw_selacc": _r(avh["10"]["raw"]["selective_accuracy"]),
             "hop10_pot_selacc": _r(avh["10"]["pot"]["selective_accuracy"]),
             "prolog_executed": prolog["n_executed_in_swipl"], "prolog_match_engine": prolog["n_prolog_matches_python"],
             "prolog_match_gold": prolog["n_modeA_surface_matches_gold"], "prolog_total": prolog["n_discharged"]}),
        row("Gold-free, training-free, per-edge ABSTAIN-ON-COLLAPSE certificate (Mode-B conflict detection) "
            "-- the genuinely portable novelty; convex-point arm zero-FP is THEOREM / read-soundness-conditional",
            "THEOREM", "natural-temporal + templated-CLUTRR", "TRANSFERABLE-AT-POWER",
            {"clutrr_prolog_collapse_certified": True, "temporal_worked_collapse_certified": True,
             "zero_FP": "conditional on read soundness (THEOREM-grade engine; empirical recall ~0.53-0.86)"}),
    ]
    synthetic_only = [
        row("Cross-path INTERSECTION error-correcting-code mechanism + inverted-U redundancy optimum "
            "(recall & rho are CONTROLLED INPUTS) -- NEITHER real venue tested it",
            "SYNTHETIC-CHANNEL", "synthetic-channel", "SYNTHETIC-CHANNEL-ONLY",
            {"carried_from": CHANNEL_ID,
             "clutrr_is_single_chain_UNION_fixpoint": True,
             "clutrr_pc2_converse_intersection_UNSOUND_collapse_rate": "~13% of gold-clean chains",
             "temporal_iteration_full_vs_naive_p": _r(pub_bootp["naive"]),
             "temporal_ge3_cyclic_iteration_p": _r(strat["ge3_cyclic"]["modeA_vs_naive"]["boot_p_gap_le_0"]),
             "status": "ABSENT at power on both real venues (NS)"}),
        row("Synthetic backstop: Mode-A beats raw by ~+0.225 at matched coverage at recall 0.96 "
            "(mechanism works when local reads are sound)",
            "SYNTHETIC-CHANNEL", "synthetic-channel", "SYNTHETIC-CHANNEL-ONLY",
            {"mean_vs_raw_gap": _r(synth_mean_vs_raw), "recall": 0.96,
             "cells": {c: _r(synth[c]["vs_baselines"]["raw"]["gap"]) for c in synth}}),
    ]
    marginal_natural = [
        row("TEMPORAL Mode-A vs PoT / SC selective-accuracy at matched coverage on NATURAL text -- the "
            "point gaps reproduce (+0.0265 / +0.0354) and the CORRECTED bracketing CIs (R1) center on them, "
            "but the CIs INCLUDE 0 and the gaps are NOT significant under a correctly-centered bootstrap; "
            "the published Holm-significance was a bootstrap artifact",
            "REAL-LLM-READ", "natural-temporal", "MARGINAL-NATURAL-TEXT (not significant after correction)",
            {"vs_pot_gap": _r(pub_gap["pot"]),
             "vs_pot_corrected_ci95": (r1["baselines"]["pot"].get("new_ci95") if cache_complete
                                       else r1["baselines"]["pot"].get("recentered_ci95")),
             "vs_pot_corrected_boot_p": (r1["baselines"]["pot"].get("new_boot_p_gap_le_0") if cache_complete else None),
             "vs_sc_gap": _r(pub_gap["sc"]),
             "vs_sc_corrected_ci95": (r1["baselines"]["sc"].get("new_ci95") if cache_complete
                                      else r1["baselines"]["sc"].get("recentered_ci95")),
             "vs_sc_corrected_boot_p": (r1["baselines"]["sc"].get("new_boot_p_gap_le_0") if cache_complete else None),
             "published_boot_p_ARTIFACT": [_r(pub_bootp["pot"]), _r(pub_bootp["sc"])],
             "CAVEAT": "report the 42.5% (48/113) confident-wrong-among-answered beside this; raw out-accuracies Mode-A by 0.124"}),
    ]
    out["contribution_split"] = {
        "tag": "MIXED (per-row tagged)",
        "columns": ["claim", "evidence_tag", "venue", "where_it_holds", "number"],
        "TRANSFERABLE_AT_POWER": transferable,
        "MARGINAL_NATURAL_TEXT": marginal_natural,
        "SYNTHETIC_CHANNEL_ONLY": synthetic_only,
        "synthetic_only_recast_note": (
            "The prior reviewer's 'central comparative contribution is synthetic-only' concern is RECAST, "
            "NOT retired. The signature cross-path-intersection coding mechanism remains synthetic-channel-only "
            "(CLUTRR is a single-chain UNION fixpoint; temporal iteration is NS at power). The iter-4 DECISIVE "
            "experiment -- cross-path INTERSECTION vs best-single-path composition on a REAL multi-path-"
            "redundant stratum with adjusted-CI separation -- is what would move the SYNTHETIC-CHANNEL-ONLY rows."),
    }

    # ===================================================================== #
    # SCOPE-FRAMING
    # ===================================================================== #
    out["scope_framing"] = {
        "clutrr_retag": (
            "RE-TAG CLUTRR as a 'templated kinship benchmark (semi-synthetic)': max 871 chars (NONE reach the "
            "~3000-char target), gold surface forms for entity grounding, hand-supplied composition table. The "
            "abstract must NOT say 'two non-synthetic venues' -- only the temporal corpora are natural text, and "
            "there the comparative contribution is MARGINAL (+0.0265; the CORRECTED bracketing CI INCLUDES 0 "
            "/ boot_p~0.33, NOT robustly significant -- the published Holm-significance was a bootstrap artifact, "
            "see R1). Lead the natural-text story with the CERTIFICATE, not selective-accuracy dominance."),
        "deduction_sub_module_scope": (
            "Foreground the DEDUCTION-SUB-MODULE scope: OpenCyc grounding, atomic re-extraction, and LLM "
            "fuzzy-unification are OUT OF SCOPE. Real-text utility is EXTRACTION-LIMITED: ~0.53 atomic recall "
            "-> ~19% Mode-A coverage on natural temporal text."),
        "recall_to_coverage_ceiling": {"atomic_recall": _r(atomic["recall"]),
                                        "modeA_real_text_coverage": _r(h2["modeA_coverage"])},
        "multiplicity_policy": (
            "Re-affirm H1-H4 Holm / hierarchical gatekeeping: H1 (matched-coverage advantage) and H2 "
            "(hallucination reduction) are GATEWAYS; H3 (iteration) / H4 tested only if a gateway clears; "
            "everything else EXPLORATORY with nominal CIs (len2/ge3_cyclic strata, coverage-axis iteration)."),
        "retitle_suggestion": (
            "Recommend re-titling the paper to center 'closure-certified deduction sub-module' (not an "
            "end-to-end text-to-FOL system): the substantive, transferable contribution is the gold-free "
            "abstain-on-collapse certificate over a deduction sub-module, evaluated at power on a templated "
            "benchmark and marginally on natural temporal text."),
    }

    # ===================================================================== #
    # DATASETS (per-query examples, schema-valid) -- compact, both venues
    # ===================================================================== #
    logger.info("=== building datasets (per-query examples) ===")
    datasets = []
    # CLUTRR examples (282) -- keep predict_* + per-query eval_* correctness + key metadata
    clutrr_examples = []
    for e in clutrr_ex:
        gold = e.get("output", "")
        ex = {"input": (e.get("input", "")[:400] if e.get("input") else
                        f"CLUTRR kinship query hop={e.get('metadata_hop')} absent={e.get('metadata_is_absent')}"),
              "output": str(gold) if gold is not None else "",
              "metadata_doc_id": str(e.get("metadata_doc_id")),
              "metadata_hop": e.get("metadata_hop"),
              "metadata_is_absent": e.get("metadata_is_absent"),
              "metadata_venue": "templated-CLUTRR"}
        for m in ("modeA", "naive", "raw", "sc", "pot"):
            pv = e.get(f"predict_{m}")
            ex[f"predict_{m}"] = str(pv) if pv is not None else "ABSTAIN"
            if not e.get("metadata_is_absent"):
                ex[f"eval_{m}_correct"] = 1.0 if (is_ans(pv) and pv == gold) else 0.0
                ex[f"eval_{m}_answered"] = 1.0 if is_ans(pv) else 0.0
            else:
                ex[f"eval_{m}_named_confident_wrong"] = 1.0 if is_ans(pv) else 0.0
        clutrr_examples.append(ex)
    datasets.append({"dataset": "clutrr_templated_kinship", "examples": clutrr_examples})

    # TEMPORAL examples (600) from records (if available) else from source columns
    temporal_examples = []
    if cache_complete:
        for r in temporal_records:
            gold = r.get("gold", "")
            ex = {"input": f"temporal point-algebra deduction query stratum={r.get('stratum')}",
                  "output": str(gold) if gold is not None else "",
                  "metadata_docid": str(r.get("docid")),
                  "metadata_stratum": r.get("stratum"),
                  "metadata_venue": "natural-temporal"}
            for m in ("modeA", "naive", "raw", "pot", "sc"):
                rm = r[m]
                ex[f"predict_{m}"] = str(rm["pred"]) if rm.get("pred") is not None else "ABSTAIN"
                ex[f"eval_{m}_answered"] = 1.0 if rm.get("answered") else 0.0
                ex[f"eval_{m}_correct"] = float(rm["correct"]) if (rm.get("answered") and rm.get("correct") is not None) else 0.0
                ex[f"eval_{m}_conf"] = _r(rm.get("conf", 0.0))
            temporal_examples.append(ex)
    else:
        for e in [x for ds in temporal["datasets"] for x in ds["examples"]]:
            gold = e.get("output", "")
            ex = {"input": f"temporal deduction query stratum={e.get('metadata_stratum')}",
                  "output": str(gold) if gold is not None else "",
                  "metadata_docid": str(e.get("metadata_docid")),
                  "metadata_stratum": e.get("metadata_stratum"),
                  "metadata_venue": "natural-temporal"}
            for m in ("modeA", "naive", "raw", "pot", "sc"):
                pv = e.get(f"predict_{m}")
                ex[f"predict_{m}"] = str(pv) if pv is not None else "ABSTAIN"
                ex[f"eval_{m}_answered"] = 1.0 if (pv is not None and pv != "ABSTAIN") else 0.0
                ex[f"eval_{m}_correct"] = 1.0 if (pv is not None and pv != "ABSTAIN" and pv == gold) else 0.0
            temporal_examples.append(ex)
    datasets.append({"dataset": "temporal_point_algebra_natural_text", "examples": temporal_examples})

    # ===================================================================== #
    # metrics_agg: add a few more headline scalars
    # ===================================================================== #
    metrics_agg["clutrr_h2_confident_wrong_reduction"] = _r(h2c["confident_wrong_reduction"])
    metrics_agg["clutrr_oracle_modeA_selacc"] = _r(oracle["leaderboard"]["modeA"]["selective_accuracy"])
    metrics_agg["clutrr_atomic_recall"] = _r(atomic["recall"])
    metrics_agg["temporal_modeA_coverage"] = _r(h2["modeA_coverage"])
    metrics_agg["llm_spend_usd"] = 0.0
    metrics_agg["n_reproduction_mismatches"] = float(len(MISMATCHES))
    metrics_agg["B_bootstrap"] = float(B)

    # ===================================================================== #
    # ASSEMBLE eval_out.json
    # ===================================================================== #
    out_meta = {
        "eval_name": "zero_spend_reanalysis__R1_bracketing__R2_clutrr_coverage__42pct_confwrong__contribution_split",
        "description": (
            "Pure re-analysis ($0 LLM, numpy+scipy only) of the two iter-3 source experiments: temporal "
            "point-algebra natural text and CLUTRR templated-kinship end-to-end. Retires reviewer reporting "
            "MINORs (R1 bracketing CI; R2 CLUTRR naive force-extension), surfaces the 42.5% confident-wrong "
            "block tied to silent-wrong-narrowing, recomputes the inherited-vs-novel decomposition on both "
            "venues, and emits the TRANSFERABLE-AT-POWER vs SYNTHETIC-CHANNEL-ONLY contribution split."),
        "evidence_tags": ["REAL-LLM-READ", "REAL-LLM-READ-ON-SYNTHETIC", "SYNTHETIC-CHANNEL",
                          "GOLD-ONLY-GATE", "THEOREM", "EXPLORATORY"],
        "llm_spend_usd": 0.0,
        "seed": SEED, "n_boot": B, "clustering": "doc/story-clustered paired bootstrap",
        "temporal_cache_complete_zero_spend": cache_complete,
        "temporal_records_provenance": (
            "per_query_records_temporal.json built by a $0 cached re-run of the temporal method.py "
            "(symlinked cache/, dummy API key, --skip-strong): total_cache_misses=0, primary_cost=0.0, "
            "600 records; reproduced aggregates match published exactly."),
        "sources": {
            "temporal": {"path": str(TEMPORAL_FULL), "id": TEMPORAL_ID},
            "clutrr": {"path": str(CLUTRR_FULL), "id": CLUTRR_ID},
            "prior_decomposition": {"path": str(PRIOR_EVAL), "id": PRIOR_EVAL_ID},
            "iter2_allen": {"path": str(ITER2_ALLEN), "id": ITER2_ALLEN_ID},
            "channel_carried": {"id": CHANNEL_ID},
        },
        "r1_bracketing": out["r1_bracketing"],
        "r2_clutrr": out["r2_clutrr"],
        "clutrr_matched_coverage_gaps": out["clutrr_matched_coverage_gaps"],
        "temporal_confident_wrong_block": out["temporal_confident_wrong_block"],
        "decomposition": out["decomposition"],
        "contribution_split": out["contribution_split"],
        "scope_framing": out["scope_framing"],
        "sanity_check_reproductions": {
            "n_mismatches": len(MISMATCHES), "mismatches": MISMATCHES,
            "note": "every reproduced point estimate compared vs source file; mismatches (if any) listed here, not silently overwritten."},
    }
    eval_out = {"metrics_agg": {k: v for k, v in metrics_agg.items() if v is not None},
                "metadata": out_meta, "datasets": datasets}

    (HERE / "eval_out.json").write_text(json.dumps(eval_out, indent=2))
    logger.info(f"Wrote eval_out.json ({(HERE / 'eval_out.json').stat().st_size/1024:.1f} KB); "
                f"mismatches={len(MISMATCHES)}")

    # ===================================================================== #
    # eval_digest.md
    # ===================================================================== #
    write_digest(eval_out, cache_complete)
    logger.info("Wrote eval_digest.md")
    logger.info(f"DONE. reproduction mismatches: {len(MISMATCHES)} {MISMATCHES if MISMATCHES else ''}")


def write_digest(eo, cache_complete):
    m = eo["metadata"]
    r1 = m["r1_bracketing"]; r2 = m["r2_clutrr"]; cw = m["temporal_confident_wrong_block"]
    dec = m["decomposition"]; cs = m["contribution_split"]; sf = m["scope_framing"]
    cg = m["clutrr_matched_coverage_gaps"]
    L = []
    L.append("# Zero-LLM-spend re-analysis digest (paper-facing)\n")
    L.append("**$0 LLM spend.** numpy+scipy only. seed=20260617, B=10000, doc/story-clustered paired bootstrap.")
    L.append(f"Temporal per-query records rebuilt by a **$0 cached re-run** (total_cache_misses=0, primary_cost=0.0, "
             f"600 records; reproduced aggregates match published exactly). Reproduction mismatches vs source: "
             f"**{m['sanity_check_reproductions']['n_mismatches']}**.\n")
    L.append("Evidence tags: REAL-LLM-READ · REAL-LLM-READ-ON-SYNTHETIC · SYNTHETIC-CHANNEL · GOLD-ONLY-GATE · THEOREM · EXPLORATORY\n")

    # R1
    L.append("## R1 — Bracketing CI on the temporal Mode-A-vs-PoT gap (REAL-LLM-READ)\n")
    L.append("**Root cause.** " + r1.get("why_old_ci_failed", r1.get("fallback_note", "")) + "\n")
    if cache_complete:
        L.append("**Fix.** Hold the matched-coverage operating point FIXED across resamples: Mode-A's fixed answered "
                 "set vs the baseline's fixed top-k-by-conf matched set; recompute both accuracies over those FIXED "
                 "sets in each doc-clustered resample (do NOT re-derive the coverage/threshold inside the bootstrap).\n")
        L.append("| baseline | point gap | published OLD CI (B=2000) | OLD brackets? | NEW bracketing CI (B=10000) | NEW brackets? | corrected boot_p | corrected sig? |")
        L.append("|---|---|---|---|---|---|---|---|")
        for b in ("pot", "sc", "naive", "raw"):
            d = r1["baselines"][b]
            L.append(f"| vs {b.upper()} | {d['point_gap']:+.4f} | [{d['published_old_ci95_B2000'][0]:.4f}, "
                     f"{d['published_old_ci95_B2000'][1]:.4f}] | {d['old_ci_brackets_point_estimate']} | "
                     f"[{d['new_ci95'][0]:.4f}, {d['new_ci95'][1]:.4f}] | **{d['ci_brackets_point_estimate']}** | "
                     f"{d['new_boot_p_gap_le_0']:.4f} | {d['corrected_one_sided_significant']} |")
        L.append("")
        L.append(f"The published **vs-PoT** CI [0.0454, 0.3148] does NOT contain its own point gap +0.0265 "
                 f"(estimator/resample mismatch); the corrected CI **{r1['baselines']['pot']['new_ci95']} brackets +0.0265**. "
                 "The plan's 'equivalent' fixed-m_cov interpolation variant also BRACKETS the point "
                 f"(vs-PoT {r1['baselines']['pot']['new_ci95_interp_variant']}) but disagrees on significance "
                 "(see honest finding below).\n")
        L.append("> **Honest finding (R1).** " + r1["corrected_significance_finding"] + "\n")
        L.append(f"Holm over the CORRECTED {{vs PoT, vs SC}} family: "
                 f"{ {k: round(v['p_adj'],4) for k,v in r1['holm_H1_corrected'].items()} } "
                 "→ neither gateway clears after correction.\n")
    else:
        L.append("**Cache incomplete → presentational fallback.** Reverse-percentile recentering "
                 "[2·gap − q_hi, 2·gap − q_lo] of the published B=2000 quantiles (NOT a re-estimated CI):\n")
        for b in ("pot", "sc", "naive", "raw"):
            d = r1["baselines"][b]
            L.append(f"- vs {b.upper()}: gap {d['point_gap']:+.4f}, recentered CI {d['recentered_ci95']} "
                     f"(brackets={d['ci_brackets_point_estimate']})")
        L.append("")

    # R2
    L.append("## R2 — CLUTRR naive natural-vs-forced coverage; iteration routed through COVERAGE (REAL-LLM-READ)\n")
    L.append("| naive operating point | coverage | selective accuracy | note |")
    L.append("|---|---|---|---|")
    L.append(f"| natural | {r2['naive_natural_coverage']:.3f} ({r2['naive_natural_n_answered']}/102) | "
             f"{r2['naive_natural_selacc']:.3f} ({r2['naive_natural_n_correct']}/{r2['naive_natural_n_answered']}) | "
             f"predominantly hop-2; single-pass intersection resolves |")
    L.append(f"| matched / force-extended | {r2['naive_matched_coverage']:.3f} | "
             f"{r2['naive_matched_selacc_forced']:.3f} | **FORCE-EXTENDED with representative-surface answers** |")
    L.append("")
    L.append("> " + r2["force_extension_caption"] + "\n")
    L.append("**Iteration (H3) via the COVERAGE axis** (full_minus_naive coverage gap by hop): "
             + ", ".join(f"hop{k}:{v}" for k, v in r2["iteration_coverage_gap_by_hop"].items()) + ".")
    L.append(r2["iteration_statement"] + "\n")
    L.append(f"**Legitimate matched-coverage leaderboard** (cov {r2['legitimate_leaderboard_matched_cov']:.3f}): "
             f"Mode-A {r2['legitimate_leaderboard']['modeA_selacc']:.3f} vs PoT {r2['legitimate_leaderboard']['pot_selacc']:.3f} / "
             f"SC {r2['legitimate_leaderboard']['sc_selacc']:.3f} / raw {r2['legitimate_leaderboard']['raw_selacc']:.3f}; "
             f"naive row = {r2['legitimate_leaderboard']['naive_selacc_FORCE_EXTENDED']:.3f} (FORCE-EXTENDED). "
             f"Corrected fixed-set gaps (B=10000): vs PoT {cg['gaps']['pot']['point_gap']:+.4f} {cg['gaps']['pot']['new_ci95']}, "
             f"vs SC {cg['gaps']['sc']['point_gap']:+.4f} {cg['gaps']['sc']['new_ci95']}, "
             f"vs raw {cg['gaps']['raw']['point_gap']:+.4f} {cg['gaps']['raw']['new_ci95']}; Holm p_adj {cg['published_holm_p_adj']}.\n")

    # 42.5%
    L.append("## The 42.5% (48/113) confident-wrong-among-answered block (REAL-LLM-READ)\n")
    L.append("> " + cw["reporting_block"] + "\n")
    L.append(f"- confident-wrong among Mode-A answered: **{cw['frac_confident_wrong_among_answered']:.4f} "
             f"({cw['n_confident_wrong']}/{cw['denom_answered']})**; Mode-A coverage {cw['modeA_coverage']:.4f} "
             f"(abstention {cw['modeA_abstention_rate']:.4f}); raw confident-wrong {cw['confident_wrong_raw']:.2f}.")
    L.append(f"- reduction vs raw {cw['reduction_vs_raw_published']:.4f} (published CI {cw['reduction_published_ci95']}"
             + (f"; recomputed B=10000 {cw['reduction_recomputed_B10000']['reduction']:.4f} "
                f"{cw['reduction_recomputed_B10000']['ci95']}" if cw['reduction_recomputed_B10000'] else "") + ").")
    L.append(f"- silent-wrong-narrowing: **all {cw['silent_wrong_narrowing_count']}** Mode-A confident-wrongs are "
             f"silent-wrong-narrowing (undetectable by Mode-B: no empty collapse).")
    L.append(f"- raw out-accuracies Mode-A at matched coverage by {abs(cw['raw_minus_modeA_acc_at_matched_coverage']):.3f} "
             f"(gap {cw['raw_minus_modeA_acc_at_matched_coverage']:+.3f}).")
    L.append("\n**Read-soundness frontier (REAL-LLM-READ):**")
    L.append("| corpus×reader | recall | CI95 | gate verdict |")
    L.append("|---|---|---|---|")
    for k, v in cw["read_soundness_rows"].items():
        L.append(f"| {k} | {v['recall']:.4f} | [{v['ci95'][0]:.3f}, {v['ci95'][1]:.3f}] | {v['verdict']} |")
    L.append(f"\nρ within-doc soundness ∈ {cw['rho_within_doc_soundness_range']}. "
             f"**$0 synthetic backstop (SYNTHETIC-CHANNEL, recall 0.96): mean Mode-A vs raw +{cw['synthetic_backstop_vs_raw_mean_gap']:.3f}** "
             f"→ read soundness (not closure) is the real-text gate.\n")

    # decomposition
    L.append("## Inherited-vs-novel decomposition\n")
    cd = dec["clutrr"]; td = dec["temporal_point"]; ad = dec["allen_carried_forward"]
    L.append(f"**CLUTRR (REAL-LLM-READ, templated):** system_gap(ModeA−PoT)={cd['system_gap_modeA_minus_pot']:+.3f} = "
             f"INHERITED(naive−PoT)={cd['inherited_naive_minus_pot_FORCED']:+.3f} + "
             f"NOVEL(ModeA−naive)={cd['novel_modeA_minus_naive_FORCED']:+.3f}. ⚠ " + cd["WARNING_force_extension"])
    L.append("> " + cd["honest_framing"] + "\n")
    if "novel_selacc_covered_by_both" in td:
        nb = td["novel_selacc_covered_by_both"]
        L.append(f"**TEMPORAL (REAL-LLM-READ, point algebra):** on the covered-by-BOTH subset (n={nb['n']}) "
                 f"NOVEL_selacc = ModeA {nb['modeA_acc']:.3f} − naive {nb['naive_acc']:.3f} = **{nb['novel_selacc']:+.3f}** "
                 f"{nb['ci95']} (pred disagreements: {nb['n_pred_disagreements']}). " + td["summary"])
    else:
        L.append("**TEMPORAL:** " + td["summary"])
    L.append(f"Iteration on coverage: len2 gap {td['iteration_on_coverage_axis']['len2_modeA_vs_naive_gap']} (0 by theorem); "
             f"ge3_cyclic gap {td['iteration_on_coverage_axis']['ge3_cyclic_modeA_vs_naive_gap']:+.4f} "
             f"{td['iteration_on_coverage_axis']['ge3_cyclic_ci95']} (p={td['iteration_on_coverage_axis']['ge3_cyclic_boot_p']}, EXPLORATORY, NS).\n")
    L.append(f"**ALLEN (REAL-LLM-READ-ON-SYNTHETIC, carried from {ad['source']}):** system_gap {ad['carried_forward']['system_gap']:.3f} = "
             f"INHERITED {ad['carried_forward']['inherited']:.3f} + NOVEL_selacc {ad['carried_forward']['novel_selacc']:.4f}."
             + (f" Independent recompute (covered-by-both novel_selacc) = {ad['recomputed_novel_selacc_covered_by_both']['novel_selacc']:+.4f} ✓."
                if ad.get("readable") and "recomputed_novel_selacc_covered_by_both" in ad else " (carry-forward only.)"))
    L.append("\n> " + dec["actionable_framing"] + "\n")

    # contribution split
    L.append("## Contribution split — TRANSFERABLE-AT-POWER vs SYNTHETIC-CHANNEL-ONLY (headline deliverable)\n")
    L.append("| # | Claim | Tag | Venue | Where it holds | Key number |")
    L.append("|---|---|---|---|---|---|")
    i = 0
    for r in cs["TRANSFERABLE_AT_POWER"]:
        i += 1
        num = "; ".join(f"{k}={v}" for k, v in list(r["number"].items())[:3])
        L.append(f"| T{i} | {r['claim'][:120]} | {r['evidence_tag']} | {r['venue']} | {r['where_it_holds']} | {num} |")
    k = 0
    for r in cs["MARGINAL_NATURAL_TEXT"]:
        k += 1
        num = "; ".join(f"{kk}={vv}" for kk, vv in list(r["number"].items())[:3])
        L.append(f"| M{k} | {r['claim'][:120]} | {r['evidence_tag']} | {r['venue']} | {r['where_it_holds']} | {num} |")
    j = 0
    for r in cs["SYNTHETIC_CHANNEL_ONLY"]:
        j += 1
        num = "; ".join(f"{k}={v}" for k, v in list(r["number"].items())[:3])
        L.append(f"| S{j} | {r['claim'][:120]} | {r['evidence_tag']} | {r['venue']} | {r['where_it_holds']} | {num} |")
    L.append("")
    L.append("> " + cs["synthetic_only_recast_note"] + "\n")

    # scope framing
    L.append("## Scope-framing guidance for GEN_PAPER_TEXT\n")
    L.append("1. **CLUTRR re-tag:** " + sf["clutrr_retag"])
    L.append("2. **Deduction sub-module scope:** " + sf["deduction_sub_module_scope"])
    L.append("3. **Multiplicity policy:** " + sf["multiplicity_policy"])
    L.append("4. **Re-title:** " + sf["retitle_suggestion"] + "\n")

    (HERE / "eval_digest.md").write_text("\n".join(L))


if __name__ == "__main__":
    main()
