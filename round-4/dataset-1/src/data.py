#!/usr/bin/env python3
"""Build the SPATIAL multi-path-redundant gold-QCN corpus (iter-4 dataset_1).

Pipeline (deterministic, $0, no LLM):
  acquire (already downloaded under temp/) -> reconstruct gold relation-graphs
  -> structural multi-path-redundancy annotation (networkx) -> standardise to the
  exp_sel_data_out schema (input=story text, output=JSON gold-graph, metadata_*)
  -> corpus-level prevalence table.

Corpora (4 standardised with full graphs + 2 evaluated extras):
  SpaRP-PS1 (SpaRTUN)   dense RCC-8 + directional workhorse        [templated]
  SpaRP-PS2 (StepGame)  cardinal multi-relation                     [templated]
  SpartQA-Human         human-authored, annotation scene-graph      [semi-natural]
  StepGame-clean        single linear k-hop chain CONTRAST          [templated]
  SpartQA-Auto          templated annotation scene-graph (extra)    [templated]
  ReSQ                  genuinely-natural anchor (no recoverable graph; extra) [natural]
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import resource
from loguru import logger

import graphmetrics as gm
import loaders as L

ROOT = Path(__file__).parent
DS = ROOT / "temp" / "datasets"
UZ = ROOT / "temp" / "unzipped"

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
(ROOT / "logs").mkdir(exist_ok=True)
logger.add(ROOT / "logs" / "run.log", rotation="30 MB", level="DEBUG")

# RAM guard (box has ~700GB but be polite); CPU-time guard.
resource.setrlimit(resource.RLIMIT_AS, (28 * 1024**3, 28 * 1024**3))

THREE_K = 3000  # project ~3000-char document target

# Per-corpus emission caps (rows in data_out.json). Prevalence is computed on the
# FULL processed population; emission is a deterministic subsample where capped.
CFG = {
    "SpaRP-PS1": {"emit_cap": None, "stat_cap": None},
    "SpaRP-PS2": {"emit_cap": 2500, "stat_cap": 15000},
    "StepGame-clean": {"emit_cap": 1500, "stat_cap": 2500},
    "SpartQA-Auto": {"emit_cap": 2500, "stat_cap": None},
    "SpartQA-Human": {"emit_cap": 1600, "stat_cap": None},
    "ReSQ": {"emit_cap": None, "stat_cap": None},
}

LIC = {
    "SpaRP": "cc-by-sa-4.0 (code Apache-2.0)",
    "SpaRTUN": "MIT",
    "SpartQA": "MIT",
    "StepGame": "research-use (CC-BY-4.0 per HF card)",
    "ReSQ": "research-use (HLR/MSU release)",
}


# --------------------------------------------------------------------------- #
#  load every corpus into the uniform Scene representation
# --------------------------------------------------------------------------- #
def _read_full(path: Path):
    d = json.loads(path.read_text())
    return d if isinstance(d, list) else d.get("examples", d)


def load_all(limit_scenes=None):
    scenes = {}

    # ---- SpaRP-PS1 (SpaRTUN) -------------------------------------------------
    p = DS / "full_UKPLab_sparp_SpaRP-PS1 (SpaRTUN)_test.json"
    rows = _read_full(p)
    if limit_scenes:
        rows = rows[:limit_scenes]
    scenes["SpaRP-PS1"] = L.load_sparp(
        rows, dataset="SpaRP-PS1", split="test",
        license=LIC["SpaRP"], source="hf:UKPLab/sparp@SpaRP-PS1 (SpaRTUN):test",
        is_templated=True)
    logger.info(f"SpaRP-PS1: {len(scenes['SpaRP-PS1'])} scenes")

    # ---- SpaRP-PS2 (StepGame) ------------------------------------------------
    p = DS / "full_UKPLab_sparp_SpaRP-PS2 (StepGame)_test.json"
    rows = _read_full(p)
    cap = CFG["SpaRP-PS2"]["stat_cap"]
    if limit_scenes:
        rows = rows[:limit_scenes]
    elif cap and len(rows) > cap:
        step = len(rows) / cap   # deterministic stride sample across ALL hop levels
        rows = [rows[int(i * step)] for i in range(cap)]
    scenes["SpaRP-PS2"] = L.load_sparp(
        rows, dataset="SpaRP-PS2", split="test",
        license=LIC["SpaRP"], source="hf:UKPLab/sparp@SpaRP-PS2 (StepGame):test",
        is_templated=True)
    logger.info(f"SpaRP-PS2: {len(scenes['SpaRP-PS2'])} scenes")

    # ---- StepGame clean (TrainVersion, single chain) -------------------------
    p = DS / "full_michaelszx_StepGame_train.json"
    rows = _read_full(p)
    # deterministic: 500 per k_hop in {1..5}
    by_k = {}
    for r in rows:
        by_k.setdefault(r.get("k_hop"), []).append(r)
    sel = []
    per_k = 500 if not limit_scenes else max(1, limit_scenes // 5)
    for k in sorted(x for x in by_k if x is not None):
        sel.extend(by_k[k][:per_k])
    scenes["StepGame-clean"] = L.load_stepgame(
        sel, dataset="StepGame-clean", split="train",
        license=LIC["StepGame"], source="hf:michaelszx/StepGame:train(clean)")
    logger.info(f"StepGame-clean: {len(scenes['StepGame-clean'])} scenes")

    # ---- SpartQA-Auto (templated annotation) ---------------------------------
    sc_auto = []
    for sp in ["train", "dev", "test"]:
        ann = L.load_json_relaxed(UZ / "SpartQA_Auto" / "SpartQA_Auto" / f"annotation_{sp}.json")
        data = ann["data"] if isinstance(ann, dict) else ann
        if sp != "test":   # keep test full; cap train/dev contribution for size
            data = data[:600]
        sc_auto += L.load_spartqa_annotation(
            data, dataset="SpartQA-Auto", split=sp,
            license=LIC["SpartQA"], source=f"msu:SpartQA_Auto/annotation_{sp}.json",
            is_natural=False)
    if limit_scenes:
        sc_auto = sc_auto[:limit_scenes]
    scenes["SpartQA-Auto"] = sc_auto
    logger.info(f"SpartQA-Auto: {len(sc_auto)} scenes")

    # ---- SpartQA-Human (semi-natural SpRL-triple annotation) -----------------
    sc_hum, hum_neg = [], 0
    for sp in ["train", "dev", "test"]:
        ann = json.loads((UZ / "SpartQA_Human" / "SpartQA_Human" / f"human_{sp}_annotation.json").read_text())
        s, neg = L.load_spartqa_human(
            ann, dataset="SpartQA-Human", split=sp,
            license=LIC["SpartQA"], source=f"msu:SpartQA_Human/human_{sp}_annotation.json")
        sc_hum += s
        hum_neg += neg
    if limit_scenes:
        sc_hum = sc_hum[:limit_scenes]
    scenes["SpartQA-Human"] = sc_hum
    logger.info(f"SpartQA-Human: {len(sc_hum)} scenes ({hum_neg} negative relations excluded)")

    # ---- ReSQ (natural anchor; no recoverable scene graph) -------------------
    sc_resq = []
    for sp in ["train", "dev", "test"]:
        d = json.loads((UZ / "ReSQ" / "ReSQ" / f"{sp}_resq.json").read_text())["data"]
        sc_resq += L.load_resq(d, dataset="ReSQ", split=sp,
                               license=LIC["ReSQ"], source=f"msu:ReSQ/{sp}_resq.json")
    if limit_scenes:
        sc_resq = sc_resq[:limit_scenes]
    scenes["ReSQ"] = sc_resq
    logger.info(f"ReSQ: {len(sc_resq)} scenes")

    return scenes


# --------------------------------------------------------------------------- #
#  enumerate deduction-required query pairs for annotation-graph corpora
# --------------------------------------------------------------------------- #
def enumerate_queries(scene):
    """All connected, NOT-directly-stated node pairs = deduction-required queries.
    Deterministic order. (SpartQA: dataset FR queries reference objects by long
    compositional descriptions unresolvable without an LLM -> enumeration is the
    well-defined $0 structural-capacity query set.)"""
    import networkx as nx
    _, g = gm.scene_graphs([(e["src"], e["dst"]) for e in scene["edges"]])
    nodes = sorted(g.nodes())
    out = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            if frozenset({u, v}) in scene["stated_pairs"]:
                continue
            if not nx.has_path(g, u, v):
                continue
            out.append((u, v))
    return out


# --------------------------------------------------------------------------- #
#  score every (scene, query) -> records (full population for prevalence)
# --------------------------------------------------------------------------- #
def score_corpus(name, scenes):
    records = []
    for scene in scenes:
        edge_pairs = [(e["src"], e["dst"]) for e in scene["edges"]]
        g_full, g = gm.scene_graphs(edge_pairs)
        queries = scene["queries"]
        if name in ("SpartQA-Auto", "SpartQA-Human"):
            queries = [{"src": u, "dst": v, "gold_native": [], "gold_canonical": [],
                        "gold_algebra": "not_derived", "answer_kind": "enumerated",
                        "query_kind": "enumerated_deduction_pair",
                        "gold_recoverable": False, "dataset_num_hop": None}
                       for (u, v) in enumerate_queries(scene)]
        for qi, q in enumerate(queries):
            if q["src"] == "?" or q["src"] is None:   # ReSQ: no recoverable graph
                m = {"hop_length": -1, "num_edge_disjoint_paths": 0,
                     "num_edge_disjoint_paths_with_root": 0,
                     "num_disjoint_paths_len_ge2": 0, "disjoint_path_lengths": [],
                     "second_path_length": -1, "cyclomatic_number": 0,
                     "deduction_required": True, "genuine_multipath_with_bite": False,
                     "genuine_multipath_with_bite_tight": False,
                     "connected": False, "n_nodes_noroot": 0, "n_edges_noroot": 0}
            else:
                m = gm.query_metrics_on(g_full, g, q["src"], q["dst"], scene["stated_pairs"])
            records.append({"scene": scene, "query": q, "qi": qi, "metrics": m})
    return records


# --------------------------------------------------------------------------- #
#  prevalence aggregation
# --------------------------------------------------------------------------- #
def _band(frac):
    if frac >= 0.10:
        return "general (>=10%)"
    if frac >= 0.05:
        return "useful_module (5-10%)"
    return "niche (<5%)"


def prevalence_row(name, records, scenes):
    n = len(records)
    if n == 0:
        return None
    ded = [r for r in records if r["metrics"]["deduction_required"]]
    bite = [r for r in records if r["metrics"]["genuine_multipath_with_bite"]]
    bite_t = [r for r in records if r["metrics"]["genuine_multipath_with_bite_tight"]]
    ge2 = [r for r in records if r["metrics"]["num_edge_disjoint_paths"] >= 2]
    conn = [r for r in records if r["metrics"]["connected"]]
    hops = [r["metrics"]["hop_length"] for r in conn]
    mus = [r["metrics"]["cyclomatic_number"] for r in records]
    cyc_or_long = [r for r in records
                   if r["metrics"]["hop_length"] >= 3 or r["metrics"]["cyclomatic_number"] >= 1]
    n_ded = len(ded)
    frac_bite_ded = (len(bite) / n_ded) if n_ded else 0.0
    # document length
    clen = [len(s["text"]) for s in scenes]
    reaches = sum(1 for c in clen if c >= THREE_K)
    is_tmpl = scenes[0]["is_templated"] if scenes else None
    is_nat = scenes[0]["is_natural_text"] if scenes else None
    return {
        "corpus": name,
        "is_templated": is_tmpl, "is_natural_text": is_nat,
        "n_scenes": len(scenes),
        "n_evaluable_queries": n,
        "frac_deduction_required": round(n_ded / n, 4),
        "frac_ge2_edge_disjoint_paths": round(len(ge2) / n, 4),
        "n_genuine_multipath_with_bite": len(bite),
        "frac_bite_of_all_queries": round(len(bite) / n, 4),
        "frac_bite_of_deduction_required": round(frac_bite_ded, 4),
        "applicability_band_(on_deduction_required)": _band(frac_bite_ded),
        "n_bite_tight": len(bite_t),
        "frac_bite_tight_of_deduction_required": round(len(bite_t) / n_ded, 4) if n_ded else 0.0,
        "band_tight_(on_deduction_required)": _band((len(bite_t) / n_ded) if n_ded else 0.0),
        "frac_connected": round(len(conn) / n, 4),
        "mean_hop_length": round(statistics.mean(hops), 3) if hops else None,
        "median_hop_length": statistics.median(hops) if hops else None,
        "mean_cyclomatic_number": round(statistics.mean(mus), 3) if mus else 0.0,
        "frac_hop_ge3_or_cyclic": round(len(cyc_or_long) / n, 4),
        "doc_char_len_mean": round(statistics.mean(clen), 1) if clen else 0,
        "doc_char_len_median": int(statistics.median(clen)) if clen else 0,
        "doc_char_len_max": max(clen) if clen else 0,
        "frac_reaching_3000_char_target": round(reaches / len(clen), 4) if clen else 0.0,
    }


# --------------------------------------------------------------------------- #
#  relation-vocabulary coverage ledger
# --------------------------------------------------------------------------- #
def vocab_ledger(scenes_by_corpus):
    """Relation-vocabulary coverage ledger.  Each edge is classified by the
    algebra computed at load time (authoritative).  Token-level breakdown re-maps
    native tokens EXCEPT for StepGame, whose native_relation is a raw sentence
    (~100 paraphrase templates) -- there we rely on the per-edge cardinal tag and
    report tokeniser coverage separately so the card is honest, not misleading."""
    from collections import Counter, defaultdict
    from algebra import map_relation
    rcc8, cdc, dist, depth, unmapped = Counter(), Counter(), Counter(), Counter(), Counter()
    by_corpus = defaultdict(lambda: {"rcc8": 0, "cardinal_direction": 0,
                                     "mixed": 0, "unmapped": 0, "n_edges": 0})
    step_cov = {"tokenised": 0, "raw_sentence_only": 0}
    for name, scenes in scenes_by_corpus.items():
        for s in scenes:
            for e in s["edges"]:
                by_corpus[name]["n_edges"] += 1
                by_corpus[name][e.get("algebra", "unmapped")] += 1
                if name == "StepGame-clean":
                    step_cov["tokenised" if e.get("tokenised") else "raw_sentence_only"] += 1
                    continue  # native is a sentence; tag is authoritative
                for nat in e["native_relation"]:
                    mm = map_relation(str(nat))
                    key = str(nat).lower().strip()
                    if mm["algebra"] == "rcc8":
                        rcc8[key] += 1
                    elif mm["algebra"] == "cardinal_direction":
                        (dist if mm["subtype"] == "distance"
                         else depth if mm["subtype"] == "depth_out_of_cdc"
                         else cdc)[key] += 1
                    else:
                        unmapped[key] += 1
    return {
        "rcc8_tokens": dict(rcc8.most_common()),
        "cardinal_direction_tokens": dict(cdc.most_common()),
        "distance_tokens": dict(dist.most_common()),
        "depth_out_of_cdc_tokens": dict(depth.most_common()),
        "unmapped_tokens": dict(unmapped.most_common(40)),
        "stepgame_tokeniser_coverage": step_cov,
        "per_corpus_edge_algebra_counts": {k: v for k, v in by_corpus.items()},
    }


# --------------------------------------------------------------------------- #
#  emit exp_sel_data_out rows (input=str, output=str, metadata_*)
# --------------------------------------------------------------------------- #
def _stratified_emit(records, cap):
    """Keep ALL genuine-multipath-with-bite records (the rows iter-5 actually
    needs to run the cross-path-intersection test on), then fill the remaining
    budget with a deterministic stride sample of the rest.  Preserves the rare
    signal while bounding file size."""
    if cap is None or len(records) <= cap:
        return records
    bite = [r for r in records if r["metrics"]["genuine_multipath_with_bite"]]
    rest = [r for r in records if not r["metrics"]["genuine_multipath_with_bite"]]
    keep_bite = bite[:cap]
    room = max(0, cap - len(keep_bite))
    if room and rest:
        step = len(rest) / room
        keep_bite += [rest[int(i * step)] for i in range(room)]
    # restore original order for reproducibility
    idx = {id(r): k for k, r in enumerate(records)}
    return sorted(keep_bite, key=lambda r: idx[id(r)])


def build_examples(name, records):
    cap = CFG[name]["emit_cap"]
    sel = _stratified_emit(records, cap)
    examples = []
    for r in sel:
        s, q, m = r["scene"], r["query"], r["metrics"]
        nodes = [{"node_id": nid, **nd} for nid, nd in sorted(s["nodes"].items())]
        output = {
            "nodes": nodes,
            "edges": s["edges"],
            "query_edge": {
                "src": q["src"], "dst": q["dst"],
                "gold_native_relation": q.get("gold_native", []),
                "gold_canonical": q.get("gold_canonical", []),
                "gold_algebra": q.get("gold_algebra"),
                "answer_kind": q.get("answer_kind"),
                "query_kind": q.get("query_kind"),
                "gold_recoverable": q.get("gold_recoverable", False),
                "is_universal_option": True,  # query edge is held-out / universal
                "dataset_num_hop": q.get("dataset_num_hop"),
                **m,
            },
        }
        ex = {
            "input": s["text"],
            "output": json.dumps(output, ensure_ascii=False),
            "metadata_id": f"{s['doc_id']}_q{r['qi']}",
            "metadata_dataset": s["dataset"],
            "metadata_doc_id": s["doc_id"],
            "metadata_split": s["split"],
            "metadata_is_templated": s["is_templated"],
            "metadata_is_natural_text": s["is_natural_text"],
            "metadata_doc_char_len": len(s["text"]),
            "metadata_reaches_3000_char_target": len(s["text"]) >= THREE_K,
            "metadata_algebras_present": sorted({e["algebra"] for e in s["edges"]
                                                 if e["algebra"] != "unmapped"}),
            "metadata_native_relation_vocab": sorted({str(x) for e in s["edges"]
                                                      for x in e["native_relation"]})[:60],
            "metadata_license": s["license"],
            "metadata_source": s["source"],
            "metadata_fold": f"{s['dataset']}::{s['doc_id']}",
            "metadata_query_kind": q.get("query_kind"),
            "metadata_answer_kind": q.get("answer_kind"),
            "metadata_gold_recoverable": q.get("gold_recoverable", False),
            "metadata_char_spans_recoverable": s.get("char_spans_recoverable", False),
            "metadata_stated_graph_recoverable": s.get("stated_graph_recoverable", True),
            "metadata_hop_length": m["hop_length"],
            "metadata_num_edge_disjoint_paths": m["num_edge_disjoint_paths"],
            "metadata_num_edge_disjoint_paths_with_root": m["num_edge_disjoint_paths_with_root"],
            "metadata_cyclomatic_number": m["cyclomatic_number"],
            "metadata_deduction_required": m["deduction_required"],
            "metadata_genuine_multipath_with_bite": m["genuine_multipath_with_bite"],
            "metadata_dataset_num_hop": q.get("dataset_num_hop"),
        }
        examples.append(ex)
    return examples


@logger.catch(reraise=True)
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit-scenes", type=int, default=None,
                    help="cap scenes per corpus (scaling/testing)")
    ap.add_argument("--out", default=str(ROOT / "full_data_out.json"))
    args = ap.parse_args()

    logger.info("=== loading corpora ===")
    scenes_by_corpus = load_all(limit_scenes=args.limit_scenes)

    logger.info("=== scoring multi-path metrics ===")
    # ALL 6 corpora are EVALUATED for the prevalence table (the gate's whole point
    # is the cross-corpus comparison, incl. the SpaRP-PS2 verify-empirically finding);
    # only the CHOSEN-4 STANDARDIZED corpora are EMITTED into datasets[].
    CHOSEN_4 = ["SpaRP-PS1", "SpartQA-Human", "StepGame-clean", "ReSQ"]
    prevalence, datasets_out = [], []
    for name in ["SpaRP-PS1", "SpaRP-PS2", "SpartQA-Human", "StepGame-clean",
                 "SpartQA-Auto", "ReSQ"]:
        scenes = scenes_by_corpus[name]
        records = score_corpus(name, scenes)
        logger.info(f"{name}: {len(records)} evaluable queries from {len(scenes)} scenes")
        pr = prevalence_row(name, records, scenes)
        if pr:
            pr["role"] = "standardized" if name in CHOSEN_4 else "evaluated_extra"
            prevalence.append(pr)
            logger.info(f"  [{pr['role']}] bite_of_deduction={pr['frac_bite_of_deduction_required']} "
                        f"band={pr['applicability_band_(on_deduction_required)']} "
                        f"mean_hop={pr['mean_hop_length']}")
        if name not in CHOSEN_4:
            continue  # evaluated-extra: prevalence only, NOT emitted into datasets[]
        examples = build_examples(name, records)
        if examples:
            datasets_out.append({"dataset": name, "examples": examples,
                                 "n_full_population": len(records),
                                 "n_emitted": len(examples)})

    # strip helper keys not allowed by schema (dataset/examples only at this level
    # is fine -- schema allows additionalProperties at dataset level? NO -> keep
    # only dataset+examples; stash counts in top metadata)
    emit_counts = {d["dataset"]: {"n_full_population": d.pop("n_full_population"),
                                  "n_emitted": d.pop("n_emitted")} for d in datasets_out}

    vocab = vocab_ledger(scenes_by_corpus)

    out = {
        "metadata": {
            "artifact": "SPATIAL multi-path-redundant gold-QCN corpus (iter-4 dataset_1)",
            "description": "Per-scene gold spatial relation-graphs with a DESCRIPTIVE "
                           "multi-path-redundancy prevalence annotation (the spatial "
                           "analog of the temporal a-priori N* gate). No closure, no LLM. "
                           "datasets[] contains the 4 STANDARDIZED corpora; prevalence_table "
                           "covers all 6 EVALUATED corpora (4 standardized + 2 evaluated extras).",
            "schema_note": "input=story text; output=JSON {nodes,edges,query_edge}; "
                           "structural metrics also surfaced as metadata_* fields.",
            "root_node_handling": "world/image container id '-1' excluded from the "
                                  "primary structural graph (non-constraining containment).",
            "applicability_bands": ">=10% bite=general; 5-10%=useful module; <5%=niche "
                                   "(on deduction-required queries).",
            "primary_4_standardized": ["SpaRP-PS1", "SpartQA-Human", "StepGame-clean", "ReSQ"],
            "primary_4_rationale": "The BEST-4 span the four qualitatively distinct "
                "text-type x structure regimes the gate must characterise: SpaRP-PS1 = "
                "dense-templated HIGH-redundancy venue (27.4% tight bite, general); "
                "SpartQA-Human = semi-natural/human MODEST redundancy (useful-module band); "
                "StepGame-clean = single-chain ZERO-by-construction contrast; ReSQ = "
                "genuinely-natural anchor (no recoverable scene graph => natural boundary).",
            "evaluated_extras": ["SpaRP-PS2", "SpartQA-Auto"],
            "evaluated_extras_note": "SpaRP-PS2 (StepGame-Ext): 10.4% raw but 0.9% TIGHT "
                "bite -- redundancy is mostly long loose paths (verify-empirically finding). "
                "SpartQA-Auto: large templated dense sample, 3.5% bite (niche).",
            "emission_counts": emit_counts,
            "prevalence_table": prevalence,
            "relation_vocab_ledger": vocab,
        },
        "datasets": datasets_out,
    }

    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=1))
    # standalone analysis sidecar (full prevalence + vocab) for the card
    (ROOT / "analysis_out.json").write_text(json.dumps(
        {"prevalence_table": prevalence, "emission_counts": emit_counts,
         "relation_vocab_ledger": vocab}, ensure_ascii=False, indent=1))
    total = sum(len(d["examples"]) for d in datasets_out)
    logger.info(f"WROTE {args.out}: {len(datasets_out)} datasets, {total} examples")
    logger.info("=== prevalence summary ===")
    for pr in prevalence:
        logger.info(f"  {pr['corpus']:<16} q={pr['n_evaluable_queries']:<6} "
                    f"bite={pr['frac_bite_of_deduction_required']:<7} "
                    f"{pr['applicability_band_(on_deduction_required)']}")


if __name__ == "__main__":
    main()
