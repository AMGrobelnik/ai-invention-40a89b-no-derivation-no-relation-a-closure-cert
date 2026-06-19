# Real-LLM Matched-Coverage Baseline Showdown on the Synthetic QCN Backbone

**experiment_iter2_dir3** — every number is tagged `REAL-LLM-READ-ON-SYNTHETIC`.

A real OpenRouter LLM (`google/gemini-3.1-flash-lite`, temp 0) reads the synthetic NL
realizations of the QCN backbone (`gen_art_dataset_2`); the disjunctive **local** reads
feed the validated path-consistency engine; and every baseline runs at **matched
single-relation coverage** over the **same** networks.

## Our method — Mode-A (closure-certified composition)

Iterated path-consistency closure (Mackworth **PC-2**) over the disjunctive local reads.
Mode-A *answers* a deduction-required query pair `(s,t)` **iff** closure narrows it to a
singleton (else it abstains; an empty-collapse is a **Mode-B** inconsistency certificate).
On the convex **point** algebra PC is **complete** (exact); on **Allen** (13 relations,
NP-hard consistency) it is sound but a **lower bound**.

## Baselines (all at matched coverage)

| method | kind | role |
|---|---|---|
| naive single-pass intersection | symbolic, free | iteration-isolation contrast (H3) |
| OFF (no composition floor) | symbolic, free | deduction-required gap (C2), coverage 0 |
| raw LLM (verbalized confidence) | full-document | completeness |
| chain-of-thought | full-document | completeness |
| self-consistency K=5 (vote margin) | full-document | **H1 gateway** |
| LINC-style multi-formalization vote | full-document | exploratory |
| **Path-of-Thoughts** (per-path independent) | full-document | **H1 gateway (primary)** |
| ILP-commit (Eirew M=5, transitivity ILP) | symbolic over M cheap reads | exploratory |

## Hypotheses / analyses

* **H1 (headline):** `selacc(Mode-A) − selacc(PoT) > 0` **AND** `… − selacc(SC) > 0` at
  matched coverage, paired-bootstrap, **Holm-Bonferroni** adjusted, on the bite-bearing pool.
* **H3 (iteration):** full PC − naive single-pass resolution gap vs **hop length** and
  **cyclomatic number**; predicted `0` at length-2, growing with hop≥3 / cycles. Reported on
  REAL reads and on a clean **gold-reads** reference that isolates the pure mechanism.
* **C2 (ON vs OFF):** Mode-A coverage = the deduction-required bite (OFF = 0).
* **Read-soundness / zero-FP audit:** per-edge recall, `J(E)`, within-doc soundness `ρ` (ICC),
  silent-wrong rate, and the zero-FP-conditional-on-soundness rate (≈1.0 by PC soundness).

## Key finding

The closure advantage over neural per-path reasoning **scales with relation-algebra
richness**. On the 3-relation point algebra a strong neural baseline (PoT) already composes
correctly → Mode-A **ties** PoT (while still beating self-consistency). On the 13-relation
Allen interval algebra neural per-path chaining collapses and Mode-A's symbolic closure
**dominates all baselines**. The H3 iteration theorem (full PC > naive on cyclomatic/hop≥3,
ties at length-2) is confirmed cleanly on the gold-reads reference.

## Files

* `method.py` — full pipeline (reads → QCN → Mode-A/naive/OFF/ILP → neural baselines →
  matched-coverage H1 → H3/C2/audit → schema-valid `method_out.json`).
* `engine.py`, `llm.py` — reused (verbatim + a per-call temperature/tag patch on `llm.py`)
  from iter-1 `gen_art_experiment_3`.
* `dataio.py` — loads/parses the synthetic backbone, maps each gold edge to its local
  sentence, **entity-normalizes** it (→ E1/E2) so identical reads share one SHA-256 cache
  slot, and parses native-vocab reads.
* `stats.py` — matched-coverage selective accuracy, paired bootstrap, Holm-Bonferroni,
  Page/Jonckheere/Spearman trend tests, ICC.
* `tests.py` — Stage-0 closure/wiring unit tests (zero spend).
* `method_out.json` (+ `mini_`/`preview_`) — schema-valid output (`exp_gen_sol_out`).
* `results/figures/` — H1 leaderboards + H3 hop/cyclomatic figures per algebra.
* `cache/` — SHA-256 disk cache of LLM responses (NOT a deliverable; excluded from upload).

## Reproduce

```bash
uv run method.py --folds test --n-point 90 --n-allen 90 --knob S4_sound   # full run
uv run method.py --mini                                                   # tiny smoke test
uv run tests.py                                                           # Stage-0 unit tests
```

Operating knob `S4_sound` frozen on the dev fold (per-edge recall 1.00 point / 0.965 Allen,
both clearing the pre-registered gates 0.90 / 0.85). Budget: hard cap **$9** OpenRouter
(per-call guard); the full run costs **≈ $3** thanks to entity-normalized read caching.
