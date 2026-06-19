#!/usr/bin/env python3
"""Spatial corpus adapter for the iter-5 RCC-8 / CDC decisive test.

(1) load_spatial(ds): yield (docid, story, G) from the FROZEN spatial corpus
    (gen_art_dataset_1/full_data_out.json; G = {nodes, edges, query_edge}).
(2) SpaRP object-DESCRIPTION recovery (the #1 plan risk): SpaRP corpus nodes carry only
    symbolic ids ('0x0'), so re-load the RAW SpaRP scene's `symbolic_entity_map`
    (id -> natural phrase, e.g. '1x2' -> 'medium yellow apple of box two') from the cached
    HF download and align to corpus docids by the 'SpaRP-PS1_test_{i}' index. A description
    is USABLE only if a content token of it appears in the story (anti-fabrication gate).
(3) build_rcc8_subgraph / build_cardinal_subgraph: per-algebra constraint graphs with the
    world-root '-1' excluded, oriented canonical relation sets, undirected adjacency.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import networkx as nx

import rcc8_layer as RL

SPATIAL = ("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/"
           "iter_4/gen_art/gen_art_dataset_1/full_data_out.json")
RAW_SPARP_PS1 = ("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/"
                 "gen_art/gen_art_dataset_1/temp/datasets/"
                 "full_UKPLab_sparp_SpaRP-PS1 (SpaRTUN)_test.json")
ROOT_ID = "-1"

_STOP = {"of", "the", "a", "an", "in", "on", "to", "and", "box", "number", "this",
         "is", "are", "with", "image"}


# --------------------------------------------------------------------------- #
# corpus loading
# --------------------------------------------------------------------------- #
def load_spatial(ds_name, path=SPATIAL):
    obj = json.loads(Path(path).read_text())
    for ds in obj["datasets"]:
        if ds["dataset"] != ds_name:
            continue
        for ex in ds["examples"]:
            yield ex["metadata_doc_id"], ex.get("input", ""), json.loads(ex["output"])


# --------------------------------------------------------------------------- #
# SpaRP description recovery (id -> natural phrase via raw symbolic_entity_map)
# --------------------------------------------------------------------------- #
_DESC_CACHE = {}


def load_sparp_desc_maps(raw_path=RAW_SPARP_PS1, dataset="SpaRP-PS1", split="test"):
    """Return desc_map[docid][node_id] = natural phrase (from raw symbolic_entity_map)."""
    if raw_path in _DESC_CACHE:
        return _DESC_CACHE[raw_path]
    out = {}
    rows = json.loads(Path(raw_path).read_text())
    for i, r in enumerate(rows):
        docid = f"{dataset}_{split}_{i}"
        sem = r.get("symbolic_entity_map") or {}
        if isinstance(sem, str):
            try:
                sem = json.loads(sem)
            except Exception:
                sem = {}
        out[docid] = {str(k): str(v) for k, v in sem.items()}
    _DESC_CACHE[raw_path] = out
    return out


def _content_tokens(phrase):
    toks = re.findall(r"[a-z]+", str(phrase).lower())
    return [t for t in toks if t not in _STOP and len(t) > 1]


def usable_desc(desc, story):
    """A recovered description is usable iff >=1 content token appears in the story."""
    if not desc:
        return False
    low = story.lower()
    return any(t in low for t in _content_tokens(desc))


# --------------------------------------------------------------------------- #
# per-algebra subgraphs
# --------------------------------------------------------------------------- #
def build_rcc8_subgraph(G):
    """Return (by_pair{(min,max):(canon_set, stored_uv)}, nx.Graph) over pure-rcc8 edges,
    world-root excluded. Edge canonical TPPI/NTPPI canonicalised to engine TPPi/NTPPi."""
    by_pair, g = {}, nx.Graph()
    for e in G["edges"]:
        if e.get("algebra") != "rcc8":
            continue
        s, d = e["src"], e["dst"]
        if s == ROOT_ID or d == ROOT_ID or s == d:
            continue
        cs = RL.canon_rcc8_set(e.get("canonical", []))
        if not cs:
            continue
        key = tuple(sorted((s, d)))
        if key not in by_pair:
            by_pair[key] = (cs, (s, d))
            g.add_edge(s, d)
    return by_pair, g


def build_cardinal_subgraph(G):
    by_pair, g = {}, nx.Graph()
    for e in G["edges"]:
        if e.get("algebra") != "cardinal_direction":
            continue
        s, d = e["src"], e["dst"]
        if s == ROOT_ID or d == ROOT_ID or s == d:
            continue
        cs = RL.canon_cdc_set(e.get("canonical", []))
        if not cs:
            continue
        key = tuple(sorted((s, d)))
        if key not in by_pair:
            by_pair[key] = (cs, (s, d))
            g.add_edge(s, d)
    return by_pair, g


def dgold(alg_converse, by_pair, a, b):
    """Oriented gold rel-set for a->b (converse if stored as b->a)."""
    rec = by_pair.get(tuple(sorted((a, b))))
    if rec is None:
        return None
    cs, (su, sv) = rec
    return cs if (su, sv) == (a, b) else alg_converse(cs)


if __name__ == "__main__":
    dm = load_sparp_desc_maps()
    print(f"recovered desc maps for {len(dm)} SpaRP-PS1 docs")
    # spot-check doc 0
    d0 = dm.get("SpaRP-PS1_test_0", {})
    print("doc0 entity map:", json.dumps(d0, indent=2)[:400])
    n_doc = n_node = n_usable = 0
    for docid, story, G in load_spatial("SpaRP-PS1"):
        n_doc += 1
        if n_doc > 200:
            break
        dmap = dm.get(docid, {})
        for n in G["nodes"]:
            nid = n["node_id"]
            if nid == ROOT_ID:
                continue
            n_node += 1
            if usable_desc(dmap.get(nid, ""), story):
                n_usable += 1
    print(f"over first 200 docs: nodes={n_node} usable_desc={n_usable} "
          f"frac={n_usable / max(n_node,1):.3f}")
