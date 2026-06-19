# iter-4 decisive real-text test — Cross-Path Allen-13 Intersection vs Best-Single-Path

**The decisive experiment for reviewer MAJOR #1** (cross-path-intersection mechanism was
synthetic-only in iter-3). Does the cross-path full-PC **INTERSECTION** of disjunctive
Allen interval reads narrow real-text deduction queries strictly **beyond the best single
path's composition**, using the **FULL Allen interval algebra (13 relations)** instead of
the coarse convex point start-point projection that made `full==naive` in iter-3?

## Verdict: **SCOPE-BOUNDARY** (powered, n=125, $0.94 LLM spend)

The cross-path coding mechanism is **structurally present in the gold** (a-priori gate GO,
N=125) and **works on a synthetic Allen channel** (positive control, intersection > best-
single at reader-recall 0.95), but **cannot realize on real text**: LLM Allen reads of the
constituent edges are near-universe / underdetermined for **both** a weak (gemini-3.1-flash-
lite) and a strong cross-family (deepseek-v3.2) reader, in **both** the local and the wider
inter-event window read regimes. This is a sharp, decisive negative that **extends iter-3's
read-soundness finding**: the *richer* Allen algebra that yields gold intersection bite is
exactly the one LLMs cannot read informatively from text.

### Headline numbers (`metadata.headline_findings`)
| quantity | value |
|---|---|
| a-priori gate | **GO**, combined gold-singleton multi-path-with-bite N = **125** (TDDMan; NarrativeTime 0; MATRES 0) |
| H_main intersection − best-single gap (matched coverage, Holm) | **0.0** (CI [0,0], not significant) |
| intersection / best-single singleton-resolution rate | **0.0 / 0.0** |
| window-primary read underdetermined-rate / breadth | **0.79 / 11.5 of 13** |
| local-primary read underdetermined-rate | **0.87** |
| cross-family (deepseek-v3.2) underdetermined-rate / breadth | **0.99 / 12.9 of 13** (more conservative ⇒ not a weak-model artifact) |
| per-edge Allen recall vs 0.85 gate | **0.90**, CI excludes-above-gate (high only because near-universe reads trivially contain gold) |
| synthetic Allen control (recall 0.95): intersection > best-single | **True** |

### The precision/recall impossibility (`metadata.precision_recall_impossibility`)
High-recall disjunctive reads are **sound but near-universe** (breadth ~11.5/13, recall 0.90)
→ 0 intersection bite. Forcing a single tight Allen relation (the **raw** baseline) restores
tightness but is only **~3%** correct → **unsound**. Text underdetermines interval endpoints,
so no reader operating point yields tight-AND-sound Allen reads; the mechanism cannot realize
regardless of prompt or model. The few times the intersection *did* commit to a singleton it
was wrong (`intersection_confident_wrong_rate = 1.0`) — the error-correcting-code failure mode.

## Method (`method.py`)
- **STEP 1 — a-priori multi-path gate** (`gate.py`, zero LLM): on the frozen NarrativeTime +
  TDDMan + MATRES gold graphs, enumerate deduction-required query edges with ≥2 edge-disjoint
  constraining paths whose best-single-path **sound** gold composition is non-singleton and
  whose full-PC intersection strictly tightens toward the atomic gold (`canon ⊆ inter`).
  Pre-registered GO at combined gold-singleton N ≥ 100. **GO at N=125** (all TDDMan;
  NarrativeTime's start-point gold is structurally disjunctive → 0 gold-singleton; MATRES is
  intra/adjacent → 0). Power/MDE table included.
- **STEP 2 — high-recall disjunctive Allen reads** (`allen_layer.py`): span-local and inter-
  event-window reads, gemini-3.1-flash-lite + deepseek-v3.2 cross-family, sha256-cached, hard
  cost-guard < $9.
- **STEP 3 — matched-coverage comparison** (`method.py`): (a) cross-path full-PC intersection,
  (b) **best-single-path** [the critical new baseline], (c) naive single-pass, (d) Path-of-
  Thoughts, (e) raw — doc-clustered paired bootstrap with a **bracketing CI** (R1 fix: a CI
  that excludes its own point estimate is flagged, never reported silently), Holm-adjusted.
- **Synthetic Allen positive control** (`synth_allen.py`): consistent-by-construction Allen
  QCNs + noisy channel; confirms the comparison code detects a true intersection>best-single
  effect when reads are sound.
- **Auditable trace-graphs**: `results/worked_intersection_*.pl` — runnable per-path-
  composition + intersection programs (SWI-Prolog if present, else a self-contained python
  checker; `discharge_method` reported truthfully — swipl is absent here). Traces faithfully
  reproduce the engine intersection (`python_matches_engine = True`).

## Files
- `method.py` — driver (gate → reads → comparison → verdict → output + figures).
- `gate.py` — STEP 1 a-priori multi-path gate (cached to `gate_cache/`).
- `allen_layer.py` — Allen-13 gold/read layer (token map, prompts, parser).
- `synth_allen.py` — synthetic Allen positive control / NO-GO backstop.
- `engine.py`, `data_adapter.py`, `llm.py`, `tests.py`, `corpora.py`, `synth_channel.py` —
  reused verbatim from `iter_3/gen_art/gen_art_experiment_2`.
- `method_out.json` (+ `results/method_out.json`) — schema `exp_gen_sol_out` (validated).
- `results/figures/*.jpg` — risk-coverage, gold-gate bite histogram, realized-bite-vs-paths.
- `gate_diag.py`, `gate_diag2.py` — standalone pre-spend gate diagnostics.

Run: `uv run method.py` (full) · `--mini` / `--limit-n N` (smoke) · `--skip-cross-family`
/ `--skip-nt`. Reads + gate enumeration are cached, so reruns are ~$0.

## Transferable contribution (what survives the negative)
The inherited exact-table composition + the gold-free **abstain-on-collapse** certificate
remain valid (Allen PC is sound; the intersection of sound read sets is always sound). The
cross-path *coding* mechanism is honestly **synthetic-channel-only** on these temporal
corpora; the recommended real-text venue is the multi-path-richer **RCC-8 spatial** corpus
(iter-5), where constituent relations may be more locally readable than Allen intervals.
