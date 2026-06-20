# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 3 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 18:03:12 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx1
type: experiment
title: >-
  CLUTRR End-to-End: Kinship Closure-Certificate Pipeline Delivering All Four Umbrella Goal Items (atomic P/R, multi-hop accuracy
  vs chain length, SWI-Prolog trace-graph, absent-relation hallucination risk-coverage)
summary: >-
  Run ONE end-to-end neuro-symbolic pipeline on the already-prepared CLUTRR kinship gold graphs (dependency art_HS7-lxhZnU9m:
  clutrr_gen for accuracy-vs-hop + atomic P/R + trace; clutrr_disc for 71,684 within-document absent pairs). A cheap OpenRouter
  LLM (gemini-3.1-flash-lite primary, deepseek-v3.2 cross-family sensitivity) reads atomic kinship triples from each de-bracketed
  story; a finite-composition-table closure engine (kinship analogue of the reused PC-2 engine.py, with disjunction-preserving
  Mode-A + abstain-on-collapse Mode-B) recovers the held-out query relation. Deliver: (i) atomic-extraction P/R/F1 vs gold
  story_edges/edge_types with doc-clustered bootstrap CIs and a hop/noise breakdown; (ii) selective accuracy at MATCHED COVERAGE
  vs PoT/self-consistency/raw/naive-single-pass and accuracy-vs-chain-length (hops 2..10), Holm-adjusted doc-clustered paired
  bootstrap; (iii) a human-auditable trace-graph ACTUALLY discharged in apt-installed SWI-Prolog (pyswip primary, `swipl -s
  f.pl -g goal -t halt` subprocess fallback, honest 'python-checked' fallback if neither runs); (iv) an absent-relation confident-wrong
  (hallucination) reduction reported as a FULL risk-coverage curve with abstention stated, pre-registered minimum effect.
  Reuse stats.py (matched_coverage_mask, paired_bootstrap_gap, holm_bonferroni, clustered_bootstrap_ci) and llm.py (sha256
  disk cache, hard $9 cost-guard) verbatim. Emit method_out.json (exp_gen_sol_out schema) with per-story predict_* + gold,
  metadata tables, the Prolog execution log, a worked 3-entity example, and an explicit CONFIRM/SCOPE-BOUNDARY verdict.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # ===================================================================================
  # GOAL: one end-to-end CLUTRR run delivering umbrella goal items (i)-(iv) on NON-synthetic,
  # NON-temporal data. The DATASET IS ALREADY PREPARED by dependency art_HS7-lxhZnU9m -- DO NOT
  # re-download CLUTRR. Load the frozen gold graphs from the dependency's full_data_out parts.
  # Reuse engine.py/llm.py/stats.py from the iter-2 experiment workspace; kinship needs a small
  # dedicated closure module because the kinship table is a FINITE composition table, NOT a full
  # relation algebra (no general converse/intersection closure beyond the listed rules).
  # Budget: HARD cap $9 via llm.py cost-guard; track cumulative spend after every call. Closure is
  # millisecond/laptop. cpu_heavy (LLM I/O is async; bootstrap over a few thousand nets wants RAM).
  # ===================================================================================

  # ----- FILES TO CREATE in this experiment workspace -----
  #   dataio.py          : load + merge the prepared CLUTRR gold graphs, subsample, schemas
  #   kinship.py         : kinship finite-composition closure engine (Mode-A / Mode-B / naive)
  #   readers.py         : LLM atomic-extraction + per-path PoT + self-consistency + raw prompts
  #   baselines.py       : assemble Mode-A / naive / PoT / SC / raw with matched abstention signals
  #   prolog.py          : emit Prolog, apt-install swipl, discharge (pyswip -> subprocess -> python)
  #   method.py          : orchestrator (CLI: --mini/--scale N, --reader, --out method_out.json)
  #   tests.py           : 0-LLM unit tests (kinship compose vs gold_proof; naive-vs-full on chains)
  # COPY-REUSE verbatim from /ai-inventor/.../iter_2/gen_art/gen_art_experiment_1/:
  #   engine.py  (Algebra/QCN/pc2_full/naive_single_pass -- pattern reference + temporal sanity)
  #   llm.py     (OpenRouterClient: sha256 disk cache, BudgetExceeded hard cap, async run_batch,
  #               parse_relations) -- ADD a kinship synonym map; keep cost-guard intact
  #   stats.py   (matched_coverage_mask, selective_accuracy, paired_bootstrap_gap, holm_bonferroni,
  #               clustered_bootstrap_ci, mean_ci, page_test) -- use AS-IS

  # ===================================================================================
  # STAGE 0 -- DATA LOADING (dataio.py) -- NO network, data already frozen
  # ===================================================================================
  DATA_DIR = dependency art_HS7-lxhZnU9m out_dependency_files:
    full_data_out/full_data_out_1.json , full_data_out/full_data_out_2.json (each <100MB)
  def load_clutrr():
      parts = [json.load(p1), json.load(p2)]
      COMP = parts[0]['metadata']['composition_table']   # identical across parts; relation_types,
          # symmetric_types, inverse_pairs, surface_forms, surface_reverse, composition_rules,
          # derived_gendered_surface_composition, label_map(_reverse), semantics
      byname = defaultdict(list)
      for part in parts:
          for ds in part['datasets']:               # dataset in {clutrr_gen, clutrr_disc}
              byname[ds['dataset']].extend(ds['examples'])
      # each example: input(story, de-bracketed) ; output=json.dumps(gold_graph) ;
      #   metadata_hop_count, metadata_noise_type, metadata_fold, metadata_genders,
      #   metadata_atomic_facts[{source_name,target_name,kinship_relation,relation_type}],
      #   metadata_gold_proof, metadata_query{source_name,target_name,relation,target_int}
      # gold_graph(output): nodes[{entity_id,surface,gender}], edges(atomic, directed:
      #   (s,t,type) reads 'name[t] is name[s]'s kinship_relation'), query_edge, absent_relation_pairs
      return byname['clutrr_gen'], byname['clutrr_disc'], COMP

  # SUBSAMPLE (stay well under budget; deterministic seed). hops 5-10 are sparse -> take ALL.
  #   gen accuracy/atomic/iteration set: per hop bin take min(n_bin, CAP) with CAP=~400 for hops 2,3,4
  #     and ALL of hops 5..10 (gen has 185,105,155,135,124,122) -> ~1.5-2.0k stories.
  #   disc absent set: sample ~600-1000 two-component stories (metadata_num_components==2),
  #     use their absent_relation_pairs (cap 20/story already) -> a few thousand absent queries.
  # --mini uses mini_data_out.json (3/dataset); --scale N caps total stories to N for pilots.

  # ===================================================================================
  # STAGE 1 -- KINSHIP CLOSURE ENGINE (kinship.py) -- 0 LLM, deterministic
  # ===================================================================================
  # Relations are TYPES: child, inv-child, SO, sibling, grand, inv-grand, in-law, inv-in-law,
  #   sibling-in-law, un, inv-un. UNIVERSE = frozenset(all 11 types). 'no-relation' is handled
  #   STRUCTURALLY: no connecting path => query stays UNIVERSE => non-singleton => ABSTAIN.
  class Kinship:
      base = 11 relation types ; universe = frozenset(base)
      converse(t):  symmetric_types -> t ; inverse_pairs (both directions) -> inverse ; else None-skip
      def converse_set(S): return frozenset(conv(t) for t in S if conv(t))
      def compose_types(t1,t2):
          r = composition_rules.get(t1,{}).get(t2)         # rules[t1][t2]=t3 (gender-agnostic type)
          return frozenset({r}) if r is not None else universe   # UNDEFINED -> universe (SOUND: unknown)
      def compose(S1,S2): return widen-free union over t1 in S1, t2 in S2 of compose_types(t1,t2)
  # QCN over kinship types, mirroring engine.py QCN but with kinship compose/converse, NO identity
  # self-relation (query pairs are distinct nodes). Store M[(i,j)] = frozenset; seed converses.
  # set_edge(i,j,S): M[i][j]=S ; M[j][i]=converse_set(S)
  # pc2_full(qcn): Mackworth PC-2 worklist to fixpoint (copy engine.pc2_full structure):
  #   for refined (i,k): new = M[i][k] & compose(M[i][j], M[j][k]); if new==empty -> return (False=
  #   Mode-B inconsistency, n_fired); if new shrinks -> update + converse + requeue. Returns consistent flag.
  # naive_single_pass(qcn,u,v): ONE pass: R=universe; for w in nbrs[u] with (w,v) known:
  #   R &= compose(M[u][w], M[w][v]); return R. NO fixpoint, NO re-propagation.
  # KEY STRUCTURAL FACT (the iteration claim, by construction): on a hop-k chain the only known
  #   edges are adjacent links, so naive resolves hop-2 (w=middle) but returns UNIVERSE on hop>=3
  #   (no single intermediate bridges query in one step) -> ABSTAINS; full PC-2 derives it. So the
  #   full-minus-naive coverage gap is ~0 at hop2 and -> ~1 at hop>=3: clean H3 on real CLUTRR text.
  # query(qcn, qsrc, qtgt) -> relation-type SET R after closure ; answer-type = sole element if |R|==1.
  # ANSWER SURFACE: map (answer_type, gender_of(qtgt)) via surface_forms -> surface relation string
  #   (gender from gold genders; entity grounding is NOT the contribution -> use gold entity set+gender,
  #    state this explicitly). Compare surface to gold query_edge.kinship_relation (or via label_map int).

  # ===================================================================================
  # STAGE 2 -- LLM ATOMIC EXTRACTION = THE NEURAL READ (readers.py) -- goal item (i) + KB for (ii)
  # ===================================================================================
  # ONE extraction call per UNIQUE story (entity-normalized for cache hits). System prompt:
  #   'Extract every directly-stated family relationship as JSON triples {a, relation, b} meaning
  #    "b is a's relation". Use ONLY: son daughter father mother husband wife brother sister
  #    grandson granddaughter grandfather grandmother son-in-law daughter-in-law father-in-law
  #    mother-in-law brother-in-law sister-in-law nephew niece uncle aunt. State only relations the
  #    text explicitly gives; do NOT infer indirect/derived relations.' (Disjunctive option allowed:
  #    a triple may carry a sound set of surface alternatives; default singleton; UNDERDETERMINED if
  #    a span is ambiguous -> contributes universe to closure, lowering bite not recall.)
  # PARSE: surface -> (relation_type, gender) via COMP.surface_reverse ; build directed atomic edges.
  # ATOMIC P/R (goal i): entity-normalized, direction-aware match of extracted (a,type,b) vs gold
  #   edges (metadata_atomic_facts). precision=#correct/#extracted ; recall=#correct/#gold ; F1.
  #   Report doc-clustered bootstrap CI (stats.clustered_bootstrap_ci) + breakdown by hop_count and
  #   noise_type {none,supporting,irrelevant,disconnected} (disc test split mixes noise -> robustness).
  # Mode-A/naive KB = extracted atomic edges as disjunctive type sets (singleton per read unless the
  #   reader emitted a set / UNDERDETERMINED).

  # ===================================================================================
  # STAGE 3 -- DEDUCTION + BASELINES at MATCHED COVERAGE (baselines.py) -- goal item (ii)
  # ===================================================================================
  # For each story's held-out query (qsrc,qtgt) build a kinship QCN from EXTRACTED atomics, hold the
  # query pair at universe, then:
  #   MODE-A (ours): pc2_full -> R(qsrc,qtgt). |R|==1 -> emit surface(answer_type,gender); covered=1;
  #       conf=1.0. |R|>1/universe -> ABSTAIN; conf=1/|R|. |R|==0 (empty collapse) -> Mode-B flag,
  #       ABSTAIN, conf=0. (Mode-A confidence is graded so coverage can be swept for matched-coverage.)
  #   NAIVE (iteration contrast): naive_single_pass on the SAME extracted KB; singleton->emit else abstain.
  #   RAW LLM forced-single: prompt 'what is b to a? answer with ONE relation word + confidence 0-1';
  #       conf = verbalized confidence. (No abstain natively -> abstention via conf threshold.)
  #   SELF-CONSISTENCY: k=5 paraphrase/temperature samples of the raw query (tag-keyed in llm.py so
  #       samples cache separately); answer = modal vote; conf = vote margin (top fraction).
  #   PATH-OF-THOUGHTS: enumerate the gold/extracted entity path(s) qsrc..qtgt; ask the LLM to compose
  #       EACH path INDEPENDENTLY into one relation (the verified PoT contract: per-path, no cross-path
  #       intersection); answer = modal vote across paths; conf = path-agreement fraction; abstain when
  #       paths disagree (matched abstention signal). [PoT is the PRIMARY learned-composition baseline.]
  #   OFF (table-fixed, no composition): coverage 0 on deduction-required queries (C2 anchor).
  # MATCHED-COVERAGE (reuse stats.py exactly):
  #   c* = Mode-A coverage on the pool; mask_a = its covered set; for each baseline threshold its conf
  #   to c* via matched_coverage_mask; selective_accuracy + paired_bootstrap_gap (DOC-CLUSTERED:
  #   resample documents not queries -> pass doc ids; primary fixed-tau, sensitivity rematch=True).
  #   CONFIRMATORY family H1 = {modeA vs pot, modeA vs sc} (gateway), H2 = absent-relation reduction
  #   (Stage 4); holm_bonferroni over {H1_pot, H1_sc, H2}; report ADJUSTED CIs. naive/off/raw
  #   leaderboard reported too (raw & naive exploratory). Predicted: Mode-A TIES naive on hop-2 stratum
  #   (report as confirmation), BEATS naive on hop>=3 (H3).
  # ACCURACY-vs-CHAIN-LENGTH (goal ii): per hop bin 2..10, plot Mode-A / naive / PoT / SC / raw
  #   selective accuracy AND coverage; full-minus-naive coverage gap vs hop = the iteration curve
  #   (stats.page_test for monotone growth across hop bins -> H3).

  # ===================================================================================
  # STAGE 4 -- ABSENT-RELATION HALLUCINATION as RISK-COVERAGE (baselines.py) -- goal item (iv)
  # ===================================================================================
  # On clutrr_disc absent_relation_pairs (entities in DIFFERENT components => provably no-relation):
  #   Mode-A: no connecting path => query stays universe => non-singleton => ABSTAINS (correct).
  #   RAW LLM (forced): asked the relation of a no-relation pair -> hallucinates a kinship => CONFIDENT-WRONG.
  #   PoT/SC: given their abstention signals at matched coverage.
  # METRIC: CONFIDENT-WRONG rate = non-abstained predictions on absent pairs that name ANY relation
  #   (all are wrong; gold=no-relation). REPORT THE FULL RISK-COVERAGE CURVE (sweep each method's conf
  #   threshold over coverage in [0,1]; plot confident-wrong-rate vs coverage), NOT a single delta;
  #   state abstention/coverage ALONGSIDE every number (the iter-2 lesson: 0.65->0.0 was ~90% abstention
  #   -> trivial in isolation). PRE-REGISTER minimum effect: at MATCHED coverage equal to raw-LLM's
  #   natural answer rate, Mode-A confident-wrong rate must be lower by >= 0.20 absolute with
  #   doc-clustered bootstrap CI excluding 0 (H2 gateway). Also include a clean PRESENT/ABSENT mixed pool
  #   so abstaining-on-everything cannot win (selective accuracy must hold on present pairs).

  # ===================================================================================
  # STAGE 5 -- TRACE-GRAPH + ACTUAL SWI-PROLOG DISCHARGE (prolog.py) -- goal item (iii)
  # ===================================================================================
  # apt-get install -y swi-prolog (target >=8.4.2); pip install -U pyswip (v0.3.3).
  # For a sample of ~30-50 solved gen queries (spanning hops 2..10) + the worked 3-entity example,
  # emit a Prolog program per query:
  #   comp(T1,T2,T3).            % from COMP.composition_rules (gender-agnostic type composition)
  #   conv(T,Tc).                % from inverse_pairs (both dirs) + symmetric_types (self-converse)
  #   rel(A,T,B).                % extracted atomic edges, asserted BOTH directions via conv/2
  #   derive(A,B,R) :- rel(A,R,B).
  #   derive(A,B,R) :- rel(A,R1,M), derive(M,B,R2), comp(R1,R2,R).   % transitive composition
  #   :- (setof(R, derive(qsrc,qtgt,R), Rs) -> ... ; ...).           % print the derived set
  # DISCHARGE order: (1) pyswip class-method Prolog(); consult; list(prolog.query(goal)).
  #   (2) FALLBACK subprocess: write f.pl; `swipl -s f.pl -g run -t halt` (exit 0/1/2); capture stdout.
  #   (3) If neither runs: compute via kinship.py Python re-impl and LABEL OUTPUT TRUTHFULLY
  #   'validated by a Python re-implementation, NOT executed in SWI-Prolog' (NEVER imply execution).
  # CROSS-CHECK each discharge: Prolog-derived R == engine Mode-A R == gold (and matches
  #   metadata_gold_proof backward-chaining). Save full stdout/stderr + exit codes to the execution log.
  # TRACE-GRAPH: for the worked example emit the QCN, which compositions fired on which path, the
  #   Prolog proof, and the gold_proof chain -> a human-auditable replayable record.

  # ===================================================================================
  # STAGE 6 -- OUTPUT ASSEMBLY (method.py) -> method_out.json (exp_gen_sol_out)
  # ===================================================================================
  # Schema mirrors iter-2: {"metadata": {...}, "datasets": [{"dataset": name, "examples":[...]}]}.
  # Per example (one per scored story/query): input=story[:2800], output=gold surface relation,
  #   predict_modeA / predict_naive / predict_raw / predict_pot / predict_sc (each a relation or
  #   'ABSTAIN'), plus per-example covered flags + conf. metadata holds, TAGGED by evidence class:
  #   - atomic_pr: {precision, recall, f1, ci, by_hop, by_noise_type}              (goal i)
  #   - deduction: {matched_coverage c*, leaderboard{modeA,naive,pot,sc,raw,off}, H1 holm+adj-CIs,
  #                 accuracy_vs_hop table (2..10), full_minus_naive_gap_vs_hop, H3 page p}  (goal ii)
  #   - absent_relation: {risk_coverage_curve per method, confident_wrong@matched_cov, H2 holm+CI,
  #                       abstention_rates}                                          (goal iv)
  #   - prolog: {installed:bool, engine:'pyswip'|'subprocess'|'python-fallback', n_discharged,
  #              n_crosscheck_match, sample execution logs}                         (goal iii)
  #   - worked_example_3entity: {story, extracted atomics, Mode-A narrowing trace, one Mode-B collapse,
  #                              Prolog proof}
  #   - budget: llm.stats() (cumulative_usd, n_llm_calls, n_cache_hits) ; reader id(s)
  #   - verdict: explicit CONFIRM vs SCOPE-BOUNDARY per claim (H1/H2/H3) with the pre-registered bars.
  # VALIDATE with aii-json against exp_gen_sol_out; if >100MB split per aii-file-size-limit.

  # ===================================================================================
  # CROSS-FAMILY SENSITIVITY (optional, budget-permitting)
  # ===================================================================================
  # Re-run Stages 2-3 atomic-read + deduction with reader=deepseek/deepseek-v3.2 on a stratified
  # subsample (~200 stories) to show the closure gain is reader-agnostic at matched per-edge recall;
  # report each reader's atomic recall so the comparison is recall-matched. Only if cumulative < ~$5.
fallback_plan: >-
  DATA: the CLUTRR gold graphs are ALREADY built by the dependency -- if a full_data_out part is missing/corrupt, fall back
  to mini_data_out.json/preview_data_out.json (verify schema), then as a last resort `uv run data.py` in the dependency workspace
  (deterministic, downloads from the kliang5 raw CSV mirror + FB yamls; do NOT use load_dataset('CLUTRR/v1') which breaks
  on datasets>=4.0). KINSHIP ENGINE: if shoehorning into engine.py's Algebra/QCN (which needs a base-symbol identity and a
  full base x base compose table) is awkward, write the small dedicated dict-based closure in kinship.py (recommended) --
  it is ~80 lines and mirrors pc2_full/naive_single_pass exactly; cross-check it against metadata_gold_proof on ALL loaded
  rows (0 LLM) before trusting it. UNDEFINED COMPOSITIONS: CLUTRR deliberately excludes ambiguous compositions, so every gold
  chain is derivable in SOME order; if PC-2 leaves a query at universe on a gold-clean (noise_type=none) row, log it as an
  engine bug and fix order-independence (the worklist must try all triangles) -- do NOT silently count it as a Mode-A abstention.
  PROLOG: pyswip import/lib-discovery failure -> set SWI_HOME_DIR/LIBSWIPL_PATH then retry; still failing -> subprocess `swipl
  -s f.pl -g run -t halt`; swipl truly absent (apt blocked) -> Python re-impl with the EXPLICIT honest label 'NOT executed
  in SWI-Prolog' (this is acceptable per the hypothesis, but only if stated plainly). BUDGET: track llm.cost after every batch;
  if approaching $5 soft-stop the cross-family arm; if approaching $9 the llm.py guard raises BudgetExceeded and run_batch
  returns partials -- report on whatever completed (cache makes reruns free). Shrink CAP per hop bin (e.g. 150) and drop SC
  k to 3 / PoT to single-path if cost is tight. STATISTICS UNDERPOWER: if a hop bin or the absent pool is too small for a
  stable CI, MERGE bins (2-3 / 4-6 / 7-10), report nominal CIs, and label the stratum exploratory rather than fabricating
  power. NEGATIVE RESULTS ARE PUBLISHABLE: if Mode-A does NOT beat PoT/SC at matched coverage, or H2 misses the 0.20 bar,
  or full==naive even on hop>=3, report the SCOPE-BOUNDARY verdict honestly with the curves -- the umbrella goal items (atomic
  P/R, accuracy-vs-length, trace, risk-coverage) are still delivered. NO STORY REACHES 3000 chars (max 871) -- state this
  caveat plainly (real ~3000-char docs live only in the temporal corpora); CLUTRR delivers the goal NUMBERS on clean non-synthetic
  non-temporal data, which is its job.
testing_plan: >-
  Scale gradually; never burn LLM budget before symbolic correctness is proven. STEP 1 (0 LLM, seconds): tests.py -- (a) load_clutrr()
  from full_data_out parts; assert COMP keys present, dataset names {clutrr_gen,clutrr_disc}, counts ~ (16131, 10545). (b)
  kinship.compose_types matches COMP.composition_rules on every listed cell; converse round-trips (conv(conv(t))==t) on inverse_pairs/symmetric.
  (c) DECISIVE engine check: for EVERY loaded row, build the QCN from metadata_atomic_facts (GOLD atomics, no LLM), run pc2_full,
  and assert the recovered query type maps (with target gender) to gold query_edge.kinship_relation -- expect ~100% on noise_type=none
  rows (0 violations is the go/no-go; investigate any miss as an order/closure bug). (d) iteration sanity: on synthetic chains
  of length 2..6, assert naive_single_pass resolves hop-2 but returns universe on hop>=3, while pc2_full resolves all -> confirms
  the H3 mechanism is real before any LLM. STEP 2 (--mini, ~6 stories, <$0.05): run the full pipeline end-to-end on mini_data_out.json
  -- LLM atomic extraction (check parse_relations maps surfaces -> types), Mode-A/naive/raw/PoT/SC predictions populate, matched-coverage
  harness returns finite numbers, absent-pair stories produce Mode-A ABSTAIN, method_out.json validates against exp_gen_sol_out.
  Inspect 2-3 worked traces by eye for correctness. STEP 3 (Prolog smoke test, 0 LLM): apt-install swipl; discharge the worked
  3-entity example; confirm pyswip OR subprocess returns the same relation set as kinship.py; record which engine ran. STEP
  4 (--scale 50, <$0.50): confirm caching hit-rate climbs on entity-normalized prompts, cost projection for full run < $9,
  no API errors, doc-clustered bootstrap produces non-degenerate CIs. CONFIRMATION SIGNALS before full run: gold-atomic engine
  check ~100%; mini Mode-A abstains on all absent pairs; atomic-extraction recall on mini is non-trivial (>0.5); naive coverage
  collapses on hop>=3 in the synthetic check. STEP 5 (full subsample): run; verify cumulative cost logged, Holm-adjusted H1/H2
  computed, accuracy-vs-hop and risk-coverage tables emitted, verdict line set. Re-run is free (cache) so iterate on analysis
  without re-billing. Keep a logs/run.log; manage the run by PID (uv run method.py & PID=$!), never by process name.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_Dm5vYXmD1R8h
type: research
title: Iter-2 Local-Reader / Prolog-Discharge / CLUTRR Implementation-Decision Dossier
summary: >-
  Executor-ready, web-verified resolution of the six NEW implementation decisions the iter-2 closure-certified text-to-logic
  experiments need (beyond the iter-1 dossier art_aQ2Rf8rwqteI). (1) LOCAL-READER PROTOCOL: minimal-span unit = the single
  sentence containing each event mention (default; +/-1 sentence as a sensitivity arm), grounded in TimeBank-Dense's own annotation
  window (same-sentence + immediately-following-sentence + DCT; 5 relations BEFORE/AFTER/INCLUDES/IS_INCLUDED/SIMULTANEOUS
  + VAGUE=underdetermined); 'no shared span' = mentions never co-occur within the window => DEDUCTION-REQUIRED, computable
  WITHOUT the LLM (T0-safe); disjunctive Pairwise read prompt adapted from Wei et al. arXiv:2407.19568 (Bulk/Iterative/Event-Ranking/Pairwise)
  + METRE arXiv:2408.07353 multi-label, enumerate base relations + explicit UNIVERSAL option, 'name every relation the text
  does NOT rule out'. (2) DISCHARGE: SWI-Prolog via pyswip v0.3.3 (class-method Prolog.assertz/query, Python>=3.9, needs apt
  swi-prolog>=8.4.2, ctypes shared-lib + SWI_HOME_DIR/LIBSWIPL_PATH) PRIMARY, robust subprocess fallback `swipl -s f.pl -g
  goal -t halt` (exit 0/1/2), clingo 5.8.0 ASP as secondary; QCN encoded as edge(E1,E2,RelSet) + algebra-seeded compose/3,converse/2;
  readback |R|==1 emit / |R|>1 ABSTAIN / |R|==0 unsound-flag; CONFIDENT-WRONG = nonabstained-single-relation-mismatch-rate
  on the deduction-required/absent subset, matched-coverage, paired-bootstrap CI, pre-registered MDE, aligned to Logic-LM/LINC
  executable-rate practice. (3) CLUTRR: HF CLUTRR/v1 (14 configs, target 0-20 mapping, fields incl proof_state/f_comb/story_edges/edge_types)
  BUT datasets>=4.0 dropped scripts => load via huggingface_hub snapshot_download of the per-task CSVs (git-LFS) or pin datasets<4.0
  + trust_remote_code; kinship composition table = rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender
  map (no-relation is a native primitive); absent-relation pairs CONSTRUCTED from rob_train_disc disconnected components /
  cross-family pairs; atomic-gold = story_edges+edge_types. (4) STRONGER READER: weak anchor = iter-1 google/gemini-3.1-flash-lite
  ($0.25/$1.50); recommend deepseek/deepseek-v3.2 ($0.2288/$0.3432, cross-family, CHEAPER, gate test ~$1.3) as budget-optimal
  stronger reader, google/gemini-3-flash-preview ($0.50/$3.00 thinking) as the clear capability-jump option on a stratified
  subsample; total two-reader run < $10 with disk cache + prompt caching + hard cost-guard. (5) SEVEN local-regime baselines
  each re-specified to read ONLY local spans with a matched single-relation abstention signal (raw verbalized-confidence,
  CoT, self-consistency vote-margin, LINC formalization-agreement, PoT path-agreement [confirmed per-path INDEPENDENT, no
  cross-path intersection], ILP-commit Eirew M=5, naive single-pass intersection), all thresholded to the SAME coverage object.
  (6) Four recent temporal/logical-consistency citations pinned (arXiv:2510.15513, 2502.11425, 2412.16100, 2409.14065) + a
  crisp novelty statement (disjunction-preserving abstain-on-collapse OUTPUT CONTRACT + gold-free closure CERTIFICATE + redundancy-as-coding-rate,
  NOT the algebra). Includes a consolidated decision table, exact IDs/URLs, and a 12-item gotchas list.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_HS7-lxhZnU9m
type: dataset
title: 'CLUTRR kinship gold graphs: two hop-stratified slices with absent-relation pairs'
summary: |-
  The clean END-TO-END venue for the closure-certificate umbrella, beside the iter-1 temporal corpora (NarrativeTime/TDDMan/MATRES) and the synthetic-QCN backbone. Standardizes CLUTRR (Sinha et al., EMNLP 2019, arXiv:1908.06177) into the aii exp_sel_data_out schema, ONE ROW per story, so iter-3 can deliver — in ONE setting — all four numbers the umbrella names: (i) atomic-extraction precision/recall, (ii) multi-hop deduction accuracy vs chain length, (iii) a human-auditable trace-graph, and (iv) a hallucination-rate reduction on absent-relation queries.

  THE BEST 2 DATASETS (26,676 rows total; target_num_datasets=2): clutrr_gen (gen_train234_test2to10; 16,131 rows; clean; train hops 2-3-4, TEST hops 2..10 → the accuracy-vs-length curve + atomic P/R + trace-graph) and clutrr_disc (rob_train_disc_23_test_all_23; 10,545 rows; disconnected-noise → 10,244 two-component stories yielding 71,684 genuine within-document ABSENT pairs for the hallucination demo; its test split also mixes clean/supporting/irrelevant/disconnected noise, so distractor examples for P/R robustness are present without a 3rd slice). The plan's explicitly-optional 3rd slice clutrr_sup is kept reproducible behind `uv run data.py --include-sup` (off by default).

  PER ROW: input = de-bracketed natural-language story; output = json.dumps(gold_graph) = nodes [{entity_id, surface, gender, mention_spans=[[start,end) into input]}] + typed ATOMIC edges (the directly-stated proof-chain facts: {source,target,kinship_relation gendered surface, relation_type abstract, is_query=false, hop_count=1}; directed: t is source's relation) + noise_edges (extra story_edges CLUTRR does NOT type; structural only) + the held-out query_edge ({source,target,kinship_relation=gold,relation_type,target_int,is_query=true,hop_count}; deduced by composing >=2 atomics) + absent_relation_pairs (entity pairs in DIFFERENT connected components ⇒ provably no kinship path ⇒ 'no-relation'; structural/conservative, capped 20/story). Flat metadata_* per row: fold (train/dev/test), corpus, hop_count, noise_type {none,supporting,irrelevant,disconnected}, task_name, f_comb, query, atomic_facts, gold_proof (backward-chaining decomposition = trace-graph gold), genders, num_entities/num_atomic_edges/num_noise_edges/num_components/absent_pair_count, story_char_len. Top-level metadata emits ONCE the finite kinship COMPOSITION TABLE read verbatim from facebookresearch/clutrr (rules_store.yaml/relations_store.yaml): 11 relation TYPES (+inverse/symmetry flags), (type×gender)→surface map and reverse, composition rules rules[t1][t2]=t3, int↔text label_map 0..20, and a derived gendered surface composition table — explicitly NOT a full relation algebra.

  RECONSTRUCTION (verified on all 26,676 source rows, 0 violations): node_id→name = genders order (verified consistent with proof leaves on every row); atomic edges = story_edges[:len(edge_types)] (the proof chain is always the prefix); noise edges = story_edges[len(edge_types):] (left untyped, NOT fabricated — a word-before-bracket heuristic recovers only ~54% even on known edges). VERIFIED noise_type↔task mapping (config↔task correspondence): {1 none, 2 supporting, 3 irrelevant, 4 disconnected}; label_map matches the canonical 0..20 order; build flags={} (0 span mismatches, 0 missing genders, 0 hop disagreements, 0 proof-leaf inconsistencies).

  DESCRIPTIVE COUNTS ONLY (no composition/closure, no P/R/accuracy/N*/hallucination numbers, no LLM — those are iter-3): 26,676 stories, 124,819 entities, 78,472 typed atomic edges, 10,545 noise edges; folds train 20,144/dev 5,039/test 1,493; hops 2(10,235),3(10,514),4(5,101),5-10(826). HONEST CAVEAT: CLUTRR stories are short — min 39/median 201/MAX 871 chars; NONE reach the umbrella's ~3000-char target (n_ge_3000_chars=0) — reported, not hidden; longer documents must come from the temporal corpora.

  FILES: full corpus split into full_data_out/full_data_out_1.json + full_data_out_2.json (each <100 MB; merge examples of the same dataset name across parts to reconstruct), mini_data_out.json (3 examples/dataset, incl. multi-hop + absent-pair rows), preview_data_out.json (10 examples/dataset, strings truncated; spans hops 2..10 and absent pairs), results/dataset_metadata.json (QA/provenance/data card). Reproduce: `uv run data.py` (downloads CSVs from the kliang5 raw mirror HF CLUTRR/v1 points at + the FB yamls; deterministic, no randomness). License: CLUTRR is research/non-commercial (CC-BY-NC-style; facebookresearch/clutrr LICENSE).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
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

### [2] HUMAN-USER prompt · 2026-06-17 18:03:12 UTC

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

### [3] SKILL-INPUT — aii-python · 2026-06-17 18:03:18 UTC

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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-17 18:03:18 UTC

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

### [5] SKILL-INPUT — aii-json · 2026-06-17 18:03:18 UTC

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

### [6] SKILL-INPUT — aii-file-size-limit · 2026-06-17 18:03:18 UTC

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

### [7] SKILL-INPUT — aii-use-hardware · 2026-06-17 18:03:18 UTC

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

### [8] SKILL-INPUT — aii-parallel-computing · 2026-06-17 18:03:18 UTC

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

### [9] SYSTEM-USER prompt · 2026-06-17 18:41:49 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx1
type: experiment
title: >-
  CLUTRR End-to-End: Kinship Closure-Certificate Pipeline Delivering All Four Umbrella Goal Items (atomic P/R, multi-hop accuracy
  vs chain length, SWI-Prolog trace-graph, absent-relation hallucination risk-coverage)
summary: >-
  Run ONE end-to-end neuro-symbolic pipeline on the already-prepared CLUTRR kinship gold graphs (dependency art_HS7-lxhZnU9m:
  clutrr_gen for accuracy-vs-hop + atomic P/R + trace; clutrr_disc for 71,684 within-document absent pairs). A cheap OpenRouter
  LLM (gemini-3.1-flash-lite primary, deepseek-v3.2 cross-family sensitivity) reads atomic kinship triples from each de-bracketed
  story; a finite-composition-table closure engine (kinship analogue of the reused PC-2 engine.py, with disjunction-preserving
  Mode-A + abstain-on-collapse Mode-B) recovers the held-out query relation. Deliver: (i) atomic-extraction P/R/F1 vs gold
  story_edges/edge_types with doc-clustered bootstrap CIs and a hop/noise breakdown; (ii) selective accuracy at MATCHED COVERAGE
  vs PoT/self-consistency/raw/naive-single-pass and accuracy-vs-chain-length (hops 2..10), Holm-adjusted doc-clustered paired
  bootstrap; (iii) a human-auditable trace-graph ACTUALLY discharged in apt-installed SWI-Prolog (pyswip primary, `swipl -s
  f.pl -g goal -t halt` subprocess fallback, honest 'python-checked' fallback if neither runs); (iv) an absent-relation confident-wrong
  (hallucination) reduction reported as a FULL risk-coverage curve with abstention stated, pre-registered minimum effect.
  Reuse stats.py (matched_coverage_mask, paired_bootstrap_gap, holm_bonferroni, clustered_bootstrap_ci) and llm.py (sha256
  disk cache, hard $9 cost-guard) verbatim. Emit method_out.json (exp_gen_sol_out schema) with per-story predict_* + gold,
  metadata tables, the Prolog execution log, a worked 3-entity example, and an explicit CONFIRM/SCOPE-BOUNDARY verdict.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # ===================================================================================
  # GOAL: one end-to-end CLUTRR run delivering umbrella goal items (i)-(iv) on NON-synthetic,
  # NON-temporal data. The DATASET IS ALREADY PREPARED by dependency art_HS7-lxhZnU9m -- DO NOT
  # re-download CLUTRR. Load the frozen gold graphs from the dependency's full_data_out parts.
  # Reuse engine.py/llm.py/stats.py from the iter-2 experiment workspace; kinship needs a small
  # dedicated closure module because the kinship table is a FINITE composition table, NOT a full
  # relation algebra (no general converse/intersection closure beyond the listed rules).
  # Budget: HARD cap $9 via llm.py cost-guard; track cumulative spend after every call. Closure is
  # millisecond/laptop. cpu_heavy (LLM I/O is async; bootstrap over a few thousand nets wants RAM).
  # ===================================================================================

  # ----- FILES TO CREATE in this experiment workspace -----
  #   dataio.py          : load + merge the prepared CLUTRR gold graphs, subsample, schemas
  #   kinship.py         : kinship finite-composition closure engine (Mode-A / Mode-B / naive)
  #   readers.py         : LLM atomic-extraction + per-path PoT + self-consistency + raw prompts
  #   baselines.py       : assemble Mode-A / naive / PoT / SC / raw with matched abstention signals
  #   prolog.py          : emit Prolog, apt-install swipl, discharge (pyswip -> subprocess -> python)
  #   method.py          : orchestrator (CLI: --mini/--scale N, --reader, --out method_out.json)
  #   tests.py           : 0-LLM unit tests (kinship compose vs gold_proof; naive-vs-full on chains)
  # COPY-REUSE verbatim from /ai-inventor/.../iter_2/gen_art/gen_art_experiment_1/:
  #   engine.py  (Algebra/QCN/pc2_full/naive_single_pass -- pattern reference + temporal sanity)
  #   llm.py     (OpenRouterClient: sha256 disk cache, BudgetExceeded hard cap, async run_batch,
  #               parse_relations) -- ADD a kinship synonym map; keep cost-guard intact
  #   stats.py   (matched_coverage_mask, selective_accuracy, paired_bootstrap_gap, holm_bonferroni,
  #               clustered_bootstrap_ci, mean_ci, page_test) -- use AS-IS

  # ===================================================================================
  # STAGE 0 -- DATA LOADING (dataio.py) -- NO network, data already frozen
  # ===================================================================================
  DATA_DIR = dependency art_HS7-lxhZnU9m out_dependency_files:
    full_data_out/full_data_out_1.json , full_data_out/full_data_out_2.json (each <100MB)
  def load_clutrr():
      parts = [json.load(p1), json.load(p2)]
      COMP = parts[0]['metadata']['composition_table']   # identical across parts; relation_types,
          # symmetric_types, inverse_pairs, surface_forms, surface_reverse, composition_rules,
          # derived_gendered_surface_composition, label_map(_reverse), semantics
      byname = defaultdict(list)
      for part in parts:
          for ds in part['datasets']:               # dataset in {clutrr_gen, clutrr_disc}
              byname[ds['dataset']].extend(ds['examples'])
      # each example: input(story, de-bracketed) ; output=json.dumps(gold_graph) ;
      #   metadata_hop_count, metadata_noise_type, metadata_fold, metadata_genders,
      #   metadata_atomic_facts[{source_name,target_name,kinship_relation,relation_type}],
      #   metadata_gold_proof, metadata_query{source_name,target_name,relation,target_int}
      # gold_graph(output): nodes[{entity_id,surface,gender}], edges(atomic, directed:
      #   (s,t,type) reads 'name[t] is name[s]'s kinship_relation'), query_edge, absent_relation_pairs
      return byname['clutrr_gen'], byname['clutrr_disc'], COMP

  # SUBSAMPLE (stay well under budget; deterministic seed). hops 5-10 are sparse -> take ALL.
  #   gen accuracy/atomic/iteration set: per hop bin take min(n_bin, CAP) with CAP=~400 for hops 2,3,4
  #     and ALL of hops 5..10 (gen has 185,105,155,135,124,122) -> ~1.5-2.0k stories.
  #   disc absent set: sample ~600-1000 two-component stories (metadata_num_components==2),
  #     use their absent_relation_pairs (cap 20/story already) -> a few thousand absent queries.
  # --mini uses mini_data_out.json (3/dataset); --scale N caps total stories to N for pilots.

  # ===================================================================================
  # STAGE 1 -- KINSHIP CLOSURE ENGINE (kinship.py) -- 0 LLM, deterministic
  # ===================================================================================
  # Relations are TYPES: child, inv-child, SO, sibling, grand, inv-grand, in-law, inv-in-law,
  #   sibling-in-law, un, inv-un. UNIVERSE = frozenset(all 11 types). 'no-relation' is handled
  #   STRUCTURALLY: no connecting path => query stays UNIVERSE => non-singleton => ABSTAIN.
  class Kinship:
      base = 11 relation types ; universe = frozenset(base)
      converse(t):  symmetric_types -> t ; inverse_pairs (both directions) -> inverse ; else None-skip
      def converse_set(S): return frozenset(conv(t) for t in S if conv(t))
      def compose_types(t1,t2):
          r = composition_rules.get(t1,{}).get(t2)         # rules[t1][t2]=t3 (gender-agnostic type)
          return frozenset({r}) if r is not None else universe   # UNDEFINED -> universe (SOUND: unknown)
      def compose(S1,S2): return widen-free union over t1 in S1, t2 in S2 of compose_types(t1,t2)
  # QCN over kinship types, mirroring engine.py QCN but with kinship compose/converse, NO identity
  # self-relation (query pairs are distinct nodes). Store M[(i,j)] = frozenset; seed converses.
  # set_edge(i,j,S): M[i][j]=S ; M[j][i]=converse_set(S)
  # pc2_full(qcn): Mackworth PC-2 worklist to fixpoint (copy engine.pc2_full structure):
  #   for refined (i,k): new = M[i][k] & compose(M[i][j], M[j][k]); if new==empty -> return (False=
  #   Mode-B inconsistency, n_fired); if new shrinks -> update + converse + requeue. Returns consistent flag.
  # naive_single_pass(qcn,u,v): ONE pass: R=universe; for w in nbrs[u] with (w,v) known:
  #   R &= compose(M[u][w], M[w][v]); return R. NO fixpoint, NO re-propagation.
  # KEY STRUCTURAL FACT (the iteration claim, by construction): on a hop-k chain the only known
  #   edges are adjacent links, so naive resolves hop-2 (w=middle) but returns UNIVERSE on hop>=3
  #   (no single intermediate bridges query in one step) -> ABSTAINS; full PC-2 derives it. So the
  #   full-minus-naive coverage gap is ~0 at hop2 and -> ~1 at hop>=3: clean H3 on real CLUTRR text.
  # query(qcn, qsrc, qtgt) -> relation-type SET R after closure ; answer-type = sole element if |R|==1.
  # ANSWER SURFACE: map (answer_type, gender_of(qtgt)) via surface_forms -> surface relation string
  #   (gender from gold genders; entity grounding is NOT the contribution -> use gold entity set+gender,
  #    state this explicitly). Compare surface to gold query_edge.kinship_relation (or via label_map int).

  # ===================================================================================
  # STAGE 2 -- LLM ATOMIC EXTRACTION = THE NEURAL READ (readers.py) -- goal item (i) + KB for (ii)
  # ===================================================================================
  # ONE extraction call per UNIQUE story (entity-normalized for cache hits). System prompt:
  #   'Extract every directly-stated family relationship as JSON triples {a, relation, b} meaning
  #    "b is a's relation". Use ONLY: son daughter father mother husband wife brother sister
  #    grandson granddaughter grandfather grandmother son-in-law daughter-in-law father-in-law
  #    mother-in-law brother-in-law sister-in-law nephew niece uncle aunt. State only relations the
  #    text explicitly gives; do NOT infer indirect/derived relations.' (Disjunctive option allowed:
  #    a triple may carry a sound set of surface alternatives; default singleton; UNDERDETERMINED if
  #    a span is ambiguous -> contributes universe to closure, lowering bite not recall.)
  # PARSE: surface -> (relation_type, gender) via COMP.surface_reverse ; build directed atomic edges.
  # ATOMIC P/R (goal i): entity-normalized, direction-aware match of extracted (a,type,b) vs gold
  #   edges (metadata_atomic_facts). precision=#correct/#extracted ; recall=#correct/#gold ; F1.
  #   Report doc-clustered bootstrap CI (stats.clustered_bootstrap_ci) + breakdown by hop_count and
  #   noise_type {none,supporting,irrelevant,disconnected} (disc test split mixes noise -> robustness).
  # Mode-A/naive KB = extracted atomic edges as disjunctive type sets (singleton per read unless the
  #   reader emitted a set / UNDERDETERMINED).

  # ===================================================================================
  # STAGE 3 -- DEDUCTION + BASELINES at MATCHED COVERAGE (baselines.py) -- goal item (ii)
  # ===================================================================================
  # For each story's held-out query (qsrc,qtgt) build a kinship QCN from EXTRACTED atomics, hold the
  # query pair at universe, then:
  #   MODE-A (ours): pc2_full -> R(qsrc,qtgt). |R|==1 -> emit surface(answer_type,gender); covered=1;
  #       conf=1.0. |R|>1/universe -> ABSTAIN; conf=1/|R|. |R|==0 (empty collapse) -> Mode-B flag,
  #       ABSTAIN, conf=0. (Mode-A confidence is graded so coverage can be swept for matched-coverage.)
  #   NAIVE (iteration contrast): naive_single_pass on the SAME extracted KB; singleton->emit else abstain.
  #   RAW LLM forced-single: prompt 'what is b to a? answer with ONE relation word + confidence 0-1';
  #       conf = verbalized confidence. (No abstain natively -> abstention via conf threshold.)
  #   SELF-CONSISTENCY: k=5 paraphrase/temperature samples of the raw query (tag-keyed in llm.py so
  #       samples cache separately); answer = modal vote; conf = vote margin (top fraction).
  #   PATH-OF-THOUGHTS: enumerate the gold/extracted entity path(s) qsrc..qtgt; ask the LLM to compose
  #       EACH path INDEPENDENTLY into one relation (the verified PoT contract: per-path, no cross-path
  #       intersection); answer = modal vote across paths; conf = path-agreement fraction; abstain when
  #       paths disagree (matched abstention signal). [PoT is the PRIMARY learned-composition baseline.]
  #   OFF (table-fixed, no composition): coverage 0 on deduction-required queries (C2 anchor).
  # MATCHED-COVERAGE (reuse stats.py exactly):
  #   c* = Mode-A coverage on the pool; mask_a = its covered set; for each baseline threshold its conf
  #   to c* via matched_coverage_mask; selective_accuracy + paired_bootstrap_gap (DOC-CLUSTERED:
  #   resample documents not queries -> pass doc ids; primary fixed-tau, sensitivity rematch=True).
  #   CONFIRMATORY family H1 = {modeA vs pot, modeA vs sc} (gateway), H2 = absent-relation reduction
  #   (Stage 4); holm_bonferroni over {H1_pot, H1_sc, H2}; report ADJUSTED CIs. naive/off/raw
  #   leaderboard reported too (raw & naive exploratory). Predicted: Mode-A TIES naive on hop-2 stratum
  #   (report as confirmation), BEATS naive on hop>=3 (H3).
  # ACCURACY-vs-CHAIN-LENGTH (goal ii): per hop bin 2..10, plot Mode-A / naive / PoT / SC / raw
  #   selective accuracy AND coverage; full-minus-naive coverage gap vs hop = the iteration curve
  #   (stats.page_test for monotone growth across hop bins -> H3).

  # ===================================================================================
  # STAGE 4 -- ABSENT-RELATION HALLUCINATION as RISK-COVERAGE (baselines.py) -- goal item (iv)
  # ===================================================================================
  # On clutrr_disc absent_relation_pairs (entities in DIFFERENT components => provably no-relation):
  #   Mode-A: no connecting path => query stays universe => non-singleton => ABSTAINS (correct).
  #   RAW LLM (forced): asked the relation of a no-relation pair -> hallucinates a kinship => CONFIDENT-WRONG.
  #   PoT/SC: given their abstention signals at matched coverage.
  # METRIC: CONFIDENT-WRONG rate = non-abstained predictions on absent pairs that name ANY relation
  #   (all are wrong; gold=no-relation). REPORT THE FULL RISK-COVERAGE CURVE (sweep each method's conf
  #   threshold over coverage in [0,1]; plot confident-wrong-rate vs coverage), NOT a single delta;
  #   state abstention/coverage ALONGSIDE every number (the iter-2 lesson: 0.65->0.0 was ~90% abstention
  #   -> trivial in isolation). PRE-REGISTER minimum effect: at MATCHED coverage equal to raw-LLM's
  #   natural answer rate, Mode-A confident-wrong rate must be lower by >= 0.20 absolute with
  #   doc-clustered bootstrap CI excluding 0 (H2 gateway). Also include a clean PRESENT/ABSENT mixed pool
  #   so abstaining-on-everything cannot win (selective accuracy must hold on present pairs).

  # ===================================================================================
  # STAGE 5 -- TRACE-GRAPH + ACTUAL SWI-PROLOG DISCHARGE (prolog.py) -- goal item (iii)
  # ===================================================================================
  # apt-get install -y swi-prolog (target >=8.4.2); pip install -U pyswip (v0.3.3).
  # For a sample of ~30-50 solved gen queries (spanning hops 2..10) + the worked 3-entity example,
  # emit a Prolog program per query:
  #   comp(T1,T2,T3).            % from COMP.composition_rules (gender-agnostic type composition)
  #   conv(T,Tc).                % from inverse_pairs (both dirs) + symmetric_types (self-converse)
  #   rel(A,T,B).                % extracted atomic edges, asserted BOTH directions via conv/2
  #   derive(A,B,R) :- rel(A,R,B).
  #   derive(A,B,R) :- rel(A,R1,M), derive(M,B,R2), comp(R1,R2,R).   % transitive composition
  #   :- (setof(R, derive(qsrc,qtgt,R), Rs) -> ... ; ...).           % print the derived set
  # DISCHARGE order: (1) pyswip class-method Prolog(); consult; list(prolog.query(goal)).
  #   (2) FALLBACK subprocess: write f.pl; `swipl -s f.pl -g run -t halt` (exit 0/1/2); capture stdout.
  #   (3) If neither runs: compute via kinship.py Python re-impl and LABEL OUTPUT TRUTHFULLY
  #   'validated by a Python re-implementation, NOT executed in SWI-Prolog' (NEVER imply execution).
  # CROSS-CHECK each discharge: Prolog-derived R == engine Mode-A R == gold (and matches
  #   metadata_gold_proof backward-chaining). Save full stdout/stderr + exit codes to the execution log.
  # TRACE-GRAPH: for the worked example emit the QCN, which compositions fired on which path, the
  #   Prolog proof, and the gold_proof chain -> a human-auditable replayable record.

  # ===================================================================================
  # STAGE 6 -- OUTPUT ASSEMBLY (method.py) -> method_out.json (exp_gen_sol_out)
  # ===================================================================================
  # Schema mirrors iter-2: {"metadata": {...}, "datasets": [{"dataset": name, "examples":[...]}]}.
  # Per example (one per scored story/query): input=story[:2800], output=gold surface relation,
  #   predict_modeA / predict_naive / predict_raw / predict_pot / predict_sc (each a relation or
  #   'ABSTAIN'), plus per-example covered flags + conf. metadata holds, TAGGED by evidence class:
  #   - atomic_pr: {precision, recall, f1, ci, by_hop, by_noise_type}              (goal i)
  #   - deduction: {matched_coverage c*, leaderboard{modeA,naive,pot,sc,raw,off}, H1 holm+adj-CIs,
  #                 accuracy_vs_hop table (2..10), full_minus_naive_gap_vs_hop, H3 page p}  (goal ii)
  #   - absent_relation: {risk_coverage_curve per method, confident_wrong@matched_cov, H2 holm+CI,
  #                       abstention_rates}                                          (goal iv)
  #   - prolog: {installed:bool, engine:'pyswip'|'subprocess'|'python-fallback', n_discharged,
  #              n_crosscheck_match, sample execution logs}                         (goal iii)
  #   - worked_example_3entity: {story, extracted atomics, Mode-A narrowing trace, one Mode-B collapse,
  #                              Prolog proof}
  #   - budget: llm.stats() (cumulative_usd, n_llm_calls, n_cache_hits) ; reader id(s)
  #   - verdict: explicit CONFIRM vs SCOPE-BOUNDARY per claim (H1/H2/H3) with the pre-registered bars.
  # VALIDATE with aii-json against exp_gen_sol_out; if >100MB split per aii-file-size-limit.

  # ===================================================================================
  # CROSS-FAMILY SENSITIVITY (optional, budget-permitting)
  # ===================================================================================
  # Re-run Stages 2-3 atomic-read + deduction with reader=deepseek/deepseek-v3.2 on a stratified
  # subsample (~200 stories) to show the closure gain is reader-agnostic at matched per-edge recall;
  # report each reader's atomic recall so the comparison is recall-matched. Only if cumulative < ~$5.
fallback_plan: >-
  DATA: the CLUTRR gold graphs are ALREADY built by the dependency -- if a full_data_out part is missing/corrupt, fall back
  to mini_data_out.json/preview_data_out.json (verify schema), then as a last resort `uv run data.py` in the dependency workspace
  (deterministic, downloads from the kliang5 raw CSV mirror + FB yamls; do NOT use load_dataset('CLUTRR/v1') which breaks
  on datasets>=4.0). KINSHIP ENGINE: if shoehorning into engine.py's Algebra/QCN (which needs a base-symbol identity and a
  full base x base compose table) is awkward, write the small dedicated dict-based closure in kinship.py (recommended) --
  it is ~80 lines and mirrors pc2_full/naive_single_pass exactly; cross-check it against metadata_gold_proof on ALL loaded
  rows (0 LLM) before trusting it. UNDEFINED COMPOSITIONS: CLUTRR deliberately excludes ambiguous compositions, so every gold
  chain is derivable in SOME order; if PC-2 leaves a query at universe on a gold-clean (noise_type=none) row, log it as an
  engine bug and fix order-independence (the worklist must try all triangles) -- do NOT silently count it as a Mode-A abstention.
  PROLOG: pyswip import/lib-discovery failure -> set SWI_HOME_DIR/LIBSWIPL_PATH then retry; still failing -> subprocess `swipl
  -s f.pl -g run -t halt`; swipl truly absent (apt blocked) -> Python re-impl with the EXPLICIT honest label 'NOT executed
  in SWI-Prolog' (this is acceptable per the hypothesis, but only if stated plainly). BUDGET: track llm.cost after every batch;
  if approaching $5 soft-stop the cross-family arm; if approaching $9 the llm.py guard raises BudgetExceeded and run_batch
  returns partials -- report on whatever completed (cache makes reruns free). Shrink CAP per hop bin (e.g. 150) and drop SC
  k to 3 / PoT to single-path if cost is tight. STATISTICS UNDERPOWER: if a hop bin or the absent pool is too small for a
  stable CI, MERGE bins (2-3 / 4-6 / 7-10), report nominal CIs, and label the stratum exploratory rather than fabricating
  power. NEGATIVE RESULTS ARE PUBLISHABLE: if Mode-A does NOT beat PoT/SC at matched coverage, or H2 misses the 0.20 bar,
  or full==naive even on hop>=3, report the SCOPE-BOUNDARY verdict honestly with the curves -- the umbrella goal items (atomic
  P/R, accuracy-vs-length, trace, risk-coverage) are still delivered. NO STORY REACHES 3000 chars (max 871) -- state this
  caveat plainly (real ~3000-char docs live only in the temporal corpora); CLUTRR delivers the goal NUMBERS on clean non-synthetic
  non-temporal data, which is its job.
testing_plan: >-
  Scale gradually; never burn LLM budget before symbolic correctness is proven. STEP 1 (0 LLM, seconds): tests.py -- (a) load_clutrr()
  from full_data_out parts; assert COMP keys present, dataset names {clutrr_gen,clutrr_disc}, counts ~ (16131, 10545). (b)
  kinship.compose_types matches COMP.composition_rules on every listed cell; converse round-trips (conv(conv(t))==t) on inverse_pairs/symmetric.
  (c) DECISIVE engine check: for EVERY loaded row, build the QCN from metadata_atomic_facts (GOLD atomics, no LLM), run pc2_full,
  and assert the recovered query type maps (with target gender) to gold query_edge.kinship_relation -- expect ~100% on noise_type=none
  rows (0 violations is the go/no-go; investigate any miss as an order/closure bug). (d) iteration sanity: on synthetic chains
  of length 2..6, assert naive_single_pass resolves hop-2 but returns universe on hop>=3, while pc2_full resolves all -> confirms
  the H3 mechanism is real before any LLM. STEP 2 (--mini, ~6 stories, <$0.05): run the full pipeline end-to-end on mini_data_out.json
  -- LLM atomic extraction (check parse_relations maps surfaces -> types), Mode-A/naive/raw/PoT/SC predictions populate, matched-coverage
  harness returns finite numbers, absent-pair stories produce Mode-A ABSTAIN, method_out.json validates against exp_gen_sol_out.
  Inspect 2-3 worked traces by eye for correctness. STEP 3 (Prolog smoke test, 0 LLM): apt-install swipl; discharge the worked
  3-entity example; confirm pyswip OR subprocess returns the same relation set as kinship.py; record which engine ran. STEP
  4 (--scale 50, <$0.50): confirm caching hit-rate climbs on entity-normalized prompts, cost projection for full run < $9,
  no API errors, doc-clustered bootstrap produces non-degenerate CIs. CONFIRMATION SIGNALS before full run: gold-atomic engine
  check ~100%; mini Mode-A abstains on all absent pairs; atomic-extraction recall on mini is non-trivial (>0.5); naive coverage
  collapses on hop>=3 in the synthetic check. STEP 5 (full subsample): run; verify cumulative cost logged, Holm-adjusted H1/H2
  computed, accuracy-vs-hop and risk-coverage tables emitted, verdict line set. Re-run is free (cache) so iterate on analysis
  without re-billing. Keep a logs/run.log; manage the run by PID (uv run method.py & PID=$!), never by process name.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_Dm5vYXmD1R8h
type: research
title: Iter-2 Local-Reader / Prolog-Discharge / CLUTRR Implementation-Decision Dossier
summary: >-
  Executor-ready, web-verified resolution of the six NEW implementation decisions the iter-2 closure-certified text-to-logic
  experiments need (beyond the iter-1 dossier art_aQ2Rf8rwqteI). (1) LOCAL-READER PROTOCOL: minimal-span unit = the single
  sentence containing each event mention (default; +/-1 sentence as a sensitivity arm), grounded in TimeBank-Dense's own annotation
  window (same-sentence + immediately-following-sentence + DCT; 5 relations BEFORE/AFTER/INCLUDES/IS_INCLUDED/SIMULTANEOUS
  + VAGUE=underdetermined); 'no shared span' = mentions never co-occur within the window => DEDUCTION-REQUIRED, computable
  WITHOUT the LLM (T0-safe); disjunctive Pairwise read prompt adapted from Wei et al. arXiv:2407.19568 (Bulk/Iterative/Event-Ranking/Pairwise)
  + METRE arXiv:2408.07353 multi-label, enumerate base relations + explicit UNIVERSAL option, 'name every relation the text
  does NOT rule out'. (2) DISCHARGE: SWI-Prolog via pyswip v0.3.3 (class-method Prolog.assertz/query, Python>=3.9, needs apt
  swi-prolog>=8.4.2, ctypes shared-lib + SWI_HOME_DIR/LIBSWIPL_PATH) PRIMARY, robust subprocess fallback `swipl -s f.pl -g
  goal -t halt` (exit 0/1/2), clingo 5.8.0 ASP as secondary; QCN encoded as edge(E1,E2,RelSet) + algebra-seeded compose/3,converse/2;
  readback |R|==1 emit / |R|>1 ABSTAIN / |R|==0 unsound-flag; CONFIDENT-WRONG = nonabstained-single-relation-mismatch-rate
  on the deduction-required/absent subset, matched-coverage, paired-bootstrap CI, pre-registered MDE, aligned to Logic-LM/LINC
  executable-rate practice. (3) CLUTRR: HF CLUTRR/v1 (14 configs, target 0-20 mapping, fields incl proof_state/f_comb/story_edges/edge_types)
  BUT datasets>=4.0 dropped scripts => load via huggingface_hub snapshot_download of the per-task CSVs (git-LFS) or pin datasets<4.0
  + trust_remote_code; kinship composition table = rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender
  map (no-relation is a native primitive); absent-relation pairs CONSTRUCTED from rob_train_disc disconnected components /
  cross-family pairs; atomic-gold = story_edges+edge_types. (4) STRONGER READER: weak anchor = iter-1 google/gemini-3.1-flash-lite
  ($0.25/$1.50); recommend deepseek/deepseek-v3.2 ($0.2288/$0.3432, cross-family, CHEAPER, gate test ~$1.3) as budget-optimal
  stronger reader, google/gemini-3-flash-preview ($0.50/$3.00 thinking) as the clear capability-jump option on a stratified
  subsample; total two-reader run < $10 with disk cache + prompt caching + hard cost-guard. (5) SEVEN local-regime baselines
  each re-specified to read ONLY local spans with a matched single-relation abstention signal (raw verbalized-confidence,
  CoT, self-consistency vote-margin, LINC formalization-agreement, PoT path-agreement [confirmed per-path INDEPENDENT, no
  cross-path intersection], ILP-commit Eirew M=5, naive single-pass intersection), all thresholded to the SAME coverage object.
  (6) Four recent temporal/logical-consistency citations pinned (arXiv:2510.15513, 2502.11425, 2412.16100, 2409.14065) + a
  crisp novelty statement (disjunction-preserving abstain-on-collapse OUTPUT CONTRACT + gold-free closure CERTIFICATE + redundancy-as-coding-rate,
  NOT the algebra). Includes a consolidated decision table, exact IDs/URLs, and a 12-item gotchas list.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_HS7-lxhZnU9m
type: dataset
title: 'CLUTRR kinship gold graphs: two hop-stratified slices with absent-relation pairs'
summary: |-
  The clean END-TO-END venue for the closure-certificate umbrella, beside the iter-1 temporal corpora (NarrativeTime/TDDMan/MATRES) and the synthetic-QCN backbone. Standardizes CLUTRR (Sinha et al., EMNLP 2019, arXiv:1908.06177) into the aii exp_sel_data_out schema, ONE ROW per story, so iter-3 can deliver — in ONE setting — all four numbers the umbrella names: (i) atomic-extraction precision/recall, (ii) multi-hop deduction accuracy vs chain length, (iii) a human-auditable trace-graph, and (iv) a hallucination-rate reduction on absent-relation queries.

  THE BEST 2 DATASETS (26,676 rows total; target_num_datasets=2): clutrr_gen (gen_train234_test2to10; 16,131 rows; clean; train hops 2-3-4, TEST hops 2..10 → the accuracy-vs-length curve + atomic P/R + trace-graph) and clutrr_disc (rob_train_disc_23_test_all_23; 10,545 rows; disconnected-noise → 10,244 two-component stories yielding 71,684 genuine within-document ABSENT pairs for the hallucination demo; its test split also mixes clean/supporting/irrelevant/disconnected noise, so distractor examples for P/R robustness are present without a 3rd slice). The plan's explicitly-optional 3rd slice clutrr_sup is kept reproducible behind `uv run data.py --include-sup` (off by default).

  PER ROW: input = de-bracketed natural-language story; output = json.dumps(gold_graph) = nodes [{entity_id, surface, gender, mention_spans=[[start,end) into input]}] + typed ATOMIC edges (the directly-stated proof-chain facts: {source,target,kinship_relation gendered surface, relation_type abstract, is_query=false, hop_count=1}; directed: t is source's relation) + noise_edges (extra story_edges CLUTRR does NOT type; structural only) + the held-out query_edge ({source,target,kinship_relation=gold,relation_type,target_int,is_query=true,hop_count}; deduced by composing >=2 atomics) + absent_relation_pairs (entity pairs in DIFFERENT connected components ⇒ provably no kinship path ⇒ 'no-relation'; structural/conservative, capped 20/story). Flat metadata_* per row: fold (train/dev/test), corpus, hop_count, noise_type {none,supporting,irrelevant,disconnected}, task_name, f_comb, query, atomic_facts, gold_proof (backward-chaining decomposition = trace-graph gold), genders, num_entities/num_atomic_edges/num_noise_edges/num_components/absent_pair_count, story_char_len. Top-level metadata emits ONCE the finite kinship COMPOSITION TABLE read verbatim from facebookresearch/clutrr (rules_store.yaml/relations_store.yaml): 11 relation TYPES (+inverse/symmetry flags), (type×gender)→surface map and reverse, composition rules rules[t1][t2]=t3, int↔text label_map 0..20, and a derived gendered surface composition table — explicitly NOT a full relation algebra.

  RECONSTRUCTION (verified on all 26,676 source rows, 0 violations): node_id→name = genders order (verified consistent with proof leaves on every row); atomic edges = story_edges[:len(edge_types)] (the proof chain is always the prefix); noise edges = story_edges[len(edge_types):] (left untyped, NOT fabricated — a word-before-bracket heuristic recovers only ~54% even on known edges). VERIFIED noise_type↔task mapping (config↔task correspondence): {1 none, 2 supporting, 3 irrelevant, 4 disconnected}; label_map matches the canonical 0..20 order; build flags={} (0 span mismatches, 0 missing genders, 0 hop disagreements, 0 proof-leaf inconsistencies).

  DESCRIPTIVE COUNTS ONLY (no composition/closure, no P/R/accuracy/N*/hallucination numbers, no LLM — those are iter-3): 26,676 stories, 124,819 entities, 78,472 typed atomic edges, 10,545 noise edges; folds train 20,144/dev 5,039/test 1,493; hops 2(10,235),3(10,514),4(5,101),5-10(826). HONEST CAVEAT: CLUTRR stories are short — min 39/median 201/MAX 871 chars; NONE reach the umbrella's ~3000-char target (n_ge_3000_chars=0) — reported, not hidden; longer documents must come from the temporal corpora.

  FILES: full corpus split into full_data_out/full_data_out_1.json + full_data_out_2.json (each <100 MB; merge examples of the same dataset name across parts to reconstruct), mini_data_out.json (3 examples/dataset, incl. multi-hop + absent-pair rows), preview_data_out.json (10 examples/dataset, strings truncated; spans hops 2..10 and absent pairs), results/dataset_metadata.json (QA/provenance/data card). Reproduce: `uv run data.py` (downloads CSVs from the kliang5 raw mirror HF CLUTRR/v1 points at + the FB yamls; deterministic, no randomness). License: CLUTRR is research/non-commercial (CC-BY-NC-style; facebookresearch/clutrr LICENSE).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
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

### [10] SYSTEM-USER prompt · 2026-06-17 18:43:32 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [11] SYSTEM-USER prompt · 2026-06-17 18:45:48 UTC

```
<validation-feedback>
Attempt 2 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [12] SYSTEM-USER prompt · 2026-06-17 18:53:00 UTC

```
<validation-feedback>
Attempt 3 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
