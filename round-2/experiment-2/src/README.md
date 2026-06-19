# Realism-Matched Synthetic Channel (experiment_iter2_dir4)

Zero-LLM-spend CPU experiment that **repairs the iter-1 synthetic channel** and
re-establishes the three mechanism results of the closure-certified text→logic
module under a reader channel **calibrated to the iter-1 real-text frontier pilot**.

## The core fix
iter-1 (`gen_art_experiment_2`) had two breaches: per-edge error-type
TV = 0.25 (vs pre-registered ≤ 0.10), and a **dead breadth knob** (per-edge recall
stuck at 0.958 across S1–S5 because recall and breadth were independent inputs).

Here the channel is a **single ordinal knob S1–S5** whose per-edge error-type
distribution is *sampled directly from the calibrated real distribution*, so
`recall = 1 − P(unsound | knob)` is an **output** and the knob genuinely trades
recall for bite. Calibration target = `gen_art_experiment_3`
`metadata.frontier_table`, arm `TBDense_dense` (NarrativeTime stand-in, ALLEN),
secondary `TDDMan_noncirc`.

## Results (full scale: N=600/cell, B=2000)
| claim | verdict | key numbers |
|---|---|---|
| recall ladder reproduced (dead-knob fixed) | ✅ | real [.572,.599,.625,.783,.796] vs sim [.572,.602,.623,.783,.796], max err 0.003 |
| per-edge error-type TV (point, apples-to-apples projection) | ✅ | max 0.0065 ≪ 0.10 (naive 5-cat = 0.19 ⇒ point-algebra representability gap) |
| ALLEN direct 5-category TV (same-algebra) | ✅ | max 0.0072 ≪ 0.10 |
| cross-edge ρ (J2 reproduced at measured ICC) | ✅ | max J2 residual 0.073 ≤ 0.10 (J2/J3 internally inconsistent ⇒ Fallback B) |
| topology TV (cyclo + short-range E≤6) | ✅ | TV_cyclo 0.14, TV_E(≤6) 0.13 ≤ 0.15 (full TV_E 0.24 = long-hop tail, descriptive) |
| **H3** iteration gap per recall slice | ✅ | tie at L=2 (CI∋0), grows with L & cyclomatic; **Page p ≈ 5e-4** (not 1e-13) |
| H3 recall-dependence | — | maxL gap 0.21→0.90 as recall 0.57→1.0 (predicted ~0.63 @0.9; got 0.647) |
| **H4** recall-dependent inverted-U | ✅ | interior peak at recall ≤0.78, peak shifts outward (3 bins), beats single/off |
| H4(e) J(E) > rᴱ under ρ>0 | ✅ | frac 1.0 at low recall, mean centroid shift +1.04 |
| **silent-wrong vs recall** | ✅ | monotone-decreasing, ≤ per-network bound 1−J(E) (rigorous); E2 stratum ≤ 1−recall |
| **zero-FP THEOREM** (separated) | ✅ | all-sound ⇒ gold in output P=1.0; collapse never with all-sound |
| C3 reliability | — | contains-gold slope on J(E)=0.65 (<1, point-algebra absorption ⇒ over-delivers); offset disappears under J(E) |

`realism_matched = True`; `evidence_tag = SYNTHETIC-CHANNEL`; the zero-FP theorem
is tagged `THEOREM`, the silent-wrong curve `EMPIRICAL/SYNTHETIC-CHANNEL`.

## Files
- `method.py` — self-contained pipeline (calibrated channel, H3/H4/silent-wrong,
  zero-FP theorem, realism block, Allen direct-match arm). `--scale smoke|mini|test|full`.
- `allen_arm.py` — Allen-13 algebra (table derived from 6-point closure, self-verified).
- `method_out.json` — full-scale results (schema `exp_gen_sol_out`, validated). `mini_`/`preview_` variants alongside.
- `figures/` — fig1 H3 gap vs L per recall; fig2 H4 inverted-U + channel decomposition;
  fig3 J(E) vs rᴱ; fig4 silent-wrong vs recall with bound overlays; fig5 realism error-type bars.
- `logs/` — run logs.

## Reproduce
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python numpy scipy matplotlib
.venv/bin/python method.py --scale full   # ~140 s on 4 CPUs, zero network/LLM
```

## Honest caveats
- POINT algebra cannot represent the ALLEN "loose" category; the per-edge TV is therefore
  computed in the apples-to-apples **projected** ladder {singleton,pair,universal,unsound}
  (loose+universal→universal), and the **ALLEN arm** matches all 5 categories directly.
- Real J2/J3 are internally inconsistent with any single exchangeable copula on some knobs
  (J2>p² but J3<p³, small-sample); we calibrate ρ to the robust directly-measured ICC and
  report J(E) vs rᴱ descriptively (Fallback B).
- Full topology TV_E = 0.24 is driven by the long-hop tail (E_min>6) outside the synthetic
  generator's hop range; the frontier pilot actually evaluated E=2 deduction triangles, which
  the synthetic backbone matches (short-range TV_E 0.13). Tail reported descriptively (Fallback C).
