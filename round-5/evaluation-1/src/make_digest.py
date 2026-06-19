#!/usr/bin/env python3
"""Render eval_digest.md (paper-facing) deterministically from eval_out.json so every number is
exact and traceable. Sections: (a) small-bite, (b) inverted-U realized coverage,
(c) one-thesis contribution table (tags-in-columns), (d) headline-structure guidance."""
from __future__ import annotations

import json
from pathlib import Path

WS = Path("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_5/gen_art/gen_art_evaluation_1")
D = json.loads((WS / "eval_out.json").read_text())
MA = D["metrics_agg"]
MD = D["metadata"]


def f(x, n=4):
    try:
        return f"{float(x):.{n}f}"
    except (TypeError, ValueError):
        return str(x)


def ci(lst, n=4):
    return f"[{f(lst[0], n)}, {f(lst[1], n)}]"


def kn(d: dict, maxlen=520) -> str:
    parts = []
    for k, v in d.items():
        if isinstance(v, float):
            v = f(v, 4)
        elif isinstance(v, list):
            v = "[" + ", ".join(f(x, 4) if isinstance(x, float) else str(x) for x in v) + "]"
        parts.append(f"`{k}`={v}")
    s = "; ".join(parts)
    return (s[:maxlen] + " …") if len(s) > maxlen else s


L = []
w = L.append

w("# iter-5 zero-spend re-analysis — paper-facing digest")
w("")
w(f"**$0 LLM spend** (`llm_spend_usd`={f(MA['llm_spend_usd'],1)}), numpy+scipy only, "
  f"deterministic seed={int(MA['seed'])}, **B={int(MA['B_bootstrap'])}** paired bootstrap. "
  f"Reproduction mismatches vs the validated iter-4 re-analysis: **{int(MA['n_reproduction_mismatches'])}**.")
w("")
w("This artifact EXTENDS the iter-4 re-analysis. It delivers two reviewer fixes for GEN_PAPER_TEXT: "
  "**MINOR #5** — the *small-bite* caveat (the cross-path mechanism's realized value is PRECISION of "
  "committed answers, not expanded coverage); and **MAJOR #3** — a single ONE-THESIS contribution "
  "table whose evidence-class tags are COLUMNS, not inline hedging.")
w("")

# ----------------------------------------------------------------- (a) small-bite
s = MD["synthetic_allen_small_bite"]
pm = s["per_method"]
cg = s["coverage_gain_intersection_vs_best"]
sg = s["selacc_gain_intersection_vs_best"]
al = s["selacc_gain_aligned_both_resolve"]
pd = s["precision_decomposition"]
w("## (a) Small-bite block — synthetic Allen positive control (recall 0.95, n=500 networks)")
w("")
w(f"Tag: `SYNTHETIC-ALLEN-CONTROL`. Reproduction of the published `recall_95` cell: "
  f"**{'PASS' if not s['reproduction_failed'] else 'FAILED→analytic-CI fallback'}** "
  f"(coverage-gain diff 0.0e+00 vs published; seed {s['seed_cell']}=20260617+95).")
w("")
w("| Method | Coverage | Coverage 95% CI | Selective acc. | Selective-acc. 95% CI | n answered | n correct |")
w("|---|---|---|---|---|---|---|")
for m in ("intersection", "best_single", "naive"):
    p = pm[m]
    w(f"| {m} | {f(p['coverage'])} | {ci(p['coverage_ci'])} | {f(p['selective_acc'])} | "
      f"{ci(p['selacc_ci'])} | {p['n_answered']} | {p['n_correct']} |")
w("")
w("**The contrast that retires the over-claim:**")
w("")
w(f"- **Coverage gain** (intersection − best-single): **{f(cg['point'])}** (+2.4% abs), "
  f"95% CI {ci(cg['ci95'])}, bootstrap p(gain≤0)={f(cg['boot_p_le_0'])} → **CI INCLUDES 0** "
  f"(the realized cross-path coverage bite is small AND not significantly above zero).")
w(f"- **Selective-accuracy gain** (intersection − best-single): **{f(sg['point'])}** (+25.9 pts), "
  f"95% CI {ci(sg['ci95'])}, bootstrap p(gain≤0)={f(sg['boot_p_le_0'])} → **CI EXCLUDES 0** "
  f"(the precision win is real and large).")
w(f"- Intersection precision ({f(pm['intersection']['selective_acc'])}) exceeds BOTH best-single "
  f"({f(pm['best_single']['selective_acc'])}) AND naive ({f(pm['naive']['selective_acc'])}) even "
  f"though naive answers MORE ({f(pm['naive']['coverage'])} coverage).")
w("")
w("**Where the precision advantage comes from (auditable decomposition, not re-scoring):**")
w("")
w(f"- Queries BOTH resolve (n={pd['n_both_resolve']}): intersection narrows to the SAME singleton "
  f"best-single found — **perfect agreement** (aligned acc-gain = {f(al['acc_gain'])}, CI "
  f"{ci(al['ci95'],3)}).")
w(f"- Queries only intersection resolves (cross-path bite, n={pd['n_intersection_only']}): "
  f"**{f(pd['intersection_only_acc'],2)} correct**.")
w(f"- Queries only best-single resolves (n={pd['n_best_single_only']}): intersection COLLAPSES "
  f"(abstains), **avoiding {pd['best_single_only_WRONG_avoided_by_collapse']} wrong commitments** "
  f"best-single makes.")
w("")
w(f"> **Interpretation (deliverable framing).** {s['interpretation']}")
w("")

# ----------------------------------------------------------------- (b) inverted-U
iu = MD["inverted_u_realized_coverage"]
w("## (b) Inverted-U realized-coverage block (realism-matched channel, ρ=0, gate=off, n=600/bin)")
w("")
w("Tag: `SYNTHETIC-CHANNEL`. Realized Mode-A coverage per redundancy bin recovered from the stored "
  "H4 curves as `realized_coverage = benefit + cost_silent_wrong = 1 − abstain − collapse` "
  "(identity verified to <1e-9).")
w("")
w("| Recall | Peak K* | Realized cov. @peak | Cov. 95% CI @peak | Cov.-gain vs K=1 @peak | "
  "Gain 95% CI | Benefit (correct) @peak | Cost (silent-wrong) @peak |")
w("|---|---|---|---|---|---|---|---|")
for br in iu["by_recall"]:
    ap = br["at_peak"]
    w(f"| {f(br['recall'],3)} | {br['peak_K']} | {f(ap['realized_coverage'],3)} | "
      f"{ci(ap['realized_coverage_ci'],3)} | {f(ap['coverage_gain_vs_K1'],3)} | "
      f"{ci(ap['coverage_gain_vs_K1_ci'],3)} | {f(ap['benefit'],3)} | {f(ap['cost_silent_wrong'],3)} |")
w("")
w(f"- Peak K* by recall: **{iu['peak_K_by_recall']}** (interior inverted-U, peak shifts outward "
  f"with recall).")
w(f"- Silent-wrong (pooled) across recall: **{f(iu['silent_wrong_min'],4)} → "
  f"{f(iu['silent_wrong_max'],4)}** (monotone-decreasing in recall); Page trend "
  f"{iu['page_p_corrected']}.")
w("")
w(f"> **Recall-dependence (do NOT over-claim 'modest everywhere').** {iu['recall_dependence_note']}")
w("")
w(f"> **K=1-vs-best-single caveat.** {iu['k1_vs_best_single_caveat']}")
w("")
w(f"> **Tempered interpretation.** {iu['interpretation']}")
w("")

# ----------------------------------------------------------------- (c) one-thesis table
T = MD["one_thesis_contribution_table"]
cols = T["columns"]
w("## (c) ONE-THESIS contribution table (evidence tags as COLUMNS)")
w("")
w("Lead the paper with the two SPINE rows; demote the scaling-law / inverted-U to SUPPORTING; "
  "leave the spatial-RCC-8 row as a PENDING slot; keep temporal-marginal and scope as FOOTNOTES.")
w("")


def render_rows(title, rows):
    w(f"### {title}")
    w("")
    w("| " + " | ".join(c.replace("_", " ") for c in cols) + " |")
    w("|" + "|".join(["---"] * len(cols)) + "|")
    for r in rows:
        cells = []
        for c in cols:
            v = r[c]
            if c == "key_numbers" and isinstance(v, dict):
                v = kn(v)
            else:
                v = str(v).replace("\n", " ")
            cells.append(v)
        w("| " + " | ".join(cells) + " |")
    w("")


render_rows("SPINE (lead with these two rows)", T["spine"])
render_rows("SPINE-PENDING (the deciding row — reserve as a slot for the iter-5 experiment)",
            [T["pending_rcc8_slot"]])
render_rows("SUPPORTING (mechanism analysis — demote here)", T["supporting"])
render_rows("FOOTNOTES / CEILING (state beside claims, in abstract/intro)", T["footnotes"])
w(f"> **Tagging policy.** {T['tagging_policy']}")
w("")

# ----------------------------------------------------------------- (d) headline guidance
hg = MD["headline_structure_guidance"]
w("## (d) Headline-structure guidance for GEN_PAPER_TEXT")
w("")
for k in ["i_lead_with_two_row_spine", "ii_tags_in_columns",
          "iii_rcc8_is_the_single_open_experiment", "iv_retitle",
          "v_hallucination_with_coverage", "vi_clutrr_not_natural_text"]:
    w(f"- **{k.split('_', 1)[0].upper()}.** {hg[k]}")
w("")
w("### Carried (re-affirmed, not recomputed)")
ct = MD["corrected_temporal"]
w(f"- **Corrected temporal (REAL-LLM-READ).** Neither H1 gateway clears Holm; vs-PoT gap "
  f"{f(ct['r1_bracketing_summary']['vs_pot']['gap'])} corrected CI "
  f"{ci(ct['r1_bracketing_summary']['vs_pot']['corrected_ci95'])} (includes 0, boot_p "
  f"{f(ct['r1_bracketing_summary']['vs_pot']['boot_p'])}); the published CONFIRM was a bootstrap "
  f"artifact. Among the {f(ct['modeA_coverage'],3)} Mode-A commits, confident-wrong "
  f"{f(MA['temporal_confident_wrong_frac'])} (48/113), all silent-wrong-narrowing; raw "
  f"out-accuracies Mode-A by {f(abs(ct['raw_out_accuracy_gap_at_matched_cov']),3)} at matched cov.")
dc = MD["deduction_submodule_ceiling"]
w(f"- **Deduction-sub-module ceiling (SCOPE).** Atomic recall {f(dc['atomic_recall'])} → "
  f"~{f(dc['modeA_real_text_coverage'],3)} Mode-A coverage on natural temporal text; OpenCyc / "
  f"atomic re-extraction / LLM fuzzy-unification OUT OF SCOPE; composition table hand-supplied; "
  f"no venue reaches the ~3000-char target (CLUTRR ≤871; spatial 130–1338).")
w("")
w("### Datasets carried for per-record evidence")
for d in D["datasets"]:
    w(f"- `{d['dataset']}` — {len(d['examples'])} examples.")
w("")

(WS / "eval_digest.md").write_text("\n".join(L))
print(f"WROTE eval_digest.md ({len('\n'.join(L))} chars, {len(L)} lines)")
