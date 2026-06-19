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
import json
from collections import deque
from pathlib import Path
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
# RCC-8 region-connection calculus (8 base spatial relations). Built from the
# authoritative dataset table (gen_art_dataset_2/qcn/algebra_tables/RCC8_Algebra.json,
# 436-check verified). The ONLY symbol mismatch is canonicalised: the JSON writes
# TPPI/NTPPI, while the dataset gold relations + this engine use TPPi/NTPPi (lowercase
# 'i'). RCC-8 consistency is NP-hard; path-consistency (PC-2) is SOUND but INCOMPLETE,
# so every closure-derived count (collapse / singleton-resolution / coverage) is a
# SOUND LOWER BOUND. convex_widen=None => NO widening is ever applied.
# ----------------------------------------------------------------------------------
RCC8_BASE = ["DC", "EC", "PO", "EQ", "TPP", "NTPP", "TPPi", "NTPPi"]
RCC8_TABLE_PATH = Path(
    "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/"
    "gen_art/gen_art_dataset_2/qcn/algebra_tables/RCC8_Algebra.json")

# Embedded verbatim transcription of RCC8_Algebra.json (used iff the dataset file is
# missing). Symbols are the JSON's raw TPPI/NTPPI; _rcc8_canon() canonicalises them.
_RCC8_TABLE_LITERAL = {
    "Relations": {
        "DC": {"Converse": "DC"}, "EC": {"Converse": "EC"}, "EQ": {"Converse": "EQ"},
        "NTPP": {"Converse": "NTPPI"}, "NTPPI": {"Converse": "NTPP"}, "PO": {"Converse": "PO"},
        "TPP": {"Converse": "TPPI"}, "TPPI": {"Converse": "TPP"},
    },
    "TransTable": {
        "DC": {"DC": "DC|EC|EQ|NTPP|NTPPI|PO|TPP|TPPI", "EC": "DC|EC|NTPP|PO|TPP", "EQ": "DC",
               "NTPP": "DC|EC|NTPP|PO|TPP", "NTPPI": "DC", "PO": "DC|EC|NTPP|PO|TPP",
               "TPP": "DC|EC|NTPP|PO|TPP", "TPPI": "DC"},
        "EC": {"DC": "DC|EC|NTPPI|PO|TPPI", "EC": "DC|EC|EQ|PO|TPP|TPPI", "EQ": "EC",
               "NTPP": "NTPP|PO|TPP", "NTPPI": "DC", "PO": "DC|EC|NTPP|PO|TPP",
               "TPP": "EC|NTPP|PO|TPP", "TPPI": "DC|EC"},
        "EQ": {"DC": "DC", "EC": "EC", "EQ": "EQ", "NTPP": "NTPP", "NTPPI": "NTPPI", "PO": "PO",
               "TPP": "TPP", "TPPI": "TPPI"},
        "NTPP": {"DC": "DC", "EC": "DC", "EQ": "NTPP", "NTPP": "NTPP",
                 "NTPPI": "DC|EC|EQ|NTPP|NTPPI|PO|TPP|TPPI", "PO": "DC|EC|NTPP|PO|TPP",
                 "TPP": "NTPP", "TPPI": "DC|EC|NTPP|PO|TPP"},
        "NTPPI": {"DC": "DC|EC|NTPPI|PO|TPPI", "EC": "NTPPI|PO|TPPI", "EQ": "NTPPI",
                  "NTPP": "EQ|NTPP|NTPPI|PO|TPP|TPPI", "NTPPI": "NTPPI", "PO": "NTPPI|PO|TPPI",
                  "TPP": "NTPPI|PO|TPPI", "TPPI": "NTPPI"},
        "PO": {"DC": "DC|EC|NTPPI|PO|TPPI", "EC": "DC|EC|NTPPI|PO|TPPI", "EQ": "PO",
               "NTPP": "NTPP|PO|TPP", "NTPPI": "DC|EC|NTPPI|PO|TPPI",
               "PO": "DC|EC|EQ|NTPP|NTPPI|PO|TPP|TPPI", "TPP": "NTPP|PO|TPP",
               "TPPI": "DC|EC|NTPPI|PO|TPPI"},
        "TPP": {"DC": "DC", "EC": "DC|EC", "EQ": "TPP", "NTPP": "NTPP",
                "NTPPI": "DC|EC|NTPPI|PO|TPPI", "PO": "DC|EC|NTPP|PO|TPP", "TPP": "NTPP|TPP",
                "TPPI": "DC|EC|EQ|PO|TPP|TPPI"},
        "TPPI": {"DC": "DC|EC|NTPPI|PO|TPPI", "EC": "EC|NTPPI|PO|TPPI", "EQ": "TPPI",
                 "NTPP": "NTPP|PO|TPP", "NTPPI": "NTPPI", "PO": "NTPPI|PO|TPPI",
                 "TPP": "EQ|PO|TPP|TPPI", "TPPI": "NTPPI|TPPI"},
    },
}


def _rcc8_canon(sym: str) -> str:
    """Canonicalise the JSON's TPPI/NTPPI to the engine/dataset TPPi/NTPPi."""
    return {"TPPI": "TPPi", "NTPPI": "NTPPi"}.get(sym, sym)


def _load_rcc8_table() -> dict:
    if RCC8_TABLE_PATH.exists():
        try:
            return json.loads(RCC8_TABLE_PATH.read_text())
        except Exception:
            pass
    return _RCC8_TABLE_LITERAL


def build_rcc8_algebra() -> Algebra:
    tbl = _load_rcc8_table()
    converse = {_rcc8_canon(r): _rcc8_canon(v["Converse"]) for r, v in tbl["Relations"].items()}
    compose: dict[tuple[str, str], frozenset] = {}
    for r1, row in tbl["TransTable"].items():
        for r2, cell in row.items():
            compose[(_rcc8_canon(r1), _rcc8_canon(r2))] = frozenset(
                _rcc8_canon(s) for s in cell.split("|"))
    return Algebra("RCC8", RCC8_BASE, converse, compose, frozenset({"EQ"}), convex_widen=None)


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
    pt = build_point_algebra()
    al = build_allen_algebra()
    print("POINT base:", pt.base)
    print("ALLEN base:", al.base, "| n compose cells:", sum(1 for _ in al._comp))
    # quick spot prints
    print("ALLEN B o B =", sorted(al.compose(frozenset({'B'}), frozenset({'B'}))))
    print("ALLEN D o DI =", sorted(al.compose(frozenset({'D'}), frozenset({'DI'}))))
    print("POINT < o > =", sorted(pt.compose(frozenset({'<'}), frozenset({'>'}))))

    # ============================================================================
    # RCC-8 LOAD-BEARING PRE-LLM GATE: rebuild the algebra and cross-check EVERY
    # one of the 64 TransTable cells + 8 converses + identity against the
    # authoritative JSON (after TPPI->TPPi / NTPPI->NTPPi canonicalisation).
    # Expect 0 mismatches; any mismatch aborts the whole experiment.
    # ============================================================================
    print("\n=== RCC-8 ENGINE SELF-TEST ===")
    rc = build_rcc8_algebra()
    print("RCC8 base:", rc.base, "| n compose cells:", sum(1 for _ in rc._comp))
    assert set(rc.base) == set(RCC8_BASE) and len(rc.base) == 8, "RCC8 base wrong"
    assert rc.identity == frozenset({"EQ"}), f"RCC8 identity {rc.identity} != {{EQ}}"
    assert rc._nonconvex is None, "RCC8 must NOT widen (PC sound-but-incomplete)"

    tbl = _load_rcc8_table()
    # converses
    conv_mismatch = 0
    for r, v in tbl["Relations"].items():
        cr = _rcc8_canon(r)
        expect = _rcc8_canon(v["Converse"])
        got = next(iter(rc.converse(frozenset({cr}))))
        if got != expect:
            conv_mismatch += 1
            print(f"  CONVERSE MISMATCH {cr}: got {got} expect {expect}")
    # compose cells
    comp_checked = comp_mismatch = 0
    for r1, row in tbl["TransTable"].items():
        for r2, cell in row.items():
            cr1, cr2 = _rcc8_canon(r1), _rcc8_canon(r2)
            expect = frozenset(_rcc8_canon(s) for s in cell.split("|"))
            got = rc.compose(frozenset({cr1}), frozenset({cr2}))
            comp_checked += 1
            if got != expect:
                comp_mismatch += 1
                print(f"  COMPOSE MISMATCH {cr1}o{cr2}: got {sorted(got)} expect {sorted(expect)}")
    print(f"converses checked: 8 mismatches: {conv_mismatch}")
    print(f"compose cells checked: {comp_checked} mismatches: {comp_mismatch}")
    # spot asserts from the dossier
    U8 = frozenset(RCC8_BASE)
    assert rc.compose(frozenset({"DC"}), frozenset({"DC"})) == U8, "DC.DC != universe"
    assert rc.compose(frozenset({"TPP"}), frozenset({"TPP"})) == frozenset({"NTPP", "TPP"}), "TPP.TPP"
    assert rc.compose(frozenset({"NTPP"}), frozenset({"NTPP"})) == frozenset({"NTPP"}), "NTPP.NTPP"
    assert rc.compose(frozenset({"EC"}), frozenset({"EC"})) == frozenset(
        {"DC", "EC", "EQ", "PO", "TPP", "TPPi"}), "EC.EC"
    assert next(iter(rc.converse(frozenset({"TPP"})))) == "TPPi", "converse(TPP)"
    assert next(iter(rc.converse(frozenset({"NTPP"})))) == "NTPPi", "converse(NTPP)"
    # EQ is the identity element of composition
    for r in RCC8_BASE:
        assert rc.compose(frozenset({"EQ"}), frozenset({r})) == frozenset({r}), f"EQ o {r}"
    assert comp_checked == 64 and comp_mismatch == 0 and conv_mismatch == 0, \
        "RCC-8 ENGINE SELF-TEST FAILED"
    print("RCC-8 SELF-TEST PASSED (64 compose cells + 8 converses + identity, 0 mismatches)")
