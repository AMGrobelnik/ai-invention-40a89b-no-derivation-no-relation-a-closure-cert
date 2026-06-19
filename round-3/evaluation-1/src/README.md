# Evaluation: decompose the +0.676 gap · risk-coverage · H1–H4 multiplicity

**Pure re-analysis of three iter-2 experiment outputs. ZERO LLM spend, no method re-run, no data collection.**

`eval.py` loads the three `full_method_out.json` files (showdown `art_N0e4pH_C_Cxw`,
channel `art_FtN4LBzazO_l`, real-text `art_fil2iJ6xSrYx`) and recomputes / reorganizes statistics
into `eval_out.json` (schema `exp_eval_sol_out`) plus a human-readable `eval_digest.md`.

## What it does

1. **Decomposition (Task 1)** — splits the Mode-A-vs-PoT system gap additively into an
   **INHERITED** exact-table-vs-LLM-composition component and a **NOVEL** iteration component, and
   separates the *selective-accuracy* axis from the *coverage/resolution* axis:
   - Allen bite pool: system_gap **+0.676** = inherited **+0.673** + novel_selacc **+0.0025**
     (additivity residual 0.000). On the selective-accuracy axis the gap is almost entirely the
     inherited neuro-symbolic premise; iteration adds ~0.
   - The genuine iteration novelty lives on the **coverage axis**: full−naive resolve-to-correct
     gap **+0.344 (point) / +0.144 (Allen)** at L=3, growing with hop & cyclomatic number, exact
     tie at length-2. Paired bootstrap CIs (B=10000, seed 20260617), Jonckheere/Spearman trends
     (recomputed JT z matches F1 exactly), Holm-adjusted family CIs, F2 per-recall-slice
     cross-source corroboration, corrected Page-p note (1e-13 → ~5e-4 order).
2. **Risk-coverage (Task 2)** — re-presents the real-text hallucination result as a risk-coverage
   view: Mode-A confident-wrong 0.65→0.0 **at ~90% abstention (answered 2/20)**; matched-coverage
   advantage NOT significant at n=20 (boot p vs raw 0.394 / PoT 0.254 / SC 0.175); AUC reused
   (n=20, underpowered); read-soundness caveat.
3. **Multiplicity (Task 3)** — Holm-Bonferroni + hierarchical gatekeeping over {H1,H2,H3,H4}:
   H2 (hallucination) CLEARS coverage-conditionally, H3/H4 CONFIRMED on synthetic, H1 (real-text
   transfer) FAILS; everything else tagged EXPLORATORY.

Retires the "central claim conflates two effects" MAJOR and the "hallucination driven by
abstention" MINOR.

## Run

```bash
uv venv .venv --python=3.12 && source .venv/bin/activate && uv pip install numpy scipy loguru
python eval.py            # full re-analysis (~13 s, CPU only)
python eval.py 200        # smoke test on first 200 per-network rows
```

## Output

- `eval_out.json` — `metadata` (eval_name, evidence_tags, llm_spend_usd=0.0, sources,
  decomposition, risk_coverage, multiplicity, summary_for_paper, provenance), `metrics_agg`
  (45 flat headline numbers), `datasets` (decomposition / risk-coverage / multiplicity tables as
  schema-valid rows). All plan-specified top-level keys live under `metadata` because the
  `exp_eval_sol_out` schema forbids extra top-level keys.
- `eval_digest.md` — human-readable mirror of `summary_for_paper` for GEN_PAPER_TEXT.

17/17 sanity checks pass, 0 discrepancies, additivity holds to 0.000, strict-valid JSON
(NaN/Inf → null). File is 0.08 MB, so no split / mini / preview variants are needed (<15 MB).
