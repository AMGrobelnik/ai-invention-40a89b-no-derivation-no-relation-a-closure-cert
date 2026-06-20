# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 15:38:00 UTC

````
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

<task>
Conduct thorough, unbiased research on the given topic.
Adapt your investigation approach based on the research question and domain.
</task>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<critical_requirements>
1. SOURCE DIVERSITY - Consult MANY sources (10+), not just the first few results
2. AVOID SELECTION BIAS - Actively seek contradicting viewpoints, not just confirming ones
3. TRIANGULATE - Cross-reference claims across multiple independent sources
4. ACKNOWLEDGE UNCERTAINTY - Be honest about confidence levels and limitations
5. SYNTHESIZE - Produce a coherent answer that accounts for conflicting evidence
</critical_requirements>

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

Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<context>
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

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>
</context>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: >-
  Iter-2 Implementation-Decision Dossier: Local-Reader Protocol, Prolog/ASP Discharge, CLUTRR, Stronger Reader, Local-Regime
  Baselines, Novelty Citations
summary: >-
  An executor-ready web-research dossier that resolves every NEW implementation decision the iter-2 experiments need but the
  iter-1 dossier (art_aQ2Rf8rwqteI) did not cover. Six workstreams: (1) the LOCAL-reader span-extraction protocol + disjunctive
  read prompt + 'no shared span' deduction-required trigger; (2) Prolog/ASP emission, SWI-Prolog/clingo discharge from Python,
  and the precise end-to-end CONFIDENT-WRONG (hallucination) metric; (3) CLUTRR access/format + finite kinship composition
  table + absent-relation construction + atomic-extraction P/R gold; (4) a substantially-stronger-but-budget-safe OpenRouter
  reader with a <$10 arithmetic budget; (5) the seven baselines re-specialized to the LOCAL regime with matched single-relation
  abstention signals; (6) 3-4 recent LLM temporal-consistency citations (verified arXiv IDs) plus a crisp one-sentence novelty
  statement. Deliver a decision table, exact IDs/URLs, and a gotchas list. The planner has pre-verified the load-bearing facts
  below; the executor confirms, deepens, and fills gaps.
runpod_compute_profile: cpu_light
question: >-
  What are the concrete, verified implementation specifications for the iter-2 local-reader / end-to-end-Prolog experiments:
  (1) how to extract minimal local event spans and prompt a high-recall sound-disjunction local reader on NarrativeTime/TDDMan,
  and how to flag 'no shared span'; (2) how to encode a closed QCN as SWI-Prolog or clingo ASP, discharge the held-out query
  from Python, and define the confident-wrong hallucination metric; (3) CLUTRR's authoritative source, format, kinship composition
  table, hop metadata, absent-relation construction, and atomic-extraction gold; (4) the cheapest 'substantially stronger'
  OpenRouter reader vs google/gemini-3.1-flash-lite with an arithmetic budget proving two-reader runs stay well under $10
  with caching; (5) the seven local-regime baseline configurations each with a matched single-relation abstention signal;
  (6) the missing recent LLM temporal-consistency citations plus a precise novelty statement (output contract + certificate
  + coding-rate, NOT the algebra)?
research_plan: |-
  # Iter-2 Implementation-Decision Research Plan (web-only, ~3h, cpu_light)

  ## ROLE & OUTPUT
  Produce an executor-ready dossier as `research_out.json` ({answer, sources, follow_up_questions}) PLUS a `research_report.md`. The `answer` must contain, for EACH of the 6 workstreams below: (a) a verified DECISION (what the experiment executor should do), (b) exact IDs/URLs/snippets backing it, and (c) gotchas. End with a single consolidated DECISION TABLE and a GOTCHAS LIST. Tag every external claim with its source URL. This artifact does NOT run code — it resolves decisions via the web so the downstream experiment executor can implement without re-researching.

  ## BUILD ON THE DEPENDENCY (do NOT re-research these)
  Dependency art_aQ2Rf8rwqteI (iter-1 dossier, workspace: runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json) ALREADY pins: NarrativeTime repo (github.com/text-machine-lab/nt, MIT, nt_format JSONL with per-event numeric `time` coordinate + bracket interval model + same-branch get_event_relation); TDDMan 4-col TSV (codes a/b/i/ii/s, join text from TimeBank-Dense; long-distance non-auto-inferable gold); MATRES (start-point convex point algebra, N*~=0 gate control); GQR Allen/point/RCC-8 composition+converse tables (Allen uses < / > tokens; convex-point !=->universal widening rule); Mackworth PC-2 a-closure pseudocode + naive-single-pass contrast (naive==full at length-2, diverges hop>=3/cyclomatic>=1); Renz-Nebel A(n,d,l) synthetic generator; baseline configs at a high level (PoT, self-consistency, LINC, DSR-LM/HtT, ILP-commit Eirew M=5, METRE); corrected citation (>=50-97% multi-relation + ILP-no-F1-gain = Kougia et al. arXiv:2406.11486, 'Analysing zero-shot temporal relation extraction on clinical notes using temporal consistency'); OpenRouter primary google/gemini-2.5-flash-lite GONE -> iter-1 used google/gemini-3.1-flash-lite; <$10 cost-guard + disk-cache strategy; 3-part realism statistic (per-edge TV<=0.10, cross-edge soundness-correlation |drho|<=0.10 via ICC, topology histogram TV<=0.15). FIRST ACTION: open the dependency research_out.json and quote its corpus/algebra/baseline facts so this dossier extends rather than repeats it.

  ## SEED FACTS THE PLANNER ALREADY VERIFIED (executor must CONFIRM + deepen, not rediscover)
  - CLUTRR HuggingFace: dataset `CLUTRR/v1` (https://huggingface.co/datasets/CLUTRR/v1). 6 configs: gen_train23_test2to10, gen_train234_test2to10, rob_train_clean_23_test_all_23, rob_train_sup_23_test_all_23, rob_train_irr_23_test_all_23, rob_train_disc_23_test_all_23. Fields: id, story, query (tuple of 2 names), target (numeric code), target_text, clean_story, proof_state, f_comb, task_name (= 'task_[noise].[clause_length]', e.g. task_1.2 = 2-hop ... task_1.10 = 10-hop), story_edges, edge_types, query_edge. Splits train/validation/test (e.g. gen_train234: 12064/3019/1048).
  - CLUTRR GitHub: github.com/facebookresearch/clutrr. Composition table = `clutrr/store/rules_store.yaml` (~15 kinship composition rules, in-law ambiguities avoided); also `relations_store.yaml`, `question_store.yaml`. Original paper arXiv:1908.06177 (Sinha et al. 2019, EMNLP); workshop arXiv:1811.02959.
  - Prolog from Python: pyswip (github.com/yuce/pyswip, docs pyswip.readthedocs.io) — pip-installable, ctypes-based shared-library embed, needs SWI-Prolog installed on the host; API Prolog().assertz(...) / list(Prolog().query(...)). SWI-Prolog Python FAQ: swi-prolog.org/FAQ/Python.md. ASP alternative: clingo (pip install clingo, CFFI bindings, Control/ground/solve; PyPI 5.8.0) + optional ORM clorm (pip install clorm).
  - Path-of-Thoughts: arXiv:2412.17963 ('Extracting and Following Paths for Robust Relational Reasoning with LLMs'), 3 stages graph-extraction -> path-identification -> per-path reasoning; CLUTRR/StepGame/Chinese-kinship; up to +21.3%; reasons each path INDEPENDENTLY (does not intersect relations across paths) — the exact gap Mode A fills.
  - OpenRouter pricing (June 2026, $/M input | output): google/gemini-2.5-flash 0.30|2.50; google/gemini-3-flash-preview 0.50|3.00; google/gemini-3.5-flash (exists, confirm price); deepseek/deepseek-chat (V3) 0.20|0.80; deepseek/deepseek-v3.2 0.229|0.343; qwen2.5-72b ~1.20. iter-1 reader = google/gemini-3.1-flash-lite (confirm its current price as the 'weak' anchor).
  - Temporal-consistency citations (verified arXiv IDs): Temporal Referential Consistency = arXiv:2510.15513; Counterfactual-Consistency Prompting for Relative Temporal Understanding (Kim & Hwang) = arXiv:2502.11425; Logical Consistency of LLMs in Fact-checking (DNF consistency) = arXiv:2412.16100; Temporally Consistent Factuality Probing = arXiv:2409.14065.
  - Local-reader prior art: 'Are LLMs Good Annotators for Discourse-level Event Relation Extraction?' arXiv:2407.19568 (EMNLP24) — defines Bulk vs Iterative vs Pairwise vs Event-Ranking prompts and same-sentence vs cross-sentence context windows; 'Consistent Discourse-level Temporal Relation Extraction' aclanthology 2025.findings-emnlp.1010. Verbalized-confidence abstention: elicit 0-100 / 'probability your guess is correct', threshold p* swept; known over-confidence (cite 'Know Your Limits' TACL survey + arXiv:2601.07767).

  ---

  ## WORKSTREAM 1 — LOCAL-READER SPAN-EXTRACTION PROTOCOL (headline-critical: defines the regime)
  Goal: a precise recipe the experiment executor can implement to (i) find the minimal local span(s) for each event in a held-out pair, (ii) prompt a span-only reader for a high-recall SOUND disjunction over the algebra base relations + explicit universal option, and (iii) flag 'no shared span' (the deduction-required trigger).
  Steps:
  1. From the iter-1 dossier, restate how NarrativeTime nt_format and TDDMan/TimeBank-Dense store event mention offsets and how text is joined. Then web-verify how to recover SENTENCE boundaries and per-event token offsets from TimeML/.tml source (search: 'TimeBank TimeML EVENT eid token offset sentence segmentation', 'TimeBank-Dense event mention sentence index'). Decide the minimal-span unit: single sentence containing the event mention (default) vs +/-1 sentence window. Document how a pair (e1,e2) maps to local spans: span(e1), span(e2), and for an intermediate event e3 the (often disjoint) span(e3).
  2. Define the 'no shared span' rule precisely: e1 and e2 share a span iff their mentions co-occur within the chosen window (same sentence, or +/-k). 'No shared span' => DEDUCTION-REQUIRED. Confirm this structural proxy is computable WITHOUT the LLM (needed for the T0 gate). Cross-check against arXiv:2407.19568's same-sentence vs cross-sentence split and against Kougia arXiv:2406.11486's locality treatment.
  3. Disjunctive local-read PROMPT TEMPLATE: research best practice for eliciting a high-recall SOUND set of base relations from a single span (not a single committed label). Pull concrete patterns from arXiv:2407.19568 (Pairwise prompt), METRE (multi-label, arXiv:2408.07353), Kougia (multi-relation), and counterfactual-consistency prompting (arXiv:2502.11425). The template must: present ONLY the span; enumerate the algebra's base relations (point: <,=,> widened per convex rule; Allen 13; TDDMan {before,after,simultaneous,includes,is_included}); instruct 'name every relation the text does NOT rule out'; offer an explicit UNIVERSAL/underdetermined option; and elicit per-edge breadth at the pre-registered frontier operating point. Provide 1 worked filled example per corpus.
  4. Deliver: the span-localization algorithm (pseudocode in prose), the 'no shared span' predicate, the prompt template(s), and a note on how the SAME local spans are fed to every baseline (fairness). GOTCHA to flag: NarrativeTime gold is timeline-placed (holistic) — the local-reader probe must read ONLY the span, never the timeline; document how to enforce this.

  ## WORKSTREAM 2 — PROLOG/ASP DISCHARGE + HALLUCINATION METRIC (the end-to-end deliverable)
  Goal: concrete, verified patterns to encode a closed QCN, discharge the held-out query, read back single-relation vs abstention, and define the confident-wrong metric.
  Steps:
  1. SWI-Prolog path: fetch github.com/yuce/pyswip README + pyswip.readthedocs.io + swi-prolog.org/FAQ/Python.md. Confirm: current pyswip version, Python 3.11/3.12 compat, that SWI-Prolog must be apt-installable (`swipl`), and the assertz/query API. Provide a CONCRETE encoding pattern for a QCN: facts `edge(E1,E2,RelSet)` with RelSet as a Prolog list; `compose/3` and `converse/2` facts from the exact algebra table (seeded from the algebra, NEVER the LLM); a query predicate that returns the relation set on the held-out edge after closure. Define readback: |RelSet|==1 -> emit that relation; |RelSet|>1 -> ABSTAIN; |RelSet|==0 -> Mode-B unsound-detection flag.
  2. ASP alternative: fetch pypi.org/project/clingo + potassco.org/clingo + clorm. Provide a clingo encoding sketch (relations as atoms, composition as rules, `#show`), and state the decision rule: pick ONE discharge engine for the experiment. RECOMMEND SWI-Prolog/pyswip as primary (matches the project's stated SWI-Prolog deliverable) with subprocess `swipl -g goal -t halt` as the robust fallback if pyswip's ctypes binding fails to load, and clingo as a secondary ASP option. Verify the subprocess fallback invocation form.
  3. Trace-graph: confirm how to emit which composition entries fired on which paths (for human-auditable replay) — this is bookkeeping the closure produces; document the schema (QCN + fired-compositions + repairs + optional discharged proof).
  4. HALLUCINATION (CONFIDENT-WRONG) METRIC — define precisely: on the deduction-required / absent-relation subset, confident-wrong rate = (# pairs where the method emits a NON-abstained single relation that MISMATCHES gold) / (# evaluable pairs), for the closure pipeline vs a raw LLM forced to a single relation. State it is computed at MATCHED coverage and reported with a paired-bootstrap CI and a PRE-REGISTERED minimum effect. Note the absent-relation case (CLUTRR no-kinship / temporal 'no relation') where gold = 'none' and any committed relation is a hallucination. Survey how Logic-LM (arXiv:2305.12295) / LINC (arXiv:2310.15164) / DSR-LM discharge symbolic programs and report errors, to align our metric with prior practice.

  ## WORKSTREAM 3 — CLUTRR (clean end-to-end venue)
  Goal: confirm access/format, extract the finite kinship composition table, define absent-relation construction and atomic-extraction P/R gold.
  Steps:
  1. Fetch huggingface.co/datasets/CLUTRR/v1 README + a data-viewer sample. Confirm load method (`datasets.load_dataset('CLUTRR/v1', '<config>')` — check whether trust_remote_code / a loading script / parquet is required; this is a known gotcha). Confirm fields (id, story, query, target, target_text, clean_story, proof_state, f_comb, task_name, story_edges, edge_types, query_edge) and the numeric->relation mapping (aunt 0 ... up to ~20). Confirm hop-count is read from task_name's clause_length.
  2. Fetch the EXACT composition table: github.com/facebookresearch/clutrr/blob/main/clutrr/store/rules_store.yaml (and relations_store.yaml). Transcribe the kinship composition rules (e.g. father-of(father) = grandfather) into a machine-usable table the experiment can load as the 'exact kinship composition table'. This table powers the exact-table-vs-LLM-elicited-table ablation. Note: CLUTRR kinship is a FINITE composition table, NOT a full relation algebra (no converse-closure guarantees) — record this scope caveat.
  3. ABSENT-relation (no-kinship) construction for the hallucination demo: research/define how to build pairs with NO valid kinship — e.g. entities not connected in story_edges, or cross-family entity pairs. Confirm whether CLUTRR ships any such negatives or whether they must be constructed; give the construction recipe.
  4. Atomic-extraction P/R gold: define gold atomic facts = the directly-stated edges (from clean_story / story_edges / edge_types); P/R = how well a reader extracts these stated relations before composition. Document the mapping from story_edges/edge_types to gold atomic triples.
  5. Deliver: load snippet, field table, hop metadata, the transcribed composition table location/format, absent-relation recipe, atomic-gold definition. Note PoT (arXiv:2412.17963) and StepGame both use CLUTRR — cite for the end-to-end comparison.

  ## WORKSTREAM 4 — SUBSTANTIALLY STRONGER OPENROUTER READER (budget-safe)
  Goal: pick the cheapest reader clearly stronger than google/gemini-3.1-flash-lite, with an arithmetic budget proving two-reader runs stay well under $10.
  Steps:
  1. Fetch current OpenRouter model/pricing pages for candidates: google/gemini-2.5-flash, google/gemini-3-flash-preview, google/gemini-3.5-flash, deepseek/deepseek-v3.2, deepseek/deepseek-chat, plus one frontier-reasoning option (e.g. a mid Gemini-pro / Claude Haiku-tier / GPT-tier — confirm live IDs+prices). Confirm google/gemini-3.1-flash-lite's current price as the weak anchor.
  2. Evidence of 'substantially stronger': cite benchmark/leaderboard signals on temporal/relational reasoning for the chosen model vs flash-lite (search MMLU/temporal-reasoning/relational benchmarks; OpenRouter model cards). The hypothesis (FIX 5) needs >=2 readers INCLUDING one substantially stronger to test whether the 0.58-0.86 recall ceiling is a weak-model artifact; a reader crossing the 0.85/0.90 gate confirms/falsifies the read-soundness-bottleneck headline.
  3. ARITHMETIC BUDGET: estimate token volume — # held-out deduction-required edges on NarrativeTime + TDDMan (cite iter-1 applicability counts if available; else conservative upper bound, e.g. low-thousands of edges) x avg paths/edge x (span tokens in + disjunction tokens out) x price, for BOTH readers, with the >=5-setting frontier sweep, x a safety factor. Show total << $10 and incorporate the iter-1 disk-cache + hard cost-guard. Confirm which candidates support prompt caching on OpenRouter (caching makes repeated-span reads 60-80% cheaper).
  4. Deliver: a ranked recommendation (primary stronger reader + 1 fallback), live model IDs, per-token prices, the arithmetic, and caching notes. RECOMMENDATION SEED: google/gemini-2.5-flash or google/gemini-3-flash-preview as the stronger reader (cheap, clearly above flash-lite), deepseek/deepseek-v3.2 as a cross-family second; executor confirms availability+price and finalizes.

  ## WORKSTREAM 5 — LOCAL-REGIME BASELINE CONFIGS (matched single-relation coverage)
  Goal: re-specialize the seven baselines to the LOCAL regime (each sees ONLY local spans, like the method), each with a matched abstention signal thresholded to the SAME single-relation coverage object.
  Steps:
  1. For EACH baseline, specify: (a) what input it sees in the local regime, (b) its abstention/confidence signal, (c) how that signal is thresholded to the shared coverage object (single-relation resolution). Baselines: local raw LLM (verbalized confidence, 0-100 elicitation — cite 'Know Your Limits' TACL + arXiv:2601.07767, note over-confidence gotcha); CoT (same, with reasoning); self-consistency (vote margin over k samples); LINC-style multi-formalization vote (arXiv:2310.15164, vote agreement); Path-of-Thoughts (arXiv:2412.17963, path-agreement abstain — CONFIRM each path reasoned INDEPENDENTLY and relations NOT intersected across paths; this is the key contrastive fact); ILP-commit (Eirew et al. arXiv:2502.11114, M=5 generations + ILP uniqueness/symmetry/transitivity — commits a single label, abstention = post-hoc confidence); naive single-pass intersection (intersect compositions arriving at the query node in ONE pass, no fixpoint/no converse seeding — the iteration contrast; coincides with full closure at length-2).
  2. State the matched-coverage protocol explicitly: every method gets its own abstention signal, thresholds swept so all report at the SAME coverage using the SAME coverage object, selective accuracy compared with paired-bootstrap CIs — preventing 'closure' from being confounded with 'closure has a better-calibrated abstain'.
  3. Deliver: a per-baseline config table (input | signal | threshold mechanism | local-regime adaptation | source). Flag any baseline that CANNOT be run web-honestly so the experiment can REMOVE rather than promise it (the hypothesis requires baselines RUN-or-REMOVED).

  ## WORKSTREAM 6 — NOVELTY CITATIONS + STATEMENT
  Goal: bibliographically pin 3-4 recent LLM temporal-consistency works and write the crisp novelty statement.
  Steps:
  1. For each verified ID, fetch the arXiv abstract page and pin: title, authors, year, venue (if any). IDs: arXiv:2510.15513 (Temporal Referential Consistency), arXiv:2502.11425 (Counterfactual-Consistency Prompting, Kim & Hwang), arXiv:2412.16100 (Logical Consistency of LLMs in Fact-checking — DNF consistency), arXiv:2409.14065 (Temporally Consistent Factuality Probing). For each, write ONE sentence on how it differs from our work (they measure/repair consistency under a commit/accuracy objective; none preserve a relation-algebra disjunction, intersect compositions across paths via an exact table, issue a gold-free closure certificate, or abstain).
  2. Write the crisp one-sentence NOVELTY statement: 'New is NOT the algebra or path-consistency (Allen/point/RCC-8, SputLink, CAEVO, Ning 2017, Kougia 2024, Eirew 2025 are established) but (1) the disjunction-preserving, abstain-on-collapse OUTPUT CONTRACT that inverts the F1-maximizing commit objective, (2) the gold-free closure CERTIFICATE, and (3) the redundancy-as-coding-rate inverted-U (currently a simulated-channel property: recall and rho are inputs, not measured outcomes).'
  3. Deliver: a mini-bibliography (BibTeX-ready fields) + the novelty sentence + the differentiation table.

  ---

  ## FINAL DELIVERABLES (in research_out.json answer + research_report.md)
  1. CONSOLIDATED DECISION TABLE: one row per decision (local-span unit; no-shared-span rule; disjunctive prompt; discharge engine = SWI-Prolog/pyswip primary + subprocess fallback + clingo secondary; hallucination metric definition; CLUTRR config + load method + composition-table location; absent-relation recipe; stronger reader = chosen model + price; each baseline's local config; novelty citations) -> DECISION | VALUE | SOURCE URL | CONFIDENCE.
  2. EXACT IDS/URLS list (all arXiv IDs, HF dataset id, GitHub paths, OpenRouter model IDs+prices).
  3. GOTCHAS LIST (>=8): e.g. pyswip needs system SWI-Prolog (apt install swi-prolog); CLUTRR/v1 may need trust_remote_code or be parquet-only — verify before relying on a loading script; verbalized confidence is over-confident (abstention policy must sweep thresholds, not trust raw numbers); NarrativeTime local reader must NEVER see the timeline; CLUTRR kinship is a finite table not a full algebra (no converse guarantees); absent-relation pairs likely must be CONSTRUCTED (not shipped); OpenRouter model IDs/prices drift — confirm live + have a fallback; caching support varies by model; matched-coverage thresholds must use the SAME coverage object for every baseline; PoT must be confirmed to NOT intersect across paths.
  4. follow_up_questions: any decision the executor could not fully resolve via web (e.g. exact NarrativeTime held-out edge count for the budget — defer to T0; whether a specific stronger model is live at run time).

  ## SUCCESS = every iter-2 experiment decision is answered with a verified value + source, so the experiment executor implements without re-researching. Web-only; no code, downloads, or computation.
explanation: >-
  The iter-2 hypothesis pivots hard from iter-1: it relocates the real-text value claim to the LOCAL-reader regime (closure-over-local-reads
  vs {local raw LLM, PoT, voting}), promotes an END-TO-END Prolog-discharged hallucination-reduction number to a co-headline,
  adds CLUTRR as the clean end-to-end venue, demands a substantially stronger second reader, requires the seven baselines
  RUN-or-REMOVED, and must cite recent LLM temporal-consistency work. The iter-1 dossier (art_aQ2Rf8rwqteI) covered corpus
  formats, algebra tables, closure pseudocode, the synthetic generator, and high-level baselines — but NONE of these six new
  decisions. Without resolving them up front, the experiment executor would burn its 3h budget rediscovering CLUTRR's format,
  fighting pyswip's system dependency, guessing a stronger reader's price, or designing the local-reader prompt from scratch
  — and would risk an unfair baseline comparison or an undefined hallucination metric that invalidates the headline. This
  research artifact front-loads every such decision into a verified, sourced dossier (the planner has already confirmed the
  load-bearing facts: CLUTRR/v1 + facebookresearch/clutrr rules_store.yaml, pyswip+clingo, Path-of-Thoughts arXiv:2412.17963
  independence, OpenRouter prices, and four temporal-consistency arXiv IDs), so downstream experiment design and execution
  are de-risked and reproducible. As a RESEARCH artifact it is pure information gathering — exactly the executor scope — and
  its findings directly gate the Tier-1 local-reader, end-to-end, and baseline experiments.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
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
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-17 15:38:00 UTC

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

### [3] SKILL-INPUT — aii-web-tools · 2026-06-17 15:38:10 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````
