#!/usr/bin/env python3
"""Assemble the final exp_sel_data_out dataset file from build.run(), attach top-level
metadata (composition table verbatim, provenance, QA, char-length distribution), and
emit full/mini/preview variants."""
from __future__ import annotations
import json, os, resource, statistics as st, time, logging

from build import run, CT, PROP2PRIM, COMPOSED_ONLY, KIN

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("assemble")
WORK = os.path.dirname(os.path.abspath(__file__))

REDOCRED_SHA = "e0ab3489edfe72c968261bffed5243b6fefddd22"
DOCRED_SHA = "7985b4e0371e6c61a756feb41b7b27becf71c666"


def corpus_charlen_summary(rows):
    cl = sorted(r["metadata_char_len"] for r in rows)
    if not cl:
        return {}
    n = len(cl)
    return {
        "n_docs": n, "min": cl[0], "median": st.median(cl), "mean": round(st.mean(cl), 1),
        "max": cl[-1],
        "frac_ge_2000": round(sum(c >= 2000 for c in cl) / n, 4),
        "frac_ge_2500": round(sum(c >= 2500 for c in cl) / n, 4),
        "frac_ge_3000": round(sum(c >= 3000 for c in cl) / n, 4),
        "frac_in_2000_4000": round(sum(2000 <= c <= 4000 for c in cl) / n, 4),
        "n_in_2000_4000": sum(2000 <= c <= 4000 for c in cl),
        "n_ge_3000": sum(c >= 3000 for c in cl),
    }


def qa_cue_check(rows, source):
    """7a: among atomic edges flagged locally_justifiable, confirm the recorded cue is
    truly present in the support-span text of the document (sanity, should be 100%);
    also report overall locally-justifiable fraction (readability / non-circularity audit)."""
    checked = 0; passed = 0; n_edges = 0; n_just = 0
    for r in rows:
        if r["metadata_source"] != source:
            continue
        gg = json.loads(r["output"])
        text = r["input"].lower()
        for e in gg["atomic_edges"]:
            n_edges += 1
            if e["locally_justifiable"]:
                n_just += 1
                cue = e["surface_cue"]
                sp = e["support_span"]
                span = text[sp[0]:sp[1]]
                checked += 1
                if cue and cue in span:
                    passed += 1
    return {"locally_justifiable_edges_checked": checked,
            "cue_present_pass_rate": round(passed / checked, 4) if checked else None,
            "n_atomic_edges": n_edges, "n_locally_justifiable": n_just,
            "locally_justifiable_frac": round(n_just / n_edges, 4) if n_edges else None}


def main():
    resource.setrlimit(resource.RLIMIT_AS, (24 * 1024**3, 24 * 1024**3))
    t0 = time.time()
    rows_by_source, stats = run(["re-docred", "docred"])
    log.info("built in %.1fs; stats=%s", time.time() - t0, json.dumps(stats))

    datasets = []
    for source in ["re-docred", "docred"]:
        rows = rows_by_source[source]
        datasets.append({"dataset": source, "examples": rows})

    # completeness-correction evidence: family-edge & absent-pair counts on SHARED titles
    def by_title(rows):
        return {r["metadata_doc_id"]: r for r in rows}
    red_t = by_title(rows_by_source["re-docred"])
    doc_t = by_title(rows_by_source["docred"])
    shared = sorted(set(red_t) & set(doc_t))
    red_edges = sum(red_t[t]["metadata_n_atomic_edges"] for t in shared)
    doc_edges = sum(doc_t[t]["metadata_n_atomic_edges"] for t in shared)
    red_abs = sum(red_t[t]["metadata_absent_pair_count"] for t in shared)
    doc_abs = sum(doc_t[t]["metadata_absent_pair_count"] for t in shared)
    completeness_evidence = {
        "shared_titles": len(shared),
        "re-docred_family_edges_on_shared": red_edges,
        "docred_family_edges_on_shared": doc_edges,
        "extra_family_edges_recovered_by_re-docred": red_edges - doc_edges,
        "re-docred_absent_pairs_on_shared": red_abs,
        "docred_absent_pairs_on_shared": doc_abs,
        "interpretation": ("Re-DocRED recovers many family edges DocRED missed (false negatives); "
            "those missing edges would otherwise turn genuinely-related pairs into SPURIOUS absent "
            "pairs and erase derivable present queries -- which is exactly why absent gold is only "
            "trustworthy on the Re-DocRED (completeness-corrected) slice."),
    }

    all_rows = rows_by_source["re-docred"] + rows_by_source["docred"]
    qa = {s: qa_cue_check(all_rows, s) for s in ["re-docred", "docred"]}
    charlen = {s: corpus_charlen_summary(rows_by_source[s]) for s in ["re-docred", "docred"]}
    mean_offset = {s: round(st.mean([r["metadata_offset_ok_frac"] for r in rows_by_source[s]]), 4)
                   for s in ["re-docred", "docred"] if rows_by_source[s]}

    metadata = {
        "name": "Natural-Text Absent-Relation Kinship Corpus (Re-DocRED + DocRED)",
        "description": (
            "Document-level kinship corpus built from genuinely-natural Wikipedia "
            "introductory prose (Re-DocRED, the completeness-corrected re-annotation of "
            "DocRED). One row per document, exp_sel_data_out schema, drop-in compatible "
            "with the CLUTRR kinship dataset (same finite composition table + forward "
            "least-fixpoint UNION closure engine, kinship.py). Each document yields atomic "
            "span-local family edges (readable), deduction-required multi-hop PRESENT "
            "query edges (gold by CLUTRR-table composition; composed_only types are outside "
            "DocRED's relation inventory => provably non-circular), and genuine within-document "
            "ABSENT (no-derivation) pairs from disconnected kinship components."),
        "schema": ("exp_sel_data_out: input=detokenized document text; output=json.dumps(gold_graph); "
                   "structured per-row data under metadata_* keys."),
        "gold_graph_field_spec": {
            "doc_id": "Wikipedia article title (DocRED title).",
            "source": "'re-docred' (completeness-corrected, trustworthy absent gold) or 'docred' (vanilla; absent gold DOWNGRADED).",
            "split": "original DocRED split: train|dev|test.",
            "nodes": "[{entity_id (vertexSet index), surface (longest mention), type (majority mention NER type, ~PER), gender ('male'|'female'|null, best-effort), mention_spans=[[char_start,char_end),...] into input, wikidata_qid=null (DocRED vertexSet carries no QIDs)}].",
            "atomic_edges": "ALL annotated family edges = the KB / proof chain; {source,target,kinship_relation (surface, gendered if known else neutral),primitive (CLUTRR type),relation_type (=primitive),target_gender,is_query=false,hop_count=1,support_span=[cs,ce),surface_cue,evidence_sent_ids,locality,has_cue,locally_justifiable,wikidata_property}. Directed: edge source->target with type=primitive means 'target is source's primitive'. locally_justifiable = a span-local reader can plausibly extract it (mentions in adjacent sentences AND a surface kinship cue present).",
            "query_edges": "held-out PRESENT deduction-required pairs (NO direct annotated edge, NO local co-occurrence within 1 sentence) with a derivable >=2-hop composition yielding a unique relation; {source,target,kinship_relation (gold surface or null if target gender unknown),primitive (robust gold),relation_type,target_gender,target_int (CLUTRR label-map id or null),is_query=true,hop_count (shortest undirected path length),derivation_path (intermediate entity_ids),composed_only (primitive outside DocRED inventory => non-circular),fully_readable (every edge on the derivation path is locally_justifiable)}.",
            "absent_relation_pairs": "[{source,target,reason='different_component',is_absent=true}] -- both entities participate in >=1 family relation but lie in DIFFERENT connected components => no kinship path. Conservative CLOSED-WORLD label within the document. Capped at 30/document.",
            "absent_pairs_source": "structural_components",
        },
        "composition_table": CT,
        "composition_table_note": ("FINITE KINSHIP COMPOSITION TABLE, NOT a relation algebra "
            "(no general intersection/converse closure beyond these rules). Emitted verbatim "
            "from the CLUTRR rules_store.yaml primitive compositions + relations_store.yaml "
            "surface<->primitive<->gender map. SAME table every kinship arm uses; iter-7 runs "
            "the kinship.py forward least-fixpoint UNION closure engine unchanged."),
        "engine_edge_mapping": {
            "note": "To feed kinship.py forward_closure(KIN, atomic_edges), map each atomic_edge to {a:source, b:target, type:primitive}.",
            "a": "source", "b": "target", "type": "primitive"},
        "docred_family_properties": {
            "P22": "father (->primitive inv-child, target male)", "P25": "mother (->inv-child, target female)",
            "P40": "child (->child)", "P26": "spouse (->SO, symmetric)", "P3373": "sibling (->sibling, symmetric)"},
        "plan_corrections": [
            "P1038 ('relative') is NOT in DocRED's 96-relation inventory (rel_info.json has no P1038; 0 edges across all splits) -- the plan listed it as present. It is therefore unused; no P1038-linked exclusion from the absent set is needed.",
            "DocRED train_annotated+dev contain ZERO family-bearing documents whose title is absent from Re-DocRED (Re-DocRED re-annotates all 4052 DocRED titles). The secondary 'docred' slice is therefore VANILLA-DocRED annotations on the SAME documents -- it corroborates the atomic/present strata and empirically demonstrates the completeness-correction effect on absent gold (vanilla DocRED's false-negative family edges inflate spurious absent pairs and miss present queries). iter-7 includes/excludes it via metadata_source.",
            "No genuinely-natural ready-made kinship/genealogy text corpus beat Re-DocRED: VLyb/Kinship is symbolic ids (person100/term6, REJECT non-text); HF 'genealogy' hits are tiny (<50 downloads) or synthetic (gabrielwu/genealogy_synthetic, REJECT non-natural).",
        ],
        "char_length_honesty": ("DocRED Wikipedia intro prose at this annotation density averages "
            "~1000 chars; NO family-bearing document reaches 3000 chars and only ~3% reach 2000. "
            "We do NOT concatenate or pad (that would defeat the natural-text purpose). The "
            "natural-text + absent-relation regime is the load-bearing property for iter-7, not "
            "the 3000-char target. Per-doc char_len and the [2000,4000] subset are flagged."),
        "char_length_distribution": charlen,
        "open_world_caveat": ("ABSENT labels are CLOSED-WORLD within each document: a pair in "
            "different annotated kinship components has no relation DERIVABLE from the document. "
            "Real-world distant kinship may exist but is not stated/derivable. Re-DocRED's "
            "completeness correction makes within-document 'no relation' defensible; the 'docred' "
            "slice's absent labels are LOWER confidence (vanilla false negatives)."),
        "qa": qa,
        "completeness_correction_evidence": completeness_evidence,
        "mean_offset_ok_frac": mean_offset,
        "build_stats": stats,
        "scale_targets_vs_actuals": {
            "target_present_multihop": ">=150", "actual_present_re-docred": stats["re-docred"]["present_total"],
            "target_absent_pairs": ">=300", "actual_absent_re-docred": stats["re-docred"]["absent_total"],
            "actual_composed_only_present_re-docred": stats["re-docred"]["composed_only_present"]},
        "provenance": {
            "primary_source": "tonytan48/Re-DocRED (HuggingFace dataset)",
            "primary_commit_sha": REDOCRED_SHA,
            "primary_paper": "Tan et al. 2022, 'Revisiting DocRED', arXiv:2205.12696",
            "secondary_source": "thunlp/docred (HuggingFace dataset)",
            "secondary_commit_sha": DOCRED_SHA,
            "secondary_paper": "Yao et al. 2019, 'DocRED', ACL 2019, arXiv:1906.06127",
            "composition_table_source": "CLUTRR (Sinha et al. 2019, arXiv:1908.06177) rules_store.yaml + relations_store.yaml, via dependency art_Dm5vYXmD1R8h",
            "text_substrate": "Detokenized DocRED tokenized `sents` (Wikipedia introductory prose). Char offsets recorded per token; mention spans verified (see mean_offset_ok_frac).",
            "license": "DocRED/Re-DocRED released under MIT License (Wikipedia text CC BY-SA).",
        },
        "metadata_field_glossary": {
            "metadata_fold": "deterministic 5-fold by SHA-256(input) % 5",
            "metadata_locally_justifiable_frac": "fraction of atomic family edges a span-local reader could extract (locality + surface cue)",
            "metadata_composed_only_present_count": "present queries whose gold type is outside DocRED's inventory (provably non-circular)",
            "metadata_offset_ok_frac": "fraction of entity mentions whose computed char span matches the mention surface",
            "metadata_present_truncated/metadata_absent_truncated": "whether per-doc strata were capped (present_cap=40, absent_cap=30)",
        },
    }

    out = {"metadata": metadata, "datasets": datasets}
    full_path = os.path.join(WORK, "full_data_out.json")
    json.dump(out, open(full_path, "w"), ensure_ascii=False)
    sz = os.path.getsize(full_path) / 1e6
    log.info("wrote %s (%.1f MB), datasets=%s", full_path,
             sz, {d["dataset"]: len(d["examples"]) for d in datasets})

    # mini / preview (object-shaped: truncate examples to 3 per dataset)
    def truncate(o, n=3, prev=False):
        import copy
        c = copy.deepcopy(o)
        for d in c["datasets"]:
            d["examples"] = d["examples"][:n]
        if prev:
            def tr(x):
                if isinstance(x, str):
                    return x[:200]
                if isinstance(x, list):
                    return [tr(i) for i in x]
                if isinstance(x, dict):
                    return {k: tr(v) for k, v in x.items()}
                return x
            c = tr(c)
        return c
    json.dump(truncate(out, 3, False), open(os.path.join(WORK, "mini_data_out.json"), "w"), ensure_ascii=False)
    json.dump(truncate(out, 10, True), open(os.path.join(WORK, "preview_data_out.json"), "w"), ensure_ascii=False)
    log.info("wrote mini_data_out.json + preview_data_out.json")
    return sz


if __name__ == "__main__":
    main()
