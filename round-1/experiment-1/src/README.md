# T0 A-Priori Envelope Gate + Reusable QCN Path-Consistency Engine

**Zero-LLM-spend, CPU-only.** This artifact decides — *from gold temporal graphs alone, before any
LLM budget is spent* — whether a real-text headline exists for the "closure certificate" hypothesis,
and on which corpus. It also ships a reusable, unit-validated **Qualitative Constraint Network (QCN)
path-consistency engine** (Allen-13, convex linear point, RCC-8) for later tiers.

## What it does

A temporal-relation *closure certificate* runs iterated path-consistency (PC) over the relations a
reader extracts and (a) detects contradictions and (b) tightens under-specified relations by
propagation. This gate measures, on **gold** graphs, where that certificate could possibly help:

For every held-out gold edge `(u,v)` we run a funnel:

1. **evaluable** — gold singleton, both endpoints have ≥1 other gold edge.
2. **(i) deduction-required** — `u,v` are not in the same/adjacent sentence (needs synthesis).
3. **(ii) multi-path** — ≥2 distinct length-2 intermediates, or ≥1 + a ≥3-edge/cyclic path.
4. **(iii) bite** — the closure stays sub-universal after widening non-convex inputs.
5. **(iv) N\*** — full iterated PC recovers the exact gold relation.

**Method vs baseline (same pipeline):**
`predict_our_method_full_pc` = FULL iterated PC-2 closure;
`predict_baseline_naive_singlepass` = single pass of length-2 intersections (Path-of-Thoughts-style);
`predict_baseline_closure_off` = no propagation (universe). The **iteration advantage**
(`full_only`) counts edges full PC resolves that single-pass cannot (≥3-edge/cyclic chains).

## Corpora (gold, no LLM)

| corpus | algebra | role | source |
|---|---|---|---|
| **MATRES** | convex point (start) | N\*≈0 **control** (all same/adjacent-sentence) | CogComp + qiangning EMNLP-19 (SENTDIFF) |
| **TDDMan** | Allen-13 | non-circular **iteration** arm (manual, all long-distance) | TDDiscourse |
| **NarrativeTime** | convex point (start) + Allen interval | dense **applicability** headline | text-machine-lab/narrative_time |

Convex point PC is **exact** (verified complete vs brute-force); the Allen arm is a sound **lower
bound** (PC incomplete on the interval algebra).

## Headline results (full run)

- **MATRES (control):** 100% of pairs are same/adjacent sentence → **0** deduction-required edges →
  **N\*=0**, exactly as predicted. Makes the gate *discriminative*.
- **NarrativeTime (applicability):** the certificate applies to **88.3%** of deduction-required
  evaluable edges and recovers them **exactly** (N\*=25,450). Because the human timeline is dense
  (near-transitively-closed), single-pass already has direct evidence, so iterated PC **ties**
  single-pass here (`full_only=0`). True-N MDE₈₀ = 0.05.
- **TDDMan (iteration):** module-band applicability (**8.5%** strict / 10.4% broad map); full PC
  recovers **12** held-out relations single-pass cannot (genuine ≥3-edge/cyclic advantage); N\*=408.
  MDE₈₀ = 0.10.
- **Gate verdict: GO** — host the real-text headline on NarrativeTime (applicability ≥10%, MDE₈₀ ≤
  pre-registered 0.10); TDDMan is the non-circular corroboration arm; MATRES is the control. Iter-2
  may spend LLM budget on the real-text comparison.

All numbers, the funnel per corpus, power/MDE, the engine validation report, and per-query
method/baseline predictions are in `method_out.json` (`metadata.headline_findings` for the summary).

## Files

- `engine.py` — reusable Algebra / QCN / `pc2_full` (FULL) / `naive_single_pass` (BASELINE) /
  `closure_off`. Bitmask-encoded relation sets; tables loaded from `algebras/` (qualreas).
- `tests.py` — engine unit-test battery (gates everything): Allen 169-cell validation, convex-point
  completeness vs brute-force, consistency detection, iteration isolation.
- `parsers.py` — corpus parsers → per-doc gold graphs, cached to `cache/`.
- `method.py` — Stage 0 tests → Stage 1 parse → Stage 2 funnel → Stage 3 power → Stage 4 hosting.
- `algebras/` — Allen-13, convex point, RCC-8 tables (from github.com/alreich/qualreas).
- `cache/` — parsed gold graphs, checkpointed for reuse by iter-2 Tier-1.
- `method_out.json` — the deliverable (validated against `exp_gen_sol_out`).

## Reproduce

```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python numpy scipy pandas networkx requests lxml loguru
# corpora (excluded from the repo; re-clone into ./data/):
#   github.com/alreich/qualreas  github.com/aakanksha19/TDDiscourse  github.com/CogComp/MATRES
#   github.com/text-machine-lab/narrative_time  github.com/qiangning/NeuralTemporalRelation-EMNLP19
.venv/bin/python method.py            # ~60s, $0
```
