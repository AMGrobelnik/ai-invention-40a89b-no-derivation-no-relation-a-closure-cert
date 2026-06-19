#!/usr/bin/env python3
"""Reusable QCN (Qualitative Constraint Network) path-consistency engine.

Implements:
  * Algebra        -- one per qualitative calculus (Allen-13, convex Linear Point, RCC-8),
                      loaded from the AUTHORITATIVE qualreas Algebras/*.json composition/converse
                      tables (github.com/alreich/qualreas). Relation sets are encoded as integer
                      bitmasks for speed (compose = OR over base*base table lookups).
  * QCN            -- a constraint network (n x n matrix of relation-set bitmasks).
  * pc2_full       -- Mackworth PC-2 worklist closure to FIXPOINT (OUR METHOD: iterated
                      path-consistency). Returns the closed network + a consistency flag +
                      a fired-composition log.
  * naive_single_pass -- BASELINE: a single pass of length-2 path intersections at the query
                      node only, NO fixpoint, NO propagation ("Path-of-Thoughts + one
                      intersection step").
  * closure_off    -- LOWER BASELINE: table held fixed but closure not run (returns universe).

This module is checkpointed for reuse by later tiers; it has no LLM / corpus dependencies.
"""
from __future__ import annotations

import json
from collections import deque
from pathlib import Path
from typing import Iterable

# --------------------------------------------------------------------------------------
# Algebra
# --------------------------------------------------------------------------------------


class Algebra:
    """A qualitative calculus with bitmask-encoded relation sets.

    base_relations[k] occupies bit (1 << k). A relation SET is the OR of its members' bits.
    universe = all bits set ("no information"). identity = the reflexive/equality relation set.
    """

    def __init__(self, name: str, base_relations: list[str],
                 converse: dict[str, str], compose_tbl: dict[tuple[str, str], frozenset],
                 identity: frozenset):
        self.name = name
        self.base_relations = list(base_relations)
        self.n = len(self.base_relations)
        self.bit = {r: (1 << k) for k, r in enumerate(self.base_relations)}
        self.rel_of_bitpos = {k: r for k, r in enumerate(self.base_relations)}
        self.universe = (1 << self.n) - 1
        self.empty = 0
        self.identity = self.mask_of(identity)
        # converse as a base->bit map for fast set converse
        self._converse_base_bit = {self.bit[r]: self.bit[converse[r]] for r in self.base_relations}
        self.converse_base = dict(converse)
        # base x base composition, as bitmasks indexed by bit position
        self._compose_bb = [[0] * self.n for _ in range(self.n)]
        for (a, b), res in compose_tbl.items():
            self._compose_bb[self.base_relations.index(a)][self.base_relations.index(b)] = self.mask_of(res)
        # caches
        self._compose_cache: dict[tuple[int, int], int] = {}
        self._converse_cache: dict[int, int] = {}

    # ---- set helpers -------------------------------------------------------------
    def mask_of(self, rels: Iterable[str]) -> int:
        m = 0
        for r in rels:
            m |= self.bit[r]
        return m

    def rels_of(self, mask: int) -> list[str]:
        return [self.base_relations[k] for k in range(self.n) if mask & (1 << k)]

    def label(self, mask: int) -> str:
        """Canonical sorted string label, e.g. '<' or 'B|M|O' or 'universe'."""
        if mask == self.universe:
            return "universe"
        if mask == 0:
            return "EMPTY"
        return "|".join(self.rels_of(mask))

    def is_singleton(self, mask: int) -> bool:
        return mask != 0 and (mask & (mask - 1)) == 0

    # ---- algebra operations ------------------------------------------------------
    def converse(self, mask: int) -> int:
        c = self._converse_cache.get(mask)
        if c is not None:
            return c
        out = 0
        m = mask
        while m:
            low = m & (-m)
            out |= self._converse_base_bit[low]
            m ^= low
        self._converse_cache[mask] = out
        return out

    def compose(self, a: int, b: int) -> int:
        """Composition of two relation sets (over-approximation in incomplete algebras)."""
        if a == 0 or b == 0:
            return 0
        if a == self.universe or b == self.universe:
            return self.universe
        key = (a, b)
        c = self._compose_cache.get(key)
        if c is not None:
            return c
        out = 0
        cbb = self._compose_bb
        ma = a
        while ma:
            lowa = ma & (-ma)
            ia = lowa.bit_length() - 1
            row = cbb[ia]
            mb = b
            while mb:
                lowb = mb & (-mb)
                ib = lowb.bit_length() - 1
                out |= row[ib]
                mb ^= lowb
                if out == self.universe:
                    break
            ma ^= lowa
            if out == self.universe:
                break
        self._compose_cache[key] = out
        return out


def _parse_qualreas_relset(s: str) -> frozenset:
    return frozenset(part for part in s.split("|") if part)


def load_algebra_from_qualreas(json_path: str | Path, name: str | None = None) -> Algebra:
    """Parse a qualreas Algebras/*.json file into an Algebra (authoritative tables)."""
    data = json.loads(Path(json_path).read_text())
    rels = data["Relations"]
    base_relations = list(rels.keys())
    converse = {r: rels[r]["Converse"] for r in base_relations}
    identity = frozenset(r for r in base_relations if rels[r].get("Reflexive", False))
    tt = data["TransTable"]
    compose_tbl: dict[tuple[str, str], frozenset] = {}
    for a in base_relations:
        for b in base_relations:
            compose_tbl[(a, b)] = _parse_qualreas_relset(tt[a][b])
    return Algebra(name or data.get("Name", "algebra"), base_relations, converse, compose_tbl, identity)


# --------------------------------------------------------------------------------------
# QCN
# --------------------------------------------------------------------------------------


class QCN:
    """Qualitative constraint network over a fixed node list, edges as relation-set bitmasks.

    Stored as a dense n x n list-of-lists of integer masks. Missing edge => universe.
    Invariants maintained on set_edge: M[j][i] == converse(M[i][j]); M[i][i] == identity.
    """

    def __init__(self, alg: Algebra, nodes: list):
        self.alg = alg
        self.nodes = list(nodes)
        self.n = len(self.nodes)
        self.index = {nd: i for i, nd in enumerate(self.nodes)}
        U = alg.universe
        self.M = [[U] * self.n for _ in range(self.n)]
        for i in range(self.n):
            self.M[i][i] = alg.identity
        # neighbours = nodes with a non-universe (informative) edge
        self.nbrs: list[set] = [set() for _ in range(self.n)]

    def set_edge(self, i: int, j: int, mask: int) -> None:
        if i == j:
            return
        self.M[i][j] = mask
        self.M[j][i] = self.alg.converse(mask)
        if mask != self.alg.universe:
            self.nbrs[i].add(j)
            self.nbrs[j].add(i)
        else:
            self.nbrs[i].discard(j)
            self.nbrs[j].discard(i)

    def get(self, i: int, j: int) -> int:
        return self.M[i][j]

    def copy(self) -> "QCN":
        q = QCN.__new__(QCN)
        q.alg = self.alg
        q.nodes = self.nodes
        q.n = self.n
        q.index = self.index
        q.M = [row[:] for row in self.M]
        q.nbrs = [set(s) for s in self.nbrs]
        return q

    def known_edges(self) -> list[tuple[int, int]]:
        U = self.alg.universe
        out = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.M[i][j] != U:
                    out.append((i, j))
        return out


# --------------------------------------------------------------------------------------
# Closure variants
# --------------------------------------------------------------------------------------


def pc2_full(qcn: QCN, record_fired: bool = False):
    """OUR METHOD: Mackworth PC-2 worklist closure to fixpoint.

    Returns (qcn, consistent: bool, fired_log). On detecting an empty edge the network is
    inconsistent (MODE-B certificate); we stop and report consistent=False.
    Exploits sparsity: only triangles with two informative sides can tighten an edge.
    """
    alg = qcn.alg
    U = alg.universe
    M = qcn.M
    nbrs = qcn.nbrs
    compose = alg.compose
    converse = alg.converse

    Q = deque()
    inq = set()
    for (i, j) in qcn.known_edges():
        Q.append((i, j)); inq.add((i, j))
        Q.append((j, i)); inq.add((j, i))
    fired = [] if record_fired else None

    def enqueue(a, b):
        if (a, b) not in inq:
            inq.add((a, b)); Q.append((a, b))

    while Q:
        i, j = Q.popleft(); inq.discard((i, j))
        rij = M[i][j]
        if rij == U:
            continue
        # path i -> j -> k  tightens (i,k)
        for k in list(nbrs[j]):
            if k == i:
                continue
            comp = compose(rij, M[j][k])
            old = M[i][k]
            new = old & comp
            if new != old:
                if new == 0:
                    return qcn, False, fired
                M[i][k] = new
                M[k][i] = converse(new)
                nbrs[i].add(k); nbrs[k].add(i)
                if fired is not None:
                    fired.append((qcn.nodes[i], qcn.nodes[k], qcn.nodes[j]))
                enqueue(i, k); enqueue(k, i)
        # path k -> i -> j  tightens (k,j)
        for k in list(nbrs[i]):
            if k == j:
                continue
            comp = compose(M[k][i], rij)
            old = M[k][j]
            new = old & comp
            if new != old:
                if new == 0:
                    return qcn, False, fired
                M[k][j] = new
                M[j][k] = converse(new)
                nbrs[k].add(j); nbrs[j].add(k)
                if fired is not None:
                    fired.append((qcn.nodes[k], qcn.nodes[j], qcn.nodes[i]))
                enqueue(k, j); enqueue(j, k)
    return qcn, True, fired


def naive_single_pass(qcn: QCN, u: int, v: int) -> int:
    """BASELINE: single pass of length-2 path compositions arriving at the query edge (u,v).

    Intersects, over every distinct intermediate w with gold edges u-w and w-v, the
    composition compose(R(u,w), R(w,v)). NO fixpoint, NO propagation to other edges,
    NO converse seeding beyond the gold edges already present in `qcn`.
    """
    alg = qcn.alg
    U = alg.universe
    M = qcn.M
    compose = alg.compose
    R = U
    for w in qcn.nbrs[u]:
        if w == v or w == u:
            continue
        if M[w][v] != U:                      # gold length-2 path u - w - v
            R &= compose(M[u][w], M[w][v])
            if R == 0:
                return 0
    return R


def closure_off(qcn: QCN, u: int, v: int) -> int:
    """LOWER BASELINE: table held fixed but closure NOT run -> no information."""
    return qcn.alg.universe
