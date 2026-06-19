"""Independent verification of the algebra tables and gold readers.

Run:  .venv/bin/python tests/test_qcn.py
All checks must pass (exit 0) before the full dataset is generated.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from qcn.algebras import load_algebras, is_convex_point_label, convex_supersets_of
from qcn.realize import point_rel, allen_rel, rcc8_rel, planted_pair, relation

PASS, FAIL = 0, 0


def check(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {msg}")


ALG = load_algebras()


def test_load():
    print("[1] algebra load + structural sanity")
    check(set(ALG) == {"point", "allen", "rcc8"}, "3 algebras")
    check(len(ALG["point"].base) == 3, "point base size")
    check(len(ALG["allen"].base) == 13, "allen base size")
    check(len(ALG["rcc8"].base) == 8, "rcc8 base size")
    for a in ALG.values():
        check(len(a.comp) == len(a.base) ** 2, f"{a.name} comp square")
        # converse involution
        for r in a.base:
            check(a.conv(a.conv(r)) == r, f"{a.name} converse involution {r}")


def test_identity_and_involution():
    print("[2] relation-algebra axioms (identity, converse-distributes)")
    for a in ALG.values():
        idr = a.identity
        for r in a.base:
            check(a.compose(idr, r) == frozenset({r}), f"{a.name} id;r {r}")
            check(a.compose(r, idr) == frozenset({r}), f"{a.name} r;id {r}")
        # converse distributes over composition: conv(r1;r2) == conv(r2);conv(r1)
        for r1, r2 in product(a.base, a.base):
            lhs = a.converse_set(a.compose(r1, r2))
            rhs = a.compose_sets(frozenset({a.conv(r2)}), frozenset({a.conv(r1)}))
            check(lhs == rhs, f"{a.name} converse-distributes {r1};{r2}")


def test_point_composition():
    print("[3] POINT composition vs. direct sign reasoning (exhaustive recover)")
    rec = defaultdict(set)
    R = 4
    for x, y, z in product(range(R + 1), repeat=3):
        rec[(point_rel(x, y), point_rel(y, z))].add(point_rel(x, z))
    a = ALG["point"]
    for (r1, r2), s in rec.items():
        check(frozenset(s) == a.compose(r1, r2),
              f"point comp({r1},{r2}) recovered={sorted(s)} table={sorted(a.compose(r1,r2))}")
    # every table entry must be recovered (completeness)
    check(len(rec) == 9, "point all 9 comp entries recovered")
    # converse law on reader
    for x, y in product(range(R + 1), repeat=2):
        check(point_rel(y, x) == a.conv(point_rel(x, y)), "point reader converse")


def test_allen_composition():
    print("[4] ALLEN composition vs. exhaustive endpoint-CSP enumeration")
    R = 12
    ivs = [(s, e) for s in range(R) for e in range(s + 1, R + 1)]
    rec = defaultdict(set)
    # precompute pairwise relations
    rels = {}
    for A in ivs:
        for B in ivs:
            rels[(A, B)] = allen_rel(A, B)
    for A in ivs:
        for B in ivs:
            r1 = rels[(A, B)]
            for C in ivs:
                rec[(r1, rels[(B, C)])].add(rels[(A, C)])
    a = ALG["allen"]
    mismatches = 0
    for (r1, r2) in product(a.base, a.base):
        if frozenset(rec[(r1, r2)]) != a.compose(r1, r2):
            mismatches += 1
            print(f"    allen comp({r1},{r2}) recovered={sorted(rec[(r1,r2)])} "
                  f"table={sorted(a.compose(r1,r2))}")
    check(mismatches == 0, f"allen composition fully matches table ({mismatches} mismatch)")
    # reader converse law
    for A in ivs[:40]:
        for B in ivs[:40]:
            check(allen_rel(B, A) == a.conv(allen_rel(A, B)), "allen reader converse")
            break


def test_rcc8_soundness():
    print("[5] RCC-8 reader: soundness vs. 2D table + converse (collinear discs)")
    a = ALG["rcc8"]
    discs = [(cx, 0, r) for cx in range(7) for r in range(1, 5)]
    seen = set()
    unsound = 0
    for A in discs:
        for B in discs:
            r1 = rcc8_rel(A, B)
            seen.add(r1)
            # converse law
            if rcc8_rel(B, A) != a.conv(r1):
                unsound += 1
            for C in discs:
                r2 = rcc8_rel(B, C)
                r3 = rcc8_rel(A, C)
                if r3 not in a.compose(r1, r2):
                    unsound += 1
    check(unsound == 0, f"rcc8 reader sound vs table + converse ({unsound} violations)")
    check(seen == set(a.base), f"rcc8 all 8 relations realized by collinear discs: {sorted(seen)}")


def test_planted():
    print("[6] planted relation fragments realize their intended relation")
    for alg in ("point", "allen", "rcc8"):
        for r in ALG[alg].base:
            oi, oj = planted_pair(alg, r)
            got = relation(alg, oi, oj)
            check(got == r, f"{alg} planted {r} -> got {got}")


def test_convex_guard():
    print("[7] convex point-label guard")
    check(not is_convex_point_label({"<", ">"}), "'!=' is non-convex")
    check(is_convex_point_label({"<", "="}), "'<=' is convex")
    for gold in ("<", "=", ">"):
        for sup in convex_supersets_of(gold):
            check(gold in sup and is_convex_point_label(sup), f"convex superset of {gold}")


def test_path_gate():
    print("[8] path-composition gate self-check on a tiny realized chain")
    a = ALG["allen"]
    # A=(0,1) b B=(2,3) b C=(4,5) -> A b C ; composed b;b must contain b
    chain = [allen_rel((0, 1), (2, 3)), allen_rel((2, 3), (4, 5))]
    composed = a.compose_path(chain)
    check(allen_rel((0, 1), (4, 5)) in composed, "allen b;b contains gold(A,C)")


if __name__ == "__main__":
    for t in (test_load, test_identity_and_involution, test_point_composition,
              test_allen_composition, test_rcc8_soundness, test_planted,
              test_convex_guard, test_path_gate):
        t()
    print(f"\nPASS={PASS}  FAIL={FAIL}")
    sys.exit(1 if FAIL else 0)
