# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 7 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 02:23:02 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1/results/out.json`
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
  STEP-B: Closure Certificate vs the 4-Signal Confidence Battery on the NATURAL Re-DocRED Kinship Corpus (the decisive iter-7
  open test)
summary: >-
  Run the iter-6 CLUTRR four-signal fair-baseline experiment VERBATIM on the genuinely-natural Wikipedia Re-DocRED present/absent
  kinship pools (art_NUWTxBVWENIJ), moving the load-bearing FACT-A (raw-LLM high-confidence absent-relation hallucination)
  + FACT-B (crux-survival under verbalized / sc-margin / P(True) / semantic-entropy) + mixed-pool matched-coverage selective-accuracy
  showdown + Holm-adjusted confident-wrong reductions off templated CLUTRR onto real prose. Reuse the iter-6 battery/stats/closure
  code (readers.py, kinship.py, baselines.py, stats.py, llm.py, prolog.py) by reading the frozen workspaces directly; the
  ONLY new code is (1) a natural-corpus loader that builds per-query records from the one-row-per-document dataset, (2) entity-name
  GROUNDING (LLM-extracted names -> gold entity_ids via mention-span aliases) so the certificate's forward-closure runs over
  real reads, (3) PRIMITIVE-level scoring (gender is best-effort), (4) natural-prose atomic P/R, (5) certificate-abstention
  DECOMPOSITION (correct-absent vs over-abstain-present), and (6) the pre-registered FORK verdict. Two readers run full (PRIMARY
  google/gemini-3.1-flash-lite + cross-family deepseek/deepseek-v3.2) for reader-diversity generality; optional stronger gemini-3-flash-preview
  on a stratified subsample if budget allows. Hard $9 OpenRouter cost-guard already in llm.py; expected total ~$1.5-3.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  =====================================================================
  GOAL (one sentence): reproduce iter-6 CLUTRR Section-6.1 (FACT A, FACT B crux-survival, mixed-pool matched-coverage showdown, Holm-adjusted confident-wrong reductions) on the NATURAL Re-DocRED corpus, with a publishable FORK (CONFIRM-HEADLINE vs EXTRACTION-LIMITED-BOUNDARY).
  =====================================================================

  # ---------------------------------------------------------------
  # STAGE 0  WORKSPACE SETUP (copy reusable modules verbatim; do NOT re-implement)
  # ---------------------------------------------------------------
  ITER6 = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_experiment_1
  DATASET = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1
  RESEARCH = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_research_1/research_out.json

  - Set up uv project (`uv init`; `uv add numpy scipy loguru httpx jsonschema`); copy ITER6/{readers.py, kinship.py, baselines.py, stats.py, llm.py, prolog.py} into the workspace VERBATIM. These are battle-tested and drop-in. (kinship.py here is the FORWARD-UNION least-fixpoint engine = the correct one for the finite kinship table; engine.py with POINT/ALLEN is NOT used.)
  - Load the dataset: read DATASET/full_data_out.json (4.5MB). KIN = Kinship(full['metadata']['composition_table']). The composition_table is the verbatim CLUTRR finite table; the README confirms 476/476 present + 577/577 absent engine round-trip.
  - Read research_out.json for the signal specs + reader recommendation paragraph (sanity-check the 4 signal definitions; they already match method.py).
  - Create logs/ dir; loguru to logs/run.log. Set RLIMIT_AS ~6GB like method.py _set_mem_limit. Read OPENROUTER_API_KEY from env.

  # ---------------------------------------------------------------
  # STAGE 1  NATURAL-CORPUS LOADER + ENTITY GROUNDING  (the ONLY substantively new module: dataio_redocred.py)
  # ---------------------------------------------------------------
  # CRITICAL SCHEMA FACTS (verified from mini_data_out.json):
  #   * one row per document; row['input']=detokenized prose; row['output']=json.dumps(gold_graph).
  #   * gold_graph.nodes = [{entity_id:int, surface, gender(best-effort|null), mention_spans:[[cs,ce),...]}]
  #   * gold_graph.atomic_edges = [{source:ENTITY_ID, target:ENTITY_ID, primitive, kinship_relation, target_gender, locally_justifiable,...}]  (the KB / gold proof chain)
  #   * gold_graph.query_edges = [{source:EID, target:EID, primitive(ROBUST gold), kinship_relation(gendered surface|null), target_gender, hop_count(>=2), derivation_path:[intermediate EIDs], composed_only, fully_readable}]
  #   * gold_graph.absent_relation_pairs = [{source:EID, target:EID, reason:'different_component', is_absent:true}]
  #   * source/target are ENTITY_IDS everywhere; nodes carry entity_id->surface. The reader returns NAMES -> must ground to entity_ids.

  def load_redocred(full, slice_name='re-docred'):
      rows = [ex for ds in full['datasets'] if ds['dataset']==slice_name for ex in ds['examples']]
      return rows  # 575 re-docred docs (PRIMARY); also load 'docred' (400) separately.

  def build_doc_context(row):
      gg = json.loads(row['output']); text = row['input']
      id2surface = {n['entity_id']: n['surface'] for n in gg['nodes']}
      id2gender  = {n['entity_id']: (n['gender'] or 'male') for n in gg['nodes']}  # default male only for SURFACE RENDERING; scoring is primitive-level
      # --- ALIAS TABLE for grounding LLM names -> entity_id ---
      alias2id = {}            # normalized mention string -> entity_id (or AMBIGUOUS sentinel)
      def norm(s): return re.sub(r'\s+',' ', str(s).strip().lower())
      for n in gg['nodes']:
          names = {norm(n['surface'])}
          for (cs,ce) in n['mention_spans']:
              names.add(norm(text[cs:ce]))      # every literal mention is an alias
          for nm in names:
              if not nm: continue
              if nm in alias2id and alias2id[nm]!=n['entity_id']: alias2id[nm]='AMBIGUOUS'
              else: alias2id[nm]=n['entity_id']
      return dict(text=text, gg=gg, id2surface=id2surface, id2gender=id2gender, alias2id=alias2id)

  def ground_name(name, ctx):
      # map an LLM-extracted person name to a gold entity_id (or a normalized fallback key)
      nm = norm(name)
      if nm in ctx['alias2id'] and ctx['alias2id'][nm] not in (None,'AMBIGUOUS'): return ctx['alias2id'][nm]
      # token-superset / surname match: name is a substring of (or contains) exactly ONE entity surface
      hits = {eid for al,eid in ctx['alias2id'].items() if eid not in (None,'AMBIGUOUS') and (nm in al or al in nm) and len(nm)>=3}
      if len(hits)==1: return next(iter(hits))
      return ('NAME::'+nm)   # ungroundable -> its own node (keeps certificate sound: it just won't connect to gold ids)

  # Build per-QUERY records (mirrors iter-6 record dicts so the battery/stats code plugs in unchanged):
  def build_records(rows):
      records=[]
      for row in rows:
          ctx=build_doc_context(row); gg=ctx['gg']; doc_id=gg['doc_id']
          # gold atomic edges keyed by ENTITY_ID for PoT path-finding + atomic P/R + gold-read certificate
          gold_atomics=[{'a':e['source'],'b':e['target'],'type':e['primitive']} for e in gg['atomic_edges']]
          genders_by_id=ctx['id2gender']
          for q in gg['query_edges']:                     # PRESENT (deduction-required, hop>=2)
              records.append(make_present_record(row,ctx,q,doc_id,gold_atomics,genders_by_id))
          for p in gg['absent_relation_pairs']:           # ABSENT (no-derivation)
              records.append(make_absent_record(row,ctx,p,doc_id,gold_atomics,genders_by_id))
      return records

  def make_present_record(row,ctx,q,doc_id,gold_atomics,genders):
      qsrc=q['source']; qtgt=q['target']                  # ENTITY_IDS (the closure keys)
      gold_prim=q['primitive']                            # ROBUST gold (gender-independent)
      gold_surface=q.get('kinship_relation') or KIN.surface(gold_prim, q.get('target_gender') or 'male')
      return dict(doc_id=doc_id, story=ctx['text'], qsrc=qsrc, qtgt=qtgt,
          qsrc_name=ctx['id2surface'][qsrc], qtgt_name=ctx['id2surface'][qtgt],
          gold_surface=gold_surface, gold_primitive=gold_prim, is_absent=False,
          hop=q['hop_count'], composed_only=q.get('composed_only',False), noise_type='natural',
          genders=genders, gold_atomics=gold_atomics, derivation_path=q.get('derivation_path',[]),
          slice=row['metadata_source'])

  def make_absent_record(row,ctx,p,doc_id,gold_atomics,genders):
      qsrc=p['source']; qtgt=p['target']
      return dict(doc_id=doc_id, story=ctx['text'], qsrc=qsrc, qtgt=qtgt,
          qsrc_name=ctx['id2surface'][qsrc], qtgt_name=ctx['id2surface'][qtgt],
          gold_surface='no-relation', gold_primitive='no-relation', is_absent=True,
          hop=0, composed_only=False, noise_type='natural', genders=genders,
          gold_atomics=gold_atomics, derivation_path=[], slice=row['metadata_source'])

  # NOTE: readers.raw_query_item / pot_item / extraction_item take (story, names). For the raw question use
  #   the entity SURFACES (qsrc_name/qtgt_name); for the closure KEYS use entity_ids. So wherever iter-6
  #   passed `qsrc`/`qtgt` strings to a PROMPT, pass the *name*; wherever it passed them to the CLOSURE, pass the *id*.

  # ---------------------------------------------------------------
  # STAGE 2  NEURAL READS (extraction + raw + SC + PoT) on NATURAL prose  -- adapt replay_clutrr_reads
  # ---------------------------------------------------------------
  client = OpenRouterClient(api_key, MODEL_PRIMARY='google/gemini-3.1-flash-lite',
              fallbacks=['deepseek/deepseek-v3.2','google/gemini-3-flash-preview'],
              cache_dir=HERE/'cache', temperature=0.0, budget_hard=9.0, budget_soft=4.0,
              concurrency=12, max_tokens=220)   # sha256 disk cache => warm reruns are $0

  # (a) ATOMIC EXTRACTION per DOCUMENT (one call/doc; many queries share it).
  #     Use readers.extraction_item(doc_text, doc_id) VERBATIM (its prompt 'extract family relationships from a
  #     short story' is generic prose extraction). parse_extraction -> edges with NAMES + types.
  #     Then GROUND each edge's a/b names to entity_ids:
  #        grounded_edges = [{'a':ground_name(e['a'],ctx),'b':ground_name(e['b'],ctx),'type':e['type']} for e in parsed.edges]
  #     Store r['_extracted_edges']=grounded_edges (per its doc). This is the certificate's INPUT.
  # (b) RAW forced-single per QUERY: readers.raw_query_item(story, qsrc_NAME, qtgt_NAME, doc_id, tag='raw').
  # (c) SELF-CONSISTENCY: readers.sc_items(...) but run the FULL k=10 here (iter-6 split k across cached tiers; here all 10 are new). temp=0.7, tags sc0..sc9.
  # (d) PATH-OF-THOUGHTS: build entity-NAME paths from gold_atomics via kinship.simple_paths_names(gold_atomics_AS_IDS, qsrc_id, qtgt_id) then map id-path -> name-path via id2surface (or use q['derivation_path'] endpoints). readers.pot_item(story, name_path, doc_id, pi). Absent pairs get no PoT (no path) -> abstain.
  # Batch everything through client.run_batch (async, cost-guarded). Attach r['raw'],r['sc'],r['pot'],r['off'] exactly as iter-6 replay_clutrr_reads does (parse_raw/aggregate_sc/aggregate_pot).

  # (e) CERTIFICATE prediction from the grounded reads (primitive-level):
  #     a = kinship.query_modeA(KIN, r['_extracted_edges'], r['qsrc'], r['qtgt'])  # keys are entity_ids
  #     singleton -> EMIT primitive a['answer_type'] (named=True); no_path -> ABSTAIN no-relation; conflict|D|>1 -> ABSTAIN.
  #     Build r['modeA'] = {surface: KIN.surface(answer_type, gender_of_target), primitive: answer_type, conf, named}.
  #     ALSO r['naive']=query_naive(...). ALSO r['modeA_goldread']=predict over gold_atomics (oracle-extraction ceiling).

  # ---------------------------------------------------------------
  # STAGE 3  CONFIDENCE BATTERY + ct BASELINES  (reuse run_battery / build_ct_baselines / signal defs VERBATIM)
  # ---------------------------------------------------------------
  # run_battery(records, client): issues SC k=10 (already done above; reuse cache) + P(True) (ptrue_item per query, 1 call). Attach r['_sig']={verbalized, sc_margin(top fraction of k=10), ptrue(Kadavath), negent(semantic-entropy negentropy over relation-clustered SC), H, ...}. Functions ptrue_item/parse_ptrue/semantic_entropy come straight from method.py.
  # build_ct_baselines(records): r['ct_verbalized'|'ct_sc_margin'|'ct_ptrue'|'ct_negent'] = commit raw top-1 iff signal>=tau (matched-coverage thresholding done downstream); r['commit_argmax'] = raw forced single.

  # ---------------------------------------------------------------
  # STAGE 4  PRIMITIVE-LEVEL SCORING PATCH  (the one correctness change vs iter-6)
  # ---------------------------------------------------------------
  # Gender is best-effort in DocRED, so a surface match (grandfather vs grandmother) would unfairly penalize a
  # correct-primitive read. Add a PRIMITIVE comparator and use it for query_correct / confident_wrong:
  #   pred_primitive(method_dict) = surface_reverse[surface][0] if named else None   (via KIN.surface_to_type)
  #   query_correct_prim(named, pred_prim, gold_primitive, is_absent): is_absent-> (not named); else named and pred_prim==gold_primitive
  # Wrap baselines.query_correct / confident_wrong to compare PRIMITIVES (monkeypatch or pass a scorer). Keep a
  # SECONDARY surface-level scoring column too (report both; primitive is load-bearing). For raw/sc/pot/ct the
  # emitted surface -> primitive via KIN.surface_to_type; certificate already has answer_type=primitive.

  # ---------------------------------------------------------------
  # STAGE 5  THE FOUR REPORTED OBJECTS  (reuse iter-6 functions, present_only adjusted)
  # ---------------------------------------------------------------
  run for slice='re-docred' (PRIMARY headline), then repeat present-stratum only for 'docred' (corroboration; absent gold DOWNGRADED -> do NOT use docred absent in the headline mixed pool):
    (i)  FACT A  = crux_survival_table(records)['raw_hallucination_rate_absent']  (raw named a relation on an ABSENT pair). Report per reader + the confidence distribution of those hallucinations (mean/median/quantiles of each signal) -- mirrors method.py crux_survival_table EXACTLY.
    (ii) FACT B  = crux_survival_table(...)['per_signal'][ct_s]['frac_surviving_certificate_matched_rule'] for each signal (fraction of absent hallucinations a confidence rule calibrated to the certificate's coverage still COMMITS). >=2 signals high => FACT B holds.
    (iii) MIXED-pool showdown = view3_matched_showdown(records, present_only=False): certificate vs each ct_signal + commit_argmax + pot + sc at the certificate's matched coverage on the MIXED present+absent pool (so abstain-on-everything cannot win). Report leaderboard selective_accuracy + c_star.
    (iv) Holm-adjusted confident-wrong reductions = {ct_s: cw_matched_to_ref(records,'modeA',ct_s)} -> holm_bonferroni over the 4 one-sided p's; story/doc-clustered paired bootstrap B=10000. Report reduction, ci95, p_adj, ci_excludes_0.
    ALSO view1_absent_reduction_by_signal + risk_coverage_dominance (absent + mixed) as in iter-6.

  # ---------------------------------------------------------------
  # STAGE 6  NATURAL-PROSE ATOMIC P/R  (the rigor-MAJOR tie: extraction is MEASURED not improved)
  # ---------------------------------------------------------------
  # Per doc: story_atomic_pr(grounded_extracted_edges, gold_atomic_edges_as_ids) [direction- & type-aware].
  # aggregate_atomic_pr(per_doc, doc_ids, hops, noises, B=1000) -> micro P/R/F1 + doc-clustered CI. Expect BELOW
  # CLUTRR's 0.53 (the README flags ~0.62 locally-justifiable, so recall is capped well under 1). Report by slice.
  # Map gold atomic_edges -> {a:source_id,b:target_id,type:primitive}; grounded extracted edges already use ids
  # (ungroundable names -> 'NAME::x' keys that simply never match gold => honest recall penalty).

  # ---------------------------------------------------------------
  # STAGE 7  ABSTENTION DECOMPOSITION  (the DECISIVE natural-prose nuance)
  # ---------------------------------------------------------------
  # On natural prose the extracted graph is NO LONGER trivially correct -> the certificate can OVER-ABSTAIN on
  # PRESENT pairs (missing connecting edges look disconnected). Decompose certificate abstentions on the mixed pool:
  #   correct_absent_abstentions   = #(is_absent & modeA not named)              # GOOD (structural)
  #   over_abstain_present         = #(not is_absent & modeA not named)          # the extraction-limited COST
  #   present_coverage             = mean(modeA named | present)                 # does it STILL answer present?
  #   present_selective_accuracy   = selacc(modeA on present, primitive-level)   # is it RIGHT when it answers present?
  #   gold-read ceiling            = same metrics using modeA_goldread (isolates extraction recall as the binding ceiling)
  # Report these so the FORK can be adjudicated: a high over_abstain_present with low present_coverage => extraction-limited.

  # ---------------------------------------------------------------
  # STAGE 8  CROSS-FAMILY (reader-diversity generality, reviewer novelty MAJOR-ii)  -- run deepseek-v3.2 FULL
  # ---------------------------------------------------------------
  # Re-run STAGES 2-3 with reader_model='deepseek/deepseek-v3.2' (cross-family tags cfraw/cfsc*/cfptrue so cache is
  # reader-specific). The certificate is reader-specific too (re-extract + re-ground with deepseek reads). Recompute
  # FACT A, FACT B, mixed-pool showdown, Holm reductions under deepseek. cross_family_battery in method.py is a
  # template; here run it FULL (not a subsample) on re-docred because budget allows. OPTIONAL: gemini-3-flash-preview
  # on a stratified subsample (first ~60 absent + 60 present) ONLY if client.cost < $5 -- as a stronger-reader spot check.
  # Generality verdict: FACT A high AND FACT B (>=2 signals survive) on BOTH readers => confidence-blindness is NOT kinship/model specific.

  # ---------------------------------------------------------------
  # STAGE 9  WORKED TRACES + PROLOG  (auditability requirement)
  # ---------------------------------------------------------------
  # (1) worked_no_derivation: an ABSENT pair where certificate ABSTAINS (extracted edges leave qsrc/qtgt in different
  #     components) while raw committed a relation at HIGH verbalized confidence -> show each signal value. Discharge via
  #     prolog.discharge(KIN, grounded_edges, qsrc_id, qtgt_id): real swipl if available else python-checked, labelled truthfully.
  # (2) worked_over_abstain_present (NEW for natural prose): a PRESENT pair the gold-read certificate solves but the
  #     LLM-read certificate ABSTAINS because extraction missed a connecting edge -> shows the extraction-limited boundary concretely.
  # (3) worked_present_composition_trace: a present pair the LLM-read certificate solves by composition + derivation_trace + Prolog.
  # prolog_discharge_summary over <=40 solved present queries: report n_executed_in_swipl / n_prolog_matches_python truthfully.

  # ---------------------------------------------------------------
  # STAGE 10  PRE-REGISTERED FORK VERDICT
  # ---------------------------------------------------------------
  fork:
    diagnostic_holds = (FACT_A_redocred high on >=1 reader) AND (FACT_B: >=2 signals frac_surviving>=0.5 on >=1 reader)  # corpus-robust DIAGNOSTIC
    certificate_wins_mixed = all(holm[ct_s].ci_excludes_0 and reduction>0 for s in SIGNALS) on re-docred MIXED pool
    if certificate_wins_mixed:  verdict='CONFIRM-HEADLINE'   # natural-corpus certificate beats the battery -> CLUTRR demoted to templated companion
    elif diagnostic_holds:      verdict='EXTRACTION-LIMITED-BOUNDARY'  # certificate over-abstains/ties on present (low recall) BUT FACT A+B survive (properties of raw LLM + signals, not the certificate)
    else:                       verdict='DIAGNOSTIC-WEAKER-THAN-CLAIMED'  # honest negative: some signal DOES filter confident absent hallucinations
    Record present_coverage, over_abstain_present, atomic recall alongside so the boundary is quantified, not asserted.

  # ---------------------------------------------------------------
  # STAGE 11  OUTPUT ASSEMBLY + SCHEMA VALIDATION (full/mini/preview)
  # ---------------------------------------------------------------
  # datasets grouped by pool: 'redocred_present', 'redocred_absent', 'redocred_mixed' (+ 'docred_present' corroboration).
  # per-query example row: input=(story[:1200]+' || Q: what is {qtgt_name} to {qsrc_name}?'), output=gold_surface,
  #   predict_certificate, predict_ct_verbalized/ct_sc_margin/ct_ptrue/ct_negent, predict_commit_argmax, predict_pot, predict_sc,
  #   metadata_stratum('no_derivation'|'deduction_required'), metadata_is_absent, metadata_reader('gemini-3.1-flash-lite'|'deepseek-v3.2'),
  #   metadata_doc_id, metadata_qsrc/qtgt(_name), metadata_hop, metadata_composed_only, metadata_gold_primitive,
  #   metadata_certificate_primitive, metadata_conf_verbalized/sc_margin/ptrue/negent, metadata_sc_semantic_entropy,
  #   metadata_n_extracted_edges, metadata_certificate_info.
  # metadata: headline_summary{FACT A, FACT B crux table, mixed leaderboard+Holm CIs, abstention decomposition, natural atomic P/R, cross-reader, fork verdict}, cost ledger (client.stats()), signal_definitions, honesty_caveats (NATURAL-PROSE tag; absent structural-by-construction conceded; docred absent downgraded; primitive-level scoring), per_dataset_counts (re-docred 360 present/368 absent; docred 116/209), worked traces, prolog summary.
  # Validate method_out.json against the experiment-output schema with the aii-json skill (exp_gen_sol_out; if the exact name differs, list available schemas via aii-json and pick the experiment-solution one). Generate mini_/preview_ variants with aii-json. If method_out.json > file-size limit, split per aii-file-size-limit skill.

  # ---------------------------------------------------------------
  # CLI / SCALING
  # ---------------------------------------------------------------
  # argparse: --slice {re-docred,docred,both}, --reader, --cross-family, --limit-docs N (smoke), --no-battery (cached-only), --budget-hard 9.0, --concurrency 12, --out method_out.json.
  # Gradual scaling per aii-long-running-tasks: --limit-docs 8 (only docs with present/absent queries) -> --limit-docs 60 -> FULL. Log cost after every run_batch; abort on BudgetExceeded (llm.py already enforces).
fallback_plan: |-
  ENTITY GROUNDING TOO LOSSY (LLM names don't match gold entity_ids, atomic recall collapses to ~0): (a) widen ground_name with fuzzy/Jaro-Winkler >=0.9 and last-token (surname) matching; (b) as a floor, give the extractor the LIST of gold entity surfaces in the prompt ('use exactly these names: ...') so emitted names are grounded by construction -- label this 'reader given entity inventory' (a weaker but honest variant that ISOLATES composition from NER); report BOTH ungated and inventory-given recall. The DIAGNOSTIC (FACT A/B) does NOT depend on grounding (it is about the raw answerer + signals on absent pairs), so it survives even if the certificate's grounding is weak.

  NATURAL-PROSE RECALL SO LOW THE CERTIFICATE OVER-ABSTAINS (present coverage ~0, mixed showdown ties/loses): this is the PRE-REGISTERED EXTRACTION-LIMITED-BOUNDARY fork -- report it HONESTLY as the publishable boundary; the headline becomes FACT A + FACT B (corpus-robust, reader-diverse) + the quantified extraction ceiling (atomic recall, gold-read certificate ceiling vs LLM-read), and CLUTRR stays the certificate's templated power demonstration. Still a more valuable result than deferral.

  ABSENT POOL DEGENERATE (on pure-absent, confident-wrong==coverage so the 4 signals coincide -- same subtlety method.py flags): rely on the MIXED-pool 4-way (the decisive signal-discriminating object) + the crux survival fraction; this is already how iter-6 handles it, so reuse view3_mixed + cw_matched_to_ref verbatim.

  BUDGET/TIME PRESSURE (>$5 spent or running long): drop the optional gemini-3-flash-preview; run deepseek cross-family on a stratified subsample (cf-absent 120 / cf-present 120) instead of full; skip the docred slice entirely (re-docred is the headline). The sha256 disk cache makes any partial run resumable at $0 -- never re-bill completed reads.

  SWI-PROLOG UNAVAILABLE: prolog.discharge already falls back to python-checked with truthful labelling ('NOT executed in SWI-Prolog'); report n_executed_in_swipl honestly (iter-5 had swipl, iter-6 did not -- whichever this env gives).

  SCHEMA VALIDATION FAILS: inspect the exp_gen_sol_out / experiment-solution schema via aii-json, coerce types (np scalars -> python via the _json_default helper already in method.py), ensure one-row-per-example + required predict_/output/input keys; only then write full/mini/preview.

  LLM JSON PARSE FAILURES on natural prose (longer, messier than CLUTRR): readers._load_json already strips fences + grabs first balanced block; treat unparseable extraction as zero edges (lowers certificate coverage, never fabricates) and unparseable raw as abstain -- honest, never inflates.
testing_plan: |-
  1) MODULE IMPORT + ENGINE SANITY ($0): after copying the 6 modules, run kinship.py's __main__-style check on the composition_table from full_data_out.json metadata (Lena/brother-wife-daughter -> niece) to confirm the forward-union engine loads. Confirm KIN.surface_to_type round-trips all 22 surfaces. Run the README's documented round-trip on a handful of dataset rows that HAVE atomic_edges: forward_closure over {a:source,b:target,type:primitive} must reproduce the present query golds and derive EMPTY on absent pairs (expect 476/476 + 577/577 on full; spot-check ~20 docs).

  2) GROUNDING UNIT TEST ($0): on 5 docs WITH query_edges/absent pairs, hand-verify ground_name maps mention-span aliases to the right entity_id (e.g. 'Abramo' -> Lelia or Claudio; ensure AMBIGUOUS surnames are handled). Confirm gold_atomics keyed by entity_id + derivation_path endpoints line up.

  3) DATA SMOKE: the dataset's mini_/preview_ variants mostly contain docs with EMPTY query/absent edges, so they will NOT exercise the strata. For the smoke test, filter full_data_out re-docred for docs with present_query_count>0 OR absent_pair_count>0 and take the first ~8. Run the FULL pipeline (extraction+raw+SC k=10+PoT+P(True)+certificate+battery+stats) end-to-end with --limit-docs 8 on the PRIMARY reader. Confirm: cost is a few cents, records build, r['modeA']/r['raw']/r['_sig'] populate, view3/crux/cw_matched_to_ref return finite numbers, no exceptions, output validates.

  4) CONFIRMATION SIGNALS to look for before scaling: (a) on the 8-doc smoke, the raw LLM should NAME a relation on some absent pairs (FACT A signal present, non-zero hallucination); (b) the certificate should ABSTAIN on those same absent pairs (modeA.named=False, info='no_path'); (c) certificate should NAME at least some present pairs whose extraction succeeded (present_coverage>0) -- if present_coverage is exactly 0 even on the smoke, debug grounding BEFORE the full run; (d) natural atomic P/R should be plausibly in ~0.3-0.6 (well below 1.0, consistent with the README's 0.62 locally-justifiable ceiling).

  5) SCALE GRADUALLY (aii-long-running-tasks): --limit-docs 60 (primary reader) -> verify FACT A/B/mixed-pool numbers are stable and cost is tracking ~linearly (~$0.1-0.3 at 60 docs) -> then FULL re-docred (both readers) -> then docred present-stratum corroboration. Watch logs/run.log cost line after every batch; the $9 hard cap aborts automatically.

  6) CROSS-CHECK vs iter-6: the stats functions are identical, so on any shared structure the numbers must be internally consistent (e.g. holm_bonferroni monotonicity, selective_accuracy in [0,1], reductions' CI floors at 1/(B+1)). Sanity-check that mixed-pool certificate selective accuracy > each ct_signal IF the CONFIRM fork is hit, and that the abstention decomposition's correct_absent + over_abstain_present + named == total certificate decisions.

  7) FINAL: confirm method_out.json validates against the experiment schema (aii-json), mini/preview generated, file under size limit (split if needed), fork verdict + headline_summary + cost ledger present, and at least one Prolog-discharged worked trace recorded truthfully.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_NUWTxBVWENIJ
type: dataset
title: Natural-Text Absent-Relation Kinship Corpus from Re-DocRED + DocRED
summary: |-
  Document-level KINSHIP corpus built from genuinely-natural Wikipedia introductory prose (no templating, no concatenation), for iter-7's STEP-B experiment: does a closure CERTIFICATE beat a confidence-thresholded abstainer on a real-text ABSENT-relation regime? It replaces templated CLUTRR / symbolic-id spatial corpora with real prose.

  SCHEMA: exp_sel_data_out, ONE ROW PER DOCUMENT, grouped by dataset. input = detokenized Wikipedia prose (per-token char offsets recorded; mention spans verified, offset_ok ~0.98). output = json.dumps(gold_graph) with: nodes [{entity_id, surface, type, gender(best-effort), mention_spans=[[char_start,char_end)], wikidata_qid:null}]; atomic_edges (the KB / proof chain; each flagged locally_justifiable = a span-local reader can extract it: adjacent-sentence co-occurrence + surface kinship cue); query_edges (held-out PRESENT, deduction-required: no direct annotated edge, no local co-occurrence, derivable >=2-hop composition; composed_only types grand/uncle/in-law/... are OUTSIDE DocRED's inventory => provably non-circular; fields incl primitive=robust gold, hop_count, derivation_path, fully_readable); absent_relation_pairs (both entities family-participating but in DIFFERENT connected components => no kinship path; closed-world). Flat metadata_* columns per row (fold by SHA-256%5, source, split, char_len, present/absent counts, hop_histogram, locally_justifiable_frac, offset_ok_frac, ...).

  DIRECTION CONVENTION (fixed): edge source->target with type=primitive means 'target is source's primitive'. DocRED {h,t,r} => source=h,target=t: P22->inv-child(parent,male), P25->inv-child(female), P40->child, P26->SO, P3373->sibling. P1038 is NOT in DocRED's inventory (0 edges) -> unused.

  DROP-IN ENGINE: top-level metadata.composition_table holds the CLUTRR finite kinship table verbatim (rules_store primitive compositions + relations_store surface<->primitive<->gender map; tagged NOT a relation algebra). iter-7 runs kinship.py forward least-fixpoint UNION closure UNCHANGED by mapping each atomic_edge to {a:source,b:target,type:primitive}. VERIFIED: the engine reproduces 476/476 emitted PRESENT golds and derives EMPTY for 577/577 ABSENT pairs.

  TWO DATASETS (target_num_datasets=2): 're-docred' (PRIMARY, 575 family-bearing docs from tonytan48/Re-DocRED, sha e0ab3489) gives 360 PRESENT multi-hop queries (222 composed-only/non-circular; hops 2:318/3:38/4:4) and 368 ABSENT pairs -- both EXCEED the >=150 / >=300 targets. 'docred' (SECONDARY, 400 docs from thunlp/docred, sha 7985b4e0) corroborates and demonstrates the completeness-correction: on 400 shared titles Re-DocRED carries 3087 family edges vs DocRED's 1716 (+1371, +80%), so vanilla false-negatives would corrupt absent gold -- the load-bearing reason absent labels are only trustworthy on the re-docred slice; docred absent gold is DOWNGRADED.

  HONESTY (report actuals, no padding): DocRED intro prose averages ~1020 chars; NO family-bearing doc reaches 3000 chars and only ~2.6% reach 2000 (15 docs in [2000,4000], flagged) -- we do NOT concatenate/pad; the natural-text + absent-relation regime is load-bearing, not the 3000-char target. locally_justifiable_frac ~0.62 (readability/non-circularity audit). Gender is best-effort (primitive is the robust gold when unknown). $0 LLM spend (deterministic cue check passes 100%; optional LLM judge skipped). All 3 variants validate against exp_sel_data_out; full=4.5MB (<100MB, no split). Files: data.py (uv entry), assemble.py/build.py/detok.py/kinship.py (pipeline + verbatim closure engine), verify.py, clutrr_composition_table.json, README.md.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1
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

--- Dependency 2 ---
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

### [2] HUMAN-USER prompt · 2026-06-18 02:23:02 UTC

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

### [3] SYSTEM-USER prompt · 2026-06-18 02:56:41 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_experiment_1/results/out.json`
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
  STEP-B: Closure Certificate vs the 4-Signal Confidence Battery on the NATURAL Re-DocRED Kinship Corpus (the decisive iter-7
  open test)
summary: >-
  Run the iter-6 CLUTRR four-signal fair-baseline experiment VERBATIM on the genuinely-natural Wikipedia Re-DocRED present/absent
  kinship pools (art_NUWTxBVWENIJ), moving the load-bearing FACT-A (raw-LLM high-confidence absent-relation hallucination)
  + FACT-B (crux-survival under verbalized / sc-margin / P(True) / semantic-entropy) + mixed-pool matched-coverage selective-accuracy
  showdown + Holm-adjusted confident-wrong reductions off templated CLUTRR onto real prose. Reuse the iter-6 battery/stats/closure
  code (readers.py, kinship.py, baselines.py, stats.py, llm.py, prolog.py) by reading the frozen workspaces directly; the
  ONLY new code is (1) a natural-corpus loader that builds per-query records from the one-row-per-document dataset, (2) entity-name
  GROUNDING (LLM-extracted names -> gold entity_ids via mention-span aliases) so the certificate's forward-closure runs over
  real reads, (3) PRIMITIVE-level scoring (gender is best-effort), (4) natural-prose atomic P/R, (5) certificate-abstention
  DECOMPOSITION (correct-absent vs over-abstain-present), and (6) the pre-registered FORK verdict. Two readers run full (PRIMARY
  google/gemini-3.1-flash-lite + cross-family deepseek/deepseek-v3.2) for reader-diversity generality; optional stronger gemini-3-flash-preview
  on a stratified subsample if budget allows. Hard $9 OpenRouter cost-guard already in llm.py; expected total ~$1.5-3.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  =====================================================================
  GOAL (one sentence): reproduce iter-6 CLUTRR Section-6.1 (FACT A, FACT B crux-survival, mixed-pool matched-coverage showdown, Holm-adjusted confident-wrong reductions) on the NATURAL Re-DocRED corpus, with a publishable FORK (CONFIRM-HEADLINE vs EXTRACTION-LIMITED-BOUNDARY).
  =====================================================================

  # ---------------------------------------------------------------
  # STAGE 0  WORKSPACE SETUP (copy reusable modules verbatim; do NOT re-implement)
  # ---------------------------------------------------------------
  ITER6 = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_experiment_1
  DATASET = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1
  RESEARCH = /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_research_1/research_out.json

  - Set up uv project (`uv init`; `uv add numpy scipy loguru httpx jsonschema`); copy ITER6/{readers.py, kinship.py, baselines.py, stats.py, llm.py, prolog.py} into the workspace VERBATIM. These are battle-tested and drop-in. (kinship.py here is the FORWARD-UNION least-fixpoint engine = the correct one for the finite kinship table; engine.py with POINT/ALLEN is NOT used.)
  - Load the dataset: read DATASET/full_data_out.json (4.5MB). KIN = Kinship(full['metadata']['composition_table']). The composition_table is the verbatim CLUTRR finite table; the README confirms 476/476 present + 577/577 absent engine round-trip.
  - Read research_out.json for the signal specs + reader recommendation paragraph (sanity-check the 4 signal definitions; they already match method.py).
  - Create logs/ dir; loguru to logs/run.log. Set RLIMIT_AS ~6GB like method.py _set_mem_limit. Read OPENROUTER_API_KEY from env.

  # ---------------------------------------------------------------
  # STAGE 1  NATURAL-CORPUS LOADER + ENTITY GROUNDING  (the ONLY substantively new module: dataio_redocred.py)
  # ---------------------------------------------------------------
  # CRITICAL SCHEMA FACTS (verified from mini_data_out.json):
  #   * one row per document; row['input']=detokenized prose; row['output']=json.dumps(gold_graph).
  #   * gold_graph.nodes = [{entity_id:int, surface, gender(best-effort|null), mention_spans:[[cs,ce),...]}]
  #   * gold_graph.atomic_edges = [{source:ENTITY_ID, target:ENTITY_ID, primitive, kinship_relation, target_gender, locally_justifiable,...}]  (the KB / gold proof chain)
  #   * gold_graph.query_edges = [{source:EID, target:EID, primitive(ROBUST gold), kinship_relation(gendered surface|null), target_gender, hop_count(>=2), derivation_path:[intermediate EIDs], composed_only, fully_readable}]
  #   * gold_graph.absent_relation_pairs = [{source:EID, target:EID, reason:'different_component', is_absent:true}]
  #   * source/target are ENTITY_IDS everywhere; nodes carry entity_id->surface. The reader returns NAMES -> must ground to entity_ids.

  def load_redocred(full, slice_name='re-docred'):
      rows = [ex for ds in full['datasets'] if ds['dataset']==slice_name for ex in ds['examples']]
      return rows  # 575 re-docred docs (PRIMARY); also load 'docred' (400) separately.

  def build_doc_context(row):
      gg = json.loads(row['output']); text = row['input']
      id2surface = {n['entity_id']: n['surface'] for n in gg['nodes']}
      id2gender  = {n['entity_id']: (n['gender'] or 'male') for n in gg['nodes']}  # default male only for SURFACE RENDERING; scoring is primitive-level
      # --- ALIAS TABLE for grounding LLM names -> entity_id ---
      alias2id = {}            # normalized mention string -> entity_id (or AMBIGUOUS sentinel)
      def norm(s): return re.sub(r'\s+',' ', str(s).strip().lower())
      for n in gg['nodes']:
          names = {norm(n['surface'])}
          for (cs,ce) in n['mention_spans']:
              names.add(norm(text[cs:ce]))      # every literal mention is an alias
          for nm in names:
              if not nm: continue
              if nm in alias2id and alias2id[nm]!=n['entity_id']: alias2id[nm]='AMBIGUOUS'
              else: alias2id[nm]=n['entity_id']
      return dict(text=text, gg=gg, id2surface=id2surface, id2gender=id2gender, alias2id=alias2id)

  def ground_name(name, ctx):
      # map an LLM-extracted person name to a gold entity_id (or a normalized fallback key)
      nm = norm(name)
      if nm in ctx['alias2id'] and ctx['alias2id'][nm] not in (None,'AMBIGUOUS'): return ctx['alias2id'][nm]
      # token-superset / surname match: name is a substring of (or contains) exactly ONE entity surface
      hits = {eid for al,eid in ctx['alias2id'].items() if eid not in (None,'AMBIGUOUS') and (nm in al or al in nm) and len(nm)>=3}
      if len(hits)==1: return next(iter(hits))
      return ('NAME::'+nm)   # ungroundable -> its own node (keeps certificate sound: it just won't connect to gold ids)

  # Build per-QUERY records (mirrors iter-6 record dicts so the battery/stats code plugs in unchanged):
  def build_records(rows):
      records=[]
      for row in rows:
          ctx=build_doc_context(row); gg=ctx['gg']; doc_id=gg['doc_id']
          # gold atomic edges keyed by ENTITY_ID for PoT path-finding + atomic P/R + gold-read certificate
          gold_atomics=[{'a':e['source'],'b':e['target'],'type':e['primitive']} for e in gg['atomic_edges']]
          genders_by_id=ctx['id2gender']
          for q in gg['query_edges']:                     # PRESENT (deduction-required, hop>=2)
              records.append(make_present_record(row,ctx,q,doc_id,gold_atomics,genders_by_id))
          for p in gg['absent_relation_pairs']:           # ABSENT (no-derivation)
              records.append(make_absent_record(row,ctx,p,doc_id,gold_atomics,genders_by_id))
      return records

  def make_present_record(row,ctx,q,doc_id,gold_atomics,genders):
      qsrc=q['source']; qtgt=q['target']                  # ENTITY_IDS (the closure keys)
      gold_prim=q['primitive']                            # ROBUST gold (gender-independent)
      gold_surface=q.get('kinship_relation') or KIN.surface(gold_prim, q.get('target_gender') or 'male')
      return dict(doc_id=doc_id, story=ctx['text'], qsrc=qsrc, qtgt=qtgt,
          qsrc_name=ctx['id2surface'][qsrc], qtgt_name=ctx['id2surface'][qtgt],
          gold_surface=gold_surface, gold_primitive=gold_prim, is_absent=False,
          hop=q['hop_count'], composed_only=q.get('composed_only',False), noise_type='natural',
          genders=genders, gold_atomics=gold_atomics, derivation_path=q.get('derivation_path',[]),
          slice=row['metadata_source'])

  def make_absent_record(row,ctx,p,doc_id,gold_atomics,genders):
      qsrc=p['source']; qtgt=p['target']
      return dict(doc_id=doc_id, story=ctx['text'], qsrc=qsrc, qtgt=qtgt,
          qsrc_name=ctx['id2surface'][qsrc], qtgt_name=ctx['id2surface'][qtgt],
          gold_surface='no-relation', gold_primitive='no-relation', is_absent=True,
          hop=0, composed_only=False, noise_type='natural', genders=genders,
          gold_atomics=gold_atomics, derivation_path=[], slice=row['metadata_source'])

  # NOTE: readers.raw_query_item / pot_item / extraction_item take (story, names). For the raw question use
  #   the entity SURFACES (qsrc_name/qtgt_name); for the closure KEYS use entity_ids. So wherever iter-6
  #   passed `qsrc`/`qtgt` strings to a PROMPT, pass the *name*; wherever it passed them to the CLOSURE, pass the *id*.

  # ---------------------------------------------------------------
  # STAGE 2  NEURAL READS (extraction + raw + SC + PoT) on NATURAL prose  -- adapt replay_clutrr_reads
  # ---------------------------------------------------------------
  client = OpenRouterClient(api_key, MODEL_PRIMARY='google/gemini-3.1-flash-lite',
              fallbacks=['deepseek/deepseek-v3.2','google/gemini-3-flash-preview'],
              cache_dir=HERE/'cache', temperature=0.0, budget_hard=9.0, budget_soft=4.0,
              concurrency=12, max_tokens=220)   # sha256 disk cache => warm reruns are $0

  # (a) ATOMIC EXTRACTION per DOCUMENT (one call/doc; many queries share it).
  #     Use readers.extraction_item(doc_text, doc_id) VERBATIM (its prompt 'extract family relationships from a
  #     short story' is generic prose extraction). parse_extraction -> edges with NAMES + types.
  #     Then GROUND each edge's a/b names to entity_ids:
  #        grounded_edges = [{'a':ground_name(e['a'],ctx),'b':ground_name(e['b'],ctx),'type':e['type']} for e in parsed.edges]
  #     Store r['_extracted_edges']=grounded_edges (per its doc). This is the certificate's INPUT.
  # (b) RAW forced-single per QUERY: readers.raw_query_item(story, qsrc_NAME, qtgt_NAME, doc_id, tag='raw').
  # (c) SELF-CONSISTENCY: readers.sc_items(...) but run the FULL k=10 here (iter-6 split k across cached tiers; here all 10 are new). temp=0.7, tags sc0..sc9.
  # (d) PATH-OF-THOUGHTS: build entity-NAME paths from gold_atomics via kinship.simple_paths_names(gold_atomics_AS_IDS, qsrc_id, qtgt_id) then map id-path -> name-path via id2surface (or use q['derivation_path'] endpoints). readers.pot_item(story, name_path, doc_id, pi). Absent pairs get no PoT (no path) -> abstain.
  # Batch everything through client.run_batch (async, cost-guarded). Attach r['raw'],r['sc'],r['pot'],r['off'] exactly as iter-6 replay_clutrr_reads does (parse_raw/aggregate_sc/aggregate_pot).

  # (e) CERTIFICATE prediction from the grounded reads (primitive-level):
  #     a = kinship.query_modeA(KIN, r['_extracted_edges'], r['qsrc'], r['qtgt'])  # keys are entity_ids
  #     singleton -> EMIT primitive a['answer_type'] (named=True); no_path -> ABSTAIN no-relation; conflict|D|>1 -> ABSTAIN.
  #     Build r['modeA'] = {surface: KIN.surface(answer_type, gender_of_target), primitive: answer_type, conf, named}.
  #     ALSO r['naive']=query_naive(...). ALSO r['modeA_goldread']=predict over gold_atomics (oracle-extraction ceiling).

  # ---------------------------------------------------------------
  # STAGE 3  CONFIDENCE BATTERY + ct BASELINES  (reuse run_battery / build_ct_baselines / signal defs VERBATIM)
  # ---------------------------------------------------------------
  # run_battery(records, client): issues SC k=10 (already done above; reuse cache) + P(True) (ptrue_item per query, 1 call). Attach r['_sig']={verbalized, sc_margin(top fraction of k=10), ptrue(Kadavath), negent(semantic-entropy negentropy over relation-clustered SC), H, ...}. Functions ptrue_item/parse_ptrue/semantic_entropy come straight from method.py.
  # build_ct_baselines(records): r['ct_verbalized'|'ct_sc_margin'|'ct_ptrue'|'ct_negent'] = commit raw top-1 iff signal>=tau (matched-coverage thresholding done downstream); r['commit_argmax'] = raw forced single.

  # ---------------------------------------------------------------
  # STAGE 4  PRIMITIVE-LEVEL SCORING PATCH  (the one correctness change vs iter-6)
  # ---------------------------------------------------------------
  # Gender is best-effort in DocRED, so a surface match (grandfather vs grandmother) would unfairly penalize a
  # correct-primitive read. Add a PRIMITIVE comparator and use it for query_correct / confident_wrong:
  #   pred_primitive(method_dict) = surface_reverse[surface][0] if named else None   (via KIN.surface_to_type)
  #   query_correct_prim(named, pred_prim, gold_primitive, is_absent): is_absent-> (not named); else named and pred_prim==gold_primitive
  # Wrap baselines.query_correct / confident_wrong to compare PRIMITIVES (monkeypatch or pass a scorer). Keep a
  # SECONDARY surface-level scoring column too (report both; primitive is load-bearing). For raw/sc/pot/ct the
  # emitted surface -> primitive via KIN.surface_to_type; certificate already has answer_type=primitive.

  # ---------------------------------------------------------------
  # STAGE 5  THE FOUR REPORTED OBJECTS  (reuse iter-6 functions, present_only adjusted)
  # ---------------------------------------------------------------
  run for slice='re-docred' (PRIMARY headline), then repeat present-stratum only for 'docred' (corroboration; absent gold DOWNGRADED -> do NOT use docred absent in the headline mixed pool):
    (i)  FACT A  = crux_survival_table(records)['raw_hallucination_rate_absent']  (raw named a relation on an ABSENT pair). Report per reader + the confidence distribution of those hallucinations (mean/median/quantiles of each signal) -- mirrors method.py crux_survival_table EXACTLY.
    (ii) FACT B  = crux_survival_table(...)['per_signal'][ct_s]['frac_surviving_certificate_matched_rule'] for each signal (fraction of absent hallucinations a confidence rule calibrated to the certificate's coverage still COMMITS). >=2 signals high => FACT B holds.
    (iii) MIXED-pool showdown = view3_matched_showdown(records, present_only=False): certificate vs each ct_signal + commit_argmax + pot + sc at the certificate's matched coverage on the MIXED present+absent pool (so abstain-on-everything cannot win). Report leaderboard selective_accuracy + c_star.
    (iv) Holm-adjusted confident-wrong reductions = {ct_s: cw_matched_to_ref(records,'modeA',ct_s)} -> holm_bonferroni over the 4 one-sided p's; story/doc-clustered paired bootstrap B=10000. Report reduction, ci95, p_adj, ci_excludes_0.
    ALSO view1_absent_reduction_by_signal + risk_coverage_dominance (absent + mixed) as in iter-6.

  # ---------------------------------------------------------------
  # STAGE 6  NATURAL-PROSE ATOMIC P/R  (the rigor-MAJOR tie: extraction is MEASURED not improved)
  # ---------------------------------------------------------------
  # Per doc: story_atomic_pr(grounded_extracted_edges, gold_atomic_edges_as_ids) [direction- & type-aware].
  # aggregate_atomic_pr(per_doc, doc_ids, hops, noises, B=1000) -> micro P/R/F1 + doc-clustered CI. Expect BELOW
  # CLUTRR's 0.53 (the README flags ~0.62 locally-justifiable, so recall is capped well under 1). Report by slice.
  # Map gold atomic_edges -> {a:source_id,b:target_id,type:primitive}; grounded extracted edges already use ids
  # (ungroundable names -> 'NAME::x' keys that simply never match gold => honest recall penalty).

  # ---------------------------------------------------------------
  # STAGE 7  ABSTENTION DECOMPOSITION  (the DECISIVE natural-prose nuance)
  # ---------------------------------------------------------------
  # On natural prose the extracted graph is NO LONGER trivially correct -> the certificate can OVER-ABSTAIN on
  # PRESENT pairs (missing connecting edges look disconnected). Decompose certificate abstentions on the mixed pool:
  #   correct_absent_abstentions   = #(is_absent & modeA not named)              # GOOD (structural)
  #   over_abstain_present         = #(not is_absent & modeA not named)          # the extraction-limited COST
  #   present_coverage             = mean(modeA named | present)                 # does it STILL answer present?
  #   present_selective_accuracy   = selacc(modeA on present, primitive-level)   # is it RIGHT when it answers present?
  #   gold-read ceiling            = same metrics using modeA_goldread (isolates extraction recall as the binding ceiling)
  # Report these so the FORK can be adjudicated: a high over_abstain_present with low present_coverage => extraction-limited.

  # ---------------------------------------------------------------
  # STAGE 8  CROSS-FAMILY (reader-diversity generality, reviewer novelty MAJOR-ii)  -- run deepseek-v3.2 FULL
  # ---------------------------------------------------------------
  # Re-run STAGES 2-3 with reader_model='deepseek/deepseek-v3.2' (cross-family tags cfraw/cfsc*/cfptrue so cache is
  # reader-specific). The certificate is reader-specific too (re-extract + re-ground with deepseek reads). Recompute
  # FACT A, FACT B, mixed-pool showdown, Holm reductions under deepseek. cross_family_battery in method.py is a
  # template; here run it FULL (not a subsample) on re-docred because budget allows. OPTIONAL: gemini-3-flash-preview
  # on a stratified subsample (first ~60 absent + 60 present) ONLY if client.cost < $5 -- as a stronger-reader spot check.
  # Generality verdict: FACT A high AND FACT B (>=2 signals survive) on BOTH readers => confidence-blindness is NOT kinship/model specific.

  # ---------------------------------------------------------------
  # STAGE 9  WORKED TRACES + PROLOG  (auditability requirement)
  # ---------------------------------------------------------------
  # (1) worked_no_derivation: an ABSENT pair where certificate ABSTAINS (extracted edges leave qsrc/qtgt in different
  #     components) while raw committed a relation at HIGH verbalized confidence -> show each signal value. Discharge via
  #     prolog.discharge(KIN, grounded_edges, qsrc_id, qtgt_id): real swipl if available else python-checked, labelled truthfully.
  # (2) worked_over_abstain_present (NEW for natural prose): a PRESENT pair the gold-read certificate solves but the
  #     LLM-read certificate ABSTAINS because extraction missed a connecting edge -> shows the extraction-limited boundary concretely.
  # (3) worked_present_composition_trace: a present pair the LLM-read certificate solves by composition + derivation_trace + Prolog.
  # prolog_discharge_summary over <=40 solved present queries: report n_executed_in_swipl / n_prolog_matches_python truthfully.

  # ---------------------------------------------------------------
  # STAGE 10  PRE-REGISTERED FORK VERDICT
  # ---------------------------------------------------------------
  fork:
    diagnostic_holds = (FACT_A_redocred high on >=1 reader) AND (FACT_B: >=2 signals frac_surviving>=0.5 on >=1 reader)  # corpus-robust DIAGNOSTIC
    certificate_wins_mixed = all(holm[ct_s].ci_excludes_0 and reduction>0 for s in SIGNALS) on re-docred MIXED pool
    if certificate_wins_mixed:  verdict='CONFIRM-HEADLINE'   # natural-corpus certificate beats the battery -> CLUTRR demoted to templated companion
    elif diagnostic_holds:      verdict='EXTRACTION-LIMITED-BOUNDARY'  # certificate over-abstains/ties on present (low recall) BUT FACT A+B survive (properties of raw LLM + signals, not the certificate)
    else:                       verdict='DIAGNOSTIC-WEAKER-THAN-CLAIMED'  # honest negative: some signal DOES filter confident absent hallucinations
    Record present_coverage, over_abstain_present, atomic recall alongside so the boundary is quantified, not asserted.

  # ---------------------------------------------------------------
  # STAGE 11  OUTPUT ASSEMBLY + SCHEMA VALIDATION (full/mini/preview)
  # ---------------------------------------------------------------
  # datasets grouped by pool: 'redocred_present', 'redocred_absent', 'redocred_mixed' (+ 'docred_present' corroboration).
  # per-query example row: input=(story[:1200]+' || Q: what is {qtgt_name} to {qsrc_name}?'), output=gold_surface,
  #   predict_certificate, predict_ct_verbalized/ct_sc_margin/ct_ptrue/ct_negent, predict_commit_argmax, predict_pot, predict_sc,
  #   metadata_stratum('no_derivation'|'deduction_required'), metadata_is_absent, metadata_reader('gemini-3.1-flash-lite'|'deepseek-v3.2'),
  #   metadata_doc_id, metadata_qsrc/qtgt(_name), metadata_hop, metadata_composed_only, metadata_gold_primitive,
  #   metadata_certificate_primitive, metadata_conf_verbalized/sc_margin/ptrue/negent, metadata_sc_semantic_entropy,
  #   metadata_n_extracted_edges, metadata_certificate_info.
  # metadata: headline_summary{FACT A, FACT B crux table, mixed leaderboard+Holm CIs, abstention decomposition, natural atomic P/R, cross-reader, fork verdict}, cost ledger (client.stats()), signal_definitions, honesty_caveats (NATURAL-PROSE tag; absent structural-by-construction conceded; docred absent downgraded; primitive-level scoring), per_dataset_counts (re-docred 360 present/368 absent; docred 116/209), worked traces, prolog summary.
  # Validate method_out.json against the experiment-output schema with the aii-json skill (exp_gen_sol_out; if the exact name differs, list available schemas via aii-json and pick the experiment-solution one). Generate mini_/preview_ variants with aii-json. If method_out.json > file-size limit, split per aii-file-size-limit skill.

  # ---------------------------------------------------------------
  # CLI / SCALING
  # ---------------------------------------------------------------
  # argparse: --slice {re-docred,docred,both}, --reader, --cross-family, --limit-docs N (smoke), --no-battery (cached-only), --budget-hard 9.0, --concurrency 12, --out method_out.json.
  # Gradual scaling per aii-long-running-tasks: --limit-docs 8 (only docs with present/absent queries) -> --limit-docs 60 -> FULL. Log cost after every run_batch; abort on BudgetExceeded (llm.py already enforces).
fallback_plan: |-
  ENTITY GROUNDING TOO LOSSY (LLM names don't match gold entity_ids, atomic recall collapses to ~0): (a) widen ground_name with fuzzy/Jaro-Winkler >=0.9 and last-token (surname) matching; (b) as a floor, give the extractor the LIST of gold entity surfaces in the prompt ('use exactly these names: ...') so emitted names are grounded by construction -- label this 'reader given entity inventory' (a weaker but honest variant that ISOLATES composition from NER); report BOTH ungated and inventory-given recall. The DIAGNOSTIC (FACT A/B) does NOT depend on grounding (it is about the raw answerer + signals on absent pairs), so it survives even if the certificate's grounding is weak.

  NATURAL-PROSE RECALL SO LOW THE CERTIFICATE OVER-ABSTAINS (present coverage ~0, mixed showdown ties/loses): this is the PRE-REGISTERED EXTRACTION-LIMITED-BOUNDARY fork -- report it HONESTLY as the publishable boundary; the headline becomes FACT A + FACT B (corpus-robust, reader-diverse) + the quantified extraction ceiling (atomic recall, gold-read certificate ceiling vs LLM-read), and CLUTRR stays the certificate's templated power demonstration. Still a more valuable result than deferral.

  ABSENT POOL DEGENERATE (on pure-absent, confident-wrong==coverage so the 4 signals coincide -- same subtlety method.py flags): rely on the MIXED-pool 4-way (the decisive signal-discriminating object) + the crux survival fraction; this is already how iter-6 handles it, so reuse view3_mixed + cw_matched_to_ref verbatim.

  BUDGET/TIME PRESSURE (>$5 spent or running long): drop the optional gemini-3-flash-preview; run deepseek cross-family on a stratified subsample (cf-absent 120 / cf-present 120) instead of full; skip the docred slice entirely (re-docred is the headline). The sha256 disk cache makes any partial run resumable at $0 -- never re-bill completed reads.

  SWI-PROLOG UNAVAILABLE: prolog.discharge already falls back to python-checked with truthful labelling ('NOT executed in SWI-Prolog'); report n_executed_in_swipl honestly (iter-5 had swipl, iter-6 did not -- whichever this env gives).

  SCHEMA VALIDATION FAILS: inspect the exp_gen_sol_out / experiment-solution schema via aii-json, coerce types (np scalars -> python via the _json_default helper already in method.py), ensure one-row-per-example + required predict_/output/input keys; only then write full/mini/preview.

  LLM JSON PARSE FAILURES on natural prose (longer, messier than CLUTRR): readers._load_json already strips fences + grabs first balanced block; treat unparseable extraction as zero edges (lowers certificate coverage, never fabricates) and unparseable raw as abstain -- honest, never inflates.
testing_plan: |-
  1) MODULE IMPORT + ENGINE SANITY ($0): after copying the 6 modules, run kinship.py's __main__-style check on the composition_table from full_data_out.json metadata (Lena/brother-wife-daughter -> niece) to confirm the forward-union engine loads. Confirm KIN.surface_to_type round-trips all 22 surfaces. Run the README's documented round-trip on a handful of dataset rows that HAVE atomic_edges: forward_closure over {a:source,b:target,type:primitive} must reproduce the present query golds and derive EMPTY on absent pairs (expect 476/476 + 577/577 on full; spot-check ~20 docs).

  2) GROUNDING UNIT TEST ($0): on 5 docs WITH query_edges/absent pairs, hand-verify ground_name maps mention-span aliases to the right entity_id (e.g. 'Abramo' -> Lelia or Claudio; ensure AMBIGUOUS surnames are handled). Confirm gold_atomics keyed by entity_id + derivation_path endpoints line up.

  3) DATA SMOKE: the dataset's mini_/preview_ variants mostly contain docs with EMPTY query/absent edges, so they will NOT exercise the strata. For the smoke test, filter full_data_out re-docred for docs with present_query_count>0 OR absent_pair_count>0 and take the first ~8. Run the FULL pipeline (extraction+raw+SC k=10+PoT+P(True)+certificate+battery+stats) end-to-end with --limit-docs 8 on the PRIMARY reader. Confirm: cost is a few cents, records build, r['modeA']/r['raw']/r['_sig'] populate, view3/crux/cw_matched_to_ref return finite numbers, no exceptions, output validates.

  4) CONFIRMATION SIGNALS to look for before scaling: (a) on the 8-doc smoke, the raw LLM should NAME a relation on some absent pairs (FACT A signal present, non-zero hallucination); (b) the certificate should ABSTAIN on those same absent pairs (modeA.named=False, info='no_path'); (c) certificate should NAME at least some present pairs whose extraction succeeded (present_coverage>0) -- if present_coverage is exactly 0 even on the smoke, debug grounding BEFORE the full run; (d) natural atomic P/R should be plausibly in ~0.3-0.6 (well below 1.0, consistent with the README's 0.62 locally-justifiable ceiling).

  5) SCALE GRADUALLY (aii-long-running-tasks): --limit-docs 60 (primary reader) -> verify FACT A/B/mixed-pool numbers are stable and cost is tracking ~linearly (~$0.1-0.3 at 60 docs) -> then FULL re-docred (both readers) -> then docred present-stratum corroboration. Watch logs/run.log cost line after every batch; the $9 hard cap aborts automatically.

  6) CROSS-CHECK vs iter-6: the stats functions are identical, so on any shared structure the numbers must be internally consistent (e.g. holm_bonferroni monotonicity, selective_accuracy in [0,1], reductions' CI floors at 1/(B+1)). Sanity-check that mixed-pool certificate selective accuracy > each ct_signal IF the CONFIRM fork is hit, and that the abstention decomposition's correct_absent + over_abstain_present + named == total certificate decisions.

  7) FINAL: confirm method_out.json validates against the experiment schema (aii-json), mini/preview generated, file under size limit (split if needed), fork verdict + headline_summary + cost ledger present, and at least one Prolog-discharged worked trace recorded truthfully.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_NUWTxBVWENIJ
type: dataset
title: Natural-Text Absent-Relation Kinship Corpus from Re-DocRED + DocRED
summary: |-
  Document-level KINSHIP corpus built from genuinely-natural Wikipedia introductory prose (no templating, no concatenation), for iter-7's STEP-B experiment: does a closure CERTIFICATE beat a confidence-thresholded abstainer on a real-text ABSENT-relation regime? It replaces templated CLUTRR / symbolic-id spatial corpora with real prose.

  SCHEMA: exp_sel_data_out, ONE ROW PER DOCUMENT, grouped by dataset. input = detokenized Wikipedia prose (per-token char offsets recorded; mention spans verified, offset_ok ~0.98). output = json.dumps(gold_graph) with: nodes [{entity_id, surface, type, gender(best-effort), mention_spans=[[char_start,char_end)], wikidata_qid:null}]; atomic_edges (the KB / proof chain; each flagged locally_justifiable = a span-local reader can extract it: adjacent-sentence co-occurrence + surface kinship cue); query_edges (held-out PRESENT, deduction-required: no direct annotated edge, no local co-occurrence, derivable >=2-hop composition; composed_only types grand/uncle/in-law/... are OUTSIDE DocRED's inventory => provably non-circular; fields incl primitive=robust gold, hop_count, derivation_path, fully_readable); absent_relation_pairs (both entities family-participating but in DIFFERENT connected components => no kinship path; closed-world). Flat metadata_* columns per row (fold by SHA-256%5, source, split, char_len, present/absent counts, hop_histogram, locally_justifiable_frac, offset_ok_frac, ...).

  DIRECTION CONVENTION (fixed): edge source->target with type=primitive means 'target is source's primitive'. DocRED {h,t,r} => source=h,target=t: P22->inv-child(parent,male), P25->inv-child(female), P40->child, P26->SO, P3373->sibling. P1038 is NOT in DocRED's inventory (0 edges) -> unused.

  DROP-IN ENGINE: top-level metadata.composition_table holds the CLUTRR finite kinship table verbatim (rules_store primitive compositions + relations_store surface<->primitive<->gender map; tagged NOT a relation algebra). iter-7 runs kinship.py forward least-fixpoint UNION closure UNCHANGED by mapping each atomic_edge to {a:source,b:target,type:primitive}. VERIFIED: the engine reproduces 476/476 emitted PRESENT golds and derives EMPTY for 577/577 ABSENT pairs.

  TWO DATASETS (target_num_datasets=2): 're-docred' (PRIMARY, 575 family-bearing docs from tonytan48/Re-DocRED, sha e0ab3489) gives 360 PRESENT multi-hop queries (222 composed-only/non-circular; hops 2:318/3:38/4:4) and 368 ABSENT pairs -- both EXCEED the >=150 / >=300 targets. 'docred' (SECONDARY, 400 docs from thunlp/docred, sha 7985b4e0) corroborates and demonstrates the completeness-correction: on 400 shared titles Re-DocRED carries 3087 family edges vs DocRED's 1716 (+1371, +80%), so vanilla false-negatives would corrupt absent gold -- the load-bearing reason absent labels are only trustworthy on the re-docred slice; docred absent gold is DOWNGRADED.

  HONESTY (report actuals, no padding): DocRED intro prose averages ~1020 chars; NO family-bearing doc reaches 3000 chars and only ~2.6% reach 2000 (15 docs in [2000,4000], flagged) -- we do NOT concatenate/pad; the natural-text + absent-relation regime is load-bearing, not the 3000-char target. locally_justifiable_frac ~0.62 (readability/non-circularity audit). Gender is best-effort (primitive is the robust gold when unknown). $0 LLM spend (deterministic cue check passes 100%; optional LLM judge skipped). All 3 variants validate against exp_sel_data_out; full=4.5MB (<100MB, no split). Files: data.py (uv entry), assemble.py/build.py/detok.py/kinship.py (pipeline + verbatim closure engine), verify.py, clutrr_composition_table.json, README.md.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1
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

--- Dependency 2 ---
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

### [4] SYSTEM-USER prompt · 2026-06-18 02:59:25 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [5] SYSTEM-USER prompt · 2026-06-18 03:05:57 UTC

```
<validation-feedback>
Attempt 2 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
