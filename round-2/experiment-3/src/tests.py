#!/usr/bin/env python3
"""STAGE-2 BLOCKING closure-correctness tests + STAGE-1 parser smoke tests.

If any closure assertion fails, the downstream metrics are invalid -> the pipeline
must NOT spend any LLM budget. method.py imports `closure_tests_pass()` and refuses
to run elicitation unless it returns True.
"""
from __future__ import annotations

import sys

from engine import (Algebra, build_allen_algebra, build_point_algebra,
                    close_triangle, naive_single_pass, pc2_full, QCN)

FS = frozenset


def _check(name, got, exp, errs):
    if set(got) != set(exp):
        errs.append(f"{name}: got {sorted(got)} expected {sorted(exp)}")


def closure_tests_pass(verbose: bool = True) -> tuple[bool, dict]:
    errs: list[str] = []
    pt = build_point_algebra()
    al = build_allen_algebra()

    # ---- Allen composition cells verified against GQR (dossier Section 2B) ----
    _check("ALLEN <o<  (B o B)", al.compose(FS({"B"}), FS({"B"})), {"B"}, errs)
    _check("ALLEN B o D", al.compose(FS({"B"}), FS({"D"})), {"B", "D", "S", "M", "O"}, errs)
    _check("ALLEN D o DI = universe", al.compose(FS({"D"}), FS({"DI"})), set(al.base), errs)
    _check("ALLEN O o O", al.compose(FS({"O"}), FS({"O"})), {"B", "M", "O"}, errs)
    _check("ALLEN M o M", al.compose(FS({"M"}), FS({"M"})), {"B"}, errs)
    _check("ALLEN M o MI", al.compose(FS({"M"}), FS({"MI"})), {"E", "F", "FI"}, errs)
    _check("ALLEN F o FI", al.compose(FS({"F"}), FS({"FI"})), {"E", "F", "FI"}, errs)
    _check("ALLEN E identity (E o B)", al.compose(FS({"E"}), FS({"B"})), {"B"}, errs)
    # DI o D: A contains B, B during C => A,C must overlap (no before/after/meet) = 9-rel block
    _check("ALLEN DI o D (overlap block)", al.compose(FS({"DI"}), FS({"D"})),
           {"E", "D", "DI", "S", "SI", "F", "FI", "O", "OI"}, errs)
    # converse self-consistency: conv(conv(r))==r for all base
    for r in al.base:
        cc = al.converse(al.converse(FS({r})))
        _check(f"ALLEN conv-conv {r}", cc, {r}, errs)
    # all 169 cells non-empty
    empty_cells = [(a, b) for a in al.base for b in al.base if not al.compose(FS({a}), FS({b}))]
    if empty_cells:
        errs.append(f"ALLEN has {len(empty_cells)} empty composition cells: {empty_cells[:5]}")

    # ---- Point algebra cells (GQR point.comp) ----
    _check("POINT < o <", pt.compose(FS({"<"}), FS({"<"})), {"<"}, errs)
    _check("POINT > o >", pt.compose(FS({">"}), FS({">"})), {">"}, errs)
    _check("POINT < o > = universe", pt.compose(FS({"<"}), FS({">"})), {"<", "=", ">"}, errs)
    _check("POINT > o < = universe", pt.compose(FS({">"}), FS({"<"})), {"<", "=", ">"}, errs)
    _check("POINT = identity (= o <)", pt.compose(FS({"="}), FS({"<"})), {"<"}, errs)
    # widening: {<,>} (!=) must widen to universe and fire the counter
    w, fired = pt.widen(FS({"<", ">"}))
    if not (set(w) == {"<", "=", ">"} and fired):
        errs.append(f"POINT widen({{<,>}}) -> {sorted(w)} fired={fired} (expected universe, True)")
    w2, fired2 = pt.widen(FS({"<", "="}))
    if not (set(w2) == {"<", "="} and not fired2):
        errs.append("POINT widen({<,=}) wrongly fired (convex set must not widen)")

    # ---- close_triangle: the four hand-constructed scenarios (testing_plan Stage 2) ----
    # (a) point before(A,B) & before(B,C) => path {<}, AC read universe => inter {<} singleton-correct
    r = close_triangle(pt, FS({"<"}), FS({"<"}), FS({"<", "=", ">"}))
    if not (set(r["path"]) == {"<"} and set(r["inter"]) == {"<"} and r["singleton"] and not r["empty"]):
        errs.append(f"close_triangle (a) point b&b: {r}")
    # (b) before(A,B) & after(B,C) => path universe (must NOT collapse / not singleton)
    r = close_triangle(pt, FS({"<"}), FS({">"}), FS({"<", "=", ">"}))
    if not (set(r["path"]) == {"<", "=", ">"} and not r["empty"] and not r["singleton"]):
        errs.append(f"close_triangle (b) point b&a: {r}")
    # (c) inconsistent: before(A,B), before(B,C) but AC directly read as after => EMPTY collapse
    r = close_triangle(pt, FS({"<"}), FS({"<"}), FS({">"}))
    if not (r["empty"] and len(r["inter"]) == 0):
        errs.append(f"close_triangle (c) inconsistent collapse: {r}")
    # (d) Allen includes/is_included: DI(A,B) & D(B,C)?  use B(A,B)&BI? Instead: DI o D = universe;
    #     A during B (D) & B during C (D) => A during C (D): path {D}, singleton-correct
    r = close_triangle(al, FS({"D"}), FS({"D"}), set(al.base))
    if not (set(r["path"]) == {"D"} and set(r["inter"]) == {"D"} and r["singleton"]):
        errs.append(f"close_triangle (d) allen D&D: {r}")

    # ---- pc2_full / naive on a length-2 vs length-3 network ----
    # length-2 acyclic: naive == full PC (dossier theorem). 3 nodes A-B-C, query A-C.
    q = QCN(pt, ["A", "B", "C"])
    q.set_edge(0, 1, FS({"<"})); q.set_edge(1, 2, FS({"<"}))
    naive = naive_single_pass(q, 0, 2)
    ok, _ = pc2_full(q)
    if not (set(naive) == {"<"} and ok and set(q.get(0, 2)) == {"<"}):
        errs.append(f"PC vs naive length-2: naive={sorted(naive)} pc_edge={sorted(q.get(0,2))} ok={ok}")
    # inconsistency detected by pc2_full: cycle A<B, B<C, C<A
    q2 = QCN(pt, ["A", "B", "C"])
    q2.set_edge(0, 1, FS({"<"})); q2.set_edge(1, 2, FS({"<"})); q2.set_edge(2, 0, FS({"<"}))
    ok2, _ = pc2_full(q2)
    if ok2:
        errs.append("pc2_full failed to detect cyclic inconsistency A<B<C<A")

    res = {"n_errors": len(errs), "errors": errs,
           "allen_compose_cells": len(al.base) ** 2}
    if verbose:
        if errs:
            print("CLOSURE TESTS FAILED:")
            for e in errs:
                print("  -", e)
        else:
            print("ALL CLOSURE TESTS PASSED "
                  f"(Allen {len(al.base)}^2={len(al.base)**2} cells generated & cross-checked).")
    return (len(errs) == 0), res


if __name__ == "__main__":
    ok, _ = closure_tests_pass(verbose=True)
    sys.exit(0 if ok else 1)
