#!/usr/bin/env python3
"""iter-8 experiment_2 -- the reviewer-mandated DISCONFIRM test for the closure-certificate paper.

Question (the reviewer's explicit ask): is the no-derivation closure CERTIFICATE's
hallucination-safety on the absent-relation stratum just a re-skin of a *query-side
false-premise verifier* the LLM could run directly?  ("Are X and Y related at all?")
If a cheap query-side verifier (or a self-verification pass) MATCHES/BEATS the structural
certificate, the certificate is not strictly needed -- an honest negative.  If the
certificate still beats it, the structural signal is necessary.

This artifact is REUSE-HEAVY.  The certificate / raw / 4-signal-battery predictions ALREADY
EXIST, fully cached, in two prediction pools:
  * CLUTRR    battery  (iter-6 / gen_art_experiment_1)  -- templated kinship, gemini reader
  * Re-DocRED battery  (iter-7 / gen_art_experiment_1)  -- natural Wikipedia kinship, gemini reader
Both pools are loaded by direct filesystem read.  The ONLY new LLM spend is the query-side
VERIFIER + a SELF-VERIFY pass (reader-matched gemini; est. <$1, hard cap $9 via llm.py).

Pipeline:
  PHASE 0  workspace / clients
  PHASE 1  load + normalise both pools (exclude the non-kinship spatial RCC-8 group);
           reconstruct the EXACT source record ORDER (so tie-break-sensitive matched-coverage
           numbers reproduce byte-exactly) and the FULL story text for the verifier prompts.
  PHASE 2  $0 REPRODUCTION GATE -- re-derive FACT-A / certificate leaderboard / crux survival
           from the carried row fields and assert they match each pool's own aggregates AND
           the published constants.  Hard-stop (no spend) on a structural mismatch.
  PHASE 3  build + run the NEW verifier + self-verify items (sha256-cached, cost-guarded).
  PHASE 4  parse -> per-row corrective-gate / sensitivity / self-verify method predictions.
  PHASE 5  matched-coverage leaderboards per venue (certificate vs the 4 signals vs the verifier
           vs self-verify), doc-clustered paired bootstrap B=10000, Holm-adjusted.
  PHASE 6  fraction-caught crux tables (threshold-free for the corrective gates).
  PHASE 7  per-venue + overall CERTIFICATE-NECESSITY verdict.
  PHASE 8  emit method_out.json (exp_gen_sol_out), validated, with mini/preview.

Reused VERBATIM from iter-6/iter-7: llm.py, stats.py, baselines.py, kinship.py,
clutrr_composition_table.json.  No edits -- imported.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import math
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
from loguru import logger

import baselines as B
from kinship import Kinship
from llm import OpenRouterClient, BudgetExceeded, _first_json_block
from stats import holm_bonferroni, matched_coverage_mask, selective_accuracy

# --------------------------------------------------------------------------- #
# Paths / constants
# --------------------------------------------------------------------------- #
HERE = Path(__file__).resolve().parent
RUN = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop")
CLUTRR_POOL = RUN / "iter_6/gen_art/gen_art_experiment_1/method_out.json"      # art_LeRQRGHJZcdQ
REDOCRED_POOL = RUN / "iter_7/gen_art/gen_art_experiment_1/method_out.json"    # art_htcr8yOZLCQy
ITER3_POOL = RUN / "iter_3/gen_art/gen_art_experiment_1/method_out.json"       # CLUTRR record order
REDOCRED_DATASET = RUN / "iter_6/gen_art/gen_art_dataset_1/full_data_out.json"  # re-docred/docred order + full text
COMP_TABLE = HERE / "clutrr_composition_table.json"

PRIMARY_MODEL = "google/gemini-3.1-flash-lite"   # reader-matched verifier (both pools read by gemini)
CROSS_MODEL = "deepseek/deepseek-v3.2"           # verifier-model robustness sensitivity (not reader-matched)
FALLBACKS = ["google/gemini-3-flash-preview"]
DEEPSEEK_FALLBACKS = ["deepseek/deepseek-chat-v3", "google/gemini-3.1-flash-lite"]

PUBLISHED_FACT_A = {("clutrr", "gemini"): 0.472, ("clutrr", "deepseek"): 0.483,
                    ("redocred", "gemini"): 0.326, ("redocred", "deepseek"): 0.318}

SIGNALS = ("verbalized", "sc_margin", "ptrue", "negent")
B_BOOT = 10000
SEED = 20260618
ALPHA = 0.05
TOL = 5e-3
ABSTAIN_TOKENS = {"ABSTAIN", "no-relation", "none", "None", "", None}

VERIFIER_SYS = (
    "You judge whether two named people are connected by ANY family/kinship relationship "
    "(directly stated OR derivable through a chain of relatives) according ONLY to the given "
    'text. Output ONLY a JSON object {"related": "RELATED" or "UNRELATED", "confidence": <number '
    "between 0 and 1>}. confidence is your probability that your RELATED/UNRELATED judgement is "
    "correct. Do not output anything except the JSON object."
)
SELFVERIFY_SYS = (
    "You verify a claimed family relationship against a text. Output ONLY a JSON object "
    '{"verdict": "TRUE" or "FALSE", "confidence": <number between 0 and 1>}. verdict is TRUE iff '
    "the claim is actually correct given the text; confidence is your probability that your "
    "verdict is correct. Do not output anything except the JSON object."
)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(HERE / "logs" / "run.log", rotation="20 MB", level="DEBUG")

KIN = Kinship(json.loads(COMP_TABLE.read_text()))


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #
def _r(x, nd=4):
    try:
        if x != x:
            return float("nan")
        return round(float(x), nd)
    except (TypeError, ValueError):
        return x


def named_of(pred) -> bool:
    """A method NAMES a relation iff its prediction string is a real relation token."""
    return pred not in ABSTAIN_TOKENS


def clip01(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return 0.5
    if v != v:
        return 0.5
    return max(0.0, min(1.0, v))


def primitive_key(rec, predstr):
    """Comparison key for a prediction string at the venue's scoring level.

    CLUTRR scores at SURFACE level (gold is the gendered word); Re-DocRED/DocRED score at
    PRIMITIVE level (gender is best-effort) -- map the gendered word to its gender-independent
    primitive via the kinship surface->type table, exactly as the source `primitivize` did."""
    if not named_of(predstr):
        return None
    if rec["scoring"] == "surface":
        return predstr
    m = KIN.surface_to_type(predstr)
    return m[0] if m else str(predstr).lower()


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, set):
        return sorted(o)
    return str(o)


# --------------------------------------------------------------------------- #
# PHASE 1: load + normalise both cached pools
# --------------------------------------------------------------------------- #
def _strip_q(text):
    """Pool `input` is `story[:1200] + '  || Q: ...'`; strip the trailing question marker."""
    i = text.find("  || Q:")
    return text[:i] if i >= 0 else text


def _collect_rows(pool_obj):
    """Walk the exp_gen_sol_out `datasets` and return every (example, dataset_name) row."""
    out = []
    for ds in pool_obj["datasets"]:
        name = ds.get("dataset")
        for ex in ds.get("examples", []):
            out.append((ex, name))
    return out


def load_pool(path: Path, pool_name: str):
    """Load one cached pool into normalised per-query records.

    EXCLUDES the non-kinship spatial RCC-8 group in the CLUTRR pool (its rows carry no
    metadata_raw_named / metadata_qsrc and have RCC-8 outputs -- not a kinship verifier case)."""
    obj = json.loads(path.read_text())
    md = obj["metadata"]
    rows = _collect_rows(obj)
    recs = []
    skipped_spatial = 0
    for ex, dsname in rows:
        # field discriminator: a kinship row carries a boolean raw_named + a query source name.
        if ex.get("metadata_raw_named") is None or "metadata_qsrc" not in ex:
            skipped_spatial += 1
            continue
        is_absent = bool(ex["metadata_is_absent"])
        slice_name = ex.get("metadata_slice") or pool_name  # CLUTRR rows lack metadata_slice
        if pool_name == "clutrr":
            slice_name = "clutrr"
            qsrc_name = str(ex["metadata_qsrc"])
            qtgt_name = str(ex["metadata_qtgt"])
            scoring = "surface"
            gold_key = "no-relation" if is_absent else ex["output"]
            doc_text = _strip_q(ex["input"])
        else:
            qsrc_name = str(ex.get("metadata_qsrc_name") or ex.get("metadata_qsrc"))
            qtgt_name = str(ex.get("metadata_qtgt_name") or ex.get("metadata_qtgt"))
            scoring = "primitive"
            gold_key = "no-relation" if is_absent else ex.get("metadata_gold_primitive")
            doc_text = _strip_q(ex["input"])  # replaced by full prose in build_order_and_text
        raw_named = bool(ex["metadata_raw_named"])
        raw_answer = ex.get("predict_commit_argmax") if raw_named else None
        rec = {
            "pool": pool_name, "slice": slice_name, "reader": "gemini",
            "is_absent": is_absent, "stratum": ex.get("metadata_stratum"),
            "doc_id": ex.get("metadata_doc_id"),
            "qsrc_id": ex.get("metadata_qsrc"), "qtgt_id": ex.get("metadata_qtgt"),
            "qsrc_name": qsrc_name, "qtgt_name": qtgt_name,
            "gold": ex["output"], "gold_primitive": ex.get("metadata_gold_primitive"),
            "gold_key": gold_key, "scoring": scoring,
            "raw_named": raw_named, "raw_answer": raw_answer,
            "conf": {s: float(ex.get(f"metadata_conf_{s}", 0.0) or 0.0) for s in SIGNALS},
            "predict_certificate": ex.get("predict_certificate"),
            "predict_certificate_goldread": ex.get("predict_certificate_goldread"),
            "predict_commit_argmax": ex.get("predict_commit_argmax"),
            "predict_conf_thresh": {s: ex.get(f"predict_conf_thresh_{s}") for s in SIGNALS},
            "predict_pot": ex.get("predict_pot"), "predict_sc": ex.get("predict_sc"),
            "doc_text": doc_text, "order_index": 10 ** 9,
        }
        recs.append(rec)
    logger.info(f"[{pool_name}] loaded {len(recs)} kinship records "
                f"(skipped {skipped_spatial} non-kinship/spatial rows)")
    return recs, md


def build_order_and_text(recs):
    """Reconstruct each record's EXACT source-pool position in the `records` list used by the
    iter-6/iter-7 matched-coverage showdown (so heavily-tied conf=1.0 baselines reproduce
    byte-exactly), and attach the FULL story text for the verifier prompt.

    * CLUTRR order  = the iter-3 pool row order (iter-6 rebuilt records in that order).
    * Re-DocRED/DocRED order = the dataset document order, present-queries then absent-pairs
      per doc (dataio_redocred.build_records), keyed on (doc_id, src, tgt, is_absent).
      The dataset `input` also supplies the full (untruncated) prose for the verifier."""
    # ---- CLUTRR order from the iter-3 pool ----
    clutrr_order = {}
    if ITER3_POOL.exists():
        it3 = json.loads(ITER3_POOL.read_text())
        gi = 0
        for ds in it3["datasets"]:
            for ex in ds["examples"]:
                key = (ex["metadata_doc_id"], ex["metadata_qsrc"], ex["metadata_qtgt"],
                       bool(ex["metadata_is_absent"]))
                if key not in clutrr_order:
                    clutrr_order[key] = gi
                    gi += 1
    else:
        logger.warning("ITER3 pool missing -> CLUTRR falls back to present-then-absent order")

    # ---- Re-DocRED/DocRED order + full text from the dataset ----
    redoc_order = {}      # (slice, doc_id_full, src, tgt, is_absent) -> global idx within slice
    full_text = {}        # (slice, doc_id_full) -> full prose
    if REDOCRED_DATASET.exists():
        ds_obj = json.loads(REDOCRED_DATASET.read_text())
        for d in ds_obj["datasets"]:
            slice_name = d["dataset"]
            if slice_name not in ("re-docred", "docred"):
                continue
            gi = 0
            for ex in d["examples"]:
                gg = json.loads(ex["output"])
                if not (gg.get("query_edges") or gg.get("absent_relation_pairs")):
                    continue
                did = f"{slice_name}::{ex['metadata_doc_id']}"
                full_text[(slice_name, did)] = ex["input"]
                for q in gg.get("query_edges", []):
                    redoc_order[(slice_name, did, q["source"], q["target"], False)] = gi
                    gi += 1
                for p in gg.get("absent_relation_pairs", []):
                    redoc_order[(slice_name, did, p["source"], p["target"], True)] = gi
                    gi += 1
    else:
        logger.warning("Re-DocRED dataset missing -> redocred order/full-text fallback")

    miss_order = 0
    for rec in recs:
        if rec["pool"] == "clutrr":
            key = (rec["doc_id"], rec["qsrc_id"], rec["qtgt_id"], rec["is_absent"])
            rec["order_index"] = clutrr_order.get(key, 10 ** 9)
            if key not in clutrr_order:
                miss_order += 1
        else:
            sl = rec["slice"]
            key = (sl, rec["doc_id"], rec["qsrc_id"], rec["qtgt_id"], rec["is_absent"])
            rec["order_index"] = redoc_order.get(key, 10 ** 9)
            if key not in redoc_order:
                miss_order += 1
            ft = full_text.get((sl, rec["doc_id"]))
            if ft:
                rec["doc_text"] = ft  # full untruncated prose (reader saw this)
    if miss_order:
        logger.warning(f"{miss_order} records missing from order maps (fell back to stored order)")
    return clutrr_order, redoc_order


# --------------------------------------------------------------------------- #
# Per-method (named, surface-key, conf) reconstruction
# --------------------------------------------------------------------------- #
def build_base_methods(rec):
    """Reconstruct the certificate / 4-signal / commit-argmax method dicts from the carried
    row fields, with the SAME (named, surface-key, conf) semantics as the source records."""
    m = {}
    cert = rec["predict_certificate"]
    m["certificate"] = {"named": named_of(cert), "surf": primitive_key(rec, cert),
                        "conf": 1.0 if named_of(cert) else 0.0, "pred": cert if named_of(cert) else "no-relation"}
    raw = rec["raw_answer"]
    raw_named = rec["raw_named"]
    raw_surf = primitive_key(rec, raw) if raw_named else None
    for s in SIGNALS:
        m[f"ct_{s}"] = {"named": raw_named, "surf": raw_surf, "conf": rec["conf"][s],
                        "pred": rec["predict_conf_thresh"][s]}
    # commit_argmax ranks by the raw answerer's own (verbalized) confidence (== source semantics)
    m["commit_argmax"] = {"named": raw_named, "surf": raw_surf, "conf": rec["conf"]["verbalized"],
                          "pred": rec["predict_commit_argmax"]}
    rec["M"] = m


def attach_verifier_methods(rec):
    """Build the NEW query-side methods from the parsed verifier / self-verify outputs."""
    raw = rec["raw_answer"]
    raw_named = rec["raw_named"]
    raw_surf = primitive_key(rec, raw) if raw_named else None

    # ---- query-side false-premise VERIFIER (corrective gate, PRIMARY) ----
    v = rec["verifier"]
    related, p_related = v["related"], v["p_related"]
    vetoed = (related is False)
    qv_named = raw_named and (not vetoed)
    rec["M"]["queryside_verifier"] = {
        "named": qv_named, "surf": raw_surf if qv_named else None,
        "conf": p_related, "pred": (raw if qv_named else "no-relation")}
    # ---- verifier as a pure ABSTENTION SIGNAL (sensitivity, commit raw, rank by p_related) ----
    rec["M"]["verifier_as_signal"] = {
        "named": raw_named, "surf": raw_surf, "conf": p_related,
        "pred": (raw if raw_named else "no-relation")}
    # ---- SELF-VERIFICATION of the raw committed answer ----
    sv = rec["selfverify"]
    if raw_named and sv["verdict"] is not None:
        sv_named = sv["verdict"] is True
        rec["M"]["queryside_selfverify"] = {
            "named": (raw_named and sv_named), "surf": raw_surf if (raw_named and sv_named) else None,
            "conf": sv["conf"], "pred": (raw if (raw_named and sv_named) else "no-relation")}
    else:
        # raw abstained (nothing to self-verify) OR parse fail -> keep raw decision (no veto)
        rec["M"]["queryside_selfverify"] = {
            "named": raw_named, "surf": raw_surf, "conf": (sv["conf"] if raw_named else 0.5),
            "pred": (raw if raw_named else "no-relation")}
    # ---- deepseek-verifier robustness sensitivity (optional) ----
    if rec.get("verifier_ds") is not None:
        vd = rec["verifier_ds"]
        vetoed_d = (vd["related"] is False)
        qvd_named = raw_named and (not vetoed_d)
        rec["M"]["queryside_verifier_dsv"] = {
            "named": qvd_named, "surf": raw_surf if qvd_named else None,
            "conf": vd["p_related"], "pred": (raw if qvd_named else "no-relation")}


# --------------------------------------------------------------------------- #
# Array extraction + venue analysis
# --------------------------------------------------------------------------- #
def method_arrays(records, m):
    named = np.array([r["M"][m]["named"] for r in records], bool)
    conf = np.array([B.coverage_confidence(r["M"][m]["named"], r["M"][m]["conf"]) for r in records], float)
    correct = np.array([B.query_correct(r["M"][m]["named"], r["M"][m]["surf"], r["gold_key"], r["is_absent"])
                        for r in records], float)
    cw = np.array([B.confident_wrong(r["M"][m]["named"], r["M"][m]["surf"], r["gold_key"], r["is_absent"])
                   for r in records], float)
    return named, conf, correct, cw


def clustered_cw_reduction(cw_ref, mask_ref, cw_cmp, mask_cmp, doc_ids, n_boot=B_BOOT, seed=SEED):
    """Doc-clustered paired bootstrap of the confident-wrong reduction (compare - ref) at
    matched coverage (pool-fraction confident-wrong, fixed masks). Mirrors iter-7 cw_matched_to_ref:
    positive reduction => the certificate keeps FEWER confident-wrong answers than `compare`."""
    N = len(cw_ref)
    ref_rate = float((cw_ref * mask_ref).sum() / N) if N else float("nan")
    cmp_rate = float((cw_cmp * mask_cmp).sum() / N) if N else float("nan")
    by_doc = defaultdict(list)
    for i, d in enumerate(doc_ids):
        by_doc[d].append(i)
    docs = list(by_doc)
    nd = len(docs)
    rng = np.random.default_rng(seed)
    diffs = []
    for _ in range(n_boot):
        pick = rng.integers(0, nd, nd)
        idx = np.concatenate([by_doc[docs[i]] for i in pick]) if nd else np.array([], int)
        if len(idx) == 0:
            continue
        n = len(idx)
        d_ref = float((cw_ref[idx] * mask_ref[idx]).sum() / n)
        d_cmp = float((cw_cmp[idx] * mask_cmp[idx]).sum() / n)
        diffs.append(d_cmp - d_ref)
    diffs = np.array(diffs, float)
    if len(diffs) < 10:
        return {"reduction": _r(cmp_rate - ref_rate), "ci95": [float("nan"), float("nan")],
                "p_one_sided": float("nan"), "ref_confident_wrong": _r(ref_rate),
                "compare_confident_wrong": _r(cmp_rate), "n_boot": int(len(diffs))}
    lo, hi = np.quantile(diffs, [ALPHA / 2, 1 - ALPHA / 2])
    p_one = max(float(np.mean(diffs <= 0.0)), 1.0 / (len(diffs) + 1))
    return {"reduction": _r(cmp_rate - ref_rate), "ci95": [_r(lo), _r(hi)], "p_one_sided": _r(p_one),
            "ref_confident_wrong": _r(ref_rate), "compare_confident_wrong": _r(cmp_rate),
            "ci_excludes_0": bool(lo > 0.0), "n_boot": int(len(diffs))}


def venue_leaderboard(records, methods, label, ref="certificate"):
    """Matched-coverage showdown for one venue (pool x stratum). Every non-ref method is
    thresholded to the certificate's natural coverage c* by ranking on its abstention
    confidence; selective accuracy + confident-wrong rate among the covered set + doc-clustered
    paired bootstrap (selacc gap AND confident-wrong reduction), Holm-adjusted per venue."""
    N = len(records)
    if N == 0:
        return {"label": label, "n": 0}
    doc_ids = [r["doc_id"] for r in records]
    ref_named, ref_conf, ref_correct, ref_cw = method_arrays(records, ref)
    cstar = float(ref_named.mean())
    mask_ref = ref_named
    sel_ref = selective_accuracy(ref_correct, mask_ref)
    cov_ref = int(mask_ref.sum())
    cw_ref_covered = float(ref_cw[mask_ref].mean()) if cov_ref else float("nan")
    lb = {ref: {"coverage": _r(cstar), "selective_accuracy": _r(sel_ref),
                "confident_wrong_rate_among_covered": _r(cw_ref_covered),
                "n_covered": cov_ref, "tag": "REAL-LLM-READ"}}
    selacc_p, cw_p = {}, {}
    for m in methods:
        if m == ref or m not in records[0]["M"]:
            continue
        named, conf, correct, cw = method_arrays(records, m)
        mask = matched_coverage_mask(conf, cstar)
        cov = int(mask.sum())
        sel = selective_accuracy(correct, mask)
        cw_cov = float(cw[mask].mean()) if cov else float("nan")
        gap = B.doc_clustered_paired_gap(ref_correct, mask_ref, correct, mask, doc_ids,
                                         B=B_BOOT, seed=SEED, alpha=ALPHA)
        cwr = clustered_cw_reduction(ref_cw, mask_ref, cw, mask, doc_ids)
        lb[m] = {"coverage_matched": _r(float(mask.mean())), "natural_coverage": _r(float(named.mean())),
                 "selective_accuracy": _r(sel), "confident_wrong_rate_among_covered": _r(cw_cov),
                 "n_covered": cov,
                 "selacc_gap_cert_minus_method": _r(gap["gap"]), "selacc_gap_ci95": gap["ci95"],
                 "selacc_gap_p_one_sided": gap["p_one_sided"],
                 "cw_reduction_cert_vs_method": cwr["reduction"], "cw_reduction_ci95": cwr["ci95"],
                 "cw_reduction_p_one_sided": cwr["p_one_sided"], "tag": "REAL-LLM-READ"}
        selacc_p[m] = gap["p_one_sided"]
        cw_p[m] = cwr["p_one_sided"]
    holm_sel = holm_bonferroni(selacc_p)
    holm_cw = holm_bonferroni(cw_p)
    for m in lb:
        if m == ref:
            continue
        lb[m]["selacc_gap_holm"] = holm_sel.get(m, {})
        lb[m]["cw_reduction_holm"] = holm_cw.get(m, {})
    return {"label": label, "n": N, "c_star": _r(cstar), "ref": ref, "leaderboard": lb,
            "holm_selacc_family": holm_sel, "holm_cw_family": holm_cw}


# --------------------------------------------------------------------------- #
# PHASE 2: $0 reproduction gate
# --------------------------------------------------------------------------- #
def _signal_mixed_selacc(mixed_sorted, signal):
    """Reproduce one confidence signal's matched-coverage mixed selective accuracy."""
    ref_named, _, _, _ = method_arrays(mixed_sorted, "certificate")
    cstar = float(ref_named.mean())
    conf = np.array([B.coverage_confidence(r["raw_named"], r["conf"][signal]) for r in mixed_sorted], float)
    mask = matched_coverage_mask(conf, cstar)
    correct = np.array([B.query_correct(r["raw_named"], primitive_key(r, r["raw_answer"]),
                                        r["gold_key"], r["is_absent"]) for r in mixed_sorted], float)
    return selective_accuracy(correct, mask)


def _crux_frac_surviving(records, signal):
    """frac of the FACT-A absent hallucinations whose signal >= the absent-pool median
    (== the source crux `frac_surviving_certificate_matched_rule` value)."""
    absent = [r for r in records if r["is_absent"]]
    halluc = [r for r in absent if r["raw_named"]]
    if not halluc:
        return float("nan")
    pool_med = float(np.median([r["conf"][signal] for r in absent]))
    vals = np.array([r["conf"][signal] for r in halluc], float)
    return float(np.mean(vals >= pool_med))


def reproduction_gate(clutrr_recs, clutrr_md, redoc_recs, redoc_md):
    """Re-derive the published literals from the carried row fields and assert they match the
    pool's OWN aggregates AND the published constants. Returns (report, all_ok)."""
    checks = []

    def chk(name, recomputed, carried, published=None, tol=TOL):
        ok = (recomputed == recomputed) and abs(recomputed - carried) <= tol
        if published is not None:
            ok = ok and abs(recomputed - published) <= tol
        checks.append({"name": name, "recomputed": _r(recomputed, 6), "carried": _r(carried, 6),
                       "published": (None if published is None else _r(published, 6)), "tol": tol, "ok": bool(ok)})
        return ok

    # ===== CLUTRR (gemini reader) =====
    cl_present = [r for r in clutrr_recs if not r["is_absent"]]
    cl_absent = [r for r in clutrr_recs if r["is_absent"]]
    cl_mixed = sorted(cl_present + cl_absent, key=lambda r: r["order_index"])
    chk("clutrr.count_present", len(cl_present), 102, 102, tol=0)
    chk("clutrr.count_absent", len(cl_absent), 180, 180, tol=0)
    fa_cl = float(np.mean([1.0 if r["raw_named"] else 0.0 for r in cl_absent]))
    chk("clutrr.gemini.FACT_A", fa_cl, clutrr_md["crux_confidence_survival_table"]["raw_hallucination_rate_absent"],
        PUBLISHED_FACT_A[("clutrr", "gemini")])
    cw_cl = float(np.mean([1.0 if named_of(r["predict_certificate"]) else 0.0 for r in cl_absent]))
    chk("clutrr.gemini.cert_confident_wrong_absent", cw_cl,
        clutrr_md["crux_confidence_survival_table"]["certificate_confident_wrong_absent"], 0.0278)
    # certificate mixed selacc (order-independent)
    rn, _, rc, _ = method_arrays(cl_mixed, "certificate")
    cstar_cl = float(rn.mean())
    chk("clutrr.gemini.cert_mixed_cstar", cstar_cl,
        clutrr_md["leaderboard_mixed"]["view3_matched_coverage_showdown"]["c_star"], 0.26595744680851063)
    chk("clutrr.gemini.cert_mixed_selacc", selective_accuracy(rc, rn),
        clutrr_md["leaderboard_mixed"]["view3_matched_coverage_showdown"]["leaderboard"]["modeA"]["selective_accuracy"],
        0.8267)
    cl_carried_lb = clutrr_md["leaderboard_mixed"]["view3_matched_coverage_showdown"]["leaderboard"]
    for s in SIGNALS:
        chk(f"clutrr.gemini.signal_mixed_selacc.{s}", _signal_mixed_selacc(cl_mixed, s),
            cl_carried_lb[f"ct_{s}"]["selective_accuracy"])
    cl_crux = clutrr_md["crux_confidence_survival_table"]["per_signal"]
    for s in SIGNALS:
        chk(f"clutrr.gemini.crux_surviving.{s}", _crux_frac_surviving(clutrr_recs, s),
            cl_crux[f"ct_{s}"]["frac_surviving_certificate_matched_rule"])
    # CLUTRR deepseek FACT-A reproduced from the carried cross-family aggregate (no per-row data)
    chk("clutrr.deepseek.FACT_A_carried_vs_published",
        clutrr_md["cross_family_sensitivity"]["raw_hallucination_rate_absent"],
        clutrr_md["cross_family_sensitivity"]["raw_hallucination_rate_absent"],
        PUBLISHED_FACT_A[("clutrr", "deepseek")])

    # ===== Re-DocRED (gemini reader) =====
    rd_present = [r for r in redoc_recs if r["slice"] == "re-docred" and not r["is_absent"]]
    rd_absent = [r for r in redoc_recs if r["slice"] == "re-docred" and r["is_absent"]]
    rd_mixed = sorted(rd_present + rd_absent, key=lambda r: r["order_index"])
    chk("redocred.count_present", len(rd_present), 360, 360, tol=0)
    chk("redocred.count_absent", len(rd_absent), 368, 368, tol=0)
    prr = redoc_md["primary_reader_results"]
    fa_rd = float(np.mean([1.0 if r["raw_named"] else 0.0 for r in rd_absent]))
    chk("redocred.gemini.FACT_A", fa_rd, prr["crux_survival_table"]["raw_hallucination_rate_absent"],
        PUBLISHED_FACT_A[("redocred", "gemini")])
    cw_rd = float(np.mean([1.0 if named_of(r["predict_certificate"]) else 0.0 for r in rd_absent]))
    chk("redocred.gemini.cert_confident_wrong_absent", cw_rd,
        prr["crux_survival_table"]["certificate_confident_wrong_absent"], 0.0707)
    rn2, _, rc2, _ = method_arrays(rd_mixed, "certificate")
    cstar_rd = float(rn2.mean())
    chk("redocred.gemini.cert_mixed_cstar", cstar_rd,
        prr["view3_mixed_showdown"]["leaderboard"]["modeA"]["coverage"], 0.27472527472527475)
    chk("redocred.gemini.cert_mixed_selacc", selective_accuracy(rc2, rn2),
        prr["view3_mixed_showdown"]["leaderboard"]["modeA"]["selective_accuracy"], 0.475)
    rd_carried_lb = prr["view3_mixed_showdown"]["leaderboard"]
    for s in SIGNALS:
        chk(f"redocred.gemini.signal_mixed_selacc.{s}", _signal_mixed_selacc(rd_mixed, s),
            rd_carried_lb[f"ct_{s}"]["selective_accuracy"])
    rd_crux = prr["crux_survival_table"]["per_signal"]
    for s in SIGNALS:
        chk(f"redocred.gemini.crux_surviving.{s}", _crux_frac_surviving(rd_present + rd_absent, s),
            rd_crux[f"ct_{s}"]["frac_surviving_certificate_matched_rule"])
    # present coverage + absent abstention (decomposition; order-independent)
    decomp = redoc_md["abstention_decomposition"]
    pres_cov = float(np.mean([1.0 if named_of(r["predict_certificate"]) else 0.0 for r in rd_present]))
    chk("redocred.gemini.present_coverage_llm_read", pres_cov, decomp["present_coverage_llm_read"], 0.4833)
    abst_rate = float(np.mean([1.0 if not named_of(r["predict_certificate"]) else 0.0 for r in rd_absent]))
    chk("redocred.gemini.correct_absent_abstention_rate", abst_rate, decomp["correct_absent_abstention_rate"], 0.9293)
    # Re-DocRED deepseek FACT-A reproduced from carried cross-family aggregate
    chk("redocred.deepseek.FACT_A_carried_vs_published",
        redoc_md["cross_family_sensitivity"]["FACT_A_raw_absent_hallucination_rate"],
        redoc_md["cross_family_sensitivity"]["FACT_A_raw_absent_hallucination_rate"],
        PUBLISHED_FACT_A[("redocred", "deepseek")])

    all_ok = all(c["ok"] for c in checks)
    n_ok = sum(1 for c in checks if c["ok"])
    report = {"all_ok": bool(all_ok), "n_checks": len(checks), "n_passed": n_ok,
              "tolerance": TOL, "checks": checks,
              "note": ("All certificate/FACT-A/crux numbers are order-independent and reproduce exactly; "
                       "the signal mixed selective-accuracies are tie-break sensitive (heavy conf=1.0 ties) "
                       "and reproduce exactly only after the source record order is reconstructed "
                       "(CLUTRR<-iter-3 row order; Re-DocRED<-dataset doc order).")}
    return report, all_ok


# --------------------------------------------------------------------------- #
# PHASE 3: build verifier / self-verify LLM items
# --------------------------------------------------------------------------- #
def build_items(records, tag_suffix=""):
    """One verifier item per record; one self-verify item per record whose raw answerer
    committed a real relation. doc_text capped to bound tokens (stories are short anyway)."""
    ver_items, sv_items = [], []
    for i, rec in enumerate(records):
        txt = (rec["doc_text"] or "")[:4000]
        rid = f"{rec['pool']}::{rec['slice']}::{i}"
        ver_items.append({
            "id": f"ver{tag_suffix}::{rid}", "tag": "verifier", "max_tokens": 60, "temperature": 0.0,
            "system": VERIFIER_SYS,
            "user": (f"Text:\n{txt}\n\nQuestion: Are {rec['qsrc_name']} and {rec['qtgt_name']} related by "
                     f"family/kinship at all (directly stated or via any chain of relatives described in the "
                     f"text)? Answer with the JSON object only."),
            "_rec": i})
        if rec["raw_named"] and named_of(rec["raw_answer"]):
            sv_items.append({
                "id": f"sv{tag_suffix}::{rid}", "tag": "selfverify", "max_tokens": 60, "temperature": 0.0,
                "system": SELFVERIFY_SYS,
                "user": (f"Text:\n{txt}\n\nClaim: {rec['qtgt_name']} is {rec['qsrc_name']}'s "
                         f"{rec['raw_answer']}. Is this claim actually true given the text? Answer with the "
                         f"JSON object only."),
                "_rec": i})
    return ver_items, sv_items


def parse_verifier(content):
    """-> (related: True/False/None, confidence: float)."""
    if not content:
        return None, 0.5
    blk = _first_json_block(content) or content
    obj = None
    try:
        obj = json.loads(blk)
    except Exception:
        obj = None
    if not isinstance(obj, dict):
        up = content.upper()
        if "UNRELATED" in up:
            return False, 0.5
        if "RELATED" in up:
            return True, 0.5
        return None, 0.5
    rel = str(obj.get("related", "")).strip().upper()
    conf = clip01(obj.get("confidence", 0.5))
    if rel == "RELATED":
        return True, conf
    if rel == "UNRELATED":
        return False, conf
    return None, conf


def parse_selfverify(content):
    """-> (verdict: True/False/None, confidence: float)."""
    if not content:
        return None, 0.5
    blk = _first_json_block(content) or content
    obj = None
    try:
        obj = json.loads(blk)
    except Exception:
        obj = None
    if not isinstance(obj, dict):
        up = content.upper()
        if "FALSE" in up:
            return False, 0.5
        if "TRUE" in up:
            return True, 0.5
        return None, 0.5
    v = str(obj.get("verdict", "")).strip().upper()
    conf = clip01(obj.get("confidence", 0.5))
    if v == "TRUE":
        return True, conf
    if v == "FALSE":
        return False, conf
    return None, conf


def run_verifier_pass(records, model, fallbacks, tag_suffix, budget_hard, do_selfverify, concurrency=12):
    """Run the verifier (+ optional self-verify) for `records` with a reader-matched client.
    Returns a stats dict; attaches rec['verifier'/'selfverify'] (or rec['verifier_ds'])."""
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    client = OpenRouterClient(api_key, model, fallbacks, HERE / "cache", temperature=0.0,
                              budget_hard=budget_hard, budget_soft=2.0, concurrency=concurrency, max_tokens=60)
    ver_items, sv_items = build_items(records, tag_suffix=tag_suffix)
    n_pf_v = n_pf_s = 0

    ver_res = asyncio.run(client.run_batch(ver_items))
    key = "verifier_ds" if tag_suffix == "_ds" else "verifier"
    for it in ver_items:
        content = (ver_res.get(it["id"]) or {}).get("content", "")
        related, conf = parse_verifier(content)
        if related is None:
            n_pf_v += 1
        p_related = conf if related is True else (1.0 - conf if related is False else 0.5)
        records[it["_rec"]][key] = {"related": related, "conf": conf, "p_related": p_related,
                                    "content": content}
    logger.info(f"[{tag_suffix or 'primary'}] verifier done | calls={client.n_calls} cache={client.n_cache_hits} "
                f"cost=${client.cost:.4f} parse_fail={n_pf_v}")

    if do_selfverify and tag_suffix != "_ds":
        if client.cost >= 3.0:
            logger.warning("self-verify skipped: cost already >= $3 after verifier pass")
            for rec in records:
                rec["selfverify"] = {"verdict": None, "conf": 0.5, "content": "", "skipped": True}
        else:
            sv_res = asyncio.run(client.run_batch(sv_items))
            for rec in records:
                rec["selfverify"] = {"verdict": None, "conf": 0.5, "content": ""}
            for it in sv_items:
                content = (sv_res.get(it["id"]) or {}).get("content", "")
                verdict, conf = parse_selfverify(content)
                if verdict is None:
                    n_pf_s += 1
                records[it["_rec"]]["selfverify"] = {"verdict": verdict, "conf": conf, "content": content}
            logger.info(f"[{tag_suffix or 'primary'}] self-verify done | parse_fail={n_pf_s}")
    elif tag_suffix != "_ds":
        for rec in records:
            rec["selfverify"] = {"verdict": None, "conf": 0.5, "content": "", "skipped": True}

    return {"model": model, "n_llm_calls": client.n_calls, "n_cache_hits": client.n_cache_hits,
            "n_errors": client.n_errors, "cost_usd": _r(client.cost, 6),
            "n_parse_fail_verifier": n_pf_v, "n_parse_fail_selfverify": n_pf_s,
            "n_verifier_items": len(ver_items), "n_selfverify_items": len(sv_items)}


# --------------------------------------------------------------------------- #
# PHASE 6: fraction-caught crux table
# --------------------------------------------------------------------------- #
def _clustered_frac_ci(records, valuefn, seed=SEED, n_boot=2000):
    """Doc-clustered 95% CI for the mean of a per-record 0/1 indicator (resample documents)."""
    by_doc = defaultdict(list)
    for r in records:
        by_doc[r["doc_id"]].append(float(valuefn(r)))
    docs = list(by_doc)
    allv = [x for v in by_doc.values() for x in v]
    point = float(np.mean(allv)) if allv else float("nan")
    if len(docs) < 2:
        return point, [point, point]
    arrs = {d: np.array(by_doc[d], float) for d in docs}
    rng = np.random.default_rng(seed)
    means = []
    nd = len(docs)
    for _ in range(n_boot):
        pick = rng.integers(0, nd, nd)
        vals = np.concatenate([arrs[docs[i]] for i in pick])
        means.append(vals.mean())
    lo, hi = np.quantile(means, [ALPHA / 2, 1 - ALPHA / 2])
    return point, [float(lo), float(hi)]


def fraction_caught_table(records, pool_name):
    """For the FACT-A absent fabrication set, the fraction CAUGHT (not kept as confident-wrong)
    by each method.  THRESHOLD-FREE for the corrective gates (certificate / verifier / self-verify):
    caught = the method abstains / answers 'no-relation' on that fabrication.  For the four
    dispersion signals + verifier-as-signal: caught = 1 - frac_surviving the certificate-matched
    GLOBAL confidence rule (== the published crux survival)."""
    absent = [r for r in records if r["is_absent"]]
    fab = [r for r in absent if r["raw_named"]]   # the absent-relation hallucinations
    n_fab = len(fab)
    out = {"pool": pool_name, "n_fabrications": n_fab, "fabrication_def": "absent pair, raw LLM committed a relation"}
    rows = {}

    # threshold-free corrective gates
    gate_methods = ["certificate", "queryside_verifier", "queryside_selfverify"]
    if fab and "queryside_verifier_dsv" in fab[0]["M"]:
        gate_methods.append("queryside_verifier_dsv")
    for m in gate_methods:
        caught_fn = lambda r, mm=m: (0.0 if r["M"][mm]["named"] else 1.0)
        point, ci = _clustered_frac_ci(fab, caught_fn) if n_fab else (float("nan"), [float("nan")] * 2)
        rows[m] = {"fraction_caught": _r(point), "survival": _r(1 - point) if point == point else float("nan"),
                   "ci95_doc_clustered": [_r(ci[0]), _r(ci[1])], "rule": "threshold-free abstention",
                   "tag": "REAL-LLM-READ"}

    # dispersion signals: caught = below the certificate-matched global confidence rule
    # (reuse the absent-pool-median threshold that reproduces the published crux survival)
    mixed = records  # the venue's full mixed pool
    cert_named = np.array([r["M"]["certificate"]["named"] for r in mixed], bool)
    for s in SIGNALS:
        pool_med = float(np.median([r["conf"][s] for r in absent])) if absent else float("nan")
        def caught_fn(r, ss=s, pm=pool_med):
            return 1.0 if (r["conf"][ss] < pm) else 0.0
        point, ci = _clustered_frac_ci(fab, caught_fn) if n_fab else (float("nan"), [float("nan")] * 2)
        rows[f"ct_{s}"] = {"fraction_caught": _r(point), "survival": _r(1 - point) if point == point else float("nan"),
                           "ci95_doc_clustered": [_r(ci[0]), _r(ci[1])],
                           "rule": "below absent-pool-median confidence (certificate-matched global rule)",
                           "tag": "REAL-LLM-READ"}
    out["per_method"] = rows
    return out


# --------------------------------------------------------------------------- #
# PHASE 7: certificate-necessity verdict
# --------------------------------------------------------------------------- #
def _paired_caught_gap(fab, m_a, m_b, seed=SEED, n_boot=B_BOOT):
    """Doc-clustered paired bootstrap of (caught_a - caught_b) over the fabrication set."""
    def caught(r, m):
        return 0.0 if r["M"][m]["named"] else 1.0
    a = np.array([caught(r, m_a) for r in fab], float)
    b = np.array([caught(r, m_b) for r in fab], float)
    point = float(a.mean() - b.mean()) if len(fab) else float("nan")
    by_doc = defaultdict(list)
    for i, r in enumerate(fab):
        by_doc[r["doc_id"]].append(i)
    docs = list(by_doc)
    nd = len(docs)
    if nd < 2:
        return {"gap": _r(point), "ci95": [float("nan"), float("nan")], "p_two_sided": float("nan")}
    rng = np.random.default_rng(seed)
    gaps = []
    for _ in range(n_boot):
        pick = rng.integers(0, nd, nd)
        idx = np.concatenate([by_doc[docs[i]] for i in pick])
        gaps.append(float(a[idx].mean() - b[idx].mean()))
    gaps = np.array(gaps, float)
    lo, hi = np.quantile(gaps, [ALPHA / 2, 1 - ALPHA / 2])
    p2 = 2.0 * min(float(np.mean(gaps <= 0.0)), float(np.mean(gaps >= 0.0)))
    return {"gap": _r(point), "ci95": [_r(lo), _r(hi)], "p_two_sided": _r(min(1.0, p2)),
            "ci_excludes_0": bool(lo > 0.0 or hi < 0.0)}


def necessity_verdict(records, pool_name):
    """Per-venue verdict: does the structural certificate catch MORE absent-relation
    hallucinations than the query-side verifier (and self-verify)?  Decided by the data."""
    absent = [r for r in records if r["is_absent"]]
    fab = [r for r in absent if r["raw_named"]]
    n_fab = len(fab)

    def caught_rate(m):
        if not n_fab:
            return float("nan")
        return float(np.mean([0.0 if r["M"][m]["named"] else 1.0 for r in fab]))

    cert_c = caught_rate("certificate")
    ver_c = caught_rate("queryside_verifier")
    sv_c = caught_rate("queryside_selfverify")
    gap_cv = _paired_caught_gap(fab, "certificate", "queryside_verifier")     # cert - verifier
    gap_cs = _paired_caught_gap(fab, "certificate", "queryside_selfverify")

    def decide(cert, other, gap):
        if not (cert == cert and other == other) or gap["ci95"][0] != gap["ci95"][0]:
            return "INCONCLUSIVE"
        lo, hi = gap["ci95"]
        if lo > 0.0:
            return "CERTIFICATE_NECESSARY"          # certificate catches strictly more
        if other >= cert or lo <= 0.0 <= hi or hi < 0.0:
            return "VERIFIER_MATCHES_OR_BEATS"       # honest negative: structural cert not strictly needed
        return "INCONCLUSIVE"

    verdict_v = decide(cert_c, ver_c, gap_cv)
    verdict_s = decide(cert_c, sv_c, gap_cs)
    out = {
        "pool": pool_name, "n_fabrications": n_fab,
        "certificate_fraction_caught": _r(cert_c),
        "queryside_verifier_fraction_caught": _r(ver_c),
        "queryside_selfverify_fraction_caught": _r(sv_c),
        "certificate_minus_verifier_caught_gap": gap_cv,
        "certificate_minus_selfverify_caught_gap": gap_cs,
        "verdict_vs_verifier": verdict_v,
        "verdict_vs_selfverify": verdict_s,
        "tag": "REAL-LLM-READ",
    }
    if n_fab and "queryside_verifier_dsv" in fab[0]["M"]:
        out["queryside_verifier_deepseek_fraction_caught"] = _r(caught_rate("queryside_verifier_dsv"))
    return out


def overall_verdict(per_venue):
    """Cross-venue summary string."""
    vs = {p: v["verdict_vs_verifier"] for p, v in per_venue.items()}
    if all(x == "CERTIFICATE_NECESSARY" for x in vs.values()):
        head = "CERTIFICATE_NECESSARY_BOTH_VENUES"
    elif all(x == "VERIFIER_MATCHES_OR_BEATS" for x in vs.values()):
        head = "VERIFIER_SUFFICES_BOTH_VENUES"
    else:
        head = "VENUE_DEPENDENT"
    return {"headline": head, "per_venue_vs_verifier": vs,
            "interpretation": (
                "CERTIFICATE_NECESSARY: the structural no-derivation certificate catches strictly more "
                "confident absent-relation hallucinations than a query-side false-premise verifier "
                "(doc-clustered CI of the caught-gap excludes 0, >0) -> the structural signal is needed. "
                "VERIFIER_MATCHES_OR_BEATS: the cheap query-side verifier catches as many or more -> the "
                "structural certificate is not strictly necessary on that stratum (the reviewer's DISCONFIRM "
                "is satisfied; honest negative). VENUE_DEPENDENT: the answer differs by corpus.")}


# --------------------------------------------------------------------------- #
# PHASE 8: output
# --------------------------------------------------------------------------- #
def _pred_str(rec, m, fallback="no-relation"):
    d = rec["M"].get(m)
    if d is None:
        return fallback
    p = d.get("pred")
    return str(p) if p is not None else fallback


def build_examples(records):
    by = defaultdict(list)
    for rec in records:
        if rec["pool"] == "clutrr":
            corpus = "clutrr_absent" if rec["is_absent"] else "clutrr_present"
        else:
            base = "redocred" if rec["slice"] == "re-docred" else "docred"
            corpus = f"{base}_{'absent' if rec['is_absent'] else 'present'}"
        v = rec["verifier"]
        sv = rec["selfverify"]
        ex = {
            "input": (rec["doc_text"] or "")[:1200] + f"  || Q: what is {rec['qtgt_name']} to {rec['qsrc_name']}?",
            "output": str(rec["gold"]),
            # ---- predictions (ALL strings) ----
            "predict_certificate": _pred_str(rec, "certificate"),
            "predict_conf_thresh_verbalized": str(rec["predict_conf_thresh"]["verbalized"]),
            "predict_conf_thresh_sc_margin": str(rec["predict_conf_thresh"]["sc_margin"]),
            "predict_conf_thresh_ptrue": str(rec["predict_conf_thresh"]["ptrue"]),
            "predict_conf_thresh_negent": str(rec["predict_conf_thresh"]["negent"]),
            "predict_commit_argmax": str(rec["predict_commit_argmax"]),
            "predict_queryside_verifier": _pred_str(rec, "queryside_verifier"),
            "predict_queryside_selfverify": _pred_str(rec, "queryside_selfverify"),
            "predict_verifier_as_signal": _pred_str(rec, "verifier_as_signal"),
            # ---- metadata ----
            "metadata_pool": rec["pool"], "metadata_slice": rec["slice"], "metadata_reader": rec["reader"],
            "metadata_is_absent": rec["is_absent"], "metadata_stratum": rec["stratum"],
            "metadata_doc_id": rec["doc_id"], "metadata_qsrc": rec["qsrc_name"], "metadata_qtgt": rec["qtgt_name"],
            "metadata_gold": str(rec["gold"]), "metadata_gold_primitive": rec["gold_primitive"],
            "metadata_raw_named": rec["raw_named"], "metadata_raw_answer": rec["raw_answer"],
            "metadata_conf_verbalized": rec["conf"]["verbalized"], "metadata_conf_sc_margin": rec["conf"]["sc_margin"],
            "metadata_conf_ptrue": rec["conf"]["ptrue"], "metadata_conf_negent": rec["conf"]["negent"],
            "metadata_verifier_related": ("RELATED" if v["related"] is True else
                                          "UNRELATED" if v["related"] is False else "PARSE_FAIL"),
            "metadata_verifier_confidence": v["conf"], "metadata_p_related": v["p_related"],
            "metadata_selfverify_verdict": ("TRUE" if sv["verdict"] is True else
                                            "FALSE" if sv["verdict"] is False else "NA"),
            "metadata_conf_queryside_selfverify": sv["conf"],
            "metadata_order_index": rec["order_index"],
        }
        if rec.get("verifier_ds") is not None:
            ex["predict_queryside_verifier_dsv"] = _pred_str(rec, "queryside_verifier_dsv")
            ex["metadata_verifier_deepseek_related"] = (
                "RELATED" if rec["verifier_ds"]["related"] is True else
                "UNRELATED" if rec["verifier_ds"]["related"] is False else "PARSE_FAIL")
        by[corpus].append(ex)
    order = ["clutrr_present", "clutrr_absent", "redocred_present", "redocred_absent",
             "docred_present", "docred_absent"]
    return [{"dataset": k, "examples": by[k]} for k in order if by.get(k)]


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="cap records per pool (smoke test)")
    ap.add_argument("--no-selfverify", action="store_true")
    ap.add_argument("--no-deepseek-sensitivity", action="store_true")
    ap.add_argument("--budget-hard", type=float, default=9.0)
    ap.add_argument("--concurrency", type=int, default=12)
    ap.add_argument("--out", type=str, default=str(HERE / "method_out.json"))
    args = ap.parse_args()

    t0 = time.time()
    logger.info("=== iter-8 exp_2: query-side verifier vs the no-derivation certificate ===")
    if not os.environ.get("OPENROUTER_API_KEY"):
        logger.error("OPENROUTER_API_KEY not set"); sys.exit(1)
    for p in (CLUTRR_POOL, REDOCRED_POOL, COMP_TABLE):
        if not p.exists():
            logger.error(f"required input missing: {p}"); sys.exit(1)

    # ---- PHASE 1 ----
    clutrr_recs, clutrr_md = load_pool(CLUTRR_POOL, "clutrr")
    redoc_recs, redoc_md = load_pool(REDOCRED_POOL, "redocred")
    all_recs = clutrr_recs + redoc_recs
    build_order_and_text(all_recs)
    for rec in all_recs:
        build_base_methods(rec)
    logger.info(f"phase1 done: {len(clutrr_recs)} clutrr + {len(redoc_recs)} redocred records")

    # ---- PHASE 2: reproduction gate ($0) ----
    gate, all_ok = reproduction_gate(clutrr_recs, clutrr_md, redoc_recs, redoc_md)
    n_fail = gate["n_checks"] - gate["n_passed"]
    logger.info(f"reproduction gate: {gate['n_passed']}/{gate['n_checks']} passed (all_ok={all_ok})")
    if not all_ok:
        for c in gate["checks"]:
            if not c["ok"]:
                logger.error(f"  GATE FAIL {c['name']}: recomputed={c['recomputed']} "
                             f"carried={c['carried']} published={c['published']}")
        out = {"metadata": {"method_name": "query-side verifier vs no-derivation certificate",
                            "ABORTED": "reproduction gate failed -- no LLM spend",
                            "reproduction_gate": gate}, "datasets": []}
        Path(args.out).write_text(json.dumps(out, indent=1, default=_json_default))
        logger.error("HARD STOP: reproduction gate failed; corrupted/mismatched pool surfaced, no spend.")
        sys.exit(2)
    logger.info("reproduction gate PASSED -> green light to spend on the verifier.")

    if args.limit:
        clutrr_recs = clutrr_recs[:args.limit]
        redoc_recs = redoc_recs[:args.limit]
        all_recs = clutrr_recs + redoc_recs

    # ---- PHASE 3 + 4: verifier (reader-matched gemini) + self-verify ----
    spend = {}
    spend["primary_gemini"] = run_verifier_pass(
        all_recs, PRIMARY_MODEL, FALLBACKS, tag_suffix="", budget_hard=args.budget_hard,
        do_selfverify=not args.no_selfverify, concurrency=args.concurrency)
    cum_cost = spend["primary_gemini"]["cost_usd"]

    # deepseek-verifier robustness sensitivity (verifier-MODEL diversity; reads still gemini's)
    if (not args.no_deepseek_sensitivity) and cum_cost < 4.0:
        try:
            spend["sensitivity_deepseek_verifier"] = run_verifier_pass(
                all_recs, CROSS_MODEL, DEEPSEEK_FALLBACKS, tag_suffix="_ds",
                budget_hard=args.budget_hard, do_selfverify=False, concurrency=args.concurrency)
            cum_cost += spend["sensitivity_deepseek_verifier"]["cost_usd"]
        except BudgetExceeded as e:
            logger.warning(f"deepseek sensitivity hit budget: {e}")
            spend["sensitivity_deepseek_verifier"] = {"skipped_budget": str(e)}
    else:
        for rec in all_recs:
            rec["verifier_ds"] = None
        spend["sensitivity_deepseek_verifier"] = {"skipped": "disabled or cost>=$4 after primary"}

    for rec in all_recs:
        if "verifier_ds" not in rec:
            rec["verifier_ds"] = None
        attach_verifier_methods(rec)

    # ---- PHASE 5: matched-coverage leaderboards per venue ----
    METHODS = ["certificate", "ct_verbalized", "ct_sc_margin", "ct_ptrue", "ct_negent",
               "queryside_verifier", "queryside_selfverify", "verifier_as_signal", "commit_argmax"]
    if all_recs and all_recs[0].get("verifier_ds") is not None:
        METHODS.append("queryside_verifier_dsv")

    def venue(recs):
        return sorted(recs, key=lambda r: r["order_index"])

    cl_present = [r for r in clutrr_recs if not r["is_absent"]]
    cl_absent = [r for r in clutrr_recs if r["is_absent"]]
    rd_present = [r for r in redoc_recs if r["slice"] == "re-docred" and not r["is_absent"]]
    rd_absent = [r for r in redoc_recs if r["slice"] == "re-docred" and r["is_absent"]]
    dd_present = [r for r in redoc_recs if r["slice"] == "docred" and not r["is_absent"]]

    leaderboards = {
        "clutrr_present": venue_leaderboard(venue(cl_present), METHODS, "CLUTRR present (multi-hop deduction)"),
        "clutrr_absent": venue_leaderboard(venue(cl_absent), METHODS, "CLUTRR absent (no-derivation)"),
        "clutrr_mixed": venue_leaderboard(venue(cl_present + cl_absent), METHODS, "CLUTRR mixed (present+absent) [DECISIVE]"),
        "redocred_present": venue_leaderboard(venue(rd_present), METHODS, "Re-DocRED present (natural deduction)"),
        "redocred_absent": venue_leaderboard(venue(rd_absent), METHODS, "Re-DocRED absent (no-derivation)"),
        "redocred_mixed": venue_leaderboard(venue(rd_present + rd_absent), METHODS, "Re-DocRED mixed (present+absent) [DECISIVE]"),
    }
    if dd_present:
        leaderboards["docred_present"] = venue_leaderboard(venue(dd_present), METHODS,
                                                           "DocRED present (corroboration; absent gold downgraded)")

    # ---- PHASE 6: fraction-caught crux tables (on the mixed pools) ----
    fraction_caught = {
        "clutrr": fraction_caught_table(venue(cl_present + cl_absent), "clutrr"),
        "redocred": fraction_caught_table(venue(rd_present + rd_absent), "redocred"),
    }

    # ---- PHASE 7: necessity verdict ----
    per_venue_verdict = {
        "clutrr": necessity_verdict(venue(cl_present + cl_absent), "clutrr"),
        "redocred": necessity_verdict(venue(rd_present + rd_absent), "redocred"),
    }
    overall = overall_verdict(per_venue_verdict)

    # ---- PHASE 8: output ----
    datasets = build_examples(all_recs)
    total_cost = sum(v.get("cost_usd", 0.0) for v in spend.values() if isinstance(v, dict))
    headline = {
        "question": ("Is the no-derivation closure certificate's absent-relation hallucination-safety "
                     "just a re-skin of a query-side false-premise verifier the LLM could run directly?"),
        "verifier_primary_model": PRIMARY_MODEL, "verifier_sensitivity_model": CROSS_MODEL,
        "reader_note": ("Both cached pools carry per-row predictions from the GEMINI reader only; the "
                        "verifier is therefore reader-matched to gemini. The deepseek FACT-A is reproduced "
                        "from each pool's carried cross-family aggregate; the deepseek VERIFIER arm is a "
                        "verifier-model robustness check on the gemini-read rows (clearly labelled, not "
                        "reader-matched)."),
        "fraction_caught_headline": {
            p: {"certificate": fraction_caught[p]["per_method"].get("certificate", {}).get("fraction_caught"),
                "queryside_verifier": fraction_caught[p]["per_method"].get("queryside_verifier", {}).get("fraction_caught"),
                "queryside_selfverify": fraction_caught[p]["per_method"].get("queryside_selfverify", {}).get("fraction_caught")}
            for p in ("clutrr", "redocred")},
        "overall_verdict": overall["headline"],
    }
    metadata = {
        "method_name": "Query-side false-premise verifier + self-verify vs the no-derivation closure certificate",
        "step": ("iter-8 experiment_2: reviewer-mandated DISCONFIRM test. Reuses the cached CLUTRR (iter-6) "
                 "+ Re-DocRED (iter-7) kinship prediction pools; adds a query-side verifier + self-verify "
                 "baseline at matched coverage."),
        "headline_summary": headline,
        "reproduction_gate": gate,
        "config": {"primary_model": PRIMARY_MODEL, "cross_model": CROSS_MODEL, "fallbacks": FALLBACKS,
                   "bootstrap_B": B_BOOT, "seed": SEED, "alpha": ALPHA, "tolerance": TOL,
                   "signals": list(SIGNALS), "methods": METHODS},
        "leaderboards": leaderboards,
        "fraction_caught_crux_tables": fraction_caught,
        "certificate_necessity_verdict": {"per_venue": per_venue_verdict, "overall": overall},
        "spend_ledger": {"per_pass": spend, "cumulative_usd": _r(total_cost, 6),
                         "hard_cap_usd": args.budget_hard,
                         "note": "sha256-cached; re-runs replay at $0. Only the verifier + self-verify are new spend."},
        "honesty_tags": {
            "all_new_numbers": "REAL-LLM-READ (genuine OpenRouter completions; cached replays $0)",
            "reproduction": "order-independent certificate/FACT-A/crux numbers reproduce exactly; "
                            "signal mixed selaccs reproduce exactly after source-order reconstruction",
            "deepseek_per_row": "NOT AVAILABLE in either pool (aggregate-only) -> deepseek FACT-A reproduced "
                                "from carried aggregate; per-row verifier is gemini-reader-matched",
            "absent_structural": "absent pairs are structural (different components) -> the certificate's absent "
                                 "abstention is structural-by-construction; the verifier comparison tests whether "
                                 "a query-side LLM call recovers the same abstention without the closure engine",
            "prolog": "no new symbolic discharge in this artifact (the certificate predictions are reused verbatim)",
        },
        "runtime_sec": _r(time.time() - t0, 1),
    }
    out = {"metadata": metadata, "datasets": datasets}
    Path(args.out).write_text(json.dumps(out, indent=1, default=_json_default))
    logger.info(f"WROTE {args.out} | cost=${total_cost:.4f} | runtime={time.time()-t0:.1f}s")
    logger.info(f"OVERALL VERDICT: {overall['headline']}")
    for p, v in per_venue_verdict.items():
        logger.info(f"  [{p}] cert_caught={v['certificate_fraction_caught']} "
                    f"verifier_caught={v['queryside_verifier_fraction_caught']} "
                    f"selfverify_caught={v['queryside_selfverify_fraction_caught']} "
                    f"-> vs_verifier={v['verdict_vs_verifier']}")
    return out


if __name__ == "__main__":
    main()
