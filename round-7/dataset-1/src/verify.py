#!/usr/bin/env python3
"""Final QA + DROP-IN engine ROUND-TRIP GATE for the located-in corpus.

For EVERY row, rebuild the closure input from atomic_edges via the documented
engine_edge_mapping {a:source, b:target, type:primitive}, run kinship.py's forward
least-fixpoint closure UNCHANGED, and assert:

  (i)   every PRESENT query reproduces D=={'located_in'} (singleton EMIT):
          - query_kind='never_annotated' : on the FULL atomic edge set (pair not annotated);
          - query_kind='held_out'        : after DROPPING the single (source,target) atomic
            edge, the engine STILL derives located_in (genuine deduction-required), and that
            edge IS present in atomic_edges;
  (ii)  every ABSENT pair yields D[(a,b)]==EMPTY AND D[(b,a)]==EMPTY (ABSTAIN), both dirs;
  (iii) report any Mode-B conflicts (|D|>1 from annotation cycles);
  (iv)  cue-present pass rate for locally_justifiable atomic edges.

FAILS loudly on any mismatch -- passing the gate guarantees the iter-8 battery experiment
(which loads this exact engine) is drop-in compatible.
"""
import json, os
from kinship import Kinship, forward_closure

WORK = os.path.dirname(os.path.abspath(__file__))
full = json.load(open(os.path.join(WORK, "full_data_out.json")))
CT = full["metadata"]["composition_table"]
KIN = Kinship(CT)
PRIM = "located_in"

REQ = ["nodes", "atomic_edges", "query_edges", "absent_relation_pairs", "absent_pairs_source"]
n_rows = 0
n_q_na = q_na_ok = 0           # never_annotated present
n_q_ho = q_ho_ok = ho_inset = 0  # held_out present
n_abs = abs_ok = 0
n_modeb = 0
cue_checked = cue_ok = 0
per_source = {}

for d in full["datasets"]:
    src = d["dataset"]
    ps = per_source.setdefault(src, {"rows": 0, "q_na": 0, "q_ho": 0, "abs": 0, "absok": 0})
    for r in d["examples"]:
        n_rows += 1; ps["rows"] += 1
        gg = json.loads(r["output"])
        for k in REQ:
            assert k in gg, f"missing {k}"
        full_edges = [{"a": e["source"], "b": e["target"], "type": e["primitive"]} for e in gg["atomic_edges"]]
        edge_set = {(e["source"], e["target"]) for e in gg["atomic_edges"]}
        dir_edges = {(e["source"], e["target"]) for e in gg["atomic_edges"] if e["primitive"] == PRIM}
        D, nbrs, _ = forward_closure(KIN, full_edges)
        n_modeb += sum(1 for ts in D.values() if len(ts) > 1)
        text = r["input"].lower()
        for e in gg["atomic_edges"]:
            if e["locally_justifiable"]:
                cue_checked += 1
                sp = e["support_span"]
                if e["surface_cue"] and e["surface_cue"] in text[sp[0]:sp[1]]:
                    cue_ok += 1
        for q in gg["query_edges"]:
            s, t = q["source"], q["target"]
            # human-auditable trace check: derivation_path must be a VALID directed located_in chain
            chain = [s] + q["derivation_path"] + [t]
            assert len(chain) >= 3, f"present query hop<2 in {gg['doc_id']}"
            for x, y in zip(chain, chain[1:]):
                assert (x, y) in dir_edges, f"invalid derivation step {x}->{y} in {gg['doc_id']}"
                if q["query_kind"] == "held_out":
                    assert (x, y) != (s, t), f"held_out path uses the held-out edge in {gg['doc_id']}"
            if q["query_kind"] == "held_out":
                n_q_ho += 1; ps["q_ho"] += 1
                if (s, t) in edge_set:
                    ho_inset += 1
                # ABLATE the single held-out edge, then the engine must still DEDUCE located_in
                seed_wo = [{"a": e["source"], "b": e["target"], "type": e["primitive"]}
                           for e in gg["atomic_edges"] if (e["source"], e["target"]) != (s, t)]
                Dw, _, _ = forward_closure(KIN, seed_wo)
                R = Dw.get((s, t), set())
                if len(R) == 1 and next(iter(R)) == PRIM:
                    q_ho_ok += 1
            else:
                n_q_na += 1; ps["q_na"] += 1
                R = D.get((s, t), set())
                if len(R) == 1 and next(iter(R)) == PRIM:
                    q_na_ok += 1
        for p in gg["absent_relation_pairs"]:
            n_abs += 1; ps["abs"] += 1
            a, b = p["source"], p["target"]
            if not D.get((a, b)) and not D.get((b, a)):     # EMPTY in BOTH directions
                abs_ok += 1; ps["absok"] += 1

print("rows:", n_rows)
print(f"PRESENT never_annotated round-trip: {q_na_ok}/{n_q_na} = {q_na_ok/max(1,n_q_na):.4f} (full-KB singleton EMIT)")
print(f"PRESENT held_out round-trip:        {q_ho_ok}/{n_q_ho} = {q_ho_ok/max(1,n_q_ho):.4f} (deduced AFTER ablating the direct edge)")
print(f"  held_out edge present in atomic_edges: {ho_inset}/{n_q_ho}")
print(f"ABSENT no-derivation (both dirs):    {abs_ok}/{n_abs} = {abs_ok/max(1,n_abs):.4f} (engine derives EMPTY => abstains)")
print(f"cue-present pass rate:               {cue_ok}/{cue_checked} = {cue_ok/max(1,cue_checked):.4f}")
print(f"Mode-B conflicts (annotation cycles): {n_modeb}")
print("per-source:", json.dumps(per_source))

assert q_na_ok == n_q_na, "engine FAILED to reproduce some never_annotated present gold"
assert q_ho_ok == n_q_ho, "engine FAILED to deduce some held_out present gold after ablation"
assert ho_inset == n_q_ho, "some held_out query edge is missing from atomic_edges"
assert abs_ok == n_abs, "some absent pair has a non-empty derivation in some direction"
assert cue_ok == cue_checked, "some locally-justifiable cue not in its support span"

for f in ["mini_data_out.json", "preview_data_out.json"]:
    o = json.load(open(os.path.join(WORK, f)))
    assert "metadata" in o and "datasets" in o
    for d in o["datasets"]:
        assert len(d["examples"]) <= 3
print("mini/preview OK")
print("\nALL VERIFICATION CHECKS PASSED")
print("char_length_distribution:", json.dumps(full["metadata"]["char_length_distribution"], indent=1))
print("scale_targets_vs_actuals:", json.dumps(full["metadata"]["scale_targets_vs_actuals"], indent=1))
