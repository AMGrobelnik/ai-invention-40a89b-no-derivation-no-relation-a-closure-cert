# Closure-Certified Text-to-Logic — iter-3 powered real-text head-to-head

Powers the iter-2 headline experiment AT SCALE (n=20 smoke -> **600** deduction-required
queries) on the FROZEN NarrativeTime + TDDMan gold graphs, resolves read-soundness per
corpus, and ACTUALLY discharges the worked programs with SWI-Prolog.

## Method vs. baselines (same pipeline, same span-LOCAL reads, same coverage object)
| arm | what it does |
|---|---|
| **Mode-A (ours)** | PC-2 iterated closure (`engine.pc2_full`) over local path-edge reads; query edge **held out**; answers iff narrows to one coarse relation, else ABSTAIN |
| naive | single-pass length-2 intersection — iteration contrast |
| raw | forced single relation from the query edge's own local read |
| Path-of-Thoughts | per-path LLM composition, modal vote, **no** cross-path intersection |
| self-consistency | majority over k=5 paraphrase samples |

Closure runs in the convex point start-point algebra (PC-COMPLETE, exact).

## Result (VERDICT = CONFIRM, n=600, powered)
- **H1** (Holm-gateway): Mode-A selective acc at matched coverage > PoT (gap +0.027, p=0.007) **and** > SC (gap +0.035, p=0.018).
- **H2** (Holm-gateway): confident-wrong 0.425 vs raw 0.61 -> reduction **0.185** (CI [0.086,0.282], p~0), reported AT 18.8% Mode-A coverage (81.2% abstain) vs raw 100% — the FAIR metric is H1.
- **Read-soundness reconciliation** vs the 0.90 gate (clustered-bootstrap CI = primary): NT primary 0.856 (excl-below), NT strong **0.932** (contains gate, crosses point-estimate), TDDMan primary 0.828 / strong 0.819 (both excl-below). Gate-crossing is **corpus/genre-specific**, not universal.
- Readers: primary `google/gemini-3.1-flash-lite` (95%; 5% deepseek-v3.2 rate-limit fallback), stronger `deepseek/deepseek-v4-pro` (100%). Parse-failed reads EXCLUDED from recall.
- **SWI-Prolog 9.0.4 executed**: `worked_modeA.pl` -> `ANSWER(lt)` (agrees engine, gold=before); `worked_collapse.pl` -> inconsistent-triangle Mode-B certificate (`comp(gt,gt)=gt but rel=lt`).
- Synthetic backstop (recall 0.96, $0): mean Mode-A gap vs raw +0.225 (mechanism intact). MATRES gate validates (0 deduction queries).

## Run
```bash
uv run python method.py --n-target 300 --concurrency 16   # full (hard global cap $9)
uv run python method.py --n-target 80                     # checkpoint
uv run python method.py --mini                            # smoke
```
Disk cache (keyed by model+temperature+max_tokens) makes reruns $0. Realized spend ~$2.4.

## Files
- `method.py` — orchestration (iter-3 edits A–E + Prolog strengthening + parse-fail recall fix).
- `engine.py` `llm.py` `data_adapter.py` `corpora.py` `synth_channel.py` `tests.py` — reused.
- `method_out.json` (+ `full_`/`mini_`/`preview_`) — schema-valid (`exp_gen_sol_out`).
- `results/worked_*.pl` — runnable, swipl-discharged trace programs.
- `results/figures/{real_risk_coverage,synthetic_matched_coverage,h2_risk_coverage}.jpg`.

Every number is tagged REAL-LLM-READ / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / THEOREM.
