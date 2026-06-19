#!/usr/bin/env python3
"""$0 blocking-gate validation: imports, closure tests, swipl, temporal selection + arm
building, CLUTRR concatenation builder, and the gold-atomic engine go/no-go. NO LLM."""
import method as M
import data_adapter as DA
import synth_channel as SC
from tests import closure_tests_pass
from dataio import load_clutrr, subsample_gen
from kinship import Kinship, query_modeA

ok, _ = closure_tests_pass(verbose=True)
print("closure_tests_pass:", ok)
SC.self_verify_point_algebra()
print("point self-verify OK")
print("swipl:", M.swipl_version())

# temporal selection + arm building (no LLM)
sel, info = M.select_temporal_docs(DA.DEFAULT_DATASET)
print("temporal selection_mode:", info["selection_mode"], "in_band:", info["n_nt_in_band_2500_3500"])
print("selected:", [(d["docid"], d["char_len"]) for d in info["selected"]])
docid, text, G = sel[0]
docs, off = DA.build_corpus("narrativetime", [(docid, text, G)])
arm = DA.build_arm("narrativetime", docs, "POINT", n_target=4, v_max=3, max_per_doc=4)
print(f"arm[{docid}] queries={arm['n_queries']} read_edges={arm['n_edges']} offset_ok={off:.3f}")
items, index = M.TC.make_read_items(arm, "primary")
print("temporal read items built:", len(items))

# kinship concat + gold-atomic go/no-go
gen, disc, comp = load_clutrr(mini=False)
kin = Kinship(comp)
test = subsample_gen(gen, fold="test")
kdocs = M.build_clutrr_concat_docs(test, 2, 6, 3000)
for doc in kdocs:
    print(f"\nkinship doc {doc['doc_id']}: chars={doc['char_len']} substories={doc['n_substories']} "
          f"within={len(doc['within'])} absent={len(doc['absent'])}")
    n_ok = n_tot = 0
    for w in doc["within"]:
        out = query_modeA(kin, doc["gold_atomic_edges"], w["qsrc"], w["qtgt"])
        g = doc["name_gender"].get(w["qtgt"], "male")
        surf = kin.surface(out["answer_type"], g) if out["singleton"] else None
        n_tot += 1
        n_ok += int(surf == w["gold"])
        print(f"  gold-close {w['qsrc']}->{w['qtgt']} gold={w['gold']} pred={surf} singleton={out['singleton']}")
    # spot-check absent pairs are no-path under gold atomics
    n_abs_nopath = sum(1 for ab in doc["absent"]
                       if query_modeA(kin, doc["gold_atomic_edges"], ab["qsrc"], ab["qtgt"])["no_path"])
    print(f"  GO/NO-GO within recovery={n_ok}/{n_tot} | absent no_path={n_abs_nopath}/{len(doc['absent'])}")
print("\nGATE OK")
