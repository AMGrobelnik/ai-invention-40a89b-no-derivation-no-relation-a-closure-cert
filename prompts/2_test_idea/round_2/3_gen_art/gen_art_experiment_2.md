# gen_art_experiment_2 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_2` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 15:38:05 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_2_idx4
type: experiment
title: >-
  Realism-Matched Synthetic Channel: Re-establish H3 (per-recall-slice iteration gap), H4 (recall-dependent inverted-U), and
  the Silent-Wrong-vs-Recall curve under a TV-calibrated breadth knob
summary: >-
  Repair the iter-1 synthetic-channel realism breach (measured per-edge error-type TV=0.25 vs pre-registered <=0.10) and the
  dead breadth knob (identical recall 0.958 across S1-S5) by RE-CALIBRATING the simulated reader so its per-edge error-type
  distribution matches the iter-1 real-text frontier-pilot distributions to TV<=0.10, with a SINGLE ordinal breadth knob that
  genuinely trades per-edge recall for bite. Then re-run H3 (FULL minus NAIVE iteration gap stratified by hop-count and cyclomatic
  number, reported AT EACH FIXED RECALL SLICE with the correctly-computed Page trend p, NOT the paper's mis-stated 1e-13),
  H4 (decompose net Mode-A gain into benefit and silent-narrowing-cost 1-J(E) vs redundancy at >=4 fixed recall levels, locate
  the inverted-U peak, verify outward movement with recall and under the recall-floor gate, confirm positive rho makes J(E)
  exceed r^E), and a NEW silent-wrong-vs-recall curve with the per-edge (1-recall) and per-network (1-J(E)) bounds. Everything
  is tagged SYNTHETIC-CHANNEL; the zero-FP soundness THEOREM (all-sound => gold-in-output, prob 1.0) is reported separately
  from the empirical silent-wrong findings. Build directly on iter-1 experiment_2/method.py (self-contained convex-point-algebra
  QCN generator + simulated channel + FULL/NAIVE/OFF closure + bootstrap/Page/Jonckheere stats); zero LLM spend (pure simulation).
  Emit aii-json-validated method_out.json with achieved realism statistics, per-recall-slice gap curves, decomposed inverted-U,
  silent-wrong-vs-recall curve, and PASS/FAIL flags.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # ==================================================================== #
  # ARTIFACT experiment_iter2_dir4 -- REALISM-MATCHED SYNTHETIC CHANNEL
  # Zero LLM spend. Pure CPU simulation. Build on iter-1 code; do NOT start from scratch.
  # ==================================================================== #
  #
  # ---- 0. SETUP / REUSE (copy iter-1 code into THIS workspace, then edit) ----
  # THIS workspace (executor's own dir), e.g.:
  #   WS = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_<n>
  # Source files to COPY in and adapt (DO NOT edit the iter-1 originals in place):
  #   SIM   = .../iter_1/gen_art/gen_art_experiment_2/method.py   # THE simulated-channel pipeline (art_TV5eEjdDP-Xp)
  #   ALLEN = .../iter_1/gen_art/gen_art_experiment_2/allen_arm.py # optional Allen secondary arm
  # Real-text calibration TARGET (read-only; art_glhgFsBUrcYo frontier pilot):
  #   FRONTIER = .../iter_1/gen_art/gen_art_experiment_3/method_out.json   # key: metadata.frontier_table
  #   (also metadata.config.knobs = [S1_single,S2_confident,S3_plausible,S4_sound,S5_maximal])
  # Real gold-graph topology (read-only; for the topology-match term):
  #   T0CACHE  = .../iter_1/gen_art/gen_art_experiment_1/cache/{NarrativeTime_point,TDDMan_allen,MATRES_point}_graphs.json
  # Dataset dep (art_ghVQmxVlmOJJ): synthetic backbone metadata + reference_disjunctive_labels
  #   DATASET  = .../iter_1/gen_art/gen_art_dataset_2/full_data_out/full_data_out_{1,2}.json  (concat same-name datasets)
  #   (use only for: (a) cross-check the convex point/Allen composition tables match the dataset's qualreas tables;
  #    (b) extract REAL-ish topology histograms is NOT here -- topology target = the gold graphs in T0CACHE.)
  # pyproject deps (uv): numpy, scipy, matplotlib (same as iter-1 experiment_2). NO network, NO openrouter.
  # Update the hardcoded WORKSPACE = Path(...) constant in the copied method.py to THIS workspace.
  #
  # Keep VERBATIM from method.py (validated, do not re-derive):
  #   - Bitmask point algebra LT/EQ/GT/U + _build_tables() + self_verify_point_algebra()
  #   - QCN generators gen_family_R(K) [H4 redundancy], gen_family_H(L,C) [H3 hop/cyclo]
  #   - closure_FULL (PC-2), closure_NAIVE (single-pass), closure_OFF; classify(); _matrix_from_read()
  #   - stats: boot_mean_ci, boot_diff_ci, page_trend_manual/page_test, jonckheere, spearman_boot_ci
  #   - stage1_toy_tests() (length-2 tie, L>=3 narrowing, unsound->collapse/wrong, all-sound zero-FP)
  #   - _json_default, the method_out.json + datasets[].examples[] structure (schema: exp_gen_sol_out)
  # The ONLY substantive changes are STEP 1 (channel + breadth knob), and the added analyses in STEP 4.
  #
  # ==================================================================== #
  # ---- 1. RE-CALIBRATE THE SIMULATED CHANNEL (the core fix) ----
  # ==================================================================== #
  # 1a. EXTRACT the real-text error-type distribution (calibration target) from FRONTIER['frontier_table'].
  #     Each row = (arm, algebra, knob in {S1..S5}) with fields:
  #        recall, breadth_mean, universal_rate, unsound_rate(=overcommit_unsound_rate),
  #        exact_correct_rate, sound_tight_rate, sound_loose_rate, J2_both_path_sound, J3_all3_sound, path_edge_recall
  #     Define the FIVE mutually-exclusive per-edge error-type categories (sum to 1):
  #        c1=exact_correct  (sound singleton == gold)
  #        c2=sound_tight    (sound, sub-universal, |set|>1 but small)
  #        c3=sound_loose    (sound, larger sub-universal set, still contains gold)
  #        c4=universal      (the '?' set; sound, zero bite)
  #        c5=unsound        (gold EXCLUDED -> over-commit)
  #     Sanity: recall == c1+c2+c3+c4 == 1 - c5 (verify against the table; e.g. TBDense S1 recall 0.572 = 1-0.428).
  #     Use the DENSE real arm 'TBDense_dense' (NarrativeTime stand-in, ALLEN) as the PRIMARY calibration target;
  #     keep 'TDDMan_noncirc' as a secondary target. Record the empirical recall LADDER across S1..S5
  #     (TBDense ~0.57,0.60,0.625,0.78,0.80) and breadth_mean ladder (~1.0,1.05,1.96,4.72,5.49) -- this proves
  #     the real knob DOES trade recall for bite; the synthetic knob must reproduce that coupling.
  #
  # 1b. REDESIGN THE BREADTH KNOB as a SINGLE ORDINAL setting b in {S1..S5} (replace the iter-1 design where
  #     recall r and the fixed breadth dict {p_singleton,p_two,p_univ} were INDEPENDENT inputs).
  #     New read_network(net, knob, rho, rng, gate, gate_drop): for each edge with gold g, draw the emitted set
  #     by SAMPLING the error-type category from the calibrated per-knob distribution P_knob = (c1..c5),
  #     then realize that category as an actual relation mask in the working algebra:
  #        - c1 exact_correct -> singleton {g}
  #        - c2 sound_tight   -> a sound sub-universal 2-relation set containing g (point: g|EQ-neighbor; pick from _SOUND[g] size-2)
  #        - c3 sound_loose   -> a larger sound set containing g (point algebra max sub-universal is size-2, so map
  #                              c3 onto the largest available sound non-universal set; if none, fold c3 into c4 and
  #                              LOG the fold as a known point-algebra representability gap)
  #        - c4 universal     -> U
  #        - c5 unsound       -> a set EXCLUDING g, drawn from _UNSOUND[g] (singleton-wrong or sub-universal-wrong
  #                              with breadth matched to the real knob's mean over-committed-set size)
  #     CONVEXITY GUARD unchanged: never emit the non-convex {<,>}; converse seeded from CONV[] (algebra), never reader.
  #     Per-edge recall is now an OUTPUT = 1 - c5(knob), so sweeping the knob GENUINELY trades recall for bite.
  #     Cross-edge soundness correlation rho stays an equicorrelated-latent knob (as in iter-1 read_network):
  #        soundness z_e = sqrt(rho)*u_latent + sqrt(1-rho)*v_e ; edge is SOUND iff z_e <= ppf(recall_knob).
  #        Sound edges then split among c1/c2/c3/c4 with weights renormalized from P_knob; unsound -> c5.
  #
  # 1c. FIT rho to the real joint-soundness. For each knob, the real table gives J2_both_path_sound and
  #     J3_all3_sound at marginal path_edge_recall. Solve for rho_knob so the equicorrelated channel reproduces
  #     J2 (Gaussian-copula: J2 = P(z1<=q & z2<=q) under corr rho); verify the implied J3 matches J3_all3_sound.
  #     Report |rho_fit - rho_indep_implied| and the J(E)-match residuals |J2_sim-J2_real|, |J3_sim-J3_real|.
  #     Realism PASS term: |Delta_rho| <= 0.10 (ICC-style) i.e. simulated within-network soundness ICC within 0.10
  #     of the real ICC inferred from J2/J3.
  #
  # 1d. COMPUTE THE THREE-PART ACHIEVED REALISM STATISTIC (pre-registered thresholds):
  #     (i)  per-edge error-type TV: TV(P_sim_knob, P_real_knob) = 0.5*sum_cat |p_sim-p_real|, at EACH matched knob.
  #          Measure P_sim by Monte-Carlo emitting >=20000 edges per knob through the calibrated channel and
  #          binning into c1..c5. THRESHOLD TV <= 0.10 (report max and mean over knobs).
  #     (ii) cross-edge rho/ICC match: |Delta_rho| <= 0.10 (from 1c).
  #     (iii) topology histogram TV <= 0.15: compare the contributing-edge-count (E) histogram AND the cycle-structure
  #          (cyclomatic number) histogram of the synthetic networks actually fed to closure against the REAL gold-graph
  #          deduction triangles. Real topology source = T0CACHE graphs (or FRONTIER n_triangles_per_arm structure):
  #          enumerate, per real corpus, the contributing-edge-count of each deduction-required query (mostly E=2 length-2
  #          paths + a long-hop/cyclic tail). Re-weight the synthetic cell sampling (the mixture over K in gen_family_R
  #          and over (L,C) in gen_family_H) so the synthetic E/cyclo histograms match the real ones to TV<=0.15.
  #          If point-algebra/topology representability blocks TV<=0.15, report achieved TV and proceed (downgrade, see 1e).
  #
  # 1e. DOWNGRADE GATE (pre-registered, honest): if per-edge error-type TV<=0.10 CANNOT be met after tuning,
  #     set realism_matched=False and TAG ALL synthetic results 'mechanism characterization under an IDEALIZED channel,
  #     no implied real-text transfer'. ALWAYS report the achieved TV/rho/topology numbers either way. The H3/H4/
  #     silent-wrong MECHANISM findings remain valid as characterization; only the real-text-transfer claim is gated.
  #
  # ==================================================================== #
  # ---- 2. RE-RUN H3: iteration gap PER FIXED RECALL SLICE ----
  # ==================================================================== #
  # Reuse simulate_H3 + analyze_H3 (gen_family_H, FULL/NAIVE/OFF). Changes:
  #  - Map the calibrated knobs S1..S5 to their OUTPUT per-edge recall slices; run H3 at a LADDER of recall slices
  #    spanning the real operating range AND the high-recall regime, e.g. recall in {0.57,0.625,0.78,0.90,0.95,1.00}
  #    (the 5 calibrated-knob recalls + 0.95 + 1.00). For each slice fix the channel so the marginal edge recall == slice.
  #  - HOP ladder L in {2,3,4,5,6}; CYCLO ladder C in {0,1,2,3} at fixed L=6 (as iter-1).
  #  - For EACH recall slice report gap_by_hop = mean(full_correct - naive_correct) per L with paired-bootstrap CI (B>=2000),
  #    the length-2 tie (CI includes 0 -> reported as CONFIRMATION not failure), the max-L positive gap,
  #    and the per-slice trend test: Page's L p-value (use page_test with >=20 blocks x len(HOP)), Jonckheere, Spearman+CI.
  #  - CRITICAL HONESTY: report the gap's RECALL DEPENDENCE explicitly (expect ~0.99 near recall 1.0 but ~0.63 at recall 0.90),
  #    and report the ACTUAL Page p (~1.2e-4 order). DO NOT report 1e-13; if a computed p underflows, clamp-report as a
  #    floor and note it. Same for the cyclomatic trend at fixed L=6 (gap grows with cyclomatic number), per slice.
  #  - H3 PASS (per slice + overall): length-2 tie CI includes 0 AND gap increasing in L (>=2 of 3 trend tests) AND max-L
  #    gap CI excludes 0 AND gap increasing in cyclomatic number; the iteration claim holds on the synthetic backbone.
  #
  # ==================================================================== #
  # ---- 3. RE-RUN H4: recall-dependent inverted-U with benefit/cost decomposition ----
  # ==================================================================== #
  # Reuse simulate_H4 + analyze_H4 (gen_family_R: K parallel length-2 paths). Changes/confirm:
  #  - >=4 fixed per-edge recall levels (use {0.50,0.625,0.78,0.90,0.95}); >=500 nets/cell (full N>=600); B>=2000.
  #  - RHO in {0.0,0.5,0.7}; GATE in {off,on}; K (redundancy) ladder in {1,2,3,4,5,6,8,10,12,16}.
  #  - DECOMPOSE net Mode-A gain into: benefit = P(CORRECT) (singleton-resolution-to-correct), and
  #    silent-narrowing-COST = WRONG rate, plus the explicit cost term (1 - J(E)) per cell. Report benefit, cost,
  #    1-J(E), collapse_rate, abstain_rate, J(E), r^E=recall^mean_E, contains_gold_rate per (recall,rho,gate,K).
  #  - LOCATE the inverted-U peak in benefit (P(CORRECT)) across K, with bootstrap CI on the argmax bin.
  #  - (c) peak moves OUTWARD with recall (peak_idx increases across recall levels, >=1-bin shift).
  #  - (d) peak moves OUTWARD under recall-floor gate ON vs OFF (>=1-bin, majority of cells).
  #  - (e) J(E) > r^E for rho>0 (>=90% of low-recall cells) AND empirical peak/centroid further out than the rho=0
  #    (independence) reference; verify rho=0 IS the independence model (|J(E)-r^E| ~ 0 there).
  #  - H4 PASS: interior inverted-U at low recall AND net-positive region beats BOTH best-single-path and naive AND
  #    peak-outward-with-recall (and, where applicable, gate + J(E)>r^E). A flat/turned-over curve ALONE is NOT a
  #    disconfirmation -- only the ABSENCE of any net-positive region beating both is.
  #
  # ==================================================================== #
  # ---- 4. NEW: SILENT-WRONG-VS-RECALL CURVE + zero-FP THEOREM separation ----
  # ==================================================================== #
  # def analyze_silent_wrong_vs_recall(results, cfg):
  #     # For each per-edge recall slice (pool over rho,gate,K, or report at a reference rho=0,gate=off and also pooled):
  #     for r in cfg['RECALL']:
  #         pool WRONG (silent confident-wrong narrowing) rate = mean(cls==WRONG) over the H4 cells at recall r,
  #         with bootstrap CI. Also compute per-network E and J(E) at that slice.
  #         record: recall, silent_wrong_rate, ci, per_edge_bound = (1 - r), per_network_bound = (1 - mean J(E)).
  #     # ASSERT/REPORT the ordering: silent_wrong_rate <= per_edge_bound and <= per_network_bound at every slice
  #     #   (the certificate is read-soundness-bounded: STRONGEST where reads are good (high recall, small bound),
  #     #    WEAKEST at low real-text recall (large bound)). Emit the monotone-DECREASING curve over recall.
  #     # SEPARATE the zero-FP soundness THEOREM from the empirical curve:
  #     #   theorem block (reuse analyze_C3 'all_sound_contains_gold' invariant): among all-sound contributing
  #     #   subnetworks, P(gold in Mode-A output) == 1.0 EXACTLY (verified, prob-1), collapse never co-occurs with
  #     #   all-sound. TAG = THEOREM/SANITY-CHECK. The silent-wrong curve = EMPIRICAL/SYNTHETIC-CHANNEL.
  #     # Also report the C3 reliability regression (contains_gold_rate ~ J(E)) and the attribution rule:
  #     #   offset shrinking under J(E) vs r^E = independence-approximation failure (NOT a soundness failure).
  #
  # ==================================================================== #
  # ---- 5. OUTPUT (method_out.json, schema exp_gen_sol_out, aii-json validated) ----
  # ==================================================================== #
  # metadata: {method_name, description, scale, llm_spend_usd:0.0, evidence_tag:'SYNTHETIC-CHANNEL',
  #   realism: {target_arm:'TBDense_dense', per_knob_error_type_TV:{S1..S5}, max_TV, mean_TV, TV_threshold:0.10,
  #             rho_fit_by_knob, delta_rho, rho_threshold:0.10, J2_match_residual, J3_match_residual,
  #             topology_TV_E, topology_TV_cyclo, topology_threshold:0.15, realism_matched:bool, downgrade_note},
  #   recall_ladder_real_vs_sim, breadth_ladder_real_vs_sim,
  #   H3:{by_recall_slice:{<r>:{gap_by_hop, length2_tie, maxL_positive, trend:{page_p, jonckheere_p, spearman_ci},
  #                              cyclo_trend}}, page_p_corrected_note, PASS, criteria},
  #   H4:{curves(benefit,cost,one_minus_JE,collapse_rate,abstain_rate,J_E,r_pow_E,contains_gold_rate per cell),
  #       peaks(+CI), net_positive_regions, peak_shift_recall, peak_shift_gate, JE_vs_independence, PASS, criteria},
  #   silent_wrong_vs_recall:[{recall, silent_wrong_rate, ci, per_edge_bound, per_network_bound, within_both_bounds}],
  #   zero_FP_theorem:{all_sound_contains_gold:1.0, invariant_holds:true, collapse_only_when_unsound:true, TAG:'THEOREM'},
  #   C3_reliability:{slope_JE, slope_JE_ci, attribution}, overall_verdict:{H3,H4,silent_wrong_bounded,realism_matched}}
  # datasets: [ {dataset:'synthetic_QCN_H3_hop_chains', examples:[...worked H3 reads w/ predict_full/naive/off...]},
  #            {dataset:'synthetic_QCN_H4_redundancy', examples:[...worked H4 reads w/ outcome,n_contrib_edges,all_sound...]} ]
  #   (KEEP one concrete 3-event WORKED EXAMPLE: one Mode-A narrowing path, one Mode-B collapse path.)
  # Generate full/mini/preview variants via aii-json; check file size with aii-file-size-limit (<100MB/part), split if needed.
  # Write figures: fig1 gap_vs_L per recall slice; fig2 H4 resolution inverted-U + channel decomposition (correct/collapse/
  #   wrong/abstain); fig3 J(E) vs r^E; fig4 silent-wrong-vs-recall with (1-recall) and (1-J(E)) bound overlays;
  #   fig5 realism: sim vs real error-type bars per knob with TV annotation.
  #
  # ---- 6. SCALING (use aii-long-running-tasks) ----
  # Run --scale smoke (N=20) -> mini (N=30) -> test (N=150) -> full (N>=600, B>=2000). Multiprocessing over cells
  # (ProcessPoolExecutor, spawn) as in iter-1; whole full run is seconds-to-minutes on 4 cores. PID-based process mgmt only.
fallback_plan: >-
  FALLBACK A -- realism TV>0.10 unreachable on the convex point algebra (its 6-set ladder cannot represent the ALLEN error-type
  mass finely): (1) FIRST try calibrating against the point-algebra-projected real distribution: project the real ALLEN frontier_table
  error-types onto the point-algebra set ladder {singleton, pair, universal} preserving recall and the sound/unsound split,
  and compute TV in that projected space (this is the apples-to-apples comparison and should pass). (2) If still >0.10, run
  the calibration on the ALLEN ARM instead (reuse allen_arm.py + the 13-relation table) where same-algebra matching to TBDense_dense/TDDMan
  ALLEN rows makes per-edge error-type TV directly minimizable, and keep point algebra as the EXACT-completeness mechanism
  arm. (3) If neither clears 0.10, INVOKE the pre-registered DOWNGRADE: set realism_matched=False, tag all synthetic results
  'mechanism characterization under an idealized channel', report the achieved TV honestly -- the H3/H4/silent-wrong mechanism
  results still stand and the experiment still satisfies the hypothesis's FIX-6 'explicit downgrade' branch. FALLBACK B --
  rho fit cannot reproduce J2/J3 (Gaussian-copula mismatch): report the achieved |Delta_rho| and J-residuals, and if >0.10
  add a beta-binomial or direct-mixture soundness-correlation model; if still off, condition results on rho and report J(E)
  vs r^E descriptively (the attribution rule already handles this -- offset shrinking under J(E) is the independence-approximation
  failing, not a disconfirmation). FALLBACK C -- topology TV>0.15: re-weight the K and (L,C) cell mixtures by solving a small
  nonneg least-squares to match the real E/cyclo histograms; if the real tail (long-hop/cyclic) is too sparse to match, restrict
  the topology-match claim to the length-2/E=2 stratum and report the tail descriptively. FALLBACK D -- H3 length-2 tie does
  NOT hold (gap CI excludes 0 at L=2): this would mean NAIVE != FULL at length-2, a bug in the channel/closure parity -- re-verify
  with stage1_toy_tests (length-2 tie is a theorem); do not ship until the tie is reproduced. FALLBACK E -- inverted-U absent
  (monotone benefit) at all recall levels: this is allowed by the hypothesis (a flat/turned-over curve alone is not a disconfirmation);
  report the recall x redundancy interaction and the net-positive-region test (beats both best-single-path and naive) as the
  load-bearing result instead of peak interiority. FALLBACK F -- runtime/memory: drop to --scale test (N=150) which already
  powers the CIs; cap K at 12; the simulation is light so this is unlikely. NEVER fabricate any number; every reported value
  is computed or the cell is dropped and logged.
testing_plan: >-
  1. SMOKE FIRST (uv run method.py --scale smoke, N=20): confirms (a) point-algebra self-verify PASS, (b) stage1_toy_tests
  PASS -- especially the length-2 FULL==NAIVE tie, the L>=3 FULL-narrows-NAIVE-abstains case, the unsound->collapse/wrong
  (never CORRECT) case, and the all-sound zero-FP invariant (P(gold in output)==1.0), (c) the NEW calibrated read_network
  runs and the realism-statistic block computes a finite TV. 2. CALIBRATION UNIT TEST (before any main run): Monte-Carlo >=20000
  edges through the calibrated channel at each knob S1..S5, bin into the 5 error-type categories, and assert (i) the simulated
  recall == 1 - c5 reproduces the real recall ladder within +/-0.02 (proving the breadth knob now trades recall for bite,
  fixing the iter-1 0.958-flat bug), (ii) the per-knob error-type TV vs the real frontier_table is computed and printed --
  this is the GO/NO-GO confirmation signal for the whole experiment; if max TV <= 0.10 the realism match SUCCEEDED, else trigger
  the downgrade branch and continue. 3. rho/J(E) CHECK: at rho_fit, simulate length-2 and length-3 contributing subnetworks
  and verify J2_sim and J3_sim match the real J2_both_path_sound/J3_all3_sound within +/-0.05; print |Delta_rho|. 4. H3 SANITY
  at mini scale: verify the length-2 gap CI includes 0 at EVERY recall slice and the gap is positive and increasing by L=6
  at recall 1.0; verify the gap SHRINKS as recall drops (0.99 near r=1.0 -> ~0.63 near r=0.90) -- the recall-dependence is
  itself a predicted signal. Confirm the Page p is order ~1e-4 (NOT 1e-13); if it underflows, report a clamped floor with
  a note. 5. H4 SANITY at mini scale: verify benefit (P(CORRECT)) rises then falls in K at low recall, that J(E) >= r^E when
  rho>0, and that 1-J(E) rises with K. 6. SILENT-WRONG SANITY: verify silent_wrong_rate at each recall slice is <= (1-recall)
  and <= (1 - mean J(E)) -- the read-soundness bound must hold by construction; a violation indicates a classification/soundness-bookkeeping
  bug. 7. SCALE UP (aii-long-running-tasks): smoke -> mini -> test (N=150) -> full (N>=600, B>=2000), checking wall-clock
  after each; abort-and-debug if any stage's PASS flags flip implausibly between scales. 8. FINAL: validate method_out.json
  against the exp_gen_sol_out schema with aii-json; confirm the realism block, per-recall-slice H3 curves, decomposed H4 inverted-U,
  and silent-wrong-vs-recall curve are all present and every number is tagged THEOREM vs SYNTHETIC-CHANNEL; run aii-file-size-limit
  and split if any output part exceeds the limit.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_aQ2Rf8rwqteI
type: research
title: >-
  Implementation/Resource Dossier for the Closure-Certified Text-to-Logic Deduction Module
summary: >-
  Verified, executor-ready specifications for the closure-certified temporal-deduction pipeline: (1) corpus access+parse formats
  for NarrativeTime (repo github.com/text-machine-lab/nt, MIT, nt_format JSONL with per-event numeric `time` coordinate +
  bracket-type interval model + same-branch get_event_relation), TDDMan (4-col TSV, codes a/b/i/ii/s, join text from TimeBank-Dense;
  long-distance non-auto-inferable gold), and MATRES (start-point convex point algebra, 2-sentence window = N*~=0 gate control);
  (2) machine-readable GQR composition/converse tables for Allen (13 tokens with < / > for before/after), convex point algebra
  (with the only-non-convex != -> universal widening rule), and RCC-8, each with verified unit-test cells; (3) Mackworth PC-2
  iterated a-closure pseudocode + the precise naive single-pass-intersection contrast (naive==full on length-2, diverges at
  hop>=3 / cyclomatic>=1) + soundness/completeness tractability facts (point-algebra arm EXACT, full Allen/RCC-8 a LOWER BOUND);
  (4) the Renz-Nebel A(n,d,l) model plus the scenario-then-abstract recipe for guaranteed-consistent synthetic QCNs with independent
  density/hop/cyclomatic/recall knobs; (5) baseline configs each with a matched abstention signal (Path-of-Thoughts, self-consistency,
  LINC, DSR-LM/HtT, ILP-commit Eirew et al. M=5, METRE) and a corrected citation (the >=50-97% multiple-relation + ILP-no-F1-gain
  facts are Kougia et al. arXiv:2406.11486, not 'Knez & Sun'); (6) OpenRouter model choice (primary google/gemini-2.5-flash-lite
  $0.10/$0.40, second-family DeepSeek-V3.2/Qwen2.5-72B/Llama-3.3-70B) with arithmetic showing <$10 and a disk-cache + hard
  cost-guard strategy; and (7) the operationalized three-part realism-matching statistic (per-edge error-type TV<=0.10, cross-edge
  soundness-correlation |dro|<=0.10 via ICC, topology histogram TV<=0.15) with J(E) vs r^E. Includes a full decision table,
  a 12-item gotchas list, and 3 unresolved follow-ups.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_ghVQmxVlmOJJ
type: dataset
title: >-
  Synthetic QCN Backbone: consistent Allen/Point/RCC-8 networks with NL realizations
summary: |-
  Clean-ground-truth SYNTHETIC backbone for the redundancy (H4) and iteration (H3) claims: 35,100 globally-consistent Qualitative Constraint Networks over three relation algebras -- convex Point ('<','=','>') and Allen Interval (13 relations) as PRIMARY (500 networks/cell), RCC-8 (8 relations) as SECONDARY (300/cell). Every network is built by model-based realization (integer points / integer-grid intervals / collinear integer discs), so the gold ATOMIC relation on each edge is read exactly off the model and the whole scenario is globally consistent BY CONSTRUCTION (no solver needed). Composition + converse come from the authoritative alreich/qualreas tables, independently cross-checked by 436 tests (Allen composition matches exhaustive endpoint-CSP enumeration; RCC-8 reader sound vs disc enumeration; relation-algebra identity/converse axioms).

  Each network has a held-out query pair (s,t) that shares no edge and never co-occurs in one sentence -- DEDUCTION-REQUIRED: the query relation is obtainable only by composing >=1 multi-edge path. Topology is independently swept across 27 cells per algebra: redundancy P in {1,2,3,4,6,8}; hop L in {2,3,4,5}; cyclomatic mu in {0,1,2,3} via chord augmentation; small/medium/large node-count regimes; and random Renz-Nebel A(n,d) for the natural joint distribution. The intended structural signal is clean (results/dataset_metadata.json -> cell_summary): singleton-resolution rises monotonically with redundancy P (allen 0.40->0.89), bite decays with hop length, cyclomatic augmentation adds paths.

  Output is the aii exp_sel_data_out schema with 3 datasets (synthetic_qcn_point / synthetic_qcn_allen / synthetic_qcn_rcc8); ONE ROW = ONE network. input = template NL realization (one professional-prose sentence per non-query edge, 2-3 paraphrases per relation, + a final 'Query:' line); output = JSON string of the gold graph {edges:[{source,target,relation}], query_edge:{...,is_query:true}}. Rich metadata_* per row: fold (pilot/dev/test by md5(seed)%100 within each cell), algebra, cell labels, MEASURED structure (cyclomatic_number, cycle_basis_size, num_simple_paths_s_t, paths_truncated, contributing_edge_count, avg_degree), enumerated s-t paths with per-path gold composition + naive_intersection + has_bite + singleton_resolved, abstract_graph, entity_map, reference_disjunctive_labels (SOUND superset per edge; convex-only for point), model_embedding, seed. The CORRECTNESS GATE -- composition of gold atomic relations along every enumerated path CONTAINS the gold query relation -- passed on all 35,100 networks. Pre-registered realism thresholds (validated=false; TV<=0.15 / rho<=0.10 / EMD<=0.10) are recorded for next-iteration matching against the real-text frontier pilot.

  Files: full corpus split into full_data_out/full_data_out_1.json + full_data_out_2.json (each <100 MB; concatenate datasets with the same name across parts to reconstruct), plus mini_data_out.json (3 examples/algebra) and preview_data_out.json (10 examples/algebra, strings truncated). Generated deterministically by `uv run data.py` (~18 s on 4 cores; per (algebra, cell, index) md5 seeds, resumable). QA/provenance/dataset-card in results/dataset_metadata.json; algebra package + 436-check verification suite in qcn/ and tests/. The real-text corpora (NarrativeTime / TDDMan / MATRES) are delivered by SIBLING artifacts and are NOT duplicated here.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2
out_dependency_files:
  file_list:
  - data.py
  - full_data_out/full_data_out_1.json
  - full_data_out/full_data_out_2.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out/full_data_out_1.json
  - full_data_out/full_data_out_2.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-17 15:38:05 UTC

```
### Goal

Develop an operational translation pipeline that converts unstructured textual content (e.g., short legal documents, news articles, kids' stories) into a formal first-order logic representation. The output must be capable of (probabilistic) reasoning using a logic reasoner (like Prolog), leveraging LLMs to dynamically resolve terminology, concepts, and relations that are not well defined in the explicit text.

### Reviewer Scope

Limit the technical core to areas the reviewer can deeply evaluate. Other fields are welcome for inspiration but should not host the substantive contribution.

Reviewer-evaluable areas: semantic technologies, logic programming, inductive logic programming, information retrieval, machine learning, LLMs, deep learning, knowledge extraction, knowledge graphs, reasoning, and text data analytics.

The pipeline should ingest a short document (approx. 3000 characters) and parse it into a structured, computable format. Methods may combine an LLM acting as a semantic translation engine (mapping natural text to first-order logic or Prolog predicates), a running logic interpreter (like SWI-Prolog) for symbolic execution, and the integration of upper ontologies like OpenCyc to supply necessary background structure and taxonomic grounding. Furthermore, an LLM should be deployed as a probabilistic reasoning engine to handle fuzzy unifications, semantic similarities, and logical gaps where strict symbolic matching fails due to language ambiguity.

Evaluation must be rigorous and compare the neuro-symbolic pipeline against purely neural baselines (e.g., standard RAG, chain-of-thought prompting) on standard logical reasoning benchmarks (e.g., RuleTaker, CLUTRR) or custom annotated datasets. It must specifically measure:
(i) the precision and recall of atomic fact extraction directly from the original document, and
(ii) the accuracy of multi-hop fact extraction and logical deductions that require synthesizing explicit document facts with implicit common-sense knowledge.

Outputs must provide human-auditable trace-graphs of the reasoning steps to clearly demonstrate the logical path taken.

Constraints: The pipeline must be highly reproducible on any short, professionally written documents. Inference must be executable on commodity hardware, and the system must report a quantified reduction in hallucination rates compared to raw LLM generation.

### Publication

Target ACL Knowledge Extraction track as the primary venue, with EMNLP or specialized neuro-symbolic AI conference tracks (e.g., NeSy) as fallback targets.

### Things to Avoid

Avoid simplistic propositional logic translations of the text. Avoid purely neural black-box systems that lack interpretable reasoning traces. The substantive contribution must be an operational, hybrid method for reasoning with textual content that explicitly minimizes hallucinations.
```

### [3] SKILL-INPUT — aii-python · 2026-06-17 15:38:15 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-17 15:38:15 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-06-17 15:38:15 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-06-17 15:38:15 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-use-hardware · 2026-06-17 15:38:15 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [8] SKILL-INPUT — aii-parallel-computing · 2026-06-17 15:38:15 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SYSTEM-USER prompt · 2026-06-17 16:11:38 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_2_idx4
type: experiment
title: >-
  Realism-Matched Synthetic Channel: Re-establish H3 (per-recall-slice iteration gap), H4 (recall-dependent inverted-U), and
  the Silent-Wrong-vs-Recall curve under a TV-calibrated breadth knob
summary: >-
  Repair the iter-1 synthetic-channel realism breach (measured per-edge error-type TV=0.25 vs pre-registered <=0.10) and the
  dead breadth knob (identical recall 0.958 across S1-S5) by RE-CALIBRATING the simulated reader so its per-edge error-type
  distribution matches the iter-1 real-text frontier-pilot distributions to TV<=0.10, with a SINGLE ordinal breadth knob that
  genuinely trades per-edge recall for bite. Then re-run H3 (FULL minus NAIVE iteration gap stratified by hop-count and cyclomatic
  number, reported AT EACH FIXED RECALL SLICE with the correctly-computed Page trend p, NOT the paper's mis-stated 1e-13),
  H4 (decompose net Mode-A gain into benefit and silent-narrowing-cost 1-J(E) vs redundancy at >=4 fixed recall levels, locate
  the inverted-U peak, verify outward movement with recall and under the recall-floor gate, confirm positive rho makes J(E)
  exceed r^E), and a NEW silent-wrong-vs-recall curve with the per-edge (1-recall) and per-network (1-J(E)) bounds. Everything
  is tagged SYNTHETIC-CHANNEL; the zero-FP soundness THEOREM (all-sound => gold-in-output, prob 1.0) is reported separately
  from the empirical silent-wrong findings. Build directly on iter-1 experiment_2/method.py (self-contained convex-point-algebra
  QCN generator + simulated channel + FULL/NAIVE/OFF closure + bootstrap/Page/Jonckheere stats); zero LLM spend (pure simulation).
  Emit aii-json-validated method_out.json with achieved realism statistics, per-recall-slice gap curves, decomposed inverted-U,
  silent-wrong-vs-recall curve, and PASS/FAIL flags.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # ==================================================================== #
  # ARTIFACT experiment_iter2_dir4 -- REALISM-MATCHED SYNTHETIC CHANNEL
  # Zero LLM spend. Pure CPU simulation. Build on iter-1 code; do NOT start from scratch.
  # ==================================================================== #
  #
  # ---- 0. SETUP / REUSE (copy iter-1 code into THIS workspace, then edit) ----
  # THIS workspace (executor's own dir), e.g.:
  #   WS = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_<n>
  # Source files to COPY in and adapt (DO NOT edit the iter-1 originals in place):
  #   SIM   = .../iter_1/gen_art/gen_art_experiment_2/method.py   # THE simulated-channel pipeline (art_TV5eEjdDP-Xp)
  #   ALLEN = .../iter_1/gen_art/gen_art_experiment_2/allen_arm.py # optional Allen secondary arm
  # Real-text calibration TARGET (read-only; art_glhgFsBUrcYo frontier pilot):
  #   FRONTIER = .../iter_1/gen_art/gen_art_experiment_3/method_out.json   # key: metadata.frontier_table
  #   (also metadata.config.knobs = [S1_single,S2_confident,S3_plausible,S4_sound,S5_maximal])
  # Real gold-graph topology (read-only; for the topology-match term):
  #   T0CACHE  = .../iter_1/gen_art/gen_art_experiment_1/cache/{NarrativeTime_point,TDDMan_allen,MATRES_point}_graphs.json
  # Dataset dep (art_ghVQmxVlmOJJ): synthetic backbone metadata + reference_disjunctive_labels
  #   DATASET  = .../iter_1/gen_art/gen_art_dataset_2/full_data_out/full_data_out_{1,2}.json  (concat same-name datasets)
  #   (use only for: (a) cross-check the convex point/Allen composition tables match the dataset's qualreas tables;
  #    (b) extract REAL-ish topology histograms is NOT here -- topology target = the gold graphs in T0CACHE.)
  # pyproject deps (uv): numpy, scipy, matplotlib (same as iter-1 experiment_2). NO network, NO openrouter.
  # Update the hardcoded WORKSPACE = Path(...) constant in the copied method.py to THIS workspace.
  #
  # Keep VERBATIM from method.py (validated, do not re-derive):
  #   - Bitmask point algebra LT/EQ/GT/U + _build_tables() + self_verify_point_algebra()
  #   - QCN generators gen_family_R(K) [H4 redundancy], gen_family_H(L,C) [H3 hop/cyclo]
  #   - closure_FULL (PC-2), closure_NAIVE (single-pass), closure_OFF; classify(); _matrix_from_read()
  #   - stats: boot_mean_ci, boot_diff_ci, page_trend_manual/page_test, jonckheere, spearman_boot_ci
  #   - stage1_toy_tests() (length-2 tie, L>=3 narrowing, unsound->collapse/wrong, all-sound zero-FP)
  #   - _json_default, the method_out.json + datasets[].examples[] structure (schema: exp_gen_sol_out)
  # The ONLY substantive changes are STEP 1 (channel + breadth knob), and the added analyses in STEP 4.
  #
  # ==================================================================== #
  # ---- 1. RE-CALIBRATE THE SIMULATED CHANNEL (the core fix) ----
  # ==================================================================== #
  # 1a. EXTRACT the real-text error-type distribution (calibration target) from FRONTIER['frontier_table'].
  #     Each row = (arm, algebra, knob in {S1..S5}) with fields:
  #        recall, breadth_mean, universal_rate, unsound_rate(=overcommit_unsound_rate),
  #        exact_correct_rate, sound_tight_rate, sound_loose_rate, J2_both_path_sound, J3_all3_sound, path_edge_recall
  #     Define the FIVE mutually-exclusive per-edge error-type categories (sum to 1):
  #        c1=exact_correct  (sound singleton == gold)
  #        c2=sound_tight    (sound, sub-universal, |set|>1 but small)
  #        c3=sound_loose    (sound, larger sub-universal set, still contains gold)
  #        c4=universal      (the '?' set; sound, zero bite)
  #        c5=unsound        (gold EXCLUDED -> over-commit)
  #     Sanity: recall == c1+c2+c3+c4 == 1 - c5 (verify against the table; e.g. TBDense S1 recall 0.572 = 1-0.428).
  #     Use the DENSE real arm 'TBDense_dense' (NarrativeTime stand-in, ALLEN) as the PRIMARY calibration target;
  #     keep 'TDDMan_noncirc' as a secondary target. Record the empirical recall LADDER across S1..S5
  #     (TBDense ~0.57,0.60,0.625,0.78,0.80) and breadth_mean ladder (~1.0,1.05,1.96,4.72,5.49) -- this proves
  #     the real knob DOES trade recall for bite; the synthetic knob must reproduce that coupling.
  #
  # 1b. REDESIGN THE BREADTH KNOB as a SINGLE ORDINAL setting b in {S1..S5} (replace the iter-1 design where
  #     recall r and the fixed breadth dict {p_singleton,p_two,p_univ} were INDEPENDENT inputs).
  #     New read_network(net, knob, rho, rng, gate, gate_drop): for each edge with gold g, draw the emitted set
  #     by SAMPLING the error-type category from the calibrated per-knob distribution P_knob = (c1..c5),
  #     then realize that category as an actual relation mask in the working algebra:
  #        - c1 exact_correct -> singleton {g}
  #        - c2 sound_tight   -> a sound sub-universal 2-relation set containing g (point: g|EQ-neighbor; pick from _SOUND[g] size-2)
  #        - c3 sound_loose   -> a larger sound set containing g (point algebra max sub-universal is size-2, so map
  #                              c3 onto the largest available sound non-universal set; if none, fold c3 into c4 and
  #                              LOG the fold as a known point-algebra representability gap)
  #        - c4 universal     -> U
  #        - c5 unsound       -> a set EXCLUDING g, drawn from _UNSOUND[g] (singleton-wrong or sub-universal-wrong
  #                              with breadth matched to the real knob's mean over-committed-set size)
  #     CONVEXITY GUARD unchanged: never emit the non-convex {<,>}; converse seeded from CONV[] (algebra), never reader.
  #     Per-edge recall is now an OUTPUT = 1 - c5(knob), so sweeping the knob GENUINELY trades recall for bite.
  #     Cross-edge soundness correlation rho stays an equicorrelated-latent knob (as in iter-1 read_network):
  #        soundness z_e = sqrt(rho)*u_latent + sqrt(1-rho)*v_e ; edge is SOUND iff z_e <= ppf(recall_knob).
  #        Sound edges then split among c1/c2/c3/c4 with weights renormalized from P_knob; unsound -> c5.
  #
  # 1c. FIT rho to the real joint-soundness. For each knob, the real table gives J2_both_path_sound and
  #     J3_all3_sound at marginal path_edge_recall. Solve for rho_knob so the equicorrelated channel reproduces
  #     J2 (Gaussian-copula: J2 = P(z1<=q & z2<=q) under corr rho); verify the implied J3 matches J3_all3_sound.
  #     Report |rho_fit - rho_indep_implied| and the J(E)-match residuals |J2_sim-J2_real|, |J3_sim-J3_real|.
  #     Realism PASS term: |Delta_rho| <= 0.10 (ICC-style) i.e. simulated within-network soundness ICC within 0.10
  #     of the real ICC inferred from J2/J3.
  #
  # 1d. COMPUTE THE THREE-PART ACHIEVED REALISM STATISTIC (pre-registered thresholds):
  #     (i)  per-edge error-type TV: TV(P_sim_knob, P_real_knob) = 0.5*sum_cat |p_sim-p_real|, at EACH matched knob.
  #          Measure P_sim by Monte-Carlo emitting >=20000 edges per knob through the calibrated channel and
  #          binning into c1..c5. THRESHOLD TV <= 0.10 (report max and mean over knobs).
  #     (ii) cross-edge rho/ICC match: |Delta_rho| <= 0.10 (from 1c).
  #     (iii) topology histogram TV <= 0.15: compare the contributing-edge-count (E) histogram AND the cycle-structure
  #          (cyclomatic number) histogram of the synthetic networks actually fed to closure against the REAL gold-graph
  #          deduction triangles. Real topology source = T0CACHE graphs (or FRONTIER n_triangles_per_arm structure):
  #          enumerate, per real corpus, the contributing-edge-count of each deduction-required query (mostly E=2 length-2
  #          paths + a long-hop/cyclic tail). Re-weight the synthetic cell sampling (the mixture over K in gen_family_R
  #          and over (L,C) in gen_family_H) so the synthetic E/cyclo histograms match the real ones to TV<=0.15.
  #          If point-algebra/topology representability blocks TV<=0.15, report achieved TV and proceed (downgrade, see 1e).
  #
  # 1e. DOWNGRADE GATE (pre-registered, honest): if per-edge error-type TV<=0.10 CANNOT be met after tuning,
  #     set realism_matched=False and TAG ALL synthetic results 'mechanism characterization under an IDEALIZED channel,
  #     no implied real-text transfer'. ALWAYS report the achieved TV/rho/topology numbers either way. The H3/H4/
  #     silent-wrong MECHANISM findings remain valid as characterization; only the real-text-transfer claim is gated.
  #
  # ==================================================================== #
  # ---- 2. RE-RUN H3: iteration gap PER FIXED RECALL SLICE ----
  # ==================================================================== #
  # Reuse simulate_H3 + analyze_H3 (gen_family_H, FULL/NAIVE/OFF). Changes:
  #  - Map the calibrated knobs S1..S5 to their OUTPUT per-edge recall slices; run H3 at a LADDER of recall slices
  #    spanning the real operating range AND the high-recall regime, e.g. recall in {0.57,0.625,0.78,0.90,0.95,1.00}
  #    (the 5 calibrated-knob recalls + 0.95 + 1.00). For each slice fix the channel so the marginal edge recall == slice.
  #  - HOP ladder L in {2,3,4,5,6}; CYCLO ladder C in {0,1,2,3} at fixed L=6 (as iter-1).
  #  - For EACH recall slice report gap_by_hop = mean(full_correct - naive_correct) per L with paired-bootstrap CI (B>=2000),
  #    the length-2 tie (CI includes 0 -> reported as CONFIRMATION not failure), the max-L positive gap,
  #    and the per-slice trend test: Page's L p-value (use page_test with >=20 blocks x len(HOP)), Jonckheere, Spearman+CI.
  #  - CRITICAL HONESTY: report the gap's RECALL DEPENDENCE explicitly (expect ~0.99 near recall 1.0 but ~0.63 at recall 0.90),
  #    and report the ACTUAL Page p (~1.2e-4 order). DO NOT report 1e-13; if a computed p underflows, clamp-report as a
  #    floor and note it. Same for the cyclomatic trend at fixed L=6 (gap grows with cyclomatic number), per slice.
  #  - H3 PASS (per slice + overall): length-2 tie CI includes 0 AND gap increasing in L (>=2 of 3 trend tests) AND max-L
  #    gap CI excludes 0 AND gap increasing in cyclomatic number; the iteration claim holds on the synthetic backbone.
  #
  # ==================================================================== #
  # ---- 3. RE-RUN H4: recall-dependent inverted-U with benefit/cost decomposition ----
  # ==================================================================== #
  # Reuse simulate_H4 + analyze_H4 (gen_family_R: K parallel length-2 paths). Changes/confirm:
  #  - >=4 fixed per-edge recall levels (use {0.50,0.625,0.78,0.90,0.95}); >=500 nets/cell (full N>=600); B>=2000.
  #  - RHO in {0.0,0.5,0.7}; GATE in {off,on}; K (redundancy) ladder in {1,2,3,4,5,6,8,10,12,16}.
  #  - DECOMPOSE net Mode-A gain into: benefit = P(CORRECT) (singleton-resolution-to-correct), and
  #    silent-narrowing-COST = WRONG rate, plus the explicit cost term (1 - J(E)) per cell. Report benefit, cost,
  #    1-J(E), collapse_rate, abstain_rate, J(E), r^E=recall^mean_E, contains_gold_rate per (recall,rho,gate,K).
  #  - LOCATE the inverted-U peak in benefit (P(CORRECT)) across K, with bootstrap CI on the argmax bin.
  #  - (c) peak moves OUTWARD with recall (peak_idx increases across recall levels, >=1-bin shift).
  #  - (d) peak moves OUTWARD under recall-floor gate ON vs OFF (>=1-bin, majority of cells).
  #  - (e) J(E) > r^E for rho>0 (>=90% of low-recall cells) AND empirical peak/centroid further out than the rho=0
  #    (independence) reference; verify rho=0 IS the independence model (|J(E)-r^E| ~ 0 there).
  #  - H4 PASS: interior inverted-U at low recall AND net-positive region beats BOTH best-single-path and naive AND
  #    peak-outward-with-recall (and, where applicable, gate + J(E)>r^E). A flat/turned-over curve ALONE is NOT a
  #    disconfirmation -- only the ABSENCE of any net-positive region beating both is.
  #
  # ==================================================================== #
  # ---- 4. NEW: SILENT-WRONG-VS-RECALL CURVE + zero-FP THEOREM separation ----
  # ==================================================================== #
  # def analyze_silent_wrong_vs_recall(results, cfg):
  #     # For each per-edge recall slice (pool over rho,gate,K, or report at a reference rho=0,gate=off and also pooled):
  #     for r in cfg['RECALL']:
  #         pool WRONG (silent confident-wrong narrowing) rate = mean(cls==WRONG) over the H4 cells at recall r,
  #         with bootstrap CI. Also compute per-network E and J(E) at that slice.
  #         record: recall, silent_wrong_rate, ci, per_edge_bound = (1 - r), per_network_bound = (1 - mean J(E)).
  #     # ASSERT/REPORT the ordering: silent_wrong_rate <= per_edge_bound and <= per_network_bound at every slice
  #     #   (the certificate is read-soundness-bounded: STRONGEST where reads are good (high recall, small bound),
  #     #    WEAKEST at low real-text recall (large bound)). Emit the monotone-DECREASING curve over recall.
  #     # SEPARATE the zero-FP soundness THEOREM from the empirical curve:
  #     #   theorem block (reuse analyze_C3 'all_sound_contains_gold' invariant): among all-sound contributing
  #     #   subnetworks, P(gold in Mode-A output) == 1.0 EXACTLY (verified, prob-1), collapse never co-occurs with
  #     #   all-sound. TAG = THEOREM/SANITY-CHECK. The silent-wrong curve = EMPIRICAL/SYNTHETIC-CHANNEL.
  #     # Also report the C3 reliability regression (contains_gold_rate ~ J(E)) and the attribution rule:
  #     #   offset shrinking under J(E) vs r^E = independence-approximation failure (NOT a soundness failure).
  #
  # ==================================================================== #
  # ---- 5. OUTPUT (method_out.json, schema exp_gen_sol_out, aii-json validated) ----
  # ==================================================================== #
  # metadata: {method_name, description, scale, llm_spend_usd:0.0, evidence_tag:'SYNTHETIC-CHANNEL',
  #   realism: {target_arm:'TBDense_dense', per_knob_error_type_TV:{S1..S5}, max_TV, mean_TV, TV_threshold:0.10,
  #             rho_fit_by_knob, delta_rho, rho_threshold:0.10, J2_match_residual, J3_match_residual,
  #             topology_TV_E, topology_TV_cyclo, topology_threshold:0.15, realism_matched:bool, downgrade_note},
  #   recall_ladder_real_vs_sim, breadth_ladder_real_vs_sim,
  #   H3:{by_recall_slice:{<r>:{gap_by_hop, length2_tie, maxL_positive, trend:{page_p, jonckheere_p, spearman_ci},
  #                              cyclo_trend}}, page_p_corrected_note, PASS, criteria},
  #   H4:{curves(benefit,cost,one_minus_JE,collapse_rate,abstain_rate,J_E,r_pow_E,contains_gold_rate per cell),
  #       peaks(+CI), net_positive_regions, peak_shift_recall, peak_shift_gate, JE_vs_independence, PASS, criteria},
  #   silent_wrong_vs_recall:[{recall, silent_wrong_rate, ci, per_edge_bound, per_network_bound, within_both_bounds}],
  #   zero_FP_theorem:{all_sound_contains_gold:1.0, invariant_holds:true, collapse_only_when_unsound:true, TAG:'THEOREM'},
  #   C3_reliability:{slope_JE, slope_JE_ci, attribution}, overall_verdict:{H3,H4,silent_wrong_bounded,realism_matched}}
  # datasets: [ {dataset:'synthetic_QCN_H3_hop_chains', examples:[...worked H3 reads w/ predict_full/naive/off...]},
  #            {dataset:'synthetic_QCN_H4_redundancy', examples:[...worked H4 reads w/ outcome,n_contrib_edges,all_sound...]} ]
  #   (KEEP one concrete 3-event WORKED EXAMPLE: one Mode-A narrowing path, one Mode-B collapse path.)
  # Generate full/mini/preview variants via aii-json; check file size with aii-file-size-limit (<100MB/part), split if needed.
  # Write figures: fig1 gap_vs_L per recall slice; fig2 H4 resolution inverted-U + channel decomposition (correct/collapse/
  #   wrong/abstain); fig3 J(E) vs r^E; fig4 silent-wrong-vs-recall with (1-recall) and (1-J(E)) bound overlays;
  #   fig5 realism: sim vs real error-type bars per knob with TV annotation.
  #
  # ---- 6. SCALING (use aii-long-running-tasks) ----
  # Run --scale smoke (N=20) -> mini (N=30) -> test (N=150) -> full (N>=600, B>=2000). Multiprocessing over cells
  # (ProcessPoolExecutor, spawn) as in iter-1; whole full run is seconds-to-minutes on 4 cores. PID-based process mgmt only.
fallback_plan: >-
  FALLBACK A -- realism TV>0.10 unreachable on the convex point algebra (its 6-set ladder cannot represent the ALLEN error-type
  mass finely): (1) FIRST try calibrating against the point-algebra-projected real distribution: project the real ALLEN frontier_table
  error-types onto the point-algebra set ladder {singleton, pair, universal} preserving recall and the sound/unsound split,
  and compute TV in that projected space (this is the apples-to-apples comparison and should pass). (2) If still >0.10, run
  the calibration on the ALLEN ARM instead (reuse allen_arm.py + the 13-relation table) where same-algebra matching to TBDense_dense/TDDMan
  ALLEN rows makes per-edge error-type TV directly minimizable, and keep point algebra as the EXACT-completeness mechanism
  arm. (3) If neither clears 0.10, INVOKE the pre-registered DOWNGRADE: set realism_matched=False, tag all synthetic results
  'mechanism characterization under an idealized channel', report the achieved TV honestly -- the H3/H4/silent-wrong mechanism
  results still stand and the experiment still satisfies the hypothesis's FIX-6 'explicit downgrade' branch. FALLBACK B --
  rho fit cannot reproduce J2/J3 (Gaussian-copula mismatch): report the achieved |Delta_rho| and J-residuals, and if >0.10
  add a beta-binomial or direct-mixture soundness-correlation model; if still off, condition results on rho and report J(E)
  vs r^E descriptively (the attribution rule already handles this -- offset shrinking under J(E) is the independence-approximation
  failing, not a disconfirmation). FALLBACK C -- topology TV>0.15: re-weight the K and (L,C) cell mixtures by solving a small
  nonneg least-squares to match the real E/cyclo histograms; if the real tail (long-hop/cyclic) is too sparse to match, restrict
  the topology-match claim to the length-2/E=2 stratum and report the tail descriptively. FALLBACK D -- H3 length-2 tie does
  NOT hold (gap CI excludes 0 at L=2): this would mean NAIVE != FULL at length-2, a bug in the channel/closure parity -- re-verify
  with stage1_toy_tests (length-2 tie is a theorem); do not ship until the tie is reproduced. FALLBACK E -- inverted-U absent
  (monotone benefit) at all recall levels: this is allowed by the hypothesis (a flat/turned-over curve alone is not a disconfirmation);
  report the recall x redundancy interaction and the net-positive-region test (beats both best-single-path and naive) as the
  load-bearing result instead of peak interiority. FALLBACK F -- runtime/memory: drop to --scale test (N=150) which already
  powers the CIs; cap K at 12; the simulation is light so this is unlikely. NEVER fabricate any number; every reported value
  is computed or the cell is dropped and logged.
testing_plan: >-
  1. SMOKE FIRST (uv run method.py --scale smoke, N=20): confirms (a) point-algebra self-verify PASS, (b) stage1_toy_tests
  PASS -- especially the length-2 FULL==NAIVE tie, the L>=3 FULL-narrows-NAIVE-abstains case, the unsound->collapse/wrong
  (never CORRECT) case, and the all-sound zero-FP invariant (P(gold in output)==1.0), (c) the NEW calibrated read_network
  runs and the realism-statistic block computes a finite TV. 2. CALIBRATION UNIT TEST (before any main run): Monte-Carlo >=20000
  edges through the calibrated channel at each knob S1..S5, bin into the 5 error-type categories, and assert (i) the simulated
  recall == 1 - c5 reproduces the real recall ladder within +/-0.02 (proving the breadth knob now trades recall for bite,
  fixing the iter-1 0.958-flat bug), (ii) the per-knob error-type TV vs the real frontier_table is computed and printed --
  this is the GO/NO-GO confirmation signal for the whole experiment; if max TV <= 0.10 the realism match SUCCEEDED, else trigger
  the downgrade branch and continue. 3. rho/J(E) CHECK: at rho_fit, simulate length-2 and length-3 contributing subnetworks
  and verify J2_sim and J3_sim match the real J2_both_path_sound/J3_all3_sound within +/-0.05; print |Delta_rho|. 4. H3 SANITY
  at mini scale: verify the length-2 gap CI includes 0 at EVERY recall slice and the gap is positive and increasing by L=6
  at recall 1.0; verify the gap SHRINKS as recall drops (0.99 near r=1.0 -> ~0.63 near r=0.90) -- the recall-dependence is
  itself a predicted signal. Confirm the Page p is order ~1e-4 (NOT 1e-13); if it underflows, report a clamped floor with
  a note. 5. H4 SANITY at mini scale: verify benefit (P(CORRECT)) rises then falls in K at low recall, that J(E) >= r^E when
  rho>0, and that 1-J(E) rises with K. 6. SILENT-WRONG SANITY: verify silent_wrong_rate at each recall slice is <= (1-recall)
  and <= (1 - mean J(E)) -- the read-soundness bound must hold by construction; a violation indicates a classification/soundness-bookkeeping
  bug. 7. SCALE UP (aii-long-running-tasks): smoke -> mini -> test (N=150) -> full (N>=600, B>=2000), checking wall-clock
  after each; abort-and-debug if any stage's PASS flags flip implausibly between scales. 8. FINAL: validate method_out.json
  against the exp_gen_sol_out schema with aii-json; confirm the realism block, per-recall-slice H3 curves, decomposed H4 inverted-U,
  and silent-wrong-vs-recall curve are all present and every number is tagged THEOREM vs SYNTHETIC-CHANNEL; run aii-file-size-limit
  and split if any output part exceeds the limit.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_aQ2Rf8rwqteI
type: research
title: >-
  Implementation/Resource Dossier for the Closure-Certified Text-to-Logic Deduction Module
summary: >-
  Verified, executor-ready specifications for the closure-certified temporal-deduction pipeline: (1) corpus access+parse formats
  for NarrativeTime (repo github.com/text-machine-lab/nt, MIT, nt_format JSONL with per-event numeric `time` coordinate +
  bracket-type interval model + same-branch get_event_relation), TDDMan (4-col TSV, codes a/b/i/ii/s, join text from TimeBank-Dense;
  long-distance non-auto-inferable gold), and MATRES (start-point convex point algebra, 2-sentence window = N*~=0 gate control);
  (2) machine-readable GQR composition/converse tables for Allen (13 tokens with < / > for before/after), convex point algebra
  (with the only-non-convex != -> universal widening rule), and RCC-8, each with verified unit-test cells; (3) Mackworth PC-2
  iterated a-closure pseudocode + the precise naive single-pass-intersection contrast (naive==full on length-2, diverges at
  hop>=3 / cyclomatic>=1) + soundness/completeness tractability facts (point-algebra arm EXACT, full Allen/RCC-8 a LOWER BOUND);
  (4) the Renz-Nebel A(n,d,l) model plus the scenario-then-abstract recipe for guaranteed-consistent synthetic QCNs with independent
  density/hop/cyclomatic/recall knobs; (5) baseline configs each with a matched abstention signal (Path-of-Thoughts, self-consistency,
  LINC, DSR-LM/HtT, ILP-commit Eirew et al. M=5, METRE) and a corrected citation (the >=50-97% multiple-relation + ILP-no-F1-gain
  facts are Kougia et al. arXiv:2406.11486, not 'Knez & Sun'); (6) OpenRouter model choice (primary google/gemini-2.5-flash-lite
  $0.10/$0.40, second-family DeepSeek-V3.2/Qwen2.5-72B/Llama-3.3-70B) with arithmetic showing <$10 and a disk-cache + hard
  cost-guard strategy; and (7) the operationalized three-part realism-matching statistic (per-edge error-type TV<=0.10, cross-edge
  soundness-correlation |dro|<=0.10 via ICC, topology histogram TV<=0.15) with J(E) vs r^E. Includes a full decision table,
  a 12-item gotchas list, and 3 unresolved follow-ups.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_ghVQmxVlmOJJ
type: dataset
title: >-
  Synthetic QCN Backbone: consistent Allen/Point/RCC-8 networks with NL realizations
summary: |-
  Clean-ground-truth SYNTHETIC backbone for the redundancy (H4) and iteration (H3) claims: 35,100 globally-consistent Qualitative Constraint Networks over three relation algebras -- convex Point ('<','=','>') and Allen Interval (13 relations) as PRIMARY (500 networks/cell), RCC-8 (8 relations) as SECONDARY (300/cell). Every network is built by model-based realization (integer points / integer-grid intervals / collinear integer discs), so the gold ATOMIC relation on each edge is read exactly off the model and the whole scenario is globally consistent BY CONSTRUCTION (no solver needed). Composition + converse come from the authoritative alreich/qualreas tables, independently cross-checked by 436 tests (Allen composition matches exhaustive endpoint-CSP enumeration; RCC-8 reader sound vs disc enumeration; relation-algebra identity/converse axioms).

  Each network has a held-out query pair (s,t) that shares no edge and never co-occurs in one sentence -- DEDUCTION-REQUIRED: the query relation is obtainable only by composing >=1 multi-edge path. Topology is independently swept across 27 cells per algebra: redundancy P in {1,2,3,4,6,8}; hop L in {2,3,4,5}; cyclomatic mu in {0,1,2,3} via chord augmentation; small/medium/large node-count regimes; and random Renz-Nebel A(n,d) for the natural joint distribution. The intended structural signal is clean (results/dataset_metadata.json -> cell_summary): singleton-resolution rises monotonically with redundancy P (allen 0.40->0.89), bite decays with hop length, cyclomatic augmentation adds paths.

  Output is the aii exp_sel_data_out schema with 3 datasets (synthetic_qcn_point / synthetic_qcn_allen / synthetic_qcn_rcc8); ONE ROW = ONE network. input = template NL realization (one professional-prose sentence per non-query edge, 2-3 paraphrases per relation, + a final 'Query:' line); output = JSON string of the gold graph {edges:[{source,target,relation}], query_edge:{...,is_query:true}}. Rich metadata_* per row: fold (pilot/dev/test by md5(seed)%100 within each cell), algebra, cell labels, MEASURED structure (cyclomatic_number, cycle_basis_size, num_simple_paths_s_t, paths_truncated, contributing_edge_count, avg_degree), enumerated s-t paths with per-path gold composition + naive_intersection + has_bite + singleton_resolved, abstract_graph, entity_map, reference_disjunctive_labels (SOUND superset per edge; convex-only for point), model_embedding, seed. The CORRECTNESS GATE -- composition of gold atomic relations along every enumerated path CONTAINS the gold query relation -- passed on all 35,100 networks. Pre-registered realism thresholds (validated=false; TV<=0.15 / rho<=0.10 / EMD<=0.10) are recorded for next-iteration matching against the real-text frontier pilot.

  Files: full corpus split into full_data_out/full_data_out_1.json + full_data_out_2.json (each <100 MB; concatenate datasets with the same name across parts to reconstruct), plus mini_data_out.json (3 examples/algebra) and preview_data_out.json (10 examples/algebra, strings truncated). Generated deterministically by `uv run data.py` (~18 s on 4 cores; per (algebra, cell, index) md5 seeds, resumable). QA/provenance/dataset-card in results/dataset_metadata.json; algebra package + 436-check verification suite in qcn/ and tests/. The real-text corpora (NarrativeTime / TDDMan / MATRES) are delivered by SIBLING artifacts and are NOT duplicated here.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2
out_dependency_files:
  file_list:
  - data.py
  - full_data_out/full_data_out_1.json
  - full_data_out/full_data_out_2.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out/full_data_out_1.json
  - full_data_out/full_data_out_2.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Descriptive title (roughly 30-90 characters). Must describe content, NOT a status message.",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [10] SYSTEM-USER prompt · 2026-06-17 16:12:48 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `title`: 'Realism-Matched Synthetic Channel: H3 iteration gap, H4 inverted-U, silent-wrong curve re-established' is too long (at most 90 characters, got 101)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
