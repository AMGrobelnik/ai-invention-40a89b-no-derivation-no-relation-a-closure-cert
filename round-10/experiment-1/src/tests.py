#!/usr/bin/env python3
"""GATE-0 (no LLM): engine-wiring check that mirrors the corpus verify.py.

Asserts the degenerate located_in/contains table is loaded correctly, records carry
query_subtype / absent_regime, and -- the KEY check -- the gold-read certificate:
  * DEDUCES located_in for every held_out present query AFTER the direct-edge ablation
    (via the alternative >=2-hop path);
  * returns EMPTY (no_path) in BOTH directions for every sibling AND different_component
    absent pair.
If this fails the wiring is wrong: STOP and fix before spending any budget.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import dataio_locatedin as D
from kinship import Kinship, query_modeA

DATASET = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/full_data_out.json")


def main(limit_docs: int = 400):
    full = json.loads(DATASET.read_text())
    kin = Kinship(full["metadata"]["composition_table"])
    assert kin.base == ["located_in", "contains"], kin.base
    assert kin.compose_types("located_in", "located_in") == "located_in"
    assert kin.compose_types("contains", "contains") == "contains"
    assert kin.compose_types("located_in", "contains") is None
    assert kin.compose_types("contains", "located_in") is None
    assert kin.conv_type("located_in") == "contains"
    assert kin.conv_type("contains") == "located_in"
    assert kin.surface("located_in", "male") == "located in"
    assert kin.surface_to_type("located in") == ("located_in", "male")
    print("[OK] degenerate located_in/contains table wired correctly")

    rows = D.load_slice(full, "re-docred")[:limit_docs]
    records, contexts = D.build_records(rows, kin, "re-docred")
    present = [r for r in records if not r["is_absent"]]
    held = [r for r in present if r["query_subtype"] == "held_out"]
    neva = [r for r in present if r["query_subtype"] == "never_annotated"]
    sib = [r for r in records if r.get("absent_regime") == "same_component_sibling"]
    diff = [r for r in records if r.get("absent_regime") == "different_component"]
    print(f"[counts] docs={len(rows)} present={len(present)} held_out={len(held)} "
          f"never_annotated={len(neva)} sibling={len(sib)} diffcomp={len(diff)}")
    assert held, "no held_out present queries found"
    assert sib, "no sibling absent pairs found"

    # ---- KEY ENGINE CHECK: held_out deduces located_in after ablation ----
    bad_held = 0
    for r in held:
        a = query_modeA(kin, r["gold_atomics"], r["qsrc"], r["qtgt"])
        # gold_atomics already has the direct (qsrc,qtgt) edge dropped
        if not (a["singleton"] and a["answer_type"] == "located_in"):
            bad_held += 1
            if bad_held <= 3:
                print(f"  [held_out FAIL] {r['doc_id']} {r['qsrc']}->{r['qtgt']} -> {a}")
    held_cov = 1.0 - bad_held / len(held)
    print(f"[gold-read] held_out present coverage (deduced located_in) = {held_cov:.4f} "
          f"({len(held)-bad_held}/{len(held)})")

    # ---- never_annotated also deduces ----
    bad_neva = 0
    for r in neva:
        a = query_modeA(kin, r["gold_atomics"], r["qsrc"], r["qtgt"])
        if not (a["singleton"] and a["answer_type"] == "located_in"):
            bad_neva += 1
    neva_cov = (1.0 - bad_neva / len(neva)) if neva else float("nan")
    print(f"[gold-read] never_annotated present coverage = {neva_cov} ({len(neva)-bad_neva}/{len(neva)})")

    # ---- absent pairs: EMPTY in BOTH directions ----
    def abstains_both(r):
        a1 = query_modeA(kin, r["gold_atomics"], r["qsrc"], r["qtgt"])
        a2 = query_modeA(kin, r["gold_atomics"], r["qtgt"], r["qsrc"])
        return a1["no_path"] and a2["no_path"]

    bad_sib = sum(0 if abstains_both(r) else 1 for r in sib)
    bad_diff = sum(0 if abstains_both(r) else 1 for r in diff)
    sib_abst = 1.0 - bad_sib / len(sib)
    diff_abst = (1.0 - bad_diff / len(diff)) if diff else float("nan")
    print(f"[gold-read] sibling absent abstention (EMPTY both dir) = {sib_abst:.4f} ({len(sib)-bad_sib}/{len(sib)})")
    print(f"[gold-read] diffcomp absent abstention = {diff_abst} ({len(diff)-bad_diff}/{len(diff)})")

    ok = (held_cov >= 0.999 and sib_abst >= 0.999 and bad_diff == 0
          and (not neva or neva_cov >= 0.999))
    print(f"\nGATE-0 {'PASS' if ok else 'FAIL'} "
          f"(expect held_out=1.0 / sibling=1.0 / diffcomp=1.0 gold-read ceiling)")
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
