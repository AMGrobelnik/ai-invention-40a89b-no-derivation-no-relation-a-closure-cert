#!/usr/bin/env python3
"""KINSHIP-domain replication of the iter-9 extraction-recall booster (second-domain bonus).

Reuses the iter-7 natural-kinship harness (dataio_redocred.py loader + readers_kinship.py readers)
and the iter-9 shared per-strategy machinery in method.py (recompute_certificate / eval_strategy /
build_frontier). The kinship corpus has NO same-component-sibling regime, so the decisive mixed
pool is present (composed deduction) + different_component absent (the clean kinship-analog). The
six FIXED competitors are the 4 dispersion signals (default-arm reads replay from the iter-7 cache
at $0) + the 2 query-side verifiers (queryside_kinship.py; NEW, cheap).

Cache replay: extraction (tag 'extract'), raw ('raw'), SC ('sc{s}' temp 0.7), and P(True) ('ptrue'
with the iter-7 kinship PTRUE_SYSTEM) reproduce the iter-7 keys exactly. The booster S2-S5 and the
query-side verifier reads are genuinely new spend (cached re-runs replay $0).
"""
from __future__ import annotations

import asyncio
import copy
import gc
import json
from collections import defaultdict
from pathlib import Path

import numpy as np
from loguru import logger

import baselines as B
import booster as BO
import core
import dataio_redocred as DK
import queryside_kinship as QK
import readers_kinship as RK
from kinship import Kinship, simple_paths_names

KINSHIP_DATA = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/full_data_out.json")
SECOND_FAMILY_MODEL = "mistralai/mistral-small-2603"
SC_K = 10

# iter-7 kinship P(True) system (verbatim, so the ptrue cache replays at $0)
PTRUE_SYSTEM = (
    "You judge whether a proposed kinship answer is correct given a short text. Output ONLY "
    'a JSON object {"p_true": <0..1>} where p_true is your probability that the proposed answer '
    "is correct. Be calibrated: give a low probability when the two people have no family "
    "relationship in the text or when the proposed relation is wrong.")


def _ptrue_item(story, qsrc_name, qtgt_name, proposed, story_id, tag="ptrue"):
    user = (f"Story:\n{story}\n\nQuestion: What is {qtgt_name} to {qsrc_name}? "
            f"(i.e. {qtgt_name} is {qsrc_name}'s ___)\nProposed answer: \"{proposed}\".\n"
            f"What is the probability this proposed answer is correct? Answer with the JSON object.")
    return {"id": f"{tag}::{story_id}::{qsrc_name}->{qtgt_name}", "system": PTRUE_SYSTEM,
            "user": user, "max_tokens": 30, "temperature": 0.0, "tag": tag}


# --------------------------------------------------------------------------- #
# record augmentation: add the fields the shared (located-in-shaped) views expect
# --------------------------------------------------------------------------- #
def _augment(records):
    for r in records:
        r["is_held_out"] = False                      # kinship present queries are composed (no direct edge)
        r["gold_atomics_full"] = r["gold_atomics"]    # no ablation in kinship
        if r["is_absent"]:
            r["absent_regime"] = "different_component"
            r["query_subtype"] = "different_component"
        else:
            r["absent_regime"] = None
            r["query_subtype"] = "composed"


# --------------------------------------------------------------------------- #
# STAGE 2 fixed-baseline reads (kinship vocab)
# --------------------------------------------------------------------------- #
def replay_reads_kinship(records, kin, client, contexts):
    docs = {}
    for r in records:
        docs.setdefault(r["doc_id"], r)
    ext_items, ext_id = [], {}
    for did, r in docs.items():
        it = RK.extraction_item(r["story"], did)
        it["tag"] = "extract"
        it["id"] = f"extract::{did}"
        ext_id[did] = it["id"]
        ext_items.append(it)
    logger.info(f"[kinship] extraction items: {len(ext_items)} docs")
    ext_results = asyncio.run(client.run_batch(ext_items))
    grounded = {}
    for did, r in docs.items():
        ctx = contexts[did]
        content = (ext_results.get(ext_id[did]) or {}).get("content", "")
        parsed = RK.parse_extraction(content, kin)
        grounded[did] = [{"a": DK.ground_name(e["a"], ctx), "b": DK.ground_name(e["b"], ctx),
                          "type": e["type"], "surface": e.get("surface")} for e in parsed["edges"]]
    # raw + PoT per query
    q_items = []
    for r in records:
        sid, story = r["doc_id"], r["story"]
        qs, qt = r["qsrc_name"], r["qtgt_name"]
        q_items.append(RK.raw_query_item(story, qs, qt, sid, tag="raw"))
        if not r["is_absent"]:
            id_paths = simple_paths_names(r["gold_atomics"], r["qsrc"], r["qtgt"], max_paths=3)
            r["_pot_id_paths"] = id_paths
            for pi, idp in enumerate(id_paths):
                name_path = DK.id_path_to_names(idp, r["_ctx"])
                it = RK.pot_item(story, name_path, sid, pi)
                it["tag"] = f"pot{pi}"
                it["id"] = it["id"]
                q_items.append(it)
        else:
            r["_pot_id_paths"] = []
    logger.info(f"[kinship] query reads (raw+pot): {len(q_items)} items")
    q_results = asyncio.run(client.run_batch(q_items))
    for r in records:
        sid, qs, qt = r["doc_id"], r["qsrc_name"], r["qtgt_name"]
        base = f"::{sid}::{qs}->{qt}"
        raw = q_results.get(f"raw{base}")
        rawp = RK.parse_raw(raw["content"]) if raw and raw.get("content") else {"surface": None, "confidence": 0.0, "abstain": True}
        r["_raw"] = rawp
        potp = []
        for pi in range(len(r["_pot_id_paths"])):
            res = q_results.get(f"pot{pi}{base}")
            if res and res.get("content"):
                potp.append(RK.parse_raw(res["content"]))
        r["_pot"] = RK.aggregate_pot(potp) if potp else {"surface": None, "confidence": 0.0, "abstain": True}
        edges = grounded.get(sid, [])
        r["_extracted_edges"] = edges
        sym = B.predict_symbolic(kin, edges, r["qsrc"], r["qtgt"], r["genders"])
        r["modeA"] = sym["modeA"]; r["naive"] = sym["naive"]; r["_modeA_raw"] = sym["modeA_raw"]
        symg = B.predict_symbolic(kin, r["gold_atomics"], r["qsrc"], r["qtgt"], r["genders"])
        r["modeA_goldread"] = symg["modeA"]
        for key, src in (("raw", "_raw"), ("pot", "_pot")):
            p = r[src]
            named = (not p["abstain"]) and (p["surface"] is not None)
            r[key] = {"surface": p["surface"], "conf": float(p["confidence"]), "named": bool(named)}
        r["off"] = {"surface": None, "conf": 0.0, "named": False}
    return grounded


def run_battery_kinship(records, client):
    sc_items, pt_items = [], []
    for r in records:
        sid, story = r["doc_id"], r["story"]
        qs, qt = r["qsrc_name"], r["qtgt_name"]
        for s in range(SC_K):
            sc_items.append(RK.raw_query_item(story, qs, qt, sid, tag=f"sc{s}", temperature=0.7))
        proposed = r["raw"]["surface"] if (r["raw"]["named"] and r["raw"]["surface"]) else "no-relation"
        pt_items.append(_ptrue_item(story, qs, qt, proposed, sid, tag="ptrue"))
    logger.info(f"[kinship] battery: SC={len(sc_items)} P(True)={len(pt_items)}")
    sc_results = asyncio.run(client.run_batch(sc_items))
    pt_results = asyncio.run(client.run_batch(pt_items))
    for r in records:
        sid, qs, qt = r["doc_id"], r["qsrc_name"], r["qtgt_name"]
        base = f"::{sid}::{qs}->{qt}"
        sc_parsed = []
        for s in range(SC_K):
            res = sc_results.get(f"sc{s}{base}")
            if res and res.get("content"):
                sc_parsed.append(RK.parse_raw(res["content"]))
        agg = RK.aggregate_sc(sc_parsed) if sc_parsed else {"surface": None, "confidence": 0.0, "abstain": True}
        ent = core.semantic_entropy(sc_parsed)
        pt = pt_results.get(f"ptrue{base}")
        ptrue = core.parse_ptrue(pt["content"]) if pt and pt.get("content") else 0.5
        r["sc"] = {"surface": agg["surface"], "conf": float(agg["confidence"]),
                   "named": bool((not agg["abstain"]) and agg["surface"] is not None)}
        r["_sig"] = {"verbalized": float(r["raw"]["conf"]), "sc_margin": float(agg["confidence"]),
                     "ptrue": float(ptrue), "negent": float(ent["negent"]), "H": float(ent["H"]),
                     "sc_k_eff": int(ent["k_eff"]), "sc_majority_surface": agg["surface"],
                     "sc10_abstain": bool(agg["abstain"])}


def build_ct_baselines_kinship(records):
    for r in records:
        raw_surface = r["raw"]["surface"]; raw_named = bool(r["raw"]["named"])
        for s in core.SIGNALS:
            r[f"ct_{s}"] = {"surface": raw_surface, "conf": float(r["_sig"][s]), "named": raw_named}
        maj = r["_sig"]["sc_majority_surface"]
        r["ct_sc_margin_maj"] = {"surface": maj, "conf": float(r["_sig"]["sc_margin"]),
                                 "named": bool(maj is not None and not r["_sig"]["sc10_abstain"])}
        r["commit_argmax"] = {"surface": raw_surface, "conf": float(r["raw"]["conf"]), "named": raw_named}
    QK.build_queryside_method_dicts(records)


# --------------------------------------------------------------------------- #
# output examples
# --------------------------------------------------------------------------- #
def _pred(p):
    return core._pred_word(p)


def build_examples_kinship(records, reader_name, best_strategy):
    by = defaultdict(list)
    for r in records:
        corpus = "kinship_present" if not r["is_absent"] else "kinship_absent"
        ex = {
            "input": (r["story"][:1200] + f"  || Q: what is {r['qtgt_name']} to {r['qsrc_name']}?"),
            "output": r["gold_surface_word"],
            "predict_certificate_best": _pred(r["modeA"]),
            "predict_certificate_default_S0": _pred(r.get("modeA_s0") or {"named": False}),
            "predict_certificate_goldread": _pred(r["modeA_goldread"]),
            "predict_conf_thresh_verbalized": _pred(r["ct_verbalized"]),
            "predict_conf_thresh_sc_margin": _pred(r["ct_sc_margin"]),
            "predict_conf_thresh_ptrue": _pred(r["ct_ptrue"]),
            "predict_conf_thresh_negent": _pred(r["ct_negent"]),
            "predict_queryside_verifier": _pred(r["queryside_verifier"]),
            "predict_queryside_selfverify": _pred(r["queryside_selfverify"]),
            "predict_commit_argmax": _pred(r["commit_argmax"]),
            "predict_pot": _pred(r["pot"]),
            "predict_sc": _pred(r["sc"]),
            "metadata_domain": "kinship",
            "metadata_best_strategy": best_strategy,
            "metadata_is_absent": r["is_absent"], "metadata_regime": r["query_subtype"],
            "metadata_reader": reader_name, "metadata_doc_id": r["doc_id"], "metadata_title": r["title"],
            "metadata_qsrc_name": r["qsrc_name"], "metadata_qtgt_name": r["qtgt_name"],
            "metadata_hop": r["hop"], "metadata_gold_primitive": r["gold_primitive"],
            "metadata_certificate_best_named": bool(r["modeA"]["named"]),
            "metadata_certificate_goldread_named": bool(r["modeA_goldread"]["named"]),
            "metadata_raw_named": bool(r["raw"]["named"]),
            "metadata_n_extracted_edges_best": len(r.get("_extracted_edges", [])),
        }
        by[corpus].append(ex)
    return [{"dataset": k, "examples": v} for k, v in sorted(by.items())]


# --------------------------------------------------------------------------- #
# driver
# --------------------------------------------------------------------------- #
def run_kinship(args, client):
    import method as M  # shared per-strategy machinery (lazy to avoid import cycle)
    cost_before = client.cost
    full = json.loads(KINSHIP_DATA.read_text())
    kin = Kinship(full["metadata"]["composition_table"])
    assert len(kin.base) == 11, kin.base
    logger.info(f"[kinship] engine OK base={kin.base[:4]}... ({len(kin.base)} types)")

    rows = DK.load_slice(full, "re-docred")
    if args.kinship_limit_docs:
        rows = rows[:args.kinship_limit_docs]
    records, contexts = DK.build_records(rows, kin, "re-docred")
    _augment(records)
    del full, rows
    gc.collect()

    if args.no_subsample:
        sub, realized = records, {"no_subsample": True, "n": len(records)}
    else:
        targets = {"composed": args.kin_target_present, "different_component": args.kin_target_absent}
        per_doc_caps = {"composed": 6, "different_component": 6}
        sub, realized = core.stratified_subsample(records, targets, per_doc_caps)
    records = sub
    contexts = {did: ctx for did, ctx in contexts.items() if any(r["doc_id"] == did for r in records)}
    logger.info(f"[kinship] subsample realized: {realized}")

    # STAGE 2 fixed baseline
    grounded_default = replay_reads_kinship(records, kin, client, contexts)
    if not args.no_battery:
        run_battery_kinship(records, client)
        QK.run_queryside(records, client, reader_tag="kinship")
    else:
        core.cached_sig_fallback(records)
        QK.build_queryside_method_dicts(records)
    build_ct_baselines_kinship(records)
    core.primitivize(records, kin)
    M.snapshot_baselines(records)
    for r in records:
        r["modeA_s0"] = copy.deepcopy(r["modeA"])
        r["_extracted_edges_s0"] = list(r.get("_extracted_edges", []))
    logger.info(f"[kinship] FIXED baselines done | cost delta=${client.cost-cost_before:.4f}")

    present = [r for r in records if not r["is_absent"]]
    absent = [r for r in records if r["is_absent"]]
    fa = core.fact_a(absent)
    factA = {"same_component_sibling": fa, "different_component": fa}  # kinship's only absent regime

    # STAGE 3 booster (RK readers); second client for S5
    from llm import OpenRouterClient
    second_client = OpenRouterClient(args.api_key, SECOND_FAMILY_MODEL,
                                     [m for m in core.MODEL_FALLBACKS if m != SECOND_FAMILY_MODEL] + [core.MODEL_PRIMARY],
                                     Path(__file__).resolve().parent / "cache", temperature=0.0,
                                     budget_hard=args.budget_hard, budget_soft=args.budget_hard,
                                     concurrency=args.concurrency, max_tokens=1200)
    strategies = [("default", grounded_default)]
    guard_stats = {}
    if client.cost < args.budget_hard - 0.8:
        strategies.append(("fewshot_enum", BO.strategy_s2(records, kin, client, contexts, DK, RK)))
    if client.cost < args.budget_hard - 0.8:
        strategies.append(("sentencewise", BO.strategy_s3(records, kin, client, contexts, DK, RK)))
    if client.cost < args.budget_hard - 0.8:
        g4, st4 = BO.strategy_s4(records, kin, client, contexts, DK, RK, k=args.booster_sc_k, reader_tag="kinship")
        strategies.append(("sc_union", g4)); guard_stats["sc_union"] = st4
    if client.cost < args.budget_hard - 1.0:
        g5, st5 = BO.strategy_s5(records, kin, client, second_client, contexts, DK, RK,
                                 second_model=SECOND_FAMILY_MODEL, reader_tag="kinship")
        strategies.append(("multimodel_union", g5)); guard_stats["multimodel_union"] = st5
    if client.cost < args.budget_hard - 0.8:
        g4s, st4s = BO.strategy_s4(records, kin, client, contexts, DK, RK, k=args.booster_sc_k,
                                   require_cue=True, reader_tag="kinship")
        strategies.append(("sc_union_highprec", g4s)); guard_stats["sc_union_highprec"] = st4s
    if client.cost < args.budget_hard - 1.0:
        g5s, st5s = BO.strategy_s5(records, kin, client, second_client, contexts, DK, RK,
                                   second_model=SECOND_FAMILY_MODEL, require_cue=True, reader_tag="kinship")
        strategies.append(("multimodel_union_highprec", g5s)); guard_stats["multimodel_union_highprec"] = st5s
    logger.info(f"[kinship] strategies: {[s[0] for s in strategies]}")

    rows_out, grounded_by_name = [], {}
    core_best = None
    for name, g in strategies:
        row, core_sib, decomp, atomic = M.eval_strategy(records, kin, g, contexts, name, present, absent,
                                                         [], factA, domain="kinship")
        rows_out.append(row); grounded_by_name[name] = g
        M.assert_baselines_unchanged(records, where=f"kinship:{name}")
        logger.info(f"[kinship:{name}] recall={row['atomic_recall_canon']} prec={row['atomic_precision_canon']} "
                    f"present_cov={row['present_coverage']} cw_abs={row['absent_sibling_confident_wrong_certificate']} "
                    f"min6_red={row['min_over6_reduction']} flip={row['flip_flag']} sub={row['sub_verdict']}")

    frontier, extrap = M.build_frontier(rows_out)
    best_name = max(rows_out, key=lambda x: (x["atomic_recall_canon"]
                                             if isinstance(x["atomic_recall_canon"], (int, float)) else -1))["strategy"]
    best_row = next(x for x in rows_out if x["strategy"] == best_name)
    domain_flip = any(x["flip_flag"] for x in rows_out)
    domain_verdict = "DEMONSTRATED-FIX" if domain_flip else best_row["sub_verdict"]
    M.recompute_certificate(records, grounded_by_name[best_name], kin)
    examples = build_examples_kinship(records, core.MODEL_PRIMARY, best_name)

    return {
        "domain": "kinship", "subsample_realized": realized,
        "n_present": len(present), "n_absent": len(absent),
        "FACT_A_absent_hallucination": fa,
        "per_strategy_rows": rows_out, "recall_vs_reduction_frontier": frontier,
        "frontier_extrapolation": extrap, "precision_guard_stats": guard_stats,
        "best_strategy": best_name, "domain_verdict": domain_verdict, "domain_flip": domain_flip,
        "examples": examples,
        "cost_usd": M._r(client.cost - cost_before + second_client.cost),
        "note": ("kinship has NO same-component-sibling regime; the decisive mixed pool is present "
                 "(composed deduction) + different_component absent (structural-by-construction). The "
                 "located-in sibling pool remains the non-structural prize."),
    }
