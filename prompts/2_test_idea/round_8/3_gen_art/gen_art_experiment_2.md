# gen_art_experiment_2 — test_idea

> Phase: `invention_loop` · round 8 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_2` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 04:10:06 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_2/results/out.json`
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
id: gen_plan_experiment_2_idx3
type: experiment
title: >-
  Query-Side False-Premise Verifier vs the No-Derivation Certificate on Cached CLUTRR + Re-DocRED Kinship Pools (matched coverage,
  $0-gate + <$1 new spend)
summary: >-
  Reviewer-mandated DISCONFIRM test for the closure-certificate paper. Reuse the two EXISTING, fully-cached prediction pools
  (CLUTRR battery art_LeRQRGHJZcdQ @ iter_6/gen_art/gen_art_experiment_1; Re-DocRED kinship battery art_htcr8yOZLCQy @ iter_7/gen_art/gen_art_experiment_1)
  by direct filesystem read, plus their llm.py (sha256-cached, $9-guarded OpenRouter client) and stats.py (matched-coverage
  selective accuracy, paired bootstrap, Holm). A $0 reproduction gate first re-derives FACT-A / crux-survival / certificate
  leaderboard literals from the carried row fields and asserts they match each file's own aggregates AND the published constants
  (CLUTRR 0.472 gemini / 0.483 deepseek; Re-DocRED 0.326 / 0.318). Then the ONLY new spend: for every (query x reader) row
  in both pools, call a query-side false-premise VERIFIER ('are X and Y related by kinship at all?') and a SELF-VERIFICATION
  pass ('is it true that Y is <raw answer> to X?'), reader-matched (gemini-3.1-flash-lite or deepseek-v3.2), sha256-cached,
  est. <$1 / hard cap $9. Analysis sweeps the verifier confidence to MATCH the certificate's coverage on present / absent
  / mixed pools and reports, per venue x reader: matched-coverage selective accuracy & confident-wrong rate of the verifier
  and self-verify vs the certificate vs the four dispersion signals with Holm-adjusted doc-clustered bootstrap CIs; fraction-caught
  crux tables; and a per-venue certificate-necessity verdict (verifier MATCHES/BEATS certificate => structural certificate
  not strictly needed, honest negative; certificate still beats => structural signal necessary). Output method_out.json (exp_gen_sol_out,
  validated, full/mini/preview).
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  ############################################################
  # GOAL: add a query-side false-premise VERIFIER + SELF-VERIFY baseline to the two
  # already-powered cached venues, benchmark them against the no-derivation certificate
  # and the 4 dispersion signals at MATCHED COVERAGE, and emit a per-venue verdict.
  # This is REUSE-HEAVY: the certificate / raw / 4-signal predictions ALREADY EXIST in
  # the cached pools; the ONLY new LLM calls are the verifier + self-verify (<$1).
  ############################################################

  # ----- CONSTANTS / PATHS (verify each exists at startup; fail loud if missing) -----
  RUN = '/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop'
  CLUTRR_POOL  = RUN+'/iter_6/gen_art/gen_art_experiment_1/method_out.json'   # art_LeRQRGHJZcdQ
  REDOCRED_POOL= RUN+'/iter_7/gen_art/gen_art_experiment_1/method_out.json'   # art_htcr8yOZLCQy
  SRC_LLM   = RUN+'/iter_7/gen_art/gen_art_experiment_1/llm.py'   # copy VERBATIM into workspace
  SRC_STATS = RUN+'/iter_7/gen_art/gen_art_experiment_1/stats.py' # copy VERBATIM into workspace
  # (optional cross-checks only) dataset deps:
  #   art_HS7-lxhZnU9m CLUTRR gold graphs @ iter_2/gen_art/gen_art_dataset_1
  #   art_NUWTxBVWENIJ Re-DocRED corpus  @ iter_6/gen_art/gen_art_dataset_1
  # Pools are SELF-CONTAINED (each row carries `input` = the story/doc text + entity names + gold),
  # so the dataset deps are needed only as a fallback if a name/doc field is missing.
  PRIMARY_MODEL = 'google/gemini-3.1-flash-lite'
  CROSS_MODEL   = 'deepseek/deepseek-v3.2'
  FALLBACKS     = ['google/gemini-3-flash-preview']
  PUBLISHED_FACT_A = {('clutrr','gemini'):0.472, ('clutrr','deepseek'):0.483,
                      ('redocred','gemini'):0.326, ('redocred','deepseek'):0.318}
  B_BOOT = 10000; SEED = 20260618; ALPHA = 0.05

  # === PHASE 0: workspace setup ===
  # 1. `uv init`; add deps: httpx, loguru, numpy, scipy, jsonschema (mirror iter_7 pyproject.toml).
  # 2. Copy SRC_LLM -> ./llm.py and SRC_STATS -> ./stats.py VERBATIM (do not edit; import them).
  # 3. mkdir ./cache  (NEW workspace cache: verifier prompts differ from battery prompts so keys never collide;
  #    re-runs are free). NEVER write into the source workspaces' cache/ (read-only reuse).
  # 4. Read OPENROUTER_API_KEY from env (same as battery).

  # === PHASE 1: load + normalize both cached pools (introspect, do NOT assume identical fields) ===
  def load_pool(path, pool_name):
      obj = json.load(open(path))
      # exp_sel_data_out: rows live under per-dataset groups (obj['data'][i]['examples']) OR a flat
      # 'examples' list. Walk obj recursively; collect every dict that has BOTH 'input' and a
      # 'metadata_is_absent' (or 'metadata_stratum') key -> that is a row.
      rows = collect_row_dicts(obj)
      norm = []
      for r in rows:
          m = {k[len('metadata_'):]: v for k,v in r.items() if k.startswith('metadata_')}
          reader = (m.get('reader') or m.get('model') or infer_reader_from_group(r)
                    or 'gemini')   # CLUTRR may lack metadata_reader; fall back to group/model tag
          reader = 'deepseek' if 'deepseek' in str(reader).lower() else ('gemini' if 'gemini' in str(reader).lower() else reader)
          qsrc = m.get('qsrc_name') or m.get('qsrc')   # CLUTRR uses qsrc/qtgt (names); Re-DocRED qsrc_name/qtgt_name
          qtgt = m.get('qtgt_name') or m.get('qtgt')
          norm.append(dict(
              pool=pool_name, reader=reader,
              doc_id=r.get('doc_id') or m.get('doc_id') or m.get('title'),
              doc_text=r['input'],
              is_absent=bool(m.get('is_absent', (m.get('stratum','').endswith('absent')))),
              stratum=m.get('stratum'),
              qsrc=qsrc, qtgt=qtgt,
              gold=normalize_gold(r.get('gold') or m.get('gold_primitive')),  # 'no-relation' on absent
              raw_named=m.get('raw_named'),                # raw LLM committed single answer (may be 'no-relation'/None)
              conf=dict(verbalized=m.get('conf_verbalized'), sc_margin=m.get('conf_sc_margin'),
                        ptrue=m.get('conf_ptrue'), negent=m.get('conf_negent')),
              # carried predictions (strings) reused as-is for the certificate + dispersion + commit baselines:
              predict_certificate=r.get('predict_certificate'),
              predict_conf_thresh={s:r.get('predict_conf_thresh_'+s) for s in ['verbalized','sc_margin','ptrue','negent']},
              predict_commit_argmax=r.get('predict_commit_argmax'),
              cert_info=m.get('certificate_info'),
              raw_row=r))
      return norm
  recs = load_pool(CLUTRR_POOL,'clutrr') + load_pool(REDOCRED_POOL,'redocred')
  # Sanity: assert per-pool/reader/stratum counts match objective (clutrr 102 present + 180 absent;
  # redocred 360 present + 368 absent) PER READER; log actuals (handle small drift, don't hard-fail on +-).

  # === PHASE 2: REPRODUCTION GATE ($0 -- must pass before ANY new spend) ===
  # Re-derive the published literals from row fields and compare to (a) each file's OWN carried
  # aggregates (top-level 'leaderboard','crux_survival_table','verdict') and (b) PUBLISHED_FACT_A.
  # A2.1 FACT-A rate: for each (pool,reader): among ABSENT rows, fraction where raw_named is a REAL
  #       relation (not 'no-relation'/None) AND it is a 'high-confidence' commit per the battery's
  #       definition (replicate the battery's threshold: read it from the carried aggregate metadata if
  #       present; else use raw committed-answer present == high-conf by construction at the LLM's
  #       natural no-abstention coverage). assert |recomputed - PUBLISHED_FACT_A[(pool,reader)]| < 5e-3.
  # A2.2 crux-survival / fraction-caught for each dispersion signal at the certificate's coverage:
  #       recompute from conf[*] + raw_named + gold; assert == carried crux_survival_table (0 mismatch, tol 5e-3).
  # A2.3 certificate mixed-pool selective accuracy + confident-wrong reductions: recompute via stats.py
  #       (matched_coverage_mask at certificate coverage) and assert == carried leaderboard (tol 5e-3).
  # A2.4 assert client.cost == 0.0 so far.
  # Emit reproduction_gate = {checks:[{name,recomputed,carried,published,ok}], all_ok:bool}.
  # IF not all_ok: WRITE the gate report into method_out.json and HARD STOP (do not spend) -- a corrupted
  # pool must be surfaced, not built upon.

  # === PHASE 3: build NEW verifier + self-verify LLM items (the only new spend) ===
  VERIFIER_SYS = ('You judge whether two named people are connected by ANY family/kinship relationship '
    '(directly stated OR derivable through a chain of relatives) according ONLY to the given text. '
    'Output ONLY JSON {"related": "RELATED"|"UNRELATED", "confidence": <0..1>}. confidence is your '
    'probability that your RELATED/UNRELATED judgement is correct.')
  SELFVERIFY_SYS = ('You verify a claimed family relationship against a text. Output ONLY JSON '
    '{"verdict": "TRUE"|"FALSE", "confidence": <0..1>}. TRUE iff the claim is actually correct given the text.')
  def model_for(reader): return PRIMARY_MODEL if reader=='gemini' else CROSS_MODEL
  items = []
  for i,rec in enumerate(recs):
      mdl = model_for(rec['reader'])
      # (a) QUERY-SIDE FALSE-PREMISE VERIFIER -- one call per row
      items.append(dict(id=f"ver::{rec['pool']}::{i}", model=mdl, tag='verifier', max_tokens=60, temperature=0.0,
          system=VERIFIER_SYS,
          user=f"Text:\n{rec['doc_text']}\n\nQuestion: Are {rec['qsrc']} and {rec['qtgt']} related by family/kinship at all (directly or via any chain of relatives in the text)? Answer with the JSON object."))
      # (b) SELF-VERIFICATION of the raw committed answer -- skip if raw said no-relation/None (set later)
      if rec['raw_named'] and rec['raw_named'] != 'no-relation':
          items.append(dict(id=f"sv::{rec['pool']}::{i}", model=mdl, tag='selfverify', max_tokens=60, temperature=0.0,
              system=SELFVERIFY_SYS,
              user=f"Text:\n{rec['doc_text']}\n\nClaim: {rec['qtgt']} is {rec['qsrc']}'s {rec['raw_named']}. Is this claim actually true given the text? Answer with the JSON object."))
  # Run with reader-matched models. llm.py keys cache on (model, temp, tag, system, user) so we can run
  # the two models in two batches OR set client.model per item-group. Simplest: group items by model,
  # instantiate OpenRouterClient(api_key, model=mdl, fallbacks=FALLBACKS, cache_dir='./cache',
  #   budget_hard=9.0, budget_soft=2.0, concurrency=12, max_tokens=60, temperature=0.0) per model,
  # results = asyncio.run(client.run_batch(group)).  Merge results by id. Track cumulative cost across
  # both clients; abort cleanly on BudgetExceeded (cached partials still usable).

  # === PHASE 4: parse verifier outputs -> per-row method triples (prediction:str, confidence:float, abstain:bool) ===
  # Reuse llm._load_json-style robust parsing (copy the helper or import from readers if copied).
  def parse_verifier(content): # -> (related:bool|None, conf:float)
      obj=_load_json(content); rel=str(obj.get('related','')).upper() if obj else ''
      conf=clip01(float(obj.get('confidence',0.5))) if obj else 0.5
      return (True if rel=='RELATED' else False if rel=='UNRELATED' else None), conf
  def parse_selfverify(content): obj=_load_json(content); v=str(obj.get('verdict','')).upper() if obj else ''; return (v=='TRUE') if v in('TRUE','FALSE') else None, clip01(float(obj.get('confidence',0.5)) if obj else 0.5)
  for i,rec in enumerate(recs):
      rel, vconf = parse_verifier(results.get(f"ver::{rec['pool']}::{i}",{}).get('content',''))
      # p_related: high => keep as related; used both as classifier decision and as coverage-confidence
      p_related = vconf if rel else (1.0-vconf if rel is False else 0.5)
      # PRIMARY framing = CORRECTIVE GATE (FalseQA-style false-premise detector, mirrors certificate which
      # actively answers 'no-relation' on absent pairs):
      rec['predict_queryside_verifier'] = ('no-relation' if rel is False else (rec['raw_named'] or 'no-relation'))
      rec['conf_queryside_verifier']    = max(p_related, 1.0-p_related)  # distance-from-boundary = abstain ranking
      rec['p_related'] = p_related
      # SENSITIVITY framing = pure ABSTENTION SIGNAL (always commit raw answer, rank by p_related), like the
      # 4 dispersion signals: prediction = raw_named always; confidence = p_related.
      rec['predict_verifier_as_signal'] = rec['raw_named'] or 'no-relation'
      rec['conf_verifier_as_signal']    = p_related
      # SELF-VERIFY: keep raw answer iff verdict TRUE else 'no-relation'; if raw was no-relation/None, keep it.
      if rec['raw_named'] and rec['raw_named']!='no-relation':
          tv, sconf = parse_selfverify(results.get(f"sv::{rec['pool']}::{i}",{}).get('content',''))
          rec['predict_queryside_selfverify'] = (rec['raw_named'] if tv else 'no-relation')
          rec['conf_queryside_selfverify']    = sconf if tv is not None else 0.5
      else:
          rec['predict_queryside_selfverify'] = 'no-relation'; rec['conf_queryside_selfverify']=rec['conf'].get('ptrue') or 0.5

  # === PHASE 5: matched-coverage analysis (reuse stats.py; mirror the battery exactly) ===
  # METHODS = {certificate, conf_verbalized, conf_sc_margin, conf_ptrue, conf_negent,
  #            queryside_verifier, queryside_selfverify, verifier_as_signal(sensitivity), commit_argmax}
  # For each VENUE-POOL in {clutrr_present, clutrr_absent, redocred_present, redocred_absent} AND the two
  # MIXED pools {clutrr_mixed, redocred_mixed}, and for each READER in {gemini, deepseek}:
  #   correct(method,row) = (method_prediction == row.gold)   # gold=='no-relation' on absent
  #   For certificate: prediction=predict_certificate; abstain when it equals the battery's abstain sentinel
  #     (read cert_info; the certificate's COVERAGE c* = fraction non-abstain). This c* is the TARGET coverage.
  #   For every other method, build (correct[], conf[]) arrays; conf = the method's confidence/abstention
  #     score (dispersion: rec.conf[signal]; verifier: rec.conf_queryside_verifier; etc.).
  #   mask = stats.matched_coverage_mask(conf, target_cov=c*); selacc = stats.selective_accuracy(correct,mask).
  #   confident_wrong_rate(method) = among covered rows, fraction wrong; on absent pools this == fabrications kept.
  #   GAP TEST: certificate vs each method via a DOC-CLUSTERED paired bootstrap (B=10000, SEED): resample
  #     doc_id clusters with replacement, concat their rows, recompute selacc(cert)-selacc(method) and the
  #     confident-wrong-rate reduction; 95% CI + one-sided p. (Implement clustered variant by grouping rows
  #     by doc_id and resampling groups -- small wrapper over stats.paired_bootstrap_gap logic; reuse
  #     stats.clustered_bootstrap_ci pattern for the cluster resample.)
  #   Holm-adjust (stats.holm_bonferroni) the family of certificate-vs-method p-values WITHIN each pool.
  # Build per-venue LEADERBOARDS: rows = methods, cols = {coverage c*, selective_accuracy, confident_wrong_rate,
  #   gap_vs_certificate, ci95(doc-clustered,Holm-adj), reject}. TAG every cell REAL-LLM-READ.

  # === PHASE 6: fraction-caught crux tables ===
  # FACT-A fabrication set per (pool,reader) = ABSENT rows where raw_named is a real relation at high conf.
  # For each method: caught = method does NOT keep it as confident-wrong (abstains OR answers 'no-relation');
  #   fraction_caught = caught / |fabrication set|;  survival = 1 - fraction_caught.
  # Report per (pool x reader x method): fraction_caught, survival, with clustered-bootstrap CI.
  # This is the headline table for objective (b): verifier & self-verify fraction-caught BESIDE the
  # certificate's and the 4 dispersion signals'.

  # === PHASE 7: per-venue CERTIFICATE-NECESSITY verdict ===
  # For each (pool x reader), compare certificate vs queryside_verifier (and vs self-verify) on the ABSENT
  # stratum using BOTH (i) confident-wrong reduction vs commit_argmax and (ii) fraction_caught:
  #   diff = certificate_metric - verifier_metric; doc-clustered bootstrap CI of diff.
  #   if CI(diff) excludes 0 and >0  -> 'CERTIFICATE_NECESSARY' (structural signal beats query-side verifier)
  #   elif verifier_metric >= certificate_metric (CI overlaps or verifier higher) -> 'VERIFIER_MATCHES_OR_BEATS'
  #        (=> structural certificate not strictly needed for this stratum; HONEST NEGATIVE -- the reviewer's
  #        DISCONFIRM is satisfied)
  #   else 'INCONCLUSIVE'.
  # Also emit an overall cross-venue verdict string.

  # === PHASE 8: OUTPUT (exp_gen_sol_out, validated, full/mini/preview) ===
  # method_out.json:
  #   data grouped into datasets ['clutrr_present','clutrr_absent','redocred_present','redocred_absent'],
  #   each example = {input (doc text or truncated ref), output (gold string),
  #     predict_certificate, predict_conf_thresh_verbalized/sc_margin/ptrue/negent, predict_commit_argmax,
  #     predict_queryside_verifier, predict_queryside_selfverify, predict_verifier_as_signal,   # ALL STRINGS
  #     metadata_reader, metadata_is_absent, metadata_stratum, metadata_qsrc, metadata_qtgt, metadata_gold,
  #     metadata_raw_named, metadata_conf_verbalized/sc_margin/ptrue/negent,
  #     metadata_conf_queryside_verifier, metadata_p_related, metadata_conf_queryside_selfverify, metadata_doc_id}
  #   IMPORTANT: every example MUST carry every predict_* as a STRING (validator treats missing/non-string as FAIL).
  #   results block (top-level metadata or results): reproduction_gate, leaderboards (per venue x reader),
  #     fraction_caught_crux_tables, holm_ci_tables, certificate_necessity_verdict (per venue + overall),
  #     cost_ledger = merged client.stats() (cumulative_usd, n_llm_calls, n_cache_hits, n_errors),
  #     honesty_tags (REAL-LLM-READ on all new numbers), config (models, B, seed).
  # Validate with aii-json against exp_gen_sol_out schema; FIX until 0 errors. Generate mini + preview.
  # Run aii-file-size-limit; if full > 100MB, split data files (truncate `input` in mini/preview).
fallback_plan: |-
  PRIMARY RISK -- pool field names differ from expectations (esp. CLUTRR lacks metadata_reader, or the certificate abstain sentinel is encoded differently). MITIGATION: Phase 1 is introspective -- dump the full key set of the first row of each group to logs FIRST, then map fields by trying a ranked list of candidate names (reader: metadata_reader|metadata_model|group-name infix; names: qsrc_name|qsrc; gold: gold|metadata_gold_primitive). If a reader split is genuinely absent in CLUTRR, treat the whole CLUTRR pool as a single reader group and report FACT-A vs the pooled published 0.472/0.483 average; still run the verifier once per row.
  IF THE REPRODUCTION GATE FAILS (recomputed != carried/published): do NOT spend. Emit the gate report with the exact mismatching literals and STOP; the pool is corrupted or the aggregation differs -- surface it. (Tolerance can be relaxed to 1e-2 once, with a logged note, only if the mismatch is pure float-formatting; a structural mismatch is a hard stop.)
  IF BUDGET/RATE-LIMIT trips ($9 hard cap or 429s): llm.py already caches every success and aborts cleanly on BudgetExceeded, returning cached partials. Re-run resumes free from cache. If gemini-3.1-flash-lite is unavailable, FALLBACKS=[google/gemini-3-flash-preview] auto-engages; if deepseek-v3.2 is down, fall back to deepseek-chat-v3 (search via aii-openrouter-llms) -- log the substitution and tag affected rows.
  IF VERIFIER OUTPUTS ARE UNPARSEABLE for some rows: treat parse-fail as related=None -> p_related=0.5 (boundary) so it neither catches nor keeps confidently; count and report n_parse_fail; never silently drop rows.
  IF THE DOC-CLUSTERED paired bootstrap is hard to wire: fall back to the i.i.d. row-resampling stats.paired_bootstrap_gap (already in stats.py) and LABEL CIs as row-level not doc-clustered (slightly anti-conservative -- note it explicitly). Do NOT block the headline on the clustering refinement.
  IF SELF-VERIFY adds little signal or doubles cost near the cap: the query-side VERIFIER is the load-bearing baseline (the reviewer's explicit ask); self-verify is secondary -- run verifier first, then self-verify only if cost < $3 after the verifier pass.
  MINIMUM PUBLISHABLE UNIT: the $0 reproduction gate PASS + the query-side verifier (corrective-gate framing) matched-coverage leaderboard + fraction-caught table + per-venue verdict on BOTH pools, single framing, even if self-verify and the verifier-as-signal sensitivity are dropped.
testing_plan: "1. STARTUP ASSERTS ($0): confirm CLUTRR_POOL, REDOCRED_POOL, SRC_LLM, SRC_STATS exist; `import llm, stats`\
  \ succeeds; OPENROUTER_API_KEY present. Print the key set of one row per group so the field-mapping is verified against\
  \ reality BEFORE coding the loop.\n2. POOL-LOAD SMOKE TEST ($0): after Phase 1, assert per-pool/reader/stratum counts are\
  \ in the expected ballpark (clutrr ~102 present + ~180 absent; redocred ~360 present + ~368 absent, per reader) and that\
  \ every row has non-null gold, raw_named-or-None, all four conf signals, and the carried predict_certificate. Log any nulls.\n\
  3. REPRODUCTION GATE AS THE GO/NO-GO ($0): Phase 2 IS the confirmation signal -- it must reproduce FACT-A (CLUTRR 0.472/0.483,\
  \ Re-DocRED 0.326/0.318) and each file's carried crux_survival_table + certificate leaderboard to tol 5e-3 with client.cost==0.\
  \ Treat a PASS here as the green light to spend; a FAIL aborts before any LLM call.\n4. LLM MICRO-BATCH ($<0.02): run the\
  \ verifier on EXACTLY 8 rows (2 present + 2 absent per pool), one per reader model, and eyeball: RELATED on a true present\
  \ pair, UNRELATED on a cross-component absent pair; JSON parses; cache files written to ./cache; a second run of the same\
  \ 8 reports n_cache_hits==8 and cost delta 0. Confirms prompts, parsing, caching, and reader-matched routing before the\
  \ full ~4000-call batch.\n5. ANALYSIS UNIT TESTS ($0): on a 20-row toy slice, check matched_coverage_mask returns exactly\
  \ ceil(c*xN) covered; selective_accuracy on a hand-built all-correct mask == 1.0; the doc-clustered bootstrap returns a\
  \ CI bracketing the point gap; holm_bonferroni on a known p-family matches hand calc.\n6. SANITY OF THE HEADLINE DIRECTION:\
  \ on absent strata, certificate fraction_caught should be high (it abstains structurally); commit_argmax fraction_caught\
  \ ~0 (keeps fabrications); the 4 dispersion signals should reproduce the published reader-dependence (deepseek dispersion\
  \ catches a majority, gemini verbalized blind). If these qualitative signs are inverted, STOP and re-check field mapping\
  \ before trusting the verifier numbers.\n7. FULL RUN + COST CHECK: run all rows; assert cumulative_usd < $2 (expected <$1)\
  \ and n_errors small; if cost climbs toward $9, BudgetExceeded halts cleanly. \n8. OUTPUT VALIDATION: aii-json validate\
  \ method_out.json against exp_gen_sol_out until 0 errors (every example has all predict_* as STRINGS); generate mini/preview;\
  \ aii-file-size-limit check + split if >100MB. Spot-read 3 example rows + the verdict block for coherence."
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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

--- Dependency 2 ---
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

--- Dependency 3 ---
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

### [2] HUMAN-USER prompt · 2026-06-18 04:10:06 UTC

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

### [3] SKILL-INPUT — aii-json · 2026-06-18 04:25:57 UTC

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

### [4] SYSTEM-USER prompt · 2026-06-18 04:46:11 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_2/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_8/gen_art/gen_art_experiment_2/results/out.json`
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
id: gen_plan_experiment_2_idx3
type: experiment
title: >-
  Query-Side False-Premise Verifier vs the No-Derivation Certificate on Cached CLUTRR + Re-DocRED Kinship Pools (matched coverage,
  $0-gate + <$1 new spend)
summary: >-
  Reviewer-mandated DISCONFIRM test for the closure-certificate paper. Reuse the two EXISTING, fully-cached prediction pools
  (CLUTRR battery art_LeRQRGHJZcdQ @ iter_6/gen_art/gen_art_experiment_1; Re-DocRED kinship battery art_htcr8yOZLCQy @ iter_7/gen_art/gen_art_experiment_1)
  by direct filesystem read, plus their llm.py (sha256-cached, $9-guarded OpenRouter client) and stats.py (matched-coverage
  selective accuracy, paired bootstrap, Holm). A $0 reproduction gate first re-derives FACT-A / crux-survival / certificate
  leaderboard literals from the carried row fields and asserts they match each file's own aggregates AND the published constants
  (CLUTRR 0.472 gemini / 0.483 deepseek; Re-DocRED 0.326 / 0.318). Then the ONLY new spend: for every (query x reader) row
  in both pools, call a query-side false-premise VERIFIER ('are X and Y related by kinship at all?') and a SELF-VERIFICATION
  pass ('is it true that Y is <raw answer> to X?'), reader-matched (gemini-3.1-flash-lite or deepseek-v3.2), sha256-cached,
  est. <$1 / hard cap $9. Analysis sweeps the verifier confidence to MATCH the certificate's coverage on present / absent
  / mixed pools and reports, per venue x reader: matched-coverage selective accuracy & confident-wrong rate of the verifier
  and self-verify vs the certificate vs the four dispersion signals with Holm-adjusted doc-clustered bootstrap CIs; fraction-caught
  crux tables; and a per-venue certificate-necessity verdict (verifier MATCHES/BEATS certificate => structural certificate
  not strictly needed, honest negative; certificate still beats => structural signal necessary). Output method_out.json (exp_gen_sol_out,
  validated, full/mini/preview).
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |
  ############################################################
  # GOAL: add a query-side false-premise VERIFIER + SELF-VERIFY baseline to the two
  # already-powered cached venues, benchmark them against the no-derivation certificate
  # and the 4 dispersion signals at MATCHED COVERAGE, and emit a per-venue verdict.
  # This is REUSE-HEAVY: the certificate / raw / 4-signal predictions ALREADY EXIST in
  # the cached pools; the ONLY new LLM calls are the verifier + self-verify (<$1).
  ############################################################

  # ----- CONSTANTS / PATHS (verify each exists at startup; fail loud if missing) -----
  RUN = '/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop'
  CLUTRR_POOL  = RUN+'/iter_6/gen_art/gen_art_experiment_1/method_out.json'   # art_LeRQRGHJZcdQ
  REDOCRED_POOL= RUN+'/iter_7/gen_art/gen_art_experiment_1/method_out.json'   # art_htcr8yOZLCQy
  SRC_LLM   = RUN+'/iter_7/gen_art/gen_art_experiment_1/llm.py'   # copy VERBATIM into workspace
  SRC_STATS = RUN+'/iter_7/gen_art/gen_art_experiment_1/stats.py' # copy VERBATIM into workspace
  # (optional cross-checks only) dataset deps:
  #   art_HS7-lxhZnU9m CLUTRR gold graphs @ iter_2/gen_art/gen_art_dataset_1
  #   art_NUWTxBVWENIJ Re-DocRED corpus  @ iter_6/gen_art/gen_art_dataset_1
  # Pools are SELF-CONTAINED (each row carries `input` = the story/doc text + entity names + gold),
  # so the dataset deps are needed only as a fallback if a name/doc field is missing.
  PRIMARY_MODEL = 'google/gemini-3.1-flash-lite'
  CROSS_MODEL   = 'deepseek/deepseek-v3.2'
  FALLBACKS     = ['google/gemini-3-flash-preview']
  PUBLISHED_FACT_A = {('clutrr','gemini'):0.472, ('clutrr','deepseek'):0.483,
                      ('redocred','gemini'):0.326, ('redocred','deepseek'):0.318}
  B_BOOT = 10000; SEED = 20260618; ALPHA = 0.05

  # === PHASE 0: workspace setup ===
  # 1. `uv init`; add deps: httpx, loguru, numpy, scipy, jsonschema (mirror iter_7 pyproject.toml).
  # 2. Copy SRC_LLM -> ./llm.py and SRC_STATS -> ./stats.py VERBATIM (do not edit; import them).
  # 3. mkdir ./cache  (NEW workspace cache: verifier prompts differ from battery prompts so keys never collide;
  #    re-runs are free). NEVER write into the source workspaces' cache/ (read-only reuse).
  # 4. Read OPENROUTER_API_KEY from env (same as battery).

  # === PHASE 1: load + normalize both cached pools (introspect, do NOT assume identical fields) ===
  def load_pool(path, pool_name):
      obj = json.load(open(path))
      # exp_sel_data_out: rows live under per-dataset groups (obj['data'][i]['examples']) OR a flat
      # 'examples' list. Walk obj recursively; collect every dict that has BOTH 'input' and a
      # 'metadata_is_absent' (or 'metadata_stratum') key -> that is a row.
      rows = collect_row_dicts(obj)
      norm = []
      for r in rows:
          m = {k[len('metadata_'):]: v for k,v in r.items() if k.startswith('metadata_')}
          reader = (m.get('reader') or m.get('model') or infer_reader_from_group(r)
                    or 'gemini')   # CLUTRR may lack metadata_reader; fall back to group/model tag
          reader = 'deepseek' if 'deepseek' in str(reader).lower() else ('gemini' if 'gemini' in str(reader).lower() else reader)
          qsrc = m.get('qsrc_name') or m.get('qsrc')   # CLUTRR uses qsrc/qtgt (names); Re-DocRED qsrc_name/qtgt_name
          qtgt = m.get('qtgt_name') or m.get('qtgt')
          norm.append(dict(
              pool=pool_name, reader=reader,
              doc_id=r.get('doc_id') or m.get('doc_id') or m.get('title'),
              doc_text=r['input'],
              is_absent=bool(m.get('is_absent', (m.get('stratum','').endswith('absent')))),
              stratum=m.get('stratum'),
              qsrc=qsrc, qtgt=qtgt,
              gold=normalize_gold(r.get('gold') or m.get('gold_primitive')),  # 'no-relation' on absent
              raw_named=m.get('raw_named'),                # raw LLM committed single answer (may be 'no-relation'/None)
              conf=dict(verbalized=m.get('conf_verbalized'), sc_margin=m.get('conf_sc_margin'),
                        ptrue=m.get('conf_ptrue'), negent=m.get('conf_negent')),
              # carried predictions (strings) reused as-is for the certificate + dispersion + commit baselines:
              predict_certificate=r.get('predict_certificate'),
              predict_conf_thresh={s:r.get('predict_conf_thresh_'+s) for s in ['verbalized','sc_margin','ptrue','negent']},
              predict_commit_argmax=r.get('predict_commit_argmax'),
              cert_info=m.get('certificate_info'),
              raw_row=r))
      return norm
  recs = load_pool(CLUTRR_POOL,'clutrr') + load_pool(REDOCRED_POOL,'redocred')
  # Sanity: assert per-pool/reader/stratum counts match objective (clutrr 102 present + 180 absent;
  # redocred 360 present + 368 absent) PER READER; log actuals (handle small drift, don't hard-fail on +-).

  # === PHASE 2: REPRODUCTION GATE ($0 -- must pass before ANY new spend) ===
  # Re-derive the published literals from row fields and compare to (a) each file's OWN carried
  # aggregates (top-level 'leaderboard','crux_survival_table','verdict') and (b) PUBLISHED_FACT_A.
  # A2.1 FACT-A rate: for each (pool,reader): among ABSENT rows, fraction where raw_named is a REAL
  #       relation (not 'no-relation'/None) AND it is a 'high-confidence' commit per the battery's
  #       definition (replicate the battery's threshold: read it from the carried aggregate metadata if
  #       present; else use raw committed-answer present == high-conf by construction at the LLM's
  #       natural no-abstention coverage). assert |recomputed - PUBLISHED_FACT_A[(pool,reader)]| < 5e-3.
  # A2.2 crux-survival / fraction-caught for each dispersion signal at the certificate's coverage:
  #       recompute from conf[*] + raw_named + gold; assert == carried crux_survival_table (0 mismatch, tol 5e-3).
  # A2.3 certificate mixed-pool selective accuracy + confident-wrong reductions: recompute via stats.py
  #       (matched_coverage_mask at certificate coverage) and assert == carried leaderboard (tol 5e-3).
  # A2.4 assert client.cost == 0.0 so far.
  # Emit reproduction_gate = {checks:[{name,recomputed,carried,published,ok}], all_ok:bool}.
  # IF not all_ok: WRITE the gate report into method_out.json and HARD STOP (do not spend) -- a corrupted
  # pool must be surfaced, not built upon.

  # === PHASE 3: build NEW verifier + self-verify LLM items (the only new spend) ===
  VERIFIER_SYS = ('You judge whether two named people are connected by ANY family/kinship relationship '
    '(directly stated OR derivable through a chain of relatives) according ONLY to the given text. '
    'Output ONLY JSON {"related": "RELATED"|"UNRELATED", "confidence": <0..1>}. confidence is your '
    'probability that your RELATED/UNRELATED judgement is correct.')
  SELFVERIFY_SYS = ('You verify a claimed family relationship against a text. Output ONLY JSON '
    '{"verdict": "TRUE"|"FALSE", "confidence": <0..1>}. TRUE iff the claim is actually correct given the text.')
  def model_for(reader): return PRIMARY_MODEL if reader=='gemini' else CROSS_MODEL
  items = []
  for i,rec in enumerate(recs):
      mdl = model_for(rec['reader'])
      # (a) QUERY-SIDE FALSE-PREMISE VERIFIER -- one call per row
      items.append(dict(id=f"ver::{rec['pool']}::{i}", model=mdl, tag='verifier', max_tokens=60, temperature=0.0,
          system=VERIFIER_SYS,
          user=f"Text:\n{rec['doc_text']}\n\nQuestion: Are {rec['qsrc']} and {rec['qtgt']} related by family/kinship at all (directly or via any chain of relatives in the text)? Answer with the JSON object."))
      # (b) SELF-VERIFICATION of the raw committed answer -- skip if raw said no-relation/None (set later)
      if rec['raw_named'] and rec['raw_named'] != 'no-relation':
          items.append(dict(id=f"sv::{rec['pool']}::{i}", model=mdl, tag='selfverify', max_tokens=60, temperature=0.0,
              system=SELFVERIFY_SYS,
              user=f"Text:\n{rec['doc_text']}\n\nClaim: {rec['qtgt']} is {rec['qsrc']}'s {rec['raw_named']}. Is this claim actually true given the text? Answer with the JSON object."))
  # Run with reader-matched models. llm.py keys cache on (model, temp, tag, system, user) so we can run
  # the two models in two batches OR set client.model per item-group. Simplest: group items by model,
  # instantiate OpenRouterClient(api_key, model=mdl, fallbacks=FALLBACKS, cache_dir='./cache',
  #   budget_hard=9.0, budget_soft=2.0, concurrency=12, max_tokens=60, temperature=0.0) per model,
  # results = asyncio.run(client.run_batch(group)).  Merge results by id. Track cumulative cost across
  # both clients; abort cleanly on BudgetExceeded (cached partials still usable).

  # === PHASE 4: parse verifier outputs -> per-row method triples (prediction:str, confidence:float, abstain:bool) ===
  # Reuse llm._load_json-style robust parsing (copy the helper or import from readers if copied).
  def parse_verifier(content): # -> (related:bool|None, conf:float)
      obj=_load_json(content); rel=str(obj.get('related','')).upper() if obj else ''
      conf=clip01(float(obj.get('confidence',0.5))) if obj else 0.5
      return (True if rel=='RELATED' else False if rel=='UNRELATED' else None), conf
  def parse_selfverify(content): obj=_load_json(content); v=str(obj.get('verdict','')).upper() if obj else ''; return (v=='TRUE') if v in('TRUE','FALSE') else None, clip01(float(obj.get('confidence',0.5)) if obj else 0.5)
  for i,rec in enumerate(recs):
      rel, vconf = parse_verifier(results.get(f"ver::{rec['pool']}::{i}",{}).get('content',''))
      # p_related: high => keep as related; used both as classifier decision and as coverage-confidence
      p_related = vconf if rel else (1.0-vconf if rel is False else 0.5)
      # PRIMARY framing = CORRECTIVE GATE (FalseQA-style false-premise detector, mirrors certificate which
      # actively answers 'no-relation' on absent pairs):
      rec['predict_queryside_verifier'] = ('no-relation' if rel is False else (rec['raw_named'] or 'no-relation'))
      rec['conf_queryside_verifier']    = max(p_related, 1.0-p_related)  # distance-from-boundary = abstain ranking
      rec['p_related'] = p_related
      # SENSITIVITY framing = pure ABSTENTION SIGNAL (always commit raw answer, rank by p_related), like the
      # 4 dispersion signals: prediction = raw_named always; confidence = p_related.
      rec['predict_verifier_as_signal'] = rec['raw_named'] or 'no-relation'
      rec['conf_verifier_as_signal']    = p_related
      # SELF-VERIFY: keep raw answer iff verdict TRUE else 'no-relation'; if raw was no-relation/None, keep it.
      if rec['raw_named'] and rec['raw_named']!='no-relation':
          tv, sconf = parse_selfverify(results.get(f"sv::{rec['pool']}::{i}",{}).get('content',''))
          rec['predict_queryside_selfverify'] = (rec['raw_named'] if tv else 'no-relation')
          rec['conf_queryside_selfverify']    = sconf if tv is not None else 0.5
      else:
          rec['predict_queryside_selfverify'] = 'no-relation'; rec['conf_queryside_selfverify']=rec['conf'].get('ptrue') or 0.5

  # === PHASE 5: matched-coverage analysis (reuse stats.py; mirror the battery exactly) ===
  # METHODS = {certificate, conf_verbalized, conf_sc_margin, conf_ptrue, conf_negent,
  #            queryside_verifier, queryside_selfverify, verifier_as_signal(sensitivity), commit_argmax}
  # For each VENUE-POOL in {clutrr_present, clutrr_absent, redocred_present, redocred_absent} AND the two
  # MIXED pools {clutrr_mixed, redocred_mixed}, and for each READER in {gemini, deepseek}:
  #   correct(method,row) = (method_prediction == row.gold)   # gold=='no-relation' on absent
  #   For certificate: prediction=predict_certificate; abstain when it equals the battery's abstain sentinel
  #     (read cert_info; the certificate's COVERAGE c* = fraction non-abstain). This c* is the TARGET coverage.
  #   For every other method, build (correct[], conf[]) arrays; conf = the method's confidence/abstention
  #     score (dispersion: rec.conf[signal]; verifier: rec.conf_queryside_verifier; etc.).
  #   mask = stats.matched_coverage_mask(conf, target_cov=c*); selacc = stats.selective_accuracy(correct,mask).
  #   confident_wrong_rate(method) = among covered rows, fraction wrong; on absent pools this == fabrications kept.
  #   GAP TEST: certificate vs each method via a DOC-CLUSTERED paired bootstrap (B=10000, SEED): resample
  #     doc_id clusters with replacement, concat their rows, recompute selacc(cert)-selacc(method) and the
  #     confident-wrong-rate reduction; 95% CI + one-sided p. (Implement clustered variant by grouping rows
  #     by doc_id and resampling groups -- small wrapper over stats.paired_bootstrap_gap logic; reuse
  #     stats.clustered_bootstrap_ci pattern for the cluster resample.)
  #   Holm-adjust (stats.holm_bonferroni) the family of certificate-vs-method p-values WITHIN each pool.
  # Build per-venue LEADERBOARDS: rows = methods, cols = {coverage c*, selective_accuracy, confident_wrong_rate,
  #   gap_vs_certificate, ci95(doc-clustered,Holm-adj), reject}. TAG every cell REAL-LLM-READ.

  # === PHASE 6: fraction-caught crux tables ===
  # FACT-A fabrication set per (pool,reader) = ABSENT rows where raw_named is a real relation at high conf.
  # For each method: caught = method does NOT keep it as confident-wrong (abstains OR answers 'no-relation');
  #   fraction_caught = caught / |fabrication set|;  survival = 1 - fraction_caught.
  # Report per (pool x reader x method): fraction_caught, survival, with clustered-bootstrap CI.
  # This is the headline table for objective (b): verifier & self-verify fraction-caught BESIDE the
  # certificate's and the 4 dispersion signals'.

  # === PHASE 7: per-venue CERTIFICATE-NECESSITY verdict ===
  # For each (pool x reader), compare certificate vs queryside_verifier (and vs self-verify) on the ABSENT
  # stratum using BOTH (i) confident-wrong reduction vs commit_argmax and (ii) fraction_caught:
  #   diff = certificate_metric - verifier_metric; doc-clustered bootstrap CI of diff.
  #   if CI(diff) excludes 0 and >0  -> 'CERTIFICATE_NECESSARY' (structural signal beats query-side verifier)
  #   elif verifier_metric >= certificate_metric (CI overlaps or verifier higher) -> 'VERIFIER_MATCHES_OR_BEATS'
  #        (=> structural certificate not strictly needed for this stratum; HONEST NEGATIVE -- the reviewer's
  #        DISCONFIRM is satisfied)
  #   else 'INCONCLUSIVE'.
  # Also emit an overall cross-venue verdict string.

  # === PHASE 8: OUTPUT (exp_gen_sol_out, validated, full/mini/preview) ===
  # method_out.json:
  #   data grouped into datasets ['clutrr_present','clutrr_absent','redocred_present','redocred_absent'],
  #   each example = {input (doc text or truncated ref), output (gold string),
  #     predict_certificate, predict_conf_thresh_verbalized/sc_margin/ptrue/negent, predict_commit_argmax,
  #     predict_queryside_verifier, predict_queryside_selfverify, predict_verifier_as_signal,   # ALL STRINGS
  #     metadata_reader, metadata_is_absent, metadata_stratum, metadata_qsrc, metadata_qtgt, metadata_gold,
  #     metadata_raw_named, metadata_conf_verbalized/sc_margin/ptrue/negent,
  #     metadata_conf_queryside_verifier, metadata_p_related, metadata_conf_queryside_selfverify, metadata_doc_id}
  #   IMPORTANT: every example MUST carry every predict_* as a STRING (validator treats missing/non-string as FAIL).
  #   results block (top-level metadata or results): reproduction_gate, leaderboards (per venue x reader),
  #     fraction_caught_crux_tables, holm_ci_tables, certificate_necessity_verdict (per venue + overall),
  #     cost_ledger = merged client.stats() (cumulative_usd, n_llm_calls, n_cache_hits, n_errors),
  #     honesty_tags (REAL-LLM-READ on all new numbers), config (models, B, seed).
  # Validate with aii-json against exp_gen_sol_out schema; FIX until 0 errors. Generate mini + preview.
  # Run aii-file-size-limit; if full > 100MB, split data files (truncate `input` in mini/preview).
fallback_plan: |-
  PRIMARY RISK -- pool field names differ from expectations (esp. CLUTRR lacks metadata_reader, or the certificate abstain sentinel is encoded differently). MITIGATION: Phase 1 is introspective -- dump the full key set of the first row of each group to logs FIRST, then map fields by trying a ranked list of candidate names (reader: metadata_reader|metadata_model|group-name infix; names: qsrc_name|qsrc; gold: gold|metadata_gold_primitive). If a reader split is genuinely absent in CLUTRR, treat the whole CLUTRR pool as a single reader group and report FACT-A vs the pooled published 0.472/0.483 average; still run the verifier once per row.
  IF THE REPRODUCTION GATE FAILS (recomputed != carried/published): do NOT spend. Emit the gate report with the exact mismatching literals and STOP; the pool is corrupted or the aggregation differs -- surface it. (Tolerance can be relaxed to 1e-2 once, with a logged note, only if the mismatch is pure float-formatting; a structural mismatch is a hard stop.)
  IF BUDGET/RATE-LIMIT trips ($9 hard cap or 429s): llm.py already caches every success and aborts cleanly on BudgetExceeded, returning cached partials. Re-run resumes free from cache. If gemini-3.1-flash-lite is unavailable, FALLBACKS=[google/gemini-3-flash-preview] auto-engages; if deepseek-v3.2 is down, fall back to deepseek-chat-v3 (search via aii-openrouter-llms) -- log the substitution and tag affected rows.
  IF VERIFIER OUTPUTS ARE UNPARSEABLE for some rows: treat parse-fail as related=None -> p_related=0.5 (boundary) so it neither catches nor keeps confidently; count and report n_parse_fail; never silently drop rows.
  IF THE DOC-CLUSTERED paired bootstrap is hard to wire: fall back to the i.i.d. row-resampling stats.paired_bootstrap_gap (already in stats.py) and LABEL CIs as row-level not doc-clustered (slightly anti-conservative -- note it explicitly). Do NOT block the headline on the clustering refinement.
  IF SELF-VERIFY adds little signal or doubles cost near the cap: the query-side VERIFIER is the load-bearing baseline (the reviewer's explicit ask); self-verify is secondary -- run verifier first, then self-verify only if cost < $3 after the verifier pass.
  MINIMUM PUBLISHABLE UNIT: the $0 reproduction gate PASS + the query-side verifier (corrective-gate framing) matched-coverage leaderboard + fraction-caught table + per-venue verdict on BOTH pools, single framing, even if self-verify and the verifier-as-signal sensitivity are dropped.
testing_plan: "1. STARTUP ASSERTS ($0): confirm CLUTRR_POOL, REDOCRED_POOL, SRC_LLM, SRC_STATS exist; `import llm, stats`\
  \ succeeds; OPENROUTER_API_KEY present. Print the key set of one row per group so the field-mapping is verified against\
  \ reality BEFORE coding the loop.\n2. POOL-LOAD SMOKE TEST ($0): after Phase 1, assert per-pool/reader/stratum counts are\
  \ in the expected ballpark (clutrr ~102 present + ~180 absent; redocred ~360 present + ~368 absent, per reader) and that\
  \ every row has non-null gold, raw_named-or-None, all four conf signals, and the carried predict_certificate. Log any nulls.\n\
  3. REPRODUCTION GATE AS THE GO/NO-GO ($0): Phase 2 IS the confirmation signal -- it must reproduce FACT-A (CLUTRR 0.472/0.483,\
  \ Re-DocRED 0.326/0.318) and each file's carried crux_survival_table + certificate leaderboard to tol 5e-3 with client.cost==0.\
  \ Treat a PASS here as the green light to spend; a FAIL aborts before any LLM call.\n4. LLM MICRO-BATCH ($<0.02): run the\
  \ verifier on EXACTLY 8 rows (2 present + 2 absent per pool), one per reader model, and eyeball: RELATED on a true present\
  \ pair, UNRELATED on a cross-component absent pair; JSON parses; cache files written to ./cache; a second run of the same\
  \ 8 reports n_cache_hits==8 and cost delta 0. Confirms prompts, parsing, caching, and reader-matched routing before the\
  \ full ~4000-call batch.\n5. ANALYSIS UNIT TESTS ($0): on a 20-row toy slice, check matched_coverage_mask returns exactly\
  \ ceil(c*xN) covered; selective_accuracy on a hand-built all-correct mask == 1.0; the doc-clustered bootstrap returns a\
  \ CI bracketing the point gap; holm_bonferroni on a known p-family matches hand calc.\n6. SANITY OF THE HEADLINE DIRECTION:\
  \ on absent strata, certificate fraction_caught should be high (it abstains structurally); commit_argmax fraction_caught\
  \ ~0 (keeps fabrications); the 4 dispersion signals should reproduce the published reader-dependence (deepseek dispersion\
  \ catches a majority, gemini verbalized blind). If these qualitative signs are inverted, STOP and re-check field mapping\
  \ before trusting the verifier numbers.\n7. FULL RUN + COST CHECK: run all rows; assert cumulative_usd < $2 (expected <$1)\
  \ and n_errors small; if cost climbs toward $9, BudgetExceeded halts cleanly. \n8. OUTPUT VALIDATION: aii-json validate\
  \ method_out.json against exp_gen_sol_out until 0 errors (every example has all predict_* as STRINGS); generate mini/preview;\
  \ aii-file-size-limit check + split if >100MB. Spot-read 3 example rows + the verdict block for coherence."
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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

--- Dependency 2 ---
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

--- Dependency 3 ---
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
