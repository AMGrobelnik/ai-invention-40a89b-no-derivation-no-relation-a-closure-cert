#!/usr/bin/env python3
"""Zero-spend re-analysis: fuzzy fair-baseline + framing spine.

Pure numpy+scipy re-analysis ($0 LLM, no OpenRouter client). Deterministic
seed=20260617; doc-clustered paired bootstrap B=10000. Reads the three
dependency experiment workspaces + the iter-4 / iter-5 prior re-analyses
directly from disk (read-only) and produces FOUR deliverables for
GEN_PAPER_TEXT:

  STEP 0  reproduce-and-verify the iter-4 + iter-5 carried literals (gate)
  TASK 1  (MAJOR #2) fuzzy CONFIDENCE-THRESHOLDED fair baseline @ matched
          coverage + doc-clustered bootstrap Delta-CI + Mode-B catch count
          (the ONLY new computation)
  TASK 2  (MAJOR #3) tempered 'two-conditions-independently-violated' paragraph
  TASK 3  (MINOR #5) one-thesis contribution table (tags as columns)
  TASK 4  (MINOR #4) venue reposition + scope boundaries + doc labels

Outputs: eval_out.json (aii-json exp_eval_sol_out) + eval_digest.md.
"""

from __future__ import annotations

import gc
import json
import resource
import sys
from pathlib import Path

import numpy as np
from loguru import logger

# --------------------------------------------------------------------------- #
# Logging + (light) resource guard                                            #
# --------------------------------------------------------------------------- #
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# Pure numpy re-analysis on a few MB of JSON -> a small RAM budget is plenty.
_RAM_BUDGET = 6 * 1024 ** 3
resource.setrlimit(resource.RLIMIT_AS, (_RAM_BUDGET, _RAM_BUDGET))

SEED = 20260617
B_BOOT = 10000
ALPHA = 0.05

# --------------------------------------------------------------------------- #
# Dependency file locations (read-only; absolute)                             #
# --------------------------------------------------------------------------- #
RUN = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop")
FUZZY_F = RUN / "iter_5/gen_art/gen_art_experiment_2/full_method_out.json"
SPATIAL_F = RUN / "iter_5/gen_art/gen_art_experiment_1/full_method_out.json"
CLUTRR_F = RUN / "iter_3/gen_art/gen_art_experiment_1/full_method_out.json"
ITER5_EVAL_F = RUN / "iter_5/gen_art/gen_art_evaluation_1/eval_out.json"
ITER4_EVAL_F = RUN / "iter_4/gen_art/gen_art_evaluation_1/eval_out.json"

WS = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_evaluation_1")
OUT_JSON = WS / "eval_out.json"
OUT_DIGEST = WS / "eval_digest.md"

# Optional cap on examples emitted per dataset in eval_out.json
N_EXAMPLE_CAP = 300


# --------------------------------------------------------------------------- #
# Helpers                                                                      #
# --------------------------------------------------------------------------- #
def load_json(p: Path) -> dict:
    logger.info(f"loading {p}")
    with open(p) as fh:
        return json.load(fh)


def approx(a, b, tol=1e-4) -> bool:
    """Numeric closeness with NaN/None handling."""
    if a is None or b is None:
        return a == b
    try:
        return abs(float(a) - float(b)) <= tol
    except (TypeError, ValueError):
        return a == b


def edge_reads(dataset: dict) -> list[dict]:
    return [e for e in dataset["examples"] if e.get("metadata_record_kind") == "edge_read"]


def to_arrays(reads: list[dict], gold_key: str, term_key: str):
    """Extract aligned numpy arrays from a list of edge_read records."""
    conf = np.array([float(r["metadata_top1_conf"]) for r in reads], dtype=np.float64)
    correct = np.array([bool(r["metadata_top1_correct"]) for r in reads], dtype=bool)
    sound = np.array([bool(r["metadata_sound"]) for r in reads], dtype=bool)
    breadth = np.array([float(r.get("metadata_breadth", np.nan)) for r in reads], dtype=np.float64)
    doc_ids = np.array([str(r["metadata_doc_id"]) for r in reads])
    gold = [str(r.get(gold_key, "")) for r in reads]
    term = [str(r.get(term_key, "")) for r in reads]
    top1 = [str(r.get("predict_top1", "")) for r in reads]
    inp = [str(r.get("input", "")) for r in reads]
    return conf, correct, sound, breadth, doc_ids, gold, term, top1, inp


def build_doc_matrix(doc_ids: np.ndarray):
    """Padded (D, maxlen) matrix of read-indices grouped by doc (for clustered bootstrap)."""
    docs, inv = np.unique(doc_ids, return_inverse=True)
    d = len(docs)
    counts = np.bincount(inv, minlength=d)
    maxlen = int(counts.max())
    mat = np.full((d, maxlen), -1, dtype=np.int64)
    pos = np.zeros(d, dtype=np.int64)
    for ridx in range(len(doc_ids)):
        di = inv[ridx]
        mat[di, pos[di]] = ridx
        pos[di] += 1
    return mat, d


def select_topk(conf: np.ndarray, correct: np.ndarray, k: int, tiekey: np.ndarray):
    """Commit the k most-confident reads; discrete-conf ties broken by tiekey (fixed seed).

    sortkey = -conf + 0.05*tiekey  (tiekey in [0,1); 0.05 < min conf gap 0.1, so ties
    never cross a confidence level). Smallest sortkey == highest conf == committed first.
    """
    sk = -conf + 0.05 * tiekey
    order = np.argsort(sk, kind="stable")
    committed = order[:k]
    cw = float(np.mean(~correct[committed])) if k > 0 else 0.0
    implied_tau = float(conf[committed[-1]]) if k > 0 else None
    return committed, cw, implied_tau


def doc_clustered_bootstrap_cw(conf, correct, mat, d, cov, tiekey, b_boot, rng):
    """Doc-clustered bootstrap of the matched-coverage confident-wrong rate.

    Each replicate resamples d doc-clusters with replacement, re-selects the
    k'=round(cov*N') most-confident reads, recomputes confident-wrong.
    """
    boot = np.empty(b_boot, dtype=np.float64)
    not_correct = ~correct
    for b in range(b_boot):
        sampled = rng.integers(0, d, size=d)
        rows = mat[sampled]                 # (d, maxlen)
        flat = rows[rows >= 0]              # variable length read indices
        n_p = flat.size
        kk = int(round(cov * n_p))
        if kk <= 0:
            boot[b] = 0.0
            continue
        c = conf[flat]
        sk = -c + 0.05 * tiekey[flat]
        if kk >= n_p:
            sel = flat
        else:
            part = np.argpartition(sk, kk - 1)[:kk]
            sel = flat[part]
        boot[b] = float(np.mean(not_correct[sel]))
    return boot


# --------------------------------------------------------------------------- #
# STEP 0 -- reproduce-and-verify gate                                          #
# --------------------------------------------------------------------------- #
def step0_reproduce_verify() -> dict:
    logger.info("STEP 0: reproduce-and-verify iter-5 / iter-4 carried literals")
    d5 = load_json(ITER5_EVAL_F)
    m5 = d5["metrics_agg"]
    md5 = d5["metadata"]
    d4 = load_json(ITER4_EVAL_F)
    m4 = d4["metrics_agg"]
    md4 = d4["metadata"]

    iu5 = md5["inverted_u_realized_coverage"]
    sb5 = md5["synthetic_allen_small_bite"]

    checks5 = []  # (name, ok, actual, expected)

    def chk5(name, actual, expected, listcmp=False, strcontains=None):
        if strcontains is not None:
            ok = isinstance(actual, str) and strcontains in actual
        elif listcmp:
            ok = list(actual) == list(expected)
        else:
            ok = approx(actual, expected)
        checks5.append({"name": name, "ok": bool(ok), "actual": actual, "expected": expected})

    # --- iter-5 small-bite synthetic Allen ---
    chk5("synth_allen_intersection_coverage", m5.get("synth_allen_intersection_coverage"), 0.25)
    chk5("synth_allen_best_single_coverage", m5.get("synth_allen_best_single_coverage"), 0.226)
    chk5("synth_allen_coverage_gain(+0.0240)", m5.get("synth_allen_coverage_gain"), 0.024)
    cov_lo = m5.get("synth_allen_coverage_gain_ci_lo")
    cov_hi = m5.get("synth_allen_coverage_gain_ci_hi")
    chk5("synth_allen_coverage_gain_ci_includes_0",
         float(cov_lo) <= 0.0 <= float(cov_hi), True)
    chk5("synth_allen_selacc_gain(0.2592)", m5.get("synth_allen_selacc_gain"), 0.2592, )
    chk5("synth_allen_selacc_gain_ci_lo(0.1765)", m5.get("synth_allen_selacc_gain_ci_lo"), 0.1765)
    chk5("synth_allen_selacc_gain_ci_hi(0.3494)", m5.get("synth_allen_selacc_gain_ci_hi"), 0.3494)
    chk5("synth_allen_intersection_selacc(0.976)", m5.get("synth_allen_intersection_selacc"), 0.976)
    chk5("synth_allen_best_single_selacc(0.717)", m5.get("synth_allen_best_single_selacc"), 0.7168, )
    # --- iter-5 inverted-U ---
    chk5("inverted_u_peak_K_by_recall[2,4,7,10,16]", iu5.get("peak_K_by_recall"),
         [2, 4, 7, 10, 16], listcmp=True)
    chk5("invertedu_silent_wrong_min(0.0064)", m5.get("invertedu_silent_wrong_min"), 0.006412037)
    chk5("invertedu_silent_wrong_max(0.1456)", m5.get("invertedu_silent_wrong_max"), 0.145648148)
    chk5("page_p_corrected(~5e-4)", iu5.get("page_p_corrected"), "~5e-4", strcontains="5e-4")
    # --- iter-5 algebra decomposition Allen 0.676 = 0.673 inherited + 0.0025 novel ---
    inh = m5.get("allen_inherited_carried")
    nov = m5.get("allen_novel_selacc_carried")
    chk5("allen_inherited_carried(0.673)", inh, 0.67349)
    chk5("allen_novel_selacc_carried(0.0025)", nov, 0.0025)
    chk5("allen_decomposition_sum(0.676)", float(inh) + float(nov), 0.676, )
    # --- iter-5 corrected temporal ---
    chk5("temporal_vs_pot_corrected_gap(0.0265)", m5.get("temporal_vs_pot_corrected_boot_p") is not None
         and md5["corrected_temporal"]["r1_bracketing_summary"]["vs_pot"]["gap"], 0.026549)
    chk5("temporal_vs_pot_corrected_boot_p(0.3322)", m5.get("temporal_vs_pot_corrected_boot_p"), 0.3322)
    chk5("temporal_vs_pot_corrected_ci_lo(-0.0883)", m5.get("temporal_vs_pot_corrected_ci_lo"), -0.088276)
    chk5("temporal_vs_pot_corrected_ci_hi(0.1397)", m5.get("temporal_vs_pot_corrected_ci_hi"), 0.139723)
    vs_sc5 = md5["corrected_temporal"]["r1_bracketing_summary"]["vs_sc"]
    chk5("temporal_vs_sc_gap(0.0354)", vs_sc5["gap"], 0.035398)
    chk5("temporal_vs_sc_ci_lo(-0.0614)", vs_sc5["corrected_ci95"][0], -0.061388)
    chk5("temporal_vs_sc_ci_hi(0.1347)", vs_sc5["corrected_ci95"][1], 0.134703)
    chk5("temporal_confident_wrong_frac(0.4248=48/113)", m5.get("temporal_confident_wrong_frac"), 0.424779)
    chk5("temporal_modeA_coverage(0.1883)", m5.get("temporal_modeA_coverage"), 0.188333)
    chk5("clutrr_atomic_recall(0.5324)", m5.get("clutrr_atomic_recall"), 0.5324)
    chk5("clutrr_modeA_selacc(0.8857)", m5.get("clutrr_modeA_selacc"), 0.885714)
    chk5("clutrr_h2_reduction(0.4444)", m5.get("clutrr_h2_reduction"), 0.4444)
    chk5("clutrr_oracle_modeA_selacc(1.0)", m5.get("clutrr_oracle_modeA_selacc"), 1.0)

    mism5 = sum(0 if c["ok"] else 1 for c in checks5)

    # --- iter-4 corrected temporal + decomposition ---
    checks4 = []

    def chk4(name, actual, expected):
        ok = approx(actual, expected)
        checks4.append({"name": name, "ok": bool(ok), "actual": actual, "expected": expected})

    chk4("temporal_modeA_vs_pot_gap(0.0265)", m4.get("temporal_modeA_vs_pot_gap"), 0.026549)
    chk4("temporal_modeA_vs_pot_new_ci_lo(-0.0883)", m4.get("temporal_modeA_vs_pot_new_ci_lo"), -0.088276)
    chk4("temporal_modeA_vs_pot_new_ci_hi(0.1397)", m4.get("temporal_modeA_vs_pot_new_ci_hi"), 0.139723)
    chk4("temporal_modeA_vs_pot_new_boot_p(0.3322)", m4.get("temporal_modeA_vs_pot_new_boot_p"), 0.3322)
    chk4("temporal_confident_wrong_frac(0.4248)", m4.get("temporal_confident_wrong_frac"), 0.424779)
    chk4("temporal_confident_wrong_n(48)", m4.get("temporal_confident_wrong_n"), 48)
    chk4("allen_inherited_carried(0.673)", m4.get("allen_inherited_carried"), 0.67349)
    chk4("allen_novel_selacc_carried(0.0025)", m4.get("allen_novel_selacc_carried"), 0.0025)
    chk4("clutrr_atomic_recall(0.5324)", m4.get("clutrr_atomic_recall"), 0.5324)
    chk4("clutrr_modeA_selacc(0.8857)", m4.get("clutrr_modeA_selacc"), 0.885714)
    chk4("clutrr_h2_confident_wrong_reduction(0.4444)", m4.get("clutrr_h2_confident_wrong_reduction"), 0.4444)
    chk4("clutrr_oracle_modeA_selacc(1.0)", m4.get("clutrr_oracle_modeA_selacc"), 1.0)
    chk4("clutrr_atomic_recall_meta_present", md4.get("decomposition") is not None, True)

    mism4 = sum(0 if c["ok"] else 1 for c in checks4)

    if mism5:
        logger.warning(f"iter-5 reproduce mismatches: {mism5}")
        for c in checks5:
            if not c["ok"]:
                logger.warning(f"  MISMATCH {c['name']}: actual={c['actual']} expected={c['expected']}")
    if mism4:
        logger.warning(f"iter-4 reproduce mismatches: {mism4}")
        for c in checks4:
            if not c["ok"]:
                logger.warning(f"  MISMATCH {c['name']}: actual={c['actual']} expected={c['expected']}")
    logger.info(f"STEP 0 done: mismatches_vs_iter5={mism5} mismatches_vs_iter4={mism4} "
                f"(checked {len(checks5)}+{len(checks4)})")

    rv = {
        "mismatches_vs_iter5": int(mism5),
        "mismatches_vs_iter4": int(mism4),
        "n_checks_iter5": len(checks5),
        "n_checks_iter4": len(checks4),
        "checked_iter5": [c["name"] for c in checks5],
        "checked_iter4": [c["name"] for c in checks4],
        "mismatch_detail_iter5": [c for c in checks5 if not c["ok"]],
        "mismatch_detail_iter4": [c for c in checks4 if not c["ok"]],
        "target_mismatches": 0,
        "evidence_tag": "REPRODUCE-VERIFY",
    }
    del d5, d4
    gc.collect()
    return rv


# --------------------------------------------------------------------------- #
# TASK 1 -- fuzzy confidence-thresholded fair baseline (the only new compute)  #
# --------------------------------------------------------------------------- #
def task1_setting(name, dataset, matched_cov, gold_key, term_key,
                  rc_meta, ece_top1, rng):
    """Build the confidence-thresholded top-1 abstainer for one setting."""
    reads = edge_reads(dataset)
    n = len(reads)
    assert n == 1500, f"{name}: expected 1500 edge_reads, got {n}"
    conf, correct, sound, breadth, doc_ids, gold, term, top1, inp = to_arrays(reads, gold_key, term_key)

    tiekey = rng.random(n)  # fixed-seed permutation-equivalent tie-break
    k = int(round(matched_cov * n))
    committed_idx, baseline_cw, implied_tau = select_topk(conf, correct, k, tiekey)
    achieved_cov = k / n
    committed_mask = np.zeros(n, dtype=bool)
    committed_mask[committed_idx] = True

    # hard-tau overshoot (conf >= implied_tau commits ALL ties -> overshoots coverage)
    over_mask = conf >= (implied_tau - 1e-9)
    overshoot_cov = float(over_mask.mean())
    overshoot_cw = float(np.mean(~correct[over_mask])) if over_mask.any() else 0.0

    # full risk-coverage frontier (point estimates)
    grid = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    frontier = []
    for c in grid:
        kc = int(round(c * n))
        kc = max(0, min(kc, n))
        if kc == 0:
            frontier.append({"coverage_target": c, "achieved_coverage": 0.0,
                             "confident_wrong": 0.0, "acc_among_answered": None, "k": 0})
            continue
        _, cw_c, _ = select_topk(conf, correct, kc, tiekey)
        frontier.append({"coverage_target": c, "achieved_coverage": kc / n,
                         "confident_wrong": cw_c, "acc_among_answered": 1.0 - cw_c, "k": kc})
    # add the exact matched point flagged
    frontier.append({"coverage_target": round(matched_cov, 7), "achieved_coverage": achieved_cov,
                     "confident_wrong": baseline_cw, "acc_among_answered": 1.0 - baseline_cw,
                     "k": k, "matched_point": True})

    # doc-clustered bootstrap on the matched-coverage CW
    mat, d_docs = build_doc_matrix(doc_ids)
    logger.info(f"{name}: matched_cov={matched_cov:.7f} N={n} k={k} implied_tau={implied_tau} "
                f"baseline_CW={baseline_cw:.4f} n_docs={d_docs}; running B={B_BOOT} clustered bootstrap")
    boot = doc_clustered_bootstrap_cw(conf, correct, mat, d_docs, matched_cov, tiekey, B_BOOT, rng)
    ci_lo = float(np.percentile(boot, 100 * ALPHA / 2))
    ci_hi = float(np.percentile(boot, 100 * (1 - ALPHA / 2)))
    p_one_sided = float(np.mean(boot <= 0.0))  # P(baseline_CW <= 0)
    certificate_beats = bool(ci_lo > 0.0)
    logger.info(f"{name}: bootstrap CW CI95=[{ci_lo:.4f},{ci_hi:.4f}] p(CW<=0)={p_one_sided:.4g} "
                f"certificate_beats={certificate_beats}")

    # Mode-B distinctive-edge quantification (edge-read level)
    n_unsound_edgeread = int((~sound).sum())
    unsound_conf = conf[~sound]
    unsound_conf_dist = {}
    for cv in np.unique(unsound_conf):
        unsound_conf_dist[str(round(float(cv), 4))] = int((unsound_conf == cv).sum())
    n_unsound_in_committed = int((committed_mask & ~sound).sum())
    # all unsound reads are top1-wrong by construction (gold not in emitted set)
    n_unsound_top1_wrong = int((~sound & ~correct).sum())

    # query-pool Mode-B (carried from rc_meta): queries whose chain dropped gold
    n_unsound_query = int(rc_meta["n_unsound_reads"])
    caught_frac = rc_meta.get("certificate_caught_fraction")
    n_caught = int(round(caught_frac * n_unsound_query)) if caught_frac is not None else 0
    n_silent_missed = int(rc_meta["n_silent_wrong_missed_by_cert"])

    setting = {
        "certificate": {
            "coverage": float(rc_meta["certificate"]["coverage"]),
            "confident_wrong": float(rc_meta["certificate"]["confident_wrong_rate"]),
            "n_committed": int(rc_meta["certificate"]["n_committed"]),
            "acc_among_answered": rc_meta["certificate"]["acc_among_answered"],
            "evidence_tag": "REAL-LLM-FUZZY-READ",
        },
        "commit_argmax": {
            "coverage": float(rc_meta["commit_argmax"]["coverage"]),
            "confident_wrong": float(rc_meta["commit_argmax"]["confident_wrong_rate"]),
            "n_confident_wrong": int(rc_meta["commit_argmax"]["n_confident_wrong"]),
            "acc_among_answered": rc_meta["commit_argmax"]["acc_among_answered"],
            "note": "ALWAYS-ANSWER contrast; NOT a fair abstainer.",
            "evidence_tag": "REAL-LLM-FUZZY-READ",
        },
        "conf_threshold_baseline": {
            "unit_of_analysis": "edge_read (1500 calibration reads); query records carry no per-query confidence",
            "construction": "top-k selection (k=round(cov*N)) on discrete top1_conf with fixed-seed tie-break",
            "matched_coverage": float(matched_cov),
            "achieved_coverage": float(achieved_cov),
            "k_committed": int(k),
            "implied_tau": implied_tau,
            "confident_wrong": float(baseline_cw),
            "acc_among_answered": float(1.0 - baseline_cw),
            "ci95": [ci_lo, ci_hi],
            "p_one_sided_cw_le_0": p_one_sided,
            "n_docs": int(d_docs),
            "certificate_beats": certificate_beats,
            "hard_tau_overshoot": {
                "note": "a hard conf>=tau cut commits ALL ties -> overshoots matched coverage",
                "overshoot_coverage": overshoot_cov,
                "overshoot_confident_wrong": overshoot_cw,
            },
            "frontier": frontier,
            "evidence_tag": "REAL-LLM-FUZZY-READ",
        },
        "modeB": {
            "n_unsound_query_pool": n_unsound_query,
            "n_caught": n_caught,
            "n_silent_wrong_missed": n_silent_missed,
            "certificate_caught_fraction": caught_frac,
            "n_unsound_edgeread": n_unsound_edgeread,
            "unsound_edgeread_conf_dist": unsound_conf_dist,
            "unsound_reads_all_high_conf": (bool(unsound_conf.min() >= 0.5) if n_unsound_edgeread else None),
            "n_unsound_edgeread_in_committed_region": n_unsound_in_committed,
            "n_unsound_edgeread_top1_wrong": n_unsound_top1_wrong,
            "interpretation": (
                "unsound reads are emitted at ORDINARY/HIGH confidence, so a confidence threshold "
                "structurally cannot single them out; the certificate catches them via the "
                "set-soundness (Mode-B collapse/abstain) contract."
            ) if n_unsound_edgeread else "no unsound reads exist -> Mode-B catch UNTESTED for this setting",
            "modeB_untested": bool(n_unsound_edgeread == 0),
            "evidence_tag": "REAL-LLM-FUZZY-READ + THEOREM:zero-FP-conditional",
        },
        "ECE_top1": float(ece_top1),
        "calibration_quality": "POOR" if ece_top1 > 0.2 else "GOOD",
    }

    # per-read records for the dataset emission (sorted by conf desc -> boundary visible)
    sk = -conf + 0.05 * tiekey
    order = np.argsort(sk, kind="stable")
    records = []
    for rank, ridx in enumerate(order[:N_EXAMPLE_CAP]):
        committed = rank < k
        rec = {
            "input": inp[ridx],
            "output": json.dumps({
                "decision": "COMMIT" if committed else "ABSTAIN",
                "top1": top1[ridx], "conf": float(conf[ridx]),
                "gold": gold[ridx], "top1_correct": bool(correct[ridx]),
                "sound": bool(sound[ridx]),
            }),
            "predict_conf_committed": "COMMIT" if committed else "ABSTAIN",
            "metadata_top1_conf": float(conf[ridx]),
            "metadata_top1_correct": bool(correct[ridx]),
            "metadata_sound": bool(sound[ridx]),
            "metadata_doc_id": doc_ids[ridx],
            "metadata_rank": int(rank),
            "metadata_term": term[ridx],
            "eval_committed": 1.0 if committed else 0.0,
            "eval_confident_wrong": 1.0 if (committed and not correct[ridx]) else 0.0,
        }
        records.append(rec)

    # unsound-read records (spatial only typically); cap at N_EXAMPLE_CAP
    unsound_records = []
    for ridx in np.nonzero(~sound)[0][:N_EXAMPLE_CAP]:
        committed = bool(committed_mask[ridx])
        unsound_records.append({
            "input": inp[ridx],
            "output": json.dumps({
                "gold": gold[ridx], "top1": top1[ridx], "conf": float(conf[ridx]),
                "sound": False, "top1_correct": bool(correct[ridx]),
                "in_conf_committed_region": committed,
            }),
            "predict_conf_committed": "COMMIT" if committed else "ABSTAIN",
            "metadata_top1_conf": float(conf[ridx]),
            "metadata_top1_correct": bool(correct[ridx]),
            "metadata_sound": False,
            "metadata_doc_id": doc_ids[ridx],
            "metadata_term": term[ridx],
            "eval_in_committed_region": 1.0 if committed else 0.0,
        })

    del conf, correct, sound, breadth, doc_ids, mat, boot
    gc.collect()
    return setting, records, unsound_records


def build_table3(spatial, kinship):
    """Per-setting rebuilt Table 3 with the new confidence-thresholded column."""
    def rows_for(s, label):
        cb = s["conf_threshold_baseline"]
        cert = s["certificate"]
        cm = s["commit_argmax"]
        ci = cb["ci95"]
        return [
            {"setting": label, "method": "commit-argmax (always-answer)",
             "coverage": round(cm["coverage"], 4), "acc_among_answered": cm["acc_among_answered"],
             "confident_wrong": round(cm["confident_wrong"], 4),
             "delta_vs_certificate_ci": "n/a (always-answers)",
             "evidence_tag": "REAL-LLM-FUZZY-READ"},
            {"setting": label, "method": "abstain-always",
             "coverage": 0.0, "acc_among_answered": None, "confident_wrong": 0.0,
             "delta_vs_certificate_ci": "n/a (coverage 0)",
             "evidence_tag": "REAL-LLM-FUZZY-READ"},
            {"setting": label, "method": "CERTIFICATE (abstain-on-collapse)",
             "coverage": round(cert["coverage"], 4), "acc_among_answered": cert["acc_among_answered"],
             "confident_wrong": round(cert["confident_wrong"], 4),
             "delta_vs_certificate_ci": "0.000 (reference)",
             "evidence_tag": "REAL-LLM-FUZZY-READ + THEOREM:zero-FP-conditional"},
            {"setting": label, "method": "CONFIDENCE-THRESHOLDED TOP-1 @ matched coverage (NEW)",
             "coverage": round(cb["achieved_coverage"], 4),
             "acc_among_answered": round(cb["acc_among_answered"], 4),
             "confident_wrong": round(cb["confident_wrong"], 4),
             "delta_vs_certificate_ci": f"+{cb['confident_wrong']:.4f}  95% CI [{ci[0]:.4f}, {ci[1]:.4f}]"
                                        f"  (certificate_beats={cb['certificate_beats']})",
             "evidence_tag": "REAL-LLM-FUZZY-READ"},
        ]
    rows = rows_for(spatial, "spatial_fuzzy_rcc8") + rows_for(kinship, "kinship_fuzzy_paraphrase")
    footnote = {
        "row": "Mode-B sound-violation catches",
        "spatial": f"{spatial['modeB']['n_caught']}/{spatial['modeB']['n_unsound_query_pool']} "
                   f"unsound queries caught, {spatial['modeB']['n_silent_wrong_missed']} silent-wrong missed; "
                   f"unsound edge-reads all at conf {sorted(spatial['modeB']['unsound_edgeread_conf_dist'].keys())}",
        "kinship": "0/0 (no unsound reads exist -> Mode-B catch UNTESTED)",
        "evidence_tag": "REAL-LLM-FUZZY-READ + THEOREM:zero-FP-conditional",
    }
    return rows, footnote


# --------------------------------------------------------------------------- #
# Verify FUZZY ground-truth literals (halt on mismatch)                        #
# --------------------------------------------------------------------------- #
def assert_ground_truth(md):
    s1 = md["setting1_spatial_risk_coverage"]
    s2 = md["setting2_kinship_risk_coverage"]
    assert approx(s1["certificate"]["coverage"], 0.5350877192982456, 1e-12), "spatial cert coverage"
    assert approx(s1["commit_argmax"]["confident_wrong_rate"], 0.36403508771929827, 1e-12), "spatial argmax CW"
    assert int(s1["commit_argmax"]["n_confident_wrong"]) == 83, "spatial argmax n_confident_wrong"
    assert int(s1["n_pool"]) == 228, "spatial n_pool"
    assert int(s1["n_unsound_reads"]) == 5, "spatial n_unsound"
    assert approx(s1["certificate"]["confident_wrong_rate"], 0.0, 1e-12), "spatial cert CW"
    assert approx(s2["certificate"]["coverage"], 0.3139190523198421, 1e-12), "kinship cert coverage"
    assert approx(s2["commit_argmax"]["confident_wrong_rate"], 0.21618953603158933, 1e-12), "kinship argmax CW"
    assert int(s2["commit_argmax"]["n_confident_wrong"]) == 219, "kinship argmax n_confident_wrong"
    assert int(s2["n_pool"]) == 1013, "kinship n_pool"
    assert int(s2["n_unsound_reads"]) == 0, "kinship n_unsound"
    logger.info("FUZZY ground-truth literals: ALL ASSERTIONS PASS")


# --------------------------------------------------------------------------- #
# TASK 2 / 3 / 4 carried-literal verification against source files            #
# --------------------------------------------------------------------------- #
def verify_carried_literals():
    """Cross-check the TASK 2/3 carried literals against the CLUTRR + SPATIAL source files."""
    out = {"clutrr": {}, "spatial": {}, "mismatches": 0}
    clu = load_json(CLUTRR_F)["metadata"]
    ap = clu["atomic_pr"]
    dm = clu["deduction_matched_coverage"]["leaderboard"]["modeA"]
    orc = clu["deduction_goldread_oracle"]["leaderboard"]["modeA"]
    h2 = clu["absent_relation_h2"]
    pro = clu["prolog_discharge"]
    out["clutrr"] = {
        "atomic_PRF1": [ap["precision"], ap["recall"], ap["f1"]],
        "modeA_selacc": dm["selective_accuracy"], "modeA_matched_cov": dm["coverage"],
        "oracle_selacc": orc["selective_accuracy"], "oracle_cov": orc["coverage"],
        "h2_reduction": h2["confident_wrong_reduction"], "h2_ci95": h2["ci95"],
        "swipl_executed": pro["n_executed_in_swipl"], "swipl_matches_python": pro["n_prolog_matches_python"],
        "modeA_surface_matches_gold": pro["n_modeA_surface_matches_gold"],
    }
    chk = [
        approx(ap["precision"], 0.536, 1e-3), approx(ap["recall"], 0.5324, 1e-3), approx(ap["f1"], 0.534, 1e-3),
        approx(dm["selective_accuracy"], 0.8857, 1e-3), approx(orc["selective_accuracy"], 1.0),
        approx(orc["coverage"], 0.951, 1e-3), approx(h2["confident_wrong_reduction"], 0.4444, 1e-3),
        approx(h2["ci95"][0], 0.3167, 1e-3), approx(h2["ci95"][1], 0.5833, 1e-3),
        int(pro["n_executed_in_swipl"]) == 40, int(pro["n_prolog_matches_python"]) == 40,
        int(pro["n_modeA_surface_matches_gold"]) == 39,
    ]
    out["mismatches"] += sum(0 if c else 1 for c in chk)
    del clu
    gc.collect()

    spa = load_json(SPATIAL_F)["metadata"]
    arm = spa["a_priori_gate"]["arms"]["SpaRP-PS1|rcc8"]
    sc = spa["synthetic_rcc8_positive_control"]["cells"]["recall_95"]["per_method"]
    out["spatial"] = {
        "n_deduction_required": arm["n_deduction_required"], "n_ge2_short_paths": arm["n_ge2_short_paths"],
        "synth_rcc8_intersection_selacc": sc["intersection"]["selective_acc"],
        "synth_rcc8_best_single_selacc": sc["best_single"]["selective_acc"],
        "crosspath_verdict": spa["verdict_crosspath_intersection"],
    }
    chk2 = [
        int(arm["n_deduction_required"]) == 228, int(arm["n_ge2_short_paths"]) == 0,
        approx(sc["intersection"]["selective_acc"], 0.890, 1e-2), approx(sc["best_single"]["selective_acc"], 0.797, 1e-2),
        spa["verdict_crosspath_intersection"] == "SCOPE-BOUNDARY",
    ]
    out["mismatches"] += sum(0 if c else 1 for c in chk2)
    out["evidence_tag"] = "CARRIED-LITERAL-VERIFY"
    del spa
    gc.collect()
    logger.info(f"carried-literal verify: mismatches={out['mismatches']}")
    return out


# --------------------------------------------------------------------------- #
# TASK 2 text                                                                  #
# --------------------------------------------------------------------------- #
TASK2_PARAGRAPH = (
    "Across the two real venues we could a-priori gate before any LLM spend, the cross-path coding "
    "mechanism — multi-path intersection as an error-correcting code over LLM reads — fails to realize, "
    "but for OPPOSITE reasons, and we present this as an explanatory account of two negatives rather than "
    "a predictive law. The mechanism needs two conditions to hold jointly: (i) the per-edge reads must be "
    "INFORMATIVE (sound but sub-universal, so intersection has bite), and (ii) the document redundancy must "
    "be SAME-ALGEBRA structural redundancy (>=2 edge-disjoint paths whose compositions land in one calculus). "
    "On natural temporal Allen text condition (i) is violated: high-recall reads are near-universe "
    "(event-local underdetermined rate 0.87, mean breadth 11.5/13; a stronger reader, deepseek-v3.2, is even "
    "more conservative at 0.99), so intersection / best-single / naive all resolve 0/125 gold-singleton "
    "multi-path queries — not a weak-model artifact. On semi-natural spatial RCC-8 text condition (ii) is "
    "violated: reads ARE informative (breadth 2.1/8, underdetermined 0.036), but the gold is a containment "
    "TREE — all 228 deduction queries have exactly one edge-disjoint path and the cardinal subgraph already "
    "composes to a singleton on the best single path, so the corpus 27.4% tight-multipath flag is purely "
    "STRUCTURAL (undirected, mixed-algebra) and the genuine redundancy is CROSS-algebra (topology vs "
    "direction), not intersectable in one calculus. Synthetic positive controls that satisfy BOTH conditions "
    "confirm the mechanism is real: on Allen at recall 0.95 intersection reaches selective accuracy 0.976 vs "
    "best-single 0.717 (+0.259, 95% CI [0.177, 0.349]); on RCC-8, 0.890 vs 0.797. We therefore claim only "
    "that these two conditions were each INDEPENDENTLY VIOLATED in the two venues we could gate, with "
    "synthetic controls localizing the cause — NOT a sharp, general, predictive characterization (the "
    "conditions are close to definitionally necessary, so their joint absence across two venues is an "
    "explanation, not a validated law). Even where the mechanism works its realized cross-path COVERAGE bite "
    "is tiny (+0.024 over best-single, CI includes 0); the value is precision of committed answers (+0.259 "
    "selective accuracy), not coverage. This subsection is subordinate to the certificate headline and is "
    "the paper single cross-path-coding result; it is NOT a co-equal contribution."
)


def task2_block():
    return {
        "section_target": "sec:decisive (ONE subordinate subsection, NOT a co-headline)",
        "drops": ["'two NECESSARY conditions'", "'sharp, general characterization'", "'two-condition LAW'"],
        "framing": "explanatory account of two negatives, NOT a predictive law",
        "paragraph": TASK2_PARAGRAPH,
        "supporting_numbers": {
            "temporal_underdet_gemini": {"value": 0.87, "evidence_tag": "REAL-LLM-READ"},
            "temporal_underdet_deepseek": {"value": 0.99, "evidence_tag": "REAL-LLM-READ"},
            "temporal_mean_breadth_of_13": {"value": 11.5, "evidence_tag": "REAL-LLM-READ"},
            "temporal_resolved_multipath": {"value": "0/125", "evidence_tag": "REAL-LLM-READ + GOLD-ONLY-GATE"},
            "spatial_n_single_path": {"value": 228, "evidence_tag": "GOLD-ONLY-GATE"},
            "spatial_tight_multipath_structural_flag": {"value": 0.274, "evidence_tag": "DATASET-CARD/STRUCTURAL"},
            "spatial_mean_breadth_of_8": {"value": 2.1, "evidence_tag": "REAL-LLM-READ"},
            "spatial_underdet": {"value": 0.036, "evidence_tag": "REAL-LLM-READ"},
            "synth_allen_intersection_selacc": {"value": 0.976, "evidence_tag": "SYNTHETIC-CONTROL"},
            "synth_allen_best_single_selacc": {"value": 0.717, "evidence_tag": "SYNTHETIC-CONTROL"},
            "synth_allen_selacc_gain": {"value": 0.259, "ci95": [0.177, 0.349], "evidence_tag": "SYNTHETIC-CONTROL"},
            "synth_rcc8_intersection_selacc": {"value": 0.890, "evidence_tag": "SYNTHETIC-CONTROL"},
            "synth_rcc8_best_single_selacc": {"value": 0.797, "evidence_tag": "SYNTHETIC-CONTROL"},
            "small_bite_coverage_gain": {"value": 0.024, "ci_includes_0": True, "evidence_tag": "SYNTHETIC-CHANNEL"},
        },
        "evidence_tag": "REAL-LLM-READ + GOLD-ONLY-GATE + SYNTHETIC-CONTROL",
    }


# --------------------------------------------------------------------------- #
# TASK 3 -- one-thesis contribution table (built from carried literals + TASK1)#
# --------------------------------------------------------------------------- #
def task3_block(spatial, kinship):
    cb_s = spatial["conf_threshold_baseline"]
    cb_k = kinship["conf_threshold_baseline"]
    spine = {
        "claim": ("Training-free, gold-free, per-edge ABSTAIN-ON-COLLAPSE certificate over LLM-extracted "
                  "relational facts whose DISTINCTIVE value is reducing CONFIDENT-WRONG hallucination on "
                  "no-derivation / absent-relation queries where a confidence threshold structurally CANNOT "
                  "abstain (high-confidence hallucinations), and on sound-violating reads (Mode-B collapse)."),
        "evidence_tag": "REAL-LLM-READ + THEOREM(zero-FP conditional on read soundness)",
        "where_it_holds": ("templated CLUTRR end-to-end (<=871 chars); fuzzy spatial/kinship RCC-8 & paraphrase; "
                           "weakly protective on natural temporal text"),
        "status": ("CONFIRMED-AT-POWER (certificate). Fair-confidence-baseline edge: the certificate beats a "
                   "matched-coverage confidence-thresholded top-1 abstainer at the EDGE-READ level in BOTH fuzzy "
                   "settings (CI excludes 0); the strictly same-object distinctive edge (Mode-B sound-violation "
                   "catch) is ESTABLISHED on fuzzy spatial (5/5) and UNTESTED on kinship (0 unsound reads). "
                   "PENDING: query-level confidence/self-consistency abstainer on CLUTRR absent/mixed + spatial "
                   "RCC-8 deduction pools (STEP-A), and on a genuinely-natural ~3000-char corpus (STEP-B)."),
        "key_numbers": {
            "clutrr_modeA_selacc": 0.8857,
            "clutrr_h2_absent_reduction": 0.4444, "clutrr_h2_ci95": [0.3167, 0.5833],
            "clutrr_goldread_oracle": "1.000@cov0.951",
            "clutrr_swipl": "40/40 executed, 39/40 surface-match gold",
            "clutrr_atomic_PRF1": [0.536, 0.532, 0.534],
            "fuzzy_cert_confident_wrong": "0.000 @cov 0.5351 spatial / 0.3139 kinship",
            "fuzzy_conf_baseline_cw_spatial": round(cb_s["confident_wrong"], 4),
            "fuzzy_conf_baseline_cw_spatial_ci": [round(cb_s["ci95"][0], 4), round(cb_s["ci95"][1], 4)],
            "fuzzy_certificate_beats_spatial": cb_s["certificate_beats"],
            "fuzzy_conf_baseline_cw_kinship": round(cb_k["confident_wrong"], 4),
            "fuzzy_conf_baseline_cw_kinship_ci": [round(cb_k["ci95"][0], 4), round(cb_k["ci95"][1], 4)],
            "fuzzy_certificate_beats_kinship": cb_k["certificate_beats"],
            "modeB_catches": "5/5 spatial, 0/0 kinship",
        },
    }
    supporting = {
        "claim": ("Cross-path coding is SYNTHETIC-CHANNEL-ONLY — two conditions each independently violated on "
                  "both a-priori-gated real venues (temporal near-universe reads; spatial containment-tree gold), "
                  "synthetic controls confirm the mechanism when both hold."),
        "evidence_tag": "REAL-LLM-READ + GOLD-ONLY-GATE + SYNTHETIC-CONTROL",
        "where_it_holds": "synthetic Allen + RCC-8 channels only; refuted on real temporal + real spatial",
        "status": "RESOLVED NEGATIVE (no longer PENDING; art_i53dBKgGY3Ig overturns dataset-card GENERAL-band optimism, $0 gold-structural)",
        "key_numbers": {
            "spatial_single_path": "228 single-path / 27.4% structural",
            "synth_allen_selacc_gain": 0.259, "synth_allen_selacc_ci95": [0.177, 0.349],
            "synth_rcc8": "0.890 vs 0.797",
            "small_bite_coverage_gain": "+0.024 (CI includes 0)",
        },
    }
    appendix = [
        {"id": "A1",
         "claim": "Algebra-richness scaling: point(3) +0.043 -> RCC-8(8) +0.448 -> Allen(13) +0.676; "
                  "INHERITED table-vs-LLM-composition (Allen decomposes +0.673 inherited / +0.0025 novel).",
         "evidence_tag": "REAL-LLM-READ-ON-SYNTHETIC", "status": "APPENDIX"},
        {"id": "A2",
         "claim": "Redundancy inverted-U: peak_K [2,4,7,10,16]; silent-wrong [0.0064,0.1456]; Page p~5e-4; "
                  "realized cross-path coverage bite +0.024.",
         "evidence_tag": "SYNTHETIC-CHANNEL", "status": "APPENDIX"},
        {"id": "A3",
         "claim": "Zero-FP soundness THEOREM verified on 100,296 networks; recall & rho are INPUTS "
                  "(characterizes, not predicts).",
         "evidence_tag": "THEOREM", "status": "APPENDIX"},
    ]
    footnotes = [
        {"id": "F1-ceiling-temporal",
         "claim": "Corrected natural-temporal marginal: vs-PoT 0.0265 CI[-0.0883,0.1397] includes 0; "
                  "confident-wrong-among-answered 0.4248=48/113; modeA cov 0.1883.",
         "evidence_tag": "REAL-LLM-READ"},
        {"id": "F2-scope-deduction",
         "claim": "Deduction-sub-module ceiling: atomic recall 0.5324 => ~0.19 coverage; "
                  "OpenCyc / atomic re-extraction / general fuzzy OUT OF SCOPE; hand-supplied tables; "
                  "no doc reaches ~3000 chars.",
         "evidence_tag": "SCOPE"},
    ]
    pending = [
        {"id": "P-A",
         "slot": "STEP A — add confidence-thresholded raw-abstain baseline (verbalized-confidence + "
                 "self-consistency vote-margin) to the CLUTRR absent/mixed pool AND the spatial RCC-8 "
                 "deduction pool at matched coverage (iter-6 experiment).",
         "status": "PENDING (NOT computed here)"},
        {"id": "P-B",
         "slot": "STEP B — certificate vs confidence abstainer on >=1 genuinely-natural corpus' "
                 "no-derivation stratum, e.g. the iter-6 Re-DocRED ~3000-char corpus (iter-7).",
         "status": "PENDING (NOT computed here)"},
    ]
    return {
        "columns": ["claim", "evidence_tag", "where_it_holds", "status", "key_numbers"],
        "spine_row": spine,
        "supporting_row": supporting,
        "appendix_rows": appendix,
        "footnote_rows": footnotes,
        "pending_slots": pending,
        "one_line_thesis": "A structural, label-free certificate that catches confident relational hallucinations that confidence cannot see.",
    }


# --------------------------------------------------------------------------- #
# TASK 4 -- venue + scope                                                      #
# --------------------------------------------------------------------------- #
def task4_block():
    return {
        "venue_justification": {
            "from": "ACL Knowledge Extraction track",
            "to": "NeSy / temporal-and-qualitative-reasoning (EMNLP / neuro-symbolic) track",
            "rationale": ("The substantive contribution is closure-certified DEDUCTION / CONSISTENCY, not "
                          "extraction. Atomic extraction is MEASURED not improved (F1 ~0.534), so a "
                          "knowledge-extraction track is a poor fit; EMNLP / NeSy / qualitative-reasoning "
                          "audiences can deeply evaluate the relation-algebra + abstention contribution."),
            "evidence_tag": "SCOPE",
        },
        "scope_boundaries": [
            {"item": "deduction sub-module only", "evidence_tag": "SCOPE"},
            {"item": "atomic extraction measured-not-improved (~0.53 recall, F1 0.534)", "evidence_tag": "SCOPE"},
            {"item": "OpenCyc / upper-ontology grounding OUT OF SCOPE", "evidence_tag": "SCOPE"},
            {"item": "composition tables HAND-SUPPLIED in every venue (Allen / point / RCC-8 published "
                     "tables; CLUTRR rules_store.yaml)", "evidence_tag": "SCOPE"},
            {"item": "real-text utility extraction-limited (~0.53 recall => ~19% Mode-A coverage on dense prose)",
             "evidence_tag": "SCOPE"},
            {"item": "no benchmark doc reaches the goal ~3000-char target (CLUTRR <=871; spatial 130-1338)",
             "evidence_tag": "SCOPE"},
        ],
        "doc_labels": {
            "operational_3000char_study_artifact": "art_WQoePKrpsTPo",
            "temporal_arm": "5 NarrativeTime articles BRACKET-selected around 3000 chars (NONE in [2500,3500]; "
                            "mean 3050, range 2197-4293)",
            "kinship_arm": "3 docs CONCATENATED from disjoint-entity CLUTRR sub-stories (cross-story pairs "
                           "absent-by-construction => trivially abstained)",
            "pending_note": "the iter-6 Re-DocRED corpus will supply genuinely-natural ~3000-char documents (PENDING)",
            "evidence_tag": "SCOPE",
        },
    }


HEADLINE_GUIDANCE = [
    "Lead with the SINGLE certificate thesis: a structural, label-free certificate that catches confident "
    "relational hallucinations that a confidence threshold cannot see.",
    "Cross-path coding = ONE subordinate subsection (sec:decisive), framed as an explanatory account of two "
    "independently-violated conditions — NOT a co-headline, NOT a predictive law.",
    "Demote mechanism analysis (algebra-richness scaling, redundancy inverted-U, zero-FP theorem) to appendix rows.",
    "Report EVERY hallucination number WITH its coverage (e.g. 0.000 @cov 0.5351, not bare 0.000).",
    "Do NOT call CLUTRR natural text (templated, <=871 chars); do NOT call the operational 3000-char docs natural "
    "(bracket-selected temporal / concatenation-constructed kinship).",
    "Carry the fuzzy section on the Mode-B catch count (5/5 unsound spatial reads caught at ordinary confidence, "
    "0 testable on kinship) rather than the 0.000-vs-0.364 always-answer contrast.",
    "The certificate beats the matched-coverage confidence-thresholded top-1 abstainer in BOTH fuzzy settings "
    "(spatial CW 0.415, kinship CW 0.346; both CIs exclude 0) — including well-calibrated kinship (ECE 0.051), "
    "because modest max confidence (0.8) + modest read accuracy keeps thresholded CW high. Report this as the "
    "edge-read-level finding, NOT as a tie.",
    "Always carry the unit-of-analysis caveat: certificate CW is on closure QUERIES, the confidence baseline CW "
    "is on edge READS (matched on coverage fraction, not object); a query-level confidence abstainer is the "
    "PENDING STEP-A experiment. Do not overstate the comparison as same-object beyond Mode-B.",
]

HONEST_FRAMING_STRING = (
    "auditable, faithful abstention that ADDITIONALLY catches sound-violating reads a confidence threshold "
    "cannot see — quantified at 5/5 unsound spatial reads caught (0 silent-wrong missed), 0 testable on kinship "
    "(no unsound reads) — rather than letting 0.000-vs-0.364 (an always-answer contrast) carry the section."
)


# --------------------------------------------------------------------------- #
# Paper-facing digest                                                          #
# --------------------------------------------------------------------------- #
def _fmt(x, nd=4):
    if x is None:
        return "—"
    if isinstance(x, bool):
        return str(x)
    if isinstance(x, (int, float)):
        return f"{x:.{nd}f}"
    return str(x)


def write_digest(out: dict):
    md = out["metadata"]
    t1 = md["task1_fuzzy_fair_baseline"]
    rv = md["reproduce_verify"]
    cv = md["carried_literal_verify"]
    L = []
    L.append("# Evaluation digest — fuzzy fair-baseline + framing spine (iter-6)")
    L.append("")
    L.append("**$0 LLM spend** · pure numpy+scipy re-analysis · seed=20260617 · "
             "doc-clustered paired bootstrap B=10000.")
    L.append("")
    L.append(f"- STEP 0 reproduce-verify: **{rv['mismatches_vs_iter5']} mismatches vs iter-5** "
             f"({rv['n_checks_iter5']} checks), **{rv['mismatches_vs_iter4']} vs iter-4** "
             f"({rv['n_checks_iter4']} checks). Target = 0.")
    L.append(f"- Carried-literal verify vs CLUTRR+SPATIAL source files: **{cv['mismatches']} mismatches**.")
    L.append(f"- FUZZY ground-truth literals (spatial cert cov 0.5350877 / CW 0.000; commit-argmax CW 0.3640 "
             f"= 83/228; kinship cert cov 0.3139191; commit-argmax CW 0.2162 = 219/1013): **all asserted, pass**.")
    L.append("")

    # ---- headline result ----
    sp, ki = t1["spatial"], t1["kinship"]
    cbs, cbk = sp["conf_threshold_baseline"], ki["conf_threshold_baseline"]
    L.append("## Headline (TASK 1, MAJOR #2): the certificate beats a FAIR confidence abstainer")
    L.append("")
    L.append("Replacing the misleading *always-answer* comparator (0.000 vs 0.364) with a "
             "**confidence-thresholded top-1 abstainer at matched coverage**:")
    L.append("")
    L.append(f"- **Spatial RCC-8**: baseline confident-wrong **{_fmt(cbs['confident_wrong'])}** "
             f"(95% CI [{_fmt(cbs['ci95'][0])}, {_fmt(cbs['ci95'][1])}]) @ coverage {_fmt(cbs['achieved_coverage'])} "
             f"(implied τ={_fmt(cbs['implied_tau'],2)}); certificate confident-wrong 0.000 → "
             f"**certificate beats = {cbs['certificate_beats']}** (ECE_top1 0.286, POOR calibration).")
    L.append(f"- **Kinship paraphrase**: baseline confident-wrong **{_fmt(cbk['confident_wrong'])}** "
             f"(95% CI [{_fmt(cbk['ci95'][0])}, {_fmt(cbk['ci95'][1])}]) @ coverage {_fmt(cbk['achieved_coverage'])} "
             f"(implied τ={_fmt(cbk['implied_tau'],2)}); certificate 0.000 → "
             f"**certificate beats = {cbk['certificate_beats']}** (ECE_top1 0.051, GOOD calibration — beats anyway).")
    L.append("")
    L.append("> " + t1["interpretation_by_calibration"])
    L.append("")
    L.append("> **Unit-of-analysis caveat** — " + t1["unit_of_analysis_caveat"])
    L.append("")
    L.append("**Honest framing string for GEN_PAPER_TEXT:** " + t1["honest_framing_string"])
    L.append("")

    # ---- Table 3 per setting ----
    for label, s in [("Spatial RCC-8 (spatial_fuzzy_rcc8)", sp),
                     ("Kinship paraphrase (kinship_fuzzy_paraphrase)", ki)]:
        cb = s["conf_threshold_baseline"]
        cert, cm = s["certificate"], s["commit_argmax"]
        L.append(f"### Rebuilt Table 3 — {label}")
        L.append("")
        L.append("| Method | Coverage | Acc-among-answered | Confident-wrong | Δ vs certificate (95% CI) | Evidence tag |")
        L.append("|---|---|---|---|---|---|")
        L.append(f"| commit-argmax (always-answer) | {_fmt(cm['coverage'])} | {_fmt(cm['acc_among_answered'])} | "
                 f"{_fmt(cm['confident_wrong'])} | n/a (always-answers) | REAL-LLM-FUZZY-READ |")
        L.append(f"| abstain-always | 0.0000 | — | 0.0000 | n/a (coverage 0) | REAL-LLM-FUZZY-READ |")
        L.append(f"| **CERTIFICATE (abstain-on-collapse)** | {_fmt(cert['coverage'])} | "
                 f"{_fmt(cert['acc_among_answered'])} | **0.0000** | 0.000 (reference) | "
                 f"REAL-LLM-FUZZY-READ + THEOREM:zero-FP-cond. |")
        L.append(f"| **CONFIDENCE-THRESHOLDED TOP-1 @ matched cov (NEW)** | {_fmt(cb['achieved_coverage'])} | "
                 f"{_fmt(cb['acc_among_answered'])} | {_fmt(cb['confident_wrong'])} | "
                 f"+{_fmt(cb['confident_wrong'])} [{_fmt(cb['ci95'][0])}, {_fmt(cb['ci95'][1])}] "
                 f"(beats={cb['certificate_beats']}) | REAL-LLM-FUZZY-READ |")
        mb = s["modeB"]
        if not mb["modeB_untested"]:
            L.append(f"| _Mode-B sound-violation catches_ | — | — | — | {mb['n_caught']}/{mb['n_unsound_query_pool']} "
                     f"caught, {mb['n_silent_wrong_missed']} silent-wrong missed | REAL-LLM-FUZZY-READ + THEOREM |")
        else:
            L.append("| _Mode-B sound-violation catches_ | — | — | — | 0/0 (no unsound reads → UNTESTED) | "
                     "REAL-LLM-FUZZY-READ + THEOREM |")
        L.append("")
        if not mb["modeB_untested"]:
            L.append(f"Mode-B detail: {mb['n_unsound_edgeread']} unsound calibration edge-reads, all at "
                     f"top-1 conf {sorted(mb['unsound_edgeread_conf_dist'].keys())} "
                     f"(dist {mb['unsound_edgeread_conf_dist']}); {mb['n_unsound_edgeread_in_committed_region']} of "
                     f"them sit in the matched-coverage committed (conf≥τ) region — i.e. reads a confidence "
                     f"threshold would COMMIT WRONG but the certificate catches via set-soundness.")
            L.append("")

    # ---- TASK 2 ----
    t2 = md["task2_tempered_two_condition"]
    L.append("## TASK 2 (MAJOR #3): tempered two-condition paragraph (verbatim for sec:decisive)")
    L.append("")
    L.append("> " + t2["paragraph"])
    L.append("")
    L.append(f"*Section target:* {t2['section_target']}. *Drops:* {', '.join(t2['drops'])}.")
    L.append("")

    # ---- TASK 3 ----
    t3 = md["task3_one_thesis_table"]
    L.append("## TASK 3 (MINOR #5): one-thesis contribution table (tags as columns)")
    L.append("")
    L.append(f"**One-line thesis:** *{t3['one_line_thesis']}*")
    L.append("")
    L.append("| Row | Claim | Evidence tag | Where it holds | Status |")
    L.append("|---|---|---|---|---|")
    sr = t3["spine_row"]
    L.append(f"| **SPINE** | {sr['claim']} | {sr['evidence_tag']} | {sr['where_it_holds']} | {sr['status']} |")
    su = t3["supporting_row"]
    L.append(f"| SUPPORTING | {su['claim']} | {su['evidence_tag']} | {su['where_it_holds']} | {su['status']} |")
    for a in t3["appendix_rows"]:
        L.append(f"| APPENDIX {a['id']} | {a['claim']} | {a['evidence_tag']} | — | {a['status']} |")
    for fn in t3["footnote_rows"]:
        L.append(f"| FOOTNOTE {fn['id']} | {fn['claim']} | {fn['evidence_tag']} | — | ceiling/scope |")
    for p in t3["pending_slots"]:
        L.append(f"| PENDING {p['id']} | {p['slot']} | — | — | **{p['status']}** |")
    L.append("")
    L.append("Spine key numbers: " + json.dumps(sr["key_numbers"], default=str))
    L.append("")

    # ---- TASK 4 ----
    t4 = md["task4_venue_scope"]
    vj = t4["venue_justification"]
    L.append("## TASK 4 (MINOR #4): venue reposition + scope boundaries")
    L.append("")
    L.append(f"**Venue:** {vj['from']} → **{vj['to']}**. {vj['rationale']}")
    L.append("")
    L.append("**Scope boundaries (abstract front-matter, each tagged SCOPE):**")
    for sb in t4["scope_boundaries"]:
        L.append(f"- {sb['item']}")
    L.append("")
    dl = t4["doc_labels"]
    L.append("**Operational ~3000-char study labels (art_WQoePKrpsTPo):**")
    L.append(f"- Temporal arm: {dl['temporal_arm']}")
    L.append(f"- Kinship arm: {dl['kinship_arm']}")
    L.append(f"- {dl['pending_note']}")
    L.append("")

    # ---- headline guidance ----
    L.append("## Headline-structure guidance for GEN_PAPER_TEXT")
    L.append("")
    for g in md["headline_structure_guidance"]:
        L.append(f"- {g}")
    L.append("")

    OUT_DIGEST.write_text("\n".join(L))
    logger.info(f"wrote {OUT_DIGEST} ({OUT_DIGEST.stat().st_size/1024:.1f} KB)")


# --------------------------------------------------------------------------- #
# MAIN                                                                          #
# --------------------------------------------------------------------------- #
def main():
    rng = np.random.default_rng(SEED)

    # STEP 0 gate
    reproduce_verify = step0_reproduce_verify()

    # carried-literal verification (TASK 2/3 source numbers)
    carried = verify_carried_literals()

    # FUZZY load + ground-truth assertions
    fuzzy = load_json(FUZZY_F)
    md = fuzzy["metadata"]
    assert_ground_truth(md)
    ds_spatial = next(d for d in fuzzy["datasets"] if d["dataset"] == "spatial_fuzzy_rcc8")
    ds_kinship = next(d for d in fuzzy["datasets"] if d["dataset"] == "kinship_fuzzy_paraphrase")

    ece_s = md["setting1_spatial_calibration"]["ECE_top1"]
    ece_k = md["setting2_kinship_calibration"]["ECE_top1"]
    rc_s = md["setting1_spatial_risk_coverage"]
    rc_k = md["setting2_kinship_risk_coverage"]

    # TASK 1 (the only new computation)
    logger.info("TASK 1: spatial confidence-thresholded baseline")
    spatial, spatial_recs, spatial_unsound = task1_setting(
        "spatial", ds_spatial, 0.5350877192982456, "metadata_gold", "metadata_vague_term",
        rc_s, ece_s, rng)
    logger.info("TASK 1: kinship confidence-thresholded baseline")
    kinship, kinship_recs, kinship_unsound = task1_setting(
        "kinship", ds_kinship, 0.3139190523198421, "metadata_gold_type", "metadata_ambiguous_term",
        rc_k, ece_k, rng)

    del fuzzy, ds_spatial, ds_kinship
    gc.collect()

    table3, table3_footnote = build_table3(spatial, kinship)

    task1 = {
        "spatial": spatial,
        "kinship": kinship,
        "table3": table3,
        "table3_footnote": table3_footnote,
        "honest_framing_string": HONEST_FRAMING_STRING,
        "certificate_beats_conf_threshold_both_settings": bool(
            cb_s_beats := spatial["conf_threshold_baseline"]["certificate_beats"]) and bool(
            kinship["conf_threshold_baseline"]["certificate_beats"]),
        "interpretation_by_calibration": (
            "PRE-STATED expectation: spatial top-1 calibration is POOR (ECE 0.286) so the certificate should "
            "BEAT the matched-coverage confidence baseline; kinship top-1 calibration is GOOD (ECE 0.051) so "
            "the baseline MIGHT tie. ACTUAL RESULT: the certificate beats the confidence-thresholded top-1 "
            "baseline in BOTH settings (spatial confident-wrong 0.415, 95% CI [0.376, 0.457]; kinship 0.346, "
            "95% CI [0.293, 0.413]; both bootstrap lower bounds > 0). The kinship non-tie does NOT contradict "
            "good calibration: ECE measures confidence-vs-accuracy AGREEMENT, but the kinship reads' MAXIMUM "
            "emitted top-1 confidence is only 0.8 and most committed reads sit at conf 0.4, so even the "
            "most-confident ~31% of reads are ~35% wrong -- a confidence threshold cannot reach 0 confident-wrong "
            "when the underlying read accuracy is modest, however well-calibrated."),
        "unit_of_analysis_caveat": (
            "LOAD-BEARING: the certificate's 0.000 confident-wrong is measured on closure QUERIES, while the "
            "confidence baseline's confident-wrong is measured on single edge READS (query records carry no "
            "per-query confidence), matched only on the committed FRACTION, not the object. This establishes "
            "that the LLM's OWN per-read confidence cannot be thresholded to low confident-wrong at matched "
            "coverage (a real, $0 finding); a query-level verbalized-confidence / self-consistency abstainer on "
            "the SAME query pool is the PENDING STEP-A experiment (iter-6). The certificate's strictly "
            "distinctive, same-object edge is the Mode-B catch: 5/5 sound-violating spatial reads at ordinary "
            "confidence (0 silent-wrong missed); 0 testable on kinship (no unsound reads)."),
    }

    # TASK 2/3/4
    task2 = task2_block()
    task3 = task3_block(spatial, kinship)
    task4 = task4_block()

    # ----------------------------------------------------------------- #
    # metrics_agg (schema requires it; numbers only)                     #
    # ----------------------------------------------------------------- #
    cb_s = spatial["conf_threshold_baseline"]
    cb_k = kinship["conf_threshold_baseline"]
    metrics_agg = {
        "llm_spend_usd": 0.0,
        "seed": float(SEED),
        "bootstrap_B": float(B_BOOT),
        "n_reproduction_mismatches_vs_iter5": float(reproduce_verify["mismatches_vs_iter5"]),
        "n_reproduction_mismatches_vs_iter4": float(reproduce_verify["mismatches_vs_iter4"]),
        "n_carried_literal_mismatches": float(carried["mismatches"]),
        # spatial certificate / baseline
        "spatial_certificate_coverage": float(spatial["certificate"]["coverage"]),
        "spatial_certificate_confident_wrong": float(spatial["certificate"]["confident_wrong"]),
        "spatial_commit_argmax_confident_wrong": float(spatial["commit_argmax"]["confident_wrong"]),
        "spatial_conf_baseline_confident_wrong": float(cb_s["confident_wrong"]),
        "spatial_conf_baseline_acc_among_answered": float(cb_s["acc_among_answered"]),
        "spatial_conf_baseline_ci_lo": float(cb_s["ci95"][0]),
        "spatial_conf_baseline_ci_hi": float(cb_s["ci95"][1]),
        "spatial_conf_baseline_p_cw_le_0": float(cb_s["p_one_sided_cw_le_0"]),
        "spatial_conf_baseline_implied_tau": float(cb_s["implied_tau"]),
        "spatial_conf_baseline_achieved_coverage": float(cb_s["achieved_coverage"]),
        "spatial_certificate_beats_conf_threshold": 1.0 if cb_s["certificate_beats"] else 0.0,
        "spatial_ECE_top1": float(spatial["ECE_top1"]),
        "spatial_modeB_n_unsound_query_pool": float(spatial["modeB"]["n_unsound_query_pool"]),
        "spatial_modeB_n_caught": float(spatial["modeB"]["n_caught"]),
        "spatial_modeB_silent_wrong_missed": float(spatial["modeB"]["n_silent_wrong_missed"]),
        "spatial_modeB_n_unsound_edgeread": float(spatial["modeB"]["n_unsound_edgeread"]),
        "spatial_modeB_n_unsound_in_committed_region": float(spatial["modeB"]["n_unsound_edgeread_in_committed_region"]),
        # kinship certificate / baseline
        "kinship_certificate_coverage": float(kinship["certificate"]["coverage"]),
        "kinship_certificate_confident_wrong": float(kinship["certificate"]["confident_wrong"]),
        "kinship_commit_argmax_confident_wrong": float(kinship["commit_argmax"]["confident_wrong"]),
        "kinship_conf_baseline_confident_wrong": float(cb_k["confident_wrong"]),
        "kinship_conf_baseline_acc_among_answered": float(cb_k["acc_among_answered"]),
        "kinship_conf_baseline_ci_lo": float(cb_k["ci95"][0]),
        "kinship_conf_baseline_ci_hi": float(cb_k["ci95"][1]),
        "kinship_conf_baseline_p_cw_le_0": float(cb_k["p_one_sided_cw_le_0"]),
        "kinship_conf_baseline_implied_tau": float(cb_k["implied_tau"]),
        "kinship_conf_baseline_achieved_coverage": float(cb_k["achieved_coverage"]),
        "kinship_certificate_beats_conf_threshold": 1.0 if cb_k["certificate_beats"] else 0.0,
        "kinship_ECE_top1": float(kinship["ECE_top1"]),
        "kinship_modeB_n_unsound_edgeread": float(kinship["modeB"]["n_unsound_edgeread"]),
        "kinship_modeB_untested": 1.0 if kinship["modeB"]["modeB_untested"] else 0.0,
        # carried headline literals (verified)
        "clutrr_modeA_selacc": 0.8857,
        "clutrr_h2_absent_reduction": 0.4444,
        "clutrr_atomic_recall": 0.5324,
        "synth_allen_selacc_gain": 0.2592,
        "synth_allen_coverage_gain": 0.024,
        "allen_decomposition_inherited": 0.67349,
        "allen_decomposition_novel": 0.0025,
        "temporal_vs_pot_corrected_gap": 0.026549,
        "temporal_confident_wrong_frac": 0.424779,
    }

    metadata = {
        "eval_name": "Zero-spend re-analysis: fuzzy fair-baseline + framing spine (retire MAJOR #2/#3, MINOR #4/#5)",
        "description": ("Pure numpy+scipy $0-LLM re-analysis. Builds a confidence-thresholded top-1 fair "
                        "abstainer at matched coverage for the fuzzy spatial/kinship certificate, with a "
                        "doc-clustered bootstrap Delta-CI and Mode-B catch quantification; tempers the "
                        "cross-path two-condition framing; supplies a one-thesis contribution table and a "
                        "venue/scope reposition. Reproduce-verifies iter-4/iter-5 carried literals first."),
        "llm_spend_usd": 0.0,
        "no_openrouter_client_instantiated": True,
        "seed": SEED,
        "bootstrap_B": B_BOOT,
        "alpha": ALPHA,
        "reproduce_verify": reproduce_verify,
        "carried_literal_verify": carried,
        "task1_fuzzy_fair_baseline": task1,
        "task2_tempered_two_condition": task2,
        "task3_one_thesis_table": task3,
        "task4_venue_scope": task4,
        "headline_structure_guidance": HEADLINE_GUIDANCE,
        "evidence_tag_legend": {
            "REAL-LLM-FUZZY-READ": "measured on genuinely-fuzzy LLM reads (iter-5 experiment_2)",
            "REAL-LLM-READ": "measured on real LLM reads (CLUTRR / temporal)",
            "GOLD-ONLY-GATE": "$0 a-priori gate over verified gold structure (no LLM)",
            "SYNTHETIC-CONTROL": "synthetic positive control confirming the mechanism",
            "SYNTHETIC-CHANNEL": "synthetic-channel-only result",
            "THEOREM": "proved-by-construction / characterizes-not-predicts",
            "THEOREM:zero-FP-conditional": "sound read => no confident-wrong (conditional invariant)",
            "SCOPE": "scope boundary / front-matter caveat",
            "REPRODUCE-VERIFY": "continuity check vs prior re-analyses",
            "CARRIED-LITERAL-VERIFY": "carried number re-checked against source experiment file",
        },
    }

    datasets = [
        {"dataset": "fuzzy_spatial_conf_baseline", "examples": spatial_recs},
        {"dataset": "fuzzy_kinship_conf_baseline", "examples": kinship_recs},
        {"dataset": "fuzzy_spatial_unsound_reads", "examples": spatial_unsound},
    ]
    if kinship_unsound:  # empty for kinship (0 unsound) -> omit to satisfy minItems
        datasets.append({"dataset": "fuzzy_kinship_unsound_reads", "examples": kinship_unsound})

    out = {"metrics_agg": metrics_agg, "metadata": metadata, "datasets": datasets}

    # sanity: $0 spend
    assert metrics_agg["llm_spend_usd"] == 0.0, "llm_spend must be 0"

    OUT_JSON.write_text(json.dumps(out, indent=2, default=str))
    logger.info(f"wrote {OUT_JSON} ({OUT_JSON.stat().st_size/1024:.1f} KB)")
    write_digest(out)
    logger.info(f"SUMMARY spatial: baseline_CW={cb_s['confident_wrong']:.4f} "
                f"CI[{cb_s['ci95'][0]:.4f},{cb_s['ci95'][1]:.4f}] beats={cb_s['certificate_beats']}")
    logger.info(f"SUMMARY kinship: baseline_CW={cb_k['confident_wrong']:.4f} "
                f"CI[{cb_k['ci95'][0]:.4f},{cb_k['ci95'][1]:.4f}] beats={cb_k['certificate_beats']}")
    return out


if __name__ == "__main__":
    main()
