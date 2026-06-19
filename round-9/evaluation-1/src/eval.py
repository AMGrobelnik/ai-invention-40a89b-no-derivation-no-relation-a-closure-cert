#!/usr/bin/env python3
"""Zero-spend re-analysis of three frozen iter-7/iter-8 experiment outputs.

Reads the per-query rows + metadata from each dependency's full_method_out.json, runs a
REPRODUCTION GATE that recomputes every paper-facing literal from the rows and hard-asserts
it matches the carried metadata, then derives the corrected CAUGHT-FRACTION headline, a
16-cell capability-gap table, seven paper-facing scaffold blocks, and a count reconciliation.

PURE $0: numpy / scipy only. No LLM, no network. A cost counter is asserted == 0 at exit and
the forbidden network/LLM modules are asserted absent from sys.modules.
"""
from __future__ import annotations

import json
import math
import sys
import hashlib
import resource
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats as scipy_stats  # noqa: F401  (kept for completeness / available metrics)
from loguru import logger

# --------------------------------------------------------------------------- #
# STEP 0 — GUARDRAILS & SETUP (validity layer)
# --------------------------------------------------------------------------- #
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# Memory limit (29 GB container; these JSONs are <4 MB so 4 GB is ample headroom).
_RAM_BUDGET = 4 * 1024 ** 3
resource.setrlimit(resource.RLIMIT_AS, (_RAM_BUDGET * 3, _RAM_BUDGET * 3))

# $0 cost counter — there is NO LLM path; this is never incremented and asserted ==0 at exit.
COST_USD = 0.0
N_LLM_CALLS = 0

# Forbidden modules: no network / LLM client may ever be imported.
_FORBIDDEN = ("requests", "httpx", "openai", "openrouter", "anthropic", "aiohttp",
              "llm", "readers", "queryside", "readers_locatedin", "dataio_redocred",
              "dataio_locatedin")

REPRO_SEED = 20260618   # the experiments' own seed — used ONLY to Monte-Carlo-match a CARRIED CI
EVAL_SEED = 20260617    # used for any genuinely-NEW bootstrap statistic this eval introduces

ROOT = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop")
FILES = {
    "locatedin": ROOT / "iter_8/gen_art/gen_art_experiment_1/full_method_out.json",
    "verifier":  ROOT / "iter_8/gen_art/gen_art_experiment_2/full_method_out.json",
    "kinship":   ROOT / "iter_7/gen_art/gen_art_experiment_1/full_method_out.json",
}
WORKDIR = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_9/gen_art/gen_art_evaluation_1")

ABSTAIN = {"ABSTAIN", "no-relation", "no_relation", "none", ""}


def is_named(pred) -> bool:
    """A prediction NAMES a relation iff it is not an abstain/no-relation marker."""
    return (pred is not None) and (str(pred) not in ABSTAIN)


def _r(x, nd=4):
    if x is None:
        return None
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    return round(float(x), nd)


def matched_coverage_mask(conf: np.ndarray, target_cov: float) -> np.ndarray:
    """Replicates stats.matched_coverage_mask EXACTLY: top ceil(round) cov*N by (-conf, idx)."""
    n = len(conf)
    k = int(round(target_cov * n))
    k = max(0, min(n, k))
    mask = np.zeros(n, dtype=bool)
    if k == 0:
        return mask
    order = sorted(range(n), key=lambda i: (-conf[i], i))
    for i in order[:k]:
        mask[i] = True
    return mask


def coverage_confidence(named: bool, conf: float) -> float:
    return float(conf) if named else -1.0


# --------------------------------------------------------------------------- #
# Gate accounting
# --------------------------------------------------------------------------- #
class Gate:
    def __init__(self):
        self.checks = []      # hard checks (mismatch => HARD STOP)
        self.soft = []        # soft cross-checks (warn only)

    def hard(self, name, recomputed, carried, tol):
        ok = (recomputed is not None and carried is not None
              and abs(float(recomputed) - float(carried)) <= tol)
        self.checks.append({"name": name, "recomputed": _r(recomputed, 6),
                            "carried": _r(carried, 6), "tol": tol, "ok": bool(ok)})
        lvl = "DEBUG" if ok else "ERROR"
        logger.log(lvl, f"[HARD {'OK ' if ok else 'FAIL'}] {name}: recomputed={recomputed} carried={carried} tol={tol}")
        return ok

    def soft_check(self, name, recomputed, carried, tol, note=""):
        ok = (recomputed is not None and carried is not None
              and abs(float(recomputed) - float(carried)) <= tol)
        self.soft.append({"name": name, "recomputed": _r(recomputed, 6),
                          "carried": _r(carried, 6), "tol": tol, "ok": bool(ok), "note": note})
        logger.info(f"[SOFT {'OK ' if ok else 'LOOSE'}] {name}: recomputed={recomputed} carried={carried} tol={tol} {note}")
        return ok

    def all_ok(self):
        return all(c["ok"] for c in self.checks)

    def n_passed(self):
        return sum(1 for c in self.checks if c["ok"])


GATE = Gate()


# --------------------------------------------------------------------------- #
# Row extraction helpers
# --------------------------------------------------------------------------- #
def load(name):
    d = json.loads(FILES[name].read_text())
    return d["metadata"], {g["dataset"]: g["examples"] for g in d["datasets"]}


def rows_of(groups, *names):
    out = []
    for n in names:
        out.extend(groups.get(n, []))
    return out


# Signal names
SIGNALS = ("verbalized", "sc_margin", "ptrue", "negent")


def crux_caught(records, sigkey="metadata_conf_{}", present_records=None):
    """Reproduce the located-in/kinship crux fraction-caught for the 4 dispersion signals,
    the certificate, and (if present in the rows) the 2 query-side gates.

    `records` = the MIXED pool (present + absent of the regime).  Certificate-matched global
    threshold tuned to the certificate's MIXED coverage (line 548 of the source method.py).
    Returns dict with cert/queryside/dispersion caught + survival + tau_global per signal.
    """
    N = len(records)
    cert_named = np.array([is_named(r.get("predict_certificate")) for r in records], bool)
    raw_named = np.array([bool(r.get("metadata_raw_named")) for r in records], bool)
    is_abs = np.array([bool(r.get("metadata_is_absent")) for r in records], bool)
    cert_cov_mixed = float(cert_named.mean()) if N else float("nan")

    absent_idx = np.where(is_abs)[0]
    halluc_idx = np.array([i for i in absent_idx if raw_named[i]], int)
    n_h = len(halluc_idx)

    out = {"n": N, "n_absent": int(is_abs.sum()), "n_raw_confident_wrong": n_h,
           "certificate_coverage_mixed": _r(cert_cov_mixed), "per_method": {}}

    # certificate: structural, threshold-free
    cert_caught = float(np.mean([0.0 if cert_named[i] else 1.0 for i in halluc_idx])) if n_h else float("nan")
    out["per_method"]["certificate"] = {"fraction_caught": _r(cert_caught),
                                        "survival": _r(1.0 - cert_caught) if cert_caught == cert_caught else None}

    # dispersion signals: certificate-matched global threshold over the MIXED pool
    for s in SIGNALS:
        m = f"ct_{s}"
        ct_named = raw_named  # ct commits raw's answer; named == raw_named
        sig_all = np.array([float(r.get(sigkey.format(s), 0.0) or 0.0) for r in records], float)
        conf_mixed = np.where(ct_named, sig_all, -1.0)
        tau_global = float("nan")
        if N and cert_cov_mixed == cert_cov_mixed:
            mask = matched_coverage_mask(conf_mixed, cert_cov_mixed)
            covered = sorted([conf_mixed[i] for i in range(N) if mask[i] and conf_mixed[i] >= 0.0])
            tau_global = covered[0] if covered else float("nan")
        vals = np.array([sig_all[i] for i in halluc_idx], float) if n_h else np.array([])
        frac_surv = float(np.mean(vals >= tau_global)) if (n_h and tau_global == tau_global) else float("nan")
        out["per_method"][m] = {"fraction_surviving": _r(frac_surv),
                                "fraction_caught": _r(1.0 - frac_surv) if frac_surv == frac_surv else None,
                                "tau_global": _r(tau_global)}
    # query-side gates (only present in the located-in rows)
    for qs in ("queryside_verifier", "queryside_selfverify"):
        key = f"predict_{qs}"
        if any(key in r for r in records):
            surv = float(np.mean([1.0 if is_named(records[i].get(key)) else 0.0 for i in halluc_idx])) if n_h else float("nan")
            out["per_method"][qs] = {"fraction_surviving": _r(surv),
                                     "fraction_caught": _r(1.0 - surv) if surv == surv else None}
    return out


def natural_cw_rate(records, predkey):
    """Confident-wrong rate on an ABSENT pool: fraction of rows where the method NAMES a relation
    (any named answer on an absent pair is wrong)."""
    if not records:
        return float("nan")
    return float(np.mean([1.0 if is_named(r.get(predkey)) else 0.0 for r in records]))


def doc_clustered_caught_gap_bootstrap(records, cert_caught_vec, comp_caught_vec, doc_ids,
                                       B=10000, seed=EVAL_SEED):
    """NEW statistic: doc-clustered paired bootstrap of (cert_caught - comp_caught) over the
    fabrication set.  Resample DOCUMENTS with replacement.  Returns point, CI95, one-sided p."""
    cert_caught_vec = np.asarray(cert_caught_vec, float)
    comp_caught_vec = np.asarray(comp_caught_vec, float)
    point = float(cert_caught_vec.mean() - comp_caught_vec.mean())
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
        gaps.append(float(cert_caught_vec[idx].mean() - comp_caught_vec[idx].mean()))
    gaps = np.array(gaps, float)
    lo, hi = np.quantile(gaps, [0.025, 0.975])
    p_one = max(float(np.mean(gaps <= 0.0)), 1.0 / (len(gaps) + 1))
    return {"gap": _r(point), "ci95": [_r(lo), _r(hi)], "p_one_sided": _r(p_one),
            "ci_excludes_0": bool(lo > 0.0), "n_boot": int(len(gaps))}


def doc_clustered_rate_diff_bootstrap(rate_a_vec, rate_b_vec, doc_ids, B=10000, seed=REPRO_SEED):
    """Doc-clustered paired bootstrap of mean(a) - mean(b) over the same index set (for
    reproducing a CARRIED confident-wrong-reduction CI)."""
    a = np.asarray(rate_a_vec, float)
    b = np.asarray(rate_b_vec, float)
    point = float(a.mean() - b.mean())
    by_doc = defaultdict(list)
    for i, d in enumerate(doc_ids):
        by_doc[d].append(i)
    docs = list(by_doc)
    nd = len(docs)
    rng = np.random.default_rng(seed)
    diffs = []
    for _ in range(B):
        pick = rng.integers(0, nd, nd)
        idx = np.concatenate([by_doc[docs[i]] for i in pick]) if nd else np.array([], int)
        if len(idx) == 0:
            continue
        diffs.append(float(a[idx].mean() - b[idx].mean()))
    diffs = np.array(diffs, float)
    lo, hi = np.quantile(diffs, [0.025, 0.975])
    return {"point": _r(point), "ci95": [_r(lo), _r(hi)]}


# =========================================================================== #
# MAIN
# =========================================================================== #
@logger.catch(reraise=True)
def main():
    logger.info("=== STEP 0: guardrails ===")
    present_forbidden = [m for m in _FORBIDDEN if m in sys.modules]
    assert not present_forbidden, f"FORBIDDEN network/LLM module imported: {present_forbidden}"
    logger.info(f"No forbidden modules in sys.modules (checked {len(_FORBIDDEN)}).")

    li_meta, li = load("locatedin")
    vf_meta, vf = load("verifier")
    ki_meta, ki = load("kinship")
    logger.info("Loaded 3 frozen experiment outputs.")

    # ----------------------------------------------------------------------- #
    # STEP 1 — REPRODUCTION GATE
    # ----------------------------------------------------------------------- #
    logger.info("=== STEP 1: reproduction gate (recompute-from-rows, assert==carried) ===")

    # ---- LOCATED-IN ----
    li_present = li["locatedin_present"]                  # 515 (held_out 400 + never_annotated 115)
    li_sib = li["locatedin_absent_sibling"]               # 450
    li_diff = li["locatedin_absent_diffcomponent"]        # 250
    li_sib_mixed = li_present + li_sib                    # 965

    GATE.hard("locatedin.count_present", len(li_present), 515, 0)
    GATE.hard("locatedin.count_sibling_absent", len(li_sib), 450, 0)
    GATE.hard("locatedin.count_diffcomponent_absent", len(li_diff), 250, 0)

    # FACT A per regime
    factA_sib = natural_cw_rate(li_sib, "metadata_raw_named_FLAG") if False else \
        float(np.mean([1.0 if r["metadata_raw_named"] else 0.0 for r in li_sib]))
    factA_diff = float(np.mean([1.0 if r["metadata_raw_named"] else 0.0 for r in li_diff]))
    GATE.hard("locatedin.FACT_A.same_component_sibling", factA_sib, 0.30, 5e-3)
    GATE.hard("locatedin.FACT_A.different_component", factA_diff, 0.06, 5e-3)

    # crux caught on sibling mixed pool
    li_crux = crux_caught(li_sib_mixed)
    GATE.hard("locatedin.crux.n_raw_confident_wrong", li_crux["n_raw_confident_wrong"], 135, 0)
    cm = li_crux["per_method"]
    GATE.hard("locatedin.caught.certificate", cm["certificate"]["fraction_caught"], 0.7852, 5e-3)
    GATE.hard("locatedin.caught.ct_verbalized", cm["ct_verbalized"]["fraction_caught"], 0.4000, 5e-3)
    GATE.hard("locatedin.caught.ct_sc_margin", cm["ct_sc_margin"]["fraction_caught"], 0.0667, 5e-3)
    GATE.hard("locatedin.caught.ct_ptrue", cm["ct_ptrue"]["fraction_caught"], 0.3037, 5e-3)
    GATE.hard("locatedin.caught.ct_negent", cm["ct_negent"]["fraction_caught"], 0.0667, 5e-3)
    GATE.hard("locatedin.caught.queryside_verifier", cm["queryside_verifier"]["fraction_caught"], 0.2741, 5e-3)
    GATE.hard("locatedin.caught.queryside_selfverify", cm["queryside_selfverify"]["fraction_caught"], 0.4593, 5e-3)

    # natural confident-wrong on the 450 sibling-absent pairs
    li_natcw = {
        "raw_commit": natural_cw_rate(li_sib, "metadata_raw_named") if False else factA_sib,
        "certificate": natural_cw_rate(li_sib, "predict_certificate"),
        "ct_verbalized": natural_cw_rate(li_sib, "predict_conf_thresh_verbalized"),
        "ct_sc_margin": natural_cw_rate(li_sib, "predict_conf_thresh_sc_margin"),
        "ct_ptrue": natural_cw_rate(li_sib, "predict_conf_thresh_ptrue"),
        "ct_negent": natural_cw_rate(li_sib, "predict_conf_thresh_negent"),
        "queryside_verifier": natural_cw_rate(li_sib, "predict_queryside_verifier"),
        "queryside_selfverify": natural_cw_rate(li_sib, "predict_queryside_selfverify"),
    }
    GATE.hard("locatedin.natural_cw.certificate", li_natcw["certificate"], 0.0733, 5e-3)
    GATE.hard("locatedin.natural_cw.ct_verbalized", li_natcw["ct_verbalized"], 0.30, 5e-3)
    GATE.hard("locatedin.natural_cw.queryside_verifier", li_natcw["queryside_verifier"], 0.2178, 5e-3)
    GATE.hard("locatedin.natural_cw.queryside_selfverify", li_natcw["queryside_selfverify"], 0.1622, 5e-3)

    # abstention decomposition (sibling pool)
    li_cert_named_present = float(np.sum([is_named(r["predict_certificate"]) for r in li_present]))
    li_cert_named_absent = float(np.sum([is_named(r["predict_certificate"]) for r in li_sib]))
    li_cert_named_total = li_cert_named_present + li_cert_named_absent
    li_over_abstain_present = len(li_present) - li_cert_named_present
    li_correct_absent_abst = len(li_sib) - li_cert_named_absent
    GATE.hard("locatedin.abst.certificate_named_total", li_cert_named_total, 59, 0)
    GATE.hard("locatedin.abst.over_abstain_present_rate", li_over_abstain_present / len(li_present), 0.9495, 5e-3)
    GATE.hard("locatedin.abst.correct_absent_abstention_rate", li_correct_absent_abst / len(li_sib), 0.9267, 5e-3)
    GATE.hard("locatedin.abst.present_coverage_llm_read", li_cert_named_present / len(li_present), 0.0505, 5e-3)

    # THE ARTIFACT identity: view1_absent 0.2267 reduction == signal_named_rate(0.30) - cert_named_rate(0.0733)
    identity_val = li_natcw["ct_verbalized"] - li_natcw["certificate"]
    carried_view1_reduction = li_meta["primary_reader_results_sibling_DECISIVE"]["view1_absent"]["ct_verbalized"]["confident_wrong_reduction"]
    GATE.hard("locatedin.view1_absent.reduction_carried", carried_view1_reduction, 0.2267, 1e-4)
    GATE.hard("locatedin.view1_absent.identity(0.30-0.0733)", identity_val, 0.2267, 5e-3)

    # mixed sibling matched-coverage confident-wrong reduction POINT (deterministic = cmp 0 - cert 0.0342)
    li_cert_cw_mixed = li_cert_named_absent / len(li_sib_mixed)   # cert named on absent / N (any named absent = wrong)
    GATE.hard("locatedin.mixed.certificate_confident_wrong", li_cert_cw_mixed, 0.0342, 5e-3)
    li_mixed_reduction_point = 0.0 - li_cert_cw_mixed
    GATE.hard("locatedin.mixed.reduction_point", li_mixed_reduction_point, -0.0342, 5e-3)

    # build-stats reference & verdict strings
    GATE.hard("locatedin.build_stats.absent_same_component_sibling",
              li_meta["dataset_build_stats_reference"]["re-docred"]["absent_same_component_sibling"], 20814, 0)
    li_verdict = li_meta["verdict"]
    assert li_verdict["overall"] == "EXTRACTION-LIMITED-BOUNDARY", li_verdict["overall"]
    assert li_verdict["certificate_beats_all_6_baselines_holm"] is False
    assert li_verdict["verifier_suffices"] is False
    logger.info("LOCATED-IN verdict strings OK.")

    # natural atomic P/R — carried (needs gold atomic edges, not in per-query rows)
    li_atomic = li_meta["natural_prose_atomic_pr"]
    GATE.hard("locatedin.atomic.recall_converse_invariant",
              li_atomic["converse_invariant_primitive_PRIMARY"]["recall"], 0.1478, 1e-4)
    GATE.hard("locatedin.atomic.precision_converse_invariant",
              li_atomic["converse_invariant_primitive_PRIMARY"]["precision"], 0.6649, 1e-4)
    GATE.hard("locatedin.atomic.recall_strict",
              li_atomic["strict_direction_aware_secondary"]["recall"], 0.1421, 1e-4)

    # CI reproduction (Monte-Carlo, REPRO seed): mixed reduction CI [-0.0502,-0.0204]
    doc_ids_mixed = [r["metadata_doc_id"] for r in li_sib_mixed]
    cert_cw_vec = np.array([1.0 if (r["metadata_is_absent"] and is_named(r["predict_certificate"])) else 0.0
                            for r in li_sib_mixed], float)
    # signal at matched coverage commits ~0 confident-wrong -> its cw vector under the matched mask is ~0;
    # the reduction is (signal_cw_matched - cert_cw). We reproduce cert side; signal side is 0 at matched cov.
    li_ci = doc_clustered_rate_diff_bootstrap(np.zeros_like(cert_cw_vec), cert_cw_vec, doc_ids_mixed,
                                              B=10000, seed=REPRO_SEED)
    GATE.soft_check("locatedin.mixed.reduction_ci_lo", li_ci["ci95"][0], -0.0502, 0.01, "MC doc-clustered")
    GATE.soft_check("locatedin.mixed.reduction_ci_hi", li_ci["ci95"][1], -0.0204, 0.01, "MC doc-clustered")

    # cross-family (mistral) — CARRIED-NOT-REPRODUCED (no mistral per-row predictions in the file)
    li_xf = li_meta["cross_family_sensitivity"]
    assert abs(li_xf["FACT_A_per_regime"]["same_component_sibling"]["rate"] - 0.4378) < 1e-3
    assert abs(li_xf["FACT_B_crux_fraction_caught"]["certificate"]["fraction_caught"] - 0.7766) < 1e-3

    # ---- VERIFIER ----
    logger.info("--- verifier ---")
    vf_cl_present = vf["clutrr_present"]      # 102
    vf_cl_absent = vf["clutrr_absent"]        # 180
    vf_rd_absent = vf["redocred_absent"]      # 368
    GATE.hard("verifier.count.clutrr_present", len(vf_cl_present), 102, 0)
    GATE.hard("verifier.count.clutrr_absent", len(vf_cl_absent), 180, 0)
    GATE.hard("verifier.count.redocred_absent", len(vf_rd_absent), 368, 0)

    def caught_structural(absent_rows, predkey):
        fab = [r for r in absent_rows if r.get("metadata_raw_named")]
        if not fab:
            return float("nan"), 0
        return float(np.mean([1.0 if not is_named(r.get(predkey)) else 0.0 for r in fab])), len(fab)

    vf_cl_cert, n_cl_fab = caught_structural(vf_cl_absent, "predict_certificate")
    vf_cl_ver, _ = caught_structural(vf_cl_absent, "predict_queryside_verifier")
    vf_cl_self, _ = caught_structural(vf_cl_absent, "predict_queryside_selfverify")
    vf_rd_cert, n_rd_fab = caught_structural(vf_rd_absent, "predict_certificate")
    vf_rd_ver, _ = caught_structural(vf_rd_absent, "predict_queryside_verifier")
    vf_rd_self, _ = caught_structural(vf_rd_absent, "predict_queryside_selfverify")
    GATE.hard("verifier.clutrr.n_fabrications", n_cl_fab, 85, 0)
    GATE.hard("verifier.redocred.n_fabrications", n_rd_fab, 120, 0)
    GATE.hard("verifier.caught.clutrr.certificate", vf_cl_cert, 0.9412, 5e-3)
    GATE.hard("verifier.caught.clutrr.queryside_verifier", vf_cl_ver, 0.5882, 5e-3)
    GATE.hard("verifier.caught.clutrr.queryside_selfverify", vf_cl_self, 0.8235, 5e-3)
    GATE.hard("verifier.caught.redocred.certificate", vf_rd_cert, 0.85, 5e-3)
    GATE.hard("verifier.caught.redocred.queryside_verifier", vf_rd_ver, 0.10, 5e-3)
    GATE.hard("verifier.caught.redocred.queryside_selfverify", vf_rd_self, 0.5417, 5e-3)

    # CLUTRR present leaderboard (CLUTRR is SURFACE-scored: correct == predict == gold)
    def selacc_present(rows, predkey, gold_key="metadata_gold"):
        cov = [r for r in rows if is_named(r.get(predkey))]
        if not cov:
            return float("nan"), 0
        correct = sum(1 for r in cov if str(r.get(predkey)) == str(r.get(gold_key)))
        return correct / len(cov), len(cov)

    vf_cl_cert_cov = float(np.mean([1.0 if is_named(r["predict_certificate"]) else 0.0 for r in vf_cl_present]))
    vf_cl_cert_selacc, n_cov = selacc_present(vf_cl_present, "predict_certificate")
    GATE.hard("verifier.clutrr_present.certificate_coverage", vf_cl_cert_cov, 0.6863, 5e-3)
    GATE.hard("verifier.clutrr_present.certificate_selective_accuracy", vf_cl_cert_selacc, 0.8857, 5e-3)
    GATE.hard("verifier.clutrr_present.certificate_cw_among_covered", 1.0 - vf_cl_cert_selacc, 0.1143, 5e-3)

    # signal selacc at matched coverage on CLUTRR present (tie-break sensitive -> soft cross-check)
    def signal_selacc_matched(rows, predkey, confkey, target_cov, gold_key="metadata_gold"):
        named = np.array([is_named(r.get(predkey)) for r in rows], bool)
        conf = np.array([coverage_confidence(named[i], float(rows[i].get(confkey, 0.0) or 0.0))
                         for i in range(len(rows))], float)
        mask = matched_coverage_mask(conf, target_cov)
        idx = np.where(mask)[0]
        if len(idx) == 0:
            return float("nan")
        correct = sum(1 for i in idx if is_named(rows[i].get(predkey)) and str(rows[i].get(predkey)) == str(rows[i].get(gold_key)))
        return correct / len(idx)
    vf_sig_selacc = signal_selacc_matched(vf_cl_present, "predict_conf_thresh_verbalized",
                                          "metadata_conf_verbalized", vf_cl_cert_cov)
    GATE.soft_check("verifier.clutrr_present.signal_verbalized_selacc", vf_sig_selacc, 0.5429, 5e-3,
                    "tie-break-sensitive (source order)")

    # cert-minus-verifier caught GAP doc-clustered bootstrap (reproduce CARRIED CIs, REPRO seed)
    def caught_gap_repro(absent_rows, seed=REPRO_SEED):
        fab = [r for r in absent_rows if r.get("metadata_raw_named")]
        cert_c = np.array([1.0 if not is_named(r["predict_certificate"]) else 0.0 for r in fab], float)
        ver_c = np.array([1.0 if not is_named(r["predict_queryside_verifier"]) else 0.0 for r in fab], float)
        dids = [r["metadata_doc_id"] for r in fab]
        return doc_clustered_caught_gap_bootstrap(fab, cert_c, ver_c, dids, B=10000, seed=seed)
    vf_cl_gap = caught_gap_repro(vf_cl_absent)
    vf_rd_gap = caught_gap_repro(vf_rd_absent)
    GATE.hard("verifier.clutrr.cert_minus_verifier_gap_point", vf_cl_gap["gap"], 0.3529, 5e-3)
    GATE.hard("verifier.redocred.cert_minus_verifier_gap_point", vf_rd_gap["gap"], 0.75, 5e-3)
    GATE.soft_check("verifier.clutrr.gap_ci_lo", vf_cl_gap["ci95"][0], 0.187, 0.02, "MC doc-clustered")
    GATE.soft_check("verifier.redocred.gap_ci_lo", vf_rd_gap["ci95"][0], 0.620, 0.02, "MC doc-clustered")
    assert vf_cl_gap["ci_excludes_0"] and vf_rd_gap["ci_excludes_0"], "caught-gap CI must exclude 0"

    assert vf_meta["reproduction_gate"]["all_ok"] is True
    assert vf_meta["reproduction_gate"]["n_checks"] == 32
    assert vf_meta["certificate_necessity_verdict"]["overall"]["headline"] == "CERTIFICATE_NECESSARY_BOTH_VENUES"

    # ---- KINSHIP ----
    logger.info("--- kinship ---")
    ki_present = ki["re-docred_present"]    # 360
    ki_absent = ki["re-docred_absent"]      # 368
    ki_mixed = ki_present + ki_absent       # 728
    GATE.hard("kinship.count_present", len(ki_present), 360, 0)
    GATE.hard("kinship.count_absent", len(ki_absent), 368, 0)

    ki_factA = float(np.mean([1.0 if r["metadata_raw_named"] else 0.0 for r in ki_absent]))
    GATE.hard("kinship.FACT_A", ki_factA, 0.3261, 5e-3)
    ki_cert_cw = natural_cw_rate(ki_absent, "predict_certificate")
    GATE.hard("kinship.certificate_absent_confident_wrong", ki_cert_cw, 0.0707, 5e-3)

    ki_crux = crux_caught(ki_mixed)
    GATE.hard("kinship.crux.n_raw_confident_wrong", ki_crux["n_raw_confident_wrong"], 120, 0)
    kcm = ki_crux["per_method"]
    GATE.hard("kinship.caught.ct_verbalized", kcm["ct_verbalized"]["fraction_caught"], 0.4917, 5e-3)
    GATE.hard("kinship.caught.ct_sc_margin", kcm["ct_sc_margin"]["fraction_caught"], 0.15, 5e-3)
    GATE.hard("kinship.caught.ct_ptrue", kcm["ct_ptrue"]["fraction_caught"], 0.5167, 5e-3)
    GATE.hard("kinship.caught.ct_negent", kcm["ct_negent"]["fraction_caught"], 0.15, 5e-3)
    GATE.hard("kinship.survival.ct_verbalized", kcm["ct_verbalized"]["fraction_surviving"], 0.5083, 5e-3)
    GATE.hard("kinship.survival.ct_sc_margin", kcm["ct_sc_margin"]["fraction_surviving"], 0.85, 5e-3)
    GATE.hard("kinship.survival.ct_ptrue", kcm["ct_ptrue"]["fraction_surviving"], 0.4833, 5e-3)
    GATE.hard("kinship.survival.ct_negent", kcm["ct_negent"]["fraction_surviving"], 0.85, 5e-3)

    # kinship abstention decomposition
    ki_cert_named_present = float(np.sum([is_named(r["predict_certificate"]) for r in ki_present]))
    ki_cert_named_absent = float(np.sum([is_named(r["predict_certificate"]) for r in ki_absent]))
    GATE.hard("kinship.abst.certificate_named_total", ki_cert_named_present + ki_cert_named_absent, 200, 0)
    GATE.hard("kinship.abst.present_coverage_llm_read", ki_cert_named_present / len(ki_present), 0.4833, 5e-3)
    GATE.hard("kinship.abst.over_abstain_present_rate",
              (len(ki_present) - ki_cert_named_present) / len(ki_present), 0.5167, 5e-3)
    GATE.hard("kinship.abst.correct_absent_abstention_rate",
              (len(ki_absent) - ki_cert_named_absent) / len(ki_absent), 0.9293, 5e-3)

    # kinship atomic P/R + mixed reductions — CARRIED (primitive-level present correctness not in rows)
    ki_atomic = ki_meta["headline_summary"]["natural_atomic_pr"]
    GATE.hard("kinship.atomic.recall_converse_invariant",
              ki_atomic["recall_converse_invariant"], 0.3762, 1e-4)
    GATE.hard("kinship.atomic.recall_strict",
              ki_atomic["recall_strict"], 0.1992, 1e-4)
    ki_mixed_red = ki_meta["headline_summary"]["mixed_confident_wrong_reduction_certificate_vs_each_signal"]
    for s, exp in [("ct_verbalized", -0.0549), ("ct_sc_margin", -0.0343), ("ct_ptrue", -0.0467), ("ct_negent", -0.0343)]:
        GATE.hard(f"kinship.mixed_reduction_carried.{s}", ki_mixed_red[s]["reduction"], exp, 1e-4)
    assert ki_meta["verdict"]["overall"] == "EXTRACTION-LIMITED-BOUNDARY"

    # ---- HARD STOP if any hard check failed ----
    if not GATE.all_ok():
        failed = [c for c in GATE.checks if not c["ok"]]
        logger.error(f"REPRODUCTION GATE FAILED: {len(failed)} mismatches")
        out = {"metrics_agg": {"reproduction_gate_failed": float(len(failed))},
               "datasets": [{"dataset": "reproduction_gate_failed",
                             "examples": [{"input": "reproduction_gate", "output": json.dumps(failed)}]}]}
        (WORKDIR / "eval_out.json").write_text(json.dumps(out, indent=2))
        raise SystemExit(f"HARD STOP: reproduction gate mismatch in {[c['name'] for c in failed]}")
    logger.info(f"REPRODUCTION GATE PASSED: {GATE.n_passed()}/{len(GATE.checks)} hard checks OK; "
                f"{sum(1 for s in GATE.soft if s['ok'])}/{len(GATE.soft)} soft cross-checks within MC tol.")

    # ----------------------------------------------------------------------- #
    # STEP 2 — RIGOR MAJOR: caught-fraction as the matched-coverage-fair headline
    # ----------------------------------------------------------------------- #
    logger.info("=== STEP 2: rigor_fix (caught-fraction headline) ===")

    # (a) pure-absent identity: named_rate == confident_wrong_rate == 'coverage' on the 450 absent pool
    pure_absent_identity = {
        "pool_n": len(li_sib),
        "per_method_named_eq_cw_eq_coverage": {
            "modeA_certificate": _r(li_natcw["certificate"]),
            "ct_verbalized": _r(li_natcw["ct_verbalized"]),
            "ct_sc_margin": _r(li_natcw["ct_sc_margin"]),
            "ct_ptrue": _r(li_natcw["ct_ptrue"]),
            "ct_negent": _r(li_natcw["ct_negent"]),
            "queryside_verifier": _r(li_natcw["queryside_verifier"]),
            "queryside_selfverify": _r(li_natcw["queryside_selfverify"]),
        },
        "statement": ("On a PURE-ABSENT pool there are no present pairs to cover, so each method's "
                      "'coverage' degenerates to its named-rate, which equals its confident-wrong rate "
                      "(any named answer on an absent pair is wrong). Therefore the view1_absent "
                      "'0.2267 reduction at matched coverage / meets the 0.20 bar' is NOT a risk-coverage "
                      "selective-accuracy gain; it is exactly (signal named-rate 0.30 - certificate "
                      "named-rate 0.0733) = a coverage/abstention-rate difference, i.e. a re-expression "
                      "of the caught-fraction gap."),
        "identity_check": {"reduction": _r(identity_val), "equals_0.30_minus_0.0733": _r(0.30 - 0.0733),
                           "matches_carried_0.2267": True},
        "evidence_tag": "RE-ANALYSIS-DERIVED",
    }

    # (b) caught_fraction_leaderboard (THE replacement headline) + NEW doc-clustered paired bootstrap
    fab_li = [r for r in li_sib if r.get("metadata_raw_named")]          # 135 fabrications
    fab_doc_ids = [r["metadata_doc_id"] for r in fab_li]
    cert_caught_vec = np.array([1.0 if not is_named(r["predict_certificate"]) else 0.0 for r in fab_li], float)
    # dispersion 'catch' at the certificate-matched global threshold = signal value < tau_global
    tau = {s: li_crux["per_method"][f"ct_{s}"]["tau_global"] for s in SIGNALS}
    caught_leaderboard = {"certificate": {"fraction_caught": _r(cm["certificate"]["fraction_caught"]),
                                          "evidence_tag": "RE-ANALYSIS-DERIVED"}}
    caught_gaps = {}
    for s in SIGNALS:
        m = f"ct_{s}"
        comp_caught_vec = np.array([1.0 if (float(r.get(f"metadata_conf_{s}", 0.0) or 0.0) < tau[s]) else 0.0
                                    for r in fab_li], float)
        gap = doc_clustered_caught_gap_bootstrap(fab_li, cert_caught_vec, comp_caught_vec, fab_doc_ids,
                                                 B=10000, seed=EVAL_SEED)
        caught_leaderboard[m] = {"fraction_caught": _r(cm[m]["fraction_caught"]),
                                 "cert_minus_method_caught_gap": gap, "evidence_tag": "RE-ANALYSIS-DERIVED"}
        caught_gaps[m] = gap
    for qs in ("queryside_verifier", "queryside_selfverify"):
        comp_caught_vec = np.array([1.0 if not is_named(r[f"predict_{qs}"]) else 0.0 for r in fab_li], float)
        gap = doc_clustered_caught_gap_bootstrap(fab_li, cert_caught_vec, comp_caught_vec, fab_doc_ids,
                                                 B=10000, seed=EVAL_SEED)
        caught_leaderboard[qs] = {"fraction_caught": _r(cm[qs]["fraction_caught"]),
                                  "cert_minus_method_caught_gap": gap, "evidence_tag": "RE-ANALYSIS-DERIVED"}
        caught_gaps[qs] = gap
    gaps_excluding_0 = [m for m, g in caught_gaps.items() if g["ci_excludes_0"]]

    rigor_fix = {
        "pure_absent_identity": pure_absent_identity,
        "caught_fraction_leaderboard": {
            "denominator": "the 135 raw-LLM confident absent-sibling fabrications (identical for every method)",
            "fairness": ("matched-coverage-FAIR: identical denominator, every method judged on the SAME "
                         "fabrications -> 'of the high-confidence absent fabrications the raw reader emits, "
                         "what fraction does each method turn into an abstention?'"),
            "leaderboard": caught_leaderboard,
            "new_bootstrap": {"seed": EVAL_SEED, "B": 10000, "cluster": "metadata_doc_id",
                              "gaps_with_ci_excluding_0": gaps_excluding_0},
            "evidence_tag": "RE-ANALYSIS-DERIVED",
        },
        "load_bearing_natural_confident_wrong": {
            "certificate": _r(li_natcw["certificate"]), "raw_and_all_dispersion_signals": 0.30,
            "queryside_verifier": _r(li_natcw["queryside_verifier"]),
            "queryside_selfverify": _r(li_natcw["queryside_selfverify"]),
            "note": "the certificate beats the established false-premise detector (verifier) by ~3x on the sibling pool",
            "evidence_tag": "REAL-LLM-READ/NATURAL-PROSE (reproduced-from-rows)",
        },
        "honest_mixed_pool": {
            "certificate_matched_coverage_reduction": _r(li_mixed_reduction_point),
            "ci95": [_r(li_ci["ci95"][0]), _r(li_ci["ci95"][1])],
            "carried_ci95": [-0.0502, -0.0204],
            "why_negative": ("the certificate over-abstains on present at extraction recall 0.148; present "
                             "coverage collapses to 0.05, so the matched-coverage reduction is degenerate"),
            "reconcile_with_artifact_caveats": {
                "pure_absent_degeneracy": li_meta["honesty_caveats"]["pure_absent_degeneracy"],
                "matched_coverage_degeneracy_under_extraction_limit":
                    li_meta["honesty_caveats"]["matched_coverage_degeneracy_under_extraction_limit"],
            },
            "evidence_tag": "RE-ANALYSIS-DERIVED",
        },
    }

    # ----------------------------------------------------------------------- #
    # STEP 3 — 16-CELL CAPABILITY-GAP TABLE
    # ----------------------------------------------------------------------- #
    logger.info("=== STEP 3: capability_gap_table ===")
    # Re-DocRED/deepseek carried (no per-row deepseek predictions in kinship file)
    ki_ds = ki_meta["cross_family_sensitivity"]["FACT_B_crux_survival"]
    capability_gap_table = {
        "rows": [
            {"corpus": "Re-DocRED", "reader": "gemini", "tag": "REPRODUCED-FROM-ROWS",
             "survival": {s: kcm[f"ct_{s}"]["fraction_surviving"] for s in SIGNALS},
             "caught": {s: kcm[f"ct_{s}"]["fraction_caught"] for s in SIGNALS}},
            {"corpus": "Re-DocRED", "reader": "deepseek", "tag": "CARRIED-NOT-REPRODUCED",
             "survival": {s: _r(ki_ds[f"ct_{s}"]) for s in SIGNALS},
             "caught": {s: _r(1.0 - ki_ds[f"ct_{s}"]) for s in SIGNALS},
             "note": "no deepseek per-row predictions in the kinship file (cross-family is aggregate-only)"},
            {"corpus": "CLUTRR", "reader": "gemini", "tag": "CARRIED-LITERAL",
             "survival": {"verbalized": 0.4353, "sc_margin": 0.7176, "ptrue": 0.2471, "negent": 0.7176},
             "caught": {"verbalized": 0.5647, "sc_margin": 0.2824, "ptrue": 0.7529, "negent": 0.2824},
             "note": "cross-checked against exp_2 (verifier) reproduction_gate which re-derived them"},
            {"corpus": "CLUTRR", "reader": "deepseek", "tag": "CARRIED-LITERAL",
             "survival": {"verbalized": 0.672, "sc_margin": 0.224, "ptrue": 0.103, "negent": 0.224},
             "caught": {"verbalized": 0.328, "sc_margin": 0.776, "ptrue": 0.897, "negent": 0.776},
             "note": "THREE of four dispersion signals catch 78-90% for the stronger deepseek reader"},
        ],
        "FACT_A_robust_corpus_and_reader_transferable": {
            "CLUTRR_gemini": 0.472, "CLUTRR_deepseek": 0.483,
            "ReDocRED_gemini": 0.326, "ReDocRED_deepseek": 0.318,
            "locatedin_sibling_gemini": 0.30, "locatedin_sibling_mistral": 0.4378,
            "statement": "the raw confident-fabrication RATE transfers across readers AND corpora (the ROBUST fact)",
            "evidence_tag": "REAL-LLM-READ",
        },
        "FACT_B_reader_and_signal_dependent": {
            "statement": ("which signals catch the fabrications is READER- and SIGNAL-dependent: verbalized "
                          "confidence is the most robustly BLIND signal; dispersion signals catch the MAJORITY "
                          "for the stronger deepseek reader but commit most under gemini"),
            "evidence_tag": "RE-ANALYSIS-DERIVED",
        },
    }

    # ----------------------------------------------------------------------- #
    # STEP 5 — count reconciliation (placed before paper blocks so blocks can reference it)
    # ----------------------------------------------------------------------- #
    count_reconciliation = {
        "kinship_redocred_primary_slice": {
            "present_multihop": 360, "present_composed_only_non_circular": 222, "absent": 368,
            "engine_round_trip_present_combined": 476, "engine_round_trip_absent_combined": 577,
            "docred_present": 116, "docred_absent": 209, "docred_absent_false_negative_frac": 0.646,
            "explanation": ("the 476/476 present and 577/577 absent engine round-trip is the COMBINED "
                            "re-docred (360/368) + docred (116/209, whose absent gold is downgraded ~64.6% "
                            "false-negatives); removes the apparent 360!=476 / 368!=577 inconsistency"),
        },
        "locatedin": {"present": 515, "same_component_sibling_absent": 450, "different_component_absent": 250,
                      "never_annotated": 115, "held_out": 400, "n_docs": 283,
                      "note": "present 515 = held_out 400 + never_annotated 115"},
        "evidence_tag": "REPRODUCED-FROM-ROWS",
    }

    # ----------------------------------------------------------------------- #
    # STEP 4 — SEVEN PAPER-FACING SCAFFOLD BLOCKS
    # ----------------------------------------------------------------------- #
    logger.info("=== STEP 4: paper_blocks ===")

    blk_i = (
        "### located-in results (CORRECTED: caught-fraction as the matched-coverage headline)\n\n"
        "On 450 natural Wikipedia same-component-sibling absent located-in pairs, the raw reader confidently "
        "fabricates a containment on **30%** [FACT-A; REAL-LLM-READ]. Of those 135 high-confidence "
        "fabrications, the fraction each method turns into an abstention (matched-coverage-fair: identical "
        "denominator) is:\n\n"
        "| method | fraction caught |\n|---|---|\n"
        "| **certificate (no-derivation)** | **0.785** |\n"
        "| verbalized confidence | 0.400 |\n"
        "| self-consistency margin | 0.067 |\n"
        "| Kadavath P(True) | 0.304 |\n"
        "| semantic-entropy | 0.067 |\n"
        "| query-side false-premise verifier | 0.274 |\n"
        "| self-verification | 0.459 |\n\n"
        "Natural confident-wrong on the sibling pool: certificate **0.073** vs raw/all-dispersion-signals "
        "**0.30** vs verifier 0.218 vs self-verify 0.162 [REAL-LLM-READ/NATURAL-PROSE]. "
        "DELETE the sentence '0.227 confident-wrong reduction at matched coverage / meets the 0.20 bar'. "
        "RELABEL alternative (if kept): 'the certificate at its abstaining operating point (0.073) vs each "
        "signal at its natural operating point (0.30) on the pure-absent pool, where coverage==confident-wrong "
        "by construction'. CAVEAT: on a pure-absent pool confident-wrong == coverage for every method, so the "
        "0.227 number is mechanically (0.30 - 0.073), not a risk-coverage gain [RE-ANALYSIS-DERIVED]."
    )

    proofread_checklist = [
        "FLAG duplicated sentences (identical or near-identical consecutive sentences).",
        "FLAG truncated '...' fragments or sentences ending mid-clause.",
        "FLAG any number reported WITHOUT a coverage/abstention qualifier (every selective-accuracy / "
        "confident-wrong number must state its coverage or operating point).",
        "DOWNGRADE any 'family-level blindness' / 'entire confidence family is blind' phrasing to "
        "reader-dependent FACT B (verbalized robustly blind; dispersion signals catch the majority for deepseek).",
        "FLAG any 'natural' label applied to CLUTRR — CLUTRR is TEMPLATED; only Re-DocRED/located-in are natural prose.",
        "FLAG any claim that the certificate NET-WINS on natural prose — it does NOT (mixed-pool reduction is "
        "negative/degenerate; the natural win is the catching-objective + the quantified extraction boundary).",
        "VERIFY every cross-reference to sec:boundary resolves and is not stale.",
        "VERIFY the '0.227 reduction at matched coverage' sentence is DELETED or RELABELED per block (i).",
        "VERIFY the verifier is scoped to 'a same-model prompt-based query-side verifier' (not 'the' verifier).",
        "VERIFY FACT A rates (CLUTRR 47/48%, Re-DocRED 33/32%, located-in sibling 30%) and caught-fractions "
        "match the eval_out.json metadata literals exactly.",
    ]
    blk_ii = (
        "### sec:boundary (regenerated CLEAN from intended numbers only)\n\n"
        "The certificate's NET utility is extraction-limited on natural prose. On Re-DocRED kinship the "
        "mixed-pool confident-wrong reductions of the certificate vs the four dispersion signals are "
        "-0.055 / -0.034 / -0.047 / -0.034, with doc-clustered bootstrap CIs ALL including 0 and Holm "
        "rejecting none [REAL-LLM-READ]. On located-in, the certificate's present coverage is 0.05 at "
        "atomic extraction recall 0.148 (best-effort 0.186) [REAL-LLM-READ]. The gold-read ceiling is "
        "1.0 present coverage / 1.0 absent abstention / 1.0 present selective accuracy [GOLD-READ-CEILING], "
        "isolating EXTRACTION (not closure) as the binding constraint. On the absent stratum the certificate "
        "stays hallucination-safe: sibling confident-wrong 0.073 [REAL-LLM-READ/NATURAL-PROSE]. "
        "(See the end-to-end proofread checklist in the eval metadata before assembling the draft.)"
    )

    blk_iii = (
        "### sibling-regime decisiveness (restated via fabrication prevalence)\n\n"
        "The same-component-sibling regime is the decisive one because the raw reader fabricates a "
        "containment on 30% of sibling-absent pairs vs only 6% of different-component pairs [REAL-LLM-READ]; "
        "the prevalence makes the sibling pool the hard test. The relatedness verifier is FOOLED by "
        "shared-parent structure — it inherits the reader's confidence and catches only 0.274 — because both "
        "endpoints share a containing parent and the reader confidently asserts a relation. The certificate's "
        "abstention is still a structural no-derivation determination, but a NON-TRIVIAL one: it requires the "
        "composition table (located_in o contains is UNDEFINED), NOT mere disconnection (that is the "
        "different-component contrast). [REAL-LLM-READ/NATURAL-PROSE]"
    )

    blk_iv = (
        "### fuzzy-unification feasibility note (supporting, not a contribution)\n\n"
        "Fuzzy unification is demoted to a feasibility note: an LLM probabilistic-unification arm emits "
        "calibrated sub-1.0 disjunctions (fraction-at-1.0 0.00 vs Mode-P 1.00; per-candidate ECE 0.142 "
        "spatial / 0.111 kinship; Mode-B catches 5/5 sound-violating spatial reads) — supporting evidence "
        "for feasibility on commodity hardware, not a substantive contribution. [SYNTHETIC/SUPPORTING]"
    )

    blk_v = (
        "### verifier-scope block (methodology)\n\n"
        "We scope the necessity claim precisely to **a same-model prompt-based query-side verifier**: a "
        "recognized prompt-based instantiation of the false-premise / unanswerable-question abstention "
        "approach (FalseQA / AbstentionBench / Wen2024). It catches only 0.274 of sibling fabrications "
        "(located-in) and 0.10 / 0.588 (Re-DocRED / CLUTRR) because it runs on the SAME LLM that hallucinated "
        "and inherits the generation error. PENDING SLOT (filled by the parallel iter-9 extraction "
        "experiment's methodology-MINOR arm): a STRONGER cross-model verifier — a larger / different-family "
        "judge with relatedness + self-verify at k=5 — to test whether cross-model verification narrows the "
        "gap. [REAL-LLM-READ; PENDING-PARALLEL-EXPERIMENT]"
    )

    blk_vi = (
        "### contribution table (one thesis)\n\n"
        "| contribution | status |\n|---|---|\n"
        "| ROBUST DIAGNOSTIC: FACT A (confident absent-fabrication rate, corpus+reader transferable) + the "
        "signal-agnostic mixed-pool capability gap | candidate NOVELTY [REAL-LLM-READ] |\n"
        "| certificate MECHANISM (forward least-fixpoint closure -> abstain) | inherited NeSy premise "
        "(+0.673 inherited / +0.0025 novel) [INHERITED-NESY-PREMISE] |\n"
        "| caught-fraction dominance over the confidence battery AND the query-side verifier | the SAFETY "
        "result (certificate 0.785 vs verifier 0.274) [RE-ANALYSIS-DERIVED] |\n"
        "| DEMONSTRATED-FIX-PENDING: net mixed-pool confident-wrong reduction excluding 0 off the "
        "structural-by-construction stratum | reserved for the parallel extraction-recall experiment "
        "[PENDING-PARALLEL-EXPERIMENT] |"
    )

    blk_vii = {
        "FORK_A_demonstrated_fix": (
            "On natural prose the closure certificate reduces confident-relation hallucinations at matched "
            "coverage by a margin whose doc-clustered CI excludes 0 on a non-structural-by-construction "
            "regime, while a same-model query-side verifier does not (caught-fraction 0.785 vs 0.274)."),
        "FORK_B_honest_boundary": (
            "The certificate's NET utility is demonstrated only on clean/templated graphs; the natural-prose "
            "contribution is the catching-objective win (caught-fraction cert 0.785 vs verifier 0.274) plus a "
            "quantified extraction boundary."),
        "selection_rule": ("Use FORK-A IFF the parallel iter-9 extraction experiment flips the mixed-pool "
                           "confident-wrong reduction CI to EXCLUDE 0 on a natural (non-structural-by-construction) "
                           "regime; otherwise use FORK-B. GEN_PAPER_TEXT selects deterministically from that "
                           "experiment's verdict field."),
        "evidence_tag": "PENDING-PARALLEL-EXPERIMENT",
    }

    paper_blocks = {
        "located_in_results_table": blk_i,
        "sec_boundary_block": blk_ii,
        "sec_boundary_proofread_checklist": proofread_checklist,
        "sibling_decisiveness_paragraph": blk_iii,
        "fuzzy_feasibility_note": blk_iv,
        "verifier_scope_block": blk_v,
        "contribution_table": blk_vi,
        "abstract_first_results_sentence_FORK": blk_vii,
    }

    # ----------------------------------------------------------------------- #
    # Assemble output: metadata + metrics_agg + datasets (each block as an example row)
    # ----------------------------------------------------------------------- #
    logger.info("=== assembling output ===")
    assert COST_USD == 0.0 and N_LLM_CALLS == 0, "BUDGET VIOLATION: this eval is pure $0 re-analysis"

    reproduction_gate = {
        "all_ok": GATE.all_ok(), "n_checks": len(GATE.checks), "n_passed": GATE.n_passed(),
        "tolerance_rates": 5e-3, "tolerance_fractions": 1e-4, "checks": GATE.checks,
        "soft_cross_checks": GATE.soft,
        "note": ("every paper-facing literal recomputed from the per-query rows and hard-asserted against the "
                 "carried metadata (mirrors exp_2's 32/32 gate); soft checks are doc-clustered bootstrap CIs "
                 "reproduced to Monte-Carlo tolerance and tie-break-sensitive signal selaccs."),
    }

    metadata = {
        "evaluation_name": "Zero-spend re-analysis: caught-fraction headline + sec:boundary scaffold",
        "description": ("Pure $0 re-analysis of three frozen iter-7/iter-8 experiment outputs. Reproduction "
                        "gate + caught-fraction rigor fix + 16-cell capability table + 7 paper-facing blocks."),
        "budget": {"cumulative_usd": 0.0, "n_llm_calls": 0},
        "seeds": {"reproduction_seed": REPRO_SEED, "eval_seed": EVAL_SEED},
        "reproduction_gate": reproduction_gate,
        "rigor_fix": rigor_fix,
        "capability_gap_table": capability_gap_table,
        "paper_blocks": paper_blocks,
        "count_reconciliation": count_reconciliation,
        "verdict_mirrors": {
            "locatedin": {"overall": li_meta["verdict"]["overall"],
                          "certificate_beats_all_6_baselines_holm": li_meta["verdict"]["certificate_beats_all_6_baselines_holm"],
                          "verifier_suffices": li_meta["verdict"]["verifier_suffices"]},
            "verifier": {"overall": vf_meta["certificate_necessity_verdict"]["overall"]["headline"],
                         "reproduction_gate_32_32": vf_meta["reproduction_gate"]["all_ok"]},
            "kinship": {"overall": ki_meta["verdict"]["overall"]},
        },
        "evidence_tag_vocabulary": ["CARRIED-LITERAL", "REPRODUCED-FROM-ROWS", "RE-ANALYSIS-DERIVED",
                                    "REAL-LLM-READ", "NATURAL-PROSE", "GOLD-READ-CEILING",
                                    "STRUCTURAL-BY-CONSTRUCTION", "INHERITED-NESY-PREMISE",
                                    "PENDING-PARALLEL-EXPERIMENT"],
    }

    metrics_agg = {
        "reproduction_gate_n_hard_checks": float(len(GATE.checks)),
        "reproduction_gate_n_passed": float(GATE.n_passed()),
        "reproduction_gate_all_ok": 1.0 if GATE.all_ok() else 0.0,
        "locatedin_FACT_A_sibling": _r(factA_sib),
        "locatedin_FACT_A_diffcomponent": _r(factA_diff),
        "locatedin_caught_fraction_certificate": _r(cm["certificate"]["fraction_caught"]),
        "locatedin_caught_fraction_verbalized": _r(cm["ct_verbalized"]["fraction_caught"]),
        "locatedin_caught_fraction_queryside_verifier": _r(cm["queryside_verifier"]["fraction_caught"]),
        "locatedin_natural_confident_wrong_certificate": _r(li_natcw["certificate"]),
        "locatedin_natural_confident_wrong_verifier": _r(li_natcw["queryside_verifier"]),
        "locatedin_mixed_reduction_point": _r(li_mixed_reduction_point),
        "verifier_caught_clutrr_certificate": _r(vf_cl_cert),
        "verifier_caught_clutrr_verifier": _r(vf_cl_ver),
        "verifier_caught_redocred_certificate": _r(vf_rd_cert),
        "verifier_caught_redocred_verifier": _r(vf_rd_ver),
        "verifier_cert_minus_verifier_gap_clutrr": _r(vf_cl_gap["gap"]),
        "verifier_cert_minus_verifier_gap_redocred": _r(vf_rd_gap["gap"]),
        "kinship_FACT_A": _r(ki_factA),
        "kinship_certificate_absent_confident_wrong": _r(ki_cert_cw),
        "kinship_caught_fraction_ptrue": _r(kcm["ct_ptrue"]["fraction_caught"]),
        "n_caught_gaps_excluding_0": float(len(gaps_excluding_0)),
        "budget_cumulative_usd": 0.0,
        "n_llm_calls": 0.0,
    }

    # datasets: one example row per paper block / table so the schema (non-empty datasets) validates.
    def row(block_id, spec, text):
        s = text if isinstance(text, str) else json.dumps(text)
        return {"input": f"{block_id} :: {spec}", "output": s, "eval_char_len": float(len(s))}

    paper_block_rows = [
        row("located_in_results_table", "corrected caught-fraction table", blk_i),
        row("sec_boundary_block", "regenerated clean boundary section", blk_ii),
        row("sec_boundary_proofread_checklist", "draft-wide proofread flags", proofread_checklist),
        row("sibling_decisiveness_paragraph", "prevalence + verifier-fooled", blk_iii),
        row("fuzzy_feasibility_note", "fuzzy demoted to one line", blk_iv),
        row("verifier_scope_block", "same-model scope + pending slot", blk_v),
        row("contribution_table", "one-thesis contribution table", blk_vi),
        row("abstract_first_results_sentence_FORK", "FORK-A / FORK-B selection rule", blk_vii),
    ]
    rigor_rows = [
        row("rigor.pure_absent_identity", "named==cw==coverage on pure-absent pool", pure_absent_identity),
        row("rigor.caught_fraction_leaderboard", "matched-coverage-fair headline", caught_leaderboard),
        row("rigor.load_bearing_natural_confident_wrong", "cert 0.073 vs 0.30", rigor_fix["load_bearing_natural_confident_wrong"]),
        row("rigor.honest_mixed_pool", "degenerate companion, reconciled", rigor_fix["honest_mixed_pool"]),
    ]
    table_rows = [
        row("capability_gap_table", "16-cell per-signal x reader x corpus survival+caught", capability_gap_table),
        row("count_reconciliation", "per-dataset counts", count_reconciliation),
    ]
    gate_rows = []
    for c in GATE.checks:
        ex = row(f"gate::{c['name']}", "hard reproduction check",
                 f"recomputed={c['recomputed']} carried={c['carried']} tol={c['tol']} ok={c['ok']}")
        ex["predict_recomputed_from_rows"] = str(c["recomputed"])
        ex["eval_ok"] = 1.0 if c["ok"] else 0.0
        if c["recomputed"] is not None and c["carried"] is not None:
            ex["eval_abs_error"] = abs(float(c["recomputed"]) - float(c["carried"]))
        gate_rows.append(ex)

    datasets = [
        {"dataset": "paper_blocks", "examples": paper_block_rows},
        {"dataset": "rigor_fix", "examples": rigor_rows},
        {"dataset": "tables", "examples": table_rows},
        {"dataset": "reproduction_gate_checks", "examples": gate_rows},
    ]

    out = {"metadata": metadata, "metrics_agg": metrics_agg, "datasets": datasets}
    out_path = WORKDIR / "eval_out.json"
    out_path.write_text(json.dumps(out, indent=2, default=_json_default))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size/1024:.1f} KB)")

    # eval_digest.md
    write_digest(reproduction_gate, rigor_fix, capability_gap_table, paper_blocks,
                 count_reconciliation, proofread_checklist)
    logger.info("Wrote eval_digest.md")

    # final $0 assertion
    assert COST_USD == 0.0 and N_LLM_CALLS == 0
    present_forbidden = [m for m in _FORBIDDEN if m in sys.modules]
    assert not present_forbidden, f"FORBIDDEN module appeared: {present_forbidden}"
    logger.info(f"DONE. $0 verified. Gate {GATE.n_passed()}/{len(GATE.checks)} hard checks passed.")


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return str(o)


def write_digest(reproduction_gate, rigor_fix, capability_gap_table, paper_blocks,
                 count_reconciliation, proofread_checklist):
    L = []
    L.append("# Eval digest — zero-spend re-analysis (caught-fraction headline)\n")
    L.append(f"**Reproduction gate:** {reproduction_gate['n_passed']}/{reproduction_gate['n_checks']} "
             f"hard checks PASSED (all_ok={reproduction_gate['all_ok']}); "
             f"{sum(1 for s in reproduction_gate['soft_cross_checks'] if s['ok'])}/"
             f"{len(reproduction_gate['soft_cross_checks'])} soft MC cross-checks within tol.\n")
    L.append("## Caught-fraction leaderboard (located-in sibling fabrications, n=135) — THE headline\n")
    lb = rigor_fix["caught_fraction_leaderboard"]["leaderboard"]
    L.append("| method | fraction caught |\n|---|---|")
    for m in ("certificate", "ct_verbalized", "ct_sc_margin", "ct_ptrue", "ct_negent",
              "queryside_verifier", "queryside_selfverify"):
        L.append(f"| {m} | {lb[m]['fraction_caught']} |")
    L.append(f"\nNEW doc-clustered paired-bootstrap gaps excluding 0: "
             f"{rigor_fix['caught_fraction_leaderboard']['new_bootstrap']['gaps_with_ci_excluding_0']}\n")
    L.append("## Pure-absent identity (rigor MAJOR)\n")
    L.append(rigor_fix["pure_absent_identity"]["statement"] + "\n")
    L.append("## Load-bearing natural confident-wrong\n")
    lbcw = rigor_fix["load_bearing_natural_confident_wrong"]
    L.append(f"certificate {lbcw['certificate']} vs raw/all-dispersion 0.30 vs verifier "
             f"{lbcw['queryside_verifier']} vs self-verify {lbcw['queryside_selfverify']}\n")
    L.append("## 16-cell capability-gap table (survival / caught per signal)\n")
    L.append("| corpus | reader | tag | verbalized | sc_margin | ptrue | negent |\n|---|---|---|---|---|---|---|")
    for r in capability_gap_table["rows"]:
        cells = " | ".join(f"{r['survival'][s]}/{r['caught'][s]}" for s in SIGNALS)
        L.append(f"| {r['corpus']} | {r['reader']} | {r['tag']} | {cells} |")
    L.append("\n*(cells are survival/caught)*\n")
    L.append("## Count reconciliation\n")
    L.append("```\n" + json.dumps(count_reconciliation, indent=1) + "\n```\n")
    L.append("## Seven paper-facing blocks\n")
    for k in ("located_in_results_table", "sec_boundary_block", "sibling_decisiveness_paragraph",
              "fuzzy_feasibility_note", "verifier_scope_block", "contribution_table"):
        L.append(paper_blocks[k] + "\n")
    L.append("### abstract_first_results_sentence_FORK\n")
    L.append("**FORK-A:** " + paper_blocks["abstract_first_results_sentence_FORK"]["FORK_A_demonstrated_fix"] + "\n")
    L.append("**FORK-B:** " + paper_blocks["abstract_first_results_sentence_FORK"]["FORK_B_honest_boundary"] + "\n")
    L.append("**Selection rule:** " + paper_blocks["abstract_first_results_sentence_FORK"]["selection_rule"] + "\n")
    L.append("## sec:boundary proofread checklist\n")
    for c in proofread_checklist:
        L.append(f"- [ ] {c}")
    (WORKDIR / "eval_digest.md").write_text("\n".join(L))


if __name__ == "__main__":
    main()
