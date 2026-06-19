#!/usr/bin/env python3
"""Engine unit-test battery. ALL must pass before any T0 scoring (Stage 0 gate).

T-A   : loaded Allen 13x13 table matches published Allen-1983 canonical cells + the
        composition/converse algebra law holds for all 169 cells (structural validation
        of every cell against the relation-algebra axioms).
T-P   : convex linear point compositions and converses.
T-C   : consistency detection -- A<B<C<A is inconsistent.
T-CMP : convex point COMPLETENESS -- PC minimal labels == brute-force enumeration of all
        consistent point scenarios on random small nets (n<=6). Confirms PC is complete
        (computes the minimal network) on the convex point algebra.
T-IT  : iteration isolation -- FULL==NAIVE on a length-2 acyclic query, FULL!=NAIVE on a
        3-hop chain (full resolves a singleton naive leaves loose). Underpins the H3
        iterated-vs-single-pass envelope.
T-NEG : (documented) PC is INCOMPLETE on a point net containing the non-convex relation
        '!=' ({<,>}) -- motivates widening non-convex inputs to universe.
"""
from __future__ import annotations

import itertools
import random
from pathlib import Path

from engine import Algebra, QCN, load_algebra_from_qualreas, pc2_full, naive_single_pass

ALG_DIR = Path(__file__).parent / "algebras"
if not (ALG_DIR / "Linear_Interval_Algebra.json").exists():
    ALG_DIR = Path(__file__).parent / "data" / "qualreas" / "Algebras"

# Canonical Allen compositions (Allen, CACM 1983 / standard interval-algebra references).
# Keys use qualreas relation symbols: B BI D DI E F FI M MI O OI S SI.
ALLEN_CANONICAL = {
    ("B", "B"): {"B"},
    ("B", "M"): {"B"},
    ("M", "M"): {"B"},
    ("B", "D"): {"B", "O", "M", "D", "S"},
    ("B", "DI"): {"B"},
    ("D", "B"): {"B"},
    ("D", "D"): {"D"},
    ("DI", "DI"): {"DI"},
    ("O", "O"): {"B", "M", "O"},
    ("S", "S"): {"S"},
    ("F", "F"): {"F"},
    ("M", "MI"): {"E", "F", "FI"},
    ("MI", "M"): {"E", "S", "SI"},
    ("S", "SI"): {"E", "S", "SI"},
    ("F", "FI"): {"E", "F", "FI"},
    ("B", "BI"): {"B", "BI", "D", "DI", "E", "F", "FI", "M", "MI", "O", "OI", "S", "SI"},
    ("D", "DI"): {"B", "BI", "D", "DI", "E", "F", "FI", "M", "MI", "O", "OI", "S", "SI"},
}


def _set(alg: Algebra, mask: int) -> set[str]:
    return set(alg.rels_of(mask))


def test_allen(alg: Algebra) -> dict:
    res = {"n_relations": alg.n, "n_cells": alg.n * alg.n}
    assert alg.n == 13, f"Allen must have 13 base relations, got {alg.n}"
    # (a) canonical published cells
    mism = []
    for (a, b), expect in ALLEN_CANONICAL.items():
        got = _set(alg, alg.compose(alg.bit[a], alg.bit[b]))
        if got != expect:
            mism.append((a, b, sorted(got), sorted(expect)))
    res["canonical_cells_checked"] = len(ALLEN_CANONICAL)
    res["canonical_mismatches"] = mism
    # (b) converse involution
    inv_ok = all(alg.converse(alg.converse(alg.bit[r])) == alg.bit[r] for r in alg.base_relations)
    res["converse_involution"] = inv_ok
    # (c) composition-converse algebra law: conv(a o b) == conv(b) o conv(a), all 169 cells
    law_fail = 0
    for a in alg.base_relations:
        for b in alg.base_relations:
            lhs = alg.converse(alg.compose(alg.bit[a], alg.bit[b]))
            rhs = alg.compose(alg.converse(alg.bit[b]), alg.converse(alg.bit[a]))
            if lhs != rhs:
                law_fail += 1
    res["composition_converse_law_failures"] = law_fail
    # (d) identity: E o x == x and x o E == x
    id_ok = all(alg.compose(alg.identity, alg.bit[r]) == alg.bit[r]
                and alg.compose(alg.bit[r], alg.identity) == alg.bit[r]
                for r in alg.base_relations)
    res["identity_law"] = id_ok
    res["passed"] = (not mism) and inv_ok and law_fail == 0 and id_ok
    return res


def test_point(alg: Algebra) -> dict:
    b = alg.bit
    checks = {
        "< o < = <": _set(alg, alg.compose(b["<"], b["<"])) == {"<"},
        "< o = = <": _set(alg, alg.compose(b["<"], b["="])) == {"<"},
        "< o > = univ": alg.compose(b["<"], b[">"]) == alg.universe,
        "> o > = >": _set(alg, alg.compose(b[">"], b[">"])) == {">"},
        "= o = = =": _set(alg, alg.compose(b["="], b["="])) == {"="},
        "conv(<) = >": alg.converse(b["<"]) == b[">"],
        "conv(=) = =": alg.converse(b["="]) == b["="],
        "identity": all(alg.compose(alg.identity, b[r]) == b[r] for r in alg.base_relations),
    }
    return {"checks": checks, "passed": all(checks.values())}


def test_consistency(alg_point: Algebra) -> dict:
    """A<B, B<C, C<A must be inconsistent."""
    q = QCN(alg_point, ["A", "B", "C"])
    lt = alg_point.bit["<"]
    q.set_edge(0, 1, lt)  # A<B
    q.set_edge(1, 2, lt)  # B<C
    q.set_edge(2, 0, lt)  # C<A
    _, consistent, _ = pc2_full(q)
    # positive control: a consistent chain stays consistent
    q2 = QCN(alg_point, ["A", "B", "C"])
    q2.set_edge(0, 1, lt); q2.set_edge(1, 2, lt)
    _, cons2, _ = pc2_full(q2)
    return {"cycle_inconsistent": (not consistent), "chain_consistent": cons2,
            "passed": (not consistent) and cons2}


def _brute_force_point_minimal(constraints: dict[tuple[int, int], set[str]], n: int):
    """Ground-truth minimal network for a CONVEX point net by enumerating coord assignments.

    Returns dict[(i,j)] -> set of relations realized across all assignments consistent with
    the constraints, or None for an (i,j) if the net is inconsistent (no assignment).
    """
    def rel(x, y):
        return "<" if x < y else (">" if x > y else "=")
    realized: dict[tuple[int, int], set[str]] = {(i, j): set() for i in range(n) for j in range(n) if i < j}
    any_consistent = False
    for assign in itertools.product(range(n), repeat=n):
        ok = True
        for (i, j), allowed in constraints.items():
            if rel(assign[i], assign[j]) not in allowed:
                ok = False
                break
        if not ok:
            continue
        any_consistent = True
        for i in range(n):
            for j in range(i + 1, n):
                realized[(i, j)].add(rel(assign[i], assign[j]))
    if not any_consistent:
        return None
    return realized


def test_convex_point_completeness(alg_point: Algebra, n_nets: int = 200, seed: int = 13) -> dict:
    """PC minimal labels == brute-force minimal labels on random small CONVEX point nets."""
    rng = random.Random(seed)
    convex_sets = [["<"], ["="], [">"], ["<", "="], ["=", ">"], ["<", "=", ">"]]
    nets_tested = 0
    nets_consistent = 0
    label_mismatches = 0
    consistency_mismatches = 0
    for _ in range(n_nets):
        n = rng.randint(3, 6)
        # build a random partial convex net by assigning each unordered pair a convex constraint
        constraints: dict[tuple[int, int], set[str]] = {}
        q = QCN(alg_point, list(range(n)))
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < 0.55:  # leave some edges as universe
                    rels = rng.choice(convex_sets)
                    constraints[(i, j)] = set(rels)
                    q.set_edge(i, j, alg_point.mask_of(rels))
        bf = _brute_force_point_minimal(constraints, n)
        qc = q.copy()
        _, consistent, _ = pc2_full(qc)
        nets_tested += 1
        if (bf is None) != (not consistent):
            consistency_mismatches += 1
            continue
        if bf is None:
            continue  # both agree inconsistent
        nets_consistent += 1
        for i in range(n):
            for j in range(i + 1, n):
                pc_label = _set(alg_point, qc.get(i, j))
                if pc_label != bf[(i, j)]:
                    label_mismatches += 1
    passed = label_mismatches == 0 and consistency_mismatches == 0
    return {"nets_tested": nets_tested, "nets_consistent": nets_consistent,
            "label_mismatches": label_mismatches, "consistency_mismatches": consistency_mismatches,
            "passed": passed}


def test_iteration_isolation(alg_point: Algebra) -> dict:
    """FULL==NAIVE on a length-2 acyclic query; FULL!=NAIVE on a 3-hop chain."""
    lt = alg_point.bit["<"]
    U = alg_point.universe
    # length-2 acyclic: a<b<c, query (a,c)
    q2 = QCN(alg_point, ["a", "b", "c"])
    q2.set_edge(0, 1, lt); q2.set_edge(1, 2, lt)
    naive2 = naive_single_pass(q2.copy(), 0, 2)
    qf2 = q2.copy(); pc2_full(qf2); full2 = qf2.get(0, 2)
    len2_equal = (naive2 == full2 == lt)
    # 3-hop chain: a<b<c<d, query (a,d) -- no length-2 path a-w-d
    q3 = QCN(alg_point, ["a", "b", "c", "d"])
    q3.set_edge(0, 1, lt); q3.set_edge(1, 2, lt); q3.set_edge(2, 3, lt)
    naive3 = naive_single_pass(q3.copy(), 0, 3)
    qf3 = q3.copy(); pc2_full(qf3); full3 = qf3.get(0, 3)
    hop3_diff = (naive3 == U) and (full3 == lt) and (naive3 != full3)
    return {"len2_naive_eq_full": len2_equal, "hop3_naive_neq_full": hop3_diff,
            "len2_label": alg_point.label(full2), "hop3_full_label": alg_point.label(full3),
            "hop3_naive_label": alg_point.label(naive3),
            "passed": len2_equal and hop3_diff}


def test_pc_incomplete_with_neq(alg_point: Algebra) -> dict:
    """DOCUMENTED: PC is incomplete on a net with the non-convex '!=' relation.

    Classic example: x{<,>}y, y{<,>}z, x{<,>}z is path-consistent but the minimal
    network is tighter than what PC reports (PC leaves all three as {<,>}). We confirm
    PC keeps {<,>} (no tightening) while brute-force shows it stays consistent -- the
    incompleteness shows up on larger '!=' nets; here we just confirm PC does not crash
    and leaves '!=' un-tightened, motivating widening non-convex inputs to universe.
    """
    neq = alg_point.bit["<"] | alg_point.bit[">"]
    q = QCN(alg_point, ["x", "y", "z"])
    q.set_edge(0, 1, neq); q.set_edge(1, 2, neq); q.set_edge(0, 2, neq)
    qc = q.copy()
    _, consistent, _ = pc2_full(qc)
    stays_neq = qc.get(0, 1) == neq and consistent
    return {"pc_keeps_neq_unchanged": stays_neq, "consistent": consistent,
            "note": "PC sound but not guaranteed minimal on non-convex (!=) inputs",
            "passed": True}  # documentation test, always informational


def run_all() -> dict:
    allen = load_algebra_from_qualreas(ALG_DIR / "Linear_Interval_Algebra.json", "ALLEN13")
    point = load_algebra_from_qualreas(ALG_DIR / "Linear_Point_Algebra.json", "POINT")
    rcc8 = load_algebra_from_qualreas(ALG_DIR / "RCC8_Algebra.json", "RCC8")
    out = {
        "allen": test_allen(allen),
        "point": test_point(point),
        "consistency": test_consistency(point),
        "convex_point_completeness": test_convex_point_completeness(point),
        "iteration_isolation": test_iteration_isolation(point),
        "pc_incompleteness_with_neq": test_pc_incomplete_with_neq(point),
        "rcc8_cells": rcc8.n * rcc8.n,
        "rcc8_n_relations": rcc8.n,
    }
    out["all_gating_tests_passed"] = bool(
        out["allen"]["passed"] and out["point"]["passed"] and out["consistency"]["passed"]
        and out["convex_point_completeness"]["passed"] and out["iteration_isolation"]["passed"]
    )
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(run_all(), indent=2, default=list))
