# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 8 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 04:09:52 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx2
type: experiment
title: >-
  iter-8 decisive test: closure certificate vs 4-signal battery vs query-side false-premise verifier on the natural located-in
  corpus (same-component-sibling mixed pool)
summary: >-
  Re-run the iter-7 STEP-B natural-corpus experiment VERBATIM-by-reuse on a SECOND genuinely-natural absent-relation domain
  (Re-DocRED geographic/administrative containment, art_RfjDpsGkBXDG), parameterizing the kinship.py forward-union engine
  with the degenerate transitive containment table. Deliver (i) FACT A on located-in (raw-LLM high-confidence located_in/contains
  fabrication rate on absent pairs, both readers), (ii) per-signal x reader crux-survival WITH fraction-caught, (iii) the
  signal-agnostic MIXED-POOL CAPABILITY GAP newly powered on the NON-structural-by-construction same_component_sibling regime,
  (iv) Holm-adjusted doc-clustered confident-wrong reductions of the certificate vs each of the 4 dispersion signals AND a
  NEW query-side false-premise verifier + self-verification baseline, plus the structural-by-construction different_component
  CONTRAST, the gold-read ceiling that isolates extraction, and the pre-registered FORK verdict (DEMONSTRATED-FIX | EXTRACTION-LIMITED-BOUNDARY
  | DIAGNOSTIC-WEAKER-THAN-CLAIMED | VERIFIER-SUFFICES). All reads REAL-LLM (OpenRouter, SHA-256 cached, hard $9 cap); gradual
  mini->full.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  ############################################################################
  # OVERVIEW
  # This is a DROP-IN ADAPTATION of the iter-7 STEP-B template (the natural-
  # kinship Re-DocRED run, art_htcr8yOZLCQy) to the iter-7 located-in corpus
  # (art_RfjDpsGkBXDG). REUSE the iter-7 code VERBATIM where possible; the ONLY
  # new substance is (a) located-in field/prompt adaptations, (b) the held_out
  # direct-edge ABLATION, (c) the absent-REGIME split (same_component_sibling vs
  # different_component), and (d) the NEW query-side false-premise verifier +
  # self-verification baselines. Every battery/stats/closure function is reused.
  #
  # SOURCE WORKSPACES (read-only; copy the .py files into THIS workspace):
  #   TEMPLATE_EXP = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1
  #       -> method.py (orchestrator template), dataio_redocred.py (loader+grounding),
  #          readers.py (prompts/parsers), kinship.py (forward-union engine = REUSE VERBATIM),
  #          baselines.py (predict_symbolic, matched_coverage_showdown, absent_h2,
  #                        confident_wrong, coverage_confidence, story_atomic_pr,
  #                        aggregate_atomic_pr = REUSE VERBATIM),
  #          stats.py (holm_bonferroni, matched_coverage_mask, selective_accuracy = REUSE VERBATIM),
  #          llm.py (OpenRouterClient: SHA-256 disk cache, budget_hard cap = REUSE VERBATIM),
  #          prolog.py (discharge() = REUSE VERBATIM).
  #   DATASET = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/full_data_out.json
  #       (one row per doc; datasets=[{dataset:'re-docred',examples}, {dataset:'docred',examples}];
  #        each ex.output = json.dumps(gold_graph); top metadata.composition_table = the
  #        DEGENERATE containment table -> feed straight into Kinship(...).)
  #   RESEARCH = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_research_1/research_out.json
  #       (art_dA_3iFe_7fn_: false-premise lit FalseQA/AbstentionBench/Wen2024 framing +
  #        the 4 confidence-signal specs; read for the verifier wording + citations note.)
  #   The corpus's OWN containment_composition_table.json also lives in the dataset dir,
  #   but PREFER full['metadata']['composition_table'] (emitted verbatim) so Kinship is
  #   parameterized from the exact table the corpus was verified against.
  ############################################################################

  # ---------------------------------------------------------------------------
  # STAGE 0 -- workspace setup (pyproject.toml: numpy, scipy, loguru, httpx; uv venv)
  # ---------------------------------------------------------------------------
  #  - cp kinship.py, baselines.py, stats.py, llm.py, prolog.py from TEMPLATE_EXP VERBATIM.
  #  - Author dataio_locatedin.py (adapt dataio_redocred.py), readers_locatedin.py
  #    (adapt readers.py), queryside.py (NEW), method.py (adapt the iter-7 orchestrator).
  #  - kin = Kinship(full['metadata']['composition_table'])  # base types = ['located_in','contains']
  #    sanity: kin.compose_types('located_in','located_in')=='located_in';
  #            kin.compose_types('located_in','contains') is None (=> siblings derive EMPTY);
  #            kin.conv_type('located_in')=='contains'.

  # ---------------------------------------------------------------------------
  # STAGE 1 -- dataio_locatedin.py  (loader + grounding + the THREE adaptations)
  # ---------------------------------------------------------------------------
  # The located-in gold_graph fields (verified from the corpus):
  #   nodes:               {entity_id, surface, type='LOC', admin_level, mention_spans:[[cs,ce],...]}  (NO gender)
  #   atomic_edges:        {source, target, primitive='located_in', relation_type, relation_surface='located in',
  #                         is_query=false, hop_count=1, support_span, locally_justifiable(bool, if present)}
  #   query_edges:         {source, target, primitive='located_in', hop_count(>=2), derivation_path, is_query=true,
  #                         composed_only(bool)}   # composed_only=True  => never_annotated (no direct edge)
  #                                                # composed_only=False => held_out (a redundant direct edge EXISTS)
  #   absent_relation_pairs:{source, target, reason, is_absent=true, same_component(bool)}
  #                         # reason in {'different_component','same_component_sibling'}
  #
  # REUSE dataio_redocred.py's load_slice / build_doc_context / ground_name / id_path_to_names
  # VERBATIM (build_doc_context already defaults gender='male'; located_in surface is
  # gender-independent so this is harmless). _atomics_to_id_edges already reads
  # source/target/primitive/locally_justifiable -> works unchanged.
  #
  # CHANGE 1 (held_out ABLATION) -- the single most important new rule. The corpus
  # engine_edge_mapping states verbatim: 'For a held_out query, FIRST drop the single
  # atomic edge whose (source,target)==(query source,target) before querying.' Implement:
  #   def closure_edges_drop_direct(edges, qsrc, qtgt):
  #       return [e for e in edges if not ({e['a'],e['b']}=={qsrc,qtgt})]   # drops edge + its converse seed
  #   In make_present_record(ctx,q,...):
  #       full_atomics = _atomics_to_id_edges(gg)
  #       r['gold_atomics']      = closure_edges_drop_direct(full_atomics, qsrc, qtgt)   # ALWAYS drop direct
  #       r['gold_atomics_just'] = closure_edges_drop_direct(_atomics_to_id_edges(gg,justifiable_only=True), qsrc, qtgt)
  #       r['composed_only']     = bool(q.get('composed_only', False))
  #       r['query_subtype']     = 'never_annotated' if r['composed_only'] else 'held_out'
  #       (never_annotated has no direct edge so the drop is a no-op there; held_out forces deduction
  #        via the alternative >=2-hop path -- this is what makes PRESENT coverage a genuine deductive result.)
  #   ALSO drop the direct edge from the LLM-EXTRACTED graph at query time (symmetry; see STAGE 2)
  #   so a held_out 'covered' decision is a real derivation, not a read-back. Record BOTH the
  #   ablated present-coverage (PRIMARY) and the un-ablated coverage (sensitivity) for honesty.
  #
  # CHANGE 2 (absent REGIME tag) -- decisive for the headline:
  #   In make_absent_record(ctx,p,...):
  #       reason = p.get('reason') or ('same_component_sibling' if p.get('same_component') else 'different_component')
  #       r['absent_regime'] = 'same_component_sibling' if 'sibling' in reason or p.get('same_component') else 'different_component'
  #   (Keep gold_surface='no-relation', is_absent=True, hop=0 as in the template.)
  #
  # CHANGE 3 (gold primitive / surface) -- located_in is gender-free:
  #   gold_prim='located_in'; gold_word=kin.surface('located_in','male')=='located in'. No kinship_relation field.
  #
  # CHANGE 4 (STRATIFIED SUBSAMPLE for cost) -- the corpus is huge (re-docred 3,510 present /
  #   24,088 absent of which 20,814 sibling). Build records, then subsample to a budget-safe,
  #   strata-BALANCED working set BEFORE any LLM call, doc-clustered (keep whole docs):
  #     target ~ {present held_out: 400, present never_annotated: ALL 118, sibling-absent: 450,
  #               diffcomponent-absent: 250}, drawn by ascending doc_id for determinism, with a
  #     per-doc query cap (e.g. <=6 present, <=6 sibling, <=4 diffcomp) so dense geography docs
  #     cannot dominate. Tunable via --limit-docs / per-stratum caps. Log the realized counts.
  #   (Whole-doc clustering matters: extraction is one call shared by a doc's queries.)

  # ---------------------------------------------------------------------------
  # STAGE 2 -- readers_locatedin.py  (located-in prompts/parsers, adapted from readers.py)
  # ---------------------------------------------------------------------------
  # Replace the kinship surface vocabulary with the containment vocabulary:
  #   CANON_SURFACES = ['located in','contains']; _NO_REL as in template (+'unrelated','no containment').
  #   normalize_surface(w): map 'located in'/'part of'/'in'/'within'/'a city in'/'subdivision of' -> 'located_in'
  #     surface 'located in'; 'contains'/'includes'/'has ... within it' -> 'contains'; no-relation words -> 'no-relation'.
  #     (Return the canonical SURFACE string; kin.surface_to_type maps 'located in'->located_in.)
  #   EXTRACTION prompt (extraction_item): 'Extract every DIRECTLY-STATED geographic/administrative
  #     containment between two named places. Output JSON {"relations":[{"a":<place>,"relation":"located in"|"contains","b":<place>}]}.
  #     a located in b means a is inside/part of/an administrative subdivision of b. Only directly stated
  #     pairs; do NOT infer transitive containment.' (max_tokens 700.) parse_extraction reused (it calls
  #     normalize_surface + kin.surface_to_type) -> works once the vocab is swapped.
  #   RAW query prompt (raw_query_item): 'Question: What is the geographic relationship of <X> to <Y>?
  #     Answer JSON {"relation":"located in"|"contains"|"no-relation","confidence":0..1}. "located in" means
  #     X is inside Y; "contains" means X contains Y; "no-relation" if neither place is inside the other.'
  #   PoT prompt (pot_item): compose a chain of places -> containment of last to first; same JSON.
  #   BEST-EFFORT extraction arm (PATH 2 hedge): a second extraction variant with 2-3 few-shot
  #     examples + the doc's place inventory (reuse template's --given-inventory _inventory_user) under
  #     prompt tag 'extract_best'; ground both, run the certificate on EACH, report present coverage /
  #     atomic recall for default vs best-effort so the positive fork gets its fair shot.
  #   parse_raw / aggregate_sc / aggregate_pot reused VERBATIM (they only depend on normalize_surface).
  # AT QUERY TIME, for held_out present queries, also drop the direct edge from the grounded extracted
  #   graph before predict_symbolic: edges_q = closure_edges_drop_direct(grounded[did], qsrc, qtgt).

  # ---------------------------------------------------------------------------
  # STAGE 2b -- queryside.py  (THE NEW BASELINE the certificate must MATCH or BEAT)
  # ---------------------------------------------------------------------------
  # (1) QUERY-SIDE FALSE-PREMISE VERIFIER ('are these related at all?') -- the established method
  #     for this failure mode (research dossier art_dA_3iFe_7fn_: FalseQA/AbstentionBench/Wen2024).
  #   verifier_item(story,Xname,Yname): system='You decide whether a presupposed geographic relation
  #     exists. Output JSON {"related":true|false,"confidence":0..1}.'; user='Story:...\n Based ONLY on the
  #     document, is <X> located in <Y>, OR does <X> contain <Y> (i.e. is there any containment between
  #     them in EITHER direction)? related=false if neither is inside the other.' (1 call, temp 0).
  #   parse_verifier -> {related:bool, conf:float}.
  #   METHOD DICT predict_queryside_verifier: when related==True -> named=True, surface = the raw
  #     answerer's committed primitive (r['raw']['surface'] after primitivize), conf = verifier conf;
  #     when related==False -> named=False (abstain), conf = 1-verifier_conf. (i.e. the verifier GATES
  #     the committed answer by a dedicated relatedness check.)
  # (2) SELF-VERIFICATION pass on the raw committed answer:
  #   selfverify_item(story,Xname,Yname,proposed): 'Is this proposed answer correct given the document?
  #     Output JSON {"correct":true|false,"confidence":0..1}.' (1 call, temp 0).
  #   METHOD DICT predict_queryside_selfverify: named = r['raw']['named'] AND correct==True; surface =
  #     raw surface; conf = self-verify confidence (used for matched-coverage thresholding).
  # Both produce {surface,conf,named} dicts identical in shape to ct_<signal>, so they plug straight
  #   into matched_coverage_showdown (add to its `baselines` tuple), cw_matched_to_ref, and the Holm
  #   family. Add to _METHOD_KEYS so primitivize() canonicalizes their surfaces.
  # COST: +2 calls/query (verifier + selfverify), both cached.

  # ---------------------------------------------------------------------------
  # STAGE 3 -- method.py orchestration (adapt iter-7 main())
  # ---------------------------------------------------------------------------
  # def main():
  #   full = json.load(DATASET_LOCATEDIN); kin = Kinship(full['metadata']['composition_table'])
  #   rows = D.load_slice(full,'re-docred')                      # PRIMARY (trustworthy absent gold)
  #   records, contexts = D.build_records(rows, kin, 're-docred')  # now carry query_subtype + absent_regime
  #   records = stratified_subsample(records)                     # STAGE-1 CHANGE 4, doc-clustered
  #   client  = OpenRouterClient(key, 'google/gemini-3.1-flash-lite', ['deepseek/deepseek-v3.2',...],
  #                              cache_dir, temperature=0.0, budget_hard=9.0, budget_soft=5.0,
  #                              concurrency=16, max_tokens=220)
  #   # ---- PRIMARY reader pipeline (gemini) ----
  #   grounded = run_reader_pipeline(records,kin,client,contexts,tag_prefix='', do_battery=True, reader_tag='primary')
  #       # replay_reads: per-doc extraction (default + best-effort arm) -> ground names -> for each query,
  #       #   edges_q = drop_direct(grounded[did],qsrc,qtgt) if held_out else grounded[did];
  #       #   r['modeA'] = predict_symbolic(kin, edges_q, qsrc, qtgt, genders)['modeA'];
  #       #   r['modeA_goldread'] = predict_symbolic(kin, r['gold_atomics'], qsrc, qtgt, genders)['modeA']  # gold_atomics already ablated
  #       #   raw + PoT per query (PoT paths from r['gold_atomics'] = the alternative route).
  #   run_battery(records,client,...)            # SC k=10 (temp 0.7) + Kadavath P(True) -> r['_sig'] {verbalized,sc_margin,ptrue,negent,H}
  #   run_queryside(records,client,...)          # NEW: verifier + selfverify -> r['queryside_verifier'], r['queryside_selfverify']
  #   build_ct_baselines(records)                # ct_verbalized/ct_sc_margin/ct_ptrue/ct_negent/commit_argmax
  #   primitivize(records,kin)                   # include the 2 queryside dicts in _METHOD_KEYS
  #
  #   # ---- POOLS (the decisive split) ----
  #   present  = [r for r in records if not r['is_absent']]
  #   sib      = [r for r in records if r.get('absent_regime')=='same_component_sibling']
  #   diff     = [r for r in records if r.get('absent_regime')=='different_component']
  #   mixed_sibling  = present + sib   # DECISIVE: non-structural-by-construction (siblings derive EMPTY because
  #                                    #           located_in o contains is UNDEFINED -> a genuine deductive abstention)
  #   mixed_diffcomp = present + diff  # CONTRAST: structural-by-construction (disconnected components)
  #
  #   SIGNALS6 = ('verbalized','sc_margin','ptrue','negent','queryside_verifier','queryside_selfverify')
  #   core_sibling  = compute_core_views(mixed_sibling,  label='sibling',  signals=SIGNALS6)
  #   core_diffcomp = compute_core_views(mixed_diffcomp, label='diffcomp', signals=SIGNALS6)
  #       # compute_core_views reused, but: (a) extend the showdown baselines + the Holm family to all 6;
  #       #   (b) crux_survival_table reports, per signal x corpus, BOTH survival AND fraction_caught=1-survival;
  #       #   (c) view3_matched_showdown gives certificate vs each baseline selective accuracy @ matched coverage.
  #   # ---- FACT A per regime (raw-LLM high-confidence located_in/contains fabrication rate) ----
  #   factA = {'same_component_sibling': fact_a(sib), 'different_component': fact_a(diff)}
  #       # fact_a(pool) = mean over pool of (raw named) ; + confidence distribution of the named (=hallucinated) ones.
  #   # ---- mixed-pool Holm-adjusted doc-clustered confident-wrong reductions (B=10000) ----
  #   #   for each pool (sibling PRIMARY, diffcomp CONTRAST): cw_matched_to_ref(pool,'modeA',m) for m in
  #   #   ['ct_verbalized','ct_sc_margin','ct_ptrue','ct_negent','queryside_verifier','queryside_selfverify'];
  #   #   holm_bonferroni over the 6 one-sided p-values; record reduction + ci95 + p_adj + reject.
  #   # ---- abstention decomposition + gold-read ceiling (isolates extraction) ----
  #   decomp_sibling  = abstention_decomposition(mixed_sibling)   # correct-absent vs over-abstain-present + present cov + sel-acc
  #   #   gold_read_ceiling: closure over r['gold_atomics'] (ablated) -> EXPECT present coverage ~1.0 and
  #   #   absent abstention ~1.0 (the corpus verify.py guarantees held_out deduces + siblings empty);
  #   #   the gap to the LLM-read certificate == the natural-prose EXTRACTION ceiling.
  #   atomic = atomic_pr(records,kin,grounded,contexts)          # converse-invariant primitive P/R/F1 (+ vs-justifiable ceiling)
  #   # ---- CROSS-FAMILY reader (deepseek) FULL on the same subsample, reader-specific certificate ----
  #   if budget allows: cf_* = same pipeline under deepseek/deepseek-v3.2 (tag_prefix='cf_'); record FACT A,
  #       crux fraction-caught, mixed-sibling showdown + Holm, abstention decomp -> reader-generality.
  #   # ---- worked traces + Prolog discharge ----
  #   worked_sibling_noderiv = worked_no_derivation(sib, kin)          # a same-component-sibling pair: raw commits a
  #       # containment at high conf; extracted graph leaves qsrc,qtgt with EMPTY closure (located_in o contains undefined)
  #       # -> certificate ABSTAINS structurally; discharge() emits comp/3,conv/2,rel/3,solve_/4 (swipl if present else python-checked).
  #   worked_over_abstain_present = worked_over_abstain_present(present, kin)  # held_out pair gold-read solves but LLM-read
  #       # abstains (extraction missed a connecting edge) -> the extraction-limited boundary, made concrete.
  #   prolog_sum = prolog_discharge_summary(present, kin)             # discharge <=40 covered present certificates, report swipl/python truthfully.
  #
  #   # ---- FORK VERDICT (pre-registered; decisive on the SIBLING pool) ----
  #   def fork(core_sibling, factA, decomp_sibling):
  #       FACT_A_high = factA['same_component_sibling']['rate'] >= 0.20
  #       surv = [1-core_sibling.crux.frac_caught[s] for s in 4 dispersion signals]  # survival
  #       FACT_B = sum(x>=0.5 for x in surv) >= 2
  #       holm = core_sibling.mixed_holm     # over the 6 baselines
  #       cert_beats_all = all(holm[m].reject and reduction[m]>0 for m in SIGNALS6)
  #       cert_beats_verifier = (holm['queryside_verifier'].reject and reduction['queryside_verifier']>0)
  #       verifier_suffices = (cw_certificate_sibling >= cw_queryside_verifier_sibling - eps)  # verifier catches as well as cert
  #       if cert_beats_all: return 'DEMONSTRATED-FIX'                       # converts headline
  #       if verifier_suffices and FACT_A_high: return 'VERIFIER-SUFFICES'   # honest negative: structural cert not needed
  #       if FACT_A_high and FACT_B: return 'EXTRACTION-LIMITED-BOUNDARY'    # diagnostic stands; cert over-abstains on present
  #       return 'DIAGNOSTIC-WEAKER-THAN-CLAIMED'
  #   verdict = fork(...); also emit per-flag booleans + the diffcomp CONTRAST verdict.
  #
  #   # ---- OUTPUT (STAGE 4) ----
  #   write method_out.json (exp_gen_sol_out), validate full/mini/preview.

  # ---------------------------------------------------------------------------
  # STAGE 4 -- output assembly (exp_gen_sol_out; one row per query)
  # ---------------------------------------------------------------------------
  # datasets grouped by corpus name into THREE groups:
  #   'locatedin_present', 'locatedin_absent_sibling', 'locatedin_absent_diffcomponent'.
  # Each example:
  #   input  = story[:1200] + '  || Q: what is the geographic relationship of <Xname> to <Yname>?'
  #   output = gold word ('located in' for present held_out/never_annotated; 'no-relation' for absent)
  #   predict_certificate, predict_certificate_goldread,
  #   predict_conf_thresh_verbalized, predict_conf_thresh_sc_margin, predict_conf_thresh_ptrue, predict_conf_thresh_negent,
  #   predict_queryside_verifier, predict_queryside_selfverify,
  #   predict_commit_argmax (=raw), predict_pot, predict_sc,
  #   gold, metadata_regime ('held_out'|'never_annotated'|'same_component_sibling'|'different_component'),
  #   metadata_reader ('gemini-3.1-flash-lite' | 'deepseek-v3.2'), metadata_doc_id, metadata_title,
  #   metadata_qsrc/qtgt (entity_ids) + metadata_qsrc_name/qtgt_name, metadata_hop, metadata_composed_only,
  #   per-signal confidences (metadata_conf_*), metadata_n_extracted_edges, metadata_certificate_info.
  # metadata block carries: FACT-A table (per regime x reader, rate + confidence distribution),
  #   fraction-caught crux table (per signal x reader: survival AND 1-survival),
  #   mixed-pool leaderboards (SIBLING primary + DIFFCOMPONENT contrast) with certificate-vs-each-baseline
  #   selective accuracy @ matched coverage and Holm-adjusted confident-wrong reductions with CIs,
  #   abstention decomposition (correct-absent vs over-abstain-present), present coverage + selective accuracy,
  #   GOLD-READ CEILING, natural-prose atomic P/R (converse-invariant primitive PRIMARY + strict secondary +
  #   vs-locally-justifiable ceiling), default-vs-best-effort extraction comparison, cross-reader comparison,
  #   cost ledger (client.stats()), one worked sibling no-derivation trace + one over-abstain-present trace
  #   (Prolog-discharged if swipl present else python-checked, labelled truthfully), and the explicit FORK verdict.
  # Tag EVERY number REAL-LLM-READ + NATURAL-PROSE + located-in domain. Then aii-json validate +
  #   generate mini/preview; aii-file-size-limit split if needed.

  # ---------------------------------------------------------------------------
  # CLI / RUN
  # ---------------------------------------------------------------------------
  #   uv run method.py --slice re-docred --cross-family --concurrency 16 --budget-hard 9.0 & PID=$!
  #   monitor: tail -f logs/run.log & ; check kill -0 $PID; wait $PID; echo $?
  #   (Caching makes re-runs $0; gradual scaling flags: --limit-docs N, --no-battery for smoke.)
fallback_plan: >-
  EXTRACTION-LIMITED (the most likely fork, still publishable): if natural-prose atomic recall is low (iter-7 kinship was
  0.376) the LLM-read certificate over-abstains on PRESENT held_out and the mixed-sibling Holm reductions include 0 -> emit
  verdict=EXTRACTION-LIMITED-BOUNDARY. The DIAGNOSTIC (FACT A high + the mixed-pool capability gap on the gold-read ceiling)
  still stands and the gold-read ceiling (expected ~1.0 present / ~1.0 absent abstention) isolates extraction as the binding
  constraint. PATH-2 HEDGE: run the best-effort few-shot + given-inventory extraction arm and, if its recall lifts present
  coverage enough that the mixed-sibling reductions turn positive with Holm-CIs excluding 0, report that as the DEMONSTRATED-FIX
  on the best-effort arm (label the arm honestly). COST: track client.cost after every batch; if approaching $9 -> (a) drop
  SC k from 10 to 5, (b) shrink the subsample (fewer docs / tighter per-doc caps), (c) skip the cross-family deepseek reader
  (report gemini-only with a note), (d) skip the best-effort extraction arm. The SHA-256 cache means partial progress is never
  lost and re-runs are $0. VERIFIER TIES CERTIFICATE: if the query-side verifier's confident-wrong on the sibling pool is
  statistically indistinguishable from the certificate's -> emit verdict=VERIFIER-SUFFICES (an honest negative: the structural
  certificate is not NEEDED for the absent stratum; the trained/prompted false-premise detector already handles it). FACT
  B READER-DEFEATED: if for the deployed reader >=3 of 4 dispersion signals catch >70% of fabrications (as deepseek did on
  kinship) report FACT B as reader-dependent and narrow the diagnostic to verbalized confidence / weaker readers -- do NOT
  claim family-level blindness. SWIPL ABSENT: prolog.discharge() already falls back to python-checked verification and labels
  it truthfully (iter-5/6/7 precedent) -- never imply swipl ran. CORPUS FIELD MISMATCH: if a gold_graph key differs from the
  spec (e.g. absent regime stored only as same_component bool, or composed_only missing), derive query_subtype by checking
  whether a direct (source,target) atomic edge EXISTS (held_out) vs not (never_annotated), and derive absent_regime from same_component
  (True=sibling, False=different_component); assert the round-trip (held_out deduces after ablation; siblings+diffcomp give
  EMPTY both directions) on a smoke sample and fail loudly if violated. DEEPSEEK UNAVAILABLE: the OpenRouterClient fallback
  chain already rotates models; if all fail, report primary-only. If the present held_out pool is too small after subsampling,
  raise the per-doc present cap and pull from more docs (present total is 3,510 -- ample). If aii-json lacks an exp_gen_sol_out
  schema, reuse the exact schema/validator invocation from the iter-7 experiment workspace.
testing_plan: |-
  GRADUAL mini->full with explicit confirmation gates (aii-long-running-tasks pattern); never launch the full battery before the engine is proven wired correctly.

  GATE 0 (no LLM): import kinship + Kinship(full['metadata']['composition_table']); assert base==['located_in','contains'], compose_types('located_in','located_in')=='located_in', compose_types('located_in','contains') is None, conv_type('located_in')=='contains'. Load 1 doc, build records; assert query_subtype/absent_regime are set. THE KEY ENGINE CHECK (mirrors the corpus verify.py): for every held_out present record, after closure_edges_drop_direct on r['gold_atomics'], query_modeA must EMIT 'located_in' (deduced via the alternative path); for every sibling AND different_component absent record, query_modeA over gold_atomics must return no_path (EMPTY) in BOTH directions. If this fails the wiring is wrong -- STOP and fix before spending. Print the gold-read ceiling on this sample (expect 1.0 present / 1.0 absent abstention).

  GATE 1 (smoke, tiny LLM): uv run method.py --slice re-docred --limit-docs 3 --no-battery. Confirms: located-in extraction prompt parses (>=1 grounded edge on a multi-place doc), grounding recall plausible (~0.99 vs gold surfaces), raw/PoT parse to {located in,contains,no-relation}, the held_out extracted-edge ablation runs, predict_symbolic produces modeA + modeA_goldread, abstention_decomposition + atomic_pr run, output assembles + aii-json validates. Check the cost ledger is ~cents.

  GATE 2 (small battery+verifier, 1 reader): --limit-docs ~12 (drop --no-battery). Confirms run_battery (SC k=10 + P(True)) and run_queryside (verifier + selfverify) attach r['_sig'] and the two queryside method dicts; crux_survival_table prints survival AND fraction_caught; view3 matched-coverage showdown and cw_matched_to_ref run on mixed_sibling and mixed_diffcomp; holm_bonferroni over the 6 baselines returns p_adj/reject. Inspect FACT A on the sibling pool (>0 expected) and that certificate confident-wrong on absent ~ 0 (structural). Verify cost stays well under budget and scales roughly linearly.

  GATE 3 (full subsample, primary reader): run the stratified subsample (~400 held_out + 118 never_annotated + 450 sibling + 250 diffcomp, doc-clustered, per-doc caps). CONFIRMATION SIGNALS: gold-read ceiling ~1.0/1.0 (engine sound); FACT A_sibling >= 0.20 with a high-confidence mass; the mixed-sibling certificate selective accuracy beats every signal at matched coverage IF extraction recall is adequate; Holm reductions reported with CIs. Read the FORK verdict.

  GATE 4 (cross-family): add --cross-family (deepseek) only if budget remains; confirm FACT A + crux fraction-caught + mixed-sibling Holm replicate the reader-generality story; record reader-dependence of FACT B honestly.

  FINAL VALIDATION: aii-json validate full/mini/preview of method_out.json; aii-file-size-limit split if oversized; assert every example carries all predict_* keys + gold + metadata_regime + metadata_reader; assert the metadata block contains the FACT-A table, fraction-caught crux table, both mixed leaderboards with Holm CIs, abstention decomposition, gold-read ceiling, atomic P/R, cross-reader block, cost ledger, both worked traces, and the explicit FORK verdict. Re-run end-to-end once to confirm cache replay is $0 and the verdict is stable.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_dA_3iFe_7fn_
type: research
title: >-
  No-Derivation Abstention vs Confidence Family; NeSy Reposition; Re-DocRED Absent Gold
summary: >-
  Pure-web research bundle ($0) for iter-6/iter-7 of the closure-certificate project, across three workstreams. (A) Pins the
  confidence/uncertainty selective-prediction family our STEP-A battery competes against -- verbalized confidence [Lin2022;
  Tian2023], self-consistency [Wang2023], P(True)/P(IK) [Kadavath2022], semantic entropy [Kuhn2023; Farquhar2024], SelfCheckGPT
  [Manakul2023], the abstention survey [Wen2024], learned temporal abstention [Zhou2026], and the adversarial internal-state-probe
  neighbour [Song2026] -- with verified BibTeX, per-method abstention signals + verbatim quotes, a paper-ready signals-vs-catches
  table, and a ~250-word drop-in differentiation paragraph arguing every signal is dispersion/confidence-driven and therefore
  BLIND to a confident, self-consistent absent-relation hallucination, whereas the certificate abstains STRUCTURALLY (no derivation
  path) regardless of confidence -- with honest scope (confidence baselines tie at matched coverage on ordinary uncertain
  deduction). (B) A timing-aware (as-of 2026-06-18) NeSy / qualitative-reasoning venue shortlist -- Neurosymbolic AI journal
  (rolling, the only open NeSy-family target now), NeSy 2026/2027, *SEM, KR 2026 (qualitative reasoning in scope), STRL, EMNLP/ARR
  -- a crisp 'why not ACL Knowledge Extraction' statement, and a recommendation to SWAP primary<->fallback. (C) Verifies Re-DocRED
  (tonytan48/Re-DocRED, arXiv:2205.12696, 2022.emnlp-main.580, MIT, splits 3,053/500/500, '~64.6% of triples missing' in original
  DocRED, recall 32.07->69.40), confirms kinship coverage (P22/P25/P26/P40/P3373 PRESENT; P1038 ABSENT), documents the false-negative
  pitfall + disconnected-component absent-gold methodology, and scouts alternative natural hosts (CustFRE = natural prose
  with explicit no_relation gold; KinshipQA = generated/synthetic, fails the natural bar). Directly retires the reviewer novelty
  MAJOR + venue MINOR and de-risks iter-7 STEP-B.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_RfjDpsGkBXDG
type: dataset
title: Natural-Text Located-In Absent-Relation Corpus from Re-DocRED + DocRED
summary: |-
  A document-level GEOGRAPHIC / ADMINISTRATIVE CONTAINMENT ('located-in') corpus over genuinely-natural Wikipedia introductory prose (Re-DocRED, the completeness-corrected re-annotation of DocRED; vanilla DocRED kept as a downgraded secondary slice). It is the STRUCTURAL TWIN of the iter-6 natural-kinship corpus and a SECOND genuinely-natural absent-relation domain, built to show the closure-certificate confidence-blindness diagnostic is NOT kinship-specific. Consumed by iter-8's domain-generality experiment. Built $0 LLM (deterministic cue check passes 100%, judge skipped).

  FORMAT: exp_sel_data_out, ONE ROW PER DOCUMENT, grouped by dataset. datasets=[{dataset:'re-docred', examples:[...]}, {dataset:'docred', examples:[...]}]. Each example: input=detokenized Wikipedia prose; output=json.dumps(gold_graph) with {doc_id, source, split, nodes, atomic_edges, query_edges, absent_relation_pairs, absent_pairs_source='structural_closure', contradiction_pairs}; plus flat metadata_* columns. Counts re-docred 2604 docs / docred 2080.

  ENGINE (drop-in): kinship.py forward least-fixpoint UNION closure is REUSED VERBATIM, parameterized by containment_composition_table.json — a DEGENERATE single-relation TRANSITIVE table (located_in∘located_in=located_in; contains∘contains=contains; ALL else UNDEFINED). NOT a relation algebra. Map each atomic edge to {a:source, b:target, type:primitive}; D[(s,t)]={located_in} EMIT, ∅ both directions ABSTAIN (absent), |D|>1 Mode-B conflict (0 here). Direction: source located_in target; P131/P17/P1376/P276 src=h tgt=t, P150/P36 INVERT.

  THREE STRATA. (1) Atomic located_in edges (LOC-LOC NER filter, deduped, true 2-cycles dropped), each flagged locally_justifiable (adjacent-sentence locality + surface cue); re-docred 20,825 edges, locally_justifiable_frac 0.588. (2) PRESENT deduction-required queries (re-docred 3,510), gold certain, TWO honest sub-types: never_annotated (118; pair never a direct edge, composed_only=true, provably non-circular — RARE because DocRED annotates geography near-transitively, a measured domain difference) and held_out (3,392; a directly-annotated located_in edge that is ALSO derivable via an alternative ≥2-hop path and is non-local — consumer MUST drop the single (source,target) atomic edge before querying, then the engine deduces it; SOUND because removing a redundant edge preserves the full transitive closure). (3) ABSENT no-derivation pairs (re-docred 24,088), two regimes: different_component (3,274; unrelated places, clean kinship-analog) and same_component_sibling (20,814; co-component, neither inside the other — the reviewer-named containment-specific regime). Per-doc caps present_cap=40, absent_cap=30 (stratified), atomic_cap=80; *_truncated flagged.

  QUALITY. Round-trip gate (verify.py) PASSES: never_annotated 367/367, held_out 4357/4357 (deduced after ablation), absent 41100/41100 empty in BOTH directions, every derivation_path a valid DIRECTED located_in chain, cue-present 19885/19885, Mode-B 0. offset_ok 0.988/0.990. Schema-validated 3/3 (full/mini/preview). Completeness correction (2079 shared titles): Re-DocRED +67.5% located-in edges and 2.8x present queries vs DocRED — so absent gold is TRUSTWORTHY only on re-docred; docred absent is DOWNGRADED. Char honesty: mean ~1025 chars, max 2969, NO doc reaches 3000 (no padding/concatenation — natural-text + absent-relation is the load-bearing property). Caveats: closed-world absent; composed_only is pair-level (not type-level as kinship); multi-parent DAG; admin_level node tag best-effort/non-load-bearing; P276 lower precision (~0 LOC-LOC on re-docred). See dataset_card.md / README.md.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
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

### [2] HUMAN-USER prompt · 2026-06-18 04:09:52 UTC

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

### [3] SKILL-INPUT — aii-python · 2026-06-18 04:10:00 UTC

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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-18 04:10:00 UTC

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

### [5] SKILL-INPUT — aii-json · 2026-06-18 04:10:00 UTC

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

### [6] SKILL-INPUT — aii-use-hardware · 2026-06-18 04:10:00 UTC

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

### [7] SKILL-INPUT — aii-file-size-limit · 2026-06-18 04:10:08 UTC

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

### [8] SKILL-INPUT — aii-parallel-computing · 2026-06-18 04:10:08 UTC

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

### [9] SKILL-INPUT — aii-openrouter-llms · 2026-06-18 05:12:44 UTC

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

### [10] SYSTEM-USER prompt · 2026-06-18 05:41:05 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx2
type: experiment
title: >-
  iter-8 decisive test: closure certificate vs 4-signal battery vs query-side false-premise verifier on the natural located-in
  corpus (same-component-sibling mixed pool)
summary: >-
  Re-run the iter-7 STEP-B natural-corpus experiment VERBATIM-by-reuse on a SECOND genuinely-natural absent-relation domain
  (Re-DocRED geographic/administrative containment, art_RfjDpsGkBXDG), parameterizing the kinship.py forward-union engine
  with the degenerate transitive containment table. Deliver (i) FACT A on located-in (raw-LLM high-confidence located_in/contains
  fabrication rate on absent pairs, both readers), (ii) per-signal x reader crux-survival WITH fraction-caught, (iii) the
  signal-agnostic MIXED-POOL CAPABILITY GAP newly powered on the NON-structural-by-construction same_component_sibling regime,
  (iv) Holm-adjusted doc-clustered confident-wrong reductions of the certificate vs each of the 4 dispersion signals AND a
  NEW query-side false-premise verifier + self-verification baseline, plus the structural-by-construction different_component
  CONTRAST, the gold-read ceiling that isolates extraction, and the pre-registered FORK verdict (DEMONSTRATED-FIX | EXTRACTION-LIMITED-BOUNDARY
  | DIAGNOSTIC-WEAKER-THAN-CLAIMED | VERIFIER-SUFFICES). All reads REAL-LLM (OpenRouter, SHA-256 cached, hard $9 cap); gradual
  mini->full.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  ############################################################################
  # OVERVIEW
  # This is a DROP-IN ADAPTATION of the iter-7 STEP-B template (the natural-
  # kinship Re-DocRED run, art_htcr8yOZLCQy) to the iter-7 located-in corpus
  # (art_RfjDpsGkBXDG). REUSE the iter-7 code VERBATIM where possible; the ONLY
  # new substance is (a) located-in field/prompt adaptations, (b) the held_out
  # direct-edge ABLATION, (c) the absent-REGIME split (same_component_sibling vs
  # different_component), and (d) the NEW query-side false-premise verifier +
  # self-verification baselines. Every battery/stats/closure function is reused.
  #
  # SOURCE WORKSPACES (read-only; copy the .py files into THIS workspace):
  #   TEMPLATE_EXP = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1
  #       -> method.py (orchestrator template), dataio_redocred.py (loader+grounding),
  #          readers.py (prompts/parsers), kinship.py (forward-union engine = REUSE VERBATIM),
  #          baselines.py (predict_symbolic, matched_coverage_showdown, absent_h2,
  #                        confident_wrong, coverage_confidence, story_atomic_pr,
  #                        aggregate_atomic_pr = REUSE VERBATIM),
  #          stats.py (holm_bonferroni, matched_coverage_mask, selective_accuracy = REUSE VERBATIM),
  #          llm.py (OpenRouterClient: SHA-256 disk cache, budget_hard cap = REUSE VERBATIM),
  #          prolog.py (discharge() = REUSE VERBATIM).
  #   DATASET = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/full_data_out.json
  #       (one row per doc; datasets=[{dataset:'re-docred',examples}, {dataset:'docred',examples}];
  #        each ex.output = json.dumps(gold_graph); top metadata.composition_table = the
  #        DEGENERATE containment table -> feed straight into Kinship(...).)
  #   RESEARCH = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_research_1/research_out.json
  #       (art_dA_3iFe_7fn_: false-premise lit FalseQA/AbstentionBench/Wen2024 framing +
  #        the 4 confidence-signal specs; read for the verifier wording + citations note.)
  #   The corpus's OWN containment_composition_table.json also lives in the dataset dir,
  #   but PREFER full['metadata']['composition_table'] (emitted verbatim) so Kinship is
  #   parameterized from the exact table the corpus was verified against.
  ############################################################################

  # ---------------------------------------------------------------------------
  # STAGE 0 -- workspace setup (pyproject.toml: numpy, scipy, loguru, httpx; uv venv)
  # ---------------------------------------------------------------------------
  #  - cp kinship.py, baselines.py, stats.py, llm.py, prolog.py from TEMPLATE_EXP VERBATIM.
  #  - Author dataio_locatedin.py (adapt dataio_redocred.py), readers_locatedin.py
  #    (adapt readers.py), queryside.py (NEW), method.py (adapt the iter-7 orchestrator).
  #  - kin = Kinship(full['metadata']['composition_table'])  # base types = ['located_in','contains']
  #    sanity: kin.compose_types('located_in','located_in')=='located_in';
  #            kin.compose_types('located_in','contains') is None (=> siblings derive EMPTY);
  #            kin.conv_type('located_in')=='contains'.

  # ---------------------------------------------------------------------------
  # STAGE 1 -- dataio_locatedin.py  (loader + grounding + the THREE adaptations)
  # ---------------------------------------------------------------------------
  # The located-in gold_graph fields (verified from the corpus):
  #   nodes:               {entity_id, surface, type='LOC', admin_level, mention_spans:[[cs,ce],...]}  (NO gender)
  #   atomic_edges:        {source, target, primitive='located_in', relation_type, relation_surface='located in',
  #                         is_query=false, hop_count=1, support_span, locally_justifiable(bool, if present)}
  #   query_edges:         {source, target, primitive='located_in', hop_count(>=2), derivation_path, is_query=true,
  #                         composed_only(bool)}   # composed_only=True  => never_annotated (no direct edge)
  #                                                # composed_only=False => held_out (a redundant direct edge EXISTS)
  #   absent_relation_pairs:{source, target, reason, is_absent=true, same_component(bool)}
  #                         # reason in {'different_component','same_component_sibling'}
  #
  # REUSE dataio_redocred.py's load_slice / build_doc_context / ground_name / id_path_to_names
  # VERBATIM (build_doc_context already defaults gender='male'; located_in surface is
  # gender-independent so this is harmless). _atomics_to_id_edges already reads
  # source/target/primitive/locally_justifiable -> works unchanged.
  #
  # CHANGE 1 (held_out ABLATION) -- the single most important new rule. The corpus
  # engine_edge_mapping states verbatim: 'For a held_out query, FIRST drop the single
  # atomic edge whose (source,target)==(query source,target) before querying.' Implement:
  #   def closure_edges_drop_direct(edges, qsrc, qtgt):
  #       return [e for e in edges if not ({e['a'],e['b']}=={qsrc,qtgt})]   # drops edge + its converse seed
  #   In make_present_record(ctx,q,...):
  #       full_atomics = _atomics_to_id_edges(gg)
  #       r['gold_atomics']      = closure_edges_drop_direct(full_atomics, qsrc, qtgt)   # ALWAYS drop direct
  #       r['gold_atomics_just'] = closure_edges_drop_direct(_atomics_to_id_edges(gg,justifiable_only=True), qsrc, qtgt)
  #       r['composed_only']     = bool(q.get('composed_only', False))
  #       r['query_subtype']     = 'never_annotated' if r['composed_only'] else 'held_out'
  #       (never_annotated has no direct edge so the drop is a no-op there; held_out forces deduction
  #        via the alternative >=2-hop path -- this is what makes PRESENT coverage a genuine deductive result.)
  #   ALSO drop the direct edge from the LLM-EXTRACTED graph at query time (symmetry; see STAGE 2)
  #   so a held_out 'covered' decision is a real derivation, not a read-back. Record BOTH the
  #   ablated present-coverage (PRIMARY) and the un-ablated coverage (sensitivity) for honesty.
  #
  # CHANGE 2 (absent REGIME tag) -- decisive for the headline:
  #   In make_absent_record(ctx,p,...):
  #       reason = p.get('reason') or ('same_component_sibling' if p.get('same_component') else 'different_component')
  #       r['absent_regime'] = 'same_component_sibling' if 'sibling' in reason or p.get('same_component') else 'different_component'
  #   (Keep gold_surface='no-relation', is_absent=True, hop=0 as in the template.)
  #
  # CHANGE 3 (gold primitive / surface) -- located_in is gender-free:
  #   gold_prim='located_in'; gold_word=kin.surface('located_in','male')=='located in'. No kinship_relation field.
  #
  # CHANGE 4 (STRATIFIED SUBSAMPLE for cost) -- the corpus is huge (re-docred 3,510 present /
  #   24,088 absent of which 20,814 sibling). Build records, then subsample to a budget-safe,
  #   strata-BALANCED working set BEFORE any LLM call, doc-clustered (keep whole docs):
  #     target ~ {present held_out: 400, present never_annotated: ALL 118, sibling-absent: 450,
  #               diffcomponent-absent: 250}, drawn by ascending doc_id for determinism, with a
  #     per-doc query cap (e.g. <=6 present, <=6 sibling, <=4 diffcomp) so dense geography docs
  #     cannot dominate. Tunable via --limit-docs / per-stratum caps. Log the realized counts.
  #   (Whole-doc clustering matters: extraction is one call shared by a doc's queries.)

  # ---------------------------------------------------------------------------
  # STAGE 2 -- readers_locatedin.py  (located-in prompts/parsers, adapted from readers.py)
  # ---------------------------------------------------------------------------
  # Replace the kinship surface vocabulary with the containment vocabulary:
  #   CANON_SURFACES = ['located in','contains']; _NO_REL as in template (+'unrelated','no containment').
  #   normalize_surface(w): map 'located in'/'part of'/'in'/'within'/'a city in'/'subdivision of' -> 'located_in'
  #     surface 'located in'; 'contains'/'includes'/'has ... within it' -> 'contains'; no-relation words -> 'no-relation'.
  #     (Return the canonical SURFACE string; kin.surface_to_type maps 'located in'->located_in.)
  #   EXTRACTION prompt (extraction_item): 'Extract every DIRECTLY-STATED geographic/administrative
  #     containment between two named places. Output JSON {"relations":[{"a":<place>,"relation":"located in"|"contains","b":<place>}]}.
  #     a located in b means a is inside/part of/an administrative subdivision of b. Only directly stated
  #     pairs; do NOT infer transitive containment.' (max_tokens 700.) parse_extraction reused (it calls
  #     normalize_surface + kin.surface_to_type) -> works once the vocab is swapped.
  #   RAW query prompt (raw_query_item): 'Question: What is the geographic relationship of <X> to <Y>?
  #     Answer JSON {"relation":"located in"|"contains"|"no-relation","confidence":0..1}. "located in" means
  #     X is inside Y; "contains" means X contains Y; "no-relation" if neither place is inside the other.'
  #   PoT prompt (pot_item): compose a chain of places -> containment of last to first; same JSON.
  #   BEST-EFFORT extraction arm (PATH 2 hedge): a second extraction variant with 2-3 few-shot
  #     examples + the doc's place inventory (reuse template's --given-inventory _inventory_user) under
  #     prompt tag 'extract_best'; ground both, run the certificate on EACH, report present coverage /
  #     atomic recall for default vs best-effort so the positive fork gets its fair shot.
  #   parse_raw / aggregate_sc / aggregate_pot reused VERBATIM (they only depend on normalize_surface).
  # AT QUERY TIME, for held_out present queries, also drop the direct edge from the grounded extracted
  #   graph before predict_symbolic: edges_q = closure_edges_drop_direct(grounded[did], qsrc, qtgt).

  # ---------------------------------------------------------------------------
  # STAGE 2b -- queryside.py  (THE NEW BASELINE the certificate must MATCH or BEAT)
  # ---------------------------------------------------------------------------
  # (1) QUERY-SIDE FALSE-PREMISE VERIFIER ('are these related at all?') -- the established method
  #     for this failure mode (research dossier art_dA_3iFe_7fn_: FalseQA/AbstentionBench/Wen2024).
  #   verifier_item(story,Xname,Yname): system='You decide whether a presupposed geographic relation
  #     exists. Output JSON {"related":true|false,"confidence":0..1}.'; user='Story:...\n Based ONLY on the
  #     document, is <X> located in <Y>, OR does <X> contain <Y> (i.e. is there any containment between
  #     them in EITHER direction)? related=false if neither is inside the other.' (1 call, temp 0).
  #   parse_verifier -> {related:bool, conf:float}.
  #   METHOD DICT predict_queryside_verifier: when related==True -> named=True, surface = the raw
  #     answerer's committed primitive (r['raw']['surface'] after primitivize), conf = verifier conf;
  #     when related==False -> named=False (abstain), conf = 1-verifier_conf. (i.e. the verifier GATES
  #     the committed answer by a dedicated relatedness check.)
  # (2) SELF-VERIFICATION pass on the raw committed answer:
  #   selfverify_item(story,Xname,Yname,proposed): 'Is this proposed answer correct given the document?
  #     Output JSON {"correct":true|false,"confidence":0..1}.' (1 call, temp 0).
  #   METHOD DICT predict_queryside_selfverify: named = r['raw']['named'] AND correct==True; surface =
  #     raw surface; conf = self-verify confidence (used for matched-coverage thresholding).
  # Both produce {surface,conf,named} dicts identical in shape to ct_<signal>, so they plug straight
  #   into matched_coverage_showdown (add to its `baselines` tuple), cw_matched_to_ref, and the Holm
  #   family. Add to _METHOD_KEYS so primitivize() canonicalizes their surfaces.
  # COST: +2 calls/query (verifier + selfverify), both cached.

  # ---------------------------------------------------------------------------
  # STAGE 3 -- method.py orchestration (adapt iter-7 main())
  # ---------------------------------------------------------------------------
  # def main():
  #   full = json.load(DATASET_LOCATEDIN); kin = Kinship(full['metadata']['composition_table'])
  #   rows = D.load_slice(full,'re-docred')                      # PRIMARY (trustworthy absent gold)
  #   records, contexts = D.build_records(rows, kin, 're-docred')  # now carry query_subtype + absent_regime
  #   records = stratified_subsample(records)                     # STAGE-1 CHANGE 4, doc-clustered
  #   client  = OpenRouterClient(key, 'google/gemini-3.1-flash-lite', ['deepseek/deepseek-v3.2',...],
  #                              cache_dir, temperature=0.0, budget_hard=9.0, budget_soft=5.0,
  #                              concurrency=16, max_tokens=220)
  #   # ---- PRIMARY reader pipeline (gemini) ----
  #   grounded = run_reader_pipeline(records,kin,client,contexts,tag_prefix='', do_battery=True, reader_tag='primary')
  #       # replay_reads: per-doc extraction (default + best-effort arm) -> ground names -> for each query,
  #       #   edges_q = drop_direct(grounded[did],qsrc,qtgt) if held_out else grounded[did];
  #       #   r['modeA'] = predict_symbolic(kin, edges_q, qsrc, qtgt, genders)['modeA'];
  #       #   r['modeA_goldread'] = predict_symbolic(kin, r['gold_atomics'], qsrc, qtgt, genders)['modeA']  # gold_atomics already ablated
  #       #   raw + PoT per query (PoT paths from r['gold_atomics'] = the alternative route).
  #   run_battery(records,client,...)            # SC k=10 (temp 0.7) + Kadavath P(True) -> r['_sig'] {verbalized,sc_margin,ptrue,negent,H}
  #   run_queryside(records,client,...)          # NEW: verifier + selfverify -> r['queryside_verifier'], r['queryside_selfverify']
  #   build_ct_baselines(records)                # ct_verbalized/ct_sc_margin/ct_ptrue/ct_negent/commit_argmax
  #   primitivize(records,kin)                   # include the 2 queryside dicts in _METHOD_KEYS
  #
  #   # ---- POOLS (the decisive split) ----
  #   present  = [r for r in records if not r['is_absent']]
  #   sib      = [r for r in records if r.get('absent_regime')=='same_component_sibling']
  #   diff     = [r for r in records if r.get('absent_regime')=='different_component']
  #   mixed_sibling  = present + sib   # DECISIVE: non-structural-by-construction (siblings derive EMPTY because
  #                                    #           located_in o contains is UNDEFINED -> a genuine deductive abstention)
  #   mixed_diffcomp = present + diff  # CONTRAST: structural-by-construction (disconnected components)
  #
  #   SIGNALS6 = ('verbalized','sc_margin','ptrue','negent','queryside_verifier','queryside_selfverify')
  #   core_sibling  = compute_core_views(mixed_sibling,  label='sibling',  signals=SIGNALS6)
  #   core_diffcomp = compute_core_views(mixed_diffcomp, label='diffcomp', signals=SIGNALS6)
  #       # compute_core_views reused, but: (a) extend the showdown baselines + the Holm family to all 6;
  #       #   (b) crux_survival_table reports, per signal x corpus, BOTH survival AND fraction_caught=1-survival;
  #       #   (c) view3_matched_showdown gives certificate vs each baseline selective accuracy @ matched coverage.
  #   # ---- FACT A per regime (raw-LLM high-confidence located_in/contains fabrication rate) ----
  #   factA = {'same_component_sibling': fact_a(sib), 'different_component': fact_a(diff)}
  #       # fact_a(pool) = mean over pool of (raw named) ; + confidence distribution of the named (=hallucinated) ones.
  #   # ---- mixed-pool Holm-adjusted doc-clustered confident-wrong reductions (B=10000) ----
  #   #   for each pool (sibling PRIMARY, diffcomp CONTRAST): cw_matched_to_ref(pool,'modeA',m) for m in
  #   #   ['ct_verbalized','ct_sc_margin','ct_ptrue','ct_negent','queryside_verifier','queryside_selfverify'];
  #   #   holm_bonferroni over the 6 one-sided p-values; record reduction + ci95 + p_adj + reject.
  #   # ---- abstention decomposition + gold-read ceiling (isolates extraction) ----
  #   decomp_sibling  = abstention_decomposition(mixed_sibling)   # correct-absent vs over-abstain-present + present cov + sel-acc
  #   #   gold_read_ceiling: closure over r['gold_atomics'] (ablated) -> EXPECT present coverage ~1.0 and
  #   #   absent abstention ~1.0 (the corpus verify.py guarantees held_out deduces + siblings empty);
  #   #   the gap to the LLM-read certificate == the natural-prose EXTRACTION ceiling.
  #   atomic = atomic_pr(records,kin,grounded,contexts)          # converse-invariant primitive P/R/F1 (+ vs-justifiable ceiling)
  #   # ---- CROSS-FAMILY reader (deepseek) FULL on the same subsample, reader-specific certificate ----
  #   if budget allows: cf_* = same pipeline under deepseek/deepseek-v3.2 (tag_prefix='cf_'); record FACT A,
  #       crux fraction-caught, mixed-sibling showdown + Holm, abstention decomp -> reader-generality.
  #   # ---- worked traces + Prolog discharge ----
  #   worked_sibling_noderiv = worked_no_derivation(sib, kin)          # a same-component-sibling pair: raw commits a
  #       # containment at high conf; extracted graph leaves qsrc,qtgt with EMPTY closure (located_in o contains undefined)
  #       # -> certificate ABSTAINS structurally; discharge() emits comp/3,conv/2,rel/3,solve_/4 (swipl if present else python-checked).
  #   worked_over_abstain_present = worked_over_abstain_present(present, kin)  # held_out pair gold-read solves but LLM-read
  #       # abstains (extraction missed a connecting edge) -> the extraction-limited boundary, made concrete.
  #   prolog_sum = prolog_discharge_summary(present, kin)             # discharge <=40 covered present certificates, report swipl/python truthfully.
  #
  #   # ---- FORK VERDICT (pre-registered; decisive on the SIBLING pool) ----
  #   def fork(core_sibling, factA, decomp_sibling):
  #       FACT_A_high = factA['same_component_sibling']['rate'] >= 0.20
  #       surv = [1-core_sibling.crux.frac_caught[s] for s in 4 dispersion signals]  # survival
  #       FACT_B = sum(x>=0.5 for x in surv) >= 2
  #       holm = core_sibling.mixed_holm     # over the 6 baselines
  #       cert_beats_all = all(holm[m].reject and reduction[m]>0 for m in SIGNALS6)
  #       cert_beats_verifier = (holm['queryside_verifier'].reject and reduction['queryside_verifier']>0)
  #       verifier_suffices = (cw_certificate_sibling >= cw_queryside_verifier_sibling - eps)  # verifier catches as well as cert
  #       if cert_beats_all: return 'DEMONSTRATED-FIX'                       # converts headline
  #       if verifier_suffices and FACT_A_high: return 'VERIFIER-SUFFICES'   # honest negative: structural cert not needed
  #       if FACT_A_high and FACT_B: return 'EXTRACTION-LIMITED-BOUNDARY'    # diagnostic stands; cert over-abstains on present
  #       return 'DIAGNOSTIC-WEAKER-THAN-CLAIMED'
  #   verdict = fork(...); also emit per-flag booleans + the diffcomp CONTRAST verdict.
  #
  #   # ---- OUTPUT (STAGE 4) ----
  #   write method_out.json (exp_gen_sol_out), validate full/mini/preview.

  # ---------------------------------------------------------------------------
  # STAGE 4 -- output assembly (exp_gen_sol_out; one row per query)
  # ---------------------------------------------------------------------------
  # datasets grouped by corpus name into THREE groups:
  #   'locatedin_present', 'locatedin_absent_sibling', 'locatedin_absent_diffcomponent'.
  # Each example:
  #   input  = story[:1200] + '  || Q: what is the geographic relationship of <Xname> to <Yname>?'
  #   output = gold word ('located in' for present held_out/never_annotated; 'no-relation' for absent)
  #   predict_certificate, predict_certificate_goldread,
  #   predict_conf_thresh_verbalized, predict_conf_thresh_sc_margin, predict_conf_thresh_ptrue, predict_conf_thresh_negent,
  #   predict_queryside_verifier, predict_queryside_selfverify,
  #   predict_commit_argmax (=raw), predict_pot, predict_sc,
  #   gold, metadata_regime ('held_out'|'never_annotated'|'same_component_sibling'|'different_component'),
  #   metadata_reader ('gemini-3.1-flash-lite' | 'deepseek-v3.2'), metadata_doc_id, metadata_title,
  #   metadata_qsrc/qtgt (entity_ids) + metadata_qsrc_name/qtgt_name, metadata_hop, metadata_composed_only,
  #   per-signal confidences (metadata_conf_*), metadata_n_extracted_edges, metadata_certificate_info.
  # metadata block carries: FACT-A table (per regime x reader, rate + confidence distribution),
  #   fraction-caught crux table (per signal x reader: survival AND 1-survival),
  #   mixed-pool leaderboards (SIBLING primary + DIFFCOMPONENT contrast) with certificate-vs-each-baseline
  #   selective accuracy @ matched coverage and Holm-adjusted confident-wrong reductions with CIs,
  #   abstention decomposition (correct-absent vs over-abstain-present), present coverage + selective accuracy,
  #   GOLD-READ CEILING, natural-prose atomic P/R (converse-invariant primitive PRIMARY + strict secondary +
  #   vs-locally-justifiable ceiling), default-vs-best-effort extraction comparison, cross-reader comparison,
  #   cost ledger (client.stats()), one worked sibling no-derivation trace + one over-abstain-present trace
  #   (Prolog-discharged if swipl present else python-checked, labelled truthfully), and the explicit FORK verdict.
  # Tag EVERY number REAL-LLM-READ + NATURAL-PROSE + located-in domain. Then aii-json validate +
  #   generate mini/preview; aii-file-size-limit split if needed.

  # ---------------------------------------------------------------------------
  # CLI / RUN
  # ---------------------------------------------------------------------------
  #   uv run method.py --slice re-docred --cross-family --concurrency 16 --budget-hard 9.0 & PID=$!
  #   monitor: tail -f logs/run.log & ; check kill -0 $PID; wait $PID; echo $?
  #   (Caching makes re-runs $0; gradual scaling flags: --limit-docs N, --no-battery for smoke.)
fallback_plan: >-
  EXTRACTION-LIMITED (the most likely fork, still publishable): if natural-prose atomic recall is low (iter-7 kinship was
  0.376) the LLM-read certificate over-abstains on PRESENT held_out and the mixed-sibling Holm reductions include 0 -> emit
  verdict=EXTRACTION-LIMITED-BOUNDARY. The DIAGNOSTIC (FACT A high + the mixed-pool capability gap on the gold-read ceiling)
  still stands and the gold-read ceiling (expected ~1.0 present / ~1.0 absent abstention) isolates extraction as the binding
  constraint. PATH-2 HEDGE: run the best-effort few-shot + given-inventory extraction arm and, if its recall lifts present
  coverage enough that the mixed-sibling reductions turn positive with Holm-CIs excluding 0, report that as the DEMONSTRATED-FIX
  on the best-effort arm (label the arm honestly). COST: track client.cost after every batch; if approaching $9 -> (a) drop
  SC k from 10 to 5, (b) shrink the subsample (fewer docs / tighter per-doc caps), (c) skip the cross-family deepseek reader
  (report gemini-only with a note), (d) skip the best-effort extraction arm. The SHA-256 cache means partial progress is never
  lost and re-runs are $0. VERIFIER TIES CERTIFICATE: if the query-side verifier's confident-wrong on the sibling pool is
  statistically indistinguishable from the certificate's -> emit verdict=VERIFIER-SUFFICES (an honest negative: the structural
  certificate is not NEEDED for the absent stratum; the trained/prompted false-premise detector already handles it). FACT
  B READER-DEFEATED: if for the deployed reader >=3 of 4 dispersion signals catch >70% of fabrications (as deepseek did on
  kinship) report FACT B as reader-dependent and narrow the diagnostic to verbalized confidence / weaker readers -- do NOT
  claim family-level blindness. SWIPL ABSENT: prolog.discharge() already falls back to python-checked verification and labels
  it truthfully (iter-5/6/7 precedent) -- never imply swipl ran. CORPUS FIELD MISMATCH: if a gold_graph key differs from the
  spec (e.g. absent regime stored only as same_component bool, or composed_only missing), derive query_subtype by checking
  whether a direct (source,target) atomic edge EXISTS (held_out) vs not (never_annotated), and derive absent_regime from same_component
  (True=sibling, False=different_component); assert the round-trip (held_out deduces after ablation; siblings+diffcomp give
  EMPTY both directions) on a smoke sample and fail loudly if violated. DEEPSEEK UNAVAILABLE: the OpenRouterClient fallback
  chain already rotates models; if all fail, report primary-only. If the present held_out pool is too small after subsampling,
  raise the per-doc present cap and pull from more docs (present total is 3,510 -- ample). If aii-json lacks an exp_gen_sol_out
  schema, reuse the exact schema/validator invocation from the iter-7 experiment workspace.
testing_plan: |-
  GRADUAL mini->full with explicit confirmation gates (aii-long-running-tasks pattern); never launch the full battery before the engine is proven wired correctly.

  GATE 0 (no LLM): import kinship + Kinship(full['metadata']['composition_table']); assert base==['located_in','contains'], compose_types('located_in','located_in')=='located_in', compose_types('located_in','contains') is None, conv_type('located_in')=='contains'. Load 1 doc, build records; assert query_subtype/absent_regime are set. THE KEY ENGINE CHECK (mirrors the corpus verify.py): for every held_out present record, after closure_edges_drop_direct on r['gold_atomics'], query_modeA must EMIT 'located_in' (deduced via the alternative path); for every sibling AND different_component absent record, query_modeA over gold_atomics must return no_path (EMPTY) in BOTH directions. If this fails the wiring is wrong -- STOP and fix before spending. Print the gold-read ceiling on this sample (expect 1.0 present / 1.0 absent abstention).

  GATE 1 (smoke, tiny LLM): uv run method.py --slice re-docred --limit-docs 3 --no-battery. Confirms: located-in extraction prompt parses (>=1 grounded edge on a multi-place doc), grounding recall plausible (~0.99 vs gold surfaces), raw/PoT parse to {located in,contains,no-relation}, the held_out extracted-edge ablation runs, predict_symbolic produces modeA + modeA_goldread, abstention_decomposition + atomic_pr run, output assembles + aii-json validates. Check the cost ledger is ~cents.

  GATE 2 (small battery+verifier, 1 reader): --limit-docs ~12 (drop --no-battery). Confirms run_battery (SC k=10 + P(True)) and run_queryside (verifier + selfverify) attach r['_sig'] and the two queryside method dicts; crux_survival_table prints survival AND fraction_caught; view3 matched-coverage showdown and cw_matched_to_ref run on mixed_sibling and mixed_diffcomp; holm_bonferroni over the 6 baselines returns p_adj/reject. Inspect FACT A on the sibling pool (>0 expected) and that certificate confident-wrong on absent ~ 0 (structural). Verify cost stays well under budget and scales roughly linearly.

  GATE 3 (full subsample, primary reader): run the stratified subsample (~400 held_out + 118 never_annotated + 450 sibling + 250 diffcomp, doc-clustered, per-doc caps). CONFIRMATION SIGNALS: gold-read ceiling ~1.0/1.0 (engine sound); FACT A_sibling >= 0.20 with a high-confidence mass; the mixed-sibling certificate selective accuracy beats every signal at matched coverage IF extraction recall is adequate; Holm reductions reported with CIs. Read the FORK verdict.

  GATE 4 (cross-family): add --cross-family (deepseek) only if budget remains; confirm FACT A + crux fraction-caught + mixed-sibling Holm replicate the reader-generality story; record reader-dependence of FACT B honestly.

  FINAL VALIDATION: aii-json validate full/mini/preview of method_out.json; aii-file-size-limit split if oversized; assert every example carries all predict_* keys + gold + metadata_regime + metadata_reader; assert the metadata block contains the FACT-A table, fraction-caught crux table, both mixed leaderboards with Holm CIs, abstention decomposition, gold-read ceiling, atomic P/R, cross-reader block, cost ledger, both worked traces, and the explicit FORK verdict. Re-run end-to-end once to confirm cache replay is $0 and the verdict is stable.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_dA_3iFe_7fn_
type: research
title: >-
  No-Derivation Abstention vs Confidence Family; NeSy Reposition; Re-DocRED Absent Gold
summary: >-
  Pure-web research bundle ($0) for iter-6/iter-7 of the closure-certificate project, across three workstreams. (A) Pins the
  confidence/uncertainty selective-prediction family our STEP-A battery competes against -- verbalized confidence [Lin2022;
  Tian2023], self-consistency [Wang2023], P(True)/P(IK) [Kadavath2022], semantic entropy [Kuhn2023; Farquhar2024], SelfCheckGPT
  [Manakul2023], the abstention survey [Wen2024], learned temporal abstention [Zhou2026], and the adversarial internal-state-probe
  neighbour [Song2026] -- with verified BibTeX, per-method abstention signals + verbatim quotes, a paper-ready signals-vs-catches
  table, and a ~250-word drop-in differentiation paragraph arguing every signal is dispersion/confidence-driven and therefore
  BLIND to a confident, self-consistent absent-relation hallucination, whereas the certificate abstains STRUCTURALLY (no derivation
  path) regardless of confidence -- with honest scope (confidence baselines tie at matched coverage on ordinary uncertain
  deduction). (B) A timing-aware (as-of 2026-06-18) NeSy / qualitative-reasoning venue shortlist -- Neurosymbolic AI journal
  (rolling, the only open NeSy-family target now), NeSy 2026/2027, *SEM, KR 2026 (qualitative reasoning in scope), STRL, EMNLP/ARR
  -- a crisp 'why not ACL Knowledge Extraction' statement, and a recommendation to SWAP primary<->fallback. (C) Verifies Re-DocRED
  (tonytan48/Re-DocRED, arXiv:2205.12696, 2022.emnlp-main.580, MIT, splits 3,053/500/500, '~64.6% of triples missing' in original
  DocRED, recall 32.07->69.40), confirms kinship coverage (P22/P25/P26/P40/P3373 PRESENT; P1038 ABSENT), documents the false-negative
  pitfall + disconnected-component absent-gold methodology, and scouts alternative natural hosts (CustFRE = natural prose
  with explicit no_relation gold; KinshipQA = generated/synthetic, fails the natural bar). Directly retires the reviewer novelty
  MAJOR + venue MINOR and de-risks iter-7 STEP-B.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_RfjDpsGkBXDG
type: dataset
title: Natural-Text Located-In Absent-Relation Corpus from Re-DocRED + DocRED
summary: |-
  A document-level GEOGRAPHIC / ADMINISTRATIVE CONTAINMENT ('located-in') corpus over genuinely-natural Wikipedia introductory prose (Re-DocRED, the completeness-corrected re-annotation of DocRED; vanilla DocRED kept as a downgraded secondary slice). It is the STRUCTURAL TWIN of the iter-6 natural-kinship corpus and a SECOND genuinely-natural absent-relation domain, built to show the closure-certificate confidence-blindness diagnostic is NOT kinship-specific. Consumed by iter-8's domain-generality experiment. Built $0 LLM (deterministic cue check passes 100%, judge skipped).

  FORMAT: exp_sel_data_out, ONE ROW PER DOCUMENT, grouped by dataset. datasets=[{dataset:'re-docred', examples:[...]}, {dataset:'docred', examples:[...]}]. Each example: input=detokenized Wikipedia prose; output=json.dumps(gold_graph) with {doc_id, source, split, nodes, atomic_edges, query_edges, absent_relation_pairs, absent_pairs_source='structural_closure', contradiction_pairs}; plus flat metadata_* columns. Counts re-docred 2604 docs / docred 2080.

  ENGINE (drop-in): kinship.py forward least-fixpoint UNION closure is REUSED VERBATIM, parameterized by containment_composition_table.json — a DEGENERATE single-relation TRANSITIVE table (located_in∘located_in=located_in; contains∘contains=contains; ALL else UNDEFINED). NOT a relation algebra. Map each atomic edge to {a:source, b:target, type:primitive}; D[(s,t)]={located_in} EMIT, ∅ both directions ABSTAIN (absent), |D|>1 Mode-B conflict (0 here). Direction: source located_in target; P131/P17/P1376/P276 src=h tgt=t, P150/P36 INVERT.

  THREE STRATA. (1) Atomic located_in edges (LOC-LOC NER filter, deduped, true 2-cycles dropped), each flagged locally_justifiable (adjacent-sentence locality + surface cue); re-docred 20,825 edges, locally_justifiable_frac 0.588. (2) PRESENT deduction-required queries (re-docred 3,510), gold certain, TWO honest sub-types: never_annotated (118; pair never a direct edge, composed_only=true, provably non-circular — RARE because DocRED annotates geography near-transitively, a measured domain difference) and held_out (3,392; a directly-annotated located_in edge that is ALSO derivable via an alternative ≥2-hop path and is non-local — consumer MUST drop the single (source,target) atomic edge before querying, then the engine deduces it; SOUND because removing a redundant edge preserves the full transitive closure). (3) ABSENT no-derivation pairs (re-docred 24,088), two regimes: different_component (3,274; unrelated places, clean kinship-analog) and same_component_sibling (20,814; co-component, neither inside the other — the reviewer-named containment-specific regime). Per-doc caps present_cap=40, absent_cap=30 (stratified), atomic_cap=80; *_truncated flagged.

  QUALITY. Round-trip gate (verify.py) PASSES: never_annotated 367/367, held_out 4357/4357 (deduced after ablation), absent 41100/41100 empty in BOTH directions, every derivation_path a valid DIRECTED located_in chain, cue-present 19885/19885, Mode-B 0. offset_ok 0.988/0.990. Schema-validated 3/3 (full/mini/preview). Completeness correction (2079 shared titles): Re-DocRED +67.5% located-in edges and 2.8x present queries vs DocRED — so absent gold is TRUSTWORTHY only on re-docred; docred absent is DOWNGRADED. Char honesty: mean ~1025 chars, max 2969, NO doc reaches 3000 (no padding/concatenation — natural-text + absent-relation is the load-bearing property). Caveats: closed-world absent; composed_only is pair-level (not type-level as kinship); multi-parent DAG; admin_level node tag best-effort/non-load-bearing; P276 lower precision (~0 LOC-LOC on re-docred). See dataset_card.md / README.md.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
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
