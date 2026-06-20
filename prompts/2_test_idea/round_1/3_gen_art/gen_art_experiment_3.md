# gen_art_experiment_3 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_3` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 13:57:19 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_3`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_3/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_3/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_3/results/out.json`
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
id: gen_plan_experiment_3_idx6
type: experiment
title: >-
  Recall-Bite Frontier & LLM Elicitation Go/No-Go (T0/Pilot for Closure-Certified Composition)
summary: >-
  A pre-main-run pilot that maps the recall-bite frontier and fixes the pre-registered LLM elicitation operating point. It
  samples temporal-relation edges (with raw text) from three real corpora (dense arm = TimeBank-Dense as a robust stand-in
  for NarrativeTime + start-point convex-point-algebra restriction; non-circular arm = TDDMan long-distance; gate-control
  = MATRES adjacent-sentence) plus a small clean-ground-truth synthetic battery, then sweeps a >=5-setting prompt BREADTH
  KNOB via a cheap OpenRouter model. At each setting it measures per-edge RECALL=P(gold in emitted set), breadth, over-commitment
  vs under-specification rates, raw closure-collapse rate on harvested triangles, strict-tightening AND singleton-resolution-to-correct
  yields, a local-only-reader probe (defines the deduction-required fraction), and the within-document cross-edge reading-error
  correlation rho (with empirical joint soundness J(E)). It plots the frontier, applies a pre-registered go/no-go, and emits
  aii-json-validated method_out.json with the frontier table, the SELECTED operating point, rho, deduction-required fraction,
  J(E), and cumulative OpenRouter spend. API-bound, no GPU, target spend < $2 (hard cap $10).
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  # =====================================================================
  # experiment_iter1_dir6 -- RECALL-BITE FRONTIER & ELICITATION GO/NO-GO
  # Role: T0/pilot viability gate for the closure-certified-composition study.
  # It does NOT run the main comparison; it decides whether the LLM can emit
  # SOUND-but-sub-universal disjunctive relation sets at usable recall with
  # non-trivial singleton-resolution yield, and fixes the operating point + rho
  # that iteration-2 (real-text comparison + synthetic realism match) will reuse.
  # Compute: cpu_heavy (NO GPU). API-bound. Closure runs in ms on CPU.
  # Skills to load: aii-openrouter-llms (LLM calls + pricing), aii-web-tools
  #   (download data files via fetch if git/curl unavailable), aii-parallel-computing
  #   (asyncio concurrency), aii-json (validate output), aii-file-size-limit,
  #   aii-python (logging/structure), aii-long-running-tasks (scale mini->full).
  # Read aii-openrouter-llms FIRST to confirm the current cheapest capable model.
  # =====================================================================

  ##### 0. CONFIG (all pre-registered constants; log them to method_out.json) #####
  SEED = 20260617
  MODEL_PRIMARY   = 'google/gemini-2.5-flash'        # verify via aii-openrouter-llms; pick cheapest CAPABLE
  MODEL_FALLBACKS = ['openai/gpt-5-mini', 'deepseek/deepseek-chat']  # if primary unavailable/too pricey
  TEMPERATURE = 0.0                                   # deterministic single emission (reproducible)
  MAX_EDGES_PER_CORPUS   = 150                         # modest pilot; scale down first (see testing)
  MAX_DOCS_PER_CORPUS    = 12                          # short docs (~3k chars) keep cost low
  MAX_TRIANGLES_PER_DOC  = 60                          # cap closure harvesting per doc
  CONCURRENCY = 12                                     # async OpenRouter calls in flight
  # --- pre-registered GO/NO-GO thresholds (fixed BEFORE any LLM call) ---
  RECALL_GATE_POINT = 0.90       # convex point-algebra (start-point) arm: PC complete -> demand high recall
  RECALL_GATE_ALLEN = 0.85       # coarse-interval (Allen) arm: sound-but-incomplete -> slightly lower bar
  APPLIC_GENERAL = 0.10          # singleton-resolution-to-correct fraction of deduction-required multi-path edges
  APPLIC_MODULE  = 0.05          #   >=0.10 GENERAL mechanism; 0.05-0.10 USEFUL MODULE; <0.05 NICHE/NO-GO
  BUDGET_USD_SOFT = 2.0; BUDGET_USD_HARD = 9.0   # STOP issuing calls if cumulative cost crosses HARD

  # >=5 BREADTH-KNOB settings, narrow -> maximal-sound (this IS the frontier axis):
  KNOB = {
    'S1_single':     'Name THE single temporal relation that holds. Output exactly one.',
    'S2_confident':  'Name the relation(s) you are confident hold; omit any you doubt.',
    'S3_plausible':  'Name every relation that plausibly holds given the text.',
    'S4_sound':      'Name ALL base relations the text does NOT exclude. Recall matters more than precision: it is better to include an extra relation than to omit the correct one. If the text does not constrain the order, output UNDERDETERMINED (the universal set).',
    'S5_maximal':    'List the MAXIMAL sound set: include every base relation not strictly ruled out by the text. Only drop a relation if the text makes it impossible. Use UNDERDETERMINED when nothing is excluded.'
  }

  ##### 1. DATA ACQUISITION (inline; depends_on=[] so this artifact fetches its own slices) #####
  # Use git clone (preferred) or curl/aii-web-tools fetch of raw files. All public, no license wall
  # for the .tml text we need (TempEval-3 TBAQ-cleaned).
  #  (a) TEXT source (.tml with inline <EVENT eid=..>word</EVENT> + <MAKEINSTANCE eventID eiid>):
  #        github.com/jspotter/TempEval-3  -> data/TBAQ-cleaned/TimeBank + AQUAINT (.tml)
  #        github.com/muk343/TimeBank-dense (36 TimeBank .tml, event eids aligned to TimeBank-Dense)
  #  (b) DENSE arm gold (stand-in for NarrativeTime; see fallback):
  #        TimeBank-Dense tlinks: docid \t e1 \t e2 \t {b,a,i,ii,s,v}  (try muk343 / CAEVO / KJETE mirror)
  #        ATTEMPT NarrativeTime/TimeBankNT first (github annargrs / paper links); if not cleanly
  #        downloadable in the time budget, USE TimeBank-Dense and LABEL it 'dense_arm=TimeBank-Dense
  #        (NarrativeTime stand-in for pilot)'. Pilot conclusions (can the LLM emit sound sub-universal
  #        sets? do triangles collapse?) do not depend on NarrativeTime's non-circular gold.
  #  (c) NON-CIRCULAR arm gold: github.com/aakanksha19/TDDiscourse -> TDDMan/TDDMan{Train,Dev,Test}.tsv
  #        format: docid \t e1 \t e2 \t rel  with rel in {b,a,i,ii,s}; ALL pairs >1 sentence apart.
  #  (d) GATE-CONTROL gold: github.com/CogComp/MATRES -> timebank.txt/aquaint.txt/platinum.txt
  #        format: docid verb1 verb2 eiid1 eiid2 rel  with rel in {BEFORE,AFTER,EQUAL,VAGUE}; same/adj-sentence.
  # Parse each .tml: extract plain text, record per-event (eid, eiid via MAKEINSTANCE, surface word,
  #   char offset, sentence index). Sentence-split with a simple splitter (regex on terminal punctuation
  #   or nltk/spacy if available). Build doc_text and event_index[docid][eid] = {word, sent_idx, char_span}.

  RELVOCAB = {  # canonical base-relation labels emitted to / parsed from the LLM, per arm
    'coarse':  ['before','after','includes','is_included','simultaneous'],  # TDDMan/TB-Dense/coarse-Allen
    'point':   ['<','=','>']                                                # start-point convex point algebra
  }
  UNIVERSAL = {'coarse': set(RELVOCAB['coarse']), 'point': {'<','=','>'}}
  # corpus gold-label normalization to coarse base:
  NORMALIZE = {'b':'before','a':'after','i':'includes','ii':'is_included','s':'simultaneous','v':'VAGUE',
               'BEFORE':'before','AFTER':'after','EQUAL':'simultaneous','VAGUE':'VAGUE',
               'INCLUDES':'includes','IS_INCLUDED':'is_included','SIMULTANEOUS':'simultaneous'}
  # VAGUE/v gold == universal target (any sound set is trivially correct) -> mark and EXCLUDE from
  # recall denominator for 'resolvable' metrics, but keep for breadth/coverage stats.

  ##### 2. EDGE & TRIANGLE SAMPLING (deterministic with SEED) #####
  for corpus in [dense_arm, TDDMan, MATRES]:
     docs = pick up to MAX_DOCS_PER_CORPUS docs with text available; prefer shortest (~3k chars)
     gold_edges[corpus] = [(docid,e1,e2,gold_coarse)] restricted to docs we have text for
     sample MAX_EDGES_PER_CORPUS edges (stratify: keep ALL relation classes; for dense_arm and TDDMan
          stratify by sentence-distance bins {same, adjacent, >1 sentence} so deduction-required edges present)
     # triangles for closure: per doc build graph of gold edges; enumerate triples (A,B,C) with all 3
     #   pairs gold-present; sample up to MAX_TRIANGLES_PER_DOC; ensure every triangle's 3 edges are in
     #   the elicitation set (add them if needed). Record each triangle's max pairwise sentence-distance
     #   (>1 => deduction-required triangle) and a structural hop label (length-2 path A-B-C resolving A-C).

  ##### 3. RELATION ALGEBRA & MINIMAL CLOSURE (pure-Python, no deps, runs in ms) #####
  # --- POINT ALGEBRA on event START-points (NarrativeTime/dense convex arm; PC COMPLETE) ---
  # base composition table comp_pt[r1][r2] (set result):
  #   '<'o'<'={<}; '<'o'='={<}; '<'o'>'=ALL; '='o r = {r}; '>'o'>'={>}; '>'o'='={>}; '>'o'<'=ALL
  # disjunctive composition = UNION over base pairs; intersection = set intersection (empty => contradiction).
  # map coarse gold/emitted -> start-point set:
  #   before->{<}; after->{>}; simultaneous->{=}; includes->{<,=}(<=); is_included->{=,>}(>=); VAGUE->{<,=,>}
  # --- COARSE INTERVAL (Allen) ARM (sound-but-INCOMPLETE; lower-bound detector) ---
  # map coarse -> Allen base: before->{b}; after->{bi}; includes->{di}; is_included->{d}; simultaneous->{eq};
  #   VAGUE->all 13. Implement Allen 13x13 composition by ENDPOINT method (robust, no 169-entry hardcode):
  #   represent interval X by points (Xs<Xe); each Allen base relation == a point-algebra config on
  #   (As,Ae,Bs,Be); compose two relations by point-algebra closure over shared endpoints; read back the
  #   set of consistent Allen base relations. (Alternative: hardcode the published Allen table or load the
  #   JSON table from the qualreas project github.com/alreich/qualreas -- but ship a self-contained version.)
  # Provide BOTH arms; POINT-ALGEBRA arm is PRIMARY for the dense corpus (completeness); coarse-Allen arm
  #   is reported as the lower-bound detector and used for TDDMan (coarse set, no VAGUE).

  def close_triangle(setAB, setBC, setAC, algebra):
     # path A-B-C constrains A-C: path = compose(setAB, setBC, algebra)
     path = compose(setAB, setBC, algebra)
     inter = path & setAC               # cross-path narrowing (Mode A) intersected w/ directly-read A-C
     return {'path':path, 'inter':inter, 'empty': len(inter)==0, 'singleton': len(inter)==1}

  ##### 4. LLM ELICITATION (OpenRouter, cached, concurrent, budget-guarded) #####
  # Build a deterministic disk CACHE keyed by sha256(model|arm|knob|prompt) -> parsed response JSON,
  #   so re-runs and identical (edge,knob) prompts never re-bill. Persist to ./cache/.
  # For each (corpus-arm, knob, edge): construct prompt =
  #   SYSTEM: 'You read temporal relations between two marked events in a news text. Allowed base
  #            relations: <ARM VOCAB>. <KNOB instruction>. Judge ONLY from the text; do NOT assume
  #            consistency with other pairs. Reply as JSON: {\"relations\":[...],\"underdetermined\":bool}.'
  #   USER: doc_text with the two target event mentions wrapped [[E1]]word[[/E1]] / [[E2]]word[[/E2]]
  #         + 'Relation of E1 to E2?'  (window to <= ~1500 tokens around the events if doc long)
  # CALL via aii-openrouter-llms with TEMPERATURE=0, json mode if available; parse robustly
  #   (map synonyms; UNDERDETERMINED/empty -> UNIVERSAL set; drop labels outside vocab and log).
  # Run with asyncio + semaphore(CONCURRENCY). After EACH call: cost += usage*price; if cost>BUDGET_USD_HARD: STOP.
  # emitted[arm][knob][edge] = parsed base-relation SET (already in arm vocab).
  #
  # LOCAL-ONLY READER PROBE (defines deduction-required fraction): for each held-out edge, build a probe
  #   prompt containing ONLY the minimal local span(s) where E1 and E2 co-occur (same/adjacent sentence);
  #   if no shared local span -> mark structurally DEDUCTION-REQUIRED, skip the call. Else elicit at the
  #   SELECTED-knob style and record local_correct = (gold in local emitted set & singleton-correct).
  #   deduction_required[edge] = (no shared span) OR (local probe fails to name gold singleton).

  ##### 5. METRICS per (arm, knob) -- the FRONTIER TABLE #####
  for arm, knob:
     recall            = mean over non-VAGUE edges of 1[gold in emitted_set]        # PRIMARY frontier axis
     breadth_mean/med  = distribution of |emitted_set|
     universal_rate    = frac(emitted_set == UNIVERSAL)                              # under-specification
     overcommit_rate   = frac(sound AND |set|<|universal| AND singleton-but-wrong-or-too-narrow-excluding-gold)
                         # decompose: under-spec (too broad/universal) vs over-commit (excludes gold)
     unsound_rate      = 1 - recall                                                 # gold excluded
     # closure on harvested triangles (use emitted sets at THIS knob; both algebra arms):
     collapse_rate     = frac(triangles with close_triangle.empty)                  # Mode-B detection signal
     strict_tighten    = frac(triangles where inter strictly subset setAC)          # any narrowing (reported, NOT load-bearing)
     singleton_to_correct = frac(triangles where inter is singleton AND == gold(A-C))# HEADLINE yield (load-bearing)
     singleton_to_correct_DEDUCTION = same restricted to deduction-required triangles# the applicability number's numerator
     # bite-lost (point arm vs coarse-Allen arm on SAME triangles):
     bite_lost = singleton_to_correct[Allen] - singleton_to_correct[point]          # info lost by convex restriction

  # rho (within-doc cross-edge reading-error correlation) at each knob:
  #   err_e = 1 - 1[gold in emitted_set]; compute INTRACLASS correlation of err grouped by docid
  #   (ICC, or: P(both edges in same doc err)/[P(err)^2] - 1 as a correlation-style ratio). rho>0 => positively
  #   correlated reading errors (single reader). Report rho per knob; the SELECTED knob's rho feeds iter-2.
  # J(E) empirical joint soundness: J(2)=frac(triangles where BOTH path edges AB,BC sound);
  #   where >=3-edge constraint paths exist, also J(3). Report J(2),J(3) and contrast vs independence r^E.

  # deduction_required_fraction[corpus] = mean(deduction_required[edge]) over evaluable edges  # for applicability

  ##### 6. FRONTIER PLOT + PRE-REGISTERED GO/NO-GO #####
  # Plot (matplotlib, save PNG/JPEG): x=recall, y=singleton_to_correct_DEDUCTION, size/color=collapse_rate,
  #   one marker per (arm,knob); overlay RECALL_GATE line. Also breadth-vs-recall and collapse-vs-knob plots.
  # SELECT operating point: among knobs whose recall >= RECALL_GATE (POINT arm: 0.90; coarse/TDDMan: 0.85),
  #   choose the one MAXIMIZING singleton_to_correct_DEDUCTION (tie -> higher recall). Record full row.
  # VERDICT:
  #   GO-GENERAL   if some arm has a recall-gated knob with singleton_to_correct_DEDUCTION >= APPLIC_GENERAL (0.10)
  #   GO-MODULE    if best is in [APPLIC_MODULE, APPLIC_GENERAL)  (0.05-0.10) -> proceed, scope as 'useful module'
  #   NO-GO/NICHE  if < APPLIC_MODULE on every arm OR no knob clears the recall gate -> recommend iter-2 demote
  #                real text to niche-safety-net and headline the SYNTHETIC arm (report honestly).
  # Report the EXPECTED gate-validation result: MATRES deduction_required_fraction ~ 0 and its
  #   singleton_to_correct_DEDUCTION ~ 0 (near-empty by construction) vs dense_arm/TDDMan >> 0.

  ##### 7. SYNTHETIC CLEAN-GROUND-TRUTH BATTERY (closure-code correctness + recall reference) #####
  # Generate ~30-60 small consistent QCNs: random total order of timepoints (point algebra) and a few
  #   interval scenarios (Allen); derive gold base relation per pair from the ground-truth order.
  # Realize each edge as a templated English sentence with surface variation ('X happened before Y',
  #   'during', 'while', 'after', 'at the same time as'); assemble a tiny doc per network.
  # Run the SAME elicitation+closure. Use this to (a) UNIT-TEST closure (known answers must match),
  #   (b) get a clean-text recall reference, (c) first rough TV-distance of error-type distribution
  #   real-vs-synthetic (full realism match is iter-2's job; report as exploratory).

  ##### 8. OUTPUT method_out.json (validate with aii-json; check size with aii-file-size-limit) #####
  # {
  #   'config': {seed, model_used, model_price, temperature, thresholds, n_edges/n_triangles per corpus, budget},
  #   'data_provenance': {dense_arm_source (NarrativeTime|TimeBank-Dense-standin), tddman_src, matres_src, text_src},
  #   'frontier_table': [ per (corpus,arm,knob): recall, breadth_mean/med, universal_rate, overcommit_rate,
  #                       unsound_rate, collapse_rate, strict_tighten, singleton_to_correct,
  #                       singleton_to_correct_DEDUCTION, rho, J2, J3 ],
  #   'selected_operating_point': {corpus, arm, knob, recall, singleton_to_correct_DEDUCTION, breadth, rho},
  #   'rho_selected': float, 'J_E': {2:..,3:..},
  #   'deduction_required_fraction': {per corpus},
  #   'bite_lost_point_vs_allen': float,
  #   'gate_validation': {matres_deduction_fraction, matres_singleton_to_correct_DEDUCTION},
  #   'applicability_verdict': 'GO-GENERAL'|'GO-MODULE'|'NO-GO/NICHE', 'recall_gate_cleared': bool,
  #   'synthetic': {closure_unit_tests_passed: bool, clean_recall_by_knob, tv_distance_error_types},
  #   'cumulative_openrouter_usd': float, 'n_llm_calls': int, 'cache_hits': int,
  #   'figures': [paths], 'notes': '...'
  # }
  # Validate against a self-defined JSON schema via the aii-json skill; split if oversized.
fallback_plan: >-
  DATA ACCESS FAILURES. (1) NarrativeTime/TimeBankNT not cleanly downloadable in budget -> USE TimeBank-Dense (github.com/muk343/TimeBank-dense;
  mirror via CAEVO github.com/nchambers/caevo or KJETE) as the dense arm, clearly labeled 'NarrativeTime stand-in for pilot';
  the pilot's questions (sound sub-universal emission + triangle collapse) are corpus-quality-agnostic, and the start-point
  convex-point-algebra restriction is applied identically. (2) TimeBank-Dense tlinks file unobtainable -> derive a dense-ish
  edge set from TDDMan (long-distance) + same-doc MATRES adjacent pairs to still get a sentence-distance spread. (3) .tml
  text or event offsets won't parse for some docs -> drop those docs (log count); the pilot only needs ~10-12 short docs per
  corpus. (4) git unavailable -> fetch raw files via aii-web-tools/WebFetch of raw.githubusercontent URLs. If NO real corpus
  is parseable at all, run the SYNTHETIC battery alone and report a synthetic-only frontier with verdict 'NO-GO/NICHE-pending-data'
  (honest, still publishable as a tooling/gate result).\n\nMODEL/BUDGET FAILURES. (a) Primary model unavailable/over-priced
  -> fall through MODEL_FALLBACKS; if all fail, use any sub-$0.50/M-output capable instruct model the aii-openrouter-llms
  skill returns and log the substitution. (b) Cost approaching BUDGET_USD_HARD -> cut MAX_EDGES_PER_CORPUS first (to 60),
  then drop the weakest corpus, then drop S3 (keep the frontier endpoints S1,S2,S4,S5 + middle), never silently truncate --
  log every reduction. (c) Frequent JSON-parse failures -> retry once with a stricter format reminder, then fall back to regex
  extraction of relation tokens; count and report parse-failure rate (a parse-failure is treated as UNDERDETERMINED/universal
  so it lowers bite, not recall artificially).\n\nCLOSURE/ALGEBRA COMPLEXITY. If the endpoint-method Allen composition is
  buggy or slow, fall back to the PRIMARY point-algebra arm only (trivial, complete, fully sufficient for the go/no-go) and
  report the coarse-Allen arm as 'not run' rather than shipping wrong numbers; optionally load the verified Allen composition
  JSON from the qualreas project. Unit tests (Section 7) gate which arms are trusted.\n\nWEAK-SIGNAL OUTCOMES (these are RESULTS,
  not failures -- report them). (i) Recall never clears the gate at any sub-universal knob (recall and bite collide) -> emit
  NO-GO with the measured frontier; this is a genuine scope boundary the umbrella study must respect. (ii) Singleton-resolution
  stays < APPLIC_MODULE even at high recall (real sets near-universal) -> NO-GO/NICHE; recommend iter-2 headline the synthetic
  arm. (iii) MATRES does NOT show N*~0 (deduction-required fraction unexpectedly high) -> flag the gate as non-discriminative
  and re-examine the sentence-distance proxy. (iv) rho ~ 0 (errors look independent) -> still report; it just means the iter-2
  inverted-U peak prediction can use a near-independence model. Each weak outcome is written to method_out.json with its measured
  numbers and an explicit interpretation so iteration-2 can re-plan rather than discover it after spend.
testing_plan: >-
  STAGE 0 -- environment & skill smoke (no spend): load aii-openrouter-llms and confirm the chosen model id + live price (record
  $/M in/out); make ONE 1-token test call to confirm auth and parse the usage/cost field; confirm asyncio concurrency + disk
  cache write/read round-trips (second identical call must be a cache hit, cost unchanged).\n\nSTAGE 1 -- parsing unit tests
  (no spend): parse ONE TimeBank .tml; assert events resolve (eid/eiid -> surface word + sentence index), the two mentions
  get wrapped with [[E1]]/[[E2]] markers, and sentence-distance is computed. Parse 3 TDDMan rows and 3 MATRES rows; assert
  gold labels normalize into the coarse vocab and map to point-algebra sets. Print one fully assembled prompt and eyeball
  it.\n\nSTAGE 2 -- closure correctness (no spend, BLOCKING): run the synthetic battery's closure unit tests. Hand-construct
  >=4 known triangles: (a) point algebra before(A,B) & before(B,C) => path {<} so A-C must be before (singleton-correct);
  (b) before(A,B) & after(B,C) => path = universal (no narrowing, must NOT falsely collapse); (c) an inconsistent triple (e.g.
  before(A,B), before(B,C), after(A,C)) => intersection EMPTY (collapse certificate fires); (d) includes/is_included composition.
  Assert close_triangle returns the exact expected sets for BOTH algebra arms. If any mismatch, FIX before any LLM spend (wrong
  closure invalidates every downstream metric).\n\nSTAGE 3 -- mini end-to-end (tiny spend, < $0.05): 1 doc per corpus, ~5
  edges each, ONLY knobs {S1_single, S4_sound}. Verify the full pipeline produces a frontier_table fragment with sane values:
  recall in [0,1]; breadth grows S1->S4; at least some triangles harvested; collapse_rate and singleton_to_correct computable;
  rho/J(2) numerically defined (or NaN-guarded when n too small). Confirm cumulative cost logged and well under budget. Confirm
  method_out.json passes aii-json validation on this fragment.\n\nCONFIRMATION SIGNALS before full run: breadth must increase
  monotonically across the knob (S1 narrowest, S5 broadest) -- if not, the knob prompts aren't biting and must be re-worded;
  recall must increase (or stay high) as breadth increases -- the basic soundness-recall tradeoff; at least one real triangle
  must produce a non-trivial intersection (else closure has nothing to chew on -- check triangle harvesting and event alignment).
  Only after these hold, scale to MAX_DOCS/MAX_EDGES and all 5 knobs (use aii-long-running-tasks gradual-scaling: 1 -> 3 ->
  all docs), checkpointing the cache so a crash never re-bills. After the full run, re-validate method_out.json with aii-json
  and check file size with aii-file-size-limit; sanity-check the verdict against the frontier plot (the selected operating
  point must actually sit above the recall gate).
</artifact_plan>



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

### [2] HUMAN-USER prompt · 2026-06-17 13:57:19 UTC

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

### [3] SKILL-INPUT — aii-openrouter-llms · 2026-06-17 13:58:55 UTC

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

### [4] SKILL-INPUT — aii-json · 2026-06-17 13:58:55 UTC

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

### [5] SYSTEM-USER prompt · 2026-06-17 14:43:14 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_3`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_3/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_3/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_experiment_3/results/out.json`
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
id: gen_plan_experiment_3_idx6
type: experiment
title: >-
  Recall-Bite Frontier & LLM Elicitation Go/No-Go (T0/Pilot for Closure-Certified Composition)
summary: >-
  A pre-main-run pilot that maps the recall-bite frontier and fixes the pre-registered LLM elicitation operating point. It
  samples temporal-relation edges (with raw text) from three real corpora (dense arm = TimeBank-Dense as a robust stand-in
  for NarrativeTime + start-point convex-point-algebra restriction; non-circular arm = TDDMan long-distance; gate-control
  = MATRES adjacent-sentence) plus a small clean-ground-truth synthetic battery, then sweeps a >=5-setting prompt BREADTH
  KNOB via a cheap OpenRouter model. At each setting it measures per-edge RECALL=P(gold in emitted set), breadth, over-commitment
  vs under-specification rates, raw closure-collapse rate on harvested triangles, strict-tightening AND singleton-resolution-to-correct
  yields, a local-only-reader probe (defines the deduction-required fraction), and the within-document cross-edge reading-error
  correlation rho (with empirical joint soundness J(E)). It plots the frontier, applies a pre-registered go/no-go, and emits
  aii-json-validated method_out.json with the frontier table, the SELECTED operating point, rho, deduction-required fraction,
  J(E), and cumulative OpenRouter spend. API-bound, no GPU, target spend < $2 (hard cap $10).
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  # =====================================================================
  # experiment_iter1_dir6 -- RECALL-BITE FRONTIER & ELICITATION GO/NO-GO
  # Role: T0/pilot viability gate for the closure-certified-composition study.
  # It does NOT run the main comparison; it decides whether the LLM can emit
  # SOUND-but-sub-universal disjunctive relation sets at usable recall with
  # non-trivial singleton-resolution yield, and fixes the operating point + rho
  # that iteration-2 (real-text comparison + synthetic realism match) will reuse.
  # Compute: cpu_heavy (NO GPU). API-bound. Closure runs in ms on CPU.
  # Skills to load: aii-openrouter-llms (LLM calls + pricing), aii-web-tools
  #   (download data files via fetch if git/curl unavailable), aii-parallel-computing
  #   (asyncio concurrency), aii-json (validate output), aii-file-size-limit,
  #   aii-python (logging/structure), aii-long-running-tasks (scale mini->full).
  # Read aii-openrouter-llms FIRST to confirm the current cheapest capable model.
  # =====================================================================

  ##### 0. CONFIG (all pre-registered constants; log them to method_out.json) #####
  SEED = 20260617
  MODEL_PRIMARY   = 'google/gemini-2.5-flash'        # verify via aii-openrouter-llms; pick cheapest CAPABLE
  MODEL_FALLBACKS = ['openai/gpt-5-mini', 'deepseek/deepseek-chat']  # if primary unavailable/too pricey
  TEMPERATURE = 0.0                                   # deterministic single emission (reproducible)
  MAX_EDGES_PER_CORPUS   = 150                         # modest pilot; scale down first (see testing)
  MAX_DOCS_PER_CORPUS    = 12                          # short docs (~3k chars) keep cost low
  MAX_TRIANGLES_PER_DOC  = 60                          # cap closure harvesting per doc
  CONCURRENCY = 12                                     # async OpenRouter calls in flight
  # --- pre-registered GO/NO-GO thresholds (fixed BEFORE any LLM call) ---
  RECALL_GATE_POINT = 0.90       # convex point-algebra (start-point) arm: PC complete -> demand high recall
  RECALL_GATE_ALLEN = 0.85       # coarse-interval (Allen) arm: sound-but-incomplete -> slightly lower bar
  APPLIC_GENERAL = 0.10          # singleton-resolution-to-correct fraction of deduction-required multi-path edges
  APPLIC_MODULE  = 0.05          #   >=0.10 GENERAL mechanism; 0.05-0.10 USEFUL MODULE; <0.05 NICHE/NO-GO
  BUDGET_USD_SOFT = 2.0; BUDGET_USD_HARD = 9.0   # STOP issuing calls if cumulative cost crosses HARD

  # >=5 BREADTH-KNOB settings, narrow -> maximal-sound (this IS the frontier axis):
  KNOB = {
    'S1_single':     'Name THE single temporal relation that holds. Output exactly one.',
    'S2_confident':  'Name the relation(s) you are confident hold; omit any you doubt.',
    'S3_plausible':  'Name every relation that plausibly holds given the text.',
    'S4_sound':      'Name ALL base relations the text does NOT exclude. Recall matters more than precision: it is better to include an extra relation than to omit the correct one. If the text does not constrain the order, output UNDERDETERMINED (the universal set).',
    'S5_maximal':    'List the MAXIMAL sound set: include every base relation not strictly ruled out by the text. Only drop a relation if the text makes it impossible. Use UNDERDETERMINED when nothing is excluded.'
  }

  ##### 1. DATA ACQUISITION (inline; depends_on=[] so this artifact fetches its own slices) #####
  # Use git clone (preferred) or curl/aii-web-tools fetch of raw files. All public, no license wall
  # for the .tml text we need (TempEval-3 TBAQ-cleaned).
  #  (a) TEXT source (.tml with inline <EVENT eid=..>word</EVENT> + <MAKEINSTANCE eventID eiid>):
  #        github.com/jspotter/TempEval-3  -> data/TBAQ-cleaned/TimeBank + AQUAINT (.tml)
  #        github.com/muk343/TimeBank-dense (36 TimeBank .tml, event eids aligned to TimeBank-Dense)
  #  (b) DENSE arm gold (stand-in for NarrativeTime; see fallback):
  #        TimeBank-Dense tlinks: docid \t e1 \t e2 \t {b,a,i,ii,s,v}  (try muk343 / CAEVO / KJETE mirror)
  #        ATTEMPT NarrativeTime/TimeBankNT first (github annargrs / paper links); if not cleanly
  #        downloadable in the time budget, USE TimeBank-Dense and LABEL it 'dense_arm=TimeBank-Dense
  #        (NarrativeTime stand-in for pilot)'. Pilot conclusions (can the LLM emit sound sub-universal
  #        sets? do triangles collapse?) do not depend on NarrativeTime's non-circular gold.
  #  (c) NON-CIRCULAR arm gold: github.com/aakanksha19/TDDiscourse -> TDDMan/TDDMan{Train,Dev,Test}.tsv
  #        format: docid \t e1 \t e2 \t rel  with rel in {b,a,i,ii,s}; ALL pairs >1 sentence apart.
  #  (d) GATE-CONTROL gold: github.com/CogComp/MATRES -> timebank.txt/aquaint.txt/platinum.txt
  #        format: docid verb1 verb2 eiid1 eiid2 rel  with rel in {BEFORE,AFTER,EQUAL,VAGUE}; same/adj-sentence.
  # Parse each .tml: extract plain text, record per-event (eid, eiid via MAKEINSTANCE, surface word,
  #   char offset, sentence index). Sentence-split with a simple splitter (regex on terminal punctuation
  #   or nltk/spacy if available). Build doc_text and event_index[docid][eid] = {word, sent_idx, char_span}.

  RELVOCAB = {  # canonical base-relation labels emitted to / parsed from the LLM, per arm
    'coarse':  ['before','after','includes','is_included','simultaneous'],  # TDDMan/TB-Dense/coarse-Allen
    'point':   ['<','=','>']                                                # start-point convex point algebra
  }
  UNIVERSAL = {'coarse': set(RELVOCAB['coarse']), 'point': {'<','=','>'}}
  # corpus gold-label normalization to coarse base:
  NORMALIZE = {'b':'before','a':'after','i':'includes','ii':'is_included','s':'simultaneous','v':'VAGUE',
               'BEFORE':'before','AFTER':'after','EQUAL':'simultaneous','VAGUE':'VAGUE',
               'INCLUDES':'includes','IS_INCLUDED':'is_included','SIMULTANEOUS':'simultaneous'}
  # VAGUE/v gold == universal target (any sound set is trivially correct) -> mark and EXCLUDE from
  # recall denominator for 'resolvable' metrics, but keep for breadth/coverage stats.

  ##### 2. EDGE & TRIANGLE SAMPLING (deterministic with SEED) #####
  for corpus in [dense_arm, TDDMan, MATRES]:
     docs = pick up to MAX_DOCS_PER_CORPUS docs with text available; prefer shortest (~3k chars)
     gold_edges[corpus] = [(docid,e1,e2,gold_coarse)] restricted to docs we have text for
     sample MAX_EDGES_PER_CORPUS edges (stratify: keep ALL relation classes; for dense_arm and TDDMan
          stratify by sentence-distance bins {same, adjacent, >1 sentence} so deduction-required edges present)
     # triangles for closure: per doc build graph of gold edges; enumerate triples (A,B,C) with all 3
     #   pairs gold-present; sample up to MAX_TRIANGLES_PER_DOC; ensure every triangle's 3 edges are in
     #   the elicitation set (add them if needed). Record each triangle's max pairwise sentence-distance
     #   (>1 => deduction-required triangle) and a structural hop label (length-2 path A-B-C resolving A-C).

  ##### 3. RELATION ALGEBRA & MINIMAL CLOSURE (pure-Python, no deps, runs in ms) #####
  # --- POINT ALGEBRA on event START-points (NarrativeTime/dense convex arm; PC COMPLETE) ---
  # base composition table comp_pt[r1][r2] (set result):
  #   '<'o'<'={<}; '<'o'='={<}; '<'o'>'=ALL; '='o r = {r}; '>'o'>'={>}; '>'o'='={>}; '>'o'<'=ALL
  # disjunctive composition = UNION over base pairs; intersection = set intersection (empty => contradiction).
  # map coarse gold/emitted -> start-point set:
  #   before->{<}; after->{>}; simultaneous->{=}; includes->{<,=}(<=); is_included->{=,>}(>=); VAGUE->{<,=,>}
  # --- COARSE INTERVAL (Allen) ARM (sound-but-INCOMPLETE; lower-bound detector) ---
  # map coarse -> Allen base: before->{b}; after->{bi}; includes->{di}; is_included->{d}; simultaneous->{eq};
  #   VAGUE->all 13. Implement Allen 13x13 composition by ENDPOINT method (robust, no 169-entry hardcode):
  #   represent interval X by points (Xs<Xe); each Allen base relation == a point-algebra config on
  #   (As,Ae,Bs,Be); compose two relations by point-algebra closure over shared endpoints; read back the
  #   set of consistent Allen base relations. (Alternative: hardcode the published Allen table or load the
  #   JSON table from the qualreas project github.com/alreich/qualreas -- but ship a self-contained version.)
  # Provide BOTH arms; POINT-ALGEBRA arm is PRIMARY for the dense corpus (completeness); coarse-Allen arm
  #   is reported as the lower-bound detector and used for TDDMan (coarse set, no VAGUE).

  def close_triangle(setAB, setBC, setAC, algebra):
     # path A-B-C constrains A-C: path = compose(setAB, setBC, algebra)
     path = compose(setAB, setBC, algebra)
     inter = path & setAC               # cross-path narrowing (Mode A) intersected w/ directly-read A-C
     return {'path':path, 'inter':inter, 'empty': len(inter)==0, 'singleton': len(inter)==1}

  ##### 4. LLM ELICITATION (OpenRouter, cached, concurrent, budget-guarded) #####
  # Build a deterministic disk CACHE keyed by sha256(model|arm|knob|prompt) -> parsed response JSON,
  #   so re-runs and identical (edge,knob) prompts never re-bill. Persist to ./cache/.
  # For each (corpus-arm, knob, edge): construct prompt =
  #   SYSTEM: 'You read temporal relations between two marked events in a news text. Allowed base
  #            relations: <ARM VOCAB>. <KNOB instruction>. Judge ONLY from the text; do NOT assume
  #            consistency with other pairs. Reply as JSON: {\"relations\":[...],\"underdetermined\":bool}.'
  #   USER: doc_text with the two target event mentions wrapped [[E1]]word[[/E1]] / [[E2]]word[[/E2]]
  #         + 'Relation of E1 to E2?'  (window to <= ~1500 tokens around the events if doc long)
  # CALL via aii-openrouter-llms with TEMPERATURE=0, json mode if available; parse robustly
  #   (map synonyms; UNDERDETERMINED/empty -> UNIVERSAL set; drop labels outside vocab and log).
  # Run with asyncio + semaphore(CONCURRENCY). After EACH call: cost += usage*price; if cost>BUDGET_USD_HARD: STOP.
  # emitted[arm][knob][edge] = parsed base-relation SET (already in arm vocab).
  #
  # LOCAL-ONLY READER PROBE (defines deduction-required fraction): for each held-out edge, build a probe
  #   prompt containing ONLY the minimal local span(s) where E1 and E2 co-occur (same/adjacent sentence);
  #   if no shared local span -> mark structurally DEDUCTION-REQUIRED, skip the call. Else elicit at the
  #   SELECTED-knob style and record local_correct = (gold in local emitted set & singleton-correct).
  #   deduction_required[edge] = (no shared span) OR (local probe fails to name gold singleton).

  ##### 5. METRICS per (arm, knob) -- the FRONTIER TABLE #####
  for arm, knob:
     recall            = mean over non-VAGUE edges of 1[gold in emitted_set]        # PRIMARY frontier axis
     breadth_mean/med  = distribution of |emitted_set|
     universal_rate    = frac(emitted_set == UNIVERSAL)                              # under-specification
     overcommit_rate   = frac(sound AND |set|<|universal| AND singleton-but-wrong-or-too-narrow-excluding-gold)
                         # decompose: under-spec (too broad/universal) vs over-commit (excludes gold)
     unsound_rate      = 1 - recall                                                 # gold excluded
     # closure on harvested triangles (use emitted sets at THIS knob; both algebra arms):
     collapse_rate     = frac(triangles with close_triangle.empty)                  # Mode-B detection signal
     strict_tighten    = frac(triangles where inter strictly subset setAC)          # any narrowing (reported, NOT load-bearing)
     singleton_to_correct = frac(triangles where inter is singleton AND == gold(A-C))# HEADLINE yield (load-bearing)
     singleton_to_correct_DEDUCTION = same restricted to deduction-required triangles# the applicability number's numerator
     # bite-lost (point arm vs coarse-Allen arm on SAME triangles):
     bite_lost = singleton_to_correct[Allen] - singleton_to_correct[point]          # info lost by convex restriction

  # rho (within-doc cross-edge reading-error correlation) at each knob:
  #   err_e = 1 - 1[gold in emitted_set]; compute INTRACLASS correlation of err grouped by docid
  #   (ICC, or: P(both edges in same doc err)/[P(err)^2] - 1 as a correlation-style ratio). rho>0 => positively
  #   correlated reading errors (single reader). Report rho per knob; the SELECTED knob's rho feeds iter-2.
  # J(E) empirical joint soundness: J(2)=frac(triangles where BOTH path edges AB,BC sound);
  #   where >=3-edge constraint paths exist, also J(3). Report J(2),J(3) and contrast vs independence r^E.

  # deduction_required_fraction[corpus] = mean(deduction_required[edge]) over evaluable edges  # for applicability

  ##### 6. FRONTIER PLOT + PRE-REGISTERED GO/NO-GO #####
  # Plot (matplotlib, save PNG/JPEG): x=recall, y=singleton_to_correct_DEDUCTION, size/color=collapse_rate,
  #   one marker per (arm,knob); overlay RECALL_GATE line. Also breadth-vs-recall and collapse-vs-knob plots.
  # SELECT operating point: among knobs whose recall >= RECALL_GATE (POINT arm: 0.90; coarse/TDDMan: 0.85),
  #   choose the one MAXIMIZING singleton_to_correct_DEDUCTION (tie -> higher recall). Record full row.
  # VERDICT:
  #   GO-GENERAL   if some arm has a recall-gated knob with singleton_to_correct_DEDUCTION >= APPLIC_GENERAL (0.10)
  #   GO-MODULE    if best is in [APPLIC_MODULE, APPLIC_GENERAL)  (0.05-0.10) -> proceed, scope as 'useful module'
  #   NO-GO/NICHE  if < APPLIC_MODULE on every arm OR no knob clears the recall gate -> recommend iter-2 demote
  #                real text to niche-safety-net and headline the SYNTHETIC arm (report honestly).
  # Report the EXPECTED gate-validation result: MATRES deduction_required_fraction ~ 0 and its
  #   singleton_to_correct_DEDUCTION ~ 0 (near-empty by construction) vs dense_arm/TDDMan >> 0.

  ##### 7. SYNTHETIC CLEAN-GROUND-TRUTH BATTERY (closure-code correctness + recall reference) #####
  # Generate ~30-60 small consistent QCNs: random total order of timepoints (point algebra) and a few
  #   interval scenarios (Allen); derive gold base relation per pair from the ground-truth order.
  # Realize each edge as a templated English sentence with surface variation ('X happened before Y',
  #   'during', 'while', 'after', 'at the same time as'); assemble a tiny doc per network.
  # Run the SAME elicitation+closure. Use this to (a) UNIT-TEST closure (known answers must match),
  #   (b) get a clean-text recall reference, (c) first rough TV-distance of error-type distribution
  #   real-vs-synthetic (full realism match is iter-2's job; report as exploratory).

  ##### 8. OUTPUT method_out.json (validate with aii-json; check size with aii-file-size-limit) #####
  # {
  #   'config': {seed, model_used, model_price, temperature, thresholds, n_edges/n_triangles per corpus, budget},
  #   'data_provenance': {dense_arm_source (NarrativeTime|TimeBank-Dense-standin), tddman_src, matres_src, text_src},
  #   'frontier_table': [ per (corpus,arm,knob): recall, breadth_mean/med, universal_rate, overcommit_rate,
  #                       unsound_rate, collapse_rate, strict_tighten, singleton_to_correct,
  #                       singleton_to_correct_DEDUCTION, rho, J2, J3 ],
  #   'selected_operating_point': {corpus, arm, knob, recall, singleton_to_correct_DEDUCTION, breadth, rho},
  #   'rho_selected': float, 'J_E': {2:..,3:..},
  #   'deduction_required_fraction': {per corpus},
  #   'bite_lost_point_vs_allen': float,
  #   'gate_validation': {matres_deduction_fraction, matres_singleton_to_correct_DEDUCTION},
  #   'applicability_verdict': 'GO-GENERAL'|'GO-MODULE'|'NO-GO/NICHE', 'recall_gate_cleared': bool,
  #   'synthetic': {closure_unit_tests_passed: bool, clean_recall_by_knob, tv_distance_error_types},
  #   'cumulative_openrouter_usd': float, 'n_llm_calls': int, 'cache_hits': int,
  #   'figures': [paths], 'notes': '...'
  # }
  # Validate against a self-defined JSON schema via the aii-json skill; split if oversized.
fallback_plan: >-
  DATA ACCESS FAILURES. (1) NarrativeTime/TimeBankNT not cleanly downloadable in budget -> USE TimeBank-Dense (github.com/muk343/TimeBank-dense;
  mirror via CAEVO github.com/nchambers/caevo or KJETE) as the dense arm, clearly labeled 'NarrativeTime stand-in for pilot';
  the pilot's questions (sound sub-universal emission + triangle collapse) are corpus-quality-agnostic, and the start-point
  convex-point-algebra restriction is applied identically. (2) TimeBank-Dense tlinks file unobtainable -> derive a dense-ish
  edge set from TDDMan (long-distance) + same-doc MATRES adjacent pairs to still get a sentence-distance spread. (3) .tml
  text or event offsets won't parse for some docs -> drop those docs (log count); the pilot only needs ~10-12 short docs per
  corpus. (4) git unavailable -> fetch raw files via aii-web-tools/WebFetch of raw.githubusercontent URLs. If NO real corpus
  is parseable at all, run the SYNTHETIC battery alone and report a synthetic-only frontier with verdict 'NO-GO/NICHE-pending-data'
  (honest, still publishable as a tooling/gate result).\n\nMODEL/BUDGET FAILURES. (a) Primary model unavailable/over-priced
  -> fall through MODEL_FALLBACKS; if all fail, use any sub-$0.50/M-output capable instruct model the aii-openrouter-llms
  skill returns and log the substitution. (b) Cost approaching BUDGET_USD_HARD -> cut MAX_EDGES_PER_CORPUS first (to 60),
  then drop the weakest corpus, then drop S3 (keep the frontier endpoints S1,S2,S4,S5 + middle), never silently truncate --
  log every reduction. (c) Frequent JSON-parse failures -> retry once with a stricter format reminder, then fall back to regex
  extraction of relation tokens; count and report parse-failure rate (a parse-failure is treated as UNDERDETERMINED/universal
  so it lowers bite, not recall artificially).\n\nCLOSURE/ALGEBRA COMPLEXITY. If the endpoint-method Allen composition is
  buggy or slow, fall back to the PRIMARY point-algebra arm only (trivial, complete, fully sufficient for the go/no-go) and
  report the coarse-Allen arm as 'not run' rather than shipping wrong numbers; optionally load the verified Allen composition
  JSON from the qualreas project. Unit tests (Section 7) gate which arms are trusted.\n\nWEAK-SIGNAL OUTCOMES (these are RESULTS,
  not failures -- report them). (i) Recall never clears the gate at any sub-universal knob (recall and bite collide) -> emit
  NO-GO with the measured frontier; this is a genuine scope boundary the umbrella study must respect. (ii) Singleton-resolution
  stays < APPLIC_MODULE even at high recall (real sets near-universal) -> NO-GO/NICHE; recommend iter-2 headline the synthetic
  arm. (iii) MATRES does NOT show N*~0 (deduction-required fraction unexpectedly high) -> flag the gate as non-discriminative
  and re-examine the sentence-distance proxy. (iv) rho ~ 0 (errors look independent) -> still report; it just means the iter-2
  inverted-U peak prediction can use a near-independence model. Each weak outcome is written to method_out.json with its measured
  numbers and an explicit interpretation so iteration-2 can re-plan rather than discover it after spend.
testing_plan: >-
  STAGE 0 -- environment & skill smoke (no spend): load aii-openrouter-llms and confirm the chosen model id + live price (record
  $/M in/out); make ONE 1-token test call to confirm auth and parse the usage/cost field; confirm asyncio concurrency + disk
  cache write/read round-trips (second identical call must be a cache hit, cost unchanged).\n\nSTAGE 1 -- parsing unit tests
  (no spend): parse ONE TimeBank .tml; assert events resolve (eid/eiid -> surface word + sentence index), the two mentions
  get wrapped with [[E1]]/[[E2]] markers, and sentence-distance is computed. Parse 3 TDDMan rows and 3 MATRES rows; assert
  gold labels normalize into the coarse vocab and map to point-algebra sets. Print one fully assembled prompt and eyeball
  it.\n\nSTAGE 2 -- closure correctness (no spend, BLOCKING): run the synthetic battery's closure unit tests. Hand-construct
  >=4 known triangles: (a) point algebra before(A,B) & before(B,C) => path {<} so A-C must be before (singleton-correct);
  (b) before(A,B) & after(B,C) => path = universal (no narrowing, must NOT falsely collapse); (c) an inconsistent triple (e.g.
  before(A,B), before(B,C), after(A,C)) => intersection EMPTY (collapse certificate fires); (d) includes/is_included composition.
  Assert close_triangle returns the exact expected sets for BOTH algebra arms. If any mismatch, FIX before any LLM spend (wrong
  closure invalidates every downstream metric).\n\nSTAGE 3 -- mini end-to-end (tiny spend, < $0.05): 1 doc per corpus, ~5
  edges each, ONLY knobs {S1_single, S4_sound}. Verify the full pipeline produces a frontier_table fragment with sane values:
  recall in [0,1]; breadth grows S1->S4; at least some triangles harvested; collapse_rate and singleton_to_correct computable;
  rho/J(2) numerically defined (or NaN-guarded when n too small). Confirm cumulative cost logged and well under budget. Confirm
  method_out.json passes aii-json validation on this fragment.\n\nCONFIRMATION SIGNALS before full run: breadth must increase
  monotonically across the knob (S1 narrowest, S5 broadest) -- if not, the knob prompts aren't biting and must be re-worded;
  recall must increase (or stay high) as breadth increases -- the basic soundness-recall tradeoff; at least one real triangle
  must produce a non-trivial intersection (else closure has nothing to chew on -- check triangle harvesting and event alignment).
  Only after these hold, scale to MAX_DOCS/MAX_EDGES and all 5 knobs (use aii-long-running-tasks gradual-scaling: 1 -> 3 ->
  all docs), checkpointing the cache so a crash never re-bills. After the full run, re-validate method_out.json with aii-json
  and check file size with aii-file-size-limit; sanity-check the verdict against the frontier plot (the selected operating
  point must actually sit above the recall gate).
</artifact_plan>



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

### [6] SKILL-INPUT — aii-file-size-limit · 2026-06-17 14:43:30 UTC

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

### [7] SYSTEM-USER prompt · 2026-06-17 14:44:32 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `title`: 'Recall-Bite Frontier & LLM Elicitation Go/No-Go Pilot for Closure-Certified Temporal Composition' is too long (at most 90 characters, got 96)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [8] SYSTEM-USER prompt · 2026-06-17 14:44:48 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 1/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json
  - Missing file: mini_method_out.json
  - Missing file: preview_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```
