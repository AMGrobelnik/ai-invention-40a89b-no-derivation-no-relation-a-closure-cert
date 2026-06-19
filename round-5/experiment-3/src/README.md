# Operational ~3000-char end-to-end case study

**text → span-local atomic read → QCN closure → runnable SWI-Prolog trace-graph → quantified hallucination reduction**

The FIRST end-to-end run of the full closure-certified text-to-logic deduction pipeline on
real **~3000-character professional documents** (retires reviewer MINOR #4). Framed
throughout as an **operational case study on a handful of documents — NOT a powered
statistical comparison**. Every number carries its coverage/abstention beside it.

## Two arms (reported per-document)

| Arm | Document | Algebra | Role |
|-----|----------|---------|------|
| **TEMPORAL (primary)** | the 5 NarrativeTime news articles closest to ~3000 chars (mean 3050; range 2197–4293) | convex **POINT** start-point (PC-complete; avoids the Allen near-universe trap) | real professional text; faithfulness-by-abstention |
| **KINSHIP (contrast)** | a ~3000-char document built by concatenating disjoint-entity CLUTRR sub-stories (3 docs, 3246–3602 chars) | finite kinship composition table (forward-union least fixpoint) | calculus memorized → pipeline works FULLY; isolates that the ceiling is **extraction-limited, not closure-limited**; yields genuine cross-story **absent-relation** pairs |

For each document the executor: (1) extracts atomic relational predicates span-locally with
`google/gemini-3.1-flash-lite` (temp 0, SHA-256 cache, hard $9 guard) and reports atomic
P/R; (2) builds the QCN and runs PC-2 / forward-union closure, emitting per held-out query
a **singleton (emit) / non-singleton (abstain) / empty (Mode-B unsound certificate)**;
(3) **discharges the closed network as a runnable SWI-Prolog program and EXECUTES it**
(`swipl` subprocess), reporting engine-match + gold-match truthfully + a human-auditable
trace-graph; (4) measures the **quantified confident-wrong (hallucination) reduction** of
the certified pipeline vs a raw LLM — both a span-local raw and a **whole-document raw
generation** baseline — AS a risk-coverage tradeoff with coverage/abstention beside every
number.

## Headline results (descriptive; see `metadata.case_study_summary`)

**Temporal (5 docs, 150 deduction queries):** atomic disjunctive-set recall 0.77–0.92
(mean 0.87, broad reads), most-likely precision 0.36–0.56; 22 emit / 126 abstain / 2
Mode-B collapse. **Hallucination reduction vs whole-document raw: 0.27–0.60 (mean 0.45)**,
with coverage_modeA 0.0–0.33 and coverage_raw = 1.0 (the raw LLM always commits and is
frequently wrong; the certified pipeline abstains where local reads under-determine →
faithfulness-by-abstention, 0–0.17 confident-wrong).

**Kinship (3 docs ~3000 chars):** atomic recall 0.39–0.56 (mean 0.49, **the extraction
bottleneck**), precision 0.38–0.60. Within-story multi-hop: 8 emit, 6 correct (selective
accuracy 0.75 — the misses are extraction-limited, not closure-limited). **Absent-relation
pairs: 56/56 abstained, 0 confident-wrong BY CONSTRUCTION** (disjoint components → empty
derivation set → Mode-A never invents a kinship).

**Prolog execution:** 95 programs discharged AND executed in SWI-Prolog 9.0.4 (60 temporal
+ 35 kinship). The kinship discharge uses a **forward-closure least-fixpoint** program
(`prolog_kinship.py`) that reproduces the certified engine exactly — **engine-match 35/35**,
gold-match 24/35 (the rest are correct abstentions on absent pairs / extraction-limited
misses). 4 worked trace-graphs (temporal narrowing, temporal faithful-abstain, kinship
multi-hop derivation, kinship absent-abstain) ship with runnable `.pl` paths + swipl stdout.

## Honesty commitments (see `metadata.honesty_commitments`)

- Sub-module scope only: the contribution is the closure **certificate** + abstain-on-collapse
  output contract. Atomic extraction is **MEASURED, not improved**; OpenCyc grounding and
  LLM fuzzy-unification are out of scope here.
- NarrativeTime has **no single article in [2500,3500] chars** (docs cluster <2500 or >4200);
  we BRACKET the target so the selected set's **mean** length is ~3000 (each exact length is
  reported). The point start-point projection is tighter than Allen but cannot express
  includes/is_included as singletons → some queries are structurally extraction-limited.
- CLUTRR stories are short; the ~3000-char kinship document is **concatenated** from
  disjoint-entity sub-stories (labelled), giving genuine within-document absent pairs.
- SWI-Prolog execution is reported truthfully per query (executed / engine-match / gold-match;
  python fallback is labelled and never implies execution).

## Files

- `method.py` — the driver (NEW: doc-selection-by-length, CLUTRR concat builder,
  most-likely precision, `run_pot`/`run_sc`/`run_full_doc_raw_temporal`, per-document
  reporting, trace-graph/output assembler).
- `prolog_kinship.py` — NEW forward-closure fixpoint discharge (reproduces the engine).
- `temporal_core.py` — iter-2 `method.py` verbatim (temporal helpers reused unchanged).
- `engine.py`, `corpora.py`, `data_adapter.py`, `synth_channel.py`, `tests.py` — iter-2 temporal modules.
- `kinship.py`, `prolog.py`, `readers.py`, `dataio.py`, `stats.py`, `baselines.py`,
  `figures.py`, `tests_kinship.py` — iter-3 CLUTRR modules. `llm.py` — iter-3 OpenRouter
  client (per-item `max_tokens`/`temperature`/`tag` overrides; SHA-256 cache; hard cost guard).
- `gate.py`, `probe.py` — $0 validation / data-inspection scripts.
- `method_out.json` (+ `full_`/`mini_`/`preview_`) — output (schema `exp_gen_sol_out`).
- `pl/` — runnable SWI-Prolog programs emitted per discharged query.

## Reproduce

```bash
uv venv .venv --python=3.12 && source .venv/bin/activate
uv pip install httpx loguru numpy scipy matplotlib jsonschema
apt-get install -y swi-prolog            # SWI-Prolog 9.0.4 used here
OPENROUTER_API_KEY=... .venv/bin/python method.py            # full run (~$0.3 cold cache, ~7 min)
.venv/bin/python method.py --mini                            # 1 temporal + 1 kinship smoke
.venv/bin/python gate.py                                     # $0 blocking-gate validation
```

Cost is gated hard at $9 (split 6.5/2.5 across the temp-0 and temp-0.7 clients); a warm-cache
rerun is ~$0.02. The cold-cache full run billed ~$0.31.
