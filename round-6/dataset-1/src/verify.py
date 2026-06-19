#!/usr/bin/env python3
"""Final QA: (1) every row parses & carries the four strata; (2) DROP-IN engine round-trip
-- rebuild closure input from atomic_edges via the documented engine_edge_mapping, run the
kinship.py forward least-fixpoint closure, and confirm it reproduces every emitted PRESENT
query gold and that every ABSENT pair has an empty derivation; (3) cue-present pass rate."""
import json, os, sys
from kinship import Kinship, forward_closure, query_modeA

WORK = os.path.dirname(os.path.abspath(__file__))
full = json.load(open(os.path.join(WORK, "full_data_out.json")))
CT = full["metadata"]["composition_table"]
KIN = Kinship(CT)

REQ = ["nodes", "atomic_edges", "query_edges", "absent_relation_pairs", "absent_pairs_source"]
n_rows = 0; n_q = 0; q_ok = 0; n_abs = 0; abs_ok = 0
cue_checked = 0; cue_ok = 0
per_source = {}
for d in full["datasets"]:
    src = d["dataset"]
    ps = per_source.setdefault(src, {"rows": 0, "q": 0, "qok": 0, "abs": 0, "absok": 0})
    for r in d["examples"]:
        n_rows += 1; ps["rows"] += 1
        gg = json.loads(r["output"])
        for k in REQ:
            assert k in gg, f"missing {k}"
        # rebuild engine input via documented mapping {a:source,b:target,type:primitive}
        edges = [{"a": e["source"], "b": e["target"], "type": e["primitive"]} for e in gg["atomic_edges"]]
        D, nbrs, _ = forward_closure(KIN, edges)
        text = r["input"].lower()
        for e in gg["atomic_edges"]:
            if e["locally_justifiable"]:
                cue_checked += 1
                sp = e["support_span"]
                if e["surface_cue"] and e["surface_cue"] in text[sp[0]:sp[1]]:
                    cue_ok += 1
        for q in gg["query_edges"]:
            n_q += 1; ps["q"] += 1
            R = D.get((q["source"], q["target"]), set())
            # engine must derive the emitted primitive as a unique singleton
            if len(R) == 1 and next(iter(R)) == q["primitive"]:
                q_ok += 1; ps["qok"] += 1
        for p in gg["absent_relation_pairs"]:
            n_abs += 1; ps["abs"] += 1
            R = D.get((p["source"], p["target"]), set())
            if len(R) == 0:
                abs_ok += 1; ps["absok"] += 1

print("rows:", n_rows)
print(f"PRESENT query round-trip: {q_ok}/{n_q} = {q_ok/n_q:.4f} (engine reproduces emitted gold)")
print(f"ABSENT no-derivation:     {abs_ok}/{n_abs} = {abs_ok/n_abs:.4f} (engine derives EMPTY => abstains)")
print(f"cue-present pass rate:    {cue_ok}/{cue_checked} = {cue_ok/cue_checked:.4f}")
print("per-source:", json.dumps(per_source))
assert q_ok == n_q, "engine FAILED to reproduce some present gold"
assert abs_ok == n_abs, "some absent pair has a non-empty derivation"
assert cue_ok == cue_checked, "some locally-justifiable cue not in span"
# parse mini/preview
for f in ["mini_data_out.json", "preview_data_out.json"]:
    o = json.load(open(os.path.join(WORK, f)))
    assert "metadata" in o and "datasets" in o
    for d in o["datasets"]:
        assert len(d["examples"]) <= 3
print("mini/preview OK")
print("\nALL VERIFICATION CHECKS PASSED")
print("char_length_distribution:", json.dumps(full["metadata"]["char_length_distribution"], indent=1))
print("scale_targets_vs_actuals:", json.dumps(full["metadata"]["scale_targets_vs_actuals"], indent=1))
