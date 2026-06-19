#!/usr/bin/env python3
"""Build canonical fold-split gold temporal relation graphs for NarrativeTime, TDDMan and
MATRES (+ optional TimeBank-Dense), and emit a schema-ready data_out.json.

One row per (corpus, document):
    input  = full document text (string)
    output = json.dumps(gold_graph)   (schema requires strings)
    metadata_* = corpus / doc_id / fold / quick counts / per-doc descriptive counts
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import nltk
import networkx
from loguru import logger

import common as C
import builders as B
import counts as CNT

WS = Path(__file__).resolve().parent
DATA = WS / "temp" / "datasets"
OUT = WS

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(WS / "logs" / "run.log"), rotation="30 MB", level="DEBUG")


def build_fold_map() -> dict[str, str]:
    """norm_docid -> {train,dev,test} from the muk343 TimeBank-Dense 22/5/9 split."""
    fm = {}
    base = DATA / "TimeBank-dense"
    for split in ["train", "dev", "test"]:
        d = base / split
        if not d.exists():
            continue
        for f in d.glob("*.tml"):
            fm[C.normalize_docid(f.stem)] = split
    logger.info(f"fold map: {len(fm)} TimeBank-Dense docs ({sum(v=='train' for v in fm.values())}/"
                f"{sum(v=='dev' for v in fm.values())}/{sum(v=='test' for v in fm.values())})")
    return fm


def parse_muk343() -> dict[str, C.TmlDoc]:
    out = {}
    base = DATA / "TimeBank-dense"
    for split in ["train", "dev", "test"]:
        for f in (base / split).glob("*.tml"):
            doc = C.parse_tml(f)
            out[C.normalize_docid(doc.docid)] = doc
    logger.info(f"parsed {len(out)} TimeBank-Dense .tml documents")
    return out


def nt_reproduction_gate(nt_root: Path) -> None:
    """BLOCKING: confirm our NarrativeTime relation extraction reproduces the authors'
    shipped nt_converted_to_tml TLINKs (non-circular correctness check). Node ids differ
    (we merge real TimeML refs; shipped used a running counter), so we compare id-independent
    invariants per doc: the node count and the full relation MULTISET over all ordered pairs."""
    import collections
    import re
    sys.path.insert(0, str(nt_root))
    from narrative_time import event_relations as ER
    from narrative_time import conversion_utils as U
    anns = B._load_nt_annotations(nt_root, "a1")
    n_docs = 0
    total_tlinks = 0
    for ann in anns:
        shipped_path = nt_root / f"corpus/timebank/nt_converted_to_tml/a1/{ann['id']}.tml"
        if not shipped_path.exists():
            continue
        ev = U.get_events_and_timexes(ann, corpus_offset=0)
        mine = collections.Counter()
        n_pairs = 0
        for i1, e1 in ev.items():
            for i2, e2 in ev.items():
                if i1 == i2:
                    continue
                r = (ER.get_event_relation(e1, e2) if e1["branch"] == e2["branch"]
                     else ER.get_event_relation_separate_branches(e1, e2))
                mine[r] += 1
                n_pairs += 1
        txt = shipped_path.read_text()
        ship = collections.Counter()
        ship_nodes = set()
        for s in re.findall(r"<TLINK ([^>]*)/?>", txt):
            a = dict(re.findall(r'(\w+)="([^"]*)"', s))
            ship[a["relType"]] += 1
            ship_nodes.add(a.get("eventInstanceID") or a.get("timeID"))
            ship_nodes.add(a.get("relatedToEventInstance") or a.get("relatedToTime"))
        if len(ev) != len(ship_nodes):
            raise AssertionError(f"NT gate FAILED {ann['id']}: node count {len(ev)} != shipped {len(ship_nodes)}")
        if mine != ship:
            raise AssertionError(f"NT gate FAILED {ann['id']}: relation multiset mismatch "
                                 f"mine={dict(mine)} shipped={dict(ship)}")
        n_docs += 1
        total_tlinks += sum(ship.values())
    logger.info(f"[GATE] NarrativeTime reproduces shipped TLINK multisets for {n_docs} docs "
                f"({total_tlinks} TLINKs); node counts match ✓")


def matres_surface_gate(records: list[dict]) -> None:
    """Sanity: every non-null MATRES char offset must point exactly at the recorded surface
    (guaranteed by construction), and char-offset COVERAGE must be high (few null offsets)."""
    bad = 0
    total = 0
    null = 0
    for r in records:
        text = r["text"]
        for n in r["nodes"]:
            total += 1
            cs, ce = n["char_start"], n["char_end"]
            if cs is None:
                null += 1
                continue
            if text[cs:ce] != n["surface"]:
                bad += 1
    null_frac = null / max(total, 1)
    logger.info(f"[GATE] MATRES char offsets: {total} events, mismatches={bad}, "
                f"null(no offset)={null} ({null_frac:.3%})")
    if bad > 0:
        raise AssertionError(f"MATRES char-offset surface mismatch (should be 0 by construction): {bad}")
    if null_frac > 0.05:
        raise AssertionError(f"MATRES char-offset coverage too low: {null_frac:.3%} null")


def to_rows(records: list[dict], per_doc_counts: dict[str, dict]) -> list[dict]:
    rows = []
    for r in records:
        if not r["text"]:
            logger.warning(f"skipping empty-text doc {r['corpus']}/{r['doc_id']}")
            continue
        dc = per_doc_counts[f"{r['corpus']}::{r['doc_id']}"]
        gold_graph = {
            "doc_id": r["doc_id"],
            "corpus": r["corpus"],
            "fold": r["fold"],
            "nodes": r["nodes"],
            "edges": r["edges"],
            "per_doc_descriptive_counts": dc,
            "warnings": r.get("warnings", []),
        }
        rows.append({
            "input": r["text"],
            "output": json.dumps(gold_graph, ensure_ascii=False),
            "metadata_corpus": r["corpus"],
            "metadata_doc_id": r["doc_id"],
            "metadata_fold": r["fold"],
            "metadata_n_nodes": dc["n_nodes"],
            "metadata_n_edges": dc["n_edges"],
            "metadata_n_events": dc["n_events"],
            "metadata_long_distance_edges": dc["sentence_distance_dist"]["long_distance"],
            "metadata_descriptive_counts": dc,
        })
    return rows


def main():
    logger.info("=== building gold temporal relation graphs ===")
    nt_root = DATA / "narrative_time"

    nt_reproduction_gate(nt_root)

    fold_map = build_fold_map()
    muk = parse_muk343()
    segmenter = C.SentenceSegmenter()

    # ---- build corpora -------------------------------------------------------------
    logger.info("building NarrativeTime ...")
    nt_recs = B.build_narrativetime(nt_root, fold_map, segmenter, annotator="a1")
    logger.info(f"  NarrativeTime: {len(nt_recs)} docs")

    logger.info("building TDDMan ...")
    tdd_recs, tdd_unmatched = B.build_tddman(DATA / "TDDiscourse" / "TDDMan", muk, fold_map, segmenter)
    logger.info(f"  TDDMan: {len(tdd_recs)} docs, {len(tdd_unmatched)} unmatched (docid,eid)")

    logger.info("building MATRES ...")
    matres_recs = B.build_matres(DATA / "NeuralTemporalRelation-EMNLP19" / "data")
    logger.info(f"  MATRES: {len(matres_recs)} docs")
    matres_surface_gate(matres_recs)

    # The 3 plan-required corpora (TimeBank-Dense was an optional bonus; not emitted).
    corpora = {
        "narrativetime": nt_recs,
        "tddman": tdd_recs,
        "matres": matres_recs,
    }
    EMIT_ORDER = ["narrativetime", "tddman", "matres"]

    # ---- per-doc descriptive counts ------------------------------------------------
    logger.info("computing descriptive structural counts ...")
    per_doc_counts = {}
    agg_counts = {}
    for cname, recs in corpora.items():
        pdc = []
        for r in recs:
            dc = CNT.descriptive_counts(r)
            per_doc_counts[f"{cname}::{r['doc_id']}"] = dc
            pdc.append(dc)
        agg_counts[cname] = CNT.aggregate_counts(pdc)
        a = agg_counts[cname]
        logger.info(f"  [{cname}] docs={a['n_documents']} events={a['n_events']} "
                    f"edges={a['n_edges']} long_dist_frac={a['long_distance_fraction']} "
                    f"ee_triangles={a['structure_event_event_informative'].get('n_triangles',0)} "
                    f"ee_path>=3={a['structure_event_event_informative'].get('n_pairs_path_len_ge3',0)}")

    # ---- doc-id overlap table ------------------------------------------------------
    norm_to_corpora = defaultdict(set)
    orig_by_norm = defaultdict(dict)
    for cname, recs in corpora.items():
        for r in recs:
            nrm = C.normalize_docid(r["doc_id"])
            norm_to_corpora[nrm].add(cname)
            orig_by_norm[nrm][cname] = r["doc_id"]
    overlap_rows = []
    for nrm in sorted(norm_to_corpora):
        cs = norm_to_corpora[nrm]
        overlap_rows.append({
            "norm_doc_id": nrm,
            "in_narrativetime": "narrativetime" in cs,
            "in_tddman": "tddman" in cs,
            "in_matres": "matres" in cs,
            "in_timebank_dense": "timebank_dense" in cs,
            "n_corpora": len(cs),
            "orig_ids": orig_by_norm[nrm],
        })
    shared_all3 = [o["norm_doc_id"] for o in overlap_rows
                   if o["in_narrativetime"] and o["in_tddman"] and o["in_matres"]]
    logger.info(f"doc-id overlap: {len(overlap_rows)} unique docs; "
                f"shared by NT&TDDMan&MATRES = {len(shared_all3)}")

    # ---- assemble datasets ---------------------------------------------------------
    datasets = []
    for cname in EMIT_ORDER:
        rows = to_rows(corpora[cname], per_doc_counts)
        datasets.append({"dataset": cname, "examples": rows})
        logger.info(f"  dataset[{cname}] -> {len(rows)} examples")

    top_meta = {
        "description": "Canonical fold-split gold temporal relation graphs over real-text "
                       "TimeML corpora (NarrativeTime, TDDMan, MATRES; + optional TimeBank-Dense). "
                       "One row per (corpus, document): input=document text, output=JSON gold graph. "
                       "DESCRIPTIVE structural counts only (no gated N*/bite/singleton-resolution).",
        "builder_versions": {"nltk": nltk.__version__, "networkx": networkx.__version__,
                             "python": sys.version.split()[0]},
        "sentence_segmentation": {
            "narrativetime": C.SentenceSegmenter.METHOD,
            "tddman": C.SentenceSegmenter.METHOD,
            "timebank_dense": C.SentenceSegmenter.METHOD,
            "matres": "qiangning_sentid (per-token sentence ids from the EMNLP19 preprocessing); "
                      "SENTDIFF used as authoritative sentence distance",
        },
        "sources": {
            "narrativetime": "https://github.com/text-machine-lab/narrative_time (Rogers et al., "
                             "NarrativeTime: Dense Temporal Annotation on a Timeline, arXiv:1908.11443). "
                             "Relations derived by the authors' own narrative_time package (event_relations + "
                             "conversion_utils), reproducing shipped nt_converted_to_tml TLINKs exactly. Annotator a1.",
            "tddman": "https://github.com/aakanksha19/TDDiscourse (TDDiscourse, Naik et al. SIGDIAL 2019), "
                      "TDDMan/ manual subset only (NOT TDDAuto). Text substrate = TimeBank-Dense .tml.",
            "matres": "https://github.com/CogComp/MATRES (Ning et al. ACL 2018) via preprocessed XML from "
                      "https://github.com/qiangning/NeuralTemporalRelation-EMNLP19 "
                      "(trainset=TimeBank+AQUAINT, testset=Platinum). Real .tml text in TempEval-3 TBAQ-cleaned.",
            "timebank_dense": "https://github.com/muk343/TimeBank-dense (Cassidy et al. ACL 2014); TLINKs as gold.",
        },
        "canonical_mappings": {
            "narrativetime_native_to_allen": B.NT_ALLEN_MAP,
            "narrativetime_native_to_point": B.NT_POINT_MAP,
            "tddman_code_map": B.TDD_CODE_MAP,
            "matres_label_to_point": B.MATRES_POINT_MAP,
            "timebank_dense_map": B.TBD_MAP,
            "allen_relations": C.ALLEN_RELATIONS,
            "point_relations": C.POINT_RELATIONS,
            "note": "canonical_relation_set is the tightest sound base-relation set; "
                    "coarse_superset_set (when present) is a coarser still-sound alternative; "
                    "startpoint_relation_set is the convex point-algebra relation over event start-points "
                    "(non-convex {<,>} widened to {<,=,>}, flagged by vague_widened).",
        },
        "fold": "Document-level fold = TimeBank-Dense 22/5/9 split (train/dev/test) for NT/TDDMan/TBD; "
                "MATRES fold = train(TimeBank+AQUAINT)/test(Platinum). TDDMan edges also carry the native "
                "per-edge split (edge_fold).",
        "iaa_context": {"narrativetime": "Krippendorff alpha ~0.68, full TLink coverage (paper).",
                        "matres": "all pairs intra/adjacent-sentence by construction (main-axis verbs).",
                        "tddman": "manual long-distance pairs not auto-inferable (non-circularity anchor)."},
        "aggregate_descriptive_counts": agg_counts,
        "doc_id_overlap": {
            "n_unique_docs": len(overlap_rows),
            "n_shared_nt_tddman_matres": len(shared_all3),
            "shared_nt_tddman_matres": shared_all3,
            "table": overlap_rows,
        },
        "coverage_gaps": {
            "tddman_unmatched_docid_eid": tdd_unmatched,
            "matres_docs_empty_text": [r["doc_id"] for r in matres_recs if not r["text"]],
        },
        "boundary_note": "DATASET provides sizes/labels/locality/triangle/cycle structural descriptors. "
                         "GATED statistics (deduction-required N*, bite-after-widening, singleton-resolution) "
                         "require composition closure / held-out-edge resolution and are the T0 experiment's job.",
    }

    out_obj = {"metadata": top_meta, "datasets": datasets}
    payload = json.dumps(out_obj, ensure_ascii=False)
    # The artifact plan names data_out.json; the aii pipeline reads full_data_out.json.
    # Write both (identical content) so either consumer works.
    for name in ("data_out.json", "full_data_out.json"):
        (OUT / name).write_text(payload)
    logger.info(f"wrote data_out.json and full_data_out.json ({len(payload)/1e6:.2f} MB)")

    # side artifacts
    (OUT / "descriptive_counts.json").write_text(json.dumps(
        {"aggregate": agg_counts, "per_doc": per_doc_counts}, ensure_ascii=False, indent=2))
    (OUT / "overlap_table.json").write_text(json.dumps(overlap_rows, ensure_ascii=False, indent=2))
    logger.info("wrote descriptive_counts.json and overlap_table.json")

    # quick console summary
    for cname in corpora:
        a = agg_counts[cname]
        logger.info(f"SUMMARY {cname}: docs={a['n_documents']} nodes={a['n_nodes']} "
                    f"edges={a['n_edges']} intra/adj/long="
                    f"{a['intra_fraction']}/{a['adjacent_fraction']}/{a['long_distance_fraction']}")


if __name__ == "__main__":
    main()
