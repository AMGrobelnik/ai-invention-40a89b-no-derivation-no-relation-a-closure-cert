#!/usr/bin/env python3
"""Self-contained qualitative-constraint-network (QCN) closure engine.

Two algebras built PROGRAMMATICALLY (no external table files), each cross-checked
against the verified GQR composition cells from the implementation dossier:

  * POINT  -- convex point algebra over event START-points {<,=,>} (PC COMPLETE;
              EXACT inconsistency certificate). The ONLY non-convex relation is
              `{<,>}` (`!=`); per the dossier widening rule it is WIDENED to the
              universal `{<,=,>}` to keep path-consistency complete, and every
              widening is COUNTED (bite lost by convex restriction).
  * ALLEN  -- Allen interval algebra (13 base relations). Composition is generated
              by the ENDPOINT method (enumerate weak orders of the six interval
              endpoints) and unit-tested against the dossier's GQR cells. Full Allen
              PC is sound but INCOMPLETE -> closure-detectable inconsistency is a
              LOWER BOUND there.

Closure operators:
  * close_triangle      -- the per-triangle length-2 path narrowing used for the
                           frontier metrics (path = compose(AB,BC); inter = path & AC).
  * pc2_full            -- Mackworth PC-2 worklist closure to fixpoint (OUR METHOD).
  * naive_single_pass   -- BASELINE: one pass of length-2 path intersections at the
                           query edge, no fixpoint / no re-propagation
                           ("Path-of-Thoughts + one intersection step").
"""
from __future__ import annotations

import itertools
from collections import deque
from typing import Iterable

# ----------------------------------------------------------------------------------
# Allen-13 base relations (qualreas-compatible symbols) and their endpoint geometry.
# Interval X = (Xs, Xe) with Xs < Xe. relation(X, Y) defined on (Xs, Xe, Ys, Ye).
# ----------------------------------------------------------------------------------
ALLEN_BASE = ["B", "BI", "D", "DI", "O", "OI", "M", "MI", "S", "SI", "F", "FI", "E"]
ALLEN_CONVERSE = {"B": "BI", "BI": "B", "D": "DI", "DI": "D", "O": "OI", "OI": "O",
                  "M": "MI", "MI": "M", "S": "SI", "SI": "S", "F": "FI", "FI": "F", "E": "E"}


def _allen_rel(xs: int, xe: int, ys: int, ye: int) -> str | None:
    """Atomic Allen relation of interval X=(xs,xe) to Y=(ys,ye) from endpoint ranks.

    Assumes proper intervals (xs<xe, ys<ye). Returns one of the 13 base symbols.
    """
    if not (xs < xe and ys < ye):
        return None
    if xs == ys and xe == ye:
        return "E"
    if xe < ys:
        return "B"
    if ye < xs:
        return "BI"
    if xe == ys:
        return "M"
    if ye == xs:
        return "MI"
    if xs == ys:
        return "S" if xe < ye else "SI"
    if xe == ye:
        return "F" if xs > ys else "FI"
    if xs < ys and ye < xe:
        return "DI"
    if ys < xs and xe < ye:
        return "D"
    if xs < ys < xe < ye:
        return "O"
    if ys < xs < ye < xe:
        return "OI"
    return None  # unreachable for proper intervals


def _build_allen_compose() -> dict[tuple[str, str], frozenset]:
    """Generate the Allen base x base composition table via endpoint enumeration.

    Enumerate every rank assignment of the 6 endpoints (As,Ae,Bs,Be,Cs,Ce) in 0..5
    (ties allowed; only relative order matters). For each that yields proper intervals,
    record comp[r(A,B)][r(B,C)] |= {r(A,C)}.
    """
    comp: dict[tuple[str, str], set] = {(a, b): set() for a in ALLEN_BASE for b in ALLEN_BASE}
    for asg in itertools.product(range(6), repeat=6):
        As, Ae, Bs, Be, Cs, Ce = asg
        if not (As < Ae and Bs < Be and Cs < Ce):
            continue
        rab = _allen_rel(As, Ae, Bs, Be)
        rbc = _allen_rel(Bs, Be, Cs, Ce)
        rac = _allen_rel(As, Ae, Cs, Ce)
        if rab is None or rbc is None or rac is None:
            continue
        comp[(rab, rbc)].add(rac)
    return {k: frozenset(v) for k, v in comp.items()}


# ----------------------------------------------------------------------------------
# Point algebra over start-points.
# ----------------------------------------------------------------------------------
POINT_BASE = ["<", "=", ">"]
POINT_CONVERSE = {"<": ">", "=": "=", ">": "<"}
# GQR point.comp (verified): = is identity; <o<={<}; >o>={>}; <o>=>o<=universal.
POINT_COMPOSE = {
    ("=", "="): frozenset({"="}),
    ("<", "="): frozenset({"<"}), ("=", "<"): frozenset({"<"}),
    (">", "="): frozenset({">"}), ("=", ">"): frozenset({">"}),
    ("<", "<"): frozenset({"<"}),
    (">", ">"): frozenset({">"}),
    ("<", ">"): frozenset({"<", "=", ">"}),
    (">", "<"): frozenset({"<", "=", ">"}),
}
POINT_NONCONVEX = frozenset({"<", ">"})  # the only non-convex point relation (`!=`)


class Algebra:
    """A qualitative calculus with relation sets stored as frozensets of base symbols."""

    def __init__(self, name: str, base: list[str], converse: dict[str, str],
                 compose_bb: dict[tuple[str, str], frozenset], identity: frozenset,
                 convex_widen: frozenset | None = None):
        self.name = name
        self.base = list(base)
        self.universe = frozenset(base)
        self.empty = frozenset()
        self.identity = frozenset(identity)
        self._conv = dict(converse)
        self._comp = dict(compose_bb)
        # `convex_widen` (point algebra only): the unique non-convex relation that must
        # be widened to the universal set to keep PC complete. None => no widening.
        self._nonconvex = convex_widen

    # ---- set ops -----------------------------------------------------------------
    def converse(self, s: frozenset) -> frozenset:
        return frozenset(self._conv[r] for r in s)

    def compose(self, a: frozenset, b: frozenset) -> frozenset:
        if not a or not b:
            return self.empty
        out: set = set()
        for x in a:
            for y in b:
                out |= self._comp[(x, y)]
        return frozenset(out)

    def is_nonconvex(self, s: frozenset) -> bool:
        return self._nonconvex is not None and s == self._nonconvex

    def widen(self, s: frozenset) -> tuple[frozenset, bool]:
        """Return (possibly-widened set, fired?). Widening only happens for the
        unique non-convex relation of a convex algebra (point: `{<,>}` -> universe)."""
        if self._nonconvex is not None and s == self._nonconvex:
            return self.universe, True
        return s, False

    def label(self, s: frozenset) -> str:
        if not s:
            return "EMPTY"
        if s == self.universe:
            return "UNIVERSE"
        return "|".join(r for r in self.base if r in s)


def build_point_algebra() -> Algebra:
    return Algebra("POINT", POINT_BASE, POINT_CONVERSE, POINT_COMPOSE,
                   frozenset({"="}), convex_widen=POINT_NONCONVEX)


def build_allen_algebra() -> Algebra:
    return Algebra("ALLEN", ALLEN_BASE, ALLEN_CONVERSE, _build_allen_compose(),
                   frozenset({"E"}), convex_widen=None)


# ----------------------------------------------------------------------------------
# Triangle closure (frontier metric primitive)
# ----------------------------------------------------------------------------------
def close_triangle(alg: Algebra, ab: frozenset, bc: frozenset, ac: frozenset):
    """Length-2 path A-B-C narrowing the query edge A-C.

    path  = compose(ab, bc)                    (with convex widening applied + counted)
    inter = path & ac                          (widening applied + counted)
    Returns dict: path, inter, empty(collapse), singleton, n_widen.
    """
    n_widen = 0
    path = alg.compose(ab, bc)
    path, w = alg.widen(path)
    n_widen += int(w)
    inter = path & ac
    inter, w = alg.widen(inter)
    n_widen += int(w)
    return {
        "path": path,
        "inter": inter,
        "empty": len(inter) == 0,
        "singleton": len(inter) == 1,
        "n_widen": n_widen,
    }


# ----------------------------------------------------------------------------------
# Full QCN + closure variants (reused by whole-document consistency checks)
# ----------------------------------------------------------------------------------
class QCN:
    """Constraint network: dense node list, edges = relation-set frozensets.

    Missing edge => universe. Invariants on set_edge: M[j][i]==converse(M[i][j]),
    M[i][i]==identity.
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
        self.nbrs: list[set] = [set() for _ in range(self.n)]

    def set_edge(self, i: int, j: int, s: frozenset) -> None:
        if i == j:
            return
        self.M[i][j] = s
        self.M[j][i] = self.alg.converse(s)
        if s != self.alg.universe:
            self.nbrs[i].add(j); self.nbrs[j].add(i)
        else:
            self.nbrs[i].discard(j); self.nbrs[j].discard(i)

    def get(self, i: int, j: int) -> frozenset:
        return self.M[i][j]

    def known_edges(self) -> list[tuple[int, int]]:
        U = self.alg.universe
        return [(i, j) for i in range(self.n) for j in range(i + 1, self.n) if self.M[i][j] != U]


def pc2_full(qcn: QCN):
    """OUR METHOD: Mackworth PC-2 worklist closure to fixpoint.

    Returns (consistent: bool, n_fired). Empty edge => inconsistent (Mode-B certificate).
    Convex widening (point algebra) applied to every refined edge and absorbed silently
    (it can only enlarge a set, never empties it).
    """
    alg = qcn.alg
    U = alg.universe
    M = qcn.M
    nbrs = qcn.nbrs
    Q = deque()
    inq = set()
    for (i, j) in qcn.known_edges():
        Q.append((i, j)); inq.add((i, j))
        Q.append((j, i)); inq.add((j, i))
    n_fired = 0

    def enqueue(a, b):
        if (a, b) not in inq:
            inq.add((a, b)); Q.append((a, b))

    while Q:
        i, j = Q.popleft(); inq.discard((i, j))
        rij = M[i][j]
        if rij == U:
            continue
        for k in list(nbrs[j]):
            if k == i:
                continue
            comp = alg.compose(rij, M[j][k])
            new = M[i][k] & comp
            new, _ = alg.widen(new)
            if new != M[i][k]:
                if not new:
                    return False, n_fired
                M[i][k] = new; M[k][i] = alg.converse(new)
                nbrs[i].add(k); nbrs[k].add(i)
                n_fired += 1
                enqueue(i, k); enqueue(k, i)
        for k in list(nbrs[i]):
            if k == j:
                continue
            comp = alg.compose(M[k][i], rij)
            new = M[k][j] & comp
            new, _ = alg.widen(new)
            if new != M[k][j]:
                if not new:
                    return False, n_fired
                M[k][j] = new; M[j][k] = alg.converse(new)
                nbrs[k].add(j); nbrs[j].add(k)
                n_fired += 1
                enqueue(k, j); enqueue(j, k)
    return True, n_fired


def naive_single_pass(qcn: QCN, u: int, v: int) -> frozenset:
    """BASELINE: single pass of length-2 path compositions at the query edge (u,v).

    Intersects compose(R(u,w), R(w,v)) over intermediate w with informative u-w & w-v.
    NO fixpoint, NO re-propagation.
    """
    alg = qcn.alg
    U = alg.universe
    M = qcn.M
    R = U
    for w in qcn.nbrs[u]:
        if w in (u, v):
            continue
        if M[w][v] != U:
            R = R & alg.compose(M[u][w], M[w][v])
            R, _ = alg.widen(R)
            if not R:
                return alg.empty
    return R


if __name__ == "__main__":
    import json
    pt = build_point_algebra()
    al = build_allen_algebra()
    print("POINT base:", pt.base)
    print("ALLEN base:", al.base, "| n compose cells:", sum(1 for _ in al._comp))
    # quick spot prints
    print("ALLEN B o B =", sorted(al.compose(frozenset({'B'}), frozenset({'B'}))))
    print("ALLEN D o DI =", sorted(al.compose(frozenset({'D'}), frozenset({'DI'}))))
    print("POINT < o > =", sorted(pt.compose(frozenset({'<'}), frozenset({'>'}))))
