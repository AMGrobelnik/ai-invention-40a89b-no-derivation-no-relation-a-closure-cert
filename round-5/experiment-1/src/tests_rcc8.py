#!/usr/bin/env python3
"""STAGE-2 BLOCKING closure-correctness tests for the RCC-8 / CDC spatial engine.

If any assertion fails the downstream metrics are invalid -> method.py refuses to spend any
LLM budget. Covers: composition spot cells, orientation (converse), naive==full on length-2,
naive DIVERGES from full on a >=3-edge chain (iteration-isolation invariant), Mode-B
inconsistency collapse, and a multi-path INTERSECTION narrowing (the mechanism)."""
from __future__ import annotations

import sys

import engine
from rcc8_layer import orient_rcc8

FS = frozenset


def _check(name, got, exp, errs):
    if set(got) != set(exp):
        errs.append(f"{name}: got {sorted(got)} expected {sorted(exp)}")


def closure_tests_pass(verbose: bool = True):
    errs = []
    rc = engine.build_rcc8_algebra()
    cd = engine.build_cardinal_algebra()

    # ---- RCC-8 composition spot cells (vs GQR) ----
    _check("RCC8 DC o DC = universe", rc.compose(FS({"DC"}), FS({"DC"})), set(rc.base), errs)
    _check("RCC8 TPP o TPP", rc.compose(FS({"TPP"}), FS({"TPP"})), {"NTPP", "TPP"}, errs)
    _check("RCC8 NTPP o NTPP", rc.compose(FS({"NTPP"}), FS({"NTPP"})), {"NTPP"}, errs)
    _check("RCC8 EC o EC", rc.compose(FS({"EC"}), FS({"EC"})),
           {"DC", "EC", "EQ", "PO", "TPP", "TPPi"}, errs)
    for r in rc.base:  # EQ identity + converse involution
        _check(f"RCC8 EQ o {r}", rc.compose(FS({"EQ"}), FS({r})), {r}, errs)
        _check(f"RCC8 conv-conv {r}", rc.converse(rc.converse(FS({r}))), {r}, errs)
    _check("RCC8 conv(TPP)", rc.converse(FS({"TPP"})), {"TPPi"}, errs)
    _check("RCC8 conv(NTPP)", rc.converse(FS({"NTPP"})), {"NTPPi"}, errs)
    if any(not rc.compose(FS({a}), FS({b})) for a in rc.base for b in rc.base):
        errs.append("RCC8 has an empty composition cell")

    # ---- orientation (non-symmetric): TPP stored (a,b) reads as TPPi for (b,a) ----
    _check("orient_rcc8 converse", orient_rcc8(FS({"TPP"}), ("a", "b"), ("b", "a")), {"TPPi"}, errs)
    _check("orient_rcc8 same-dir", orient_rcc8(FS({"NTPP"}), ("a", "b"), ("a", "b")), {"NTPP"}, errs)

    # ---- naive == full on a length-2 query (A NTPP B, B NTPP C; query A-C) ----
    q = engine.QCN(rc, ["A", "B", "C"])
    q.set_edge(0, 1, FS({"NTPP"})); q.set_edge(1, 2, FS({"NTPP"}))
    naive = engine.naive_single_pass(q, 0, 2)
    ok, _ = engine.pc2_full(q)
    if not (set(naive) == {"NTPP"} and ok and set(q.get(0, 2)) == {"NTPP"}):
        errs.append(f"RCC8 len-2 naive/full: naive={sorted(naive)} full={sorted(q.get(0,2))} ok={ok}")

    # ---- naive DIVERGES from full on a 3-edge chain (A-B-C-D; query A-D) ----
    q2 = engine.QCN(rc, ["A", "B", "C", "D"])
    q2.set_edge(0, 1, FS({"NTPP"})); q2.set_edge(1, 2, FS({"NTPP"})); q2.set_edge(2, 3, FS({"NTPP"}))
    naive2 = engine.naive_single_pass(q2, 0, 3)        # A's only nbr B has M[B][D]=universe -> universe
    ok2, _ = engine.pc2_full(q2)
    full2 = q2.get(0, 3)
    if not (set(naive2) == set(rc.base) and ok2 and set(full2) == {"NTPP"}):
        errs.append(f"RCC8 chain divergence: naive={sorted(naive2)} full={sorted(full2)} ok={ok2}")

    # ---- Mode-B inconsistency collapse (A NTPP B, B NTPP C, A DC C is impossible) ----
    q3 = engine.QCN(rc, ["A", "B", "C"])
    q3.set_edge(0, 1, FS({"NTPP"})); q3.set_edge(1, 2, FS({"NTPP"})); q3.set_edge(0, 2, FS({"DC"}))
    ok3, _ = engine.pc2_full(q3)
    if ok3:
        errs.append("RCC8 failed to detect inconsistency A NTPP B NTPP C but A DC C")

    # ---- multi-path INTERSECTION narrowing (CDC, the mechanism) ----
    # query A-D; path1 via B: A {N,NE} B, B {N} D -> {N,NE}; path2 via C: A {N,NW} C, C {N} D
    # -> {N,NW}; PC intersection at A-D = {N} (singleton). Best single path is non-singleton.
    qc = engine.QCN(cd, ["A", "B", "C", "D"])
    qc.set_edge(0, 1, FS({"N", "NE"})); qc.set_edge(1, 3, FS({"N"}))
    qc.set_edge(0, 2, FS({"N", "NW"})); qc.set_edge(2, 3, FS({"N"}))
    p1 = cd.compose(FS({"N", "NE"}), FS({"N"}))
    p2 = cd.compose(FS({"N", "NW"}), FS({"N"}))
    okc, _ = engine.pc2_full(qc)
    inter = qc.get(0, 3)
    if not (okc and set(p1) == {"N", "NE"} and set(p2) == {"N", "NW"} and set(inter) == {"N"}
            and inter <= p1 and inter <= p2 and len(inter) < min(len(p1), len(p2))):
        errs.append(f"CDC multi-path narrowing: p1={sorted(p1)} p2={sorted(p2)} inter={sorted(inter)} ok={okc}")

    # ---- CDC composition + converse spot cells ----
    _check("CDC N o E", cd.compose(FS({"N"}), FS({"E"})), {"NE"}, errs)
    _check("CDC N o S", cd.compose(FS({"N"}), FS({"S"})), {"N", "EQ", "S"}, errs)
    _check("CDC conv(NE)", cd.converse(FS({"NE"})), {"SW"}, errs)

    res = {"n_errors": len(errs), "errors": errs,
           "rcc8_compose_cells": len(rc.base) ** 2, "cdc_compose_cells": len(cd.base) ** 2}
    if verbose:
        if errs:
            print("CLOSURE TESTS FAILED:")
            for e in errs:
                print("  -", e)
        else:
            print(f"ALL CLOSURE TESTS PASSED (RCC-8 {len(rc.base)}^2={len(rc.base)**2} + "
                  f"CDC {len(cd.base)}^2={len(cd.base)**2} cells cross-checked; "
                  "naive==full@len2, naive!=full@chain, Mode-B collapse, multi-path narrowing).")
    return (len(errs) == 0), res


if __name__ == "__main__":
    ok, _ = closure_tests_pass(verbose=True)
    sys.exit(0 if ok else 1)
