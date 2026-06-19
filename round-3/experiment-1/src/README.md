# CLUTRR end-to-end kinship closure-certificate pipeline

A single neuro-symbolic run on **real (non-synthetic, non-temporal) text** that delivers,
in one venue, the four numbers the closure-certificate umbrella names:

1. **atomic-extraction precision / recall / F1** of directly-stated facts from the document;
2. **multi-hop deduction accuracy at MATCHED COVERAGE** vs purely-neural baselines, and
   **accuracy vs chain length** (hops 2..10);
3. a **human-auditable trace-graph ACTUALLY discharged in SWI-Prolog**;
4. a **quantified hallucination-rate reduction** on absent-relation queries, reported as a
   full **risk-coverage curve** with abstention stated.

The neural half is an LLM (`google/gemini-3.1-flash-lite`) acting as a *semantic translation
engine* that reads atomic kinship triples from the de-bracketed CLUTRR story. The symbolic
half is a finite-composition-table **closure engine** that recovers the held-out query
relation and emits a certificate (Mode-A: emit iff a unique derivation exists, else abstain).

## Pipeline

```
story --LLM extraction--> atomic kinship triples --forward-closure--> query relation + Prolog proof
                              (precision/recall)        (Mode-A / naive)      (SWI-Prolog discharge)
```

* **`dataio.py`** — loads the PREPARED gold graphs (dependency `art_HS7-lxhZnU9m`,
  `clutrr_gen` 16,131 / `clutrr_disc` 10,545); the decisive `gold_atomic_check` go/no-go.
* **`kinship.py`** — the closure engine. CLUTRR's table is a **finite composition table, NOT
  a relation algebra**; the sound closure is a **forward least-fixpoint UNION derivation over
  defined compositions** (a converse-intersection PC-2 port is *unsound* here and collapses
  ~13 % of gold-clean chains). Output contract: `|D[query]|==1` → emit; `>1` → abstain
  (Mode-B conflict); `==0` → abstain (no path = absent-relation, hallucination-safe).
* **`readers.py`** — LLM atomic-extraction prompt + the learned-composition baselines
  (raw forced-single, self-consistency vote, Path-of-Thoughts per-path composition).
* **`baselines.py`** — symbolic predictions, atomic P/R, matched-coverage selective accuracy,
  doc-clustered paired bootstrap, accuracy-vs-hop, risk-coverage, the H2 operating point.
* **`prolog.py`** — emits `comp/3`,`conv/2`,`rel/3`,`solve_/4`; discharges in real SWI-Prolog
  (pyswip / subprocess), with an honest `python-checked` fallback; cross-checks vs the engine.
* **`method.py`** — orchestrator (CLI `--mini` / `--scale` / `--reader` / `--sc-k` / ...).
* **`stats.py` / `llm.py` / `engine.py`** — reused VERBATIM from the iter-2 experiment
  (matched-coverage stats; sha256-cached, hard-$9-capped async OpenRouter client; the
  temporal PC-2 engine kept as a sanity reference).
* **`figures.py`** — accuracy/coverage-vs-hop, risk-coverage, matched-coverage bar.
* **`tests.py`** — 0-LLM unit tests gating every LLM spend (DECISIVE soundness gate).

## Baselines (all thresholded to the SAME matched-coverage object)

| method | description |
|---|---|
| **Mode-A (ours)** | LLM extraction → forward-closure; emit iff unique derivation, else abstain |
| naive single-pass | one composition step at the query edge (no fixpoint) → resolves hop-2, abstains hop≥3 |
| raw LLM | forced single-relation answer + verbalized confidence (the hallucination reference) |
| self-consistency | k=5 samples, modal vote, vote-margin confidence |
| Path-of-Thoughts | per-path independent composition over the entity chain, path-agreement confidence |
| off | table-fixed, no composition (C2 anchor: 0 coverage on deduction-required queries) |
| Mode-A (gold-read) | oracle upper bound on GOLD atomics — isolates extraction as the bottleneck |

## Key engineering finding

The decisive go/no-go (`tests.py`): closing every story from its **gold** atomic facts,
Mode-A recovers the gold query with **100 % accuracy on every emitted answer** (soundness)
and ~98.5 % singleton-rate on clean rows. The ~1.5 % abstentions are a *genuine* table
ambiguity (`inv-child` vs `inv-in-law`: the same surface chain `husband-son-grandmother`
yields gold `mother` for one story and `mother-in-law` for another — the finite table
provably cannot disambiguate), so Mode-A abstains rather than guess. This is the
hallucination-safe contract, validated before any LLM call.

## Reproduce

```bash
uv run tests.py --full              # 0-LLM unit tests (soundness gate)
uv run method.py --mini             # end-to-end smoke (~$0.01)
uv run method.py                    # full subsample (gen test 1048 + disc test 445), <$2, ~35 min
uv run method.py --reader deepseek/deepseek-v3.2   # cross-family sensitivity
```

Output: `method_out.json` (`exp_gen_sol_out` schema) with per-query `predict_*` + gold,
the atomic-P/R / matched-coverage / accuracy-vs-hop / risk-coverage tables, the Holm family,
the SWI-Prolog execution log, a worked 3-entity example, and an explicit CONFIRM /
SCOPE-BOUNDARY verdict. Figures in `results/`.

## Honest caveats

* **Story length.** CLUTRR stories are short (max 871 chars); **none** reach the umbrella's
  ~3000-char target. CLUTRR delivers the goal *numbers* on clean non-synthetic non-temporal
  text; ~3000-char documents live only in the temporal corpora (iter-1/2).
* **Entity grounding** (which surface string is which person, and gender) is taken from gold
  for the final surface realization — entity grounding is **not** the contribution; the LLM
  read of atomic relations + the closure certificate are.
* CLUTRR is research/non-commercial (CC-BY-NC-style; `facebookresearch/clutrr` LICENSE).

_Headline results are written into `method_out.json:metadata.verdict` by the run._
