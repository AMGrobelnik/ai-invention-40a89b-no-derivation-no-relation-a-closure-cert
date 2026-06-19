# Extraction-Recall Booster for the Closure-Certificate Net-Utility Fork

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** experiment  
**ID:** `art_fXvxt4JO9hWy`

## Layman Summary

Tests whether smarter prompting that extracts more facts from text lets a logic certificate beat confidence-based hallucination detectors on natural Wikipedia prose.

## Full Summary

iter-9 experiment that tries to FLIP the iter-8 EXTRACTION-LIMITED-BOUNDARY fork by RAISING natural-prose atomic extraction recall, on two genuinely-natural Re-DocRED absent-relation domains (located-in administrative containment + kinship). It reuses the entire iter-8 located-in harness VERBATIM (the iter-8 method.py is imported as core.py; kinship.py forward-union closure engine, dataio_locatedin/readers_locatedin/queryside, baselines/stats/llm/prolog) and the iter-7 kinship harness (dataio_redocred + readers_kinship), and adds ONE new module booster.py plus a new orchestrator method.py + queryside_kinship.py + kinship_pipeline.py.

METHOD. booster.py sweeps >=4 extraction strategies above the iter-8 floor: S0 default + S1 best-effort (iter-8 arms, cached), S2 fewshot_enum (few-shot + place/person inventory + explicit NO-OMISSION, max_tokens 1200), S3 sentencewise (sentence-by-sentence + coref->inventory, max_tokens 1500), S4 sc_union (self-consistency UNION over k=4 temp-0.7 samples), S5 multimodel_union (gemini ∪ mistral-small-2603), plus high-precision variants (agreement>=2 AND cue-supported). A PRECISION GUARD canonicalises edges converse-invariantly, counts per-edge source agreement, drops directed 2-cycles, and keeps an edge iff agreement>=2 OR a domain cue phrase co-occurs with both endpoint mentions; ungroundable names become isolated NAME:: nodes. Per strategy, ONLY the certificate (modeA) is recomputed; the 6 confident-wrong competitors (verbalized / SC-margin / P(True) / semantic-entropy + query-side verifier + self-verify) stay FIXED and are snapshot-asserted byte-identical (replayed from the iter-8/iter-7 sha256 caches at $0). Downstream views (matched-coverage mixed-pool confident-wrong reduction with doc-clustered Holm B=10000 CIs, abstention decomposition, atomic P/R, FACT A, fraction-caught) are the iter-8 functions reused verbatim.

RESULT (verdict EXTRACTION-LIMITED-BOUNDARY-CONFIRMED, both domains). The booster MEASURABLY raises recall (located-in 0.148->0.227, kinship 0.376->0.396) and lifts the certificate's present coverage ~3x (0.051->0.165), with corr(recall, present_coverage)=0.96 -- the dose-response is real. BUT the recall is PRECISION-BOUGHT: corr(recall, sibling-confident-wrong)=0.91, so injected false edges make the certificate fabricate sibling paths, and the worst-case (min-over-6) mixed-pool confident-wrong REDUCTION moves AWAY from a flip as recall rises (CI-lower-vs-recall slope -0.30 located-in / -0.67 kinship). The reduction-optimal operating point is the HIGHEST-precision / LOWEST-recall strategy; no prompt-only strategy flips the fork. S0 default reproduces iter-8 EXACTLY (recall 0.1478, present cov 0.0505, sibling conf-wrong 0.0733); kinship default recall 0.3762 reproduces iter-7. The gold-read ceiling stays 1.0/1.0/1.0 (engine sound) -- so the headroom is real but NOT promptable without precision loss: the fix requires precision-preserving (fine-tuned) extraction, not better prompts.

SECONDARY (retires methodology MINOR #5). A STRONGER, larger, different-family query-side verifier (deepseek-v3.2, k=5 self-consistency) catches only 0.10 of the raw LLM's confident sibling hallucinations -- WORSE than the same-model weak verifier (0.20) and far below the certificate (0.67-0.79), because a better geographer over-infers containment. Certificate-necessity is therefore not an artifact of a same-model verifier.

FOR THE PAPER. This converts iter-8's 'diagnostic + boundary' into a quantified recall-PRECISION frontier proving the boundary is FUNDAMENTAL for prompt-only extraction, plus a stronger-verifier robustness result. Output method_out.json (schema exp_gen_sol_out, 4.95MB) has 5 corpora (locatedin_present/absent_sibling/absent_diffcomponent + kinship_present/absent), per-strategy rows, the recall-vs-reduction frontier + extrapolation, FACT A, the stronger-verifier block, the cost ledger (one-time $1.21, re-runs $0), and worked traces (a present-RECOVERY newly enabled by the booster, a residual over-abstain, a composition trace, a sibling no-derivation abstention; Prolog python-checked, swipl unavailable, labelled truthfully). All four variants validate against exp_gen_sol_out.

## Dependencies

- `art_RfjDpsGkBXDG` — dataset
- `art_NUWTxBVWENIJ` — dataset
- `art_oUhZgMSjf7lm` — methodology

## Output Files

- `method.py`
- `full_method_out.json`
- `mini_method_out.json`
- `preview_method_out.json`

## Demo Files

- **method.py** — Research methodology implementation

---
*Generated by AI Inventor Pipeline*
