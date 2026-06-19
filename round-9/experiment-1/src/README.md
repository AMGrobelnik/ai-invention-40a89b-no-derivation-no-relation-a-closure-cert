# iter-9 — Extraction-recall BOOSTER: can a better extractor flip the certificate net-utility fork?

**One-line result.** Prompt-only extraction strategies **measurably raise** natural-prose atomic
recall above the iter-8 floor (located-in **0.148 → 0.227**, kinship **0.376 → 0.396**) and lift
the closure certificate's present coverage **~3×**, but the recall is **precision-bought**: every
extra edge that lifts coverage also injects false edges that make the certificate *fabricate
sibling paths*, so the decisive same-component-sibling mixed-pool confident-wrong **REDUCTION moves
AWAY from a flip as recall rises** (CI-lower-vs-recall slope **−0.30** located-in / **−0.67**
kinship). No prompt-only strategy flips the pre-registered fork on either domain ⇒
**EXTRACTION-LIMITED-BOUNDARY-CONFIRMED**, now sharpened from "we need more recall" to a quantified
**recall–PRECISION frontier**: the gold-read ceiling headroom (1.0/1.0/1.0) is real but *not
promptable without precision loss*, so the fix requires precision-preserving (fine-tuned)
extraction, not better prompts.

## What is new vs iter-8 (everything else reused VERBATIM)

Reused verbatim as frozen deps (copied into this workspace): `kinship.py` (forward least-fixpoint
UNION closure engine), `dataio_locatedin.py` / `readers_locatedin.py` / `queryside.py` (located-in
harness), `dataio_redocred.py` / `readers_kinship.py` (iter-7 kinship harness), `baselines.py`,
`stats.py`, `llm.py`, `prolog.py`. The entire iter-8 `method.py` is reused as **`core.py`** (a
library of the view / verdict / output functions).

New code:
- **`booster.py`** — ≥4 extraction strategies with a precision guard. `S2 fewshot_enum` (few-shot +
  inventory + explicit NO-OMISSION, max_tokens 1200), `S3 sentencewise` (sentence-by-sentence +
  coref→inventory, max_tokens 1500), `S4 sc_union` (self-consistency UNION over k=4 temp-0.7 samples
  of S2), `S5 multimodel_union` (S2 on gemini ∪ S2 on `mistral-small-2603`), plus high-precision
  variants `*_highprec` (agreement≥2 **AND** cue-supported). The **precision guard**: converse-
  invariant canonicalisation, per-edge source-agreement count, directed-2-cycle drop (keep the
  higher-agreement direction), KEEP iff agreement≥2 **OR** a domain cue phrase co-occurs with both
  endpoint mentions in a sentence window. Ungroundable names → isolated `NAME::` nodes (honest
  recall penalty, never a fabricated link).
- **`method.py`** — per-strategy certificate **recompute** (only `modeA` changes; the 6 confident-
  wrong competitors are FIXED and snapshot-asserted byte-identical), the recall-vs-reduction
  **frontier** + extrapolation, the **stronger cross-model query-side verifier** (deepseek-v3.2,
  k=5), the pre-registered FORK verdict, and the `exp_gen_sol_out` output.
- **`queryside_kinship.py`** / **`kinship_pipeline.py`** — the kinship-domain replication (second
  domain; no sibling regime, so the mixed pool is present + different_component absent).

## Headline numbers (primary reader = `google/gemini-3.1-flash-lite`)

**located-in recall-vs-reduction frontier (decisive same-component-sibling mixed pool):**

| strategy | atomic recall | present cov | cert fraction-caught (sib) | sibling conf-wrong | min-over-6 reduction |
|---|---|---|---|---|---|
| multimodel_union_highprec | 0.054 | 0.012 | — | **0.036** | **−0.017** (best) |
| sc_union_highprec | 0.084 | 0.033 | — | 0.047 | −0.022 |
| **default (= iter-8)** | **0.148** | **0.051** | **0.785** | **0.073** | −0.034 |
| best_effort | 0.186 | 0.113 | 0.711 | 0.096 | −0.045 |
| fewshot_enum | 0.213 | 0.163 | 0.696 | 0.100 | −0.047 |
| sc_union | **0.227** | **0.165** | 0.659 | 0.118 | −0.055 |

The reduction is a **monotone-decreasing** function of recall; the reduction-optimal operating point
is the **highest-precision / lowest-recall** strategy. `S0 default` reproduces iter-8 **exactly**
(recall 0.1478, present cov 0.0505, sibling conf-wrong 0.0733). Gold-read ceiling stays
**1.0/1.0/1.0** across all strategies (engine sound; all headroom is extraction).

**Stronger cross-model verifier (methodology MINOR #5 retired).** On the sibling pool the certificate
catches **0.67–0.79** of the raw LLM's confident containment hallucinations; the same-model weak
verifier catches **0.20**, and a **stronger, different-family** verifier (deepseek-v3.2, k=5) catches
**0.10** — *worse*, because a better geographer over-infers containment. Natural sibling
confident-wrong: certificate **0.07–0.10** vs weak verifier **0.19** vs **strong** verifier **0.22**.
Certificate-necessity is therefore **not** an artifact of using the same weak reader.

**FACT A** (load-bearing, preserved): the raw LLM confidently hallucinates a containment on **30%** of
natural sibling-absent pairs (mean conf 0.94). **Kinship** replicates the same recall→precision→
reduction pattern (slope −0.67; default recall 0.376 reproduces iter-7).

## Pre-registered FORK verdict

`DEMONSTRATED-FIX` (some strategy makes the mixed reduction CI exclude 0 vs all 6 competitors AND
beats the query-side verifier) — **NOT reached**. `EXTRACTION-LIMITED-BOUNDARY-CONFIRMED` —
**reached on both domains**, sharpened to the recall-precision frontier above. This is the honest
fallback-#1/#2 outcome: it lifts the paper from "diagnostic + boundary" to "diagnostic + quantified
recall-precision frontier showing the boundary is fundamental for prompt-only extraction".

## Run

```bash
uv run method.py --slice re-docred --sc-k 10 --booster-sc-k 4 --strong-k 5 --strong-cap 250 \
  --do-kinship --concurrency 16 --budget-hard 9.0
```

- GATE-0 (no LLM): `uv run tests.py` (engine wiring + gold-read ceiling) and
  `uv run test_booster.py` (parser recovers the toy edges, precision guard drops a 2-cycle + an
  ungroundable name, cue-support fires correctly).
- Subsample (doc-clustered, per-doc capped, seed 20260618): 400 held_out + 115 never_annotated + 450
  sibling + 250 diffcomponent = 1215 located-in queries over 283 docs (identical to iter-8 → the
  fixed-baseline reads replay from the iter-8 cache); kinship 279 present + 250 absent over 140 docs
  (replays the iter-7 cache).
- All reads are REAL OpenRouter completions, sha256-cached (`cache/`, git-ignored). One-time
  generation spend ≈ **$1.21** (gemini $0.95 + mistral $0.05 + deepseek $0.20); re-runs replay $0.

## Outputs

`method_out.json` (+ `full_/mini_/preview_` variants), schema `exp_gen_sol_out`, one row per query
in five groups (`locatedin_present`, `locatedin_absent_sibling`, `locatedin_absent_diffcomponent`,
`kinship_present`, `kinship_absent`). `metadata` carries the per-strategy rows (atomic P/R, present
coverage, present selective accuracy, sibling/diffcomp confident-wrong, mixed 6-way confident-wrong
reduction + Holm CIs), the recall-vs-reduction frontier + extrapolation (negative slope → fix is not
promptable), FACT A per regime, the gold-read ceiling, the stronger-verifier block, the cost ledger,
worked traces (a present-RECOVERY newly enabled by the booster, a residual over-abstain still
unsolved, a present composition trace, a sibling no-derivation abstention; Prolog-discharged —
python-checked here as SWI-Prolog is unavailable, labelled truthfully), and the explicit FORK
verdict per domain + overall.
