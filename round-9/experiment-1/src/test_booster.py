#!/usr/bin/env python3
"""GATE-0 booster unit test (no LLM): the deterministic parse + precision guard + cue-support.

Hand-made located-in document with 3 known containment sentences + inventory:
  * the extraction PARSER recovers the 3 canonical edges (recall 1.0 vs the toy gold);
  * the precision guard drops an injected directed 2-cycle (keeps the higher-agreement direction);
  * an ungroundable fabricated name becomes an isolated NAME:: node (never links to gold);
  * cue_supported fires on a sentence with both endpoints + a containment cue and not otherwise.
"""
from __future__ import annotations

import json
import sys

import booster as BO
import dataio_locatedin as D
import readers_locatedin as R
from kinship import Kinship

LOC = "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/full_data_out.json"


def _toy_ctx():
    text = ("Pasay City is located in Metro Manila. Metro Manila is part of the Philippines. "
            "The Philippines contains Palawan.")
    # entity ids 0..3 with mention spans matching the text
    def span(name):
        i = text.find(name)
        return [i, i + len(name)]
    nodes = [{"entity_id": 0, "surface": "Pasay City", "mention_spans": [span("Pasay City")]},
             {"entity_id": 1, "surface": "Metro Manila", "mention_spans": [span("Metro Manila")]},
             {"entity_id": 2, "surface": "Philippines", "mention_spans": [span("Philippines")]},
             {"entity_id": 3, "surface": "Palawan", "mention_spans": [span("Palawan")]}]
    gg = {"doc_id": "TOY", "nodes": nodes, "atomic_edges": [], "query_edges": [], "absent_relation_pairs": []}
    row = {"input": text, "output": json.dumps(gg), "metadata_source": "toy", "metadata_split": "toy"}
    return D.build_doc_context(row), text


def main():
    kin = Kinship(json.loads(open(LOC).read())["metadata"]["composition_table"])
    ctx, text = _toy_ctx()

    # ---- (1) PARSER recovers the 3 directly-stated edges ----
    model_json = json.dumps({"relations": [
        {"a": "Pasay City", "relation": "located in", "b": "Metro Manila"},
        {"a": "Metro Manila", "relation": "part of", "b": "Philippines"},   # synonym -> located in
        {"a": "Philippines", "relation": "contains", "b": "Palawan"},
    ]})
    parsed = R.parse_extraction(model_json, kin)
    assert len(parsed["edges"]) == 3, parsed
    grounded = BO._light_guard(parsed["edges"], ctx, kin, D)
    gold = [{"a": 0, "b": 1, "type": "located_in"}, {"a": 1, "b": 2, "type": "located_in"},
            {"a": 2, "b": 3, "type": "contains"}]
    # canon-recall on the toy gold (converse-invariant)
    def cset(edges):
        return {BO.canon_id(kin, e["a"], e["b"], e["type"]) for e in edges} - {None}
    rec = len(cset(grounded) & cset(gold)) / len(cset(gold))
    print(f"[parser] grounded={len(grounded)} canon-recall_vs_toy_gold={rec:.3f}")
    assert rec == 1.0, (grounded, gold)

    # ---- (2) precision guard drops an injected 2-cycle + keeps higher-agreement direction ----
    # source A: correct edges; source B: correct edges + an injected reverse (2-cycle) on (0,1)
    srcA = {"TOY": parsed["edges"]}
    srcB = {"TOY": parsed["edges"] + [{"a": "Metro Manila", "type": "located_in", "surface": "located in",
                                       "b": "Pasay City"}]}
    g_union, stats = BO._union_guard([srcA, srcB], {"TOY": ctx}, kin, D, R,
                                     min_agreement=2, require_cue=False, doc_ids=["TOY"])
    edges = g_union["TOY"]
    print(f"[guard] kept={len(edges)} stats={stats}")
    # the 2-cycle pair {0,1} must collapse to ONE directed edge (the agreement-2 'located in 0->1')
    pair01 = [e for e in edges if {str(e["a"]), str(e["b"])} == {"0", "1"}]
    assert len(pair01) == 1, pair01
    assert pair01[0]["a"] == 0 and pair01[0]["b"] == 1 and pair01[0]["type"] == "located_in", pair01
    assert stats["n_2cycles_resolved"] >= 1

    # ---- (3) ungroundable fabricated name -> isolated NAME:: node (no gold link) ----
    fab = [{"a": "Atlantis", "relation": "located in", "b": "Metro Manila", "type": "located_in",
            "surface": "located in"}]
    gfab = BO._light_guard(fab, ctx, kin, D)
    assert any(str(e["a"]).startswith("NAME::") for e in gfab), gfab
    print(f"[guard] ungroundable -> {gfab[0]['a']!r} (isolated, never a gold link)")

    # ---- (4) cue support ----
    cues = BO.cue_words_for(R)
    assert BO.cue_supported(text, "Pasay City", "Metro Manila", cues) is True
    assert BO.cue_supported(text, "Palawan", "Pasay City", cues) is False  # not co-mentioned w/ cue
    print(f"[cue] cue-support fires on co-mentioned-with-cue pair, not otherwise ({len(cues)} cues)")

    print("\nGATE-0 BOOSTER PASS")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"GATE-0 BOOSTER FAIL: {e}"); sys.exit(1)
