# experiment_iter2_dir5 — LOCAL-reader real-text head-to-head + end-to-end Prolog

**The headline experiment of the Closure-Certified Text-to-Logic Deduction Module.**

Tests whether iterated path-consistency **closure** over span-**LOCAL** LLM reads of the
constituent path edges recovers deduction-required temporal relations that the local reads
alone cannot — beating Path-of-Thoughts, self-consistency, raw local LLM, and naive
single-pass at **matched coverage** (H1), and cutting the **confident-wrong (hallucination)
rate** versus a raw LLM (H2), on the **frozen ACTUAL NarrativeTime + TDDMan** gold graphs,
with a SWI-Prolog-discharged trace and a $0 fully-powered synthetic matched-coverage backstop.

## Method vs. baselines (same pipeline, same local reads, same coverage object)

| arm | what it does |
|---|---|
| **Mode-A (ours)** | PC-2 iterated closure (`engine.pc2_full`) over local path-edge reads; query edge **held out**; answers iff it narrows to one coarse relation, else ABSTAIN |
| naive | single-pass length-2 intersection (`engine.naive_single_pass`) — iteration contrast (ties Mode-A on length-2 by theorem) |
| raw | forced single relation from the query edge's **own** local read |
| Path-of-Thoughts | per-path LLM composition, modal vote, abstain on path disagreement — **no** cross-path intersection |
| self-consistency | majority over `SC_K` paraphrase samples of the query local read |

Closure runs in the **convex point start-point algebra** (PC-COMPLETE, exact). The five coarse
labels {before, after, simultaneous, includes, is_included} are exactly the five convex point
relations {`<`},{`>`},{`=`},{`<,=`},{`=,>`}; the universe {`<,=,>`} is no-commitment.

## Hypotheses (pre-registered, Holm-Bonferroni gatekept)
- **H1** (gateway): Mode-A selective accuracy at matched coverage > PoT **and** > SC (doc-clustered paired bootstrap, adjusted CI lo > 0).
- **H2** (gateway): Mode-A confident-wrong rate drops ≥ 0.05 abs vs raw on deduction-required queries (doc-clustered paired bootstrap, adjusted).

Two readers: **primary = google/gemini-3.1-flash-lite**; **stronger = google/gemini-3.5-flash**
(higher tier; the recall-gate test localizes whether read soundness — not closure — is the bottleneck).

Every number is TAGGED `REAL-LLM-READ` / `SYNTHETIC-CHANNEL` / `GOLD-ONLY-GATE` / `THEOREM`.

## Files
- `method.py` — orchestration (NEW): local reads, matched-coverage risk-coverage, H1/H2, Prolog discharge, verdict.
- `data_adapter.py` — NEW: reads the frozen `gen_art_dataset_1/full_data_out.json`, char-offset event marking, deduction-required multi-path query sampling.
- `engine.py`, `llm.py`, `tests.py`, `corpora.py` — REUSED verbatim from the iter-1 frontier pilot (closure engine, OpenRouter client w/ disk cache + cost guard, blocking closure tests, coarse maps).
- `synth_channel.py` — synthetic point-algebra channel + generators (verbatim from iter-1 exp-2) + NEW matched-coverage harness (recall 0.96, $0 backstop).
- `method_out.json` (+ `mini_`/`preview_`) — schema-valid (`exp_gen_sol_out`) results.
- `results/worked_modeA.pl`, `results/worked_collapse.pl` — runnable Prolog trace programs.
- `results/figures/*.jpg` — risk-coverage + synthetic matched-coverage figures.

## Run
```bash
uv run python method.py --n-target 300 --concurrency 16   # full (hard global cap $9 < $10)
uv run python method.py --mini                            # tiny smoke (cached -> $0 reruns)
```
Disk cache makes reruns $0. A GLOBAL budget cap is enforced across all three OpenRouter clients.

## Honest verdict policy
`CONFIRM` (both gateways) / `PARTIAL/SCOPE-BOUNDARY` (one) / `DISCONFIRM/SCOPE-BOUNDARY` (neither →
negative-localization: local reads + even the stronger reader at/below the recall gate ⇒ the
bottleneck is real-text local read soundness, not closure; the synthetic mechanism win carries the
matched-coverage claim, retargeted to NeSy/findings).
