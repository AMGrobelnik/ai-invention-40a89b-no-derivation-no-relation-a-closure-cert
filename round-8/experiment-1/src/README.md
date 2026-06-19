# iter-8 — Closure certificate vs 4-signal battery vs query-side false-premise verifier on the NATURAL located-in corpus

**Decisive domain-generality test.** A drop-in adaptation of the iter-7 STEP-B natural-kinship
experiment to a SECOND genuinely-natural absent-relation domain — Re-DocRED geographic /
administrative containment (`located_in` / `contains`) — to show the closure-certificate
confidence-blindness diagnostic is **not kinship-specific**, and to pit the structural
certificate against a **NEW query-side false-premise verifier** (the established method for
this failure mode: FalseQA / AbstentionBench / Wen2024) on the decisive
**same-component-sibling** mixed pool.

## What is new vs iter-7 (everything else is reused VERBATIM)

Reused verbatim: `kinship.py` (forward least-fixpoint UNION closure, here parameterized by the
DEGENERATE `located_in`/`contains` transitive table), `baselines.py`, `stats.py`, `llm.py`
(sha256-cached, hard-capped OpenRouter client), `prolog.py`.

New code:
- `dataio_locatedin.py` — located-in loader with **(1) the held_out direct-edge ABLATION**
  (drop the single directly-annotated `(source,target)` edge from BOTH gold and extracted
  graphs before querying, so a "covered" present decision is a genuine ≥2-hop deduction, not a
  read-back — sound because removing a redundant edge preserves the transitive closure) and
  **(2) the absent-REGIME split** (`same_component_sibling` vs `different_component`).
- `readers_locatedin.py` — containment extraction / raw / PoT prompts (+ best-effort few-shot
  arm) over the `{located in, contains, no-relation}` vocabulary.
- `queryside.py` — the **NEW query-side false-premise VERIFIER + SELF-VERIFICATION** baselines.
- `method.py` — orchestration: the decisive **sibling mixed pool** (non-structural: siblings
  derive EMPTY because `located_in ∘ contains` is UNDEFINED — a *genuine deductive* abstention,
  not disconnected-component) vs the **different_component CONTRAST** (structural-by-construction);
  FACT A per regime; crux **fraction-caught** for all 6 competitors; gold-read ceiling; the
  pre-registered **4-way FORK** verdict.

## Headline result (primary reader = `google/gemini-3.1-flash-lite`, cross-family = `mistralai/mistral-small-2603`)

- **FACT A** — the raw LLM confidently hallucinates a containment on **30%** of natural
  sibling-absent pairs (mean confidence 0.94; 95% at conf ≥ 0.9). Different-component: only 6%
  (disconnected places are easy) — so the **sibling regime is the hard, decisive one**.
- **Certificate catches 78.5%** of those high-confidence sibling hallucinations *structurally*,
  vs ≤ 40% for every dispersion signal (verbalized / SC-margin / P(True) / semantic-entropy) and
  only **27%** for the query-side verifier / **46%** for self-verify. Natural confident-wrong on
  the sibling pool: certificate **0.073** vs raw / all signals **0.30** vs verifier **0.218** —
  the certificate beats the established false-premise detector by ~3×.
- **Cross-family replication** (mistral): FACT A sibling **0.44** (even higher for the weaker
  reader), certificate fraction-caught **0.78** — the diagnostic is **reader-general**.
- **FORK verdict = EXTRACTION-LIMITED-BOUNDARY.** The gold-read ceiling is **1.0 present
  coverage / 1.0 absent abstention / 1.0 present selective accuracy** — the engine is sound — but
  natural-prose extraction recall (~0.15 gemini, ~0.19 best-effort) caps the LLM-read
  certificate's present coverage at ~0.05, so the certificate over-abstains on PRESENT. The
  diagnostic (FACT A + the certificate-beats-all-6 fraction-caught + the gold-read ceiling) stands.

The MIXED-pool matched-coverage *reduction* is degenerate here (the certificate's coverage
collapses under the extraction limit), so the **load-bearing** comparison is the crux
fraction-caught and the natural confident-wrong on the sibling pool (see
`honesty_caveats.matched_coverage_degeneracy_under_extraction_limit`).

## Run

```bash
uv run method.py --slice re-docred --best-effort --cross-family \
  --cross-family-reader mistralai/mistral-small-2603 \
  --sc-k 10 --cf-sc-k 5 --concurrency 16 --budget-hard 6.0
```

- GATE-0 (no LLM) engine wiring: `uv run tests.py` (asserts held_out deduces after ablation;
  sibling + diffcomp abstain EMPTY both directions; gold-read ceiling 1.0/1.0).
- Subsample (doc-clustered, per-doc capped): 400 held_out + 115 never_annotated + 450 sibling +
  250 diffcomponent = 1215 queries over 283 docs.
- All reads are REAL OpenRouter completions, SHA-256 cached (`cache/`, git-ignored); re-runs
  replay at $0. Total spend ≈ **$2.66** (gemini $2.29 + mistral $0.37), well under the $9 cap.

## Outputs

`method_out.json` (+ `full_/mini_/preview_` variants), schema `exp_gen_sol_out`. One row per
query in three groups (`locatedin_present`, `locatedin_absent_sibling`,
`locatedin_absent_diffcomponent`); `metadata` carries the FACT-A-per-regime table, the
fraction-caught crux table, both mixed leaderboards with Holm-adjusted confident-wrong
reductions, the abstention decomposition, the gold-read ceiling, natural-prose atomic P/R
(default + best-effort), the cross-family block, the cost ledger, worked traces (a sibling
no-derivation abstention + an over-abstain-present + a present composition trace, Prolog-
discharged — python-checked here as SWI-Prolog is unavailable, labelled truthfully), and the
explicit FORK verdict.
