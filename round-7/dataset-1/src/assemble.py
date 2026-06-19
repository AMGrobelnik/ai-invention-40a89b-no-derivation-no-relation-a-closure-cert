#!/usr/bin/env python3
"""Assemble the final exp_sel_data_out dataset file for the Located-In (administrative
containment) corpus from build.run(), attach top-level metadata (degenerate containment
composition table verbatim, provenance, QA, char-length distribution, completeness-correction
evidence), and emit full/mini/preview variants."""
from __future__ import annotations
import json, os, resource, statistics as st, time, logging

from build import run, CT, CORE_PROPS, OPT_PROPS, LOC_PROPS, KIN

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
        "n_in_2000_4000": sum(2000 <= c <= 4000 for c in cl),
        "n_ge_3000": sum(c >= 3000 for c in cl),
    }


def qa_cue_check(rows, source):
    """Among atomic edges flagged locally_justifiable, confirm the recorded surface cue is
    truly present in the support-span text (sanity, should be 100%); also report the overall
    locally-justifiable fraction (readability / non-circularity audit)."""
    checked = passed = n_edges = n_just = 0
    for r in rows:
        if r["metadata_source"] != source:
            continue
        gg = json.loads(r["output"])
        text = r["input"].lower()
        for e in gg["atomic_edges"]:
            n_edges += 1
            if e["locally_justifiable"]:
                n_just += 1
                cue, sp = e["surface_cue"], e["support_span"]
                checked += 1
                if cue and cue in text[sp[0]:sp[1]]:
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

    datasets = [{"dataset": s, "examples": rows_by_source[s]} for s in ["re-docred", "docred"]]

    # completeness-correction evidence on SHARED titles (re-docred recovers DocRED false negatives)
    def by_title(rows):
        return {r["metadata_doc_id"]: r for r in rows}
    red_t, doc_t = by_title(rows_by_source["re-docred"]), by_title(rows_by_source["docred"])
    shared = sorted(set(red_t) & set(doc_t))
    red_edges = sum(red_t[t]["metadata_n_atomic_edges"] for t in shared)
    doc_edges = sum(doc_t[t]["metadata_n_atomic_edges"] for t in shared)
    red_abs = sum(red_t[t]["metadata_absent_pair_count"] for t in shared)
    doc_abs = sum(doc_t[t]["metadata_absent_pair_count"] for t in shared)
    red_pres = sum(red_t[t]["metadata_present_query_count"] for t in shared)
    doc_pres = sum(doc_t[t]["metadata_present_query_count"] for t in shared)
    completeness_evidence = {
        "shared_titles": len(shared),
        "re-docred_locatedin_edges_on_shared": red_edges,
        "docred_locatedin_edges_on_shared": doc_edges,
        "extra_locatedin_edges_recovered_by_re-docred": red_edges - doc_edges,
        "pct_extra": round(100 * (red_edges - doc_edges) / doc_edges, 1) if doc_edges else None,
        "re-docred_absent_pairs_on_shared": red_abs, "docred_absent_pairs_on_shared": doc_abs,
        "re-docred_present_queries_on_shared": red_pres, "docred_present_queries_on_shared": doc_pres,
        "interpretation": ("Re-DocRED recovers many located-in edges DocRED missed (false "
            "negatives). Those missing edges would otherwise (a) turn genuinely-contained pairs "
            "into SPURIOUS absent pairs and (b) erase derivable present queries. This is exactly "
            "why absent gold is TRUSTWORTHY only on the Re-DocRED (completeness-corrected) slice; "
            "the vanilla 'docred' slice's absent gold is DOWNGRADED."),
    }

    all_rows = rows_by_source["re-docred"] + rows_by_source["docred"]
    qa = {s: qa_cue_check(all_rows, s) for s in ["re-docred", "docred"]}
    charlen = {s: corpus_charlen_summary(rows_by_source[s]) for s in ["re-docred", "docred"]}
    mean_offset = {s: round(st.mean([r["metadata_offset_ok_frac"] for r in rows_by_source[s]]), 4)
                   for s in ["re-docred", "docred"] if rows_by_source[s]}

    metadata = {
        "name": "Natural-Text Absent-Relation Located-In (Administrative Containment) Corpus (Re-DocRED + DocRED)",
        "description": (
            "Document-level GEOGRAPHIC / ADMINISTRATIVE CONTAINMENT ('located-in') corpus built "
            "from genuinely-natural Wikipedia introductory prose (Re-DocRED, the completeness-"
            "corrected re-annotation of DocRED). The structural TWIN of the natural-kinship "
            "corpus: a SECOND genuinely-natural absent-relation domain showing the closure-"
            "certificate confidence-blindness diagnostic is NOT kinship-specific. One row per "
            "document, exp_sel_data_out schema, drop-in compatible with the kinship closure "
            "engine (kinship.py) reused VERBATIM under a DEGENERATE single-relation TRANSITIVE "
            "composition table (located_in o located_in = located_in; contains o contains = "
            "contains; everything else UNDEFINED). Each document yields atomic span-local "
            "located_in edges (readable), deduction-required multi-hop PRESENT query edges (two "
            "honest sub-types: rare never-annotated transitive pairs + held-out redundant edges "
            "ablated at query time), and genuine within-document ABSENT (no-derivation) pairs in "
            "two regimes (different-component + same-component-sibling)."),
        "schema": ("exp_sel_data_out: input=detokenized document text; output=json.dumps(gold_graph); "
                   "structured per-row data under metadata_* keys."),
        "gold_graph_field_spec": {
            "doc_id": "Wikipedia article title (DocRED title).",
            "source": "'re-docred' (completeness-corrected, TRUSTWORTHY absent gold) or 'docred' (vanilla; absent gold DOWNGRADED).",
            "split": "original DocRED split: train|dev|test.",
            "nodes": "[{entity_id (vertexSet index), surface (longest mention), type (majority NER type = LOC by filter), admin_level ('country'|'region'|'city'|'other', best-effort cue heuristic, non-load-bearing), mention_spans=[[char_start,char_end),...] into input, wikidata_qid=null}].",
            "atomic_edges": "ALL kept located_in edges = the KB / proof chain; {source,target,relation_surface='located in',primitive='located_in',relation_type='located_in',is_query=false,hop_count=1,support_span=[cs,ce),surface_cue,evidence_sent_ids,locality,has_cue,locally_justifiable,wikidata_property (primary),wikidata_properties (all contributing),core_property (>=1 of P131/P17/P150/P1376/P36),inverted (direction flipped from the annotated triple, i.e. from P150/P36)}. Directed: edge source->target means 'source is located_in target' (source = sub-region/descendant). locally_justifiable = a span-local reader can plausibly extract it (mentions in adjacent sentences AND a surface containment cue present).",
            "query_edges": "held-out PRESENT deduction-required pairs, gold primitive='located_in'. {source,target,relation_surface,primitive,relation_type,is_query=true,hop_count(>=2 undirected/alt-path),derivation_path (intermediate entity_ids),query_kind,held_out_edge,composed_only,fully_readable,path_uses_optional_property}. query_kind='never_annotated': the pair is NOT a directly-annotated edge and does not co-occur within adjacent sentences -> composed_only=true (never an annotated edge => non-circular, the strict kinship analog; RARE here, see card). query_kind='held_out': a directly-annotated located_in edge that is ALSO independently derivable via an ALTERNATIVE >=2-hop directed path through OTHER edges (a redundant edge) and is NON-LOCAL -> composed_only=false; held_out_edge=true means the consumer MUST drop the single (source,target) atomic edge before querying, after which the engine deduces located_in. Gold is doubly certified (annotated AND derivable). Removing a redundant edge preserves the full transitive closure, so all absent/other-present gold is unchanged.",
            "absent_relation_pairs": "[{source,target,reason,is_absent=true,same_component}] -- both entities participate in the located_in graph but have NO containment path in EITHER direction (closed-world within the document). reason='different_component' (totally unrelated places, the clean kinship-analog) OR 'same_component_sibling' (under a common container but neither inside the other, e.g. two cities in one country -- the containment-specific, reviewer-named regime). Stratified-capped at 30/document.",
            "absent_pairs_source": "structural_closure",
            "contradiction_pairs": "[{pair,props_ab,props_ba}] annotated 2-cycles (located_in BOTH ways) dropped from the KB (rare; logged for transparency).",
        },
        "composition_table": CT,
        "composition_table_note": CT["note"],
        "engine_edge_mapping": {
            "note": "To feed kinship.py forward_closure(KIN, atomic_edges), map each atomic_edge to {a:source, b:target, type:primitive}. For a held_out query, FIRST drop the single atomic edge whose (source,target)==(query.source,query.target), THEN run the closure.",
            "a": "source", "b": "target", "type": "primitive"},
        "docred_locatedin_properties": {
            "P131": "located in the administrative territorial entity (h located_in t) [CORE]",
            "P17": "country (h located_in t) [CORE]",
            "P150": "contains administrative territorial entity (h contains t => INVERT to t located_in h) [CORE]",
            "P1376": "capital of (h is capital of t => h located_in t) [CORE]",
            "P36": "capital (t is capital of h => INVERT to t located_in h) [CORE]",
            "P276": "location (h located_in t) [OPTIONAL, lower precision; ~0 LOC-LOC on re-docred so contributes nothing there]",
            "core_properties": sorted(CORE_PROPS), "optional_properties": sorted(OPT_PROPS),
            "entity_type_filter": "both endpoints must have majority NER type LOC.",
        },
        "present_stratum_note": (
            "Unlike kinship -- whose composed types (grandfather/uncle/...) are OUTSIDE DocRED's "
            "relation inventory and therefore yield abundant never-annotated present queries -- "
            "located_in is a SINGLE relation that DocRED annotates near-TRANSITIVELY (a place's "
            "country P17 is almost always stated directly). So pure never-annotated transitive "
            "pairs are RARE (a directly-measured, honest domain difference). The bulk of the "
            "present-deduction stratum is therefore the HELD-OUT sub-type: directly-annotated "
            "redundant edges that are independently derivable via an alternative >=2-hop path and "
            "are non-local, withheld at query time -- a KG-completion-style deduction query with "
            "doubly-certified gold. This domain difference is itself a reportable generality "
            "finding: the ABSENT regime transfers cleanly; the present-DERIVATION regime is "
            "domain-shaped."),
        "plan_corrections": [
            "PRESENT-query construction CHANGED vs the plan's STEP 4f. The plan assumed never-annotated transitive pairs (the kinship analog) would be plentiful; they are NOT, because DocRED annotates geographic containment near-transitively (measured: of ~2000 derivable singleton located_in pairs in a 267-doc sample, ~1997 are DIRECTLY annotated; only ~9 are never-annotated). The present stratum is therefore built primarily from a HELD-OUT redundant-edge sub-type (sound because removing a redundant edge preserves the transitive closure), with the rare never-annotated pairs kept as a pure composed_only sub-type. Both are deduction-required and non-local.",
            "P276 'location' contributes ~0 LOC-LOC edges on re-docred (it links non-LOC entities); the LOC-LOC entity-type filter removes it cleanly there. It is kept in the mapping (lower-precision, core_property=false) and contributes a small number of edges only on the docred slice.",
            "P30 'continent', P706 'located on terrain feature', P205 'basin country' are NOT used in the primary build (reserved fallback F1). Their LOC-LOC availability is large (P30~1087, P706~488, P205~272 on re-docred) but they are looser containment; CORE {P131,P17,P150,P1376,P36} already yields a dense corpus, so they are omitted to keep gold trustworthy.",
            "atomic edges are capped per document (atomic_cap=80, core-first) so a dense geography article cannot dominate; the participating set is recomputed from the kept edges. (Caps almost never bind.)",
        ],
        "char_length_honesty": ("DocRED Wikipedia intro prose averages ~1000 chars; essentially NO "
            "document reaches 3000 chars. We do NOT concatenate or pad (that would defeat the "
            "natural-text purpose). The natural-text + absent-relation regime is the load-bearing "
            "property, not the 3000-char target. Per-doc char_len and the [2000,4000] subset are flagged."),
        "char_length_distribution": charlen,
        "open_world_caveat": ("ABSENT labels are CLOSED-WORLD within each document: a pair with no "
            "containment path DERIVABLE from the annotated graph. Real-world distant containment "
            "may exist but is not stated/derivable. Re-DocRED's completeness correction makes "
            "within-document 'no containment' defensible; the 'docred' slice's absent labels are "
            "LOWER confidence (vanilla false negatives)."),
        "located_in_caveats": [
            "Administrative-hierarchy ambiguity: containers can be administrative (P131) or by-country (P17); both are collapsed to located_in.",
            "Multi-parent DAG: an entity may be located in several containers (e.g. an admin parent AND its country); the closure is a partial order over a DAG, not a strict tree -- handled correctly by the union fixpoint.",
            "Country-vs-region granularity is not normalized; admin_level is a best-effort, non-load-bearing stratifier.",
            "P276 'location' is lower precision (kept tagged core_property=false; ~0 on re-docred).",
            "same_component_sibling absent pairs assume the document's annotated containment graph is complete enough that two co-component places with no ancestor/descendant path are genuinely not nested -- defensible under Re-DocRED, downgraded under DocRED.",
        ],
        "qa": qa,
        "completeness_correction_evidence": completeness_evidence,
        "mean_offset_ok_frac": mean_offset,
        "build_stats": stats,
        "scale_targets_vs_actuals": {
            "target_present_multihop": ">=150 (plan); achieved via held-out sub-type",
            "actual_present_re-docred": stats["re-docred"]["present_total"],
            "actual_present_never_annotated_re-docred": stats["re-docred"]["present_never_annotated"],
            "actual_present_held_out_re-docred": stats["re-docred"]["present_held_out"],
            "target_absent_pairs": ">=300 (plan)",
            "actual_absent_re-docred": stats["re-docred"]["absent_total"],
            "actual_absent_different_component_re-docred": stats["re-docred"]["absent_different_component"],
            "actual_absent_same_component_sibling_re-docred": stats["re-docred"]["absent_same_component_sibling"]},
        "provenance": {
            "primary_source": "tonytan48/Re-DocRED (HuggingFace dataset)",
            "primary_commit_sha": REDOCRED_SHA,
            "primary_paper": "Tan et al. 2022, 'Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction', EMNLP 2022, arXiv:2205.12696",
            "secondary_source": "thunlp/docred (HuggingFace dataset)",
            "secondary_commit_sha": DOCRED_SHA,
            "secondary_paper": "Yao et al. 2019, 'DocRED: A Large-Scale Document-Level Relation Extraction Dataset', ACL 2019, arXiv:1906.06127",
            "composition_table_source": "DEGENERATE single-relation transitive table authored here (containment_composition_table.json); NO CLUTRR kinship table is used -- the geographic primitive is its own. The kinship.py ENGINE is reused verbatim.",
            "text_substrate": "Detokenized DocRED tokenized `sents` (Wikipedia introductory prose). Char offsets recorded per token; mention spans verified (see mean_offset_ok_frac).",
            "license": "DocRED/Re-DocRED released under MIT License (Wikipedia text CC BY-SA).",
        },
        "metadata_field_glossary": {
            "metadata_fold": "deterministic 5-fold by SHA-256(input) % 5",
            "metadata_n_entities/metadata_n_loc_entities": "total doc vertexSet entities / containment-participating LOC entities",
            "metadata_locally_justifiable_frac": "fraction of atomic located_in edges a span-local reader could extract (locality + surface cue)",
            "metadata_present_never_annotated_count/metadata_present_held_out_count": "the two present sub-types (see present_stratum_note)",
            "metadata_composed_only_present_count": "present queries that are NEVER an annotated edge (= never_annotated; provably non-circular)",
            "metadata_absent_different_component_count/metadata_absent_same_component_count": "the two absent regimes",
            "metadata_offset_ok_frac": "fraction of entity mentions whose computed char span matches the mention surface",
            "metadata_n_mode_b_conflicts/metadata_n_contradiction_pairs": "annotation-cycle conflicts (|D|>1) / dropped 2-cycles",
            "metadata_relation_set": "json list of the located-in wikidata properties present in the document",
        },
    }

    out = {"metadata": metadata, "datasets": datasets}
    full_path = os.path.join(WORK, "full_data_out.json")
    json.dump(out, open(full_path, "w"), ensure_ascii=False)
    sz = os.path.getsize(full_path) / 1e6
    log.info("wrote %s (%.1f MB), datasets=%s", full_path, sz,
             {d["dataset"]: len(d["examples"]) for d in datasets})

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
    json.dump(truncate(out, 3, True), open(os.path.join(WORK, "preview_data_out.json"), "w"), ensure_ascii=False)
    log.info("wrote mini_data_out.json + preview_data_out.json")
    return sz


if __name__ == "__main__":
    main()
