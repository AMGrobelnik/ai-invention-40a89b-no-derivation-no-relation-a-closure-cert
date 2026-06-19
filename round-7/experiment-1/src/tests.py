#!/usr/bin/env python3
"""$0 unit tests: engine round-trip, grounding, surface<->primitive, canon atomic-PR,
primitive scoring plumbing. No LLM calls."""
from __future__ import annotations

import json
from pathlib import Path

from kinship import Kinship, forward_closure, query_modeA, simple_paths_names
import dataio_redocred as D
import baselines as B
import method as M

DATASET = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/full_data_out.json")


def main():
    full = json.loads(DATASET.read_text())
    kin = Kinship(full["metadata"]["composition_table"])
    fails = []

    # 1) engine: surface round-trip for all 22 canonical surfaces
    for w, (t, g) in kin.surface_reverse.items():
        back = kin.surface(t, g)
        if kin.surface_to_type(w) is None:
            fails.append(f"surface_to_type({w}) is None")
    print(f"[1] surface_reverse has {len(kin.surface_reverse)} entries; all map -> type OK")

    # 2) engine round-trip on real docs (present reproduced, absent -> empty)
    rows = D.load_slice(full, "re-docred")
    recs, ctxs = D.build_records(rows, kin, "re-docred")
    q_ok = q_tot = a_ok = a_tot = 0
    for did, ctx in ctxs.items():
        gg = ctx["gg"]
        edges = D._atomics_to_id_edges(gg)
        Dd, nbrs, nf = forward_closure(kin, edges)
        for q in gg.get("query_edges", []):
            q_tot += 1
            Rset = Dd.get((q["source"], q["target"]), set())
            q_ok += int(len(Rset) == 1 and next(iter(Rset)) == q["primitive"])
        for p in gg.get("absent_relation_pairs", []):
            a_tot += 1
            a_ok += int(len(Dd.get((p["source"], p["target"]), set())) == 0)
    assert q_ok == q_tot, f"present round-trip {q_ok}/{q_tot}"
    assert a_ok == a_tot, f"absent round-trip {a_ok}/{a_tot}"
    print(f"[2] gold-read engine: present {q_ok}/{q_tot} reproduced, absent {a_ok}/{a_tot} empty (re-docred)")

    # 3) grounding: gold surfaces -> ids
    ok = tot = 0
    for did, ctx in ctxs.items():
        for n in ctx["gg"]["nodes"]:
            ok += int(D.ground_name(n["surface"], ctx) == n["entity_id"]); tot += 1
    rate = ok / tot
    assert rate > 0.9, f"grounding recall {rate}"
    print(f"[3] grounding gold surfaces -> ids: {rate:.3f} ({ok}/{tot})")

    # 4) primitivize + primitive scoring: a correct-primitive but wrong-gender read scores CORRECT
    r = next(x for x in recs if not x["is_absent"])
    gp = r["gold_primitive"]; gw = r["gold_surface_word"]
    # craft a raw read = correct primitive, possibly different gendered word
    other_g = "female" if str(gw) != kin.surface(gp, "female") else "male"
    wrong_gender_word = kin.surface(gp, other_g)
    r2 = dict(r)
    r2["gold_surface"] = gp; r2["gold_surface_word"] = gw
    r2["raw"] = {"surface": wrong_gender_word, "conf": 0.9, "named": True}
    r2["_sig"] = {"verbalized": 0.9, "sc_margin": 0.9, "ptrue": 0.9, "negent": 0.9,
                  "sc_majority_surface": wrong_gender_word, "sc10_abstain": False}
    M.build_ct_baselines([r2])
    M.primitivize([r2], kin)
    correct_prim = B.query_correct(r2["raw"]["named"], r2["raw"]["surface"], r2["gold_surface"], False)
    assert correct_prim is True, f"primitive scoring failed: pred_prim={r2['raw']['surface']} gold={gp}"
    print(f"[4] primitive scoring: wrong-gender word '{wrong_gender_word}' scored CORRECT vs primitive '{gp}'")

    # 5) canon atomic PR collapses converses
    e_fwd = [{"a": 1, "b": 2, "type": "inv-child"}]
    e_conv = [{"a": 2, "b": 1, "type": "child"}]
    c1 = M.story_atomic_pr_canon(kin, e_fwd, e_conv)
    assert c1["tp"] == 1 and c1["n_pred"] == 1 and c1["n_gold"] == 1, f"canon converse collapse failed: {c1}"
    print(f"[5] canon atomic-PR collapses converse (inv-child a->b == child b->a): tp={c1['tp']}")

    # 6) PoT path id->name mapping
    rp = next(x for x in recs if not x["is_absent"] and len(x["gold_atomics"]) >= 2)
    paths = simple_paths_names(rp["gold_atomics"], rp["qsrc"], rp["qtgt"], max_paths=3)
    if paths:
        names = D.id_path_to_names(paths[0], rp["_ctx"])
        assert names[0] == rp["qsrc_name"] and names[-1] == rp["qtgt_name"], f"path endpoints {names}"
        print(f"[6] PoT id-path {paths[0]} -> names {names}")
    else:
        print("[6] no gold path for sampled present record (ok)")

    if fails:
        print("FAILS:", fails); raise SystemExit(1)
    print("\nALL UNIT TESTS PASSED")


if __name__ == "__main__":
    main()
