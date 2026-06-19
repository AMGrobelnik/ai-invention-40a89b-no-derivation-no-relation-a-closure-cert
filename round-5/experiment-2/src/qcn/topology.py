"""Constraint-graph topology generators (the controlled design).

Every generator returns ``(G, s, t)`` where ``G`` is an undirected ``networkx``
graph on integer nodes ``0..V-1`` that EXCLUDES the held-out query edge ``(s, t)``
(the query relation starts universal and is obtainable only by composing >=1
multi-edge path).  The geometric embedding + gold relations are added later by
``method.py``; topology here is purely structural.

Cyclomatic number used downstream:  mu = E - V + C  (C = #connected components).

FAMILY 1  theta        : P internally vertex-disjoint s->t paths of length L
                         => redundancy=P, hop=L, V=P*(L-1)+2, derived mu=P-1.
FAMILY 2  cyclo_aug    : theta base + chords between intermediates of DIFFERENT
                         paths (each chord on a connected graph raises mu by 1 and
                         generally creates new s->t paths -- the cross-links that let
                         ITERATED propagation tighten the query beyond one pass).
FAMILY 3  random_andl  : Renz & Nebel A(n,d,l) random network, avg degree d; query =
                         a non-adjacent connected pair (deduction-required).
"""
from __future__ import annotations

from typing import List, Tuple

import networkx as nx
import numpy as np


def theta(rng: np.random.RandomState, P: int, L: int) -> Tuple[nx.Graph, int, int]:
    """P internally vertex-disjoint s->t paths, each with L edges (L-1 intermediates)."""
    assert L >= 2, "theta needs L>=2 so s,t share no direct edge"
    G = nx.Graph()
    s, t = 0, 1
    G.add_nodes_from([s, t])
    nxt = 2
    for _ in range(P):
        prev = s
        for j in range(L - 1):
            node = nxt
            nxt += 1
            G.add_node(node)
            G.add_edge(prev, node)
            prev = node
        G.add_edge(prev, t)
    return G, s, t


def cyclo_aug(rng: np.random.RandomState, P: int, L: int, n_chords: int
              ) -> Tuple[nx.Graph, int, int]:
    """theta(P,L) base + `n_chords` chords between intermediates of different paths."""
    G, s, t = theta(rng, P, L)
    # group intermediates by path
    paths_mids: List[List[int]] = []
    node = 2
    for _ in range(P):
        paths_mids.append(list(range(node, node + (L - 1))))
        node += (L - 1)
    # candidate chords: intermediate pairs on DIFFERENT paths, not already edges,
    # never touching s or t (so we don't shortcut the query).
    cands = []
    for pi in range(P):
        for pj in range(pi + 1, P):
            for u in paths_mids[pi]:
                for v in paths_mids[pj]:
                    if not G.has_edge(u, v):
                        cands.append((u, v))
    rng.shuffle(cands)
    for (u, v) in cands[:n_chords]:
        G.add_edge(u, v)
    return G, s, t


def single_path(rng: np.random.RandomState, L: int) -> Tuple[nx.Graph, int, int]:
    """A single s->t chain of length L (redundancy 1, mu 0). Used for the mu=0 cell."""
    return theta(rng, 1, L)


def add_distractors(G: nx.Graph, s: int, t: int, rng: np.random.RandomState, k: int
                    ) -> nx.Graph:
    """Attach k distractor nodes as a random tree bridged to a non-terminal core node.

    Adds nodes/edges (inflating node count) WITHOUT creating any new s->t path:
    distractors form a tree, bridged to the core by a single edge at an intermediate
    node (never s or t), so no alternative s->t route is introduced.
    """
    if k <= 0:
        return G
    core_internal = [n for n in G.nodes if n not in (s, t)]
    anchor = int(rng.choice(core_internal)) if core_internal else s
    start = max(G.nodes) + 1
    new_nodes = list(range(start, start + k))
    G.add_node(new_nodes[0])
    G.add_edge(anchor, new_nodes[0])  # single bridge (tree edge, no new s-t path)
    for i in range(1, k):
        parent = int(rng.choice(new_nodes[:i]))
        G.add_node(new_nodes[i])
        G.add_edge(parent, new_nodes[i])
    return G


def random_andl(rng: np.random.RandomState, n: int, d: int, max_tries: int = 200
                ) -> Tuple[nx.Graph, int, int]:
    """Renz & Nebel A(n,d): G(n, p=d/(n-1)); query = far-apart non-adjacent pair.

    Returns the largest connected component (relabeled 0..m-1) with a designated
    non-adjacent query pair (s,t) at graph distance >=2 (deduction-required).

    Edge probability is capped strictly below 1 ((n-2)/(n-1)) so the graph is never
    complete -- a deduction-required (non-adjacent) query pair always exists.  When the
    requested average degree d >= n-1 this caps realized density below target; the
    realized average degree is recorded per row (num_edges/num_nodes).
    """
    p = min(d / (n - 1), (n - 2) / (n - 1))
    for _ in range(max_tries):
        seed = int(rng.randint(0, 2 ** 31 - 1))
        G0 = nx.gnp_random_graph(n, p, seed=seed)
        if G0.number_of_edges() == 0:
            continue
        comp = max(nx.connected_components(G0), key=len)
        if len(comp) < 4:
            continue
        H = nx.convert_node_labels_to_integers(G0.subgraph(comp).copy())
        # all non-adjacent pairs reachable at distance >=2
        nonadj = [(u, v) for u in H.nodes for v in H.nodes
                  if u < v and not H.has_edge(u, v)]
        if not nonadj:
            continue
        # choose the pair with the largest shortest-path distance (deeper deduction)
        best = None
        best_d = -1
        # sample up to 60 candidate pairs for speed on dense graphs
        idx = rng.permutation(len(nonadj))[:60]
        for i in idx:
            u, v = nonadj[i]
            try:
                dd = nx.shortest_path_length(H, u, v)
            except nx.NetworkXNoPath:
                continue
            if dd > best_d:
                best_d, best = dd, (u, v)
        if best is None:
            continue
        s, t = best
        # relabel so s=0, t=1 for consistency with theta (optional but tidy)
        return H, int(s), int(t)
    raise RuntimeError(f"random_andl: no valid network for n={n} d={d}")
