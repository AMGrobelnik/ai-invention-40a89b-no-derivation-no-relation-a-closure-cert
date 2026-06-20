# gen_art_experiment_3 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_3` (terminal_claude_agent)

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/results/out.json`
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
id: gen_plan_experiment_3_idx5
type: experiment
title: >-
  LOCAL-Reader Real-Text Head-to-Head + End-to-End Prolog Slice (H1 narrowing, H2 hallucination-reduction) on ACTUAL NarrativeTime
  (+TDDMan), two readers, matched-coverage baselines
summary: >-
  THE HEADLINE EXPERIMENT (experiment_iter2_dir5). Tests whether ITERATED path-consistency closure over SPAN-LOCAL LLM reads
  recovers deduction-required temporal relations the local reads alone cannot, beating {local raw LLM, Path-of-Thoughts, self-consistency
  voting, naive single-pass} at MATCHED COVERAGE (H1) and cutting the confident-wrong (hallucination) rate vs a raw LLM on
  deduction-required/absent-relation pairs (H2), with a Prolog-discharged trace-graph and a quantified hallucination number.
  Operates on the FROZEN ACTUAL NarrativeTime gold graphs (dense co-primary, un-conflated from the iter-1 TimeBank-Dense stand-in)
  corroborated on TDDMan (non-circular long-distance). Reuses the iter-1 closure engine + cached/cost-guarded OpenRouter client
  VERBATIM; the genuinely NEW code is (a) a dataset adapter reading full_data_out.json with char-offset event marking, (b)
  span-LOCAL reads of the constituent path edges, (c) matched-coverage risk-coverage comparison with Holm-Bonferroni-adjusted
  doc-clustered bootstrap CIs, (d) the end-to-end SWI-Prolog discharge + hallucination number, and (e) a $0 fully-powered
  synthetic matched-coverage baseline comparison (recall 0.96) that carries the mechanism claim if real text is thin/underpowered.
  Runs >=2 readers INCLUDING one substantially stronger model and reports per-edge recall vs the 0.85/0.90 gate (directly
  testing the read-soundness-bottleneck headline). Every number TAGGED REAL-LLM-READ / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE
  / THEOREM; honest DISCONFIRM/SCOPE-BOUNDARY fallback to negative-localization + synthetic-mechanism (NeSy/findings) if neither
  gateway clears. Hard $9 cost guard, well under $10.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # ===================================================================================
  # experiment_iter2_dir5 : LOCAL-reader real-text H1/H2 head-to-head + end-to-end Prolog
  # Runtime: Python 3.12 (uv). NO GPU. LLM via OpenRouter only. Hard cap $9 (well < $10).
  # Closure/bootstrap are laptop-fast CPU; the only cost is LLM reads (cached on disk).
  # ===================================================================================
  #
  # ---- 0. WORKSPACE BOOTSTRAP (reuse iter-1 code VERBATIM) -----------------------------
  # Create the experiment workspace. COPY these files in (do not re-derive them):
  #   FROM gen_art_experiment_3/ (frontier pilot, art_glhgFsBUrcYo):
  #     llm.py      -> OpenRouterClient(cache, hard/soft budget guard, async batch,
  #                    parse_relations). USE VERBATIM. Disk cache => reruns recompute at $0.
  #     engine.py   -> Algebra, build_point_algebra(), build_allen_algebra(), QCN,
  #                    pc2_full(qcn)->(consistent,n_fired), naive_single_pass(qcn,u,v),
  #                    close_triangle(alg,ab,bc,ac), convex widen. USE VERBATIM.
  #     corpora.py  -> mark_text(), local_span()(*lives in method.py*), harvest_triangles(),
  #                    COARSE_VOCAB_*, COARSE_TO_POINT/ALLEN, coarse_to_set, emitted_set,
  #                    gold_atom, directed. REUSE the mapping+marking helpers; REPLACE the
  #                    .tml corpus LOADERS with a dataset adapter (below).
  #     tests.py    -> closure_tests_pass(): BLOCKING closure unit battery (Allen cells,
  #                    convex-point completeness, collapse detection, naive==full on len-2).
  #     synth.py + (gen_art_experiment_2/method.py) -> synthetic QCN generators
  #                    gen_family_R / gen_family_H + read_network() simulated channel
  #                    (recall/breadth/rho knobs) for the $0 baseline comparison.
  #   FROM gen_art_experiment_3/method.py reuse: build_prompt(), KNOB/KNOB_ORDER,
  #     parse_all(), arm_knob_metrics(), closure_metrics(), clustered_bootstrap_ci(),
  #     icc_oneway(), local_span(), run_local_probe().
  # Set env: OPENROUTER_API_KEY already present. uv pip install numpy scipy pandas networkx
  #   httpx loguru matplotlib jsonschema. (Add pyswip ONLY if swipl binary present.)
  #
  # ---- 1. PRE-REGISTERED CONFIG (FIX before any LLM call; write to method_out.metadata) -
  SEED = 20260617
  KNOB_OP = 'S4_sound'        # operating point: high-recall SOUND disjunction (iter-1 pilot)
  RECALL_GATE = {'POINT':0.90,'ALLEN':0.85}   # PC complete on point / lower bound on Allen
  APPLIC = {'general':0.10,'module':0.05}     # singleton-to-correct on deduction-required
  H2_MIN_EFFECT = 0.05        # PRE-REGISTERED: confident-wrong rate must drop >= 5 pts ABS,
                              #                 with doc-clustered paired-bootstrap CI lo > 0
  N_TARGET_DEDUCTION = 300    # >=10x iter-1 n=7 (aim hundreds on NarrativeTime; TDDMan top-up)
  SC_K = 5                    # self-consistency samples (query edge only)
  BOOT_B = 2000; ALPHA = 0.05
  CONFIRM_FAMILY = ['H1_vs_PoT','H1_vs_SC','H2_halluc']  # Holm-Bonferroni adjusted (gateways)
  # Readers: primary (cheap) + one SUBSTANTIALLY STRONGER. Resolve current IDs via the
  # aii-openrouter-llms skill at runtime (iter-1 found gemini-2.5-flash-lite GONE ->
  # used google/gemini-3.1-flash-lite). Selection rule:
  #   READER_PRIMARY  = cheapest reliable-JSON flash-lite-class model that is AVAILABLE
  #                     (try 'google/gemini-3.1-flash-lite','google/gemini-2.5-flash-lite',
  #                      then 'deepseek/deepseek-v3.2').
  #   READER_STRONG   = a CLEARLY more capable model, cheapest such available
  #                     (try 'google/gemini-3-pro','google/gemini-3.1-flash',
  #                      'openai/gpt-5.1','anthropic/claude-sonnet-4.5'); verify via skill,
  #                     pick cheapest that is unambiguously stronger than READER_PRIMARY.
  # One shared OpenRouterClient PER reader (separate cache namespace via model in sha key).
  #
  # ---- 2. DATASET ADAPTER (NEW; un-conflation FIX 5) ----------------------------------
  # data_adapter.py: read the FROZEN dataset artifact (art_PNrS9T8JeATf):
  DATASET = '/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json'
  # top-level {metadata, datasets}; iterate datasets -> examples; each example:
  #   text  = example['input']                       # stripped document text (string)
  #   G     = json.loads(example['output'])           # gold_graph {nodes, edges}
  #   corpus= example['metadata_corpus'] in {narrativetime, tddman, matres}
  # Build per-corpus 'arm' dicts in the SAME shape corpora.py emits so reused metric code
  # works unchanged: arm = {arm, algebra, edge_tasks:{(docid,u,v):task}, triangles:[...]}.
  def build_arm(corpus, examples):
      algebra = 'POINT' if corpus=='matres' else 'ALLEN'   # NT uses Allen + a POINT start-pt arm
      docs = {}
      for ex in examples:
          text=ex['input']; G=json.loads(ex['output']); docid=ex['metadata_doc_id']
          node={n['node_id']:n for n in G['nodes'] if n['node_type']=='event'}  # event-event only
          edges=[]
          for e in G['edges']:
              if e['source'] not in node or e['target'] not in node: continue
              # gold relation sets: use dataset-computed canonical_relation_set (Allen) and
              # startpoint_relation_set (convex point). native_relation -> coarse for prompts.
              edges.append({'u':e['source'],'v':e['target'],
                            'gold_allen':frozenset(e['canonical_relation_set']),
                            'gold_point':frozenset(e['startpoint_relation_set']),
                            'native':e['native_relation'],'sentdiff':e['sentence_distance'],
                            'deduction_required':bool(e['structural_deduction_required_proxy'])})
          # marked_text per edge: VERIFY char offsets align (dataset blocking-gate guarantees
          # NT reproduces TLINKs exactly). Mark with node char_start/char_end via mark_text();
          # if text[cs:ce]!=surface, fall back to ordered surface search (corpora.py pattern).
          docs[docid]={'text':text,'node':node,'edges':edges}
      # edge_tasks + triangles: reuse corpora._assemble_arm-style logic but DRIVEN BY
      # deduction-required QUERY edges (not budget-blind). See step 3.
      return docs, algebra
  #
  # ---- 3. SAMPLE DEDUCTION-REQUIRED MULTI-PATH QUERIES + HARVEST CONSTRAINING EDGES ----
  # For NarrativeTime (primary) then TDDMan (corroboration):
  #   Build undirected gold adjacency per doc. A QUERY edge q=(qx,qy) is admissible if:
  #     (i) deduction_required (sentdiff>=2) AND gold is a recall-scorable singleton/atom,
  #     (ii) >=1 length-2 path qx-via-qy through other gold edges  (multi-path if >=2 vias
  #          OR a >=3-edge/cyclic path exists -> tag stratum 'len2' vs 'ge3/cyclic').
  #   Stratify + sample up to N_TARGET_DEDUCTION queries round-robin across docs (seeded).
  #   The EDGES TO READ = union over admissible queries of {all constituent path edges} +
  #     the query edge itself. This is the BILLED set; dedupe so each (doc,u,v) read ONCE.
  #   Record per-query: query, list of vias, constituent edges per path, min-path-length,
  #     cyclomatic of the local query subgraph (|E|-|V|+1), gold relation, locality stratum
  #     (deduction-required vs directly-readable via locally_justifiable_proxy).
  #
  # ---- 4. SPAN-LOCAL ELICITATION (the load-bearing regime; FIX 1) ----------------------
  # For EACH unique edge to read, build the LOCAL read item:
  #   marked = mark_text(doc.text, span(u), span(v))      # [[E1]]..[[E2]] inserted by offset
  #   local  = local_span(marked)                          # ONLY sentence(s) containing E1/E2
  #   if '[[E1]]' not in local or '[[E2]]' not in local:   # NO SHARED SPAN
  #        record as structurally-deduction-required; emit UNIVERSAL (no LLM call) for that edge
  #   else: system,user = build_prompt({...,'marked_text':local,'algebra':alg}, KNOB_OP)
  # AUGMENT build_prompt to also request a calibrated confidence (for matched coverage):
  #   '... ALSO return "confidence": <0..1> for your most likely single relation.'
  #   (parse_relations ignores extra keys; add a tiny parse_confidence() fallback=0.5.)
  # Run client.run_batch(items) for READER_PRIMARY (all corpora) and READER_STRONG
  #   (NarrativeTime deduction queries ONLY, to bound cost). All cached on disk.
  # parse_all() -> emitted[(arm,reader)][(doc,u,v)] = {coarse, underdet, algset, conf}.
  #
  # ---- 5. PER-EDGE RECALL + STRONGER-READER GATE TEST (FIX 5) --------------------------
  # For each (arm,reader): recall = P(gold_atom in emitted_set) via arm_knob_metrics() with
  #   doc-clustered CI. Report recall vs RECALL_GATE[algebra]. KEY result either way:
  #   does READER_STRONG cross 0.85/0.90?  crossed => read-soundness was a weak-model artifact
  #   (confirms bottleneck headline); not crossed => bottleneck is real-text read soundness.
  #   Also report within-doc soundness rho (icc_oneway over per-doc sound 0/1) per reader.
  #
  # ---- 6. CLOSURE PIPELINE + BASELINES (per query, per reader) -------------------------
  # closure_pipeline.py: for each admissible query q on doc d:
  #   alg = ALG[algebra]; nodes = endpoints + all vias on q's constraining paths
  #   qcn = QCN(alg, nodes)
  #   for each constituent gold edge e on q's paths: qcn.set_edge(idx(e.u),idx(e.v), emitted[e])
  #   HELD-OUT query edge (qx,qy) left at UNIVERSE (NOT seeded with its own read for closure).
  #   # --- METHOD: Mode-A FULL iterated closure ---
  #   ok,_ = pc2_full(qcn); res_full = alg.empty if not ok else qcn.get(idx(qx),idx(qy))
  #       # collapse(empty) => Mode-B detection => ABSTAIN (record as Mode-B flag)
  #   modeA_pred = singleton(res_full) ? the relation : ABSTAIN ; conf = min contributing-edge conf
  #   # --- BASELINE naive single-pass (iteration contrast; PREDICTED TIE on len2) ---
  #   res_naive = naive_single_pass(qcn, idx(qx), idx(qy)); naive_pred similarly.
  #   # --- BASELINE local raw LLM (forced single) = the DIRECT local read of (qx,qy) ---
  #   raw_pred = argmax-likelihood single relation from the query edge's OWN local read
  #       (forced to a singleton even if underdetermined); conf = reader confidence.
  #   # --- BASELINE Path-of-Thoughts (per-path INDEPENDENT reasoning, path-agreement abstain) -
  #   For each path qx->via->qy: ONE LLM call giving the two LOCAL edge reads as facts and
  #       asking the single composed relation INDEPENDENTLY (no cross-path intersection).
  #       PoT_pred = modal relation across paths; abstain if paths DISAGREE (path-agreement
  #       fraction is the abstention signal). (This is the gap Mode A fills: it INTERSECTS.)
  #   # --- BASELINE self-consistency voting (query edge) ---
  #   SC: SC_K sampled single-relation reads of the query's local span (temperature>0 OR
  #       k prompt-paraphrases at temp 0 if provider is deterministic); SC_pred = majority;
  #       abstention signal = vote margin (top/k).
  # Cache every LLM call; PoT + SC run on READER_PRIMARY (bound cost); Mode-A/naive/raw use
  #   the already-read LOCAL sets for BOTH readers.
  #
  # ---- 7. H1: MATCHED-COVERAGE SELECTIVE ACCURACY (gateway, Holm-adjusted) -------------
  # matched_coverage.py: for each method produce per-query (pred|ABSTAIN, confidence).
  #   Build risk-coverage curve: sweep threshold tau over confidence; coverage(tau)=frac
  #   predicted; selective_acc(tau)=correct among predicted. Interpolate every method to a
  #   SHARED coverage grid (0.05..0.95). 'coverage object' = single-relation resolution,
  #   applied IDENTICALLY to all methods.
  #   H1 metric = Mode-A selective_acc MINUS {PoT, SC} at MATCHED coverage (report the gap
  #     at Mode-A's natural coverage AND the area between curves). DOC-CLUSTERED paired
  #     bootstrap (resample documents, B=BOOT_B) -> gap CI; Holm-Bonferroni adjust across
  #     CONFIRM_FAMILY. H1 CONFIRM if Mode-A > PoT AND > SC, adjusted CI lo > 0.
  #   STRATIFY (exploratory, nominal CI): len2 stratum (Mode-A PREDICTED TO TIE naive ->
  #     report tie as confirmation) vs ge3/cyclic stratum (full>naive corroborates H3 on real
  #     text). Also report deduction-required vs directly-readable strata.
  #
  # ---- 8. H2: END-TO-END HALLUCINATION REDUCTION (gateway) -----------------------------
  # hallucination.py: on the deduction-required / absent-relation subset:
  #   confident_wrong(method) = frac of NON-ABSTAINED predictions whose singleton != gold.
  #   compare closure-pipeline (Mode-A; abstains on disjunction/collapse) vs raw LLM (forced
  #   single). reduction = cw(raw) - cw(closure). DOC-CLUSTERED paired bootstrap CI.
  #   H2 CONFIRM if reduction >= H2_MIN_EFFECT (0.05) AND adjusted CI lo > 0. Decompose
  #   closure confident-wrong into SILENT-WRONG-NARROWING (unsound contributing edge) per the
  #   pre-registered failure mode; report rate vs per-edge recall (<= 1-recall bound) (FIX 4).
  #
  # ---- 9. END-TO-END PROLOG DISCHARGE + WORKED EXAMPLE (FIX 2) -------------------------
  # prolog_discharge.py: pick ONE NarrativeTime 3-event triangle where Mode-A narrows to a
  #   correct singleton (Mode-A path) and ONE where closure COLLAPSES (Mode-B path).
  #   Emit the closed QCN as a Prolog/ASP program: facts rel(e1,e2,[before,...]) for read
  #   edges + composition/converse clauses from the EXACT algebra table; query the held-out
  #   pair. DISCHARGE:
  #     if shutil.which('swipl'): run `swipl -q -g "goal,halt" prog.pl` via subprocess and
  #        capture the derived relation;  (try `apt-get install -y swi-prolog` once; non-fatal)
  #     else: emit prog.pl AS A RUNNABLE ARTIFACT + verify entailment in-process with a tiny
  #        self-contained resolution over the closed table (clearly TAGGED 'python-checked,
  #        swipl-unavailable'). H2 number does NOT depend on the Prolog engine.
  #   Build a human-auditable TRACE-GRAPH (QCN nodes/edges, which compositions FIRED on which
  #   paths, the resolved/collapsed query) and the compact notation/metric table.
  #
  # ---- 10. SYNTHETIC $0 MATCHED-COVERAGE BASELINE COMPARISON (FIX 3 backstop) ----------
  # synthetic_baselines.py (reuse gen_art_experiment_2 channel, recall~0.96, NO LLM, $0,
  #   fully powered N=600/cell): run Mode-A FULL closure, naive single-pass, raw-forced-single,
  #   self-consistency (resample channel k=5), PoT-analog (per-path compose without cross-path
  #   intersection) at MATCHED COVERAGE; confirm Mode-A > {PoT-analog, SC, raw} where reads are
  #   sound. This carries the matched-coverage baseline claim if real text is thin/underpowered.
  #
  # ---- 11. VERDICT + OUTPUT ------------------------------------------------------------
  # verdict:
  #   if H1 (vs PoT AND SC) CONFIRM and H2 CONFIRM (adjusted) -> 'CONFIRM' (LOCAL-reader value
  #       + end-to-end deliverable established on real text).
  #   elif exactly one gateway clears -> 'PARTIAL/SCOPE-BOUNDARY' (report which).
  #   else -> 'DISCONFIRM/SCOPE-BOUNDARY': contribution = NEGATIVE-LOCALIZATION + SYNTHETIC
  #       MECHANISM (synthetic matched-coverage win + stronger-reader recall map), honestly
  #       retargeted to NeSy/findings (per the hypothesis fallback). Real text = niche safety-net.
  #   Always report: per-reader recall vs gate + gate-crossing answer; applicability N* and
  #       singleton-to-correct vs APPLIC thresholds; len2-tie; ge3/cyclic real-iteration stratum.
  # TAG every number THEOREM / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / REAL-LLM-READ.
  # Emit method_out.json validated against exp_gen_sol_out via aii-json (mini/preview variants;
  #   split if > size limit via aii-file-size-limit). Structure: metadata.headline_findings,
  #   per-reader recall, H1 leaderboard w/ adjusted CIs, H2 number+CI+pre-reg comparison,
  #   worked_example (trace-graph + prolog text + discharge), synthetic comparison, verdict,
  #   examples[] one per query edge with predict_modeA/predict_naive/predict_raw/predict_pot/
  #   predict_sc + gold + strata. Print client.stats() (cumulative_usd, calls, cache hits).
  #
  # ---- 12. EXECUTION ORDER (gradual scaling; aii-long-running-tasks) -------------------
  # (a) closure_tests_pass() MUST pass (gates all LLM spend).
  # (b) synthetic_baselines ($0) -> sanity that matched-coverage harness + mechanism work.
  # (c) --mini real smoke: 2-3 docs, ~10 queries, both readers (~$0.02) -> full pipeline +
  #     schema + one Prolog discharge.
  # (d) full real run under hard cost guard; monitor client.cost; stop tail on BudgetExceeded.
fallback_plan: |-
  PROLOG ENGINE UNAVAILABLE (most likely infra risk): swipl may not be installable without sudo. Try `apt-get install -y swi-prolog` (non-fatal); if absent, STILL emit a runnable prog.pl artifact and discharge the held-out query with a self-contained in-process resolution over the closed composition table, TAGGED 'python-verified, swipl-unavailable'. H1/H2 numbers are independent of the Prolog engine (closure is computed in engine.py), so the headline survives; only the literal SWI-Prolog replay is downgraded to an emitted-but-not-shell-run artifact.

  NARRATIVETIME OFFSET MISALIGNMENT: the dataset artifact's blocking gate guarantees NT reproduces shipped TLINKs and nodes carry char_start/char_end, so marking should work directly. If text[char_start:char_end] != node surface for some events, fall back to corpora.py's ordered surface-search marking; if a doc still fails, drop it and log coverage_gaps (do not silently proceed).

  TOO FEW MULTI-PATH DEDUCTION TRIANGLES ON NARRATIVETIME (underpowered H1): NT is dense (1.58M event-event triangles) so this is unlikely, but if admissible multi-path deduction queries < ~100 after sampling, (1) widen the constraining-path search to >=3-edge paths, (2) PROMOTE TDDMan (all-long-distance, non-circular) to the primary real arm, (3) if both real arms are thin, fall back to the $0 fully-powered SYNTHETIC matched-coverage comparison as the matched-coverage evidence and DEMOTE real text to the honestly-scoped niche-safety-net boundary (the pre-registered TINY-ENVELOPE failure mode), decided from the GOLD-ONLY counts BEFORE heavy LLM spend.

  BUDGET PRESSURE (approaching $9 hard cap): the cost guard in llm.py aborts new calls automatically and returns cached/partial results. Mitigations in priority order: (1) restrict READER_STRONG to NarrativeTime deduction queries only (already planned); (2) drop SC_K from 5 to 3; (3) shrink N_TARGET_DEDUCTION (keep >=10x the iter-1 n=7, i.e. >=70); (4) run PoT on a query subsample. Primary-reader H1/H2 take priority over the stronger-reader arm. NEVER exceed $9; report actual spend.

  NEITHER GATEWAY CLEARS (H1 and H2 both fail): this is an ANTICIPATED, publishable outcome, NOT an execution failure. Emit verdict 'DISCONFIRM/SCOPE-BOUNDARY' with the contribution reframed as (i) NEGATIVE LOCALIZATION (local reads pin gold ~27%, stronger reader still below the 0.85/0.90 gate => the bottleneck is real-text read soundness, not closure) + (ii) the SYNTHETIC MECHANISM win at matched coverage, honestly retargeted to NeSy / a findings/short track. Report the full recall-bite picture so the scope boundary is legible.

  STRONGER READER ID DRIFT / UNAVAILABLE: iter-1 already hit this (gemini-2.5-flash-lite gone). Resolve current IDs via the aii-openrouter-llms skill at runtime; the OpenRouterClient has a fallback list and retries. If no clearly-stronger model is affordable, use the next-best available (e.g. gemini-3.1-flash or deepseek-v3.2) and label the 'stronger reader' honestly by its actual capability tier.

  PoT/SELF-CONSISTENCY REIMPLEMENTATION RISK: no public PoT repo (dossier-confirmed); reimplement per arXiv:2412.17963 (graph extraction -> path identification -> per-path INDEPENDENT reasoning, path-agreement abstain). If PoT's path-extraction is unreliable on these short docs, fall back to giving PoT the SAME harvested gold paths as Mode-A but reasoning each path independently WITHOUT cross-path intersection (this is the fair, paper-faithful contrast and isolates exactly the intersection step Mode A adds).
testing_plan: |-
  STAGE 0 - BLOCKING ENGINE TESTS ($0, seconds, gates ALL LLM spend): run the copied tests.py closure_tests_pass(). Must verify: Allen composition cells vs GQR, convex-point PC completeness vs brute force, COLLAPSE detection on an injected gold-excluding edge, and the iteration-isolation invariant naive_single_pass == pc2_full on length-2 multi-path queries but pc2_full strictly narrows on >=3-edge chains. Abort the whole run if any fails.

  STAGE 1 - SYNTHETIC MATCHED-COVERAGE SANITY ($0, fully powered): run synthetic_baselines.py (reused gen_art_experiment_2 channel at recall~0.96, N=600/cell). CONFIRMATION SIGNAL: Mode-A FULL closure beats {PoT-analog, self-consistency, raw-forced-single} in selective accuracy at matched coverage with non-overlapping bootstrap CIs, and ties naive single-pass on length-2 while exceeding it on >=3-edge/cyclic. This proves the matched-coverage harness + risk-coverage interpolation + Holm-adjustment code are correct and the mechanism works WHEN READS ARE SOUND, before spending any LLM budget.

  STAGE 2 - DATASET ADAPTER + MARKING UNIT CHECK ($0): load full_data_out.json; assert 36 NarrativeTime + 34 TDDMan + 275 MATRES docs; for a 5-doc sample assert text[char_start:char_end]==node.surface for >=95% of events (dataset blocking-gate should make this ~100%); assert mark_text inserts both [[E1]] and [[E2]] and local_span recovers the co-occurrence sentence(s); print the admissible-deduction-query count per corpus and the len2 vs ge3/cyclic stratum sizes (this is the GOLD-ONLY applicability N* -- decide hosting BEFORE heavy spend).

  STAGE 3 - MINI REAL SMOKE (~$0.01-0.05, both readers): method.py --mini on 2-3 NarrativeTime docs and ~10 deduction queries. CONFIRMATION SIGNALS: 0 parse failures (parse_relations robust); each query produces predict_modeA / predict_naive / predict_raw / predict_pot / predict_sc + confidence; the matched-coverage curve is monotone-ish and well-defined; ONE worked example emits a valid trace-graph + prog.pl that discharges (swipl or python-checked); method_out.json validates against exp_gen_sol_out (aii-json). Inspect one marked LOCAL read by eye to confirm it really shows only the local span (not the whole doc) -- this is the load-bearing regime check.

  STAGE 4 - FULL RUN WITH LIVE COST MONITORING: launch under the hard cost guard; tail the log for client.cost and cache-hit ratio (PID-based: `uv run method.py & PID=$!`; `tail -f logs/run.log & TPID=$!`). Re-runs are $0 (disk cache) so iterate analysis freely. SUCCESS CHECK before declaring done: per-reader recall reported vs gate (with the explicit stronger-reader gate-crossing answer); H1 adjusted-CI gaps vs PoT and SC; H2 reduction vs the pre-registered 0.05 with CI; >=N_TARGET_DEDUCTION (or the budget-reduced floor, >=70) deduction queries scored with doc-clustered CIs; worked example + Prolog present; verdict emitted with every number TAGGED by evidence class; total spend < $9 printed. If any headline number rests on < ~70 queries, label it underpowered and lean on the synthetic + stronger-reader-recall evidence in the verdict.
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
id: art_PNrS9T8JeATf
type: dataset
title: 'Fold-split gold temporal relation graphs: NarrativeTime, TDDMan, MATRES'
summary: |-
  Frozen, reusable real-text gold temporal relation graphs that all downstream real-text closure experiments (the T0 envelope go/no-go pilot now; later arms) consume. Schema exp_sel_data_out, grouped by dataset, ONE example per (corpus, document) row (345 examples): input = the stripped document text (string), output = json.dumps(gold_graph) (string; parse with json.loads). The gold_graph has nodes [{node_id, node_type in {event,timex,dct}, surface, char_start, char_end, global_token_index, sentence_index, eiid/tid/eid, event_class, plus nt_event_type/nt_time/nt_branch/nt_start/nt_end for NarrativeTime}] and edges [{source, target, native_relation, canonical_algebra, canonical_relation_set, coarse_superset_set?, startpoint_relation_set, vague_widened, src/tgt_sentence_index, sentence_distance, locality_class in {intra,adjacent,long_distance}, structural_deduction_required_proxy (dist>=2), locally_justifiable_proxy (dist<=1), edge_fold, phenomena?}], plus per_doc_descriptive_counts. Each example also carries metadata_corpus/doc_id/fold/n_nodes/n_edges/n_events/long_distance_edges/descriptive_counts.

  Three corpora by role: (1) NarrativeTime (36 docs, 1,715 events, 103,748 edges, dense full TLink coverage, 1.58M event-event triangles) is the DENSE headline host; relations are produced by the corpus authors' OWN code (narrative_time.event_relations + conversion_utils), reproducing the shipped nt_converted_to_tml TLINKs EXACTLY (blocking gate: 207,496 relation-multisets + node counts match across all 36 docs) — non-circular gold; canonical_algebra=interval_allen with start-point point relations, non-convex {<,>} widened to {<,=,>} (vague_widened, 124 edges). (2) TDDMan (34 docs, 6,137 manually-annotated event-event pairs, 99.9% long-distance >=2 sentences apart) is the non-circularity anchor; codes {b,a,s,i,ii} mapped to tightest Allen + coarse superset + convex point sets; 107 test pairs carry TDDiscourse phenomena tags. (3) MATRES (275 docs, 6,099 events, 13,577 edges, 0% long-distance: 30% intra / 70% adjacent) is the gate-validation control with a near-empty deduction envelope; point algebra (BEFORE/AFTER/EQUAL/VAGUE -> {<}/{>}/{=}/{<,=,>}, no non-convex relations).

  Folds: document-level TimeBank-Dense 22/5/9 train/dev/test for NarrativeTime/TDDMan; MATRES train(TimeBank+AQUAINT)/test(Platinum); TDDMan edges also carry native edge_fold. One frozen NLTK Punkt sentence segmentation is reused across NarrativeTime/TDDMan; MATRES uses the canonical qiangning per-token sentence ids with SENTDIFF as authoritative distance. A doc-id overlap table (overlap_table.json) shows 33 documents shared by all three corpora. Aggregate + per-document DESCRIPTIVE structural counts (sizes, native/canonical label distributions, locality distribution, triangles, >=2-intermediate query edges, cyclomatic number, >=3-hop pairs) are in descriptive_counts.json. The gated statistics (deduction-required N*, bite-after-widening, singleton-resolution) are intentionally NOT computed here — they need composition closure / held-out-edge resolution and are the T0 experiment's job. Caveats: 1 TDDMan eid absent from the muk343 .tml version (APW19980213.1310/e257, 13 pairs dropped, reported in metadata.coverage_gaps); 238/6,099 MATRES events (3.9%) lack a char offset (boundary edge cases) but retain sentence_index + global_token_index; every non-null MATRES offset is surface-exact by construction; NarrativeTime gold uses annotator a1. Sources cited in README.md and metadata.sources (CogComp MATRES, qiangning EMNLP19 XML, TDDiscourse, text-machine-lab narrative_time, muk343 TimeBank-Dense, TempEval-3 TBAQ-cleaned). Reproduce via data.py / build_dataset.py with pinned pyproject.toml. An optional 4th TimeBank-Dense corpus builder is available (builders.build_timebank_dense) but not emitted.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

### [3] SKILL-INPUT — aii-json · 2026-06-17 15:43:01 UTC

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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-17 15:43:01 UTC

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

### [5] SKILL-INPUT — aii-openrouter-llms · 2026-06-17 15:51:51 UTC

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

### [6] SYSTEM-USER prompt · 2026-06-17 16:25:46 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/results/out.json`
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
id: gen_plan_experiment_3_idx5
type: experiment
title: >-
  LOCAL-Reader Real-Text Head-to-Head + End-to-End Prolog Slice (H1 narrowing, H2 hallucination-reduction) on ACTUAL NarrativeTime
  (+TDDMan), two readers, matched-coverage baselines
summary: >-
  THE HEADLINE EXPERIMENT (experiment_iter2_dir5). Tests whether ITERATED path-consistency closure over SPAN-LOCAL LLM reads
  recovers deduction-required temporal relations the local reads alone cannot, beating {local raw LLM, Path-of-Thoughts, self-consistency
  voting, naive single-pass} at MATCHED COVERAGE (H1) and cutting the confident-wrong (hallucination) rate vs a raw LLM on
  deduction-required/absent-relation pairs (H2), with a Prolog-discharged trace-graph and a quantified hallucination number.
  Operates on the FROZEN ACTUAL NarrativeTime gold graphs (dense co-primary, un-conflated from the iter-1 TimeBank-Dense stand-in)
  corroborated on TDDMan (non-circular long-distance). Reuses the iter-1 closure engine + cached/cost-guarded OpenRouter client
  VERBATIM; the genuinely NEW code is (a) a dataset adapter reading full_data_out.json with char-offset event marking, (b)
  span-LOCAL reads of the constituent path edges, (c) matched-coverage risk-coverage comparison with Holm-Bonferroni-adjusted
  doc-clustered bootstrap CIs, (d) the end-to-end SWI-Prolog discharge + hallucination number, and (e) a $0 fully-powered
  synthetic matched-coverage baseline comparison (recall 0.96) that carries the mechanism claim if real text is thin/underpowered.
  Runs >=2 readers INCLUDING one substantially stronger model and reports per-edge recall vs the 0.85/0.90 gate (directly
  testing the read-soundness-bottleneck headline). Every number TAGGED REAL-LLM-READ / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE
  / THEOREM; honest DISCONFIRM/SCOPE-BOUNDARY fallback to negative-localization + synthetic-mechanism (NeSy/findings) if neither
  gateway clears. Hard $9 cost guard, well under $10.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # ===================================================================================
  # experiment_iter2_dir5 : LOCAL-reader real-text H1/H2 head-to-head + end-to-end Prolog
  # Runtime: Python 3.12 (uv). NO GPU. LLM via OpenRouter only. Hard cap $9 (well < $10).
  # Closure/bootstrap are laptop-fast CPU; the only cost is LLM reads (cached on disk).
  # ===================================================================================
  #
  # ---- 0. WORKSPACE BOOTSTRAP (reuse iter-1 code VERBATIM) -----------------------------
  # Create the experiment workspace. COPY these files in (do not re-derive them):
  #   FROM gen_art_experiment_3/ (frontier pilot, art_glhgFsBUrcYo):
  #     llm.py      -> OpenRouterClient(cache, hard/soft budget guard, async batch,
  #                    parse_relations). USE VERBATIM. Disk cache => reruns recompute at $0.
  #     engine.py   -> Algebra, build_point_algebra(), build_allen_algebra(), QCN,
  #                    pc2_full(qcn)->(consistent,n_fired), naive_single_pass(qcn,u,v),
  #                    close_triangle(alg,ab,bc,ac), convex widen. USE VERBATIM.
  #     corpora.py  -> mark_text(), local_span()(*lives in method.py*), harvest_triangles(),
  #                    COARSE_VOCAB_*, COARSE_TO_POINT/ALLEN, coarse_to_set, emitted_set,
  #                    gold_atom, directed. REUSE the mapping+marking helpers; REPLACE the
  #                    .tml corpus LOADERS with a dataset adapter (below).
  #     tests.py    -> closure_tests_pass(): BLOCKING closure unit battery (Allen cells,
  #                    convex-point completeness, collapse detection, naive==full on len-2).
  #     synth.py + (gen_art_experiment_2/method.py) -> synthetic QCN generators
  #                    gen_family_R / gen_family_H + read_network() simulated channel
  #                    (recall/breadth/rho knobs) for the $0 baseline comparison.
  #   FROM gen_art_experiment_3/method.py reuse: build_prompt(), KNOB/KNOB_ORDER,
  #     parse_all(), arm_knob_metrics(), closure_metrics(), clustered_bootstrap_ci(),
  #     icc_oneway(), local_span(), run_local_probe().
  # Set env: OPENROUTER_API_KEY already present. uv pip install numpy scipy pandas networkx
  #   httpx loguru matplotlib jsonschema. (Add pyswip ONLY if swipl binary present.)
  #
  # ---- 1. PRE-REGISTERED CONFIG (FIX before any LLM call; write to method_out.metadata) -
  SEED = 20260617
  KNOB_OP = 'S4_sound'        # operating point: high-recall SOUND disjunction (iter-1 pilot)
  RECALL_GATE = {'POINT':0.90,'ALLEN':0.85}   # PC complete on point / lower bound on Allen
  APPLIC = {'general':0.10,'module':0.05}     # singleton-to-correct on deduction-required
  H2_MIN_EFFECT = 0.05        # PRE-REGISTERED: confident-wrong rate must drop >= 5 pts ABS,
                              #                 with doc-clustered paired-bootstrap CI lo > 0
  N_TARGET_DEDUCTION = 300    # >=10x iter-1 n=7 (aim hundreds on NarrativeTime; TDDMan top-up)
  SC_K = 5                    # self-consistency samples (query edge only)
  BOOT_B = 2000; ALPHA = 0.05
  CONFIRM_FAMILY = ['H1_vs_PoT','H1_vs_SC','H2_halluc']  # Holm-Bonferroni adjusted (gateways)
  # Readers: primary (cheap) + one SUBSTANTIALLY STRONGER. Resolve current IDs via the
  # aii-openrouter-llms skill at runtime (iter-1 found gemini-2.5-flash-lite GONE ->
  # used google/gemini-3.1-flash-lite). Selection rule:
  #   READER_PRIMARY  = cheapest reliable-JSON flash-lite-class model that is AVAILABLE
  #                     (try 'google/gemini-3.1-flash-lite','google/gemini-2.5-flash-lite',
  #                      then 'deepseek/deepseek-v3.2').
  #   READER_STRONG   = a CLEARLY more capable model, cheapest such available
  #                     (try 'google/gemini-3-pro','google/gemini-3.1-flash',
  #                      'openai/gpt-5.1','anthropic/claude-sonnet-4.5'); verify via skill,
  #                     pick cheapest that is unambiguously stronger than READER_PRIMARY.
  # One shared OpenRouterClient PER reader (separate cache namespace via model in sha key).
  #
  # ---- 2. DATASET ADAPTER (NEW; un-conflation FIX 5) ----------------------------------
  # data_adapter.py: read the FROZEN dataset artifact (art_PNrS9T8JeATf):
  DATASET = '/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json'
  # top-level {metadata, datasets}; iterate datasets -> examples; each example:
  #   text  = example['input']                       # stripped document text (string)
  #   G     = json.loads(example['output'])           # gold_graph {nodes, edges}
  #   corpus= example['metadata_corpus'] in {narrativetime, tddman, matres}
  # Build per-corpus 'arm' dicts in the SAME shape corpora.py emits so reused metric code
  # works unchanged: arm = {arm, algebra, edge_tasks:{(docid,u,v):task}, triangles:[...]}.
  def build_arm(corpus, examples):
      algebra = 'POINT' if corpus=='matres' else 'ALLEN'   # NT uses Allen + a POINT start-pt arm
      docs = {}
      for ex in examples:
          text=ex['input']; G=json.loads(ex['output']); docid=ex['metadata_doc_id']
          node={n['node_id']:n for n in G['nodes'] if n['node_type']=='event'}  # event-event only
          edges=[]
          for e in G['edges']:
              if e['source'] not in node or e['target'] not in node: continue
              # gold relation sets: use dataset-computed canonical_relation_set (Allen) and
              # startpoint_relation_set (convex point). native_relation -> coarse for prompts.
              edges.append({'u':e['source'],'v':e['target'],
                            'gold_allen':frozenset(e['canonical_relation_set']),
                            'gold_point':frozenset(e['startpoint_relation_set']),
                            'native':e['native_relation'],'sentdiff':e['sentence_distance'],
                            'deduction_required':bool(e['structural_deduction_required_proxy'])})
          # marked_text per edge: VERIFY char offsets align (dataset blocking-gate guarantees
          # NT reproduces TLINKs exactly). Mark with node char_start/char_end via mark_text();
          # if text[cs:ce]!=surface, fall back to ordered surface search (corpora.py pattern).
          docs[docid]={'text':text,'node':node,'edges':edges}
      # edge_tasks + triangles: reuse corpora._assemble_arm-style logic but DRIVEN BY
      # deduction-required QUERY edges (not budget-blind). See step 3.
      return docs, algebra
  #
  # ---- 3. SAMPLE DEDUCTION-REQUIRED MULTI-PATH QUERIES + HARVEST CONSTRAINING EDGES ----
  # For NarrativeTime (primary) then TDDMan (corroboration):
  #   Build undirected gold adjacency per doc. A QUERY edge q=(qx,qy) is admissible if:
  #     (i) deduction_required (sentdiff>=2) AND gold is a recall-scorable singleton/atom,
  #     (ii) >=1 length-2 path qx-via-qy through other gold edges  (multi-path if >=2 vias
  #          OR a >=3-edge/cyclic path exists -> tag stratum 'len2' vs 'ge3/cyclic').
  #   Stratify + sample up to N_TARGET_DEDUCTION queries round-robin across docs (seeded).
  #   The EDGES TO READ = union over admissible queries of {all constituent path edges} +
  #     the query edge itself. This is the BILLED set; dedupe so each (doc,u,v) read ONCE.
  #   Record per-query: query, list of vias, constituent edges per path, min-path-length,
  #     cyclomatic of the local query subgraph (|E|-|V|+1), gold relation, locality stratum
  #     (deduction-required vs directly-readable via locally_justifiable_proxy).
  #
  # ---- 4. SPAN-LOCAL ELICITATION (the load-bearing regime; FIX 1) ----------------------
  # For EACH unique edge to read, build the LOCAL read item:
  #   marked = mark_text(doc.text, span(u), span(v))      # [[E1]]..[[E2]] inserted by offset
  #   local  = local_span(marked)                          # ONLY sentence(s) containing E1/E2
  #   if '[[E1]]' not in local or '[[E2]]' not in local:   # NO SHARED SPAN
  #        record as structurally-deduction-required; emit UNIVERSAL (no LLM call) for that edge
  #   else: system,user = build_prompt({...,'marked_text':local,'algebra':alg}, KNOB_OP)
  # AUGMENT build_prompt to also request a calibrated confidence (for matched coverage):
  #   '... ALSO return "confidence": <0..1> for your most likely single relation.'
  #   (parse_relations ignores extra keys; add a tiny parse_confidence() fallback=0.5.)
  # Run client.run_batch(items) for READER_PRIMARY (all corpora) and READER_STRONG
  #   (NarrativeTime deduction queries ONLY, to bound cost). All cached on disk.
  # parse_all() -> emitted[(arm,reader)][(doc,u,v)] = {coarse, underdet, algset, conf}.
  #
  # ---- 5. PER-EDGE RECALL + STRONGER-READER GATE TEST (FIX 5) --------------------------
  # For each (arm,reader): recall = P(gold_atom in emitted_set) via arm_knob_metrics() with
  #   doc-clustered CI. Report recall vs RECALL_GATE[algebra]. KEY result either way:
  #   does READER_STRONG cross 0.85/0.90?  crossed => read-soundness was a weak-model artifact
  #   (confirms bottleneck headline); not crossed => bottleneck is real-text read soundness.
  #   Also report within-doc soundness rho (icc_oneway over per-doc sound 0/1) per reader.
  #
  # ---- 6. CLOSURE PIPELINE + BASELINES (per query, per reader) -------------------------
  # closure_pipeline.py: for each admissible query q on doc d:
  #   alg = ALG[algebra]; nodes = endpoints + all vias on q's constraining paths
  #   qcn = QCN(alg, nodes)
  #   for each constituent gold edge e on q's paths: qcn.set_edge(idx(e.u),idx(e.v), emitted[e])
  #   HELD-OUT query edge (qx,qy) left at UNIVERSE (NOT seeded with its own read for closure).
  #   # --- METHOD: Mode-A FULL iterated closure ---
  #   ok,_ = pc2_full(qcn); res_full = alg.empty if not ok else qcn.get(idx(qx),idx(qy))
  #       # collapse(empty) => Mode-B detection => ABSTAIN (record as Mode-B flag)
  #   modeA_pred = singleton(res_full) ? the relation : ABSTAIN ; conf = min contributing-edge conf
  #   # --- BASELINE naive single-pass (iteration contrast; PREDICTED TIE on len2) ---
  #   res_naive = naive_single_pass(qcn, idx(qx), idx(qy)); naive_pred similarly.
  #   # --- BASELINE local raw LLM (forced single) = the DIRECT local read of (qx,qy) ---
  #   raw_pred = argmax-likelihood single relation from the query edge's OWN local read
  #       (forced to a singleton even if underdetermined); conf = reader confidence.
  #   # --- BASELINE Path-of-Thoughts (per-path INDEPENDENT reasoning, path-agreement abstain) -
  #   For each path qx->via->qy: ONE LLM call giving the two LOCAL edge reads as facts and
  #       asking the single composed relation INDEPENDENTLY (no cross-path intersection).
  #       PoT_pred = modal relation across paths; abstain if paths DISAGREE (path-agreement
  #       fraction is the abstention signal). (This is the gap Mode A fills: it INTERSECTS.)
  #   # --- BASELINE self-consistency voting (query edge) ---
  #   SC: SC_K sampled single-relation reads of the query's local span (temperature>0 OR
  #       k prompt-paraphrases at temp 0 if provider is deterministic); SC_pred = majority;
  #       abstention signal = vote margin (top/k).
  # Cache every LLM call; PoT + SC run on READER_PRIMARY (bound cost); Mode-A/naive/raw use
  #   the already-read LOCAL sets for BOTH readers.
  #
  # ---- 7. H1: MATCHED-COVERAGE SELECTIVE ACCURACY (gateway, Holm-adjusted) -------------
  # matched_coverage.py: for each method produce per-query (pred|ABSTAIN, confidence).
  #   Build risk-coverage curve: sweep threshold tau over confidence; coverage(tau)=frac
  #   predicted; selective_acc(tau)=correct among predicted. Interpolate every method to a
  #   SHARED coverage grid (0.05..0.95). 'coverage object' = single-relation resolution,
  #   applied IDENTICALLY to all methods.
  #   H1 metric = Mode-A selective_acc MINUS {PoT, SC} at MATCHED coverage (report the gap
  #     at Mode-A's natural coverage AND the area between curves). DOC-CLUSTERED paired
  #     bootstrap (resample documents, B=BOOT_B) -> gap CI; Holm-Bonferroni adjust across
  #     CONFIRM_FAMILY. H1 CONFIRM if Mode-A > PoT AND > SC, adjusted CI lo > 0.
  #   STRATIFY (exploratory, nominal CI): len2 stratum (Mode-A PREDICTED TO TIE naive ->
  #     report tie as confirmation) vs ge3/cyclic stratum (full>naive corroborates H3 on real
  #     text). Also report deduction-required vs directly-readable strata.
  #
  # ---- 8. H2: END-TO-END HALLUCINATION REDUCTION (gateway) -----------------------------
  # hallucination.py: on the deduction-required / absent-relation subset:
  #   confident_wrong(method) = frac of NON-ABSTAINED predictions whose singleton != gold.
  #   compare closure-pipeline (Mode-A; abstains on disjunction/collapse) vs raw LLM (forced
  #   single). reduction = cw(raw) - cw(closure). DOC-CLUSTERED paired bootstrap CI.
  #   H2 CONFIRM if reduction >= H2_MIN_EFFECT (0.05) AND adjusted CI lo > 0. Decompose
  #   closure confident-wrong into SILENT-WRONG-NARROWING (unsound contributing edge) per the
  #   pre-registered failure mode; report rate vs per-edge recall (<= 1-recall bound) (FIX 4).
  #
  # ---- 9. END-TO-END PROLOG DISCHARGE + WORKED EXAMPLE (FIX 2) -------------------------
  # prolog_discharge.py: pick ONE NarrativeTime 3-event triangle where Mode-A narrows to a
  #   correct singleton (Mode-A path) and ONE where closure COLLAPSES (Mode-B path).
  #   Emit the closed QCN as a Prolog/ASP program: facts rel(e1,e2,[before,...]) for read
  #   edges + composition/converse clauses from the EXACT algebra table; query the held-out
  #   pair. DISCHARGE:
  #     if shutil.which('swipl'): run `swipl -q -g "goal,halt" prog.pl` via subprocess and
  #        capture the derived relation;  (try `apt-get install -y swi-prolog` once; non-fatal)
  #     else: emit prog.pl AS A RUNNABLE ARTIFACT + verify entailment in-process with a tiny
  #        self-contained resolution over the closed table (clearly TAGGED 'python-checked,
  #        swipl-unavailable'). H2 number does NOT depend on the Prolog engine.
  #   Build a human-auditable TRACE-GRAPH (QCN nodes/edges, which compositions FIRED on which
  #   paths, the resolved/collapsed query) and the compact notation/metric table.
  #
  # ---- 10. SYNTHETIC $0 MATCHED-COVERAGE BASELINE COMPARISON (FIX 3 backstop) ----------
  # synthetic_baselines.py (reuse gen_art_experiment_2 channel, recall~0.96, NO LLM, $0,
  #   fully powered N=600/cell): run Mode-A FULL closure, naive single-pass, raw-forced-single,
  #   self-consistency (resample channel k=5), PoT-analog (per-path compose without cross-path
  #   intersection) at MATCHED COVERAGE; confirm Mode-A > {PoT-analog, SC, raw} where reads are
  #   sound. This carries the matched-coverage baseline claim if real text is thin/underpowered.
  #
  # ---- 11. VERDICT + OUTPUT ------------------------------------------------------------
  # verdict:
  #   if H1 (vs PoT AND SC) CONFIRM and H2 CONFIRM (adjusted) -> 'CONFIRM' (LOCAL-reader value
  #       + end-to-end deliverable established on real text).
  #   elif exactly one gateway clears -> 'PARTIAL/SCOPE-BOUNDARY' (report which).
  #   else -> 'DISCONFIRM/SCOPE-BOUNDARY': contribution = NEGATIVE-LOCALIZATION + SYNTHETIC
  #       MECHANISM (synthetic matched-coverage win + stronger-reader recall map), honestly
  #       retargeted to NeSy/findings (per the hypothesis fallback). Real text = niche safety-net.
  #   Always report: per-reader recall vs gate + gate-crossing answer; applicability N* and
  #       singleton-to-correct vs APPLIC thresholds; len2-tie; ge3/cyclic real-iteration stratum.
  # TAG every number THEOREM / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / REAL-LLM-READ.
  # Emit method_out.json validated against exp_gen_sol_out via aii-json (mini/preview variants;
  #   split if > size limit via aii-file-size-limit). Structure: metadata.headline_findings,
  #   per-reader recall, H1 leaderboard w/ adjusted CIs, H2 number+CI+pre-reg comparison,
  #   worked_example (trace-graph + prolog text + discharge), synthetic comparison, verdict,
  #   examples[] one per query edge with predict_modeA/predict_naive/predict_raw/predict_pot/
  #   predict_sc + gold + strata. Print client.stats() (cumulative_usd, calls, cache hits).
  #
  # ---- 12. EXECUTION ORDER (gradual scaling; aii-long-running-tasks) -------------------
  # (a) closure_tests_pass() MUST pass (gates all LLM spend).
  # (b) synthetic_baselines ($0) -> sanity that matched-coverage harness + mechanism work.
  # (c) --mini real smoke: 2-3 docs, ~10 queries, both readers (~$0.02) -> full pipeline +
  #     schema + one Prolog discharge.
  # (d) full real run under hard cost guard; monitor client.cost; stop tail on BudgetExceeded.
fallback_plan: |-
  PROLOG ENGINE UNAVAILABLE (most likely infra risk): swipl may not be installable without sudo. Try `apt-get install -y swi-prolog` (non-fatal); if absent, STILL emit a runnable prog.pl artifact and discharge the held-out query with a self-contained in-process resolution over the closed composition table, TAGGED 'python-verified, swipl-unavailable'. H1/H2 numbers are independent of the Prolog engine (closure is computed in engine.py), so the headline survives; only the literal SWI-Prolog replay is downgraded to an emitted-but-not-shell-run artifact.

  NARRATIVETIME OFFSET MISALIGNMENT: the dataset artifact's blocking gate guarantees NT reproduces shipped TLINKs and nodes carry char_start/char_end, so marking should work directly. If text[char_start:char_end] != node surface for some events, fall back to corpora.py's ordered surface-search marking; if a doc still fails, drop it and log coverage_gaps (do not silently proceed).

  TOO FEW MULTI-PATH DEDUCTION TRIANGLES ON NARRATIVETIME (underpowered H1): NT is dense (1.58M event-event triangles) so this is unlikely, but if admissible multi-path deduction queries < ~100 after sampling, (1) widen the constraining-path search to >=3-edge paths, (2) PROMOTE TDDMan (all-long-distance, non-circular) to the primary real arm, (3) if both real arms are thin, fall back to the $0 fully-powered SYNTHETIC matched-coverage comparison as the matched-coverage evidence and DEMOTE real text to the honestly-scoped niche-safety-net boundary (the pre-registered TINY-ENVELOPE failure mode), decided from the GOLD-ONLY counts BEFORE heavy LLM spend.

  BUDGET PRESSURE (approaching $9 hard cap): the cost guard in llm.py aborts new calls automatically and returns cached/partial results. Mitigations in priority order: (1) restrict READER_STRONG to NarrativeTime deduction queries only (already planned); (2) drop SC_K from 5 to 3; (3) shrink N_TARGET_DEDUCTION (keep >=10x the iter-1 n=7, i.e. >=70); (4) run PoT on a query subsample. Primary-reader H1/H2 take priority over the stronger-reader arm. NEVER exceed $9; report actual spend.

  NEITHER GATEWAY CLEARS (H1 and H2 both fail): this is an ANTICIPATED, publishable outcome, NOT an execution failure. Emit verdict 'DISCONFIRM/SCOPE-BOUNDARY' with the contribution reframed as (i) NEGATIVE LOCALIZATION (local reads pin gold ~27%, stronger reader still below the 0.85/0.90 gate => the bottleneck is real-text read soundness, not closure) + (ii) the SYNTHETIC MECHANISM win at matched coverage, honestly retargeted to NeSy / a findings/short track. Report the full recall-bite picture so the scope boundary is legible.

  STRONGER READER ID DRIFT / UNAVAILABLE: iter-1 already hit this (gemini-2.5-flash-lite gone). Resolve current IDs via the aii-openrouter-llms skill at runtime; the OpenRouterClient has a fallback list and retries. If no clearly-stronger model is affordable, use the next-best available (e.g. gemini-3.1-flash or deepseek-v3.2) and label the 'stronger reader' honestly by its actual capability tier.

  PoT/SELF-CONSISTENCY REIMPLEMENTATION RISK: no public PoT repo (dossier-confirmed); reimplement per arXiv:2412.17963 (graph extraction -> path identification -> per-path INDEPENDENT reasoning, path-agreement abstain). If PoT's path-extraction is unreliable on these short docs, fall back to giving PoT the SAME harvested gold paths as Mode-A but reasoning each path independently WITHOUT cross-path intersection (this is the fair, paper-faithful contrast and isolates exactly the intersection step Mode A adds).
testing_plan: |-
  STAGE 0 - BLOCKING ENGINE TESTS ($0, seconds, gates ALL LLM spend): run the copied tests.py closure_tests_pass(). Must verify: Allen composition cells vs GQR, convex-point PC completeness vs brute force, COLLAPSE detection on an injected gold-excluding edge, and the iteration-isolation invariant naive_single_pass == pc2_full on length-2 multi-path queries but pc2_full strictly narrows on >=3-edge chains. Abort the whole run if any fails.

  STAGE 1 - SYNTHETIC MATCHED-COVERAGE SANITY ($0, fully powered): run synthetic_baselines.py (reused gen_art_experiment_2 channel at recall~0.96, N=600/cell). CONFIRMATION SIGNAL: Mode-A FULL closure beats {PoT-analog, self-consistency, raw-forced-single} in selective accuracy at matched coverage with non-overlapping bootstrap CIs, and ties naive single-pass on length-2 while exceeding it on >=3-edge/cyclic. This proves the matched-coverage harness + risk-coverage interpolation + Holm-adjustment code are correct and the mechanism works WHEN READS ARE SOUND, before spending any LLM budget.

  STAGE 2 - DATASET ADAPTER + MARKING UNIT CHECK ($0): load full_data_out.json; assert 36 NarrativeTime + 34 TDDMan + 275 MATRES docs; for a 5-doc sample assert text[char_start:char_end]==node.surface for >=95% of events (dataset blocking-gate should make this ~100%); assert mark_text inserts both [[E1]] and [[E2]] and local_span recovers the co-occurrence sentence(s); print the admissible-deduction-query count per corpus and the len2 vs ge3/cyclic stratum sizes (this is the GOLD-ONLY applicability N* -- decide hosting BEFORE heavy spend).

  STAGE 3 - MINI REAL SMOKE (~$0.01-0.05, both readers): method.py --mini on 2-3 NarrativeTime docs and ~10 deduction queries. CONFIRMATION SIGNALS: 0 parse failures (parse_relations robust); each query produces predict_modeA / predict_naive / predict_raw / predict_pot / predict_sc + confidence; the matched-coverage curve is monotone-ish and well-defined; ONE worked example emits a valid trace-graph + prog.pl that discharges (swipl or python-checked); method_out.json validates against exp_gen_sol_out (aii-json). Inspect one marked LOCAL read by eye to confirm it really shows only the local span (not the whole doc) -- this is the load-bearing regime check.

  STAGE 4 - FULL RUN WITH LIVE COST MONITORING: launch under the hard cost guard; tail the log for client.cost and cache-hit ratio (PID-based: `uv run method.py & PID=$!`; `tail -f logs/run.log & TPID=$!`). Re-runs are $0 (disk cache) so iterate analysis freely. SUCCESS CHECK before declaring done: per-reader recall reported vs gate (with the explicit stronger-reader gate-crossing answer); H1 adjusted-CI gaps vs PoT and SC; H2 reduction vs the pre-registered 0.05 with CI; >=N_TARGET_DEDUCTION (or the budget-reduced floor, >=70) deduction queries scored with doc-clustered CIs; worked example + Prolog present; verdict emitted with every number TAGGED by evidence class; total spend < $9 printed. If any headline number rests on < ~70 queries, label it underpowered and lean on the synthetic + stronger-reader-recall evidence in the verdict.
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
id: art_PNrS9T8JeATf
type: dataset
title: 'Fold-split gold temporal relation graphs: NarrativeTime, TDDMan, MATRES'
summary: |-
  Frozen, reusable real-text gold temporal relation graphs that all downstream real-text closure experiments (the T0 envelope go/no-go pilot now; later arms) consume. Schema exp_sel_data_out, grouped by dataset, ONE example per (corpus, document) row (345 examples): input = the stripped document text (string), output = json.dumps(gold_graph) (string; parse with json.loads). The gold_graph has nodes [{node_id, node_type in {event,timex,dct}, surface, char_start, char_end, global_token_index, sentence_index, eiid/tid/eid, event_class, plus nt_event_type/nt_time/nt_branch/nt_start/nt_end for NarrativeTime}] and edges [{source, target, native_relation, canonical_algebra, canonical_relation_set, coarse_superset_set?, startpoint_relation_set, vague_widened, src/tgt_sentence_index, sentence_distance, locality_class in {intra,adjacent,long_distance}, structural_deduction_required_proxy (dist>=2), locally_justifiable_proxy (dist<=1), edge_fold, phenomena?}], plus per_doc_descriptive_counts. Each example also carries metadata_corpus/doc_id/fold/n_nodes/n_edges/n_events/long_distance_edges/descriptive_counts.

  Three corpora by role: (1) NarrativeTime (36 docs, 1,715 events, 103,748 edges, dense full TLink coverage, 1.58M event-event triangles) is the DENSE headline host; relations are produced by the corpus authors' OWN code (narrative_time.event_relations + conversion_utils), reproducing the shipped nt_converted_to_tml TLINKs EXACTLY (blocking gate: 207,496 relation-multisets + node counts match across all 36 docs) — non-circular gold; canonical_algebra=interval_allen with start-point point relations, non-convex {<,>} widened to {<,=,>} (vague_widened, 124 edges). (2) TDDMan (34 docs, 6,137 manually-annotated event-event pairs, 99.9% long-distance >=2 sentences apart) is the non-circularity anchor; codes {b,a,s,i,ii} mapped to tightest Allen + coarse superset + convex point sets; 107 test pairs carry TDDiscourse phenomena tags. (3) MATRES (275 docs, 6,099 events, 13,577 edges, 0% long-distance: 30% intra / 70% adjacent) is the gate-validation control with a near-empty deduction envelope; point algebra (BEFORE/AFTER/EQUAL/VAGUE -> {<}/{>}/{=}/{<,=,>}, no non-convex relations).

  Folds: document-level TimeBank-Dense 22/5/9 train/dev/test for NarrativeTime/TDDMan; MATRES train(TimeBank+AQUAINT)/test(Platinum); TDDMan edges also carry native edge_fold. One frozen NLTK Punkt sentence segmentation is reused across NarrativeTime/TDDMan; MATRES uses the canonical qiangning per-token sentence ids with SENTDIFF as authoritative distance. A doc-id overlap table (overlap_table.json) shows 33 documents shared by all three corpora. Aggregate + per-document DESCRIPTIVE structural counts (sizes, native/canonical label distributions, locality distribution, triangles, >=2-intermediate query edges, cyclomatic number, >=3-hop pairs) are in descriptive_counts.json. The gated statistics (deduction-required N*, bite-after-widening, singleton-resolution) are intentionally NOT computed here — they need composition closure / held-out-edge resolution and are the T0 experiment's job. Caveats: 1 TDDMan eid absent from the muk343 .tml version (APW19980213.1310/e257, 13 pairs dropped, reported in metadata.coverage_gaps); 238/6,099 MATRES events (3.9%) lack a char offset (boundary edge cases) but retain sentence_index + global_token_index; every non-null MATRES offset is surface-exact by construction; NarrativeTime gold uses annotator a1. Sources cited in README.md and metadata.sources (CogComp MATRES, qiangning EMNLP19 XML, TDDiscourse, text-machine-lab narrative_time, muk343 TimeBank-Dense, TempEval-3 TBAQ-cleaned). Reproduce via data.py / build_dataset.py with pinned pyproject.toml. An optional 4th TimeBank-Dense corpus builder is available (builders.build_timebank_dense) but not emitted.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

### [7] SYSTEM-USER prompt · 2026-06-17 16:29:30 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [8] SYSTEM-USER prompt · 2026-06-17 16:38:16 UTC

```
<validation-feedback>
Attempt 2 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
