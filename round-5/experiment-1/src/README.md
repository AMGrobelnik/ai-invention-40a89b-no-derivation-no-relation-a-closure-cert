# Decisive Spatial RCC-8 Test: cross-path-intersection FORK + real-venue closure-certified deduction

Two pre-registered questions on **SpaRTUN / SpaRP-PS1** — the strongest real spatial venue
(27.4 % structurally-flagged "tight multipath" per the iter-4 prevalence gate). CPU-only;
total LLM spend **$0.225** (< $9 hard cap); cached reruns are $0.

## Q1 — cross-path-intersection FORK → **SCOPE-BOUNDARY (gold-structural, $0)**
Does the full-PC **intersection** of disjunctive LLM RCC-8 / cardinal reads narrow deduction
queries strictly beyond best-single-path composition? A **zero-LLM a-priori gate over
VERIFIED gold composition** (`gate_spatial.py`) shows the structure is **absent in the gold
graphs of both single algebras**:
- **RCC-8 subgraph is a containment TREE** — all 228 RCC-8 deduction queries have exactly 1
  edge-disjoint path (`maxdisjoint={1: 228}`); zero same-algebra redundancy.
- **Cardinal subgraph**: 57 deduction queries have ≥2 short disjoint paths, but
  `best_single_len_hist={1:54, 2:2, 3:1}` — the single short path's CDC composition is already
  a **singleton** (54/57), so intersection has no room to add bite; the 3 non-singleton cases
  collapse or fail soundness (annotation noise).
- The corpus's 27.4 % flag is **purely structural** (undirected, mixed-algebra, no composition);
  the real redundancy is **cross-algebra** (topology ⊥ direction), not intersectable in one
  calculus. The mechanism is therefore **synthetic-only** here — a *sharper* negative than the
  iter-4 temporal one (it needs no LLM reads at all).

The mechanism **is real when same-algebra redundancy + sound reads exist**: the synthetic
RCC-8 positive control (1-D interval model) at recall 0.95 gives intersection selective-acc
**0.89 > 0.80** best-single (+0.093, mean bite 1.23), degrading correctly as recall drops.

## Q2 — real-venue closure-certified deduction vs neural baselines → **ABSTENTION-DRIVEN hallucination reduction**
On the **228 single-path RCC-8 deduction queries** SpaRP-PS1 *does* host, the neuro-symbolic
method (read local stated RCC-8 constituents → exact GQR-table compose → **abstain on collapse
/ non-singleton**) is compared against raw LLM generation and chain-of-thought:

| method | confident-wrong (hallucination) | coverage | resolution |
|---|---|---|---|
| raw LLM (forced) | 0.193 | 1.00 | 0.81 |
| chain-of-thought | 0.123 | 1.00 | 0.88 |
| **closure-certified (ours)** | **0.022** | 0.15 | 0.13 |
| raw LLM + abstain (neural baseline) | 0.035 | 0.29 | 0.25 |
| gold-read oracle | 0.000 | 0.89 | 0.89 |

The confident-wrong reduction (0.193 → 0.022, 95 % CI [0.118, 0.228], Holm-significant) is
**real but ABSTENTION-DRIVEN, not an accuracy gain**: the method answers only 15 % of queries;
**at matched coverage the raw LLM is not less accurate** (0.853 vs 0.941, gap CI [−0.22, 0.04]),
and a neural baseline with the same abstention signal is competitive. The **gold-read oracle
resolves 0.89 at 0 hallucination** → the symbolic engine is **sound and not the bottleneck**;
the binding constraint is **constituent read recall (0.55)** under the coverage-vs-soundness
tradeoff. Spatial RCC-8 reads are far more informative than temporal-Allen reads (breadth
2.1/8 vs 11.5/13, underdetermined 0.04 vs 0.87) → the spatial negative is **structural, not a
read-quality failure**. Net: the certified abstain-on-collapse mechanism converts confident-
wrong LLM outputs into **auditable abstentions**, but does not beat a confidence-thresholded
neural baseline on this venue — the value is interpretability of the abstention, not raw accuracy.

## Files
- `engine.py` — RCC-8 + CDC (= product of two convex point algebras) QCN closure engine
  (Mackworth PC-2, `naive_single_pass`); `python engine.py` runs the blocking 64+81-cell self-test.
- `rcc8_layer.py` — disjunctive RCC-8 / CDC read + CoT prompts, robust parser, orientation.
- `cardinal` — built inside `engine.build_cardinal_algebra()` (verified vs GQR cd.comp recipe).
- `synth_rcc8.py` — synthetic RCC-8 positive control + audit-instance finder.
- `spatial_adapter.py` — loads the frozen spatial corpus; recovers SpaRP object descriptions
  from the raw `symbolic_entity_map` (100 % usable); per-algebra subgraphs.
- `gate_spatial.py` — the zero-LLM a-priori gate + single-path deduction-query collector.
- `tests_rcc8.py` — blocking closure unit tests (naive==full@len2, naive≠full@chain, Mode-B
  collapse, multi-path narrowing, orientation).
- `method.py` — main driver (Stage-0 tests → synthetic control → gate → real reads → leaderboard
  → Prolog audit → figures → `method_out.json`).
- `method_out.json` (+ `full_/mini_/preview_`) — results; validates against `exp_gen_sol_out`.
- `results/figures/` — risk-coverage, gold-bite cascade, read-informativeness, synthetic control.

Run: `OPENROUTER_API_KEY=... .venv/bin/python method.py` (full) or `--mini` (smoke).
Every number is tagged REAL-LLM-READ / GOLD-ONLY-GATE / SYNTHETIC-RCC8-CONTROL / THEOREM.
RCC-8 PC is sound-but-incomplete (coverage/collapse are sound lower bounds); CDC is convex →
PC complete. The `cache/` directory (content-addressed LLM reads) is excluded from publication.
