#!/usr/bin/env python3
"""Zero-spend iter-5 re-analysis (numpy+scipy only, deterministic, B=10000 paired bootstrap).

EXTENDS the validated iter-4 re-analysis at
  iter_4/gen_art/gen_art_evaluation_1/eval_out.json
with three deliverables for GEN_PAPER_TEXT:

  STEP 0  reproduce & reuse iter-4 headline numbers (sanity gate, mismatch ledger).
  STEP 1  (MINOR #5a) SYNTHETIC ALLEN CONTROL -- bootstrap CIs on BOTH the small cross-path
          COVERAGE bite (+0.024) AND the large SELECTIVE-ACCURACY gain (+0.259), so the paper
          can state the realized bite is small and the practical win is PRECISION of committed
          answers, not coverage expansion.
  STEP 2  (MINOR #5b) INVERTED-U -- recover REALIZED Mode-A coverage per redundancy bin
          (benefit + cost_silent_wrong = 1 - abstain - collapse) from the stored H4 curves,
          with Wilson / Newcombe CIs; reframe inverted-U as precision, not coverage.
  STEP 3  (MAJOR #3) ONE-THESIS CONTRIBUTION TABLE with evidence tags as COLUMNS, a two-row
          SPINE (certificate; read-informativeness impossibility), supporting + footnote rows,
          and a PENDING spatial-RCC-8 slot.

NO new LLM calls, NO dataset downloads, NO method re-execution beyond the $0 synthetic Allen
positive control (numpy-only). Every number is tagged; tags live in COLUMNS, never inline prose.
"""
from __future__ import annotations

import gc
import json
import math
import resource
import sys
from pathlib import Path

import numpy as np
from loguru import logger

# ----------------------------------------------------------------------------- logging
Path("logs").mkdir(exist_ok=True)
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# ----------------------------------------------------------------------------- memory cap
# Tiny re-analysis (<=10000 x 500 float64 bootstrap matrices ~ a few hundred MB). Cap at 8 GB.
_RAM_BUDGET = 8 * 1024 ** 3
resource.setrlimit(resource.RLIMIT_AS, (_RAM_BUDGET, _RAM_BUDGET))

# ----------------------------------------------------------------------------- constants
SEED = 20260617
B_BOOT = 10000
ALPHA = 0.05
Z = 1.959963984540054  # norm.ppf(0.975)

RUN_ROOT = "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop"
WS = Path(RUN_ROOT) / "iter_5/gen_art/gen_art_evaluation_1"

# Dependency artifacts (exact paths + ids from the artifact plan).
SRC = {
    "iter4_eval": {
        "id": "art_D0cHQUJ8kY75_iter4eval",
        "path": f"{RUN_ROOT}/iter_4/gen_art/gen_art_evaluation_1/eval_out.json",
    },
    "synth_allen_control": {
        "id": "art_0AIWMhwc1pJM",
        "path": f"{RUN_ROOT}/iter_4/gen_art/gen_art_experiment_1/full_method_out.json",
        "workspace": f"{RUN_ROOT}/iter_4/gen_art/gen_art_experiment_1",
    },
    "inverted_u_channel": {
        "id": "art_FtN4LBzazO_l",
        "path": f"{RUN_ROOT}/iter_2/gen_art/gen_art_experiment_2/full_method_out.json",
    },
    "clutrr_certificate": {
        "id": "art_0a7i481ZRwS1",
        "path": f"{RUN_ROOT}/iter_3/gen_art/gen_art_experiment_1/full_method_out.json",
    },
    "temporal_corrected": {
        "id": "art_OETjJkketEVS",
        "path": f"{RUN_ROOT}/iter_3/gen_art/gen_art_experiment_2/full_method_out.json",
    },
}


def load_json(path: str) -> dict:
    return json.loads(Path(path).read_text())


# ============================================================================
# Bootstrap / CI helpers.
#   - clustered_bootstrap_ci / matched_coverage_gap / holm_bonferroni are COPIED
#     VERBATIM from iter_4/.../gen_art_evaluation_1/rerun_temporal/method.py
#     (carried for traceability; the temporal numbers they produced are reused, not
#     recomputed here).
#   - The synthetic Allen control uses a dedicated i.i.d. PAIRED bootstrap (networks
#     are independent, NOT doc-clustered).
# ============================================================================
def clustered_bootstrap_ci(doc_to_vals, B=B_BOOT, seed=SEED, alpha=ALPHA):
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


def wilson_ci(x: int, n: int, z: float = Z):
    """Wilson score interval for a single proportion x/n."""
    if n == 0:
        return [float("nan"), float("nan")]
    p = x / n
    denom = 1.0 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return [float(center - half), float(center + half)]


def newcombe_diff_ci(x1: int, n1: int, x2: int, n2: int, z: float = Z):
    """Newcombe (method 10) score interval for the difference of two INDEPENDENT
    proportions p1 - p2 (each (recall,K) cell is an independent 600-network draw)."""
    l1, u1 = wilson_ci(x1, n1, z)
    l2, u2 = wilson_ci(x2, n2, z)
    p1, p2 = x1 / n1, x2 / n2
    lo = (p1 - p2) - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    hi = (p1 - p2) + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return [float(lo), float(hi)]


# ============================================================================
# STEP 0 -- reproduce & reuse iter-4 (sanity gate)
# ============================================================================
def step0_sanity(iter4: dict) -> dict:
    logger.info("STEP 0 -- reproducing iter-4 headline numbers (sanity gate)")
    ma = iter4["metrics_agg"]
    md = iter4["metadata"]
    mismatches = []

    def check(name, got, expected, tol=1e-4):
        ok = (got is not None) and (abs(float(got) - expected) <= tol)
        if not ok:
            mismatches.append({"name": name, "got": got, "expected": expected})
            logger.error(f"  MISMATCH {name}: got={got} expected={expected}")
        else:
            logger.info(f"  OK {name} = {got}")
        return ok

    # Headline numbers that feed the spine / footnotes.
    check("clutrr_modeA_selacc", ma.get("clutrr_modeA_selacc"), 0.885714)
    check("clutrr_modeA_vs_pot_gap", ma.get("clutrr_modeA_vs_pot_gap"), 0.428571)
    pot_ci = md["clutrr_matched_coverage_gaps"]["gaps"]["pot"]["new_ci95"]
    check("clutrr_vs_pot_ci_lo", pot_ci[0], 0.298589, tol=1e-3)
    check("clutrr_vs_pot_ci_hi", pot_ci[1], 0.563015, tol=1e-3)
    check("temporal_vs_pot_ci_lo", ma.get("temporal_modeA_vs_pot_new_ci_lo"), -0.088276)
    check("temporal_vs_pot_ci_hi", ma.get("temporal_modeA_vs_pot_new_ci_hi"), 0.139723)
    check("temporal_vs_pot_boot_p", ma.get("temporal_modeA_vs_pot_new_boot_p"), 0.3322)
    check("temporal_confident_wrong_frac", ma.get("temporal_confident_wrong_frac"), 0.424779)
    cw = md["temporal_confident_wrong_block"]
    check("temporal_confident_wrong_n", cw["n_confident_wrong"], 48, tol=0.5)
    check("temporal_confident_wrong_denom", cw["denom_answered"], 113, tol=0.5)

    logger.info(f"STEP 0 done: {len(mismatches)} mismatch(es)")
    return {"n_mismatches": len(mismatches), "mismatches": mismatches,
            "note": "every reproduced point estimate compared vs the iter-4 validated "
                    "eval_out.json; mismatches (if any) listed here, never silently overwritten."}


# ============================================================================
# STEP 1 (MINOR #5a) -- SYNTHETIC ALLEN CONTROL: small coverage bite vs large precision gain
# ============================================================================
def _rows_via_synth_allen(n_net: int, r: float, seed: int):
    """Re-run the $0 synthetic Allen positive control EXACTLY as the iter-4 experiment did
    (SA.run_control body), but ALSO expose the per-network rows. Mirrors
    synth_allen.run_control(n_net, r, seed) draw-for-draw so the aggregate reproduces the
    published recall_95 cell. Also returns a parallel VERBOSE view (true relation + resolved
    set per method) for worked examples, computed from a fresh, identically-seeded RNG."""
    sys.path.insert(0, SRC["synth_allen_control"]["workspace"])
    import engine  # noqa: F401  (imported by synth_allen)
    import synth_allen as SA

    AL = SA.AL

    # --- authoritative loop: identical to SA.run_control, capturing rows -------------
    rng = np.random.default_rng(seed)
    full_rows = [SA.run_one(6, r, rng) for _ in range(n_net)]
    rows = {m: [fr[m] for fr in full_rows] for m in ("intersection", "best_single", "naive")}

    # --- verbose loop: identical draw sequence, capturing true_q + resolved sets ------
    def run_one_verbose(n_events, rr, rg):
        intervals = SA.gen_network(n_events, rg)
        nodes = list(range(n_events))
        s, t = 0, 1
        vias = nodes[2:]
        true_q = SA._atomic(intervals, s, t)
        qcn = engine.QCN(AL, nodes)
        reads, confs = {}, {}
        induced = [(s, w) for w in vias] + [(w, t) for w in vias]
        for i in range(len(vias)):
            for j in range(i + 1, len(vias)):
                induced.append((vias[i], vias[j]))
        for (a, b) in induced:
            tr = SA._atomic(intervals, a, b)
            rd = SA.simulate_read(tr, rr, rg)
            reads[(a, b)] = rd
            confs[(a, b)] = float(min(1.0, max(0.0, rg.normal(0.7, 0.15))))
            qcn.set_edge(qcn.index[a], qcn.index[b], rd)
        qi, qj = qcn.index[s], qcn.index[t]
        naive_set = engine.naive_single_pass(qcn, qi, qj)
        per_path = [AL.compose(reads[(s, w)], reads[(w, t)]) for w in vias]
        best = min(per_path, key=len) if per_path else AL.universe
        ok, _ = engine.pc2_full(qcn)
        inter = AL.empty if not ok else qcn.get(qi, qj)

        def render(R):
            if not R:
                return "ABSTAIN(collapse-empty)"
            if len(R) == 1:
                return str(next(iter(R)))
            return "ABSTAIN(disjunction:" + "|".join(sorted(str(x) for x in R)) + ")"
        return {"true_q": str(true_q), "intersection_set": sorted(str(x) for x in inter),
                "best_single_set": sorted(str(x) for x in best),
                "naive_set": sorted(str(x) for x in naive_set),
                "intersection_pred": render(inter), "best_single_pred": render(best),
                "naive_pred": render(naive_set),
                "bite": len(best) - len(inter)}

    rng2 = np.random.default_rng(seed)
    verbose = [run_one_verbose(6, r, rng2) for _ in range(n_net)]
    return rows, full_rows, verbose


def _to_arrays(rows):
    """answered (0/1) and correct (0/1, 0 where not answered) per method as numpy arrays."""
    out = {}
    for m, recs in rows.items():
        ans = np.array([1.0 if x["answered"] else 0.0 for x in recs])
        cor = np.array([float(x["correct"]) if (x["answered"] and x["correct"] is not None)
                        else 0.0 for x in recs])
        out[m] = (ans, cor)
    return out


def step1_synth_allen(published_cell: dict) -> dict:
    logger.info("STEP 1 (MINOR #5a) -- synthetic Allen control small-bite, paired bootstrap")
    n_net, r = 500, 0.95
    seed_cell = SEED + int(r * 100)  # 20260617 + 95 = 20260712
    logger.info(f"  reproducing recall_95 cell: SA.run_control(n_net={n_net}, r={r}, seed={seed_cell})")
    rows, full_rows, verbose = _rows_via_synth_allen(n_net, r, seed_cell)

    arr = _to_arrays(rows)
    agg = {}
    for m, (ans, cor) in arr.items():
        cov = float(ans.mean())
        sel = float(cor[ans > 0].sum() / ans.sum()) if ans.sum() > 0 else float("nan")
        agg[m] = {"coverage": cov, "selective_acc": sel,
                  "n_answered": int(ans.sum()), "n_correct": int(cor.sum())}
        logger.info(f"    {m}: coverage={cov:.4f} selective_acc={sel:.4f} "
                    f"(answered={int(ans.sum())} correct={int(cor.sum())})")

    # ----- precision decomposition (where intersection's precision advantage comes from) -----
    ai, ci = arr["intersection"]
    ab, cb = arr["best_single"]
    both_m = (ai > 0) & (ab > 0)
    inter_only_m = (ai > 0) & (ab == 0)
    best_only_m = (ab > 0) & (ai == 0)
    precision_decomposition = {
        "n_both_resolve": int(both_m.sum()),
        "n_intersection_only": int(inter_only_m.sum()),
        "n_best_single_only": int(best_only_m.sum()),
        "both_resolve_intersection_correct": int(ci[both_m].sum()),
        "both_resolve_best_single_correct": int(cb[both_m].sum()),
        "intersection_only_correct": int(ci[inter_only_m].sum()),
        "intersection_only_acc": float(ci[inter_only_m].sum() / max(1, inter_only_m.sum())),
        "best_single_only_correct_kept": int(cb[best_only_m].sum()),
        "best_single_only_WRONG_avoided_by_collapse": int(best_only_m.sum() - cb[best_only_m].sum()),
        "note": ("Intersection's precision (0.976) beats best-single (0.717) through TWO channels, "
                 "NOT by re-scoring shared queries: (1) on the queries BOTH resolve, intersection "
                 "narrows to the SAME singleton best-single found (perfect agreement); (2) on "
                 "queries only intersection resolves (cross-path bite), it is ~96% correct; (3) on "
                 "queries only best-single resolves, intersection COLLAPSES (abstains) -- avoiding "
                 "best-single's wrong commitments instead of guessing. The coverage gain is small "
                 "(+2.4%) but the avoided-wrong-commitments + high-precision extra coverage drive "
                 "the precision advantage."),
    }
    logger.info(f"  precision decomposition: both={precision_decomposition['n_both_resolve']} "
                f"inter_only={precision_decomposition['n_intersection_only']} "
                f"(acc {precision_decomposition['intersection_only_acc']:.2f}) "
                f"best_only={precision_decomposition['n_best_single_only']} "
                f"(wrong avoided by collapse="
                f"{precision_decomposition['best_single_only_WRONG_avoided_by_collapse']})")

    # ----- BLOCKING reproduction check vs published recall_95 cell -----
    pub = published_cell["per_method"]
    repro_ok = True
    repro_detail = {}
    for m in ("intersection", "best_single", "naive"):
        dcov = abs(agg[m]["coverage"] - pub[m]["coverage"])
        dsel = abs(agg[m]["selective_acc"] - pub[m]["selective_acc"])
        repro_detail[m] = {"d_coverage": dcov, "d_selective_acc": dsel}
        if dcov > 1e-6 or dsel > 1e-6:
            repro_ok = False
    dgain = abs((agg["intersection"]["coverage"] - agg["best_single"]["coverage"])
                - published_cell["coverage_gain_intersection_vs_best"])
    if dgain > 1e-6:
        repro_ok = False
    logger.info(f"  reproduction check: {'PASS' if repro_ok else 'FAIL'} "
                f"(max coverage_gain diff {dgain:.2e})")

    cov_gain_point = agg["intersection"]["coverage"] - agg["best_single"]["coverage"]
    sel_gain_point = agg["intersection"]["selective_acc"] - agg["best_single"]["selective_acc"]

    if repro_ok:
        # ---------- PAIRED bootstrap over the 500 networks (same indices for both) ----------
        rng = np.random.default_rng(SEED)
        ai, ci = arr["intersection"]
        ab, cb = arr["best_single"]
        an, cn = arr["naive"]
        both = (ai > 0) & (ab > 0)  # networks BOTH intersection and best-single resolve

        cg, sg, sg_aligned = [], [], []
        cov_b = {m: [] for m in ("intersection", "best_single", "naive")}
        sel_b = {m: [] for m in ("intersection", "best_single", "naive")}
        idx_all = rng.integers(0, n_net, size=(B_BOOT, n_net))
        for bidx in range(B_BOOT):
            idx = idx_all[bidx]
            covi = ai[idx].mean(); covb = ab[idx].mean(); covn = an[idx].mean()
            di = ai[idx].sum(); db = ab[idx].sum(); dn = an[idx].sum()
            seli = ci[idx][ai[idx] > 0].sum() / di if di > 0 else np.nan
            selb = cb[idx][ab[idx] > 0].sum() / db if db > 0 else np.nan
            seln = cn[idx][an[idx] > 0].sum() / dn if dn > 0 else np.nan
            cg.append(covi - covb)
            sg.append(seli - selb)
            cov_b["intersection"].append(covi); cov_b["best_single"].append(covb); cov_b["naive"].append(covn)
            sel_b["intersection"].append(seli); sel_b["best_single"].append(selb); sel_b["naive"].append(seln)
            # aligned: among networks BOTH resolve in this resample, fraction correct each
            bm = both[idx]
            dboth = bm.sum()
            if dboth > 0:
                ia = ci[idx][bm].sum() / dboth
                ba = cb[idx][bm].sum() / dboth
                sg_aligned.append(ia - ba)
        cg = np.array(cg); sg = np.array(sg); sg_aligned = np.array(sg_aligned)

        def pctci(a):
            a = a[~np.isnan(a)]
            return [float(np.quantile(a, ALPHA / 2)), float(np.quantile(a, 1 - ALPHA / 2))]

        per_method = {}
        for m in ("intersection", "best_single", "naive"):
            per_method[m] = {
                "coverage": agg[m]["coverage"], "coverage_ci": pctci(np.array(cov_b[m])),
                "selective_acc": agg[m]["selective_acc"], "selacc_ci": pctci(np.array(sel_b[m])),
                "n_answered": agg[m]["n_answered"], "n_correct": agg[m]["n_correct"]}

        n_both = int(both.sum())
        ia_point = float(ci[both].sum() / n_both) if n_both else float("nan")
        ba_point = float(cb[both].sum() / n_both) if n_both else float("nan")
        result = {
            "recall": r, "n_net": n_net, "seed_cell": seed_cell, "B": B_BOOT,
            "reproduction_failed": False, "analytic_ci_fallback": False,
            "per_method": per_method,
            "coverage_gain_intersection_vs_best": {
                "point": float(cov_gain_point), "ci95": pctci(cg),
                "boot_p_le_0": float(np.mean(cg <= 0))},
            "selacc_gain_intersection_vs_best": {
                "point": float(sel_gain_point), "ci95": pctci(sg),
                "boot_p_le_0": float(np.mean(sg <= 0)),
                "note": "difference of the two per-resample SELECTIVE accuracies (different "
                        "denominators by construction: intersection answers more queries)."},
            "selacc_gain_aligned_both_resolve": {
                "n_both_resolve": n_both,
                "intersection_acc": ia_point, "best_single_acc": ba_point,
                "acc_gain": (ia_point - ba_point) if n_both else float("nan"),
                "ci95": pctci(sg_aligned) if len(sg_aligned) else [float("nan"), float("nan")],
                "note": "among queries BOTH methods resolve, intersection narrows to the SAME "
                        "singleton best-single found (inter is a SUBSET of best), so the aligned "
                        "selective-accuracy gain is ~0. The precision advantage comes from (a) "
                        "extra queries intersection resolves via cross-path bite and (b) "
                        "intersection COLLAPSING (abstaining) where best-single commits a wrong "
                        "singleton -- NOT from re-scoring the shared queries."},
            "mean_bite": published_cell["mean_bite"],
            "singleton_resolved_rate": published_cell["singleton_resolved_rate"],
            "reproduction_detail": repro_detail,
            "precision_decomposition": precision_decomposition,
            "tag": "SYNTHETIC-ALLEN-CONTROL",
            "interpretation": (
                "Intersection sets are a SUBSET of best-single sets (tighter), so intersection "
                "mechanically resolves a SUPERSET of queries WHEN it does not collapse -- but the "
                "REALIZED coverage gain is only +2.4% absolute (0.250 vs 0.226), while the "
                "selective-accuracy gain is large (+25.9 pts; 0.976 vs 0.717) and intersection's "
                "precision (0.976) exceeds BOTH best_single (0.717) AND naive (0.842) even though "
                "naive answers MORE (0.316). Structurally the only resolution-axis win is a "
                "coverage superset, but its realized MAGNITUDE is tiny; the practically meaningful "
                "effect is PRECISION OF COMMITTED ANSWERS, not coverage expansion."),
        }
    else:
        logger.error("  reproduction FAILED -> analytic (Wilson/Newcombe) CI fallback")
        per_method = {}
        for m in ("intersection", "best_single", "naive"):
            na = agg[m]["n_answered"]
            per_method[m] = {
                "coverage": agg[m]["coverage"],
                "coverage_ci": wilson_ci(na, n_net),
                "selective_acc": agg[m]["selective_acc"],
                "selacc_ci": wilson_ci(agg[m]["n_correct"], na) if na else [float("nan")] * 2,
                "n_answered": na, "n_correct": agg[m]["n_correct"]}
        ni = agg["intersection"]["n_answered"]; nb = agg["best_single"]["n_answered"]
        result = {
            "recall": r, "n_net": n_net, "seed_cell": seed_cell, "B": 0,
            "reproduction_failed": True, "analytic_ci_fallback": True,
            "per_method": per_method,
            "coverage_gain_intersection_vs_best": {
                "point": float(cov_gain_point),
                "ci95": newcombe_diff_ci(ni, n_net, nb, n_net),
                "boot_p_le_0": float("nan")},
            "selacc_gain_intersection_vs_best": {
                "point": float(sel_gain_point),
                "ci95": newcombe_diff_ci(agg["intersection"]["n_correct"], ni,
                                         agg["best_single"]["n_correct"], nb),
                "boot_p_le_0": float("nan")},
            "mean_bite": published_cell["mean_bite"],
            "singleton_resolved_rate": published_cell["singleton_resolved_rate"],
            "reproduction_detail": repro_detail,
            "precision_decomposition": precision_decomposition,
            "tag": "SYNTHETIC-ALLEN-CONTROL"}

    # ----- worked examples (a handful, with variety) -----
    worked = _build_worked_examples(full_rows, verbose, r)
    gc.collect()
    return result, worked


def _build_worked_examples(full_rows, verbose, r):
    """Select a varied handful of synthetic networks for the datasets[] worked-example block:
    cross-path bite wins, precision-via-collapse, agreement, and abstentions."""
    cats = {"bite_win": [], "precision_collapse": [], "agreement": [], "abstain": []}
    for i, (fr, vb) in enumerate(zip(full_rows, verbose)):
        inter, best = fr["intersection"], fr["best_single"]
        ia, ba = inter["answered"], best["answered"]
        if ia and not ba:
            cats["bite_win"].append((i, fr, vb))
        elif (not ia) and ba and best["correct"] == 0:
            cats["precision_collapse"].append((i, fr, vb))
        elif ia and ba:
            cats["agreement"].append((i, fr, vb))
        else:
            cats["abstain"].append((i, fr, vb))
    picked = []
    for c, k in (("bite_win", 3), ("precision_collapse", 2), ("agreement", 2), ("abstain", 1)):
        picked.extend(cats[c][:k])
    examples = []
    for i, fr, vb in picked:
        ex = {
            "input": (f"Synthetic Allen-13 QCN positive control (consistent-by-construction, "
                      f"n_events=6, reader recall={r}); network #{i}. Cross-path query relation "
                      f"between events 0 and 1; gold atomic Allen relation = '{vb['true_q']}'. "
                      f"Compare cross-path full-PC INTERSECTION vs BEST-SINGLE-PATH vs naive."),
            "output": vb["true_q"],
            "metadata_network_index": i,
            "metadata_recall": r,
            "metadata_bite": int(fr["bite"]),
            "metadata_singleton_resolved": int(fr["singleton_resolved"]),
            "metadata_intersection_set": vb["intersection_set"],
            "metadata_best_single_set": vb["best_single_set"],
            "metadata_naive_set": vb["naive_set"],
            "predict_intersection": vb["intersection_pred"],
            "predict_best_single": vb["best_single_pred"],
            "predict_naive": vb["naive_pred"],
            "eval_intersection_answered": 1.0 if fr["intersection"]["answered"] else 0.0,
            "eval_intersection_correct": float(fr["intersection"]["correct"] or 0)
                if fr["intersection"]["answered"] else 0.0,
            "eval_best_single_answered": 1.0 if fr["best_single"]["answered"] else 0.0,
            "eval_best_single_correct": float(fr["best_single"]["correct"] or 0)
                if fr["best_single"]["answered"] else 0.0,
            "eval_naive_answered": 1.0 if fr["naive"]["answered"] else 0.0,
            "eval_naive_correct": float(fr["naive"]["correct"] or 0)
                if fr["naive"]["answered"] else 0.0,
        }
        examples.append(ex)
    logger.info(f"  built {len(examples)} synthetic-Allen worked examples "
                f"({ {k: len(v) for k, v in cats.items()} })")
    return examples


# ============================================================================
# STEP 2 (MINOR #5b) -- INVERTED-U realized coverage per redundancy bin
# ============================================================================
def step2_inverted_u(channel: dict) -> dict:
    logger.info("STEP 2 (MINOR #5b) -- inverted-U realized coverage per redundancy bin")
    h4 = channel["metadata"]["H4"]
    sw = channel["metadata"]["silent_wrong_vs_recall"]
    n_bin = 600

    curves = [c for c in h4["curves"] if c["rho"] == 0.0 and c["gate"] == "off"]
    peaks = {round(p["recall"], 4): p for p in h4["peaks"]
             if p["rho"] == 0.0 and p["gate"] == "off"}
    recalls = sorted(set(c["recall"] for c in curves))

    by_recall = []
    max_cov_gain = -1.0
    for rc in recalls:
        cs = sorted([c for c in curves if c["recall"] == rc], key=lambda c: c["K"])
        Ks = [c["K"] for c in cs]
        realized = []  # benefit + cost_silent_wrong
        realized_chk = []  # 1 - abstain - collapse (identity check)
        benefit = []
        cost = []
        for c in cs:
            realized.append(c["benefit"] + c["cost_silent_wrong"])
            realized_chk.append(1.0 - c["abstain_rate"] - c["collapse_rate"])
            benefit.append(c["benefit"])
            cost.append(c["cost_silent_wrong"])
        # identity assertion
        assert all(abs(a - b) < 1e-9 for a, b in zip(realized, realized_chk)), \
            f"realized-coverage identity broken at recall={rc}"
        x_cov = [int(round(v * n_bin)) for v in realized]
        cov_ci = [wilson_ci(x, n_bin) for x in x_cov]
        x_k1 = x_cov[0]  # K==1 is first
        cov_gain_vs_k1 = [v - realized[0] for v in realized]
        cov_gain_ci = [newcombe_diff_ci(x, n_bin, x_k1, n_bin) for x in x_cov]
        pk = peaks.get(round(rc, 4))
        peak_K = pk["peak_K"] if pk else None
        # locate peak index
        pk_i = Ks.index(peak_K) if (peak_K in Ks) else int(np.argmax(benefit))
        max_cov_gain = max(max_cov_gain, max(cov_gain_vs_k1))
        by_recall.append({
            "recall": rc,
            "Ks": Ks,
            "peak_K": peak_K,
            "coverage_by_K": [float(v) for v in realized],
            "coverage_ci_by_K": cov_ci,
            "coverage_gain_vs_K1_by_K": [float(v) for v in cov_gain_vs_k1],
            "coverage_gain_vs_K1_ci_by_K": cov_gain_ci,
            "benefit_by_K": [float(v) for v in benefit],
            "cost_silent_wrong_by_K": [float(v) for v in cost],
            "at_peak": {
                "peak_K": peak_K,
                "realized_coverage": float(realized[pk_i]),
                "realized_coverage_ci": cov_ci[pk_i],
                "coverage_gain_vs_K1": float(cov_gain_vs_k1[pk_i]),
                "coverage_gain_vs_K1_ci": cov_gain_ci[pk_i],
                "benefit": float(benefit[pk_i]),
                "cost_silent_wrong": float(cost[pk_i]),
                "resolution_at_peak": pk["resolution_at_peak"] if pk else None,
                "resolution_at_K1": pk["resolution_at_K1"] if pk else None},
        })
        logger.info(f"    recall={rc} peak_K={peak_K} rc@peak={realized[pk_i]:.3f} "
                    f"cov_gain_vs_K1@peak={cov_gain_vs_k1[pk_i]:+.3f} "
                    f"benefit@peak={benefit[pk_i]:.3f} cost@peak={cost[pk_i]:.3f}")

    sw_curve = [{"recall": c["recall"],
                 "silent_wrong_rate_pooled": c["silent_wrong_rate_pooled"],
                 "silent_wrong_rate_ref_rho0_gateoff": c["silent_wrong_rate_ref_rho0_gateoff"]}
                for c in sw["curve"]]
    sw_pooled = [c["silent_wrong_rate_pooled"] for c in sw["curve"]]

    cov_gain_peak_by_recall = [{"recall": br["recall"], "peak_K": br["peak_K"],
                                "coverage_gain_vs_K1_at_peak": br["at_peak"]["coverage_gain_vs_K1"],
                                "cost_silent_wrong_at_peak": br["at_peak"]["cost_silent_wrong"]}
                               for br in by_recall]

    return {
        "tag": "SYNTHETIC-CHANNEL",
        "n_per_bin": n_bin,
        "rho": 0.0, "gate": "off",
        "by_recall": by_recall,
        "peak_K_by_recall": [br["peak_K"] for br in by_recall],
        "max_coverage_gain_vs_K1": float(max_cov_gain),
        "coverage_gain_vs_K1_at_peak_by_recall": cov_gain_peak_by_recall,
        "silent_wrong_vs_recall_pooled": sw_curve,
        "silent_wrong_min": float(min(sw_pooled)),
        "silent_wrong_max": float(max(sw_pooled)),
        "silent_wrong_rises": "0.006 -> 0.146 across recall (pooled; monotone-decreasing in recall)",
        "page_p_corrected": "~5e-4 (NOT the paper's earlier mis-stated 1e-13)",
        "recall_dependence_note": (
            "Realized-coverage gain over K=1 is RECALL-DEPENDENT, not uniformly modest: at the "
            "peak it rises from +0.135 (recall 0.50, where cost_silent_wrong 0.280 ~= benefit) to "
            "+0.612 (recall 0.95, cost ~0.000). The LARGE coverage gains live only in the "
            "high-recall regime where reads are near-sound -- exactly the regime LLMs do NOT reach "
            "on natural Allen text (the cross-path-bite experiment found per-edge reads "
            "near-universe / underdetermined). In the achievable regime (recall <=~0.85, and on "
            "Allen near-universe) the realized coverage bite is small."),
        "k1_vs_best_single_caveat": (
            "K=1 in the H4 channel is a SINGLE (arbitrary) contributing path, so coverage_gain_vs_K1 "
            "conflates redundancy with best-path SELECTION and OVERSTATES the cross-path bite. The "
            "conservative apples-to-apples measure is intersection vs the STRONGEST single path "
            "(best_single = min-cardinality composition): the synthetic Allen control gives only "
            "+0.024 there at recall 0.95 (bootstrap CI INCLUDES 0), while its selective-accuracy "
            "gain +0.259 is strongly significant. Both analyses agree: the practical value is "
            "PRECISION of committed answers, not coverage expansion."),
        "interpretation": (
            "The inverted-U on RESOLUTION (benefit) conflates two effects -- higher recall AND "
            "added redundancy. Decomposing onto the COVERAGE axis (realized coverage = benefit + "
            "cost_silent_wrong = 1 - abstain - collapse) shows that redundancy's realized coverage "
            "gain over K=1 is offset by a rising silent-wrong cost at low recall (cost grows with K "
            "as J(E) decays, then collapse dominates and coverage FALLS); the large coverage gains "
            "appear only at high recall (near-sound reads). Measured against the STRONGEST single "
            "path rather than an arbitrary K=1 path, the realized cross-path coverage bite is small "
            "(synthetic Allen control +2.4%, CI includes 0). The net practical value of the coding "
            "mechanism is therefore improved PRECISION of committed answers (fewer wrong singletons "
            "among those it commits to), not expanded coverage. Temper any 'expanded coverage' "
            "phrasing accordingly."),
    }


# ============================================================================
# STEP 3 (MAJOR #3) -- ONE-THESIS CONTRIBUTION TABLE (tags as COLUMNS)
# ============================================================================
def step3_contribution_table(iter4: dict, clutrr_src: dict, synth_small_bite: dict,
                             inverted_u: dict) -> dict:
    logger.info("STEP 3 (MAJOR #3) -- one-thesis contribution table (tags-in-columns)")
    columns = ["claim", "evidence_tag", "where_it_holds", "status", "key_numbers"]

    # pull the EXACT Prolog + oracle numbers from the CLUTRR source (not the iter-4 mirror)
    cm = clutrr_src["metadata"]
    prolog = cm["prolog_discharge"]
    swipl_engine = f"{prolog['n_prolog_matches_python']}/{prolog['n_executed_in_swipl']}"
    swipl_gold = f"{prolog['n_modeA_surface_matches_gold']}/{prolog['n_discharged']}"

    spine_1 = {
        "claim": ("Training-free, gold-free, per-edge ABSTAIN-ON-COLLAPSE certificate over "
                  "LLM-extracted relational facts: keep the LLM a high-recall disjunctive reader, "
                  "compose ONLY through exact relation-algebra tables, EMIT a singleton / ABSTAIN "
                  "on residual disjunction / FLAG unsound read on empty closure. Confirmed at power "
                  "end-to-end on templated CLUTRR."),
        "evidence_tag": "REAL-LLM-READ + THEOREM(zero-FP conditional on read soundness)",
        "where_it_holds": ("templated-CLUTRR (<=871 chars) end-to-end; weakly protective on "
                           "natural temporal text"),
        "status": "CONFIRMED-AT-POWER",
        "key_numbers": {
            "modeA_selacc": 0.8857, "vs_pot_gap": 0.428571,
            "vs_pot_ci95": [0.298589, 0.563015], "vs_sc_gap": 0.328571, "vs_raw_gap": 0.342857,
            "holm_p_adj": 0.001499, "h2_absent_reduction": 0.4444, "h2_ci95": [0.3167, 0.5833],
            "h2_p_one_sided": 0.0005, "goldread_oracle_selacc": 1.00, "oracle_coverage": 0.951,
            "oracle_raw_selacc": 0.433, "swipl_engine_match": swipl_engine,
            "swipl_gold_match": swipl_gold, "atomic_PRF1": [0.536, 0.532, 0.534]},
    }
    spine_2 = {
        "claim": ("A quantitative law for WHEN cross-path qualitative-algebra coding can be read "
                  "off text: richer algebra gives an exact table more headroom but lets an LLM read "
                  "constituent relations LESS informatively -- high-recall disjunctive reads are "
                  "sound but near-universe (no intersection bite); forcing tight reads is ~3% "
                  "correct (unsound). On temporal Allen, intersection/best-single/naive all resolve "
                  "0/125 gold-singleton multi-path queries; the synthetic Allen positive control "
                  "PASSES at recall 0.95, localizing the cause to read-informativeness, NOT closure."),
        "evidence_tag": "REAL-LLM-READ + GOLD-ONLY-GATE + SYNTHETIC-ALLEN-CONTROL",
        "where_it_holds": "natural temporal text (TDDMan gold-singleton multi-path N=125)",
        "status": "CONFIRMED-AS-CHARACTERIZATION",
        "key_numbers": {
            "gold_singleton_multipath_N": 125, "intersection_resolved": "0/125",
            "best_single_resolved": "0/125", "naive_resolved": "0/125", "holm": "n.s.",
            "per_edge_allen_recall": 0.90, "recall_gate": 0.85, "event_local_underdet_rate": 0.87,
            "window_underdet_rate": 0.79, "breadth": "11.5/13", "deepseek_underdet_rate": 0.99,
            "deepseek_breadth": "12.9/13", "tight_raw_allen_correct": 0.032,
            "intersection_commit_confident_wrong": 1.0,
            "synth_control_recall95_intersection_cov":
                synth_small_bite["per_method"]["intersection"]["coverage"],
            "synth_control_best_single_cov":
                synth_small_bite["per_method"]["best_single"]["coverage"],
            "synth_control_coverage_gain":
                synth_small_bite["coverage_gain_intersection_vs_best"]["point"],
            "synth_control_coverage_gain_ci95":
                synth_small_bite["coverage_gain_intersection_vs_best"]["ci95"],
            "synth_control_selacc_gain":
                synth_small_bite["selacc_gain_intersection_vs_best"]["point"],
            "synth_control_selacc_gain_ci95":
                synth_small_bite["selacc_gain_intersection_vs_best"]["ci95"]},
    }
    spine_pending = {
        "claim": ("DECISIVE iter-5 open experiment: cross-path INTERSECTION on the gated spatial "
                  "RCC-8 venue (SpaRTUN) -- does it narrow beyond best-single-path at power where "
                  "constituent relations (containment/connection) may read locally? FORK: narrows "
                  "-> first real-venue POSITIVE for the coding mechanism; also underdetermines -> "
                  "SECOND decisive negative, drop cross-path coding from the headline."),
        "evidence_tag": "SYNTHETIC-CHANNEL -> REAL(ISTIC)-LLM-READ (PENDING)",
        "where_it_holds": ("spatial RCC-8 SpaRTUN (gated 27.4% tight-bite, GENERAL band; tables "
                           "engine-validated)"),
        "status": "PENDING - NOT YET RUN (slot to be filled by iter-5 experiment)",
        "key_numbers": {"spartun_tight_bite_fraction": 0.274, "rcc8_table_validated": True,
                        "projection_cardinal_is_product_of_two_point_algebras": True},
    }
    supporting_1 = {
        "claim": ("The scaling-law engine behind SPINE-2 first half: with real LLM reads on "
                  "synthetic NL the advantage over PoT grows monotonically with base-relation count "
                  "-- point(3) +0.043 -> RCC-8(8) +0.448 -> Allen(13) +0.676. This is the INHERITED "
                  "exact-table-vs-LLM-composition effect at recall ~1.0 on templated NL (the "
                  "standard NeSy premise), NOT this work's novel coding mechanism. On Allen the "
                  "+0.676 DECOMPOSES into inherited +0.673 + novel-on-selective-accuracy +0.0025 "
                  "(~0)."),
        "evidence_tag": "REAL-LLM-READ-ON-SYNTHETIC",
        "where_it_holds": "synthetic/templated NL",
        "status": "SUPPORTING (inherited premise; RCC-8/Allen are SOUND LOWER BOUNDS, PC incomplete)",
        "key_numbers": {"point3": 0.043, "rcc8_8": 0.448, "allen13": 0.676,
                        "allen_inherited": 0.673, "allen_novel_selacc": 0.0025,
                        "provenance": "point(+0.043) and RCC-8(+0.448) carried as CITED literals "
                        "from hypothesis CLAIM 5a (art_QToTkRe6Umb8, algebra-richness scaling -- "
                        "NOT a dependency of this eval); NOT recomputed here. Allen +0.676 = "
                        "inherited 0.673 + novel 0.0025 reproduced in iter-4 eval "
                        "metadata.decomposition.allen_carried_forward."},
    }
    supporting_2 = {
        "claim": ("On a realism-matched channel iterated closure error-corrects per recall slice "
                  "(H3 Page p~5e-4, length-2 tie growing with hop/cyclomatic) and net Mode-A "
                  "resolution is a recall-dependent inverted-U (peak K*=2,4,7,10,16 for recall "
                  "0.5->0.95); silent-wrong rises 0.006->0.146 bounded by (1-r) and (1-J(E)). "
                  "CRITICAL CAVEAT: realized cross-path COVERAGE bite is SMALL -- intersection adds "
                  "only ~+2.4% coverage over best-single (synthetic Allen control); the mechanism's "
                  "practical value is PRECISION of committed answers, not expanded coverage."),
        "evidence_tag": "SYNTHETIC-CHANNEL + THEOREM(zero-FP on all-sound networks)",
        "where_it_holds": "synthetic-channel only",
        "status": ("SUPPORTING (recall & rho are CONTROLLED INPUTS; does NOT predict a real-text "
                   "operating point)"),
        "key_numbers": {"peak_K_by_recall": inverted_u["peak_K_by_recall"],
                        "silent_wrong_range": [inverted_u["silent_wrong_min"],
                                               inverted_u["silent_wrong_max"]],
                        "page_p_corrected": 5e-4,
                        "realized_coverage_bite_vs_best_single":
                            synth_small_bite["coverage_gain_intersection_vs_best"]["point"],
                        "max_realized_coverage_gain_vs_K1": inverted_u["max_coverage_gain_vs_K1"],
                        "zero_FP_theorem_networks": 100296},
    }
    footnote_a = {
        "claim": ("On NATURAL temporal text the matched-coverage Mode-A advantage is MARGINAL and "
                  "NOT robustly significant: corrected fixed-operating-point CIs bracket the point "
                  "gaps but INCLUDE ZERO; neither H1 gateway clears Holm; the earlier published "
                  "CONFIRM was a bootstrap artifact. Raw OUT-accuracies Mode-A by 0.124 at matched "
                  "coverage; among the ~19% Mode-A commits to it is confident-wrong 42.5% (48/113), "
                  "ALL silent-wrong-narrowing."),
        "evidence_tag": "REAL-LLM-READ",
        "where_it_holds": "natural temporal (NarrativeTime+TDDMan)",
        "status": "MARGINAL / CERTIFICATE-ONLY VALUE",
        "key_numbers": {"vs_pot_gap": 0.026549, "vs_pot_corrected_ci95": [-0.088276, 0.139723],
                        "vs_pot_boot_p": 0.3322, "vs_sc_gap": 0.035398,
                        "vs_sc_corrected_ci95": [-0.061388, 0.134703], "holm_p_adj": 0.5186,
                        "confident_wrong_among_answered": "48/113=0.425", "modeA_coverage": 0.1883,
                        "raw_out_accuracy_gap": -0.124},
    }
    footnote_b = {
        "claim": ("Contribution is the DEDUCTION SUB-MODULE only: atomic extraction MEASURED not "
                  "improved (~0.53 recall => ~19% Mode-A coverage on natural text); OpenCyc "
                  "grounding, atomic re-extraction, general LLM fuzzy-unification OUT OF SCOPE; "
                  "composition table HAND-SUPPLIED in every venue; NO document reaches ~3000 chars "
                  "(CLUTRR <=871; spatial 130-1338)."),
        "evidence_tag": "SCOPE",
        "where_it_holds": "all venues",
        "status": "CEILING (state in abstract/intro)",
        "key_numbers": {"atomic_recall": 0.5324, "modeA_real_text_coverage": 0.1883,
                        "clutrr_max_chars": 871, "spatial_char_range": [130, 1338]},
    }

    return {
        "columns": columns,
        "spine": [spine_1, spine_2],
        "pending_rcc8_slot": spine_pending,
        "supporting": [supporting_1, supporting_2],
        "footnotes": [footnote_a, footnote_b],
        "tagging_policy": ("Every row carries an evidence_tag COLUMN drawn from {THEOREM, "
                           "SYNTHETIC-CHANNEL, SYNTHETIC-ALLEN-CONTROL, GOLD-ONLY-GATE, "
                           "REAL-LLM-READ, REAL-LLM-READ-ON-SYNTHETIC, SCOPE, EXPLORATORY}; "
                           "provenance is legible at a glance, NOT buried in inline hedging."),
    }


# ============================================================================
# OUTPUT ASSEMBLY
# ============================================================================
def build_metrics_agg(synth, inverted_u, iter4, repro) -> dict:
    pm = synth["per_method"]
    cg = synth["coverage_gain_intersection_vs_best"]
    sg = synth["selacc_gain_intersection_vs_best"]
    ma = iter4["metrics_agg"]
    out = {
        # ---- STEP 1 synthetic Allen ----
        "synth_allen_coverage_gain": cg["point"],
        "synth_allen_coverage_gain_ci_lo": cg["ci95"][0],
        "synth_allen_coverage_gain_ci_hi": cg["ci95"][1],
        "synth_allen_coverage_gain_boot_p_le_0": cg["boot_p_le_0"],
        "synth_allen_selacc_gain": sg["point"],
        "synth_allen_selacc_gain_ci_lo": sg["ci95"][0],
        "synth_allen_selacc_gain_ci_hi": sg["ci95"][1],
        "synth_allen_selacc_gain_boot_p_le_0": sg["boot_p_le_0"],
        "synth_allen_selacc_gain_aligned": synth["selacc_gain_aligned_both_resolve"]["acc_gain"]
            if "selacc_gain_aligned_both_resolve" in synth else float("nan"),
        "synth_allen_intersection_coverage": pm["intersection"]["coverage"],
        "synth_allen_intersection_selacc": pm["intersection"]["selective_acc"],
        "synth_allen_best_single_coverage": pm["best_single"]["coverage"],
        "synth_allen_best_single_selacc": pm["best_single"]["selective_acc"],
        "synth_allen_naive_coverage": pm["naive"]["coverage"],
        "synth_allen_naive_selacc": pm["naive"]["selective_acc"],
        "synth_allen_mean_bite": synth["mean_bite"],
        "synth_allen_singleton_resolved_rate": synth["singleton_resolved_rate"],
        "synth_allen_reproduction_failed": 1.0 if synth["reproduction_failed"] else 0.0,
        "synth_allen_analytic_ci_fallback": 1.0 if synth["analytic_ci_fallback"] else 0.0,
        # ---- STEP 2 inverted-U realized coverage ----
        "invertedu_max_coverage_gain_vs_k1": inverted_u["max_coverage_gain_vs_K1"],
        "invertedu_silent_wrong_max": inverted_u["silent_wrong_max"],
        "invertedu_silent_wrong_min": inverted_u["silent_wrong_min"],
        # ---- carried headline numbers (spine / footnotes) ----
        "clutrr_modeA_selacc": ma["clutrr_modeA_selacc"],
        "clutrr_modeA_vs_pot_gap": ma["clutrr_modeA_vs_pot_gap"],
        "clutrr_h2_reduction": ma["clutrr_h2_confident_wrong_reduction"],
        "clutrr_oracle_modeA_selacc": ma["clutrr_oracle_modeA_selacc"],
        "clutrr_atomic_recall": ma["clutrr_atomic_recall"],
        "temporal_vs_pot_corrected_boot_p": ma["temporal_modeA_vs_pot_new_boot_p"],
        "temporal_vs_pot_corrected_ci_lo": ma["temporal_modeA_vs_pot_new_ci_lo"],
        "temporal_vs_pot_corrected_ci_hi": ma["temporal_modeA_vs_pot_new_ci_hi"],
        "temporal_confident_wrong_frac": ma["temporal_confident_wrong_frac"],
        "temporal_modeA_coverage": ma["temporal_modeA_coverage"],
        "allen_inherited_carried": ma["allen_inherited_carried"],
        "allen_novel_selacc_carried": ma["allen_novel_selacc_carried"],
        # ---- meta ----
        "llm_spend_usd": 0.0,
        "n_reproduction_mismatches": float(repro["n_mismatches"]),
        "B_bootstrap": float(B_BOOT),
        "seed": float(SEED),
    }
    return out


def main():
    logger.info("=== iter-5 zero-spend re-analysis START (numpy+scipy only, $0) ===")
    # assert no OpenRouter client anywhere
    assert "openrouter" not in " ".join(sys.argv).lower()

    iter4 = load_json(SRC["iter4_eval"]["path"])
    clutrr_src = load_json(SRC["clutrr_certificate"]["path"])
    channel = load_json(SRC["inverted_u_channel"]["path"])
    synth_full = load_json(SRC["synth_allen_control"]["path"])
    published_cell = synth_full["metadata"]["synthetic_allen_control"]["cells"]["recall_95"]

    # STEP 0
    repro = step0_sanity(iter4)

    # STEP 1
    synth, worked = step1_synth_allen(published_cell)

    # STEP 2
    inverted_u = step2_inverted_u(channel)

    # STEP 3
    table = step3_contribution_table(iter4, clutrr_src, synth, inverted_u)

    # STEP 4 -- carry corrected temporal + ceiling (REUSE, no recompute)
    corrected_temporal = {
        "tag": "REAL-LLM-READ",
        "carried_from": SRC["iter4_eval"]["id"],
        "r1_bracketing_summary": {
            "neither_gateway_clears_holm": True,
            "vs_pot": {"gap": 0.026549, "corrected_ci95": [-0.088276, 0.139723],
                       "boot_p": 0.3322, "ci_brackets_point": True, "significant": False},
            "vs_sc": {"gap": 0.035398, "corrected_ci95": [-0.061388, 0.134703],
                      "boot_p": 0.2593, "significant": False},
            "published_confirm_was_bootstrap_artifact": True},
        "confident_wrong_block": iter4["metadata"]["temporal_confident_wrong_block"],
        "modeA_coverage": 0.188333, "modeA_abstention_rate": 0.811667,
        "raw_out_accuracy_gap_at_matched_cov": -0.123894,
    }
    deduction_submodule_ceiling = {
        "tag": "SCOPE",
        "carried_from": SRC["iter4_eval"]["id"],
        "atomic_recall": 0.5324, "modeA_real_text_coverage": 0.188333,
        "out_of_scope": ["OpenCyc grounding", "atomic re-extraction",
                         "general LLM fuzzy-unification"],
        "composition_table": "HAND-SUPPLIED in every venue",
        "max_chars": {"clutrr": 871, "spatial": [130, 1338], "target": 3000,
                      "note": "NO venue reaches the umbrella ~3000-char target"},
        "extraction_limited_statement": ("Real-text utility is EXTRACTION-LIMITED: ~0.53 atomic "
                                         "recall -> ~19% Mode-A coverage on natural temporal text."),
    }

    headline_structure_guidance = {
        "i_lead_with_two_row_spine": ("LEAD abstract/intro/title with the two-row SPINE "
            "(the certificate + the read-informativeness impossibility); DEMOTE the 5-claim "
            "'honest split' to ONE mechanism-analysis section."),
        "ii_tags_in_columns": ("Put evidence tags in TABLE COLUMNS (claim | evidence_tag | "
            "where_it_holds | status | key_numbers), NOT inline prose hedging."),
        "iii_rcc8_is_the_single_open_experiment": ("The spatial RCC-8 SpaRTUN fork is the SINGLE "
            "decisive open experiment -- reserve the SPINE-PENDING row as a slot."),
        "iv_retitle": ("Re-title around 'closure-certified DEDUCTION SUB-MODULE' (NOT an "
            "end-to-end text-to-FOL system)."),
        "v_hallucination_with_coverage": ("Report every hallucination number WITH its "
            "coverage/abstention (e.g. H2 reduction 0.444 @ Mode-A coverage 26.6%; temporal "
            "confident-wrong 42.5% @ coverage 18.8%)."),
        "vi_clutrr_not_natural_text": ("Do NOT call CLUTRR natural text -- it is a TEMPLATED "
            "kinship benchmark (<=871 chars, gold surface forms, hand-supplied table)."),
    }

    metrics_agg = build_metrics_agg(synth, inverted_u, iter4, repro)

    metadata = {
        "eval_name": "iter5_zero_spend_reanalysis_small_bite_and_one_thesis_table",
        "description": ("Zero-spend ($0, numpy+scipy only, deterministic seed=20260617, B=10000 "
                        "paired bootstrap) iter-5 re-analysis extending the validated iter-4 "
                        "re-analysis. (1) MINOR #5: synthetic-Allen small cross-path COVERAGE bite "
                        "(+0.024) vs large SELECTIVE-ACCURACY gain (+0.259) with bootstrap CIs, and "
                        "inverted-U realized-coverage decomposition -> 'precision of committed "
                        "answers, not expanded coverage'. (2) MAJOR #3: ONE-THESIS contribution "
                        "table with evidence tags as COLUMNS, two-row spine + supporting + footnote "
                        "rows + pending spatial-RCC-8 slot."),
        "evidence_tags": ["THEOREM", "SYNTHETIC-CHANNEL", "SYNTHETIC-ALLEN-CONTROL",
                          "GOLD-ONLY-GATE", "REAL-LLM-READ", "REAL-LLM-READ-ON-SYNTHETIC",
                          "SCOPE", "EXPLORATORY"],
        "seed": SEED, "B_bootstrap": B_BOOT, "alpha": ALPHA, "llm_spend_usd": 0.0,
        "no_openrouter_client_instantiated": True,
        "sources": SRC,
        "reproduction_checks": repro,
        "synthetic_allen_small_bite": synth,
        "inverted_u_realized_coverage": inverted_u,
        "one_thesis_contribution_table": table,
        "headline_structure_guidance": headline_structure_guidance,
        "corrected_temporal": corrected_temporal,
        "deduction_submodule_ceiling": deduction_submodule_ceiling,
    }

    # ---- datasets[]: synthetic-Allen worked examples + carried iter-4 clutrr/temporal ----
    datasets = [{"dataset": "synthetic_allen_control_worked", "examples": worked}]
    for d in iter4["datasets"]:
        datasets.append(d)
    logger.info(f"datasets: {[ (d['dataset'], len(d['examples'])) for d in datasets ]}")

    out = {"metrics_agg": metrics_agg, "metadata": metadata, "datasets": datasets}
    out_path = WS / "eval_out.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    logger.info(f"WROTE {out_path} ({out_path.stat().st_size/1024:.1f} KB)")

    # quick stdout summary
    logger.info("---- SUMMARY ----")
    logger.info(f"  synth coverage_gain={metrics_agg['synth_allen_coverage_gain']:.4f} "
                f"CI[{metrics_agg['synth_allen_coverage_gain_ci_lo']:.4f},"
                f"{metrics_agg['synth_allen_coverage_gain_ci_hi']:.4f}]")
    logger.info(f"  synth selacc_gain={metrics_agg['synth_allen_selacc_gain']:.4f} "
                f"CI[{metrics_agg['synth_allen_selacc_gain_ci_lo']:.4f},"
                f"{metrics_agg['synth_allen_selacc_gain_ci_hi']:.4f}]")
    logger.info(f"  invertedu max_cov_gain_vs_k1={metrics_agg['invertedu_max_coverage_gain_vs_k1']:.4f} "
                f"silent_wrong[{metrics_agg['invertedu_silent_wrong_min']:.4f},"
                f"{metrics_agg['invertedu_silent_wrong_max']:.4f}]")
    logger.info(f"  reproduction mismatches={repro['n_mismatches']}")
    logger.info("=== DONE ===")
    return out


if __name__ == "__main__":
    main()
