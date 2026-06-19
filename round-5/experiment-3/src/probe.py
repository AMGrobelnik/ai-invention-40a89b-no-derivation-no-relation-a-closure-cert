#!/usr/bin/env python3
"""$0 probe: NarrativeTime/TDDMan doc char-length distribution + per-doc deduction-query
counts when built as a single-doc POINT arm; CLUTRR gold-graph node structure + a dry-run
of the disjoint-entity concatenation builder. No LLM, no mutation."""
from __future__ import annotations

import json
from collections import defaultdict

import data_adapter as DA
from dataio import _atomics_to_edges, load_clutrr, parse_gold_graph, subsample_gen
from kinship import Kinship

CHAR_LO, CHAR_HI, CHAR_TARGET = 2500, 3500, 3000


def probe_temporal():
    print("=" * 78)
    print("TEMPORAL: NarrativeTime / TDDMan document char lengths")
    print("=" * 78)
    by_corpus = defaultdict(list)
    for (corpus, docid, text, G) in DA.load_dataset(DA.DEFAULT_DATASET):
        by_corpus[corpus].append((docid, text, G))
    for corpus in ("narrativetime", "tddman", "matres"):
        rows = by_corpus.get(corpus, [])
        if not rows:
            continue
        lens = sorted((len(t), d) for (d, t, _) in rows)
        chars = [l for l, _ in lens]
        in_band = [(l, d) for (l, d) in lens if CHAR_LO <= l <= CHAR_HI]
        print(f"\n[{corpus}] n_docs={len(rows)} "
              f"min={chars[0]} median={chars[len(chars)//2]} max={chars[-1]}")
        print(f"  docs in [{CHAR_LO},{CHAR_HI}]: {len(in_band)} -> {in_band[:8]}")
        print(f"  5 longest: {lens[-5:]}")
    # build single-doc POINT arms for the 5 NT docs nearest 3000 chars, count deduction queries
    nt = sorted(by_corpus["narrativetime"], key=lambda r: abs(len(r[1]) - CHAR_TARGET))
    sel = [r for r in nt if CHAR_LO <= len(r[1]) <= CHAR_HI][:5]
    if not sel:
        sel = sorted(by_corpus["narrativetime"], key=lambda r: -len(r[1]))[:5]
    print("\n  selected NT docs (POINT single-doc arm) -- deduction-query counts:")
    for (docid, text, G) in sel:
        docs, off = DA.build_corpus("narrativetime", [(docid, text, G)])
        if not docs:
            print(f"    {docid}: char={len(text)} BUILD-EMPTY")
            continue
        arm = DA.build_arm("narrativetime", docs, "POINT", n_target=10**6, v_max=3)
        print(f"    {docid}: char={len(text)} n_read_edges={arm['n_edges']} "
              f"n_queries={arm['n_queries']} (len2={arm['n_len2']} ge3={arm['n_ge3_cyclic']}) "
              f"offset_ok={off:.3f}")


def probe_clutrr():
    print("\n" + "=" * 78)
    print("CLUTRR: gold-graph structure + disjoint-entity concatenation dry-run")
    print("=" * 78)
    gen, disc, comp = load_clutrr(mini=False)
    kin = Kinship(comp)
    test = subsample_gen(gen, fold="test")
    print(f"\n  test-fold stories: {len(test)}")
    ex0 = test[0]
    G0 = parse_gold_graph(ex0)
    print(f"  gold-graph node keys: {list(G0['nodes'][0].keys())}")
    print(f"  sample node: {G0['nodes'][0]}")
    print(f"  metadata_query: {ex0['metadata_query']}")
    print(f"  n atomic_facts: {len(ex0['metadata_atomic_facts'])} sample: {ex0['metadata_atomic_facts'][0]}")
    print(f"  story_char_len(meta)={ex0.get('metadata_story_char_len')} input_len={len(ex0['input'])} hop={ex0['metadata_hop_count']}")
    # dry-run concat: longest-first, pairwise-disjoint surfaces, until ~3000 chars or 6 stories
    chosen = []
    used = set()
    total = 0
    for ex in sorted(test, key=lambda e: -len(e["input"])):
        G = parse_gold_graph(ex)
        names = {n["surface"] for n in G["nodes"]}
        if names & used:
            continue
        chosen.append((ex, G, names))
        used |= names
        total += len(ex["input"])
        if total >= CHAR_TARGET or len(chosen) >= 6:
            break
    print(f"\n  concat dry-run: {len(chosen)} stories, total_chars(approx)={total}")
    join_len = len("\n\n".join(ex["input"] for (ex, _, _) in chosen))
    print(f"  joined doc char length = {join_len}")
    for (ex, G, names) in chosen:
        q = ex["metadata_query"]
        print(f"    {ex['metadata_doc_id']}: chars={len(ex['input'])} hop={ex['metadata_hop_count']} "
              f"n_entities={len(names)} query={q['source_name']}->{q['target_name']}={q['relation']}")
    # absent cross-story pairs available?
    print(f"\n  disc-fold stories: {len(disc)}")


if __name__ == "__main__":
    probe_temporal()
    probe_clutrr()
