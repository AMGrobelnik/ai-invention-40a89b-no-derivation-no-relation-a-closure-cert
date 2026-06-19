#!/usr/bin/env python3
"""Structural multi-path-redundancy metrics on a reconstructed gold scene-graph.

These are STRUCTURAL annotations of the data (like StepGame's existing k_hop
field) -- NOT experimental results.  No closure, no LLM, no derived P/R.

For a held-out query pair (src,dst) on the undirected projection G of the
STATED relation edges we compute:
  hop_length              : shortest-path length (#edges) between src and dst.
  num_edge_disjoint_paths : max number of edge-disjoint paths (Menger / max-flow).
  cyclomatic_number mu    : E - V + C on the subgraph induced by the union of
                            those edge-disjoint paths (E edges, V nodes,
                            C connected components).
  deduction_required      : the query pair is NOT a directly-stated edge in G.
  genuine_multipath_with_bite : deduction_required AND >=2 edge-disjoint paths
                            each of length >=2.  (When deduction_required is True
                            there is no direct edge, so EVERY path is length>=2;
                            we still check explicitly.)

The IMAGE/WORLD-ROOT container node (SpaRP/SpaRTUN id '-1') is EXCLUDED from the
primary structural graph: "object X is inside the image" is a near-universal
containment relation that composes to the universal relation (no narrowing), so
a path routed through the root carries no deductive bite and would only spuriously
inflate redundancy.  We report both root-excluded (primary) and root-included
(transparency) edge-disjoint-path counts.
"""
from __future__ import annotations

import networkx as nx

ROOT_IDS = {"-1"}  # world/image container node(s) excluded from the primary graph.


def build_undirected(edges, drop_nodes=frozenset()):
    """edges: iterable of (src,dst) stated relation pairs (relation labels are
    collapsed -- one undirected edge per related node pair).  Self-loops and
    edges touching drop_nodes are skipped.  Returns a simple nx.Graph."""
    g = nx.Graph()
    for s, d in edges:
        if s == d or s in drop_nodes or d in drop_nodes:
            continue
        g.add_edge(s, d)
    return g


def _edge_disjoint_paths(g, src, dst):
    if src not in g or dst not in g or src == dst:
        return []
    if not nx.has_path(g, src, dst):
        return []
    try:
        return [list(p) for p in nx.edge_disjoint_paths(g, src, dst)]
    except nx.NetworkXNoPath:
        return []


def _cyclomatic(g, paths):
    """mu = E - V + C on the subgraph induced by the union of `paths`."""
    sub = nx.Graph()
    for p in paths:
        for a, b in zip(p[:-1], p[1:]):
            sub.add_edge(a, b)
    if sub.number_of_nodes() == 0:
        return 0
    E = sub.number_of_edges()
    V = sub.number_of_nodes()
    C = nx.number_connected_components(sub)
    return E - V + C


def scene_graphs(edges):
    """Build the (root-included, root-excluded) graphs ONCE per scene so a scene
    with many enumerated queries does not rebuild them per query."""
    g_full = build_undirected(edges)
    g = build_undirected(edges, drop_nodes=ROOT_IDS)
    return g_full, g


def query_metrics_on(g_full, g, src, dst, stated_pairs):
    """Structural metric bundle for query (src,dst) on prebuilt graphs."""
    directly_stated = frozenset({src, dst}) in stated_pairs
    deduction_required = not directly_stated

    paths = _edge_disjoint_paths(g, src, dst)
    paths_full = _edge_disjoint_paths(g_full, src, dst)
    n_disjoint = len(paths)
    n_disjoint_with_root = len(paths_full)
    n_len_ge2 = sum(1 for p in paths if (len(p) - 1) >= 2)

    if src in g and dst in g and nx.has_path(g, src, dst):
        hop = nx.shortest_path_length(g, src, dst)
    else:
        hop = -1  # query endpoints not connected via non-root stated edges

    mu = _cyclomatic(g, paths)

    # Path-length profile of the edge-disjoint set (networkx returns A maximal
    # edge-disjoint set via max-flow -- shorter augmenting paths first but NOT
    # provably length-minimal, so these lengths are a near-tight upper bound).
    path_lens = sorted(len(p) - 1 for p in paths)
    n_short = sum(1 for ln in path_lens if 2 <= ln <= 4)

    bite = bool(deduction_required and n_disjoint >= 2 and n_len_ge2 >= 2)
    # TIGHT redundancy: >=2 disjoint constraining paths that are BOTH short
    # (len<=4) -> the cross-path intersection is far likelier to actually narrow
    # (long cardinal-composition paths tend to compose toward the universal rel).
    bite_tight = bool(deduction_required and n_short >= 2)

    return {
        "hop_length": int(hop),
        "num_edge_disjoint_paths": int(n_disjoint),
        "num_edge_disjoint_paths_with_root": int(n_disjoint_with_root),
        "num_disjoint_paths_len_ge2": int(n_len_ge2),
        "disjoint_path_lengths": path_lens,
        "second_path_length": int(path_lens[1]) if len(path_lens) >= 2 else -1,
        "cyclomatic_number": int(mu),
        "deduction_required": bool(deduction_required),
        "genuine_multipath_with_bite": bite,
        "genuine_multipath_with_bite_tight": bite_tight,
        "connected": bool(hop >= 1),
        "n_nodes_noroot": int(g.number_of_nodes()),
        "n_edges_noroot": int(g.number_of_edges()),
    }


def query_metrics(edges, src, dst, stated_pairs):
    """Convenience wrapper: build the scene graphs then score one query."""
    g_full, g = scene_graphs(edges)
    return query_metrics_on(g_full, g, src, dst, stated_pairs)
