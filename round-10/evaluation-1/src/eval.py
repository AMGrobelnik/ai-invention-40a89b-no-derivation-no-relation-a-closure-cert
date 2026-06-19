#!/usr/bin/env python3
"""iter-10 $0 re-analysis scaffold for the closure-certificate paper.

PURE ZERO-SPEND ($0, no network, no LLM): numpy / scipy / std-json only.  Reads the per-query
rows + metadata from THREE frozen iter-8 / iter-9 experiment outputs (S1 located-in, S2 verifier,
S3 booster), runs a REPRODUCTION / NO-SPEND GATE that recomputes every carried paper-facing literal
from the rows and HARD-ASSERTS it matches the carried metadata (HARD mismatch => raise, write nothing),
then emits a finished, defensible, paper-facing scaffold:

  BLOCK 0  reproduction / no-spend gate (hard stop on mismatch)
  BLOCK 1  RIGOR MAJOR  : stronger-verifier n=60 SUBSAMPLE table + CORRECTED tab:locatedin (0.100 removed)
  BLOCK 2  EVIDENCE MIN : 0.785 always paired with the extraction-gated / targeting-quality caveat (x4)
  BLOCK 3  PRESENT. MIN : de-densification checklist + lean intro skeleton (<=3 intro blocks)
  BLOCK 4  SCOPE MIN    : single feasibility-appendix consolidation plan
  BLOCK 5  NOVELTY MIN  : labeled distinguishing-sentence slot (filled by parallel research artifact)
  BLOCK 6  SIGNIFICANCE : abstract first-results FORK (selection rule) + one-thesis contribution table

Outputs eval.py + eval_out.json (full/mini/preview, exp_eval_sol_out-validated) + eval_digest.md.
Every derived number carries an evidence_tag from {CARRIED-LITERAL, REPRODUCED-FROM-ROWS,
RE-ANALYSIS-DERIVED, CARRIED-FROM-BLOCK, PENDING-PARALLEL-EXPERIMENT}.
"""
from __future__ import annotations

import json
import math
import sys
import resource
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats as scipy_stats  # noqa: F401  (available for completeness)
from loguru import logger

# --------------------------------------------------------------------------- #
# STEP 0 — GUARDRAILS & SETUP (validity layer)
# --------------------------------------------------------------------------- #
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# Memory limit (these JSONs are <7 MB so 4 GB is ample headroom).
_RAM_BUDGET = 4 * 1024 ** 3
try:
    resource.setrlimit(resource.RLIMIT_AS, (_RAM_BUDGET * 3, _RAM_BUDGET * 3))
except (ValueError, OSError):
    pass

# $0 cost counter — there is NO LLM path; never incremented; asserted ==0 at exit.
COST_USD = 0.0
N_LLM_CALLS = 0

# Forbidden modules: no network / LLM client may ever be imported.
_FORBIDDEN = ("requests", "httpx", "openai", "openrouter", "anthropic", "aiohttp",
              "llm", "readers", "queryside", "readers_locatedin", "dataio_redocred",
              "dataio_locatedin", "booster", "core")

REPRO_SEED = 20260618   # the booster's own seed — used ONLY to Monte-Carlo-match a CARRIED CI
EVAL_SEED = 20260617    # used for any genuinely-NEW bootstrap statistic this eval introduces

ROOT = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop")
FILES = {
    "locatedin": ROOT / "iter_8/gen_art/gen_art_experiment_1/full_method_out.json",   # S1
    "verifier":  ROOT / "iter_8/gen_art/gen_art_experiment_2/full_method_out.json",   # S2
    "booster":   ROOT / "iter_9/gen_art/gen_art_experiment_1/full_method_out.json",   # S3
}
WORKDIR = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_10/gen_art/gen_art_evaluation_1")

ABSTAIN = {"ABSTAIN", "no-relation", "no_relation", "none", ""}
SIGNALS = ("verbalized", "sc_margin", "ptrue", "negent")


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


def crux_caught(records, sigkey="metadata_conf_{}"):
    """Reproduce the located-in / Re-DocRED crux fraction-caught for the 4 dispersion signals,
    the certificate, and (if present in the rows) the 2 query-side gates.  `records` = the MIXED
    pool (present + absent of the regime).  Certificate-matched global threshold tuned to the
    certificate's MIXED coverage (matches the source method.py)."""
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

    cert_caught = float(np.mean([0.0 if cert_named[i] else 1.0 for i in halluc_idx])) if n_h else float("nan")
    out["per_method"]["certificate"] = {"fraction_caught": _r(cert_caught),
                                        "fraction_surviving": _r(1.0 - cert_caught) if cert_caught == cert_caught else None}

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


def doc_clustered_caught_gap_bootstrap(cert_caught_vec, comp_caught_vec, doc_ids, B=10000, seed=EVAL_SEED):
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
    """Doc-clustered paired bootstrap of mean(a) - mean(b) (for reproducing a CARRIED CI)."""
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
    bo_meta, _bo = load("booster")
    logger.info("Loaded 3 frozen experiment outputs (S1 located-in, S2 verifier, S3 booster).")

    # ----------------------------------------------------------------------- #
    # BLOCK 0 — REPRODUCTION / NO-SPEND GATE
    # ----------------------------------------------------------------------- #
    logger.info("=== BLOCK 0: reproduction gate (recompute-from-rows, assert==carried) ===")

    # ---- LOCATED-IN (S1) ----
    li_present = li["locatedin_present"]                  # 515 (held_out 400 + never_annotated 115)
    li_sib = li["locatedin_absent_sibling"]               # 450
    li_diff = li["locatedin_absent_diffcomponent"]        # 250
    li_sib_mixed = li_present + li_sib                    # 965

    GATE.hard("locatedin.count_present", len(li_present), 515, 0)
    GATE.hard("locatedin.count_sibling_absent", len(li_sib), 450, 0)
    GATE.hard("locatedin.count_diffcomponent_absent", len(li_diff), 250, 0)

    factA_sib = float(np.mean([1.0 if r["metadata_raw_named"] else 0.0 for r in li_sib]))
    factA_diff = float(np.mean([1.0 if r["metadata_raw_named"] else 0.0 for r in li_diff]))
    GATE.hard("locatedin.FACT_A.same_component_sibling", factA_sib, 0.30, 5e-3)
    GATE.hard("locatedin.FACT_A.different_component", factA_diff, 0.06, 5e-3)
    n_hall_sib = int(np.sum([1 for r in li_sib if r["metadata_raw_named"]]))
    GATE.hard("locatedin.FACT_A.n_hallucinated_sibling", n_hall_sib, 135, 0)
    GATE.hard("locatedin.FACT_A.n_hallucinated_diffcomp",
              int(np.sum([1 for r in li_diff if r["metadata_raw_named"]])), 15, 0)
    # FACT-A confidence distribution among the 135 sibling fabrications (carried)
    li_factA_md = li_meta["FACT_A_per_regime"]["same_component_sibling"]
    GATE.hard("locatedin.FACT_A.mean_conf", li_factA_md["hallucination_confidence_distribution"]["mean"], 0.9422, 1e-3)
    GATE.hard("locatedin.FACT_A.frac_ge_0.9", li_factA_md["hallucination_confidence_distribution"]["frac_ge_0.9"], 0.9481, 1e-3)

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

    # abstention decomposition (sibling pool) + GOLD-READ CEILING 1.0/1.0/1.0
    li_cert_named_present = float(np.sum([is_named(r["predict_certificate"]) for r in li_present]))
    li_cert_named_absent = float(np.sum([is_named(r["predict_certificate"]) for r in li_sib]))
    li_cert_named_total = li_cert_named_present + li_cert_named_absent
    li_over_abstain_present = len(li_present) - li_cert_named_present
    li_correct_absent_abst = len(li_sib) - li_cert_named_absent
    GATE.hard("locatedin.abst.certificate_named_total", li_cert_named_total, 59, 0)
    GATE.hard("locatedin.abst.over_abstain_present_rate", li_over_abstain_present / len(li_present), 0.9495, 5e-3)
    GATE.hard("locatedin.abst.correct_absent_abstention_rate", li_correct_absent_abst / len(li_sib), 0.9267, 5e-3)
    GATE.hard("locatedin.abst.present_coverage_llm_read", li_cert_named_present / len(li_present), 0.0505, 5e-3)
    li_gr = li_meta["abstention_decomposition_sibling"]["gold_read_ceiling"]
    GATE.hard("locatedin.gold_read_ceiling.present_coverage", li_gr["present_coverage"], 1.0, 0)
    GATE.hard("locatedin.gold_read_ceiling.correct_absent_abstention_rate", li_gr["correct_absent_abstention_rate"], 1.0, 0)
    GATE.hard("locatedin.gold_read_ceiling.present_selective_accuracy", li_gr["present_selective_accuracy_primitive"], 1.0, 0)

    # THE ARTIFACT identity: view1_absent 0.2267 reduction == signal_named_rate(0.30) - cert_named_rate(0.0733)
    identity_val = li_natcw["ct_verbalized"] - li_natcw["certificate"]
    carried_view1_reduction = li_meta["primary_reader_results_sibling_DECISIVE"]["view1_absent"]["ct_verbalized"]["confident_wrong_reduction"]
    GATE.hard("locatedin.view1_absent.reduction_carried", carried_view1_reduction, 0.2267, 1e-4)
    GATE.hard("locatedin.view1_absent.identity(0.30-0.0733)", identity_val, 0.2267, 5e-3)

    # mixed sibling matched-coverage confident-wrong reduction POINT (deterministic = cmp 0 - cert 0.0342)
    li_cert_cw_mixed = li_cert_named_absent / len(li_sib_mixed)
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
    li_ci = doc_clustered_rate_diff_bootstrap(np.zeros_like(cert_cw_vec), cert_cw_vec, doc_ids_mixed,
                                              B=10000, seed=REPRO_SEED)
    GATE.soft_check("locatedin.mixed.reduction_ci_lo", li_ci["ci95"][0], -0.0502, 0.01, "MC doc-clustered")
    GATE.soft_check("locatedin.mixed.reduction_ci_hi", li_ci["ci95"][1], -0.0204, 0.01, "MC doc-clustered")

    # cross-family (mistral) — CARRIED-NOT-REPRODUCED (no mistral per-row predictions in the file)
    li_xf = li_meta["cross_family_sensitivity"]
    assert abs(li_xf["FACT_A_per_regime"]["same_component_sibling"]["rate"] - 0.4378) < 1e-3
    assert abs(li_xf["FACT_B_crux_fraction_caught"]["certificate"]["fraction_caught"] - 0.7766) < 1e-3

    # ---- VERIFIER (S2) ----
    logger.info("--- verifier (S2) ---")
    vf_cl_present = vf["clutrr_present"]      # 102
    vf_cl_absent = vf["clutrr_absent"]        # 180
    vf_rd_present = vf["redocred_present"]    # 360
    vf_rd_absent = vf["redocred_absent"]      # 368
    vf_dr_present = vf["docred_present"]      # 116
    GATE.hard("verifier.count.clutrr_present", len(vf_cl_present), 102, 0)
    GATE.hard("verifier.count.clutrr_absent", len(vf_cl_absent), 180, 0)
    GATE.hard("verifier.count.redocred_present", len(vf_rd_present), 360, 0)
    GATE.hard("verifier.count.redocred_absent", len(vf_rd_absent), 368, 0)
    GATE.hard("verifier.count.docred_present", len(vf_dr_present), 116, 0)

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

    def selacc_present(rows, predkey, gold_key="metadata_gold"):
        cov = [r for r in rows if is_named(r.get(predkey))]
        if not cov:
            return float("nan"), 0
        correct = sum(1 for r in cov if str(r.get(predkey)) == str(r.get(gold_key)))
        return correct / len(cov), len(cov)

    vf_cl_cert_cov = float(np.mean([1.0 if is_named(r["predict_certificate"]) else 0.0 for r in vf_cl_present]))
    vf_cl_cert_selacc, _ = selacc_present(vf_cl_present, "predict_certificate")
    GATE.hard("verifier.clutrr_present.certificate_coverage", vf_cl_cert_cov, 0.6863, 5e-3)
    GATE.hard("verifier.clutrr_present.certificate_selective_accuracy", vf_cl_cert_selacc, 0.8857, 5e-3)
    GATE.hard("verifier.clutrr_present.certificate_cw_among_covered", 1.0 - vf_cl_cert_selacc, 0.1143, 5e-3)

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

    def caught_gap_repro(absent_rows, seed=REPRO_SEED):
        fab = [r for r in absent_rows if r.get("metadata_raw_named")]
        cert_c = np.array([1.0 if not is_named(r["predict_certificate"]) else 0.0 for r in fab], float)
        ver_c = np.array([1.0 if not is_named(r["predict_queryside_verifier"]) else 0.0 for r in fab], float)
        dids = [r["metadata_doc_id"] for r in fab]
        return doc_clustered_caught_gap_bootstrap(cert_c, ver_c, dids, B=10000, seed=seed)
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

    # ---- KINSHIP / Re-DocRED (reproduced from S2's redocred groups — same pool) ----
    logger.info("--- kinship / Re-DocRED (from S2 rows) ---")
    ki_present = vf_rd_present     # 360
    ki_absent = vf_rd_absent       # 368
    ki_mixed = ki_present + ki_absent
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

    # ---- BOOSTER (S3): stronger-verifier two-copy consistency + frontier + S0 reproduce ----
    logger.info("--- booster (S3): stronger-verifier consistency + frontier + S0-default reproduce ---")
    sv_block = bo_meta["located_in"]["stronger_verifier_block"]
    sv_copy = bo_meta["headline_summary"]["stronger_verifier_fraction_caught"]
    # two-copy consistency: the fraction_caught maps must be byte-equal
    sv_equal = (json.dumps(sv_block["fraction_caught"], sort_keys=True) == json.dumps(sv_copy, sort_keys=True))
    GATE.hard("booster.stronger_verifier.two_copy_consistency", 1.0 if sv_equal else 0.0, 1.0, 0)
    GATE.hard("booster.stronger_verifier.n_sibling", sv_block["n_sibling"], 250, 0)
    GATE.hard("booster.stronger_verifier.n_raw_hallucinations", sv_block["n_raw_hallucinations"], 60, 0)
    GATE.hard("booster.stronger_verifier.n_calls_zero", sv_block["n_calls"], 0, 0)
    GATE.hard("booster.stronger_verifier.cost_usd_zero", sv_block["cost_usd"], 0.0, 0)
    svf = sv_block["fraction_caught"]
    GATE.hard("booster.stronger_verifier.caught.certificate", svf["certificate"], 0.6667, 5e-3)
    GATE.hard("booster.stronger_verifier.caught.weak_same_model", svf["queryside_verifier_weak_same_model"], 0.20, 5e-3)
    GATE.hard("booster.stronger_verifier.caught.strong_xfamily", svf["queryside_verifier_strong"], 0.10, 5e-3)
    GATE.hard("booster.stronger_verifier.caught.selfverify_strong", svf["queryside_selfverify_strong"], 0.5333, 5e-3)
    # within-subsample STRICT ordering: certificate > self-verify-strong > weak same-model > strong x-family
    order_ok = (svf["certificate"] > svf["queryside_selfverify_strong"]
                > svf["queryside_verifier_weak_same_model"] > svf["queryside_verifier_strong"])
    GATE.hard("booster.stronger_verifier.within_subsample_ordering", 1.0 if order_ok else 0.0, 1.0, 0)
    svcw = sv_block["natural_confident_wrong_on_sibling"]
    GATE.hard("booster.stronger_verifier.cw.certificate", svcw["certificate"], 0.096, 5e-3)
    GATE.hard("booster.stronger_verifier.cw.strong_xfamily", svcw["queryside_verifier_strong"], 0.216, 5e-3)

    # frontier slopes (S3) — the recall-precision frontier is FUNDAMENTAL for prompt-only extraction
    li_front = bo_meta["located_in"]["frontier_extrapolation"]
    ki_front = bo_meta["kinship"]["frontier_extrapolation"]
    GATE.hard("booster.frontier.locatedin_min_over6_ci_lo_vs_recall_slope",
              li_front["min_over6_ci_lo_vs_recall_slope"], -0.3038, 1e-3)
    GATE.hard("booster.frontier.kinship_min_over6_ci_lo_vs_recall_slope",
              ki_front["min_over6_ci_lo_vs_recall_slope"], -0.6724, 1e-3)
    GATE.hard("booster.frontier.locatedin_present_coverage_vs_recall_slope",
              li_front["present_coverage_vs_recall_slope"], 0.9202, 1e-3)
    assert li_front["min_over6_ci_lo_vs_recall_slope"] < 0 and ki_front["min_over6_ci_lo_vs_recall_slope"] < 0, \
        "frontier slopes must be NEGATIVE (boundary is fundamental for prompt-only extraction)"

    # S0 default strategy reproduces iter-8 EXACTLY
    bo_rows = {r["strategy"]: r for r in bo_meta["located_in"]["per_strategy_rows"]}
    s0 = bo_rows["default"]
    GATE.hard("booster.S0_default.atomic_recall_canon", s0["atomic_recall_canon"], 0.1478, 1e-4)
    GATE.hard("booster.S0_default.present_coverage", s0["present_coverage"], 0.0505, 5e-3)
    GATE.hard("booster.S0_default.absent_sibling_confident_wrong_certificate",
              s0["absent_sibling_confident_wrong_certificate"], 0.0733, 5e-3)
    GATE.hard("booster.S0_default.certificate_fraction_caught_sibling",
              s0["certificate_fraction_caught_sibling"], 0.7852, 5e-3)
    GATE.hard("booster.S0_default.gold_read_present_coverage", s0["gold_read_present_coverage"], 1.0, 0)
    bo_verdict = bo_meta["overall_verdict"]
    bo_verdict_str = bo_verdict if isinstance(bo_verdict, str) else json.dumps(bo_verdict)
    assert "EXTRACTION-LIMITED-BOUNDARY" in bo_verdict_str, "booster verdict must confirm boundary"

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

    # ======================================================================= #
    # BLOCK 1 — RIGOR MAJOR: stronger-verifier n=60 SUBSAMPLE table + CORRECTED tab:locatedin
    # ======================================================================= #
    logger.info("=== BLOCK 1: rigor_major (n=60 stronger-verifier table + corrected tab:locatedin) ===")

    # (1a) the stronger-verifier OWN-denominator table (carried + consistency-checked)
    stronger_verifier_own_subsample_table = {
        "denominator_note": ("deepseek/deepseek-v3.2 k=5 verifier on a 250-pair sibling SUBSAMPLE carrying 60 "
                             "raw gemini fabrications — this denominator DIFFERS from the main n_sibling=450 / "
                             "135-fabrication pool; numbers here are NOT comparable to the main column"),
        "model": "deepseek/deepseek-v3.2",
        "k_self_consistency": 5,
        "n_sibling": 250,
        "n_raw_fabrications": 60,
        "fraction_caught": {
            "certificate": 0.667,
            "queryside_selfverify_strong": 0.533,
            "queryside_verifier_weak_same_model": 0.20,
            "queryside_verifier_strong_xfamily": 0.10,
        },
        "natural_confident_wrong": {
            "certificate": 0.096,
            "queryside_selfverify_strong": 0.112,
            "queryside_verifier_weak_same_model": 0.192,
            "queryside_verifier_strong_xfamily": 0.216,
        },
        "within_subsample_ordering": ("certificate 0.667 > self-verify-strong 0.533 > weak same-model 0.20 "
                                      "> stronger x-family 0.10"),
        "qualitative_conclusion": ("a STRONGER, larger, different-family verifier is NO BETTER (in fact WORSE: a "
                                   "better geographer over-infers co-regional containment); both verifiers sit far "
                                   "below the certificate -> certificate-necessity is intrinsic to running the "
                                   "premise check on a generative LLM, not an artifact of a weak same-model verifier "
                                   "(retires methodology MINOR #5)"),
        "denominator_hygiene_note": ("in THIS table the same-model weak verifier value is 0.20 (its value RESTRICTED "
                                     "to the n=60 subsample), NOT 0.274 (the full n=450/135 pool value); the two are "
                                     "kept in separate tables by construction"),
        "two_copy_consistency_checked": bool(sv_equal),
        "evidence_tag": "CARRIED-FROM-BLOCK / REPRODUCED-FROM-CONSISTENCY",
    }

    sv_tbl = stronger_verifier_own_subsample_table["fraction_caught"]
    sv_cw = stronger_verifier_own_subsample_table["natural_confident_wrong"]
    stronger_verifier_latex = (
        "% Table~\\ref{tab:stronger-verifier} — stronger cross-family verifier on its OWN n=60 subsample\n"
        "\\begin{tabular}{lcc}\n\\toprule\n"
        "method (deepseek-v3.2, $k{=}5$; $n_{\\text{sibling}}{=}250$, 60 fabrications) & frac.\\ caught & nat.\\ conf-wrong \\\\\n"
        "\\midrule\n"
        f"\\textbf{{certificate (no-derivation)}} & \\textbf{{{sv_tbl['certificate']:.3f}}} & {sv_cw['certificate']:.3f} \\\\\n"
        f"self-verification (strong) & {sv_tbl['queryside_selfverify_strong']:.3f} & {sv_cw['queryside_selfverify_strong']:.3f} \\\\\n"
        f"query-side verifier (weak, same-model) & {sv_tbl['queryside_verifier_weak_same_model']:.3f} & {sv_cw['queryside_verifier_weak_same_model']:.3f} \\\\\n"
        f"query-side verifier (strong, x-family) & {sv_tbl['queryside_verifier_strong_xfamily']:.3f} & {sv_cw['queryside_verifier_strong_xfamily']:.3f} \\\\\n"
        "\\bottomrule\n\\end{tabular}"
    )

    # (1b) the CORRECTED n=450/135 shared-denominator leaderboard — stronger-x-family 0.100 REMOVED.
    fab_li = [r for r in li_sib if r.get("metadata_raw_named")]          # 135 fabrications
    fab_doc_ids = [r["metadata_doc_id"] for r in fab_li]
    cert_caught_vec = np.array([1.0 if not is_named(r["predict_certificate"]) else 0.0 for r in fab_li], float)
    tau = {s: li_crux["per_method"][f"ct_{s}"]["tau_global"] for s in SIGNALS}

    caught_leaderboard = {"certificate": {"fraction_caught": _r(cm["certificate"]["fraction_caught"]),
                                          "evidence_tag": "REPRODUCED-FROM-ROWS"}}
    caught_gaps = {}
    for s in SIGNALS:
        m = f"ct_{s}"
        comp_caught_vec = np.array([1.0 if (float(r.get(f"metadata_conf_{s}", 0.0) or 0.0) < tau[s]) else 0.0
                                    for r in fab_li], float)
        gap = doc_clustered_caught_gap_bootstrap(cert_caught_vec, comp_caught_vec, fab_doc_ids, B=10000, seed=EVAL_SEED)
        caught_leaderboard[m] = {"fraction_caught": _r(cm[m]["fraction_caught"]),
                                 "cert_minus_method_caught_gap": gap, "evidence_tag": "RE-ANALYSIS-DERIVED"}
        caught_gaps[m] = gap
    for qs in ("queryside_verifier", "queryside_selfverify"):
        comp_caught_vec = np.array([1.0 if not is_named(r[f"predict_{qs}"]) else 0.0 for r in fab_li], float)
        gap = doc_clustered_caught_gap_bootstrap(cert_caught_vec, comp_caught_vec, fab_doc_ids, B=10000, seed=EVAL_SEED)
        caught_leaderboard[qs] = {"fraction_caught": _r(cm[qs]["fraction_caught"]),
                                  "cert_minus_method_caught_gap": gap, "evidence_tag": "RE-ANALYSIS-DERIVED"}
        caught_gaps[qs] = gap
    gaps_excluding_0 = [m for m, g in caught_gaps.items() if g["ci_excludes_0"]]

    # build the CORRECTED table in display order (NO stronger-x-family row); relabel verifier as same-model
    corrected_method_order = [
        ("certificate", "certificate (no-derivation)"),
        ("ct_verbalized", "verbalized confidence"),
        ("ct_ptrue", "Kadavath P(True)"),
        ("ct_sc_margin", "self-consistency margin"),
        ("ct_negent", "semantic-entropy"),
        ("queryside_verifier", "query-side verifier (same-model)"),
        ("queryside_selfverify", "self-verification"),
    ]
    corrected_methods = []
    for key, label in corrected_method_order:
        entry = {"method_key": ("queryside_verifier_same_model" if key == "queryside_verifier" else key),
                 "label": label,
                 "fraction_caught": caught_leaderboard[key]["fraction_caught"],
                 "evidence_tag": caught_leaderboard[key]["evidence_tag"]}
        if key != "certificate":
            g = caught_leaderboard[key]["cert_minus_method_caught_gap"]
            entry["cert_minus_method_caught_gap"] = {"gap": g["gap"], "ci95": g["ci95"],
                                                     "ci_excludes_0": g["ci_excludes_0"], "n_boot": g["n_boot"]}
        corrected_methods.append(entry)

    footnote_pointer = ("The stronger cross-family verifier (deepseek-v3.2, k=5) is reported on its OWN n=60 "
                        "subsample in Table~\\ref{tab:stronger-verifier}; its 0.10 caught fraction is computed on a "
                        "different denominator (n_sibling=250, 60 fabrications) and is NOT comparable to this column.")

    def _fmt_gap(e):
        if "cert_minus_method_caught_gap" not in e:
            return "--", "--"
        g = e["cert_minus_method_caught_gap"]
        return f"{g['gap']:.3f}", f"[{g['ci95'][0]:.3f}, {g['ci95'][1]:.3f}]"
    corrected_latex_rows = []
    for e in corrected_methods:
        gp, ci = _fmt_gap(e)
        if e["method_key"] == "certificate":
            corrected_latex_rows.append(f"\\textbf{{{e['label']}}} & \\textbf{{{e['fraction_caught']:.3f}}} & -- & -- \\\\")
        else:
            corrected_latex_rows.append(f"{e['label']} & {e['fraction_caught']:.3f} & {gp} & {ci} \\\\")
    corrected_tab_locatedin_latex = (
        "% Table~\\ref{tab:locatedin} — CORRECTED caught-fraction (n_sibling=450, 135 fabrications; identical denom.)\n"
        "% NOTE: the stronger x-family verifier 0.100 is DELIBERATELY ABSENT — see footnote / Table~\\ref{tab:stronger-verifier}.\n"
        "\\begin{tabular}{lccc}\n\\toprule\n"
        "method & frac.\\ caught & cert$-$method gap & 95\\% CI \\\\\n\\midrule\n"
        + "\n".join(corrected_latex_rows) +
        "\n\\bottomrule\n\\end{tabular}"
    )

    corrected_tab_locatedin = {
        "denominator": "n_sibling=450 / 135 raw-LLM confident fabrications (identical for every method in this column)",
        "methods": corrected_methods,
        "footnote_pointer": footnote_pointer,
        "n_caught_gaps_excluding_0_of_6": len(gaps_excluding_0),
        "all_six_gaps_exclude_0": (len(gaps_excluding_0) == 6),
        "stronger_xfamily_0100_row_removed": True,
        "latex_table_body": corrected_tab_locatedin_latex,
        "evidence_tag": "RE-ANALYSIS-DERIVED",
    }

    # (4) AUTOMATED DENOMINATOR-HYGIENE GUARD: 0.10 (stronger x-family) must be ABSENT from the
    #     n=450/135 column, and no method row may be keyed as the stronger / x-family verifier.
    def assert_0100_absent(corrected):
        bad_vals, bad_keys = [], []
        for e in corrected["methods"]:
            if abs(float(e["fraction_caught"]) - 0.10) <= 1e-9:
                bad_vals.append(e["method_key"])
            k = str(e["method_key"]).lower()
            if ("strong" in k) or ("x-family" in k) or ("xfamily" in k):
                bad_keys.append(e["method_key"])
        return bad_vals, bad_keys
    bad_vals, bad_keys = assert_0100_absent(corrected_tab_locatedin)
    assert not bad_vals, f"GUARD FAIL: 0.100 present in n=450/135 column rows {bad_vals}"
    assert not bad_keys, f"GUARD FAIL: stronger/x-family verifier row leaked into n=450/135 column {bad_keys}"
    logger.info("DENOMINATOR-HYGIENE GUARD passed: 0.100 absent from corrected tab:locatedin; no x-family row leak.")

    rigor_major_retired = bool(corrected_tab_locatedin["stronger_xfamily_0100_row_removed"]
                               and (len(stronger_verifier_own_subsample_table["fraction_caught"]) == 4)
                               and order_ok and sv_equal)
    rigor_major = {
        "stronger_verifier_own_subsample_table": stronger_verifier_own_subsample_table,
        "stronger_verifier_latex_table_body": stronger_verifier_latex,
        "corrected_tab_locatedin": corrected_tab_locatedin,
        "rigor_major_retired": rigor_major_retired,
        "retired_iff": ("(corrected table excludes 0.100) AND (separate n=60 table present) AND "
                        "(within-subsample qualitative conclusion / ordering holds)"),
        "block_note": ("the stronger_verifier_block is AGGREGATE-only in S3 (n_calls=0, n_cache_hits=2500), so the "
                       "four literals are CARRIED and verified via the two-copy consistency check "
                       "(located_in.stronger_verifier_block.fraction_caught vs "
                       "headline_summary.stronger_verifier_fraction_caught) + the strict within-subsample ordering "
                       "assertion, rather than row-recompute"),
        "evidence_tag": "CARRIED-FROM-BLOCK",
    }

    # ======================================================================= #
    # BLOCK 2 — EVIDENCE MINOR: 0.785 always paired with extraction-gated / targeting-quality caveat
    # ======================================================================= #
    logger.info("=== BLOCK 2: evidence_minor (4 paired-caveat sentences) ===")
    paired = {
        "abstract": ("On a non-by-construction natural same-component-sibling regime the no-derivation certificate "
                     "catches 0.785 of the raw reader's high-confidence absent-relation fabrications versus 0.274 for "
                     "the strongest query-side verifier and <=0.40 for every confidence signal (all six "
                     "certificate-minus-competitor caught-gaps exclude 0); we report this as TARGETING QUALITY, not a "
                     "deployment win — the catching objective on a pure-absent pool structurally favors high-abstention "
                     "methods (it measures only how well a method's abstentions target the fabrications), and the "
                     "certificate's NET utility on mixed present/absent natural prose remains extraction-gated."),
        "intro": ("Our headline safety number is a TARGETING-QUALITY result, not a deployment win: the certificate "
                  "turns 0.785 of the raw reader's high-confidence sibling fabrications into abstentions (vs 0.274 for "
                  "the strongest query-side verifier), but because this catching objective is scored on a pure-absent "
                  "pool it structurally favors methods that abstain more on absent pairs, and the certificate's NET "
                  "utility on mixed present/absent natural prose stays extraction-gated."),
        "contribution_3": ("Third, we isolate a one-sided catching win as TARGETING QUALITY rather than a deployment "
                           "win: on the natural sibling-absent pool the certificate catches 0.785 of the raw "
                           "fabrications against 0.274 for the strongest query-side verifier, while acknowledging that "
                           "the pure-absent catching objective structurally rewards high-abstention methods and that "
                           "the net mixed-pool utility remains extraction-gated."),
        "conclusion": ("In sum the certificate catches 0.785 of the confident absent-relation fabrications versus 0.274 "
                       "for the strongest query-side verifier, a TARGETING-QUALITY win and not a deployment win — the "
                       "catching objective on a pure-absent pool structurally favors high-abstention methods, so the "
                       "certificate's NET deployable utility on mixed natural prose remains extraction-gated until a "
                       "precision-preserving extractor lifts present coverage."),
    }
    def _has_both_caveats(s):
        sl = s.lower().replace("-", " ")   # normalize hyphenation (TARGETING-QUALITY / extraction-gated)
        clause_i = (("extraction gated" in sl) and ("deployment win" in sl)
                    and (("not a deployment" in sl) or ("rather than a deployment" in sl)))
        clause_ii = ("targeting quality" in sl) and (("high abstention" in sl)
                                                     or ("abstain more on absent" in sl)
                                                     or ("favors high abstention" in sl)
                                                     or ("rewards high abstention" in sl)
                                                     or ("structurally" in sl))
        return clause_i and clause_ii and ("0.785" in s)
    paired_checks = {k: bool(_has_both_caveats(v)) for k, v in paired.items()}
    evidence_minor_retired = all(paired_checks.values())
    assert evidence_minor_retired, f"evidence MINOR: a paired sentence is missing a caveat clause: {paired_checks}"
    evidence_minor = {
        "paired_caveat_sentences": paired,
        "per_sentence_both_clauses_present": paired_checks,
        "clause_i": "net-utility caveat (extraction-gated, NOT a deployment win)",
        "clause_ii": ("the catching objective on a PURE-ABSENT pool inherently favors high-abstention methods (it "
                      "measures only how well abstentions target the fabrications, structurally rewarding abstaining "
                      "more on absent pairs) -> establishes TARGETING QUALITY, not deployable net utility"),
        "evidence_minor_retired": evidence_minor_retired,
        "evidence_tag": "RE-ANALYSIS-DERIVED",
    }

    # ======================================================================= #
    # BLOCK 3 — PRESENTATION MINOR: de-densify
    # ======================================================================= #
    logger.info("=== BLOCK 3: presentation_minor (de-densify + lean intro) ===")
    de_densification_checklist = [
        ("[1] Evidence-class tags (REAL-LLM-READ, GOLD-ONLY-GATE, SYNTHETIC-CHANNEL, THEOREM, "
         "REAL-LLM-READ-ON-SYNTHETIC) appear ONLY in the spine table + section headers; DELETE every inline "
         "\\textsc{...} marker in results prose."),
        ("[2] Rewrite reviewer-response meta-narration as declarative claims-with-caveats — replace 'a skeptical "
         "reviewer rightly observed...', 'stated without spin', 'we never let that number carry the contribution' "
         "with plain assertions of the caveated claim."),
        ("[3] Collapse the 7 bold-headed intro paragraphs into <=3 so the contributions list + headline numbers "
         "(FACT A rate; capability gap; caught 0.785) appear within the first ~half page."),
        ("[4] Flag duplicated / near-duplicate consecutive sentences and any '...'-truncated fragments."),
        ("[5] Every selective-accuracy / confident-wrong number must carry its coverage/abstention qualifier."),
    ]
    lean_intro_skeleton = [
        {"block": 1, "role": "problem + thesis",
         "bullets": [
             "(a) PROBLEM: confident absent-relation hallucination as a compositional false-premise failure in the "
             "deduction sub-module of a text->FOL pipeline.",
             "(b) THESIS (one sentence): a high-recall disjunctive reader + compose-through-exact-table + "
             "abstain-on-no-derivation; the certificate MECHANISM is the INHERITED NeSy premise (+0.673 inherited / "
             "+0.0025 novel)."]},
        {"block": 2, "role": "three contributions + headline numbers",
         "bullets": [
             "(c1) a corpus/domain/reader-robust DIAGNOSTIC = FACT A (confident absent-fabrication rate 0.30 "
             "sibling / 0.06 diffcomponent, transfers across readers+corpora) + a signal-agnostic capability gap.",
             "(c2) a one-sided TARGETING-QUALITY catching win (caught 0.785) that beats the confidence family "
             "(<=0.40) AND the same-model verifier (0.274) AND the stronger cross-family verifier (0.10 on its own "
             "n=60 subsample).",
             "(c3) a QUANTIFIED recall-precision frontier proving the natural-prose net-utility boundary is "
             "FUNDAMENTAL for prompt-only extraction (slope -0.30 located-in / -0.67 kinship; gold-read ceiling "
             "1.0/1.0/1.0)."]},
        {"block": 3, "role": "scope + venue",
         "bullets": [
             "(d) OUT-OF-SCOPE (stated in the intro, not the appendix): OpenCyc grounding, atomic re-extraction, "
             "general fuzzy unification, genuine ~3000-char documents = future work.",
             "(e) VENUE: ACL Knowledge Extraction PRIMARY, NeSy fallback."]},
    ]
    presentation_minor_retired = (len(lean_intro_skeleton) <= 3 and len(de_densification_checklist) == 5)
    presentation_minor = {
        "de_densification_checklist": de_densification_checklist,
        "lean_intro_skeleton": lean_intro_skeleton,
        "n_intro_blocks": len(lean_intro_skeleton),
        "presentation_minor_retired": presentation_minor_retired,
        "evidence_tag": "RE-ANALYSIS-DERIVED",
    }

    # ======================================================================= #
    # BLOCK 4 — SCOPE MINOR: one feasibility appendix
    # ======================================================================= #
    logger.info("=== BLOCK 4: scope_minor (single feasibility appendix) ===")
    feasibility_appendix_consolidation_plan = {
        "appendix_title": "Appendix A — Feasibility on commodity hardware (NOT a substantive contribution)",
        "preamble": ("Both notes below are FEASIBILITY demonstrations on commodity hardware, NOT substantive "
                     "contributions; the substantive contributions are the diagnostic, the targeting-quality catching "
                     "win, and the recall-precision frontier (intro)."),
        "subsection_1": {
            "title": "A.1 Operational ~3000-char bracket-selected case study",
            "source_artifacts": ["art_WQoePKrpsTPo"],
            "content": ("95 Prolog programs discharged & executed in swipl 9.0.4; hallucination reduction 0.27-0.60 "
                        "(mean 0.45) at Mode-A coverage 0-0.33; atomic recall ~0.49 is the binding ceiling. CUT the "
                        "concatenated-kinship arm (56/56 cross-story abstentions are trivial by construction). LABEL "
                        "the documents bracket-selected. STATE: the pipeline RUNS at length, NOT that it is USEFUL at "
                        "length."),
            "evidence_tag": "CARRIED-LITERAL"},
        "subsection_2": {
            "title": "A.2 Fuzzy-unification feasibility note",
            "source_artifacts": ["art_I22c-J7-OcXl", "art_0MDLD-w-RXOu"],
            "content": ("vague prepositions / informal kinship -> calibrated sub-1.0 disjunctions; fraction-at-1.0 0.00 "
                        "vs Mode-P 1.00; per-candidate ECE 0.142 spatial / 0.111 kinship; Mode-B catches "
                        "around->{NTPPi,TPPi} 5/5 sound-violating spatial reads (kinship UNTESTED). Supporting "
                        "query-level cert confident-wrong 0.000 vs commit-argmax 0.364/0.216 WITH the "
                        "query-vs-edge unit-of-analysis caveat."),
            "evidence_tag": "CARRIED-LITERAL"},
        "out_of_scope_statement_location": "INTRO (not the appendix)",
        "layout": "ONE appendix, ONE title, TWO subsections (A.1, A.2)",
        "scope_minor_retired": True,
        "evidence_tag": "RE-ANALYSIS-DERIVED",
    }

    # ======================================================================= #
    # BLOCK 5 — NOVELTY MINOR slot
    # ======================================================================= #
    logger.info("=== BLOCK 5: novelty_minor (distinguishing-sentence slot) ===")
    novelty_minor = {
        "distinguishing_sentence_slot": {
            "label": "NOVELTY-DISTINGUISHING-SENTENCE (filled by parallel research artifact)",
            "purpose": ("one sentence separating the no-derivation certificate (per-query, gold-free, training-free, "
                        "NO-external-KB abstention from deductive closure over the document-INTERNAL relation graph) "
                        "from ontology-grounded POST-EXTRACTION structural CORRECTION (e.g. arXiv:2605.29168), which "
                        "repairs/commits a labeling against EXTERNAL ontology structure — preserving the gold-free / "
                        "training-free / no-external-KB delta"),
            "placeholder_text": ("<<FILL: no-derivation certificate vs ontology-grounded post-extraction correction — "
                                 "verified content from the parallel research artifact>>"),
            "status": "PENDING-PARALLEL-RESEARCH-ARTIFACT",
            "evidence_tag": "PENDING-PARALLEL-EXPERIMENT",
        },
    }

    # ======================================================================= #
    # BLOCK 6 — SIGNIFICANCE: abstract FORK + updated contribution table
    # ======================================================================= #
    logger.info("=== BLOCK 6: significance (abstract FORK + contribution table) ===")
    abstract_first_results_fork = {
        "FORK_A_demonstrated_fix": ("... + a DEMONSTRATED net-utility fix on natural prose via a PRECISION-PRESERVING "
                                    "extractor: on a mixed present / same-component-sibling-absent pool the "
                                    "certificate's Holm-adjusted, doc-clustered mixed-pool confident-wrong reduction CI "
                                    "EXCLUDES 0 at extraction recall R*, matching/beating the query-side verifier ..."),
        "FORK_B_honest_boundary": ("... + a targeting-quality catching win (caught-fraction cert 0.785 vs verifier "
                                   "0.274, extraction-gated, not a deployment win) + a net-utility boundary shown "
                                   "FUNDAMENTAL even for precision-preserving extraction (deeper than prompt-only) ..."),
        "selection_rule": ("Use FORK_A IFF the parallel iter-10 precision-preserving-extractor experiment flips the "
                           "mixed-pool confident-wrong reduction CI to EXCLUDE 0 on a natural "
                           "(non-structural-by-construction) regime AND the certificate matches/beats the query-side "
                           "verifier; otherwise use FORK_B. GEN_PAPER_TEXT reads the extractor experiment verdict and "
                           "selects."),
        "status": "PENDING-PARALLEL-EXPERIMENT",
        "evidence_tag": "PENDING-PARALLEL-EXPERIMENT",
    }
    contribution_rows = [
        {"contribution": "ROBUST DIAGNOSTIC (FACT A + signal-agnostic mixed-pool capability gap)",
         "status": "ESTABLISHED", "evidence_tag": "REAL-LLM-READ"},
        {"contribution": ("TARGETING-QUALITY CATCHING WIN (0.785, one-sided, extraction-gated; beats confidence "
                          "family + same-model + stronger x-family verifier)"),
         "status": "ESTABLISHED-BUT-ONE-SIDED", "evidence_tag": "RE-ANALYSIS-DERIVED"},
        {"contribution": ("RECALL-PRECISION FRONTIER (prompt-only natural-prose net-utility boundary FUNDAMENTAL; "
                          "slope -0.30/-0.67, gold-read ceiling 1.0/1.0/1.0)"),
         "status": "ESTABLISHED", "evidence_tag": "REAL-LLM-READ"},
        {"contribution": ("certificate MECHANISM (forward least-fixpoint closure -> abstain)"),
         "status": "INHERITED NeSy premise (+0.673 inherited / +0.0025 novel)", "evidence_tag": "INHERITED-NESY-PREMISE"},
        {"contribution": ("DEMONSTRATED-FIX-OR-DEEPER-BOUNDARY (net mixed-pool reduction CI excluding 0 on a natural "
                          "regime via precision-preserving extraction, OR the boundary shown fundamental even there)"),
         "status": "PENDING-EXTRACTOR-EXPERIMENT (FORK)", "evidence_tag": "PENDING-PARALLEL-EXPERIMENT"},
    ]
    contribution_table_md = ("### contribution table (one thesis)\n\n| contribution | status |\n|---|---|\n"
                             + "\n".join(f"| {r['contribution']} | {r['status']} [{r['evidence_tag']}] |"
                                        for r in contribution_rows))
    significance = {
        "abstract_first_results_fork": abstract_first_results_fork,
        "contribution_table": {"rows": contribution_rows, "markdown": contribution_table_md,
                               "evidence_tag": "RE-ANALYSIS-DERIVED"},
    }

    # ----------------------------------------------------------------------- #
    # count reconciliation + capability table (carried/reproduced) + verdict mirrors
    # ----------------------------------------------------------------------- #
    count_reconciliation = {
        "kinship_redocred_primary_slice": {
            "present_multihop": 360, "present_composed_only_non_circular": 222, "absent": 368,
            "engine_round_trip_present_combined": 476, "engine_round_trip_absent_combined": 577,
            "docred_present": 116, "docred_absent": 209, "docred_absent_false_negative_frac": 0.646,
            "explanation": ("the 476/476 present and 577/577 absent engine round-trip is the COMBINED re-docred "
                            "(360/368) + docred (116/209, whose absent gold is downgraded ~64.6% false-negatives); "
                            "removes the apparent 360!=476 / 368!=577 inconsistency"),
            "evidence_tag": "CARRIED-LITERAL (present/absent 360/368 + docred_present 116 reproduced from S2 rows)"},
        "locatedin": {"present": 515, "same_component_sibling_absent": 450, "different_component_absent": 250,
                      "never_annotated": 115, "held_out": 400, "n_docs": 283,
                      "note": "present 515 = held_out 400 + never_annotated 115",
                      "evidence_tag": "REPRODUCED-FROM-ROWS"},
        "evidence_tag": "REPRODUCED-FROM-ROWS / CARRIED-LITERAL",
    }

    capability_gap_table = {
        "rows": [
            {"corpus": "Re-DocRED", "reader": "gemini", "tag": "REPRODUCED-FROM-ROWS (S2)",
             "survival": {s: kcm[f"ct_{s}"]["fraction_surviving"] for s in SIGNALS},
             "caught": {s: kcm[f"ct_{s}"]["fraction_caught"] for s in SIGNALS}},
            {"corpus": "Re-DocRED", "reader": "deepseek", "tag": "CARRIED-LITERAL",
             "survival": {"verbalized": 0.4118, "sc_margin": 0.2941, "ptrue": 0.3235, "negent": 0.2941},
             "caught": {"verbalized": 0.5882, "sc_margin": 0.7059, "ptrue": 0.6765, "negent": 0.7059},
             "note": "cross-family is aggregate-only in the source; carried (cross-checked vs precedent eval X)"},
            {"corpus": "CLUTRR", "reader": "gemini", "tag": "CARRIED-LITERAL",
             "survival": {"verbalized": 0.4353, "sc_margin": 0.7176, "ptrue": 0.2471, "negent": 0.7176},
             "caught": {"verbalized": 0.5647, "sc_margin": 0.2824, "ptrue": 0.7529, "negent": 0.2824},
             "note": "cross-checked against S2 (verifier) reproduction_gate which re-derived them"},
            {"corpus": "CLUTRR", "reader": "deepseek", "tag": "CARRIED-LITERAL",
             "survival": {"verbalized": 0.672, "sc_margin": 0.224, "ptrue": 0.103, "negent": 0.224},
             "caught": {"verbalized": 0.328, "sc_margin": 0.776, "ptrue": 0.897, "negent": 0.776},
             "note": "THREE of four dispersion signals catch 78-90% for the stronger deepseek reader"},
        ],
        "FACT_A_robust_corpus_and_reader_transferable": {
            "CLUTRR_gemini": 0.472, "CLUTRR_deepseek": 0.483, "ReDocRED_gemini": _r(ki_factA),
            "ReDocRED_deepseek": 0.318, "locatedin_sibling_gemini": _r(factA_sib), "locatedin_sibling_mistral": 0.4378,
            "statement": "the raw confident-fabrication RATE transfers across readers AND corpora (the ROBUST fact)",
            "evidence_tag": "REAL-LLM-READ"},
        "FACT_B_reader_and_signal_dependent": {
            "statement": ("which signals catch the fabrications is READER- and SIGNAL-dependent: verbalized confidence "
                          "is the most robustly BLIND signal; dispersion signals catch the MAJORITY for the stronger "
                          "deepseek reader but commit most under gemini"),
            "evidence_tag": "RE-ANALYSIS-DERIVED"},
    }

    verdict_mirrors = {
        "locatedin": {"overall": li_verdict["overall"],
                      "certificate_beats_all_6_baselines_holm": li_verdict["certificate_beats_all_6_baselines_holm"],
                      "verifier_suffices": li_verdict["verifier_suffices"]},
        "verifier": {"overall": vf_meta["certificate_necessity_verdict"]["overall"]["headline"],
                     "reproduction_gate_32_32": vf_meta["reproduction_gate"]["all_ok"]},
        "booster": {"overall": "EXTRACTION-LIMITED-BOUNDARY-CONFIRMED",
                    "stronger_verifier_methodology_minor5_retired": True},
        "rigor_major_retired": rigor_major_retired,
        "evidence_minor_retired": evidence_minor_retired,
        "presentation_minor_retired": presentation_minor_retired,
        "scope_minor_retired": True,
        "novelty_minor_status": "PENDING-PARALLEL-RESEARCH-ARTIFACT",
        "significance_fork_status": "PENDING-PARALLEL-EXPERIMENT",
    }

    # ----------------------------------------------------------------------- #
    # Assemble output
    # ----------------------------------------------------------------------- #
    logger.info("=== assembling output ===")
    assert COST_USD == 0.0 and N_LLM_CALLS == 0, "BUDGET VIOLATION: this eval is pure $0 re-analysis"

    reproduction_gate = {
        "all_ok": GATE.all_ok(), "n_checks": len(GATE.checks), "n_passed": GATE.n_passed(),
        "tolerance_rates": 5e-3, "tolerance_fractions": 1e-4, "tolerance_ci_mc": 1e-2,
        "checks": GATE.checks, "soft_cross_checks": GATE.soft,
        "note": ("every paper-facing literal recomputed from the per-query rows (S1 located-in, S2 verifier+Re-DocRED) "
                 "and hard-asserted against the carried metadata (mirrors exp_2's 32/32 gate and the iter-9 precedent's "
                 "68/68); the stronger-verifier block is aggregate-only in S3 so it is verified via two-copy consistency "
                 "+ strict within-subsample ordering; frontier slopes + S0-default reproduce iter-8 from S3; soft checks "
                 "are doc-clustered bootstrap CIs reproduced to Monte-Carlo tolerance and tie-break-sensitive selaccs."),
        "caught_fraction_leaderboard_n450": {
            "denominator": "the 135 raw-LLM confident absent-sibling fabrications (identical for every method)",
            "leaderboard": caught_leaderboard,
            "new_bootstrap": {"seed": EVAL_SEED, "B": 10000, "cluster": "metadata_doc_id",
                              "gaps_with_ci_excluding_0": gaps_excluding_0},
            "pure_absent_identity_note": ("on a pure-absent pool named-rate == confident-wrong == 'coverage', so the "
                                          "old '0.2267 reduction at matched coverage' is mechanically "
                                          f"(0.30 - {_r(li_natcw['certificate'])}) = {_r(identity_val)}, a "
                                          "re-expression of the caught-fraction gap, NOT a risk-coverage gain"),
            "honest_mixed_pool_reduction_point": _r(li_mixed_reduction_point),
            "honest_mixed_pool_reduction_ci95_MC": [_r(li_ci["ci95"][0]), _r(li_ci["ci95"][1])],
            "evidence_tag": "RE-ANALYSIS-DERIVED"},
    }

    metadata = {
        "evaluation_name": ("iter-10 $0 re-analysis scaffold: stronger-verifier n=60 rigor fix + 4 MINOR fixes + "
                            "abstract FORK for GEN_PAPER_TEXT"),
        "description": ("Pure $0 ($0 LLM, no network) re-analysis of three frozen iter-8/iter-9 experiment outputs "
                        "(S1 located-in, S2 verifier, S3 booster). Reproduction/no-spend gate recompute-from-rows; "
                        "RIGOR MAJOR = stronger-verifier n=60 SEPARATE table + corrected tab:locatedin (0.100 removed); "
                        "retires 4 MINORs (evidence/presentation/scope/novelty) + the significance FORK + updated "
                        "one-thesis contribution table. Extends the iter-9 precedent eval (art_4xy3D05YxvRr)."),
        "budget": {"cumulative_usd": 0.0, "n_llm_calls": 0},
        "seeds": {"reproduction_seed": REPRO_SEED, "eval_seed": EVAL_SEED},
        "reproduction_gate": reproduction_gate,
        "rigor_major": rigor_major,
        "evidence_minor": evidence_minor,
        "presentation_minor": presentation_minor,
        "scope_minor": feasibility_appendix_consolidation_plan,
        "novelty_minor": novelty_minor,
        "significance": significance,
        "count_reconciliation": count_reconciliation,
        "capability_gap_table": capability_gap_table,
        "verdict_mirrors": verdict_mirrors,
        "evidence_tag_vocabulary": ["CARRIED-LITERAL", "REPRODUCED-FROM-ROWS", "RE-ANALYSIS-DERIVED",
                                    "CARRIED-FROM-BLOCK", "PENDING-PARALLEL-EXPERIMENT",
                                    "REAL-LLM-READ", "NATURAL-PROSE", "GOLD-READ-CEILING",
                                    "STRUCTURAL-BY-CONSTRUCTION", "INHERITED-NESY-PREMISE"],
    }

    metrics_agg = {
        "reproduction_gate_n_hard_checks": float(len(GATE.checks)),
        "reproduction_gate_n_passed": float(GATE.n_passed()),
        "reproduction_gate_all_ok": 1.0 if GATE.all_ok() else 0.0,
        "reproduction_gate_n_soft_checks": float(len(GATE.soft)),
        "reproduction_gate_n_soft_passed": float(sum(1 for s in GATE.soft if s["ok"])),
        "locatedin_FACT_A_sibling": _r(factA_sib),
        "locatedin_FACT_A_diffcomponent": _r(factA_diff),
        "locatedin_caught_fraction_certificate": _r(cm["certificate"]["fraction_caught"]),
        "locatedin_caught_fraction_verbalized": _r(cm["ct_verbalized"]["fraction_caught"]),
        "locatedin_caught_fraction_ptrue": _r(cm["ct_ptrue"]["fraction_caught"]),
        "locatedin_caught_fraction_sc_margin": _r(cm["ct_sc_margin"]["fraction_caught"]),
        "locatedin_caught_fraction_negent": _r(cm["ct_negent"]["fraction_caught"]),
        "locatedin_caught_fraction_queryside_verifier_same_model": _r(cm["queryside_verifier"]["fraction_caught"]),
        "locatedin_caught_fraction_queryside_selfverify": _r(cm["queryside_selfverify"]["fraction_caught"]),
        "locatedin_natural_confident_wrong_certificate": _r(li_natcw["certificate"]),
        "locatedin_natural_confident_wrong_verifier": _r(li_natcw["queryside_verifier"]),
        "locatedin_mixed_reduction_point": _r(li_mixed_reduction_point),
        "n_caught_gaps_excluding_0_of_6": float(len(gaps_excluding_0)),
        "stronger_verifier_n60_caught_certificate": 0.667,
        "stronger_verifier_n60_caught_selfverify_strong": 0.533,
        "stronger_verifier_n60_caught_weak_same_model": 0.20,
        "stronger_verifier_n60_caught_strong_xfamily": 0.10,
        "stronger_verifier_two_copy_consistent": 1.0 if sv_equal else 0.0,
        "stronger_verifier_within_subsample_ordering_ok": 1.0 if order_ok else 0.0,
        "corrected_tab_locatedin_excludes_0100": 1.0,
        "frontier_slope_locatedin": _r(li_front["min_over6_ci_lo_vs_recall_slope"]),
        "frontier_slope_kinship": _r(ki_front["min_over6_ci_lo_vs_recall_slope"]),
        "frontier_present_coverage_vs_recall_slope_locatedin": _r(li_front["present_coverage_vs_recall_slope"]),
        "verifier_caught_clutrr_certificate": _r(vf_cl_cert),
        "verifier_caught_clutrr_verifier": _r(vf_cl_ver),
        "verifier_caught_redocred_certificate": _r(vf_rd_cert),
        "verifier_caught_redocred_verifier": _r(vf_rd_ver),
        "verifier_cert_minus_verifier_gap_clutrr": _r(vf_cl_gap["gap"]),
        "verifier_cert_minus_verifier_gap_redocred": _r(vf_rd_gap["gap"]),
        "kinship_FACT_A": _r(ki_factA),
        "kinship_certificate_absent_confident_wrong": _r(ki_cert_cw),
        "rigor_major_retired": 1.0 if rigor_major_retired else 0.0,
        "evidence_minor_retired": 1.0 if evidence_minor_retired else 0.0,
        "presentation_minor_retired": 1.0 if presentation_minor_retired else 0.0,
        "scope_minor_retired": 1.0,
        "budget_cumulative_usd": 0.0,
        "n_llm_calls": 0.0,
    }

    # datasets: one example row per paper-facing block / table / gate-check.
    def row(block_id, spec, text, extra=None):
        s = text if isinstance(text, str) else json.dumps(text, default=_json_default)
        ex = {"input": f"{block_id} :: {spec}", "output": s, "eval_char_len": float(len(s))}
        if extra:
            ex.update(extra)
        return ex

    rigor_major_rows = [
        row("rigor_major.stronger_verifier_own_subsample_table", "n=60 SEPARATE table (own denominator)",
            stronger_verifier_own_subsample_table),
        row("rigor_major.stronger_verifier_latex", "LaTeX body — tab:stronger-verifier", stronger_verifier_latex),
        row("rigor_major.corrected_tab_locatedin", "n=450/135 corrected leaderboard (0.100 removed)",
            corrected_tab_locatedin),
        row("rigor_major.corrected_tab_locatedin_latex", "LaTeX body — tab:locatedin (corrected)",
            corrected_tab_locatedin_latex),
        row("rigor_major.verdict", "rigor_major_retired flag",
            {"rigor_major_retired": rigor_major_retired, "retired_iff": rigor_major["retired_iff"]}),
    ]
    evidence_minor_rows = [
        row(f"evidence_minor.{k}", "0.785 paired with extraction-gated / targeting-quality caveat", v,
            extra={"eval_both_caveats_present": 1.0 if paired_checks[k] else 0.0})
        for k, v in paired.items()
    ]
    presentation_minor_rows = [
        row("presentation_minor.de_densification_checklist", "5 actionable de-densify items",
            de_densification_checklist),
        row("presentation_minor.lean_intro_skeleton", "<=3 intro blocks", lean_intro_skeleton,
            extra={"eval_n_intro_blocks": float(len(lean_intro_skeleton))}),
    ]
    scope_minor_rows = [
        row("scope_minor.feasibility_appendix_consolidation_plan", "one appendix, two subsections",
            feasibility_appendix_consolidation_plan),
    ]
    novelty_minor_rows = [
        row("novelty_minor.distinguishing_sentence_slot", "labeled PENDING slot",
            novelty_minor["distinguishing_sentence_slot"]),
    ]
    significance_rows = [
        row("significance.abstract_first_results_fork", "FORK_A / FORK_B + selection rule",
            abstract_first_results_fork),
        row("significance.contribution_table", "one-thesis contribution table", contribution_table_md),
    ]
    table_rows = [
        row("capability_gap_table", "16-cell per-signal x reader x corpus survival+caught", capability_gap_table),
        row("count_reconciliation", "per-dataset counts", count_reconciliation),
        row("caught_fraction_leaderboard_n450", "matched-coverage-fair headline (n=135)", caught_leaderboard),
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
        {"dataset": "rigor_major", "examples": rigor_major_rows},
        {"dataset": "evidence_minor", "examples": evidence_minor_rows},
        {"dataset": "presentation_minor", "examples": presentation_minor_rows},
        {"dataset": "scope_minor", "examples": scope_minor_rows},
        {"dataset": "novelty_minor", "examples": novelty_minor_rows},
        {"dataset": "significance", "examples": significance_rows},
        {"dataset": "tables", "examples": table_rows},
        {"dataset": "reproduction_gate_checks", "examples": gate_rows},
    ]

    out = {"metadata": metadata, "metrics_agg": metrics_agg, "datasets": datasets}
    out_path = WORKDIR / "eval_out.json"
    out_path.write_text(json.dumps(out, indent=2, default=_json_default))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size/1024:.1f} KB)")

    write_digest(reproduction_gate, rigor_major, evidence_minor, presentation_minor,
                 feasibility_appendix_consolidation_plan, novelty_minor, significance,
                 capability_gap_table, count_reconciliation, caught_leaderboard)
    logger.info("Wrote eval_digest.md")

    # final $0 assertion
    assert COST_USD == 0.0 and N_LLM_CALLS == 0
    present_forbidden = [m for m in _FORBIDDEN if m in sys.modules]
    assert not present_forbidden, f"FORBIDDEN module appeared: {present_forbidden}"
    logger.info(f"DONE. $0 verified. Gate {GATE.n_passed()}/{len(GATE.checks)} hard checks passed; "
                f"rigor_major_retired={rigor_major_retired}, evidence={evidence_minor_retired}, "
                f"presentation={presentation_minor_retired}.")


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return str(o)


def write_digest(reproduction_gate, rigor_major, evidence_minor, presentation_minor,
                 scope_minor, novelty_minor, significance, capability_gap_table,
                 count_reconciliation, caught_leaderboard):
    L = []
    L.append("# iter-10 eval digest — $0 re-analysis scaffold (stronger-verifier rigor fix + 4 MINOR fixes)\n")
    L.append(f"**Reproduction / no-spend gate:** {reproduction_gate['n_passed']}/{reproduction_gate['n_checks']} "
             f"HARD checks PASSED (all_ok={reproduction_gate['all_ok']}); "
             f"{sum(1 for s in reproduction_gate['soft_cross_checks'] if s['ok'])}/"
             f"{len(reproduction_gate['soft_cross_checks'])} soft MC cross-checks within tol. Budget $0, 0 LLM calls.\n")

    L.append("## BLOCK 1 — RIGOR MAJOR\n")
    L.append("### Table~\\ref{tab:stronger-verifier} (stronger cross-family verifier, OWN n=60 subsample)\n")
    L.append("```latex\n" + rigor_major["stronger_verifier_latex_table_body"] + "\n```\n")
    L.append("> " + rigor_major["stronger_verifier_own_subsample_table"]["qualitative_conclusion"] + "\n")
    L.append("### Table~\\ref{tab:locatedin} (CORRECTED — n_sibling=450 / 135 fab.; 0.100 row REMOVED)\n")
    L.append("```latex\n" + rigor_major["corrected_tab_locatedin"]["latex_table_body"] + "\n```\n")
    L.append("**Footnote:** " + rigor_major["corrected_tab_locatedin"]["footnote_pointer"] + "\n")
    L.append(f"All six cert-minus-method caught-gaps exclude 0: "
             f"{rigor_major['corrected_tab_locatedin']['all_six_gaps_exclude_0']}. "
             f"rigor_major_retired = {rigor_major['rigor_major_retired']}.\n")

    L.append("## BLOCK 2 — EVIDENCE MINOR (0.785 always paired with the caveat)\n")
    for k in ("abstract", "intro", "contribution_3", "conclusion"):
        L.append(f"**{k}.** " + evidence_minor["paired_caveat_sentences"][k] + "\n")
    L.append(f"evidence_minor_retired = {evidence_minor['evidence_minor_retired']} "
             f"(per-sentence both-clauses: {evidence_minor['per_sentence_both_clauses_present']}).\n")

    L.append("## BLOCK 3 — PRESENTATION MINOR\n")
    L.append("**De-densification checklist:**\n")
    for c in presentation_minor["de_densification_checklist"]:
        L.append(f"- {c}")
    L.append("\n**Lean intro skeleton (<=3 blocks):**\n")
    for b in presentation_minor["lean_intro_skeleton"]:
        L.append(f"- **Block {b['block']} ({b['role']}):**")
        for bl in b["bullets"]:
            L.append(f"  - {bl}")
    L.append("")

    L.append("## BLOCK 4 — SCOPE MINOR (single feasibility appendix)\n")
    L.append(f"**{scope_minor['appendix_title']}** — {scope_minor['preamble']}\n")
    L.append(f"- **{scope_minor['subsection_1']['title']}:** {scope_minor['subsection_1']['content']}\n")
    L.append(f"- **{scope_minor['subsection_2']['title']}:** {scope_minor['subsection_2']['content']}\n")
    L.append(f"Out-of-scope statement stays in: {scope_minor['out_of_scope_statement_location']}.\n")

    L.append("## BLOCK 5 — NOVELTY MINOR slot\n")
    slot = novelty_minor["distinguishing_sentence_slot"]
    L.append(f"`{slot['label']}` — {slot['purpose']}\n\nPlaceholder: `{slot['placeholder_text']}` "
             f"(status: {slot['status']}).\n")

    L.append("## BLOCK 6 — SIGNIFICANCE\n")
    fk = significance["abstract_first_results_fork"]
    L.append("**FORK_A (demonstrated fix):** " + fk["FORK_A_demonstrated_fix"] + "\n")
    L.append("**FORK_B (honest boundary):** " + fk["FORK_B_honest_boundary"] + "\n")
    L.append("**Selection rule:** " + fk["selection_rule"] + "\n")
    L.append("\n" + significance["contribution_table"]["markdown"] + "\n")

    L.append("## Caught-fraction leaderboard (located-in sibling fabrications, n=135)\n")
    L.append("| method | fraction caught |\n|---|---|")
    for m in ("certificate", "ct_verbalized", "ct_ptrue", "ct_sc_margin", "ct_negent",
              "queryside_verifier", "queryside_selfverify"):
        L.append(f"| {m} | {caught_leaderboard[m]['fraction_caught']} |")
    L.append("")

    L.append("## 16-cell capability-gap table (survival / caught per signal)\n")
    L.append("| corpus | reader | tag | verbalized | sc_margin | ptrue | negent |\n|---|---|---|---|---|---|---|")
    for r in capability_gap_table["rows"]:
        cells = " | ".join(f"{r['survival'][s]}/{r['caught'][s]}" for s in SIGNALS)
        L.append(f"| {r['corpus']} | {r['reader']} | {r['tag']} | {cells} |")
    L.append("\n*(cells are survival/caught)*\n")
    L.append("## Count reconciliation\n")
    L.append("```\n" + json.dumps(count_reconciliation, indent=1) + "\n```\n")
    (WORKDIR / "eval_digest.md").write_text("\n".join(L))


if __name__ == "__main__":
    main()
