# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 15:37:49 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx3
type: experiment
title: >-
  Real-LLM Matched-Coverage Baseline Showdown on the Synthetic QCN Backbone (H1, with H3/zero-FP audit)
summary: >-
  Run REAL OpenRouter LLM reads over the synthetic QCN NL realizations (point + Allen primary, RCC-8 optional), feed the disjunctive
  local reads into the validated FULL-PC / NAIVE / OFF engine, and execute every enumerated baseline (raw LLM, CoT, self-consistency,
  LINC, Path-of-Thoughts, ILP-commit, naive single-pass) at MATCHED COVERAGE using a shared single-relation coverage object.
  Headline H1: Mode-A (FULL closure over disjunctive reads) achieves strictly higher selective accuracy at matched coverage
  than Path-of-Thoughts AND self-consistency, with paired-bootstrap Holm-Bonferroni-adjusted CIs. Secondary: full-minus-naive
  iteration gap vs hop/cyclomatic (H3 on synthetic), Mode-A vs OFF (C2), and a read-soundness/J(E) audit. Every number tagged
  REAL-LLM-READ-ON-SYNTHETIC. Heavy reuse of iter-1 gen_art_experiment_3 assets (engine.py, llm.py, method.py prompt+bootstrap
  helpers); spend held well under $10 via SHA-256 caching of entity-normalized edge reads and a hard cost guard.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  # ============================================================================
  # EXPERIMENT experiment_iter2_dir3 -- REAL-LLM matched-coverage baseline showdown
  # on the SYNTHETIC QCN backbone. Output: method_out.json (aii-json validated).
  # Compute: CPU only (LLM calls are async API I/O; closure/ILP are millisecond).
  # Budget: HARD cap $9 OpenRouter, soft warn $2; track client.cost after every call.
  # ============================================================================
  #
  # ---------- 0. REUSE MAP (copy these files into the workspace, do NOT re-derive) ----------
  # DATASET (dep art_ghVQmxVlmOJJ):
  #   DS = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2
  #   data: DS/full_data_out/full_data_out_1.json + full_data_out_2.json
  #         (each <100MB; reconstruct by CONCATENATING datasets sharing the same
  #          'dataset' name across the two parts). DS/mini_data_out.json (3/algebra),
  #          DS/preview_data_out.json (10/algebra) for smoke tests.
  #   tables: DS/qcn/algebra_tables/{Linear_Point_Algebra,Linear_Interval_Algebra,RCC8_Algebra}.json
  #   algebra pkg (for RCC-8 only): DS/qcn/algebras.py (load_algebras(), compose_sets, intersect, converse_set)
  # ENGINE (referenced art_K7riobQ_Rmwz / found in gen_art_experiment_3):
  #   ENG = .../gen_art/gen_art_experiment_3/engine.py
  #     build_point_algebra(), build_allen_algebra()  (point + Allen ONLY, no RCC-8)
  #     class QCN(alg, nodes): set_edge(i,j,frozenset), get(i,j), known_edges()
  #     pc2_full(qcn) -> (consistent:bool, n_fired); read closed query rel from qcn.get(s,t) AFTER
  #     naive_single_pass(qcn, u, v) -> frozenset  (single pass, no fixpoint = PoT+1 step)
  #     close_triangle(alg, ab, bc, ac) -> {path, inter, empty, singleton, n_widen}
  #     alg.widen(s)->(s',fired) applies the point convex {<,>}->universe rule (COUNT widenings)
  # LLM CLIENT + PROMPT (art_glhgFsBUrcYo / gen_art_experiment_3):
  #   LLM = .../gen_art_experiment_3/llm.py : OpenRouterClient(api_key, model, fallbacks, cache_dir,...)
  #         attrs .cost .n_calls .n_cache_hits .n_errors ; SHA-256 disk cache; hard budget guard.
  #         parse_relations(content, vocab) -> (coarse_set, underdetermined_bool, parse_fail_bool)
  #   MET = .../gen_art_experiment_3/method.py : KNOB / KNOB_ORDER (S1_single..S5_maximal breadth knob),
  #         build_prompt(task, knob) (marked [[E1]]..[[/E1]] + JSON {relations:[...],underdetermined:bool}),
  #         clustered_bootstrap_ci(doc_to_vals,...) (resamples DOCS for rho), icc_oneway(groups) (rho via ICC).
  #         pre-reg constants: MODEL_PRIMARY='google/gemini-3.1-flash-lite',
  #         MODEL_FALLBACKS=['deepseek/deepseek-v3.2','deepseek/deepseek-v4-flash'], TEMPERATURE=0.0,
  #         RECALL_GATE_POINT=0.90, RECALL_GATE_ALLEN=0.85, APPLIC_GENERAL=0.10, BUDGET_USD_HARD=9.0
  #   STATS (reuse from gen_art_experiment_2/method.py): boot_diff_ci, page_test, jonckheere, spearman_boot_ci
  # DOSSIER (dep art_aQ2Rf8rwqteI): .../gen_art_research_1/research_out.json -- baseline configs,
  #   ILP-commit (Eirew M=5), LINC, PoT, model arithmetic, gotchas. READ before coding baselines.
  # NOTE: verify model id with aii-openrouter-llms skill at runtime (gemini-2.5-flash-lite was
  #   RETIRED; iter-1 used google/gemini-3.1-flash-lite). If primary gone, pick cheapest capable
  #   instruct model from the skill and record model_used in output.
  #
  # ---------- 1. LOAD + SUBSET THE SYNTHETIC DATA ----------
  # Reconstruct each of the 3 datasets (synthetic_qcn_point, synthetic_qcn_allen, synthetic_qcn_rcc8)
  # by merging the same-named dataset across full_data_out_1.json and _2.json.
  # Parse per row: input (NL realization), output JSON -> {edges:[{source,target,relation}], query_edge},
  #   metadata_fold, metadata_algebra, metadata_cell.cell_id, metadata_query{source,target,relation},
  #   metadata_structure{cyclomatic_number, num_simple_paths_s_t, contributing_edge_count, num_nodes},
  #   metadata_paths{path_list, path_compositions, naive_intersection, has_bite, singleton_resolved},
  #   metadata_entity_map (node_idx -> entity phrase),
  #   metadata_reference_disjunctive_labels (SOUND superset per edge -> used ONLY to MEASURE recall, never as the read).
  # COMPARISON STRATA (cells where Mode-A has bite & baselines are meaningful):
  #   redundancy axis: red_P1_L2,red_P2_L2,red_P3_L2,red_P4_L2,red_P6_L2,red_P8_L2  (singleton_resolved 0.4->0.89)
  #   hop axis:        hop_L2_P2,hop_L3_P2,hop_L4_P2,hop_L5_P2
  #   cyclomatic axis: cyc_mu0,cyc_mu1,cyc_mu2,cyc_mu3                              (iteration / H3)
  # PRIMARY algebras = point (PC COMPLETE, 3 relations, exact) + allen (13 rels, LOWER BOUND).
  #   point is the CLEAN headline arm; allen is the generality arm. RCC-8 = OPTIONAL Tier-2.
  # Use FOLD discipline: dev fold (md5%100 in 10..29) to fix the operating point + sanity;
  #   test fold (>=30) for the REPORTED H1 numbers (never tune on test).
  # Sampling: N_PER_CELL networks/cell (start dev pilot ~10; full test ~60-100). Stratified, deterministic
  #   (sort test rows by metadata_seed, take first N). Record exactly which rows were used.
  #
  # ---------- 2. NEURAL READING (the disjunctive local reads = the SHARED substrate) ----------
  # Operating point = the breadth knob that clears the recall gate. Reuse the frontier finding:
  #   iter-1 synthetic clean text had recall ~0.96; default OPERATING_KNOB='S4_sound'. On the dev
  #   fold, sweep {S3_plausible,S4_sound,S5_maximal} on a small sample, MEASURE per-edge recall vs
  #   the gold atom, and PICK the cheapest knob with recall>=RECALL_GATE (0.90 point / 0.85 allen).
  #   Freeze OPERATING_KNOB before the test-fold run.
  # Build a SYNTHETIC read prompt (variant of MET.build_prompt) presenting the NATIVE algebra vocab:
  #   point: '<' (E1 before E2), '=' (same time), '>' (E1 after E2).
  #   allen: the 13 base relations each with a one-line endpoint definition (b,bi,m,mi,o,oi,d,di,s,si,f,fi,eq).
  #   rcc8 (opt): DC,EC,PO,EQ,TPP,NTPP,TPPi,NTPPi each defined.
  #   System: 'Read ONLY from this sentence; do NOT assume consistency with other pairs.' + KNOB[knob].
  #   Output JSON {"relations":[...],"underdetermined":bool}. Reuse LLM.parse_relations (extend its
  #   vocab to the native base sets) to get the emitted frozenset.
  # READ EACH NON-QUERY EDGE LOCALLY:
  #   for edge (u,v) in output.edges:
  #       sent = the input sentence mentioning BOTH entity_map[u] and entity_map[v] (unique per network;
  #              match by substring of the two entity phrases). Mark them E1=u, E2=v.
  #       NORMALIZE for caching: replace entity_map[u]->'E1', entity_map[v]->'E2' in sent; cache key =
  #              sha256(normalized_sent + '|' + knob + '|' + algebra). -> near-100% cache hits across
  #              networks (read is entity-agnostic & local), making edge reads ~free.
  #       emitted_uv = parse(LLM(system,user))  # sound disjunctive set, oriented u->v
  #       POINT widening: if emitted_uv=={'<','>'} -> universe, COUNT bite_lost (convexity guard).
  #       store read[(u,v)] = emitted_uv ; read[(v,u)] = alg.converse(emitted_uv)  # converse from ALGEBRA
  #   Run reads CONCURRENTLY (async, ~16-32 in flight) via the reused client; check client.cost each batch.
  # RECORD per-edge soundness vs gold: sound_uv = (gold_atom(u,v) in emitted_uv); recall = mean(sound_uv);
  #   breadth = |emitted_uv|; over_commit = not sound_uv; also store doc-id (network) for rho/ICC.
  #
  # ---------- 3. METHOD + SYMBOLIC VARIANTS (free, no LLM) over the SAME reads ----------
  # Build QCN from reads: nodes=range(num_nodes); for each non-query edge set_edge(u,v,read[(u,v)]);
  #   query edge (s,t) left at universe.
  # MODE-A (FULL, our method):
  #   q = QCN(...); set all read edges; consistent,_ = pc2_full(q); rq = q.get(s,t)
  #   if not consistent (empty anywhere) -> ModeB_DETECT (abstain, collapse-certificate)
  #   elif |rq|==1 -> answer=rq.single ; covered=True   # singleton-resolution
  #   else -> abstain (rq still disjunctive)
  # NAIVE single-pass (iteration contrast): rn = naive_single_pass(q_reads, s, t)  # NO fixpoint
  #   covered iff |rn|==1; answer=rn.single.   (coincides w/ FULL on length-2; diverges hop>=3/cyclic)
  # OFF (no composition floor): query edge never locally readable -> always abstain (coverage 0);
  #   report as the deduction-required gap (echoes iter-1 local-read 26.7%).
  # correctness for any variant: covered & (answer == gold_query).
  #
  # ---------- 4. NEURAL BASELINES (full-document; each emits prediction + abstention SCORE) ----------
  # All baselines see the SAME document = the full NL realization (all edge sentences + Query line).
  # The query relation is NEVER stated (deduction-required), so every method must DEDUCE it.
  # Define the coarse/native answer vocab = algebra base relations (point 3 / allen 13).
  # (b1) RAW LLM  [HEADLINE-supporting]: 'Give THE single relation of {Es}->{Et}; also output confidence 0-1.'
  #        temp=0.0; conf = verbalized confidence. 1 call/net.
  # (b2) CoT: same but 'reason step by step, then give the single relation + confidence.' 1 call/net.
  # (b3) SELF-CONSISTENCY (vote margin) [H1 GATEWAY baseline]: K=5 CoT samples temp=0.7;
  #        answer = majority relation; conf = (top_votes - second_votes)/K. 5 calls/net.
  # (b4) LINC-style multi-formalization vote [lightweight]: M=3 prompts that translate the doc to a
  #        single-label relation set per pair then read off the query (committed, single-label per edge),
  #        majority-vote the query answer; conf = agreement fraction. 3 calls/net.
  # (b5) PATH-OF-THOUGHTS [PRIMARY H1 baseline, run faithfully]: (i) one graph-extraction call OR reuse
  #        the per-edge reads as the extracted graph; (ii) enumerate s-t paths (cap PATHS<=6 by
  #        num_simple_paths; log truncation); (iii) for EACH path, ONE LLM call reasoning that path's
  #        chained relations to a SINGLE query relation INDEPENDENTLY (no cross-path intersection);
  #        (iv) aggregate by agreement: answer=majority across paths, conf=path-agreement fraction
  #        (abstain when paths disagree). This is exactly the cross-path-intersection gap Mode-A fills.
  # (b6) ILP-COMMIT (Eirew M=5) [lightweight]: take the disjunctive reads (or M=5 single-label reads),
  #        solve a small ILP over the subnetwork induced by edges on s-t paths: binary x[e,r],
  #        sum_r x[e,r]=1 (uniqueness), transitivity constraints from the composition table on triples,
  #        maximize total read-confidence; read committed query relation; conf = solver objective margin
  #        (or fraction of M=5 agreeing). Use PuLP+CBC (pip). KEEP SMALL (path-induced subgraph only).
  # (b7) NAIVE single-pass = symbolic baseline from step 3 (no extra LLM).
  # COST CONTROL: cache every prompt by sha256(messages+model+temp+sample_idx). Self-consistency
  #   samples keyed by idx. Project cost before the full run; if >budget, cut in priority order:
  #   drop ILP/LINC first, then reduce K (5->3), then reduce N_PER_CELL. NEVER drop PoT or SC.
  #
  # ---------- 5. MATCHED-COVERAGE SELECTIVE COMPARISON (the H1 statistic) ----------
  # Coverage OBJECT = single-relation resolution (identical for all methods).
  # For each network n and method m: have correct_m[n] in {0,1}, covered/conf.
  # Target coverage c* = Mode-A coverage = mean(Mode-A covered).   # structural, fixed
  # For each baseline b with continuous conf:
  #   choose tau_b so fraction(conf_b >= tau_b) == c* (interpolate on the sorted conf grid);
  #   covered_b[n] = conf_b[n] >= tau_b ; selacc_b = sum(correct_b*covered_b)/sum(covered_b).
  # selacc_ModeA = sum(correct_A*covered_A)/sum(covered_A).
  # gap_b = selacc_ModeA - selacc_b.
  # PAIRED BOOTSTRAP (B=2000): resample NETWORK indices with replacement (shared across methods =
  #   paired); recompute selacc_ModeA and selacc_b at FIXED tau_b each resample; collect gap*; 95% CI.
  #   (sensitivity: also report a re-matched-tau-per-resample variant.)
  # Also compute and store FULL risk-coverage curves (sweep tau over a grid) for each method, for figures.
  # MULTIPLICITY: confirmatory H1 family = {Mode-A vs PoT, Mode-A vs self-consistency}. Apply
  #   Holm-Bonferroni across the family; report ADJUSTED CIs. PASS_H1 = both adjusted CIs exclude 0
  #   on the positive side. Report raw LLM/CoT/LINC/ILP/naive gaps too (labelled exploratory, nominal CIs).
  # STRATIFY everything by algebra, redundancy P, hop L, cyclomatic mu; report per-stratum gaps.
  #   Headline pooled over the bite-bearing strata (P>=2 redundancy + low-hop). Predicted: Mode-A TIES
  #   naive on length-2 (report tie as confirmation), > PoT/SC across.
  #
  # ---------- 6. SECONDARY ANALYSES (tag each) ----------
  # H3 ITERATION (synthetic): full_correct - naive_correct accuracy gap per hop L (hop_L*) and per
  #   cyclomatic mu (cyc_mu*); monotone-trend (Page/Jonckheere/Spearman-boot, reuse exp_2 fns).
  #   Predicted: ~0 at L=2, GROWS with L and mu. (Mirrors iter-1 simulated channel but now REAL reads.)
  # C2 closure ON vs OFF: Mode-A coverage/accuracy vs OFF (=0) -> quantifies deduction-required gap.
  # READ-SOUNDNESS / ZERO-FP AUDIT (REAL-LLM-READ-ON-SYNTHETIC): per-edge recall; J(E)=fraction of
  #   networks where ALL contributing edges sound (group by contributing_edge_count); silent-wrong rate
  #   = covered & wrong & query-set-omits-gold; reliability: among all-sound networks, fraction whose
  #   Mode-A set still CONTAINS gold (should be ~1.0 = zero-FP-conditional-on-soundness). Report
  #   within-document cross-edge soundness correlation rho via icc_oneway. Compare the real-read
  #   per-edge error-type distribution to iter-1's simulated channel (TV distance) -- informational.
  # WORKED EXAMPLE: dump one network's full trace (reads, which compositions fired on which paths,
  #   the narrowed query set) as a human-auditable trace-graph (Mode-A narrowing path + a Mode-B collapse).
  #
  # ---------- 7. OUTPUT method_out.json (aii-json validated) ----------
  # Use the aii-json skill to find/validate the experiment solution-output schema (iter-1 used
  #   'exp_gen_sol_out'); conform to it. Include:
  #   metadata: {model_primary, model_used, fallbacks, temperature, operating_knob, recall_gates,
  #              folds_used, n_networks_per_cell, seed, EVIDENCE_TAG:'REAL-LLM-READ-ON-SYNTHETIC'}
  #   leaderboard: per method {coverage, selective_accuracy_at_matched_cov, singleton_resolution_to_correct,
  #              strict_tightening (non-load-bearing), gap_vs_ModeA, ci, adjusted_ci}
  #   per_stratum: gaps by (algebra,P,L,mu)
  #   H1: {target_coverage, gap_PoT, gap_SC, holm_adjusted_cis, PASS:bool}
  #   H3: {gap_by_hop, gap_by_cyclo, trend tests, length2_tie}
  #   audit: {per_edge_recall, J_E_by_E, silent_wrong_rate, zero_fp_contains_gold_rate, rho_icc, tv_vs_sim_channel}
  #   cost: {cumulative_openrouter_usd, n_llm_calls, cache_hits}
  #   worked_example, verdict (PASS/FAIL H1 on synthetic + honest scope note).
  # Generate mini/preview variants if the file is large; run aii-file-size-limit check.
fallback_plan: |-
  MODEL: if 'google/gemini-3.1-flash-lite' is retired, query aii-openrouter-llms for the cheapest capable instruct model (try deepseek/deepseek-v3.2, then a small Gemini/Llama-3.3-70B) and record model_used; the cached client already supports a fallback list. If the chosen model's verbalized confidence is uninformative for raw/CoT, substitute token-logprob or self-consistency margin as the abstention score and note it.

  BUDGET: project cost on the dev pilot (cost-per-network x planned N). If it would exceed ~$8, cut in this fixed priority order WITHOUT touching the H1 gateways: (1) drop ILP-commit and LINC (the dossier itself calls them lightweight/optional), (2) reduce self-consistency K 5->3, (3) cap PoT paths to 4, (4) reduce N_PER_CELL, (5) restrict to the POINT algebra headline only. Always keep Mode-A, PoT, self-consistency, naive, raw on >=1 fully-powered arm. Entity-normalized read caching should already make edge reads ~free; if not, cache aggressively and dedupe.

  ALLEN READS WEAK: if the 13-relation read recall stays below RECALL_GATE_ALLEN (0.85) even at S4/S5 (LLM struggles to enumerate 13 Allen relations), fall back to (a) the coarse 5-relation interval vocab used by the iter-1 real-text arm (before/after/simultaneous/includes/is_included) mapped to a coarse interval algebra, or (b) make POINT the sole headline arm (3 relations, recall ~0.96, PC-complete, exact) and report Allen as exploratory/lower-bound. Point alone is a sufficient, clean H1 venue.

  ENGINE/CLIENT IMPORT FAILS: engine.py and llm.py are self-contained iter-1 files -- copy them into the workspace. If they cannot be imported, reimplement: (closure) from the dossier's Mackworth PC-2 pseudocode + the DS/qcn/algebra_tables/*.json composition/converse tables (point/allen/rcc8 all present, 436-check verified); (client) a thin async OpenRouter wrapper from the aii-openrouter-llms skill with a SHA-256 disk cache + a running-cost guard that raises before exceeding $9. RCC-8 has no built-in engine algebra: build an Algebra from DS/qcn/algebras.py load_algebras()['rcc8'] (it exposes compose_sets/intersect/converse_set) and write a tiny PC-2 over it, or skip RCC-8 (optional).

  ILP SOLVER MISSING: if PuLP/CBC is unavailable, implement ILP-commit as greedy most-confident-singleton-per-edge + transitivity repair over the path-induced subgraph, or drop it (optional baseline).

  H1 NEGATIVE: if Mode-A does NOT beat PoT and self-consistency even on synthetic where reads are recall~0.96 (a surprising result), report it honestly as a REAL-LLM-ON-SYNTHETIC negative, keep the H3 iteration gap, the zero-FP/J(E) audit, and the OFF-gap (deduction-required) findings, and flag for the paper that the synthetic mechanism advantage is contingent (feeds the NeSy/findings retarget the hypothesis already pre-registers). Diagnose WHY (e.g., PoT also composes correctly when reads are near-perfect; the Mode-A edge should appear most where reads are noisier or paths longer -- check the hop/cyclomatic strata and any reader-degradation arm).

  LOW POWER IN A STRATUM: deduction-required coverage collapses at L>=4/L5 (singleton_resolved ~0.01-0.04). Pool the headline over bite-bearing strata (P>=2, L=2-3, cyc) and report sparse strata descriptively only; do not gate H1 on an under-powered cell.
testing_plan: |-
  Follow the aii-long-running-tasks gradual-scaling pattern; never launch the full paid run before the confirmation signals below fire.

  STAGE 0 -- wiring & engine (zero spend). Copy engine.py, llm.py, and the needed helpers from gen_art_experiment_3 (+ exp_2 stats fns). Import build_point_algebra/build_allen_algebra, run the iter-1 engine unit checks (closure_tests_pass / the __main__ spot prints: ALLEN B o B, POINT '<' o '>' == universe). Add OWN sanity asserts: (a) feed the GOLD atomic reads of a mini network into the QCN, run pc2_full, assert q.get(s,t) == {gold_query} (pipeline wired right; closure recovers gold from sound singletons); (b) on a length-2 example assert naive_single_pass == pc2_full result (the predicted tie); (c) on a length-3 chain assert FULL narrows where NAIVE abstains (engine docstring example). Confirm point convexity widening fires & is counted for {'<','>'}.

  STAGE 0b -- model + cache round-trip (tiny spend, <$0.01). Instantiate OpenRouterClient; send one read prompt; resend identical -> assert the 2nd is a cache hit and client.cost unchanged; assert parse_relations returns a valid frozenset for the native vocab. Verify the entity-normalization cache key dedupes two networks that share a relation phrasing.

  STAGE 1 -- end-to-end mini (<$0.10). Run the WHOLE pipeline (reads -> QCN -> Mode-A/naive/OFF -> all baselines -> matched-coverage -> method_out skeleton) on DS/mini_data_out.json (3/algebra) then ~5 networks/cell from the DEV fold, point algebra first. Assert: no crashes; cost logged; method_out validates against the aii-json schema; PoT/SC produce predictions+conf.

  STAGE 2 -- DEV-fold pilot + CONFIRMATION SIGNALS (a few hundred reads, <$0.50). On ~10 networks/cell (dev), point + allen:
    * SIGNAL 1 (reads work): per-edge recall at the operating knob >= RECALL_GATE (>=0.90 point / >=0.85 allen), echoing iter-1's ~0.96 on synthetic clean text. If not, invoke the Allen/operating-knob fallback BEFORE scaling.
    * SIGNAL 2 (mechanism alive): Mode-A singleton-resolution-to-correct > 0 and tracks the metadata singleton_resolved_frac ordering (rises with redundancy P: red_P1<red_P4<red_P8).
    * SIGNAL 3 (machinery sane): matched-coverage gaps are finite, coverage matches across methods at c*, paired-bootstrap CIs computed, Holm adjustment runs.
    Freeze the operating knob now. Project full-run cost from measured cost/network.

  STAGE 3 -- TEST-fold full run (the reported numbers). Scale N_PER_CELL to the budget-feasible max (target ~60-100/cell). Run async with the hard $9 cost guard; checkpoint reads/results to disk (resumable). Monitor client.cost each batch; if approaching budget, apply the fallback cut order. Compute H1 (Holm-adjusted), H3, C2, the zero-FP/J(E) audit, the worked example. Tag every number REAL-LLM-READ-ON-SYNTHETIC. Validate the final method_out.json with aii-json and run the aii-file-size-limit check (emit mini/preview variants if oversized). Cross-check: the OFF arm coverage is ~0 (no direct query read); Mode-A ties naive on the L=2 stratum; full-minus-naive gap grows with L/mu.
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

### [2] HUMAN-USER prompt · 2026-06-17 15:37:49 UTC

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

### [3] SKILL-INPUT — aii-json · 2026-06-17 15:43:23 UTC

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

### [4] SKILL-INPUT — aii-openrouter-llms · 2026-06-17 15:43:43 UTC

The agent loaded the **aii-openrouter-llms** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-openrouter-llms
description: Searches and calls LLMs from OpenRouter's extensive catalog (Claude, GPT, Gemini, Llama, Mistral, DeepSeek, etc.) with reasoning and temperature control. Use when user needs to access various LLMs, compare language models, call different model providers, find the best model for a task, or look up model pricing and costs per million tokens.
---

## Contents

- Workflow (2-phase model discovery and calling)
- Scripts (Search, Get Params, Call)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: Model Discovery and Calling

### Phase 1: Search for Models
Find models with pricing, context length, and descriptions
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_search_llms.py "claude" --limit 5
```

### Phase 2 (optional): Get Model Parameters
Check what parameters a specific model supports
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "anthropic/claude-haiku-4.5"
```

### Phase 3: Call Model
Call a model using the API name from search results
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py --model "anthropic/claude-haiku-4.5" --input "What is 2+2?"
```

---

## Scripts

### Search OpenRouter models (aii_or_search_llms.py)

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_search_llms.py "claude" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: When running multiple searches, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_search_llms.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {} --limit 5' ::: 'claude' 'gpt' 'gemini'
```

**Example output:**
```
Found 5 models for query: claude

[1] Anthropic: Claude Opus 4.5
    API: anthropic/claude-opus-4.5
    Context: 200,000 tokens
    Price: $5.00/M in, $25.00/M out
    Claude Opus 4.5 is Anthropic's frontier reasoning model...

[2] Anthropic: Claude Haiku 4.5
    API: anthropic/claude-haiku-4.5
    Context: 200,000 tokens
    Price: $1.00/M in, $5.00/M out
    ...
```

**Parameters:**

`query` (optional, positional)
- Search query to filter models (e.g., 'claude', 'gpt', 'reasoning')

`--limit, -n` (optional)
- Maximum number of results (default: 10)

`--series, -s` (optional)
- Filter by model family
- Valid: GPT, Claude, Gemini, Grok, Cohere, Nova, Qwen, Yi, DeepSeek, Mistral, Llama2, Llama3, Llama4, RWKV, Qwen3, Router, Media, Other, PaLM

`--timeout` (optional)
- Request timeout in seconds (default: 60)

**Tips:**
- Use the `API` field from results for the `--model` parameter in calls
- Search is fast (queries OpenRouter's model list)

---

### Get model parameters (aii_or_get_llm_params.py)

Get detailed information and supported parameters for a specific model.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "anthropic/claude-haiku-4.5"
```

**Parallel execution (multiple models):**

IMPORTANT: When checking multiple models, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_get_llm_params.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {}' ::: 'anthropic/claude-haiku-4.5' 'openai/gpt-4o-mini' 'google/gemini-2.0-flash-001'
```

**Example output:**
```
Model: Anthropic: Claude Haiku 4.5
API: anthropic/claude-haiku-4.5

=== Capabilities ===
Context Length: 200,000 tokens
Max Output: 64,000 tokens
Modality: text+image->text
Input: image, text
Output: text
Moderated: Yes

=== Pricing ===
Input: $1.0000/M tokens
Output: $5.0000/M tokens

=== Supported Parameters ===
  - include_reasoning
  - max_tokens
  - reasoning
  - stop
  - temperature
  - tool_choice
  - tools
  - top_k
  - top_p
```

**Parameters:**

`model` (required, positional)
- Model API name (e.g., 'anthropic/claude-haiku-4.5', 'openai/o1')

`--timeout` (optional)
- Request timeout in seconds (default: 30)

**Tips:**
- Use after search to see which parameters a model supports
- Check supported_parameters before using --reasoning or other options

---

### Call OpenRouter model (aii_or_call_llms.py)

Make an API call to an OpenRouter LLM model.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py --model "anthropic/claude-haiku-4.5" --input "What is 2+2?"
```

**Parallel execution (multiple calls):**

IMPORTANT: When calling multiple models, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_call_llms.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --model {} --input "What is 2+2?"' ::: 'anthropic/claude-haiku-4.5' 'openai/gpt-4o-mini' 'google/gemini-2.0-flash-001'
```

**Example output:**
```
Model: anthropic/claude-haiku-4.5

Response:
Four.

Tokens: 12 in, 5 out
```

**Parameters:**

`--model, -m` (required)
- API model name from search results (format: `provider/model-name`)
- Examples: `anthropic/claude-sonnet-4`, `openai/gpt-5`, `google/gemini-2.5-pro`

`--input, -i` (required, unless using --input-json)
- Simple string prompt

`--input-json` (optional)
- Full conversation JSON for multi-turn (mutually exclusive with --input)

`--max-tokens` (optional)
- Maximum output tokens (default: 9000)

`--reasoning` (optional)
- Reasoning effort for reasoning models: `minimal`, `low`, `medium`, `high`

`--temperature, -t` (optional)
- Randomness (0.0-2.0): 0.0=deterministic, 0.7=balanced, 1.5+=creative

`--top-p` (optional)
- Nucleus sampling (0.0-1.0)

`--instructions` (optional)
- System instructions/prompt

`--web-search` (optional)
- Enable web search with max results (e.g., 10)

`--params, -p` (optional)
- Extra model-specific parameters as JSON string
- Use `aii_or_get_llm_params.py` to see which params a model supports
- Example: `--params '{"top_k": 50, "seed": 42, "frequency_penalty": 0.5}'`

`--timeout` (optional)
- Request timeout in seconds (default: 120)

**Examples:**

Simple call:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-sonnet-4" \
  --input "Write a haiku about coding" \
  --temperature 0.8
```

With system instructions:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-haiku-4.5" \
  --input "Explain recursion" \
  --instructions "You are a helpful programming tutor. Keep explanations concise."
```

With reasoning (for o1-style models):
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "openai/o1" \
  --input "Solve this complex math problem" \
  --reasoning high
```

With web search:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-sonnet-4" \
  --input "What are the latest AI news?" \
  --web-search 10 \
  --max-tokens 15000
```

With extra model-specific params:
```bash
# Step 1: Check what params the model supports
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "meta-llama/llama-3.3-70b-instruct"
# Shows: frequency_penalty, top_k, seed, min_p, etc.

# Step 2: Call with those params
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "meta-llama/llama-3.3-70b-instruct" \
  --input "Write a short poem" \
  --params '{"top_k": 50, "seed": 42, "frequency_penalty": 0.5}'
```

---

## Tips

- Use `aii_or_search_llms.py` first to find models, then copy `API` field for `--model`
- Use `aii_or_get_llm_params.py` to check what params a model supports before using `--params`
- For web search, increase `--max-tokens` to handle larger responses (15000+)

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-long-running-tasks · 2026-06-17 15:50:07 UTC

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

### [6] SYSTEM-USER prompt · 2026-06-17 16:43:20 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx3
type: experiment
title: >-
  Real-LLM Matched-Coverage Baseline Showdown on the Synthetic QCN Backbone (H1, with H3/zero-FP audit)
summary: >-
  Run REAL OpenRouter LLM reads over the synthetic QCN NL realizations (point + Allen primary, RCC-8 optional), feed the disjunctive
  local reads into the validated FULL-PC / NAIVE / OFF engine, and execute every enumerated baseline (raw LLM, CoT, self-consistency,
  LINC, Path-of-Thoughts, ILP-commit, naive single-pass) at MATCHED COVERAGE using a shared single-relation coverage object.
  Headline H1: Mode-A (FULL closure over disjunctive reads) achieves strictly higher selective accuracy at matched coverage
  than Path-of-Thoughts AND self-consistency, with paired-bootstrap Holm-Bonferroni-adjusted CIs. Secondary: full-minus-naive
  iteration gap vs hop/cyclomatic (H3 on synthetic), Mode-A vs OFF (C2), and a read-soundness/J(E) audit. Every number tagged
  REAL-LLM-READ-ON-SYNTHETIC. Heavy reuse of iter-1 gen_art_experiment_3 assets (engine.py, llm.py, method.py prompt+bootstrap
  helpers); spend held well under $10 via SHA-256 caching of entity-normalized edge reads and a hard cost guard.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  # ============================================================================
  # EXPERIMENT experiment_iter2_dir3 -- REAL-LLM matched-coverage baseline showdown
  # on the SYNTHETIC QCN backbone. Output: method_out.json (aii-json validated).
  # Compute: CPU only (LLM calls are async API I/O; closure/ILP are millisecond).
  # Budget: HARD cap $9 OpenRouter, soft warn $2; track client.cost after every call.
  # ============================================================================
  #
  # ---------- 0. REUSE MAP (copy these files into the workspace, do NOT re-derive) ----------
  # DATASET (dep art_ghVQmxVlmOJJ):
  #   DS = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2
  #   data: DS/full_data_out/full_data_out_1.json + full_data_out_2.json
  #         (each <100MB; reconstruct by CONCATENATING datasets sharing the same
  #          'dataset' name across the two parts). DS/mini_data_out.json (3/algebra),
  #          DS/preview_data_out.json (10/algebra) for smoke tests.
  #   tables: DS/qcn/algebra_tables/{Linear_Point_Algebra,Linear_Interval_Algebra,RCC8_Algebra}.json
  #   algebra pkg (for RCC-8 only): DS/qcn/algebras.py (load_algebras(), compose_sets, intersect, converse_set)
  # ENGINE (referenced art_K7riobQ_Rmwz / found in gen_art_experiment_3):
  #   ENG = .../gen_art/gen_art_experiment_3/engine.py
  #     build_point_algebra(), build_allen_algebra()  (point + Allen ONLY, no RCC-8)
  #     class QCN(alg, nodes): set_edge(i,j,frozenset), get(i,j), known_edges()
  #     pc2_full(qcn) -> (consistent:bool, n_fired); read closed query rel from qcn.get(s,t) AFTER
  #     naive_single_pass(qcn, u, v) -> frozenset  (single pass, no fixpoint = PoT+1 step)
  #     close_triangle(alg, ab, bc, ac) -> {path, inter, empty, singleton, n_widen}
  #     alg.widen(s)->(s',fired) applies the point convex {<,>}->universe rule (COUNT widenings)
  # LLM CLIENT + PROMPT (art_glhgFsBUrcYo / gen_art_experiment_3):
  #   LLM = .../gen_art_experiment_3/llm.py : OpenRouterClient(api_key, model, fallbacks, cache_dir,...)
  #         attrs .cost .n_calls .n_cache_hits .n_errors ; SHA-256 disk cache; hard budget guard.
  #         parse_relations(content, vocab) -> (coarse_set, underdetermined_bool, parse_fail_bool)
  #   MET = .../gen_art_experiment_3/method.py : KNOB / KNOB_ORDER (S1_single..S5_maximal breadth knob),
  #         build_prompt(task, knob) (marked [[E1]]..[[/E1]] + JSON {relations:[...],underdetermined:bool}),
  #         clustered_bootstrap_ci(doc_to_vals,...) (resamples DOCS for rho), icc_oneway(groups) (rho via ICC).
  #         pre-reg constants: MODEL_PRIMARY='google/gemini-3.1-flash-lite',
  #         MODEL_FALLBACKS=['deepseek/deepseek-v3.2','deepseek/deepseek-v4-flash'], TEMPERATURE=0.0,
  #         RECALL_GATE_POINT=0.90, RECALL_GATE_ALLEN=0.85, APPLIC_GENERAL=0.10, BUDGET_USD_HARD=9.0
  #   STATS (reuse from gen_art_experiment_2/method.py): boot_diff_ci, page_test, jonckheere, spearman_boot_ci
  # DOSSIER (dep art_aQ2Rf8rwqteI): .../gen_art_research_1/research_out.json -- baseline configs,
  #   ILP-commit (Eirew M=5), LINC, PoT, model arithmetic, gotchas. READ before coding baselines.
  # NOTE: verify model id with aii-openrouter-llms skill at runtime (gemini-2.5-flash-lite was
  #   RETIRED; iter-1 used google/gemini-3.1-flash-lite). If primary gone, pick cheapest capable
  #   instruct model from the skill and record model_used in output.
  #
  # ---------- 1. LOAD + SUBSET THE SYNTHETIC DATA ----------
  # Reconstruct each of the 3 datasets (synthetic_qcn_point, synthetic_qcn_allen, synthetic_qcn_rcc8)
  # by merging the same-named dataset across full_data_out_1.json and _2.json.
  # Parse per row: input (NL realization), output JSON -> {edges:[{source,target,relation}], query_edge},
  #   metadata_fold, metadata_algebra, metadata_cell.cell_id, metadata_query{source,target,relation},
  #   metadata_structure{cyclomatic_number, num_simple_paths_s_t, contributing_edge_count, num_nodes},
  #   metadata_paths{path_list, path_compositions, naive_intersection, has_bite, singleton_resolved},
  #   metadata_entity_map (node_idx -> entity phrase),
  #   metadata_reference_disjunctive_labels (SOUND superset per edge -> used ONLY to MEASURE recall, never as the read).
  # COMPARISON STRATA (cells where Mode-A has bite & baselines are meaningful):
  #   redundancy axis: red_P1_L2,red_P2_L2,red_P3_L2,red_P4_L2,red_P6_L2,red_P8_L2  (singleton_resolved 0.4->0.89)
  #   hop axis:        hop_L2_P2,hop_L3_P2,hop_L4_P2,hop_L5_P2
  #   cyclomatic axis: cyc_mu0,cyc_mu1,cyc_mu2,cyc_mu3                              (iteration / H3)
  # PRIMARY algebras = point (PC COMPLETE, 3 relations, exact) + allen (13 rels, LOWER BOUND).
  #   point is the CLEAN headline arm; allen is the generality arm. RCC-8 = OPTIONAL Tier-2.
  # Use FOLD discipline: dev fold (md5%100 in 10..29) to fix the operating point + sanity;
  #   test fold (>=30) for the REPORTED H1 numbers (never tune on test).
  # Sampling: N_PER_CELL networks/cell (start dev pilot ~10; full test ~60-100). Stratified, deterministic
  #   (sort test rows by metadata_seed, take first N). Record exactly which rows were used.
  #
  # ---------- 2. NEURAL READING (the disjunctive local reads = the SHARED substrate) ----------
  # Operating point = the breadth knob that clears the recall gate. Reuse the frontier finding:
  #   iter-1 synthetic clean text had recall ~0.96; default OPERATING_KNOB='S4_sound'. On the dev
  #   fold, sweep {S3_plausible,S4_sound,S5_maximal} on a small sample, MEASURE per-edge recall vs
  #   the gold atom, and PICK the cheapest knob with recall>=RECALL_GATE (0.90 point / 0.85 allen).
  #   Freeze OPERATING_KNOB before the test-fold run.
  # Build a SYNTHETIC read prompt (variant of MET.build_prompt) presenting the NATIVE algebra vocab:
  #   point: '<' (E1 before E2), '=' (same time), '>' (E1 after E2).
  #   allen: the 13 base relations each with a one-line endpoint definition (b,bi,m,mi,o,oi,d,di,s,si,f,fi,eq).
  #   rcc8 (opt): DC,EC,PO,EQ,TPP,NTPP,TPPi,NTPPi each defined.
  #   System: 'Read ONLY from this sentence; do NOT assume consistency with other pairs.' + KNOB[knob].
  #   Output JSON {"relations":[...],"underdetermined":bool}. Reuse LLM.parse_relations (extend its
  #   vocab to the native base sets) to get the emitted frozenset.
  # READ EACH NON-QUERY EDGE LOCALLY:
  #   for edge (u,v) in output.edges:
  #       sent = the input sentence mentioning BOTH entity_map[u] and entity_map[v] (unique per network;
  #              match by substring of the two entity phrases). Mark them E1=u, E2=v.
  #       NORMALIZE for caching: replace entity_map[u]->'E1', entity_map[v]->'E2' in sent; cache key =
  #              sha256(normalized_sent + '|' + knob + '|' + algebra). -> near-100% cache hits across
  #              networks (read is entity-agnostic & local), making edge reads ~free.
  #       emitted_uv = parse(LLM(system,user))  # sound disjunctive set, oriented u->v
  #       POINT widening: if emitted_uv=={'<','>'} -> universe, COUNT bite_lost (convexity guard).
  #       store read[(u,v)] = emitted_uv ; read[(v,u)] = alg.converse(emitted_uv)  # converse from ALGEBRA
  #   Run reads CONCURRENTLY (async, ~16-32 in flight) via the reused client; check client.cost each batch.
  # RECORD per-edge soundness vs gold: sound_uv = (gold_atom(u,v) in emitted_uv); recall = mean(sound_uv);
  #   breadth = |emitted_uv|; over_commit = not sound_uv; also store doc-id (network) for rho/ICC.
  #
  # ---------- 3. METHOD + SYMBOLIC VARIANTS (free, no LLM) over the SAME reads ----------
  # Build QCN from reads: nodes=range(num_nodes); for each non-query edge set_edge(u,v,read[(u,v)]);
  #   query edge (s,t) left at universe.
  # MODE-A (FULL, our method):
  #   q = QCN(...); set all read edges; consistent,_ = pc2_full(q); rq = q.get(s,t)
  #   if not consistent (empty anywhere) -> ModeB_DETECT (abstain, collapse-certificate)
  #   elif |rq|==1 -> answer=rq.single ; covered=True   # singleton-resolution
  #   else -> abstain (rq still disjunctive)
  # NAIVE single-pass (iteration contrast): rn = naive_single_pass(q_reads, s, t)  # NO fixpoint
  #   covered iff |rn|==1; answer=rn.single.   (coincides w/ FULL on length-2; diverges hop>=3/cyclic)
  # OFF (no composition floor): query edge never locally readable -> always abstain (coverage 0);
  #   report as the deduction-required gap (echoes iter-1 local-read 26.7%).
  # correctness for any variant: covered & (answer == gold_query).
  #
  # ---------- 4. NEURAL BASELINES (full-document; each emits prediction + abstention SCORE) ----------
  # All baselines see the SAME document = the full NL realization (all edge sentences + Query line).
  # The query relation is NEVER stated (deduction-required), so every method must DEDUCE it.
  # Define the coarse/native answer vocab = algebra base relations (point 3 / allen 13).
  # (b1) RAW LLM  [HEADLINE-supporting]: 'Give THE single relation of {Es}->{Et}; also output confidence 0-1.'
  #        temp=0.0; conf = verbalized confidence. 1 call/net.
  # (b2) CoT: same but 'reason step by step, then give the single relation + confidence.' 1 call/net.
  # (b3) SELF-CONSISTENCY (vote margin) [H1 GATEWAY baseline]: K=5 CoT samples temp=0.7;
  #        answer = majority relation; conf = (top_votes - second_votes)/K. 5 calls/net.
  # (b4) LINC-style multi-formalization vote [lightweight]: M=3 prompts that translate the doc to a
  #        single-label relation set per pair then read off the query (committed, single-label per edge),
  #        majority-vote the query answer; conf = agreement fraction. 3 calls/net.
  # (b5) PATH-OF-THOUGHTS [PRIMARY H1 baseline, run faithfully]: (i) one graph-extraction call OR reuse
  #        the per-edge reads as the extracted graph; (ii) enumerate s-t paths (cap PATHS<=6 by
  #        num_simple_paths; log truncation); (iii) for EACH path, ONE LLM call reasoning that path's
  #        chained relations to a SINGLE query relation INDEPENDENTLY (no cross-path intersection);
  #        (iv) aggregate by agreement: answer=majority across paths, conf=path-agreement fraction
  #        (abstain when paths disagree). This is exactly the cross-path-intersection gap Mode-A fills.
  # (b6) ILP-COMMIT (Eirew M=5) [lightweight]: take the disjunctive reads (or M=5 single-label reads),
  #        solve a small ILP over the subnetwork induced by edges on s-t paths: binary x[e,r],
  #        sum_r x[e,r]=1 (uniqueness), transitivity constraints from the composition table on triples,
  #        maximize total read-confidence; read committed query relation; conf = solver objective margin
  #        (or fraction of M=5 agreeing). Use PuLP+CBC (pip). KEEP SMALL (path-induced subgraph only).
  # (b7) NAIVE single-pass = symbolic baseline from step 3 (no extra LLM).
  # COST CONTROL: cache every prompt by sha256(messages+model+temp+sample_idx). Self-consistency
  #   samples keyed by idx. Project cost before the full run; if >budget, cut in priority order:
  #   drop ILP/LINC first, then reduce K (5->3), then reduce N_PER_CELL. NEVER drop PoT or SC.
  #
  # ---------- 5. MATCHED-COVERAGE SELECTIVE COMPARISON (the H1 statistic) ----------
  # Coverage OBJECT = single-relation resolution (identical for all methods).
  # For each network n and method m: have correct_m[n] in {0,1}, covered/conf.
  # Target coverage c* = Mode-A coverage = mean(Mode-A covered).   # structural, fixed
  # For each baseline b with continuous conf:
  #   choose tau_b so fraction(conf_b >= tau_b) == c* (interpolate on the sorted conf grid);
  #   covered_b[n] = conf_b[n] >= tau_b ; selacc_b = sum(correct_b*covered_b)/sum(covered_b).
  # selacc_ModeA = sum(correct_A*covered_A)/sum(covered_A).
  # gap_b = selacc_ModeA - selacc_b.
  # PAIRED BOOTSTRAP (B=2000): resample NETWORK indices with replacement (shared across methods =
  #   paired); recompute selacc_ModeA and selacc_b at FIXED tau_b each resample; collect gap*; 95% CI.
  #   (sensitivity: also report a re-matched-tau-per-resample variant.)
  # Also compute and store FULL risk-coverage curves (sweep tau over a grid) for each method, for figures.
  # MULTIPLICITY: confirmatory H1 family = {Mode-A vs PoT, Mode-A vs self-consistency}. Apply
  #   Holm-Bonferroni across the family; report ADJUSTED CIs. PASS_H1 = both adjusted CIs exclude 0
  #   on the positive side. Report raw LLM/CoT/LINC/ILP/naive gaps too (labelled exploratory, nominal CIs).
  # STRATIFY everything by algebra, redundancy P, hop L, cyclomatic mu; report per-stratum gaps.
  #   Headline pooled over the bite-bearing strata (P>=2 redundancy + low-hop). Predicted: Mode-A TIES
  #   naive on length-2 (report tie as confirmation), > PoT/SC across.
  #
  # ---------- 6. SECONDARY ANALYSES (tag each) ----------
  # H3 ITERATION (synthetic): full_correct - naive_correct accuracy gap per hop L (hop_L*) and per
  #   cyclomatic mu (cyc_mu*); monotone-trend (Page/Jonckheere/Spearman-boot, reuse exp_2 fns).
  #   Predicted: ~0 at L=2, GROWS with L and mu. (Mirrors iter-1 simulated channel but now REAL reads.)
  # C2 closure ON vs OFF: Mode-A coverage/accuracy vs OFF (=0) -> quantifies deduction-required gap.
  # READ-SOUNDNESS / ZERO-FP AUDIT (REAL-LLM-READ-ON-SYNTHETIC): per-edge recall; J(E)=fraction of
  #   networks where ALL contributing edges sound (group by contributing_edge_count); silent-wrong rate
  #   = covered & wrong & query-set-omits-gold; reliability: among all-sound networks, fraction whose
  #   Mode-A set still CONTAINS gold (should be ~1.0 = zero-FP-conditional-on-soundness). Report
  #   within-document cross-edge soundness correlation rho via icc_oneway. Compare the real-read
  #   per-edge error-type distribution to iter-1's simulated channel (TV distance) -- informational.
  # WORKED EXAMPLE: dump one network's full trace (reads, which compositions fired on which paths,
  #   the narrowed query set) as a human-auditable trace-graph (Mode-A narrowing path + a Mode-B collapse).
  #
  # ---------- 7. OUTPUT method_out.json (aii-json validated) ----------
  # Use the aii-json skill to find/validate the experiment solution-output schema (iter-1 used
  #   'exp_gen_sol_out'); conform to it. Include:
  #   metadata: {model_primary, model_used, fallbacks, temperature, operating_knob, recall_gates,
  #              folds_used, n_networks_per_cell, seed, EVIDENCE_TAG:'REAL-LLM-READ-ON-SYNTHETIC'}
  #   leaderboard: per method {coverage, selective_accuracy_at_matched_cov, singleton_resolution_to_correct,
  #              strict_tightening (non-load-bearing), gap_vs_ModeA, ci, adjusted_ci}
  #   per_stratum: gaps by (algebra,P,L,mu)
  #   H1: {target_coverage, gap_PoT, gap_SC, holm_adjusted_cis, PASS:bool}
  #   H3: {gap_by_hop, gap_by_cyclo, trend tests, length2_tie}
  #   audit: {per_edge_recall, J_E_by_E, silent_wrong_rate, zero_fp_contains_gold_rate, rho_icc, tv_vs_sim_channel}
  #   cost: {cumulative_openrouter_usd, n_llm_calls, cache_hits}
  #   worked_example, verdict (PASS/FAIL H1 on synthetic + honest scope note).
  # Generate mini/preview variants if the file is large; run aii-file-size-limit check.
fallback_plan: |-
  MODEL: if 'google/gemini-3.1-flash-lite' is retired, query aii-openrouter-llms for the cheapest capable instruct model (try deepseek/deepseek-v3.2, then a small Gemini/Llama-3.3-70B) and record model_used; the cached client already supports a fallback list. If the chosen model's verbalized confidence is uninformative for raw/CoT, substitute token-logprob or self-consistency margin as the abstention score and note it.

  BUDGET: project cost on the dev pilot (cost-per-network x planned N). If it would exceed ~$8, cut in this fixed priority order WITHOUT touching the H1 gateways: (1) drop ILP-commit and LINC (the dossier itself calls them lightweight/optional), (2) reduce self-consistency K 5->3, (3) cap PoT paths to 4, (4) reduce N_PER_CELL, (5) restrict to the POINT algebra headline only. Always keep Mode-A, PoT, self-consistency, naive, raw on >=1 fully-powered arm. Entity-normalized read caching should already make edge reads ~free; if not, cache aggressively and dedupe.

  ALLEN READS WEAK: if the 13-relation read recall stays below RECALL_GATE_ALLEN (0.85) even at S4/S5 (LLM struggles to enumerate 13 Allen relations), fall back to (a) the coarse 5-relation interval vocab used by the iter-1 real-text arm (before/after/simultaneous/includes/is_included) mapped to a coarse interval algebra, or (b) make POINT the sole headline arm (3 relations, recall ~0.96, PC-complete, exact) and report Allen as exploratory/lower-bound. Point alone is a sufficient, clean H1 venue.

  ENGINE/CLIENT IMPORT FAILS: engine.py and llm.py are self-contained iter-1 files -- copy them into the workspace. If they cannot be imported, reimplement: (closure) from the dossier's Mackworth PC-2 pseudocode + the DS/qcn/algebra_tables/*.json composition/converse tables (point/allen/rcc8 all present, 436-check verified); (client) a thin async OpenRouter wrapper from the aii-openrouter-llms skill with a SHA-256 disk cache + a running-cost guard that raises before exceeding $9. RCC-8 has no built-in engine algebra: build an Algebra from DS/qcn/algebras.py load_algebras()['rcc8'] (it exposes compose_sets/intersect/converse_set) and write a tiny PC-2 over it, or skip RCC-8 (optional).

  ILP SOLVER MISSING: if PuLP/CBC is unavailable, implement ILP-commit as greedy most-confident-singleton-per-edge + transitivity repair over the path-induced subgraph, or drop it (optional baseline).

  H1 NEGATIVE: if Mode-A does NOT beat PoT and self-consistency even on synthetic where reads are recall~0.96 (a surprising result), report it honestly as a REAL-LLM-ON-SYNTHETIC negative, keep the H3 iteration gap, the zero-FP/J(E) audit, and the OFF-gap (deduction-required) findings, and flag for the paper that the synthetic mechanism advantage is contingent (feeds the NeSy/findings retarget the hypothesis already pre-registers). Diagnose WHY (e.g., PoT also composes correctly when reads are near-perfect; the Mode-A edge should appear most where reads are noisier or paths longer -- check the hop/cyclomatic strata and any reader-degradation arm).

  LOW POWER IN A STRATUM: deduction-required coverage collapses at L>=4/L5 (singleton_resolved ~0.01-0.04). Pool the headline over bite-bearing strata (P>=2, L=2-3, cyc) and report sparse strata descriptively only; do not gate H1 on an under-powered cell.
testing_plan: |-
  Follow the aii-long-running-tasks gradual-scaling pattern; never launch the full paid run before the confirmation signals below fire.

  STAGE 0 -- wiring & engine (zero spend). Copy engine.py, llm.py, and the needed helpers from gen_art_experiment_3 (+ exp_2 stats fns). Import build_point_algebra/build_allen_algebra, run the iter-1 engine unit checks (closure_tests_pass / the __main__ spot prints: ALLEN B o B, POINT '<' o '>' == universe). Add OWN sanity asserts: (a) feed the GOLD atomic reads of a mini network into the QCN, run pc2_full, assert q.get(s,t) == {gold_query} (pipeline wired right; closure recovers gold from sound singletons); (b) on a length-2 example assert naive_single_pass == pc2_full result (the predicted tie); (c) on a length-3 chain assert FULL narrows where NAIVE abstains (engine docstring example). Confirm point convexity widening fires & is counted for {'<','>'}.

  STAGE 0b -- model + cache round-trip (tiny spend, <$0.01). Instantiate OpenRouterClient; send one read prompt; resend identical -> assert the 2nd is a cache hit and client.cost unchanged; assert parse_relations returns a valid frozenset for the native vocab. Verify the entity-normalization cache key dedupes two networks that share a relation phrasing.

  STAGE 1 -- end-to-end mini (<$0.10). Run the WHOLE pipeline (reads -> QCN -> Mode-A/naive/OFF -> all baselines -> matched-coverage -> method_out skeleton) on DS/mini_data_out.json (3/algebra) then ~5 networks/cell from the DEV fold, point algebra first. Assert: no crashes; cost logged; method_out validates against the aii-json schema; PoT/SC produce predictions+conf.

  STAGE 2 -- DEV-fold pilot + CONFIRMATION SIGNALS (a few hundred reads, <$0.50). On ~10 networks/cell (dev), point + allen:
    * SIGNAL 1 (reads work): per-edge recall at the operating knob >= RECALL_GATE (>=0.90 point / >=0.85 allen), echoing iter-1's ~0.96 on synthetic clean text. If not, invoke the Allen/operating-knob fallback BEFORE scaling.
    * SIGNAL 2 (mechanism alive): Mode-A singleton-resolution-to-correct > 0 and tracks the metadata singleton_resolved_frac ordering (rises with redundancy P: red_P1<red_P4<red_P8).
    * SIGNAL 3 (machinery sane): matched-coverage gaps are finite, coverage matches across methods at c*, paired-bootstrap CIs computed, Holm adjustment runs.
    Freeze the operating knob now. Project full-run cost from measured cost/network.

  STAGE 3 -- TEST-fold full run (the reported numbers). Scale N_PER_CELL to the budget-feasible max (target ~60-100/cell). Run async with the hard $9 cost guard; checkpoint reads/results to disk (resumable). Monitor client.cost each batch; if approaching budget, apply the fallback cut order. Compute H1 (Holm-adjusted), H3, C2, the zero-FP/J(E) audit, the worked example. Tag every number REAL-LLM-READ-ON-SYNTHETIC. Validate the final method_out.json with aii-json and run the aii-file-size-limit check (emit mini/preview variants if oversized). Cross-check: the OFF arm coverage is ~0 (no direct query read); Mode-A ties naive on the L=2 stratum; full-minus-naive gap grows with L/mu.
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

### [7] SYSTEM-USER prompt · 2026-06-17 16:44:30 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [8] SKILL-INPUT — aii-file-size-limit · 2026-06-17 17:07:25 UTC

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
