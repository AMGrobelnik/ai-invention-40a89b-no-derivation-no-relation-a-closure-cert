# Minimal LLM fuzzy-unification (composition-cell gap-filling) — EXPLORATORY

This experiment substantiates the neuro-symbolic **"fuzzy unification"** framing (project goal +
reviewer MAJOR #3) **without overclaiming** OpenCyc grounding or general fuzzy unification. It asks
one sharp, falsifiable question:

> When a **sound symbolic closure engine abstains** because a composition-table cell is **missing**
> (no path) or **ambiguous** (conflicting derivations), can a minimal probabilistic LLM read
> **fill/resolve that cell** and add **net faithful coverage** — recovering answers the symbolic
> engine could not give — **without** a confident-wrong (silent-wrong-narrowing) hallucination cost
> that swamps the gain?

**Scope (stated honestly):** this is composition-**CELL** gap-filling (a missing/ambiguous cell of an
*exact* qualitative or kinship composition table, filled by a probabilistic LLM read). It is **NOT**
OpenCyc/upper-ontology grounding and **NOT** general fuzzy unification — both are out of scope.

The reader LLM is `google/gemini-3.1-flash-lite` (temp 0, sha256 disk-cached, $9 hard cap). Total real
API spend to build the cache: **$0.28** (1797 calls); cached re-runs are **$0**.

---

## The three settings

### Setting 1a — clean LLM composition-cell accuracy vs algebra richness *(primary synthetic)*
Query the LLM on **every** base×base composition cell of convex **Point** (3), **RCC-8** (8) and
**Allen** (13) — whose true cell is known from the authoritative `qualreas` algebra tables — and score
the LLM **exactly** vs the withheld true cell. The same machinery scores the 16 **CLUTRR kinship**
cells (a 4th, finite calculus).

**Result (exact-match / soundness):** point **0.67 / 0.78** → rcc8 **0.52 / 0.78** → allen **0.38 / 0.44**.
Quality **degrades monotonically with richness**, and on Allen the LLM is *un-sound* 56% of the time
(it drops feasible relations = the silent-wrong-narrowing hazard). By contrast the LLM knows the
**kinship** calculus perfectly (**1.00**) — common-sense calculi are where its implicit knowledge shines.

### Setting 1b — end-to-end synthetic gap-fill *(secondary, $0 extra)*
Reuse the cached per-cell predictions as an alternative table. Ablate K% of cells, recompose the
held-out query along the dataset's enumerated paths, intersect, and measure coverage **recovered** by
LLM-filling vs the abstain (gap=universe) baseline and the added confident-wrong cost. Path-recompose
sanity-check vs the dataset's own gold compositions = **100%** (point 760/760, allen 631/631, rcc8 485/485).

**Result:** recovered precision tracks richness and ablation. Point/RCC-8 = **1.0** precision, 0
hallucination at every K. Allen degrades **0.52 → 0.45 → 0.30** (and confident-wrong rises
**0.02 → 0.06 → 0.17**) as K = 0.10 → 0.20 → 0.30.

### Setting 2 — HEADLINE end-to-end demo on CLUTRR kinship
Under a consistently **ablated** kinship table (headline K = 0.20, converse-closed → 5 cells removed),
solvable test queries that need an ablated cell become **manufactured gaps** (clean gold, n = 391).
Separately, the documented **inv-child vs inv-in-law** cells are **natural conflict gaps** (n = 244,
genuinely ambiguous under the *full* table). The symbolic engine on the ablated mixed pool is
**provably hallucination-safe**: for a solvable query D_full = {gold}, ablation only removes rules, so
D_abl ⊆ {gold} → it returns gold or abstains, **never a wrong singleton** (verified: 0 confident-wrong).

**Two gap-fill modes** (both cached):
- **Mode P** (table-level): fill the missing *atomic* composition cell with the LLM's abstract
  composition (`son` of `son` = `grandson`…), then let the **symbolic engine do the multi-hop chaining**.
- **Mode S** (story-level): give the LLM the story + the symbolic candidate set and ask it to do the
  multi-hop read directly.

**Two baselines** on the *same* mixed pool:
- **symbolic-abstain** — pure closure (never hallucinates, zero coverage on gaps);
- **raw_llm CoT** — pure-neural: read the story, answer every query directly.

**Result (mixed pool = 663; full coverage):**

| method | coverage | acc. among answered | **confident-wrong (hallucination)** |
|---|---|---|---|
| symbolic-only | 0.47 | 1.00 | 0.000 |
| **Mode-P (cell-fill, neuro-symbolic)** | **1.00** | **1.00** | **0.000** |
| Mode-S (story-fill, neuro-symbolic) | 0.99 | 0.65 | 0.343 |
| raw LLM CoT (pure neural) | 1.00 | 0.54 | 0.522 |

- **Mode-P recovers 100% of gaps at precision 1.00 (net +391), cutting the hallucination rate
  100% (0.522 → 0.000) vs raw LLM at FULL coverage** — it extends the symbolic engine's perfect
  accuracy to full coverage.
- **Honest negative:** naive **story-level** filling is **NOT net-faithful** — Mode-S recovers gaps at
  only 0.33 precision (net −133), because asking the weak LLM to do the multi-hop read inherits its
  chain errors. This quantifies *why* the neuro-symbolic division of labour matters: the LLM should
  fill only the **atomic rule**, not do the reasoning.
- **Scope boundary:** the method's success is *conditional* on the LLM knowing the calculus —
  decisive on kinship (Setting 2), unsafe on abstract Allen (Setting 1b, 0.30 precision).
- **Natural-conflict arm (n = 244):** both Mode-S and raw struggle on genuine ambiguity; Mode-S
  (symbolic-candidate-narrowed) marginally beats raw.

**Auditable trace-graphs:** every composition step is tagged `exact_table` vs `llm_fuzzy` (with the
LLM's confidence and whether it matched the true cell). Manufactured traces show the single filled
cell inside an otherwise-exact chain; natural traces show the exact-table conflict + one LLM
disambiguation step — including one honest failure (mother vs mother-in-law).

---

## Files

| file | description |
|---|---|
| `method.py` | the full experiment (Settings 1a/1b/2 + both baselines) |
| `figures.py` | paper figures from `method_out.json` |
| `method_out.json` | **deliverable** — aii `exp_gen_sol_out` schema (validated) |
| `mini_method_out.json` / `preview_method_out.json` | size-reduced variants |
| `results/fig_*.png` | richness curve, risk-coverage, hallucination bar, recovered precision |
| `kinship.py` `llm.py` `stats.py` `dataio.py` `qcn/` | reused from sibling artifacts |
| `cache/` | sha256 LLM cache (excluded from upload; makes re-runs $0) |

`metadata` in `method_out.json` carries every block: `composition_accuracy_by_algebra`,
`composition_accuracy_by_true_cell_size`, `composition_richness_curve`, `end_to_end_synthetic_gapfill`,
`clutrr_gap_pool_counts`, `clutrr_gapfill_risk_coverage`, `clutrr_manufactured_K_sweep`,
`clutrr_gapfill_mixed_pool_curve`, `clutrr_full_coverage_point`, `clutrr_hallucination_reduction`,
`llm_resolved_step_accuracy` (Mode-P cells + Mode-S manufactured/natural arms), `bootstrap_cis`
(doc-clustered), `flagged_fuzzy_step_traces`, `honesty_caveats`, `budget`, `verdict`.

Two datasets: `synthetic_composition_cells` (242 cells, `predict_llm`) and `clutrr_gapfill`
(663 queries, `predict_symbolic` / `predict_gapfill_P` / `predict_gapfill_S` / `predict_raw_llm`).

---

## Reproduce

```bash
uv venv .venv --python=3.12
uv pip install --python=.venv/bin/python numpy==2.4.6 scipy==1.17.1 matplotlib==3.11.0 \
    httpx==0.28.1 loguru==0.7.3 jsonschema==4.26.0
export OPENROUTER_API_KEY=...                      # only needed for a cold cache
.venv/bin/python method.py --cap-per-hop 80 --n-normal 350 --modeS-cap 244 --s1b-per-alg 500
.venv/bin/python figures.py
```

Flags: `--no-llm` (symbolic-only validation, $0), `--mini` (3-row smoke), `--smoke-cells N`
(query only N composition cells). The disk cache means a warm re-run is deterministic and free.

## Honesty caveats
- CLUTRR is a **templated** kinship benchmark (max 871 chars), not natural text.
- Gaps are composition **cells**, not ontology/common-sense grounding.
- Manufactured gaps are clearly labelled and separated from natural gaps.
- A non-sound LLM fill is the silent-wrong-narrowing failure mode → reported as confident-wrong.
- Mode-S and raw_llm see the same story; the neuro-symbolic system invokes the LLM **only on gap
  cells** and uses the exact table everywhere else.
