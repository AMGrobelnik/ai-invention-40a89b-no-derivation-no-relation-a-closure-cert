#!/usr/bin/env python3
"""STAGE 0 -- wiring & engine sanity (ZERO LLM spend).

Validates that the closure pipeline is wired correctly BEFORE any paid run:
  (a) GOLD atomic reads of a network, fed into the QCN + pc2_full, recover the gold query
      singleton (closure recovers gold from sound singletons);
  (b) on a length-2 (single-intermediate) query, naive single-pass == full PC (the predicted
      TIE -- no upstream edges to re-tighten);
  (c) on a >=3-hop / cyclomatic query, full PC narrows where naive abstains (iteration bite);
  (d) point convex widening fires and is counted for {<,>};
  (e) native-vocab parsing + entity-normalization round-trips.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import dataio
from dataio import load_networks_from_file, parse_native, normalize_sentence
from engine import build_point_algebra, naive_single_pass, pc2_full
import method as M

DS = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/"
          "gen_art/gen_art_dataset_2")


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    return bool(cond)


def test_gold_recovers_query(algebra):
    """(a) gold atomic reads -> pc2_full -> gold query singleton (or sound superset)."""
    nets = load_networks_from_file(DS / "mini_data_out.json", algebra)
    ok_all = True
    for n in nets:
        gdir = M.gold_read_dir(n)
        a = M.mode_a(n, gdir)
        # closure over GOLD singletons must be CONSISTENT and contain the gold query
        contains = n["query"]["gold"] in (a["query_set"] or [])
        ok_all = ok_all and a["consistent"] and contains
    return check(f"[{algebra}] gold reads -> closure contains gold query (n={len(nets)})", ok_all)


def test_length2_tie():
    """(b) length-2 multi-path: naive == full PC (point)."""
    pt = build_point_algebra()
    # s=0, t=1, intermediates 2 and 3; two length-2 paths 0-2-1 and 0-3-1
    from engine import QCN
    q = QCN(pt, [0, 1, 2, 3])
    q.set_edge(0, 2, frozenset({"<"}))
    q.set_edge(2, 1, frozenset({">"}))   # 0<2, 2>1 -> 0 ? 1 underdetermined via this path
    q.set_edge(0, 3, frozenset({"<"}))
    q.set_edge(3, 1, frozenset({"<"}))   # 0<3<1 -> 0<1
    naive = naive_single_pass(q, 0, 1)
    from engine import QCN as Q2
    q2 = Q2(pt, [0, 1, 2, 3])
    q2.set_edge(0, 2, frozenset({"<"})); q2.set_edge(2, 1, frozenset({">"}))
    q2.set_edge(0, 3, frozenset({"<"})); q2.set_edge(3, 1, frozenset({"<"}))
    pc2_full(q2)
    full = q2.get(0, 1)
    return check("length-2 multi-path: naive == full", naive == full,
                 f"naive={sorted(naive)} full={sorted(full)}")


def test_length3_iteration():
    """(c) a chain where full PC narrows strictly more than naive single-pass."""
    pt = build_point_algebra()
    from engine import QCN
    # chain 0<2<3<1 (3 hops). naive at (0,1) sees only length-2 paths via direct neighbors of 0
    # and 1; the full chain requires propagation. Build: 0<2, 2<3, 3<1, plus a slack edge.
    q = QCN(pt, [0, 1, 2, 3])
    q.set_edge(0, 2, frozenset({"<"}))
    q.set_edge(2, 3, frozenset({"<"}))
    q.set_edge(3, 1, frozenset({"<"}))
    naive = naive_single_pass(q, 0, 1)        # no length-2 path 0-w-1 with both known -> universe
    q2 = QCN(pt, [0, 1, 2, 3])
    q2.set_edge(0, 2, frozenset({"<"})); q2.set_edge(2, 3, frozenset({"<"}))
    q2.set_edge(3, 1, frozenset({"<"}))
    pc2_full(q2)
    full = q2.get(0, 1)
    narrows = len(full) < len(naive) and full == frozenset({"<"})
    return check("3-hop chain: full narrows where naive abstains", narrows,
                 f"naive={sorted(naive)} full={sorted(full)}")


def test_point_widening():
    """(d) point {<,>} widens to universe and is counted."""
    pt = build_point_algebra()
    w, fired = pt.widen(frozenset({"<", ">"}))
    return check("point {<,>} widening fires -> universe", fired and w == pt.universe,
                 f"-> {sorted(w)}")


def test_normalization_and_parse():
    """(e) entity-normalization dedups + native parse maps symbols/words."""
    s = "The price adjustment and the design review ended together, but the price adjustment began earlier."
    norm = normalize_sentence(s, "the price adjustment", "the design review")
    dedup_ok = "the price adjustment" not in norm.lower() and "E1" in norm and "E2" in norm
    p1, u1, f1 = parse_native('{"relations":["<"],"underdetermined":false}', "point")
    p2, u2, f2 = parse_native('{"relations":["before","after"]}', "point")
    p3, u3, f3 = parse_native('{"relations":["b","mi"]}', "allen")
    parse_ok = (p1 == frozenset({"<"}) and not f1 and
                p2 == frozenset({"<", ">"}) and
                p3 == frozenset({"B", "MI"}))
    return (check("entity-normalization -> E1/E2", dedup_ok, norm) and
            check("native parse maps symbols+words", parse_ok,
                  f"{sorted(p1)} {sorted(p2)} {sorted(p3)}"))


def test_edge_sentence_mapping():
    """Every gold edge maps to a unique local sentence in the mini networks."""
    ok_all = True
    detail = []
    for algebra in ("point", "allen"):
        nets = load_networks_from_file(DS / "mini_data_out.json", algebra)
        for n in nets:
            ok = len(n["edge_sentences"]) == len(n["gold_edges"])
            ok_all = ok_all and ok
        detail.append(f"{algebra}:{len(nets)} nets")
    return check("edge->sentence mapping complete", ok_all, " ".join(detail))


def main():
    print("STAGE 0 closure + wiring tests (no LLM spend):")
    results = [
        test_gold_recovers_query("point"),
        test_gold_recovers_query("allen"),
        test_length2_tie(),
        test_length3_iteration(),
        test_point_widening(),
        test_normalization_and_parse(),
        test_edge_sentence_mapping(),
    ]
    allok = all(results)
    print(f"\nSTAGE 0: {'ALL PASS' if allok else 'FAILURES PRESENT'} "
          f"({sum(results)}/{len(results)})")
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
