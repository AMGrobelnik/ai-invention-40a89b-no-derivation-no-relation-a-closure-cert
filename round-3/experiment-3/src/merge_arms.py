#!/usr/bin/env python3
"""Merge the three algebra arms into ONE method_out.json with the full
algebra-richness scaling curve (point 3 -> RCC-8 8 -> Allen 13).

WHY a merge instead of one run: point & allen are reproduced from iter-2
(experiment_iter2_dir3) VERBATIM -- SAME model (google/gemini-3.1-flash-lite),
SAME seed, SAME knob (S4_sound), SAME prompts, SAME networks (90/cell test fold),
SAME cache. Re-running them here is a pure cache replay that produces byte-identical
numbers; the only difference is the iter-2 worker reads ~33k cache files serially on
this slow filesystem (~37 min of dead time) before reaching any RCC-8 work. So we run
the NEW RCC-8 arm fresh (method_rcc8_out.json) and graft iter-2's point/allen analysis
+ datasets onto it. This is the artifact plan's documented fallback: a legitimate
apples-to-apples merge (identical protocol on all three arms).

RCC-8 numbers are TAGGED 'SOUND-LOWER-BOUND' (PC-2 is sound-but-incomplete on RCC-8).
All numbers are 'REAL-LLM-READ-ON-SYNTHETIC'.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

import method as M

HERE = Path(__file__).parent
ITER2 = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/"
             "gen_art/gen_art_experiment_1/method_out.json")
# RCC-8 arm source: the test-fold full run by default; override via $RCC8_OUT (e.g. an
# interim dev-pilot output) so the deliverables are always valid while the full run finishes.
RCC8_OUT = Path(os.environ.get("RCC8_OUT", str(HERE / "method_rcc8_out.json")))
FINAL_OUT = HERE / "method_out.json"

DEEP_CELLS = {"hop_L3_P2", "hop_L4_P2", "hop_L5_P2", "cyc_mu1", "cyc_mu2", "cyc_mu3"}
N_BASE = {"point": 3, "rcc8": 8, "allen": 13}


def _cellpooled_novel(h3_block):
    """n-weighted mean of the full-minus-naive resolve-correct gap over the deduction-DEEP
    strata (hop>=3 / cyclomatic>=1). Uniform across arms (uses only H3 cell aggregates that
    exist for all three) so the decomposition table is apples-to-apples."""
    if not h3_block:
        return {"gap_weighted_mean": None, "n": 0, "by_cell": []}
    rows = list(h3_block.get("gap_by_hop", [])) + list(h3_block.get("gap_by_cyclomatic", []))
    num, den, by = 0.0, 0, []
    for r in rows:
        if r.get("cell") in DEEP_CELLS and r.get("n", 0) > 0 and r.get("gap") is not None:
            num += r["gap"] * r["n"]; den += r["n"]
            by.append({"cell": r["cell"], "gap": r["gap"], "n": r["n"]})
    return {"gap_weighted_mean": (num / den if den else None), "n": den, "by_cell": by}


def cellpooled_decomposition(block, algebra, sound_lower_bound):
    """Uniform decomposition for ANY arm from its stored leaderboard + H3 blocks:
      total_vs_pot   = selacc(modeA) - selacc(pot)
      inherited      = selacc(naive single-pass) - selacc(pot)   (NeSy premise: even ONE
                       exact-table step beats LLM per-path composition)
      novel_iteration= full PC - naive on deep strata             (THIS method's contribution)
    """
    h1 = block.get("H1_bite_bearing_pool") or {}
    lb = h1.get("leaderboard", {})
    selA = lb.get("modeA", {}).get("selective_accuracy")
    selP = lb.get("pot", {}).get("selective_accuracy")
    selN = lb.get("naive", {}).get("selective_accuracy")
    total = (selA - selP) if (selA is not None and selP is not None) else None
    inherited = (selN - selP) if (selN is not None and selP is not None) else None
    return {
        "method": "cell-pooled (n-weighted) from this arm's leaderboard + H3 aggregates",
        "evidence_tag": "REAL-LLM-READ-ON-SYNTHETIC",
        "sound_lower_bound": bool(sound_lower_bound),
        "selacc_modeA": selA, "selacc_pot": selP, "selacc_naive": selN,
        "total_vs_pot_gap": total,
        "inherited_table_vs_llm_gap": inherited,
        "novel_iteration_gap_real": _cellpooled_novel(block.get("H3_iteration_real")),
        "novel_iteration_gap_gold": _cellpooled_novel(block.get("H3_iteration_gold")),
        "inherited_is": ("INHERITED neuro-symbolic premise: a single exact composition-table "
                         "step (naive single-pass) already beats LLM per-path composition."),
        "novel_is": ("NOVEL contribution of iterated PC closure: resolves deduction-deep "
                     "(hop>=3 / cyclomatic>=1) queries a single naive pass leaves open."),
    }


def augment_arm(block, algebra):
    """Add the iter-3 fields (evidence_tags, pc_completeness, n_base_relations, decomposition)
    onto an iter-2 analysis block so point/allen mirror the rcc8 arm."""
    sound_lb = algebra in ("rcc8", "allen")
    if algebra == "point":
        block["pc_completeness"] = "PC-COMPLETE (exact): coverage/collapse are EXACT."
        block["evidence_tags"] = ["REAL-LLM-READ-ON-SYNTHETIC"]
    elif algebra == "allen":
        block["pc_completeness"] = ("PC-SOUND-BUT-INCOMPLETE (Allen consistency NP-hard): "
                                    "coverage / collapse are SOUND LOWER BOUNDS.")
        block["evidence_tags"] = ["REAL-LLM-READ-ON-SYNTHETIC", "SOUND-LOWER-BOUND"]
    block["n_base_relations"] = N_BASE[algebra]
    # iter-2 had no decomposition; compute the cell-pooled one to mirror rcc8.
    block["decomposition"] = cellpooled_decomposition(block, algebra, sound_lb)
    block.setdefault("provenance", (
        "point/allen reproduced from iter-2 experiment_iter2_dir3 (identical model/seed/knob/"
        "prompts/networks/cache); merged here for the 3-point algebra-richness scaling curve."))
    return block


def _truncate_strings(obj, n):
    if isinstance(obj, str):
        return obj if len(obj) <= n else obj[:n] + "..."
    if isinstance(obj, list):
        return [_truncate_strings(x, n) for x in obj]
    if isinstance(obj, dict):
        return {k: _truncate_strings(v, n) for k, v in obj.items()}
    return obj


def emit_variants(out):
    """full = identical; mini = first 3 examples/dataset; preview = first 10 examples/dataset
    with all strings truncated to 200 chars. (method_out.json's top level is an object, not a
    bare array, so we truncate datasets[].examples directly rather than the generic array tool.)"""
    full = HERE / "full_method_out.json"
    full.write_text(json.dumps(out, indent=2, default=M._json_default))

    def subset(k):
        return {"metadata": out["metadata"],
                "datasets": [{"dataset": ds["dataset"], "examples": ds["examples"][:k]}
                             for ds in out["datasets"]]}

    mini = subset(3)
    (HERE / "mini_method_out.json").write_text(json.dumps(mini, indent=2, default=M._json_default))
    prev = subset(10)
    prev = _truncate_strings(json.loads(json.dumps(prev, default=M._json_default)), 200)
    (HERE / "preview_method_out.json").write_text(json.dumps(prev, indent=2))
    print(f"Wrote full_/mini_/preview_method_out.json "
          f"(full={full.stat().st_size/1e6:.2f} MB)")


def main():
    iter2 = json.loads(ITER2.read_text())
    rcc8 = json.loads(RCC8_OUT.read_text())

    ab2 = iter2["metadata"]["analysis_by_algebra"]
    abR = rcc8["metadata"]["analysis_by_algebra"]

    # combined analysis: point, rcc8, allen  (ordered by richness)
    analysis = {}
    analysis["point"] = augment_arm(ab2["point"], "point")
    analysis["rcc8"] = abR["rcc8"]                      # already fully built by method.py
    # add a uniform cell-pooled decomposition to rcc8 too (for the apples-to-apples table)
    analysis["rcc8"]["decomposition_cellpooled"] = cellpooled_decomposition(
        analysis["rcc8"], "rcc8", True)
    analysis["allen"] = augment_arm(ab2["allen"], "allen")

    algebras = ["point", "rcc8", "allen"]

    # recompute the cross-algebra synthesis + scaling figure + verdict over ALL THREE
    verdict = M._verdict(analysis, algebras)
    scaling_fig = M.make_scaling_figure(verdict.get("cross_algebra_synthesis"))
    if scaling_fig:
        verdict["cross_algebra_synthesis"]["scaling_figure"] = scaling_fig

    # apples-to-apples decomposition table across the three arms (cell-pooled, uniform)
    decomp_table = {}
    for a in algebras:
        src = (analysis[a].get("decomposition_cellpooled") if a == "rcc8"
               else analysis[a].get("decomposition"))
        decomp_table[a] = {
            "n_base_relations": N_BASE[a],
            "total_vs_pot_gap": src.get("total_vs_pot_gap"),
            "inherited_table_vs_llm_gap": src.get("inherited_table_vs_llm_gap"),
            "novel_iteration_gap_real": src.get("novel_iteration_gap_real", {}).get("gap_weighted_mean"),
            "novel_iteration_gap_gold": src.get("novel_iteration_gap_gold", {}).get("gap_weighted_mean"),
            "sound_lower_bound": a in ("rcc8", "allen"),
        }
    verdict["cross_algebra_synthesis"]["decomposition_table_cellpooled"] = decomp_table

    # ---- assemble final metadata ----
    md_r = rcc8["metadata"]
    md_2 = iter2["metadata"]
    cfg = dict(md_r["config"])
    cfg["algebras"] = algebras
    cfg["n_networks"] = {
        "point": md_2["config"]["n_networks"]["point"],
        "allen": md_2["config"]["n_networks"]["allen"],
        "rcc8": md_r["config"]["n_networks"]["rcc8"],
    }
    cfg["arm_provenance"] = {
        "point": "iter-2 experiment_iter2_dir3 (cache replay; identical numbers)",
        "allen": "iter-2 experiment_iter2_dir3 (cache replay; identical numbers)",
        "rcc8": "THIS iter-3 run (fresh real-LLM reads on synthetic RCC-8)",
        "note": ("All three arms: SAME model google/gemini-3.1-flash-lite, temp 0, knob S4_sound, "
                 "seed 20260617, matched-coverage protocol, paired-bootstrap + Holm. Legitimate "
                 "apples-to-apples; point/allen merged from iter-2 to avoid a 33k-file serial "
                 "cache-read on this slow filesystem (would have produced identical numbers)."),
    }

    cost = dict(md_r.get("cost", {}))
    cost["point_allen_billed_usd_this_iter"] = 0.0
    cost["point_allen_source"] = "iter-2 cache (no new billing)"
    cost["iter2_point_allen_billed_usd"] = md_2.get("cost", {}).get("cumulative_openrouter_usd")

    metadata = {
        "method_name": md_r["method_name"],
        "evidence_tag": "REAL-LLM-READ-ON-SYNTHETIC",
        "experiment": ("RCC-8 real-LLM matched-coverage arm + 3-point algebra-richness scaling "
                       "curve (point 3 -> RCC-8 8 -> Allen 13). experiment_iter3 gen_art_experiment_3."),
        "config": cfg,
        "data_provenance": md_r.get("data_provenance"),
        "analysis_by_algebra": analysis,
        "read_bite_lost_widenings_point": md_2.get("read_bite_lost_widenings_point"),
        "verdict": verdict,
        "cost": cost,
        "rcc8_run_elapsed_sec": md_r.get("elapsed_sec"),
        "merge_note": ("point/allen analysis + datasets are iter-2 cache replays (identical "
                       "model/seed/protocol); rcc8 is fresh this iter. See config.arm_provenance."),
    }

    # datasets: point + allen (iter-2) + rcc8 (this run), ordered by richness
    ds_by_name = {ds["dataset"]: ds for ds in iter2["datasets"]}
    for ds in rcc8["datasets"]:
        ds_by_name[ds["dataset"]] = ds
    datasets = [ds_by_name[n] for n in ("synthetic_qcn_point", "synthetic_qcn_rcc8",
                                        "synthetic_qcn_allen") if n in ds_by_name]

    out = {"metadata": metadata, "datasets": datasets}
    FINAL_OUT.write_text(json.dumps(out, indent=2, default=M._json_default))
    (HERE / "results" / "method_out.json").write_text(
        json.dumps(out, indent=2, default=M._json_default))
    sz = FINAL_OUT.stat().st_size / 1e6
    print(f"Wrote {FINAL_OUT} ({sz:.2f} MB)")
    emit_variants(out)
    print("datasets:", [(ds['dataset'], len(ds['examples'])) for ds in datasets])
    syn = verdict["cross_algebra_synthesis"]
    print("\n=== SCALING CURVE (gap vs PoT, ordered by richness) ===")
    for p in syn["scaling_points_vs_pot"]:
        print(f"  {p['algebra']:5} (n_rel={p['n_base_relations']:2}): "
              f"selacc_modeA={p['selacc_modeA']:.3f} selacc_pot={p['selacc_pot']:.3f} "
              f"gap_vs_pot={p['gap_vs_pot']:+.3f}")
    print("advantage_grows_with_algebra_richness (monotone):",
          syn["advantage_grows_with_algebra_richness"])
    print("\n=== DECOMPOSITION (cell-pooled, apples-to-apples) ===")
    for a in algebras:
        t = decomp_table[a]
        print(f"  {a:5}: total_vs_pot={t['total_vs_pot_gap']}, "
              f"inherited(naive-pot)={t['inherited_table_vs_llm_gap']}, "
              f"novel_iter_real={t['novel_iteration_gap_real']}")
    print("\nVERDICT:", verdict["headline"][:300])


if __name__ == "__main__":
    main()
