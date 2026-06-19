#!/usr/bin/env python3
"""Dataset adapter: read the FROZEN real-text gold temporal graphs (NarrativeTime,
TDDMan, MATRES) from gen_art_dataset_1/full_data_out.json and (a) build per-document
event graphs with char-offset event marking, (b) sample DEDUCTION-REQUIRED multi-path
query edges, and (c) emit the deduplicated set of constituent edges to read LOCALLY.

This un-conflates the iter-1 TimeBank-Dense STAND-IN: we now operate on the ACTUAL
NarrativeTime gold (dense co-primary host) + TDDMan (non-circular long-distance anchor).

Output arm dicts share the corpora.py shape so the reused metric code runs unchanged:
  arm = {arm, algebra, edge_tasks:{(docid,u,v):task}, triangles:[], queries:[...],
         docs:{...}, provenance}
where each query carries its induced-subgraph closure scaffold (endpoints + vias +
path edges) and each task carries the marked LOCAL span (the load-bearing regime).
"""
from __future__ import annotations

import json
import random
import re
from collections import defaultdict
from pathlib import Path

# native corpus relation -> shared coarse vocabulary (corpora.py vocab).
# OVERLAP / VAGUE are NOT representable in the coarse vocab -> excluded from scoring
# (mapped to VAGUE so gold_atom() returns None and the edge is dropped from recall).
NATIVE_TO_COARSE = {
    "BEFORE": "before", "AFTER": "after", "INCLUDES": "includes",
    "IS_INCLUDED": "is_included", "SIMULTANEOUS": "simultaneous", "IDENTITY": "simultaneous",
    "OVERLAP": "VAGUE", "VAGUE": "VAGUE",
    # TDDMan lowercase natives:
    "before": "before", "after": "after", "includes": "includes",
    "is_included": "is_included", "simultaneous": "simultaneous",
    # MATRES:
    "EQUAL": "simultaneous",
}

DEFAULT_DATASET = ("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/"
                   "iter_1/gen_art/gen_art_dataset_1/full_data_out.json")

CORPUS_ALGEBRA = {"narrativetime": "ALLEN", "tddman": "ALLEN", "matres": "POINT"}


# --------------------------------------------------------------------------- #
# local-span extraction (load-bearing: the reader sees ONLY the event sentences)
# --------------------------------------------------------------------------- #
def local_span(marked_text: str) -> str:
    """Sentence(s) containing [[E1]] and/or [[E2]] from a marked document."""
    sents = re.split(r"(?<=[.!?])\s+", marked_text)
    keep = [s for s in sents if "[[E1]]" in s or "[[E2]]" in s]
    if not keep:
        return marked_text[:400]
    return " ".join(keep)


def mark_local(text: str, span1: tuple, span2: tuple) -> str:
    """Insert [[E1]]..[[/E1]] / [[E2]]..[[/E2]] by char offset, then keep only the
    local sentence(s). Falls back to ordered surface search if offsets misalign."""
    (s1, e1, w1), (s2, e2, w2) = span1, span2
    # verify offsets; fall back to ordered surface search if they do not line up
    if not (0 <= s1 < e1 <= len(text) and text[s1:e1] == w1):
        idx = text.find(w1)
        if idx < 0:
            return ""
        s1, e1 = idx, idx + len(w1)
    if not (0 <= s2 < e2 <= len(text) and text[s2:e2] == w2):
        idx = text.find(w2, e1)
        if idx < 0:
            idx = text.find(w2)
        if idx < 0:
            return ""
        s2, e2 = idx, idx + len(w2)
    spans = sorted([(s1, e1, "E1"), (s2, e2, "E2")], reverse=True)
    out = text
    for s, e, tag in spans:
        out = out[:s] + f"[[{tag}]]" + out[s:e] + f"[[/{tag}]]" + out[e:]
    return local_span(out)


# --------------------------------------------------------------------------- #
# dataset loading
# --------------------------------------------------------------------------- #
def load_dataset(path: str = DEFAULT_DATASET):
    """Yield (corpus, docid, text, gold_graph_dict) per example."""
    obj = json.loads(Path(path).read_text())
    for ds in obj["datasets"]:
        for ex in ds["examples"]:
            corpus = ex["metadata_corpus"]
            docid = ex["metadata_doc_id"]
            text = ex["input"]
            G = json.loads(ex["output"])
            yield corpus, docid, text, G


def build_corpus(corpus, rows, max_docs=None, seed=20260617):
    """rows = list of (docid, text, G). Returns docs dict:
       docs[docid] = {text, node:{nid:(cs,ce,surface)}, edges:[edge dicts], offset_ok_frac}.
    Each edge dict: u,v (event node_ids), gold(coarse), native, sentdiff,
    deduction_required, locally_justifiable, vague_widened."""
    rng = random.Random(seed)
    docs = {}
    n_offset_ok = n_offset_tot = 0
    for (docid, text, G) in rows:
        nodes = {n["node_id"]: n for n in G["nodes"] if n["node_type"] == "event"}
        node = {}
        for nid, n in nodes.items():
            cs, ce = n.get("char_start"), n.get("char_end")
            surf = n.get("surface", "")
            node[nid] = (cs, ce, surf)
            if cs is not None and ce is not None:
                n_offset_tot += 1
                if 0 <= cs < ce <= len(text) and text[cs:ce] == surf:
                    n_offset_ok += 1
        edges = []
        for e in G["edges"]:
            u, v = e["source"], e["target"]
            if u not in nodes or v not in nodes or u == v:
                continue
            native = e.get("native_relation", "VAGUE")
            coarse = NATIVE_TO_COARSE.get(native, "VAGUE")
            edges.append({
                "u": u, "v": v, "gold": coarse, "native": native,
                "sentdiff": e.get("sentence_distance"),
                "deduction_required": bool(e.get("structural_deduction_required_proxy")),
                "locally_justifiable": bool(e.get("locally_justifiable_proxy")),
                "vague_widened": bool(e.get("vague_widened", False)),
                "canonical_relation_set": e.get("canonical_relation_set"),
                "startpoint_relation_set": e.get("startpoint_relation_set"),
            })
        if len(edges) < 1 or not node:
            continue
        docs[docid] = {"text": text, "node": node, "edges": edges}
    if max_docs is not None and len(docs) > max_docs:
        keep = sorted(docs.keys())
        rng.shuffle(keep)
        docs = {k: docs[k] for k in keep[:max_docs]}
    off_frac = (n_offset_ok / n_offset_tot) if n_offset_tot else 1.0
    return docs, off_frac


# --------------------------------------------------------------------------- #
# deduction-required multi-path query sampling
# --------------------------------------------------------------------------- #
def _scorable(coarse):
    return coarse != "VAGUE"


def sample_queries(corpus, docs, algebra, n_target, v_max=3, seed=20260617,
                   max_per_doc=None):
    """Sample deduction-required query edges with >=1 length-2 gold path.

    Returns (queries, edge_tasks). Each query:
      {corpus, algebra, docid, qx, qy, gold, sentdiff, deduction_required,
       vias:[...], induced_nodes:[...], path_edges:[(a,b)...], stratum, cyclomatic}
    edge_tasks[(docid,u,v)] = task dict with marked LOCAL span (deduped, read ONCE).
    """
    rng = random.Random(seed + 7)
    queries = []
    edge_tasks = {}

    def directed_gold(d_edges_by_pair, a, b):
        """Return (gold_coarse, stored_uv) for the undirected pair {a,b}."""
        key = tuple(sorted((a, b)))
        e = d_edges_by_pair.get(key)
        if e is None:
            return None, None
        return e["gold"], (e["u"], e["v"])

    doc_order = sorted(docs.keys())
    rng.shuffle(doc_order)
    # round-robin pools of admissible queries per doc
    doc_pools = {}
    for docid in doc_order:
        d = docs[docid]
        by_pair = {}
        adj = defaultdict(set)
        for ed in d["edges"]:
            key = tuple(sorted((ed["u"], ed["v"])))
            if key in by_pair:
                continue
            by_pair[key] = ed
            adj[ed["u"]].add(ed["v"]); adj[ed["v"]].add(ed["u"])
        pool = []
        for ed in d["edges"]:
            if not ed["deduction_required"]:
                continue
            if not _scorable(ed["gold"]):
                continue
            qx, qy = ed["u"], ed["v"]
            common = sorted((adj[qx] & adj[qy]) - {qx, qy})
            if not common:
                continue  # no length-2 gold path -> not multi-path deduction-recoverable
            rng.shuffle(common)
            vias = common[:v_max]
            induced = [qx, qy] + vias
            # induced-subgraph edges (except the query edge) = constituent path edges
            path_edges = []
            for ii in range(len(induced)):
                for jj in range(ii + 1, len(induced)):
                    a, b = induced[ii], induced[jj]
                    if {a, b} == {qx, qy}:
                        continue
                    key = tuple(sorted((a, b)))
                    if key in by_pair:
                        path_edges.append((a, b))
            # iteration stratum: >=3-edge/cyclic local path beyond direct triangles
            # ge3 if any via-via gold edge exists (closure must iterate through it)
            has_via_via = any(tuple(sorted((vias[a], vias[b]))) in by_pair
                              for a in range(len(vias)) for b in range(a + 1, len(vias)))
            stratum = "ge3_cyclic" if has_via_via else "len2"
            cyclomatic = len(path_edges) + 1 - len(induced) + 1  # |E|-|V|+1 incl. query
            pool.append({
                "corpus": corpus, "algebra": algebra, "docid": docid,
                "qx": qx, "qy": qy, "gold": ed["gold"], "sentdiff": ed["sentdiff"],
                "deduction_required": True, "vias": vias, "induced_nodes": induced,
                "path_edges": path_edges, "stratum": stratum,
                "cyclomatic": int(cyclomatic), "by_pair_keys": list(by_pair.keys()),
            })
        rng.shuffle(pool)
        if max_per_doc:
            pool = pool[:max_per_doc]
        doc_pools[docid] = pool

    # round-robin draw to spread coverage across documents
    idx = {docid: 0 for docid in doc_order}
    while len(queries) < n_target:
        progressed = False
        for docid in doc_order:
            if len(queries) >= n_target:
                break
            pool = doc_pools[docid]
            if idx[docid] < len(pool):
                queries.append(pool[idx[docid]])
                idx[docid] += 1
                progressed = True
        if not progressed:
            break

    # materialize the deduplicated edge-read set (path edges + query edges)
    for q in queries:
        d = docs[q["docid"]]
        by_pair = {tuple(sorted((e["u"], e["v"]))): e for e in d["edges"]}
        to_read = list(q["path_edges"]) + [(q["qx"], q["qy"])]
        for (a, b) in to_read:
            key = (q["docid"],) + tuple(sorted((a, b)))
            if key in edge_tasks:
                continue
            ed = by_pair.get(tuple(sorted((a, b))))
            if ed is None:
                continue
            cs_u = d["node"].get(ed["u"]); cs_v = d["node"].get(ed["v"])
            if cs_u is None or cs_v is None:
                continue
            marked = mark_local(d["text"], cs_u, cs_v)
            has_span = ("[[E1]]" in marked and "[[E2]]" in marked)
            edge_tasks[key] = {
                "arm": corpus, "algebra": algebra, "docid": q["docid"],
                "u": ed["u"], "v": ed["v"], "gold": ed["gold"], "native": ed["native"],
                "sentdiff": ed["sentdiff"],
                "deduction_required": bool(ed["deduction_required"]),
                "locally_justifiable": bool(ed["locally_justifiable"]),
                "marked_text": marked, "has_local_span": bool(has_span),
            }
    return queries, edge_tasks


def build_arm(corpus, docs, algebra, n_target, v_max=3, seed=20260617, max_per_doc=None):
    queries, edge_tasks = sample_queries(corpus, docs, algebra, n_target, v_max,
                                         seed, max_per_doc)
    n_ge3 = sum(1 for q in queries if q["stratum"] == "ge3_cyclic")
    return {
        "arm": corpus, "algebra": algebra, "docs": docs, "queries": queries,
        "edge_tasks": edge_tasks, "triangles": [],
        "n_docs": len(docs), "n_edges": len(edge_tasks), "n_queries": len(queries),
        "n_ge3_cyclic": n_ge3, "n_len2": len(queries) - n_ge3,
        "provenance": f"{corpus} (frozen gold graphs, gen_art_dataset_1; "
                      f"event-event, deduction-required multi-path queries, LOCAL reads)",
    }


if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DATASET
    by_corpus = defaultdict(list)
    for (corpus, docid, text, G) in load_dataset(path):
        by_corpus[corpus].append((docid, text, G))
    for corpus in ("narrativetime", "tddman", "matres"):
        rows = by_corpus.get(corpus, [])
        docs, off = build_corpus(corpus, rows)
        arm = build_arm(corpus, docs, CORPUS_ALGEBRA[corpus], n_target=200, v_max=3)
        print(f"{corpus:14s} docs={arm['n_docs']:3d} read_edges={arm['n_edges']:4d} "
              f"queries={arm['n_queries']:4d} (len2={arm['n_len2']} ge3={arm['n_ge3_cyclic']}) "
              f"offset_ok={off:.3f}")
        if arm["queries"]:
            q = arm["queries"][0]
            k = (q["docid"],) + tuple(sorted((q["qx"], q["qy"])))
            t = arm["edge_tasks"].get(k)
            print(f"   sample q gold={q['gold']} sd={q['sentdiff']} vias={len(q['vias'])} "
                  f"path_edges={len(q['path_edges'])} stratum={q['stratum']}")
            if t:
                print(f"   query LOCAL span: {t['marked_text'][:200]!r}")
