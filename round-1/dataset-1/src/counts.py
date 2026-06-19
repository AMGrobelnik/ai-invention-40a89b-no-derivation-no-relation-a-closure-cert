#!/usr/bin/env python3
"""DESCRIPTIVE structural counts for a gold relation graph.

These are pure graph descriptors only (sizes / label distributions / locality / triangle &
cycle structure). They DO NOT compute the gated experiment statistics (deduction-required
N*, bite-after-widening, singleton-resolution) -- those require composition-table closure
and held-out-edge resolution and are the downstream T0 experiment's job.
"""

from __future__ import annotations

import collections

import networkx as nx


def _is_informative(edge: dict) -> bool:
    """An edge carries a temporal constraint iff its canonical set is not the full
    disjunction. NarrativeTime/MATRES/TBD use the native label 'VAGUE'; TDDMan has none."""
    nr = str(edge.get("native_relation", "")).upper()
    if nr == "VAGUE":
        return False
    cset = edge.get("canonical_relation_set") or []
    # full Allen (13) or full point (3) == no constraint
    if len(cset) >= 13:
        return False
    if edge.get("canonical_algebra") == "point" and len(cset) >= 3:
        return False
    return True


def _structural(nodes_by_id: dict, edges: list[dict], restrict_event_event: bool) -> dict:
    G = nx.Graph()
    type_of = {nid: n["node_type"] for nid, n in nodes_by_id.items()}
    for e in edges:
        if not _is_informative(e):
            continue
        u, v = e["source"], e["target"]
        if restrict_event_event:
            if type_of.get(u) != "event" or type_of.get(v) != "event":
                continue
        if u == v:
            continue
        G.add_edge(u, v)
    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()
    if n_nodes == 0:
        return {"n_informative_edges": 0, "n_nodes_in_graph": 0, "n_triangles": 0,
                "n_query_edges_ge2_intermediates": 0, "cyclomatic_number": 0,
                "n_pairs_path_len_ge3": 0, "max_node_degree": 0}
    tri = sum(nx.triangles(G).values()) // 3
    ge2 = 0
    for u, v in G.edges():
        common = len(set(G[u]) & set(G[v]))
        if common >= 2:
            ge2 += 1
    cyclo = n_edges - n_nodes + nx.number_connected_components(G)
    # pairs reachable only via a path of length >= 3 (genuine multi-hop deduction structure)
    ge3 = 0
    for src, lengths in nx.all_pairs_shortest_path_length(G):
        for dst, d in lengths.items():
            if src < dst and d >= 3:
                ge3 += 1
    degs = [d for _, d in G.degree()]
    return {
        "n_informative_edges": n_edges,
        "n_nodes_in_graph": n_nodes,
        "n_triangles": tri,
        "n_query_edges_ge2_intermediates": ge2,
        "cyclomatic_number": cyclo,
        "n_pairs_path_len_ge3": ge3,
        "max_node_degree": max(degs) if degs else 0,
    }


def descriptive_counts(record: dict) -> dict:
    nodes = record["nodes"]
    edges = record["edges"]
    nodes_by_id = {n["node_id"]: n for n in nodes}

    n_events = sum(1 for n in nodes if n["node_type"] == "event")
    n_timex = sum(1 for n in nodes if n["node_type"] == "timex")
    n_dct = sum(1 for n in nodes if n["node_type"] == "dct")

    native = collections.Counter(str(e.get("native_relation")) for e in edges)
    canon = collections.Counter("|".join(e.get("canonical_relation_set") or []) for e in edges)
    loc = collections.Counter(e.get("locality_class") for e in edges)
    n_ee = sum(1 for e in edges
               if nodes_by_id.get(e["source"], {}).get("node_type") == "event"
               and nodes_by_id.get(e["target"], {}).get("node_type") == "event")
    vw = sum(1 for e in edges if e.get("vague_widened"))

    return {
        "n_documents": 1,
        "n_events": n_events,
        "n_timex": n_timex,
        "n_dct": n_dct,
        "n_nodes": len(nodes),
        "n_edges": len(edges),
        "n_edges_event_event": n_ee,
        "native_relation_dist": dict(native),
        "canonical_relation_set_dist": dict(canon),
        "sentence_distance_dist": {
            "intra": loc.get("intra", 0),
            "adjacent": loc.get("adjacent", 0),
            "long_distance": loc.get("long_distance", 0),
            "undefined": loc.get("undefined", 0),
        },
        "vague_widened_count": vw,
        "structure_event_event_informative": _structural(nodes_by_id, edges, restrict_event_event=True),
        "structure_all_nodes_informative": _structural(nodes_by_id, edges, restrict_event_event=False),
    }


def aggregate_counts(per_doc: list[dict]) -> dict:
    """Sum / merge per-document descriptive counts into a corpus-level summary."""
    agg = {
        "n_documents": len(per_doc),
        "n_events": 0, "n_timex": 0, "n_dct": 0, "n_nodes": 0, "n_edges": 0,
        "n_edges_event_event": 0, "vague_widened_count": 0,
        "native_relation_dist": collections.Counter(),
        "sentence_distance_dist": collections.Counter(),
        "structure_event_event_informative": collections.Counter(),
        "structure_all_nodes_informative": collections.Counter(),
    }
    for d in per_doc:
        for k in ["n_events", "n_timex", "n_dct", "n_nodes", "n_edges",
                  "n_edges_event_event", "vague_widened_count"]:
            agg[k] += d[k]
        agg["native_relation_dist"].update(d["native_relation_dist"])
        agg["sentence_distance_dist"].update(d["sentence_distance_dist"])
        for sk in ["structure_event_event_informative", "structure_all_nodes_informative"]:
            for k, v in d[sk].items():
                agg[sk][k] += v
    for k in ["native_relation_dist", "sentence_distance_dist",
              "structure_event_event_informative", "structure_all_nodes_informative"]:
        agg[k] = dict(agg[k])
    # locality fraction (the headline descriptor: long-distance share)
    sd = agg["sentence_distance_dist"]
    tot = sum(sd.values()) or 1
    agg["long_distance_fraction"] = round(sd.get("long_distance", 0) / tot, 4)
    agg["adjacent_fraction"] = round(sd.get("adjacent", 0) / tot, 4)
    agg["intra_fraction"] = round(sd.get("intra", 0) / tot, 4)
    return agg
