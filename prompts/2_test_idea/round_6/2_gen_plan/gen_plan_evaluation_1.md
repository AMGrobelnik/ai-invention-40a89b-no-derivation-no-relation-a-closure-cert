# gen_plan_evaluation_1 — test_idea

> Phase: `invention_loop` · round 6 · `gen_plan`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_evaluation_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 00:28:01 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: EVALUATION

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed
</artifact_type_info>

<available_resources>
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

<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budget>

The evaluation executor has 3h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

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

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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

<hypothesis>
kind: hypothesis
title: >-
  A Training-Free, Gold-Free, Per-Edge ABSTAIN-ON-COLLAPSE CERTIFICATE for the Deduction Sub-Module of Text-to-Logic Pipelines:
  Reducing Confident Hallucination Where Confidence Thresholds Structurally Cannot (cross-path qualitative-algebra coding
  is synthetic-channel-only — a bounded negative on both a-priori-gated real venues)
hypothesis: |-
  ONE THESIS, STATED FIRST AND ALONE (reviewer clarity + novelty MAJORs: the prior draft still carried two co-headline theses; collapse to a SINGLE load-bearing advance). The contribution of this paper is a TRAINING-FREE, GOLD-FREE, PER-EDGE ABSTAIN-ON-COLLAPSE CERTIFICATE over LLM-extracted relational facts that inverts the F1-maximizing COMMIT contract — keep the LLM as a high-recall disjunctive reader, compose ONLY through exact relation-algebra tables, EMIT a singleton, ABSTAIN on a residual disjunction, and FLAG an unsound read when iterated closure collapses to empty — whose DISTINCTIVE, NON-INCREMENTAL value is that it reduces CONFIDENT-WRONG hallucination exactly where a confidence-thresholded neural abstainer structurally CANNOT: on no-derivation / absent-relation queries (where the LLM hallucinates a relation at HIGH confidence, so no confidence threshold abstains on it, yet the certificate abstains because no derivation path exists) and on sound-violating reads (Mode-B collapse). One sentence a reader can repeat: 'A structural, label-free certificate that catches confident relational hallucinations that confidence cannot see.' Everything else in the paper — the cross-path coding thesis, the algebra-richness scaling law, the inherited-vs-novel decomposition, the redundancy inverted-U, the zero-FP theorem — is DEMOTED to a single supporting subsection or a compact appendix half-page, NOT presented as co-equal contributions (reviewer clarity MINOR). Keep evidence-class tags in TABLE COLUMNS, not inline hedging.

    WHY THIS REVISION (the iter-5 evidence). The decisive iter-5 spatial RCC-8 experiment (art_i53dBKgGY3Ig) CONFIRMED, rather than overturned, the prior round's central concern: the signature novel mechanism (cross-path intersection as an error-correcting code over LLM reads, with an inverted-U coding rate) is synthetic-channel-only on BOTH a-priori-gated real venues — temporal Allen (reads near-universe) and spatial RCC-8 (gold is a containment tree) — and the most novel REAL-text findings in the paper are NEGATIVES about that mechanism. The reviewer's verdict is unambiguous and we accept it: do NOT re-run RCC-8 (the negative is clean and needs no LLM); the issue is contribution MAGNITUDE, not a missing experiment. We therefore stop trying to rescue the cross-path mechanism on real text and re-center the ENTIRE paper on the certificate, whose strongest, confidence-threshold-beating evidence becomes load-bearing.

    OPERATIONAL CEILING + VENUE, FOREGROUNDED IN TITLE/ABSTRACT/INTRO (reviewer scope MINOR). (a) The technical core is the DEDUCTION SUB-MODULE: atomic extraction is MEASURED not improved (CLUTRR P/R/F1 ~= 0.536/0.532/0.534); (b) OpenCyc/upper-ontology grounding is OUT OF SCOPE; (c) in EVERY venue the composition table is HAND-SUPPLIED (Allen/point/RCC-8 published tables; CLUTRR rules_store.yaml); (d) real-text utility is structurally EXTRACTION-LIMITED (~0.53 atomic recall => ~19% Mode-A coverage on dense prose; the certificate is only WEAKLY protective on natural temporal text); (e) no BENCHMARK document reaches the goal's ~3000-char target (CLUTRR <=871; spatial 130-1338), and the one ~3000-char study is constructed (temporal docs BRACKET-selected around 3000 with none in [2500,3500]; kinship docs CONCATENATED from disjoint-entity CLUTRR sub-stories with cross-story pairs absent-by-construction) — label both explicitly. RE-TARGET the primary venue from ACL Knowledge Extraction (a poor fit, since the contribution is deduction/consistency not extraction) to a NeSy / temporal-and-qualitative-reasoning track, and SAY SO.

    ----- CLAIM 1 (THE SINGLE HEADLINE, CONFIRMED): THE CERTIFICATE, AND ITS CONFIDENCE-THRESHOLD-BEATING VALUE ON CONFIDENT HALLUCINATIONS. TAG: REAL-LLM-READ + THEOREM. -----
    The portable, demonstrated-at-power result. (1a) The certificate runs end-to-end on real (templated) CLUTRR (art_0a7i481ZRwS1): a real LLM reads atomic kinship triples span-locally, a forward-union least-fixpoint engine recovers the held-out query, and the contract EMITs/ABSTAINs/FLAGs. Multi-hop selective accuracy holds 0.75-1.00 through 10-hop chains (raw collapses hop-3 0.444 -> hop-10 0.0; PoT 0.357 -> 0.20); traces ACTUALLY EXECUTED in SWI-Prolog 9.0.4 (40/40 run, 40/40 match the Python engine, 39/40 gold). HONESTY, FOREGROUNDED: the matched-coverage selective-accuracy win (Mode-A 0.886 vs PoT 0.457, gap +0.429, Holm p_adj=0.0015) is the INHERITED neuro-symbolic premise (compose with the exact table, not the LLM): on rich Allen the +0.676 system gap DECOMPOSES (art_D0cHQUJ8kY75) into +0.673 inherited + only +0.0025 novel-on-selective-accuracy, so the SELECTIVE-ACCURACY win is NOT the paper's distinctive contribution and must be labeled the standard NeSy premise wherever it appears.
    (1b) THE LOAD-BEARING, DISTINCTIVE EVIDENCE (reviewer novelty MAJOR — 'make the certificate's strongest real-text evidence load-bearing'): the ABSENT-RELATION hallucination reduction, which exploits a capability gap confidence thresholds CANNOT close. On 180 CLUTRR absent-relation queries (disconnected components, truthful answer 'no relation'), the raw LLM is confidently wrong 47.2% of the time and the certificate 2.8% (reduction 0.444, CI [0.317,0.583], clears the pre-registered 0.20 bar); on a MIXED present/absent pool (n=282) the certificate answers 26.6% @ confident-wrong 4.6% vs raw 58.9% @ 44.0%. The KEY mechanistic claim, made explicit: these hallucinations are HIGH-confidence, so a confidence-thresholded neural abstainer keeps them — only a structural 'no-derivation => abstain' signal catches them. (1c) THE GOLD-READ ORACLE (Mode-A 1.00 @ coverage 0.951) proves the symbolic closure is NOT the bottleneck — the neural read is (atomic recall ~0.53). The genuinely portable NOVELTY is the CERTIFICATE itself (training-free, per-edge, gold-free abstain-on-collapse), separated cleanly from both the inherited composition premise and the synthetic-only coding-rate thesis.

    ----- CLAIM 2 (THE SINGLE DECISIVE OPEN EXPERIMENT for iter-6): SHOW THE CERTIFICATE BEATS A CONFIDENCE-THRESHOLDED NEURAL ABSTAINER, NOT JUST AN ALWAYS-ANSWER COMMIT. TAG: REAL-LLM-READ. -----
    This is the reviewer's primary action (novelty MAJOR + evidence MAJOR) and the paper's path above the bar. Across the paper the certificate has so far been benchmarked mostly against ALWAYS-ANSWER baselines (commit-the-argmax; raw forced-single), so 'certificate confident-wrong = 0.000/0.028' largely reflects ABSTENTION, not a demonstrated edge over a FAIR neural abstainer. The honest spatial RCC-8 Q2 analysis already showed that on DEDUCTION queries a confidence-thresholded raw-abstain baseline is COMPETITIVE (confident-wrong 0.035 @ coverage 0.285; method 0.022 but answers only ~15%, and at matched coverage raw is NOT less accurate). So the certificate's distinctive advantage is NOT on ordinary deduction queries — it is on the NO-DERIVATION / absent-relation regime and on Mode-B sound-violation catches. iter-6 must PROVE this with a fair baseline:
      * STEP A (load-bearing, cheaply collectable): add a CONFIDENCE-THRESHOLDED RAW-ABSTAIN baseline (verbalized-confidence AND self-consistency vote-margin, thresholded to MATCHED coverage) to EVERY certificate comparison already run — the CLUTRR absent-relation/mixed pool, the spatial RCC-8 deduction pool, and the fuzzy-unification table. PRE-REGISTERED prediction: on the ABSENT-relation / no-derivation stratum the certificate's confident-wrong rate is strictly below the confidence-thresholded baseline at matched coverage (because absent-relation hallucinations are high-confidence and structurally invisible to confidence signals), with a doc-clustered paired-bootstrap CI excluding 0; on the ordinary DEDUCTION stratum the certificate TIES or LOSES to the confidence-thresholded baseline (already observed on spatial), which we report as an honest scope boundary that SHARPENS where the certificate's value lives.
      * STEP B (contribution-raising, the harder ask): demonstrate the certificate's confident-wrong advantage over the confidence-thresholded baseline on AT LEAST ONE additional GENUINELY NATURAL corpus (not templated CLUTRR, not symbolic-id SpaRP), focused on the no-derivation regime where the gap should appear — e.g. a natural narrative kinship/genealogy source, natural spatial-containment descriptions with disconnected objects, or absent/unanswerable relational queries over natural news/biography text with a hand-supplied relational table. Report atomic recall and per-edge breadth so the result is attributable. FORK (both publishable): IF the certificate beats the confidence-thresholded baseline on a natural corpus' no-derivation stratum -> the certificate is a genuine, non-incremental capability and the paper clears the bar; IF NO clean natural corpus with genuine absent pairs + recoverable gold can be sourced, SCOPE HONESTLY to CLUTRR (templated) + semi-natural spatial + the confidence-thresholded-baseline result, and present the certificate as a deduction-sub-module contribution validated on templated/semi-natural venues, repositioned to NeSy.

    ----- CLAIM 3 (SUPPORTING NEGATIVE, ONE SUBSECTION ONLY — no longer a co-headline; reviewer rigor MAJOR): CROSS-PATH CODING IS SYNTHETIC-CHANNEL-ONLY. TAG: REAL-LLM-READ + GOLD-ONLY-GATE + SYNTHETIC-CONTROL. -----
    The signature cross-path-intersection mechanism (multi-path redundancy as an error-correcting code over LLM reads) remains established at power ONLY on synthetic channels, and FAILED on BOTH a-priori-gated real venues for OPPOSITE reasons: temporal Allen reads are near-universe (event-local underdetermined-rate 0.87; intersection/best-single/naive all resolve 0/125; stronger deepseek-v3.2 even MORE conservative at 0.99 — not a weak-model artifact), and spatial RCC-8 reads informatively (breadth 2.1/8, underdetermined 0.036) but its gold is a containment TREE (all 228 deduction queries have exactly one edge-disjoint path; the cardinal subgraph already composes to a singleton on the best single path), so the corpus's 27.4% 'tight-multipath' flag was purely STRUCTURAL and the genuine redundancy is CROSS-algebra, not intersectable in one calculus (art_i53dBKgGY3Ig overturns the dataset card's GENERAL-band optimism, a $0 gold-structural negative). Synthetic positive controls satisfying both conditions confirm the mechanism is real (Allen recall_95: selective accuracy 0.976 vs best-single 0.717, gain +0.259, CI [0.177,0.349]; RCC-8: 0.890 vs 0.797). CRITICAL TEMPERING (reviewer rigor MAJOR — do NOT call this a 'law' or 'sharp/general characterization'): present it as 'two conditions — informative sub-universal reads AND same-algebra structural redundancy — that were each INDEPENDENTLY VIOLATED in the two real venues we could a-priori-gate, with synthetic controls confirming the mechanism when both hold' — an EXPLANATORY ACCOUNT of two negatives, NOT a predictive law (the conditions are close to definitionally necessary, so their joint absence across two venues is not a validated characterization). Also temper the synthetic mechanism's value: even where it works the realized cross-path COVERAGE bite is tiny (+0.024 over best-single-path, CI includes 0); the gain is precision-of-commitments (+0.259 selective accuracy), not coverage. This entire claim is ONE honestly-bounded subsection, explicitly subordinate to the certificate.

    ----- CLAIM 4 (GENUINE FUZZY UNIFICATION, SUPPORTING; reporting corrected per reviewer evidence MAJOR). TAG: REAL-LLM-READ. -----
    The genuine fuzzy-unification experiment (art_I22c-J7-OcXl) correctly retired the iter-4 circular Mode-P (memorized-table recall at confidence EXACTLY 1.0): rendering a known relation with a VAGUE preposition (near/touching/around) or an INFORMAL kinship term (guardian/family elder/relative by marriage) yields CALIBRATED sub-1.0 disjunctions (fraction-at-1.0 = 0.00 in both settings vs Mode-P's 1.00; per-candidate ECE 0.142 spatial / 0.111 kinship), and the certificate drives confident-wrong to 0.000 at coverage 0.535/0.314. REPORTING FIX (reviewer evidence MAJOR): the current 0.000-vs-commit-argmax-0.364/0.216 comparison is against an ALWAYS-ANSWER baseline and so mostly reflects abstention. ADD a CONFIDENCE-THRESHOLDED RAW-ABSTAIN baseline at MATCHED coverage (0.535 spatial / 0.314 kinship), exactly as in the spatial Q2 section, and report whether the certificate beats it. Because the fuzzy reads are calibrated, a confidence-thresholded top-1 baseline may achieve low confident-wrong too; the certificate's DISTINCTIVE edge is catching SOUND-VIOLATING reads via Mode-B collapse (e.g. 'around' -> {NTPPi,TPPi} drops gold EC => abstain instead of committing wrong DC) — but this is THINLY evidenced (~5 caught reads on spatial, 0 on kinship, where 0 unsound reads make the catch untested). FRAME the contribution honestly as 'auditable, faithful abstention that ADDITIONALLY catches sound-violations confidence cannot,' QUANTIFYING the small number of catches rather than letting '0.000 vs 0.364' carry the section. This stays a supporting subsection under the certificate headline.

    ----- CLAIM 5 (OPERATIONAL CASE STUDY, SUPPORTING; honestly labeled). TAG: REAL-LLM-READ. -----
    The first end-to-end ~3000-char run (art_WQoePKrpsTPo) is an OPERATIONAL CASE STUDY (per-document operating points, not a powered test): temporal arm = 5 NarrativeTime news articles BRACKET-selected around 3000 chars (NONE in [2500,3500]; mean 3050, range 2197-4293 — say so), kinship arm = 3 docs CONCATENATED from disjoint-entity CLUTRR sub-stories (cross-story pairs absent-by-construction => trivially abstained — say so). 95 Prolog programs discharged AND executed in swipl 9.0.4; hallucination reduction vs whole-document raw 0.27-0.60 (mean 0.45) at Mode-A coverage 0-0.33 vs raw 1.0; atomic recall ~0.49 isolated as the binding ceiling. LABEL the documents bracket-selected (temporal) and concatenation-constructed (kinship) so 'operational ~3000-char' is not read as natural 3000-char professional documents. Keep this as a short demonstration that the pipeline is operational and that extraction (not closure) is the ceiling.

    ----- CLAIM 6 (MECHANISM ANALYSIS / APPENDIX, DEMOTED). TAG: REAL-LLM-READ-ON-SYNTHETIC + SYNTHETIC-CHANNEL + THEOREM. -----
    Compress the following into a COMPACT half-page or APPENDIX (reviewer clarity MINOR), labeled inherited/synthetic/textbook: (6a) ALGEBRA-RICHNESS SCALING with real LLM reads on synthetic NL (point(3) +0.043 -> RCC-8(8) +0.448 -> Allen(13) +0.676; the INHERITED table-vs-LLM-composition effect at recall ~1.0, RCC-8/Allen sound lower bounds); (6b) the REDUNDANCY INVERTED-U on a realism-matched channel (Page p ~= 5e-4 corrected from the paper's mis-stated 1e-13; peak K* = 2,4,7,10,16 for recall 0.5->0.95; silent-wrong 0.006->0.146 bounded by (1-r) and (1-J(E))), with the small-bite caveat (intersection adds only +0.024 coverage); (6c) the ZERO-FP soundness THEOREM (all-sound contributing edges => gold in Mode-A output with probability exactly 1.0; verified on 100,296 networks) — a textbook PC invariant, tagged THEOREM, whose empirical content is the conditionality (silent-wrong rises as recall falls); recall and rho are INPUTS so it characterizes, not predicts a real-text operating point. None of this competes with the certificate headline.

    ----- CLAIM 7 (NATURAL TEMPORAL TEXT: certificate only WEAKLY protective; corrected statistics carried). TAG: REAL-LLM-READ. -----
    On natural temporal text the raw LLM OUT-ACCURACIES Mode-A at matched coverage (0.699 vs 0.575, gap -0.124), and among the ~19% Mode-A commits to it is CONFIDENT-WRONG 42.5% (48/113), ALL silent-wrong-narrowing (gold omitted from a contributing read => confident wrong singleton with NO collapse, UNDETECTABLE at ~0.85 recall). The corrected FIXED-operating-point H1 CI INCLUDES ZERO (vs PoT +0.027 [-0.088,0.140] p=0.33; vs SC +0.035 [-0.061,0.135] p=0.26; neither clears Holm); the earlier published CONFIRM was a bootstrap artifact. State plainly: the natural-text temporal comparative advantage is MARGINAL and not robustly significant; the certificate's value there is the gold-free certificate + abstention-as-an-OPTION, bounded by read recall (end-to-end confident-wrong reduction 0.61->0.425 = 0.185, CI [0.087,0.280], read alongside Mode-A's 0.188 coverage vs raw 1.0). Read-soundness is the binding, CORPUS-SPECIFIC constraint (NarrativeTime stronger reader 0.932, CI [0.888,0.967] straddles the 0.90 gate; TDDMan stays below). This is supporting, not a headline.

    ----- METHOD CORE (unchanged in substance; re-scoped). -----
    MODE A (SOUND NARROWING / no-derivation abstention, PRIMARY, READ-SOUNDNESS-CONDITIONAL zero-FP). The local reader emits per span a high-recall sub-universal disjunction (with an explicit universal/underdetermined option); composing+intersecting through the EXACT table either resolves a singleton (EMIT), leaves a disjunction (ABSTAIN), or finds NO derivation path (ABSTAIN 'no relation' — the load-bearing absent-relation behavior). zero-FP survives PC incompleteness but is CONDITIONAL on every contributing read being sound. The cross-path-INTERSECTION variant is SYNTHETIC-ONLY-at-power (CLAIM 3); CLUTRR uses a union-fixpoint, not intersection.
    MODE B (DETECTION/REPAIR, SECONDARY). An empty closure certifies that some read is UNSOUND — a gold-free, zero-FP DETECTION flag (conditional on recall) — carrying the SILENT-WRONG-NARROWING dual (an unsound set OMITTING gold drives a confident WRONG singleton with no collapse; the undetectable failure behind CLAIM 7's 42.5%). The handful of Mode-B catches in the fuzzy setting are the certificate's distinctive edge over a fair neural abstainer (CLAIM 4). Reiter-style minimal-hitting-set repair is future work.
    BASELINES (reviewer evidence MAJOR): every certificate comparison must include a CONFIDENCE-THRESHOLDED RAW-ABSTAIN baseline (verbalized confidence + self-consistency vote-margin) thresholded to MATCHED coverage, alongside always-answer commit-the-argmax/raw-forced-single, PoT, and self-consistency. The certificate's claim is specifically that it beats the confidence-thresholded abstainer on the NO-DERIVATION/absent stratum.
    GENERALITY, TEMPERED. EXACT only on the convex point algebra (PC complete); Allen IA and RCC-8 are SOUND LOWER BOUNDS; CLUTRR kinship is a finite UNION composition table, NOT a relation algebra, NOT a cross-path-intersection venue.

    ----- HONESTY COMMITMENTS. -----
    (1) TAG every number THEOREM / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / REAL-LLM-READ / REAL-LLM-READ-ON-SYNTHETIC in TABLE COLUMNS. (2) Do NOT call CLUTRR natural — it is TEMPLATED (<=871 chars, gold surface forms, hand-supplied table); the only natural text is the temporal corpora, where the contribution is marginal. (3) The certificate's selective-accuracy CLUTRR win is the INHERITED NeSy premise (+0.673 inherited / +0.0025 novel); the DISTINCTIVE certificate value is the absent-relation hallucination reduction over a CONFIDENCE-THRESHOLDED baseline, not over always-answer commit. (4) Cross-path coding is SYNTHETIC-CHANNEL-ONLY — a single bounded negative subsection, framed as an explanatory account of two gated-venue negatives, NOT a 'law' or co-headline. (5) zero-FP is READ-SOUNDNESS-CONDITIONAL. (6) The fuzzy-unification certificate edge over a fair neural abstainer rests on ~5 Mode-B catches — quantify honestly; the kinship catch is untested (0 unsound reads). (7) Report every hallucination number WITH coverage/abstention. (8) SWI-Prolog execution reported truthfully (40/40 engine, 39/40 gold; 95 programs discharged in the operational study). (9) DEDUCTION SUB-MODULE only — OpenCyc grounding, atomic re-extraction, general fuzzy unification OUT OF SCOPE; extraction-limited (~0.53 recall => ~19% coverage); no benchmark doc reaches ~3000 chars and the ~3000-char study is bracket-selected/concatenation-constructed. (10) RE-TARGET venue to NeSy / temporal-and-qualitative-reasoning, not ACL Knowledge Extraction. (11) Include one worked Mode-A no-derivation abstention + one Mode-B collapse + a compact notation/metric table.

    SUCCESS / DISCONFIRM (re-centered on the certificate). CONFIRM if: the certificate reduces confident-wrong on the no-derivation/absent-relation stratum strictly below a CONFIDENCE-THRESHOLDED neural abstainer at matched coverage on >=1 real/realistic venue (CLUTRR absent pool already strongly suggestive; iter-6 adds the fair baseline + ideally one natural corpus), with a doc-clustered paired-bootstrap CI excluding 0, AND a SWI-Prolog-executed pipeline reports atomic P/R, multi-hop accuracy, trace-graphs, and abstention beside every hallucination number (MET on CLUTRR vs always-answer; the fair-baseline version is the iter-6 test). DISCONFIRM / SCOPE-BOUNDARY (each publishable): the certificate does NOT beat a confidence-thresholded abstainer on the no-derivation stratum of ANY real venue (=> the certificate is the inherited NeSy premise plus abstention with no distinctive edge — an honest negative); cross-path intersection never beats single-path on any real multi-path stratum at power (already observed on both gated venues => coding mechanism honestly synthetic-only).
motivation: >-
  Faithful multi-hop relational reasoning over short professional text -- temporal ordering of events in news, kinship in
  narratives, containment/region relations in descriptions -- is where LLM hallucination is most damaging and where a text-to-logic
  pipeline most needs to fuse explicit document facts with implicit composition knowledge while staying auditable. The umbrella
  pipeline reads text into FOL/Prolog predicates, types entities against an upper ontology, and answers queries with a reasoner;
  the WEAK LINK is the composition/deduction step. Existing systems handle composition unsatisfyingly: humans hand-craft composition
  rules (the kinship rules behind CLUTRR), which do not scale; the LLM composes freely, locally fluent but globally inconsistent,
  producing silent errors that solver-crash feedback (Logic-LM) and answer voting (LINC) cannot see; or paths are reasoned
  in ISOLATION (LAMBADA, Path-of-Thoughts), which deliberately avoids the global check and so cannot tighten a disjunctive
  query by intersecting evidence from multiple paths nor detect contradictions arriving at the same pair from two paths. A
  cluster of negative/commit-contract results sharpens the opportunity: Knez & Sun (2024, arXiv:2406.11486) show zero-shot
  LLMs assign MORE THAN ONE temporal relation to a pair for >=50% (up to 97%) of pairs and violate transitivity, then enforce
  consistency with ILP and find it DOES NOT improve F1; and -- decisively up to date -- a 2025 global zero-shot temporal-graph
  generator (arXiv:2502.11114, EMNLP 2025) STILL enforces uniqueness/symmetry/transitivity by ILP, committing to a single
  label per pair, preserving no disjunction, issuing no certificate, and offering no abstention. We read this lineage as evidence
  that consistency enforcement under the F1-maximizing COMMIT contract is the wrong objective; the LLM's native multi-relation
  output is not noise to be collapsed but a SOUND DISJUNCTION to be PRESERVED and NARROWED, and the right objective is faithfulness-by-abstention,
  not extraction F1. The qualitative-reasoning community has had exact, commodity-cheap path-consistency algorithms over relation
  algebras (Allen 1983; Renz & Nebel; GQR, SparQ) for forty years, but they assume a clean hand-given table and have never
  been coupled to an LLM reading relations off natural language. We are NOT the first to run closure over machine-extracted
  temporal relations (SputLink densifies TimeBank; CAEVO does global temporal inference via cascaded sieves; Ning et al.'s
  ILP enforces transitivity) -- but ALL COMMIT to a single consistent labeling to maximize F1, preserving no disjunction,
  certifying no reading error, offering no abstention. Our contribution is the OPPOSITE output contract: keep the LLM's job
  as high-recall disjunctive READING, use cross-path INTERSECTION as a zero-FP faithfulness operation (Mode A) and closure
  COLLAPSE as a gold-free reading-error certificate (Mode B), and optimize faithfulness via a risk-coverage objective. Three
  ideas make the transfer a genuine contribution rather than a port. FIRST, because Allen/point/RCC-8 tables are EXACT ground
  truth, cross-path intersection of SOUND sets can only move toward gold -- a calibration-free, zero-FP narrowing that needs
  no over-commitment and no labels, and multi-path redundancy becomes an ERROR-CORRECTING CODE over LLM extractions. SECOND,
  the coding-theory lens predicts an OPTIMAL RATE: narrowing stays zero-FP only while all contributing edges are sound and
  that JOINT probability (measured EMPIRICALLY as J(E), not assumed independent) decays with redundancy, so net benefit is
  an INVERTED-U whose peak we predict from measured recall and the measured cross-edge error correlation and shift with a
  recall-floor gate. THIRD, the objective inverts F1 -- we preserve disjunctive uncertainty and ABSTAIN, trading coverage
  for faithfulness, and we measure the ACTIONABLE yield (intersection-to-correct-singleton at matched coverage) and the DOWNSTREAM
  hallucination-rate reduction, not whether a set merely shrank. The decisive realism move this iteration is choosing the
  corpus that can ACTUALLY host the claim: MATRES annotates only same/adjacent-sentence pairs, so its deduction-required envelope
  is empty BY CONSTRUCTION; the headline must live on a DENSE, direct-human-gold corpus (NarrativeTime, full TLink coverage,
  human-timeline gold) and be corroborated where gold is provably non-closure-derived (TDDMan long-distance manual pairs).
  If it works, this is a general, training-free recipe for trustworthy relational deduction over text with quantified, certificate-backed
  hallucination reduction and replayable trace-graphs; if it fails (intersection rarely resolves correct singletons because
  real sets are near-universal; the redundancy peak sits at trivially low redundancy; recall failures dominate the joint-soundness
  bound; or even the dense corpus's deduction-required multi-path-with-bite slice is below the pre-registered applicability
  number), each is itself a publishable scope boundary on repairing LLM-read relational knowledge.
assumptions:
- >-
  ARM-SCOPED CLAIMS + DENSE-CORPUS RELOCATION (resolves the prior contradiction AND the MATRES-locality problem). The real-text
  narrowing/hallucination win is claimed on a DENSE direct-human-gold corpus's deduction-required multi-path subset (NarrativeTime
  CO-PRIMARY; TDDMan non-circularity corroboration), NOT on MATRES, which is EXPECTED TO FAIL the deduction-required gate
  by construction (same/adjacent-sentence annotation -> all gold local). Mode A beats path-isolated Path-of-Thoughts and answer-voting;
  it TIES naive single-pass intersection on length-2 queries; FULL ITERATED closure beats naive ONLY where >=3-edge/cyclic
  structure exists -- now demonstrated on synthetic AND, where T0 finds a usable real-text stratum, on real text.
- >-
  CORPUS ALGEBRA & NON-CIRCULARITY CHARACTERIZED A-PRIORI FOR ALL CORPORA (before any LLM spend). NarrativeTime gold = HUMAN
  TIMELINE placement (manual, full TLink coverage, IAA alpha ~0.68), restrictable to START-POINTS -> CONVEX POINT ALGEBRA
  where PC is COMPLETE and the table exact (full-interval Allen scored as a lower-bound detector); its non-local gold is human-holistic,
  NOT algorithmic-closure output, so closure recovery over independently-read edges is non-circular -- quantified by the LOCALLY-JUSTIFIABLE
  vs PURELY-TIMELINE-IMPLIED fraction. TDDMan gold = direct human annotation of long-distance pairs explicitly NOT auto-inferable
  -> a structurally non-circular anchor whose win moots the timeline-circularity worry. Mode A's zero-FP soundness SURVIVES
  PC incompleteness (intersection of sound sets is always sound), so the mechanism is not lost where completeness fails.
- >-
  REDUNDANCY IS DOUBLE-EDGED, AUDITED ON EMPIRICAL JOINT SOUNDNESS (no independence assumption). Mode A's zero-FP narrowing
  holds only when ALL contributing edges are sound. We MEASURE the empirical joint soundness J(E) and report the within-document
  cross-edge reading-error correlation rho. Net Mode-A gain is an INVERTED-U in redundancy at fixed recall, cost term 1 -
  J(E), peak located using empirical J(E); positive rho pushes the peak outward. A flat/non-monotone curve is the predicted
  recall x redundancy interaction, not a disconfirmation.
- >-
  A-PRIORI ENVELOPE GATE EXTENDED TO ALL CORPORA + CONCRETE APPLICABILITY THRESHOLD. From each gold graph alone (zero LLM
  spend) we count N* (deduction-required AND >=2-path AND bite-after-widening AND singleton-resolving) AND the >=3-edge/cyclic
  prevalence (the real-text iteration envelope), with a paired-bootstrap power calc, for NarrativeTime, TDDMan AND MATRES;
  we report widening-induced bite loss; and we pre-register the applicability-envelope threshold as a NUMBER (deduction-required
  multi-path-with-bite fraction >=10% of evaluable held-out edges = 'general mechanism'; 5-10% = 'useful module'; <5% = 'niche
  safety-net'). The headline is never contingent on an unmeasured quantity.
- >-
  ACTIONABLE YIELD = SINGLETON-RESOLUTION-TO-CORRECT + DOWNSTREAM HALLUCINATION REDUCTION, AND RECALL-AND-RHO-MATCHED READER-AGNOSTICITY.
  The matched-coverage win and the hallucination-rate drop are both driven by intersection-to-correct-SINGLETON (strict-tightening
  reported separately, stated non-load-bearing); the coverage axis (single-relation resolution) is applied IDENTICALLY to
  closure and every baseline. The gain is attributable to the ALGEBRA: swapping the disjunctive edge-reader preserves the
  gain when each alternative reader is tuned to MATCHED per-edge recall AND its rho is reported (conditioned on rho if it
  differs materially), so reader-specific error correlation cannot confound the conclusion.
investigation_approach: |-
  TIERING (pre-committed; T0 then Tier-1 must COMPLETE before Tier-2; a fully-executed T0+Tier-1 with a thin Tier-2 is the acceptable minimum publishable unit). T0 -- A-PRIORI ENVELOPE GATE FOR ALL CORPORA (zero LLM spend): from each gold graph compute N* (deduction-required AND >=2-path AND bite-after-widening AND singleton-resolving), the >=3-edge/cyclic prevalence, the widening-induced bite loss, and a paired-bootstrap power calc, for NarrativeTime, TDDMan AND MATRES; for NarrativeTime also compute the locally-justifiable vs purely-timeline-implied split (non-circularity audit, structural proxy only). Decide hosting via the pre-registered applicability NUMBER; the expected MATRES N* ~ 0 vs NarrativeTime/TDDMan N* >> 0 is reported as gate validation. TIER-1 (headline-critical, on the dense co-primary): (T1) the RECALL-BITE FRONTIER map + pre-registered go/no-go; (T2) the real-text Mode-A comparison vs Path-of-Thoughts and self-consistency at MATCHED COVERAGE with paired-bootstrap CIs, stratified by deduction-required vs directly-readable; (T2b) the END-TO-END HALLUCINATION-REDUCTION on the deduction-required/absent-relation subset vs a raw LLM, with a PRE-REGISTERED minimum effect size; (T3) the SYNTHETIC long-hop/cyclic redundancy-scaling DECOMPOSITION separating Mode-A BENEFIT from silent-narrowing COST, locating the inverted-U peak, conditioning the zero-FP audit on EMPIRICAL J(E), PLUS a coarse REAL-TEXT decomposition anchor binned by contributing-edge count; (T4) the isolating ablations -- closure ON/OFF table-held-fixed, Mode-A-only, and NAIVE-INTERSECTION vs FULL ITERATED closure with hop/cyclomatic stratification ON BOTH synthetic AND the dense corpus's real >=3-edge/cyclic stratum (the iteration claim). TIER-2 (runs only after Tier-1): TDDMan non-circularity replication, RCC-8 second algebra, CLUTRR elicited-table ablation + absent-relation end-to-end demo, TimeBank-Dense (framed noisy-read-vs-clean-read), Mode-B repair quality, the METRE-style alternative-reader ablation, exploratory semiring variant.

  MULTIPLICITY POLICY (pre-registered; inoculates against a garden-of-forking-paths objection). CONFIRMATORY FAMILY (Holm-Bonferroni / hierarchical gatekeeping across the family; report ADJUSTED CIs): (H1) real-text Mode-A selective-accuracy gap vs PoT & voting; (H2) end-to-end hallucination-rate reduction vs raw LLM; (H3) full-minus-naive iteration gap growing with hop/cyclomatic; (H4) the single redundancy inverted-U disconfirmer. H1 and H2 are the gateway tests; H3/H4 are tested only if a gateway clears. EVERYTHING ELSE -- per-stratum splits, per-bin curves, reader-agnosticity, Mode-B repair, RCC-8/CLUTRR/TB-Dense, the real-text iteration stratum (corroborative) -- is EXPLORATORY, reported with nominal CIs and labelled as such.

  EMPIRICAL-J(E) ATTRIBUTION RULE (stated ONCE here): a reliability-slope offset that DISAPPEARS when the predictor is switched from the independence product r^E to empirical J(E) is the independence approximation failing (NOT a disconfirmation); an offset that PERSISTS under empirical J(E) is a genuine soundness failure. ESCALATION LADDER (stated ONCE here): the dense direct-human-gold CO-PRIMARY is NarrativeTime if its T0 N* clears the applicability number; TDDMan corroborates and supplies a non-circularity-clean (and harder) arm; MATRES is the gate-validation control; if NO real corpus clears the number even after these, the synthetic arm becomes the headline and real text is demoted to an honestly-scoped niche-safety-net boundary -- but T0 makes that decision before LLM spend.

  COMPACT LOGICAL STRUCTURE (claim -> precondition -> metric -> baseline -> CI test). [H1 REAL-TEXT NARROWING] Mode-A singleton-resolution-to-correct > PoT & self-consistency (ties naive-intersection) -> precondition: dense-corpus deduction-required multi-path-with-bite subset with N* powering the CI (from T0) -> metric: selective accuracy at matched coverage -> baselines: PoT (path-agreement abstain), self-consistency (vote margin) -> paired-bootstrap adjusted CI on the gap, separated from 0. [H2 HALLUCINATION REDUCTION] closure pipeline confident-wrong rate < raw-LLM on the absent-relation subset -> precondition: same subset -> metric: confident-wrong (non-abstained gold-mismatch) rate -> baseline: raw LLM forced to a single relation -> paired-bootstrap adjusted CI meeting the pre-registered minimum effect. [H3 ITERATION] full closure > naive-intersection, gap grows with hop/cyclomatic -> precondition: paths longer than 2 / cycles present (synthetic; real >=3-edge/cyclic stratum) -> metric: selective-accuracy gap vs hop-count bin -> baseline: naive single-pass intersection -> per-bin adjusted CI + monotone-trend test. [H4 REDUNDANCY OPTIMUM] net gain inverted-U with located peak; peak increases with recall; gate shifts it -> precondition: >=4 fixed per-edge-recall arms + estimation-precision pre-reg -> metric: separate benefit and cost curves vs redundancy (synthetic + coarse real anchor) -> peak-detection meeting the >=1-bin shift bar. [C2 PATH-CONSISTENCY] closure ON > OFF, table held FIXED -> paired bootstrap (exploratory). [C3 ZERO-FP AUDIT] realized fraction-still-contains-gold tracks EMPIRICAL J(E), slope ~1 (exploratory). [C5 READER-AGNOSTIC] gain persists under swapped reader at matched recall AND reported rho (exploratory). [C6 MODE-B] zero-FP DETECTION; repair toward gold (exploratory).

  PILOT AS A FRONTIER MAP (after T0, before main runs). On synthetic and real edges, SWEEP a prompt-elicited breadth knob across >=5 settings from 'name THE relation' to 'name the maximal SOUND set the text does not exclude.' At each setting MEASURE: per-edge RECALL = P(gold in emitted set); breadth distribution; over-commitment vs under-specification rate; raw closure-collapse rate; strict-tightening AND singleton-resolution-to-correct yields; local-only-reader accuracy defining the deduction-required fraction; and the within-document cross-edge reading-error correlation rho. PLOT the RECALL-BITE FRONTIER as a primary deliverable and pre-register go/no-go (a region clearing a recall gate AND non-trivial singleton-resolution-to-correct) BEFORE any main run. PRE-REGISTER the EXTENDED REALISM-MATCHING STATISTIC for the synthetic NL-realization: total-variation distance between real and synthetic per-edge error-type distributions PLUS a cross-edge error-CORRELATION (rho) match term PLUS a redundancy/path-topology match (contributing-edge-count and cycle-structure histograms), thresholds FIXED before generating the redundancy curve.

  PIPELINE (four stages). (1) NEURAL READING -- prompt the LLM (via OpenRouter, cheap model, short docs, caching; well under $10) to map each surface relation phrase onto a SOUND DISJUNCTION of canonical base relations at the pre-registered frontier operating point; for the NarrativeTime point-algebra arm restrict emitted vocabulary to CONVEX point relations on start-points (widen non-convex {<,>} to VAGUE) so PC stays COMPLETE, and MEASURE the bite lost. (2) ALGEBRA -- use the EXACT published composition table (Allen 13-relation, point algebra, RCC-8; the convex table for the coarse interval label sets); seed converses/identity from the algebra, never from an LLM. (3) SYMBOLIC CLOSURE -- build a QCN (nodes=events/entities, edges=relation SETS; query/held-out edge starts universal), run path-consistency to a FIXPOINT. Three instrumented variants: FULL iterated PC; NAIVE single-pass intersection at the query node (no fixpoint, no converse seeding); closure-OFF (table fixed). MODE A narrows by cross-path intersection and emits an answer ONLY when the query resolves to a single relation (coverage axis), else ABSTAINS. MODE B (Tier-2): an empty collapse CERTIFIES a reading error; compute a minimal Reiter-style hitting-set/MaxSAT repair preferring lowest-confidence edges, recording the diagnosis and flagging possible mislocalization. (4) AUDIT -- emit the QCN, which compositions fired on which paths, and repairs as a TRACE-GRAPH, optionally discharged in SWI-Prolog/ASP from the closed table for a replayable proof (connective tissue to the umbrella pipeline's auditability + quantified-hallucination-reduction requirements).

  DATASETS. DENSE REAL-TEXT CO-PRIMARY: NarrativeTime / TimeBankNT (Rogers et al., LREC-COLING 2024; arXiv:1908.11443) -- timeline-based FULL-coverage human re-annotation of TimeBank-Dense (news), IAA alpha ~0.68; start-point restriction -> convex point algebra (PC COMPLETE), full-interval arm as lower-bound detector; non-local gold is HUMAN-timeline-placed (non-circular vs algorithmic PC). NON-CIRCULARITY ANCHOR: TDDMan (Naik et al., TDDiscourse 2019; aclanthology W19-5929) -- MANUAL long-distance (>1-sentence-apart) pairs that 'cannot be inferred automatically from existing annotations'; relation set {before, after, simultaneous, includes, is_included}, mutually exclusive (no VAGUE), coarse interval algebra; cleanest non-circularity, used to replicate the narrowing win where gold is provably not a closure artifact. GATE-VALIDATION CONTROL: MATRES (Ning, Wu & Roth 2018) -- same/adjacent-sentence annotation, expected N* ~ 0 on the deduction-required gate, demonstrating the gate discriminates. SYNTHETIC PRIMARY (clean ground truth, controlled redundancy): a Renz-Nebel-style random consistent Allen/point QCN generator GUARANTEEING redundant paths/cycles and sweeping redundancy/density/hop-count INDEPENDENTLY; the NL-realization protocol is VALIDATED to clear the EXTENDED realism statistic; the redundancy DECOMPOSITION is reported at >=4 FIXED per-edge-recall levels with >=500 networks per cell. SECOND ALGEBRA: RCC-8 synthetic. ELICITED-TABLE VENUE: CLUTRR kinship (LLM-elicited table vs gold) doubling as an end-to-end hallucination-reduction-on-ABSENT-relation demo. TimeBank-Dense as a Tier-2 noisy-read-vs-clean-read arm; RuleTaker an out-of-scope propositional contrast.

  KEY ABLATIONS: (i) closure/intersection ON vs OFF with the table HELD FIXED; (ii) NAIVE single-pass vs FULL iterated closure with hop/cyclomatic stratification (synthetic + real); (iii) Mode A ONLY vs Mode A+B; (iv) disjunction OFF (force singletons); (v) exact-table vs LLM-elicited-table (kinship); (vi) recall-floor gate ON vs OFF; (vii) ALTERNATIVE EDGE-READER (METRE-style multi-label head + a second LLM into the SAME closure pipeline -- recall-AND-rho-matched). BASELINES, EACH WITH A MATCHED ABSTENTION SIGNAL thresholded to the SAME coverage object: raw LLM (verbalized confidence), CoT, self-consistency (vote margin), LINC-style multi-formalization vote, DSR-LM-style induced-rule Prolog (no closure), Path-of-Thoughts (PRIMARY real-text baseline; path-agreement abstain), NAIVE single-pass intersection (iteration contrast), a TempRel-style COMMIT baseline, and a soft-unification neural theorem prover.

  METRICS, per-regime and STRATIFIED: (1) SINGLETON-RESOLUTION-TO-CORRECT yield + risk-coverage/selective accuracy AT MATCHED COVERAGE (HEADLINE H1) with paired-bootstrap adjusted CIs, reported alongside strict-tightening yield (stated non-load-bearing); (2) END-TO-END hallucination-rate reduction vs raw LLM on the deduction-required/absent-relation subset (HEADLINE H2) with a pre-registered minimum effect; (3) empirical zero-FP audit CONDITIONED on EMPIRICAL J(E) (reliability curve slope ~1; rho reported); (4) REDUNDANCY DECOMPOSITION (benefit vs silent-narrowing cost, located peak, gate shift) on SYNTHETIC + coarse REAL anchor; (5) full-minus-naive gap vs hop/cyclomatic on SYNTHETIC and the real >=3-edge/cyclic stratum; (6) Mode-B detection (lower bound on Allen IA/RCC-8, exact on the point-algebra arm) + repair quality; (7) reader-agnostic closure delta at matched recall and reported rho; (8) APPLICABILITY ENVELOPE -- relation-composable, multi-path-with-bite, deduction-required, AND >=3-edge/cyclic fractions per corpus (N* up front), scored against the pre-registered NUMBER; (9) atomic extraction P/R as a HELD-FIXED control; (10) the non-circularity audit (locally-justifiable vs purely-timeline-implied fraction on NarrativeTime). Closure and repair run in milliseconds per network on a laptop.
success_criteria: |-
  THREE ARM-SCOPED HEADLINE PREDICTIONS (stated before all qualifiers; the confirmatory family H1-H4 is Holm-Bonferroni-adjusted, H1/H2 are gateways). CONFIRM lines: (REAL-TEXT) On the dense co-primary's deduction-required multi-path-with-bite subset at the pre-registered frontier operating point, Mode A achieves strictly higher SELECTIVE ACCURACY AT MATCHED COVERAGE than Path-of-Thoughts AND self-consistency (H1), AND cuts the CONFIDENT-WRONG (hallucination) rate versus a raw LLM on the same absent-relation pairs by at least the pre-registered minimum effect (H2) -- both adjusted-CI-separated from zero, driven by singleton-resolution-to-correct; Mode A is PREDICTED TO TIE naive single-pass intersection on the length-2 stratum and that tie is reported as confirmation, not failure. (ITERATION) FULL ITERATED closure beats NAIVE single-pass intersection with the gap GROWING in hop-count/cyclomatic number (and ~0 on length-2) on synthetic QCNs AND, where T0 found a usable real >=3-edge/cyclic stratum, on real text (H3). (REDUNDANCY) Net Mode-A gain is an INVERTED-U whose peak increases with recall and shifts outward under the recall-floor gate, at the pre-registered estimation precision (>=4 recall levels, >=500 networks/cell, >=1-bin minimum-detectable peak shift, peak bin CI-above both neighbors) (H4). Additionally CONFIRMS if: T0 reports N* clearing the applicability NUMBER on >=1 real corpus (NarrativeTime preferred, TDDMan corroborating) so the headline is genuine deduction not re-reading; the empirical zero-FP audit tracks J(E) (slope ~1, rho reported, slope-offset correctly attributed); the coarse real-text redundancy anchor matches the synthetic inverted-U sign; disjunction-ON beats commit-to-singleton; and the gain is reader-agnostic at matched recall+rho. DISCONFIRM lines: (REAL-TEXT) NEITHER a singleton-resolution advantage over PoT/voting NOR a hallucination-rate drop vs raw LLM exists on the deduction-required multi-path-with-bite subset even when sound sets are sub-universal and bite exists; (ITERATION) the full-minus-naive gap is ~0 even on multi-hop/cyclic queries (the win is 'any intersection,' not iteration); (REDUNDANCY) the SINGLE genuine disconfirmer -- the ABSENCE of any net-positive redundancy region beating BOTH best-single-path and naive-intersection (a flat/turned-over curve ALONE is NOT a disconfirmation); or T0 shows NO corpus clears the applicability NUMBER (then honestly scoped to synthetic + niche-safety-net).

  PRE-REGISTERED FAILURE MODES (each a publishable scope boundary): [NEAR-UNIVERSAL UNDER-SPECIFICATION | precondition: sets effectively universal | bound: Mode A inert, intersection cannot resolve singletons | the ONLY under-specification outcome that disconfirms Mode A]. [SILENT WRONG NARROWING | precondition: a contributing set OMITS gold (unsound) | bound: rate <= (1-recall) per-edge and (1 - J(E)) per-network | suppressed by the recall-floor gate, which also shifts the redundancy peak]. [CONSISTENT-BUT-WRONG ELICITED TABLE | precondition: LLM supplies the composition table | bound: quantified vs gold in kinship only | shown NOT to arise in exact-table settings]. [INVISIBLE SINGLE-CHAIN HALLUCINATION | precondition: confident self-consistent single chain | bound: closure cannot see it | scopes Mode B to multi-path collapse only]. [TINY/CIRCULAR ENVELOPE | precondition: N* below the applicability NUMBER even on the dense corpus, or gold purely-timeline-implied with no non-circular replication on TDDMan | bound: contribution scoped to synthetic + niche safety-net | decided a-priori by T0, not after spend]. Throughout, 'zero false-positive' is stated separately for Mode A (intersected set still contains gold under JOINT-sound inputs, audited against EMPIRICAL J(E)) and Mode B (DETECTION only); the closure-detectable hallucination rate is a LOWER BOUND because PC is incomplete for Allen IA/RCC-8 (complete only on the NarrativeTime start-point convex-point-algebra arm). Atomic extraction P/R must remain comparable to baselines, the per-corpus fractions (including a-priori N* and the >=3-edge/cyclic prevalence) must be reported up front, and trace-graphs must be judged human-auditable.
related_works:
- >-
  NarrativeTime / TimeBankNT (Rogers et al., LREC-COLING 2024; arXiv:1908.11443): the FIRST timeline-based annotation achieving
  FULL coverage of all possible TLinks, a human re-annotation of TimeBank-Dense (news) with IAA Krippendorff alpha ~0.68 and
  significantly higher density, plus tools converting to TimeML. We USE it as the dense real-text CO-PRIMARY because (unlike
  MATRES) it has direct human gold for NON-LOCAL pairs and (unlike TimeBank-Dense) its dense relations are HUMAN-timeline-backed
  rather than SputLink-inferred. Difference from our work: NarrativeTime is a DATASET/annotation scheme producing a single
  consistent labeling for extraction evaluation; it neither preserves LLM disjunction, intersects compositions across paths,
  certifies reading errors, nor abstains. We restrict its start-points to the convex point algebra (PC COMPLETE) and audit
  the locally-justifiable vs purely-timeline-implied fraction to neutralise residual circularity.
- >-
  TDDiscourse / TDDMan (Naik, Breitfeller et al., 2019; aclanthology W19-5929): the first dataset of DISCOURSE-LEVEL temporal
  links between events MORE THAN ONE SENTENCE APART, MANUALLY annotating global pairs that 'cannot be inferred automatically
  from existing annotations,' doubling TimeBank-Dense's links; relation set {before, after, simultaneous, includes, is_included},
  mutually exclusive, no VAGUE. We USE TDDMan as the NON-CIRCULARITY anchor: its gold is provably NOT the output of the closure
  algorithm we test, so a Mode-A narrowing win there cannot be a closure artifact. Difference: TDDiscourse is a benchmark
  for committed single-label discourse-level extraction; it preserves no disjunction, performs no cross-path intersection,
  issues no certificate, and does not abstain.
- >-
  Global Zero-shot Temporal Graph Generation (2025, arXiv:2502.11114; EMNLP 2025 main): prompts an LLM to generate a whole
  temporal graph, aggregates M=5 generations, then enforces uniqueness/symmetry/transitivity with ILP using Allen's laws.
  MOST RECENT directly-relevant prior art. Difference: it COMMITS to a single deterministic label per pair, preserves NO disjunction,
  intersects NO compositions across paths, issues NO gold-free certificate, and does NOT abstain -- the same F1-maximizing
  COMMIT contract we invert.
- >-
  Knez & Sun 2024 (arXiv:2406.11486): zero-shot LLMs assign MORE THAN ONE relation to a pair for >=50% (up to 97%) of pairs
  and violate uniqueness/transitivity; the authors ENFORCE consistency with ILP and find it DOES NOT improve F1. Difference:
  it enforces consistency under the F1-maximizing COMMIT contract (which it shows fails); no closure-as-CERTIFICATE, no preserved
  disjunction, no abstention/risk-coverage, no cross-path zero-FP narrowing. We read its negative result as motivation to
  PRESERVE and NARROW the disjunction.
- >-
  Hu, Huang & Feng 2024 (arXiv:2408.07353, METRE): a TRAINED multi-LABEL classifier inferring the possibility of each temporal
  relation independently, treating VAGUE as >1 possible relation, on TB-Dense/MATRES/UDS-T. Difference: METRE is trained to
  maximise F1 (not recall-oriented soundness); it carries no set through an EXACT composition table across MULTIPLE paths,
  performs no cross-path intersection, issues no certificate, does not abstain. We use it as an ALTERNATIVE EDGE-READER into
  the SAME closure pipeline (Tier-2) at MATCHED per-edge recall with reported rho, to show the cross-path-closure gain is
  reader-AGNOSTIC -- explicitly handling that its F1 training may make its soundness differ from the LLM reader.
- >-
  Temporal-relation extraction with ILP global inference (Ning, Feng & Roth 2017, EMNLP; CogCompTime) and SputLink (Verhagen
  2004/2005) / CAEVO (Chambers et al. 2014, TACL): trained/sieve extractors that enforce transitivity to output a single globally-consistent
  labeling; SputLink computes closure to DENSIFY TimeBank. Differences: all COMMIT to one relation per pair for F1, use learned/approximate
  inference, and (for SputLink) produce the very non-adjacent gold whose circularity we AVOID by using NarrativeTime's direct
  human-timeline gold and TDDMan's manual non-auto-inferable gold; we PRESERVE disjunction, NARROW by exact-table cross-path
  intersection, and ABSTAIN.
- >-
  Path-of-Thoughts (2024, arXiv:2412.17963): graph extraction -> path identification -> per-path reasoning, beating SOTA by
  up to 21.3% on StepGame/CLUTRR. PRIMARY real-text baseline. Difference (verified): it calls an external reasoner 'for each
  reasoning path' INDEPENDENTLY and does NOT intersect relations arriving at the same pair from multiple paths nor detect
  cross-path contradictions; when paths disagree it outputs multiple relations but does NOT abstain. This is EXACTLY the gap
  Mode A fills; PoT is given a matched abstention signal (path-agreement).
- >-
  DSR-LM / 'LLMs can Learn Rules' (Yang et al. 2023, arXiv:2305.03742; Zhu et al. 2023, arXiv:2310.07064): INDUCE weighted/symbolic
  composition rules to fit task accuracy. Difference: rule induction optimises data fit and gives a point answer; we enforce
  the EXACT ALGEBRAIC LAWS (converse, associativity, disjointness) necessary for soundness independent of training data, and
  use closure for zero-FP narrowing, detection, repair, and abstention. Our table-held-fixed closure ON-vs-OFF ablation isolates
  path-consistency from 'a fixed consistent table exists' (DSR-LM's contribution).
- >-
  Logic-LM (Pan et al. 2023, arXiv:2305.12295) and LINC (Olausson et al. 2023, arXiv:2310.15164): Logic-LM self-refines using
  solver crash/unsat messages; LINC majority-votes the answers of multiple formalisations. Difference: Logic-LM reacts only
  to crashes and has no positive global INVARIANT over relational knowledge; LINC's answer-level voting cannot see that individually-popular
  composition steps are JOINTLY inconsistent, nor tighten a disjunctive query by intersection. Algebraic closure is a global
  necessary condition both lack; we give LINC vote-agreement as a matched abstention signal.
- >-
  LAMBADA (Kazemi et al. 2023, arXiv:2212.13894) and path-isolation reasoning: backward chaining / per-path reasoning that
  manages inconsistency by COMPOSITIONAL ISOLATION rather than global enforcement. Difference: we INTERSECT across paths via
  closure, which both tightens disjunctions (Mode A) and detects contradictions (Mode B); isolation can return mutually inconsistent
  answers and cannot resolve disjunctive uncertainty.
- >-
  Logically Consistent Language Models / LOCO-LMs (Calanzone, Teso & Vergari 2024, arXiv:2409.13724; ICLR 2025): a TRAINING-TIME
  neuro-symbolic loss fine-tuning an LLM to be consistent with propositional facts/rules. Difference: it is training-time
  and PROPOSITIONAL; we are training-free at INFERENCE time and enforce multi-hop COMPOSITION closure over a RELATION ALGEBRA
  read off text, producing per-instance certificates, abstention, and trace-graphs.
- >-
  Generic LLM selective prediction / abstention, incl. temporal QA (SelectLLM 2025; abstention surveys 2025; 'When Silence
  Is Golden: Can LLMs Learn to Abstain in Temporal QA' arXiv:2602.04755): reduce error by abstaining via learned uncertainty,
  vote margins, or RL with abstention-aware rewards. Difference: abstention is driven by GENERIC confidence/uncertainty signals
  or learned at the QA-answer level; there is no algebraic consistency certificate, no per-edge reading-error localisation,
  no preserved relation-algebra disjunction, and no closure-based narrowing. Ours abstains precisely because deductive closure
  leaves the query a disjunction -- a structural, training-free, per-edge certificate.
- >-
  Classical qualitative reasoners and tractability theory: GQR, SparQ, Allen (1983), Mackworth (1977, path-consistency PC-1/PC-2
  ITERATED to a fixpoint -- distinguishing full closure from a single intersection pass, exploited in our naive-intersection
  ablation), Renz & Nebel (random network model A(n,d,l)), Vilain & Kautz 1986 (point algebra), Nebel & Burckert 1995 (ORD-Horn,
  JACM 42(1)). So PC is COMPLETE for the convex point algebra and ORD-Horn yet SOUND-BUT-INCOMPLETE for full Allen IA / RCC-8.
  Difference: these assume a clean human-given table on already-formal data; none read the algebra off NL via an LLM, certify
  reading errors, narrow by cross-path intersection of LLM disjunctions, model an EMPIRICALLY-audited recall-bounded redundancy
  OPTIMUM, or optimise risk-coverage.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer from Qualitative Spatial-Temporal Reasoning and Tarski's relation algebras
  -- Allen's interval algebra, RCC-8, the convex point algebra, composition tables, and the path-consistency / algebraic-closure
  constraint-propagation algorithms (GQR/SparQ; Mackworth's iterated PC), plus the tractability theory (point-algebra and
  ORD-Horn completeness vs full-Allen NP-completeness) -- imported into LLM-based relational reasoning and hallucination control,
  with Reiter's 1980s model-based diagnosis (minimal hitting sets of conflict sets) for localising which extracted atom to
  retract. The Level-1 framing is CODING THEORY: an exact composition table turns multi-path redundancy in a document into
  an error-correcting code over LLM extractions -- redundant constraining paths let closure DETECT and CORRECT mis-reads with
  no external labels, as parity checks detect bit errors. The coding-theory 'optimal rate' sharpening (net benefit is an INVERTED-U
  because narrowing stays zero-FP only while every contributing symbol is sound) is made RIGOROUS: the joint-soundness 'decoding
  margin' is MEASURED empirically as J(E) rather than assumed as the independence product r^E, since a single LLM reader produces
  positively-correlated reading errors -- so the predicted peak uses the measured channel correlation. The Level-2 framing
  is SELECTIVE PREDICTION / risk-coverage in ML: compare an abstaining method against non-abstaining baselines at MATCHED
  COVERAGE with a shared coverage object and report the ACTIONABLE (singleton-resolution-to-correct) yield AND the downstream
  hallucination-rate reduction. Two refinements drive THIS iteration. (a) CORPUS SELECTION AS EXPERIMENTAL DESIGN: a mechanism's
  claim must live on a corpus that can structurally host it -- since MATRES annotates only adjacent-sentence pairs its deduction-required
  envelope is empty by construction, so the headline is relocated to a DENSE, full-coverage, direct-human-gold corpus (NarrativeTime)
  and corroborated where gold is provably non-closure-derived (TDDMan), with MATRES retained as a control that proves the
  gate discriminates. (b) ARM SCOPING borrowed from the discipline of stating where a mechanism's advantage must and must
  not appear: iterated closure provably equals a single intersection pass on acyclic length-2 structures, so the iteration
  win is claimed only on >=3-edge/cyclic structures -- now found on BOTH synthetic networks and the dense corpus's real long-hop
  stratum, dissolving the prior internal contradiction without confining the win to synthetic data. Three cross-field insights
  anchor the design: (1) LLMs are competent LOCAL qualitative namers that do NOT propagate constraints across paths -- the
  missing piece is global ITERATED propagation, and cross-path INTERSECTION of sound sets is a zero-FP win needing no over-commitment;
  (2) because the table is mathematical ground truth, intersection-of-sound-sets can only move toward gold and collapse-of-unsound-sets
  is a calibration-free certificate -- flipping the objective from accuracy-by-committing (ILP global inference, whose own
  results show consistency-enforcement does not raise F1) to faithfulness-by-abstaining; (3) the coding-theory lens names
  BOTH the safe primary mode (erasure-style narrowing) and the Achilles heel (a recall-bounded decoding radius whose EMPIRICAL
  joint-soundness decay produces an inverted-U), elevated to a pre-registered, decomposed, estimation-precision-bounded prediction
  anchored on both synthetic and real text.
terms:
- term: Dense direct-human-gold CO-PRIMARY (NarrativeTime / TimeBankNT)
  definition: >-
    The relocated real-text headline host: a timeline-based, FULL-TLink-coverage human re-annotation of TimeBank-Dense (news),
    IAA Krippendorff alpha ~0.68. Its density supplies abundant multi-path and >=3-edge/cyclic constraint structures (hosting
    both narrowing and a real-text iteration demonstration); its start-point restriction lands in the convex point algebra
    (PC COMPLETE); and its non-local gold is HUMAN-timeline-placed, not algorithmic-closure output, so closure recovery is
    non-circular. Replaces MATRES as primary because MATRES annotates only adjacent-sentence pairs.
- term: Gate-validation control (MATRES)
  definition: >-
    MATRES is retained but repositioned: because it annotates ONLY same/adjacent-sentence event pairs, every gold edge is
    locally co-occurring (directly-readable), so its deduction-required multi-path-with-bite envelope is structurally near-EMPTY
    and T0's N* ~ 0 by construction. Reporting this N* ~ 0 alongside NarrativeTime/TDDMan N* >> 0 demonstrates the deduction-required
    gate is DISCRIMINATIVE rather than vacuous.
- term: Non-circularity anchor (TDDMan)
  definition: >-
    The manually-annotated long-distance (>1-sentence-apart) subset of TDDiscourse whose pairs 'cannot be inferred automatically
    from existing annotations' -- so its gold is provably NOT the output of the closure algorithm under test. A Mode-A narrowing
    win on TDDMan therefore cannot be a closure artifact, bounding the residual timeline-implied-circularity worry about NarrativeTime
    by empirical replication rather than assertion. Relation set {before, after, simultaneous, includes, is_included}, coarse
    interval algebra.
- term: Non-circularity audit (locally-justifiable vs purely-timeline-implied)
  definition: >-
    For NarrativeTime, a partition of held-out edges into LOCALLY-JUSTIFIABLE (a textual cue near both events that the local-only
    reader can exploit) versus PURELY-TIMELINE-IMPLIED (no local cue; gold obtainable only from the human's holistic timeline).
    The deduction-required headline subset is the latter; because its gold is human-timeline placement (not algorithmic PC),
    recovering it by closure over independently LLM-read edges uses a DIFFERENT inference process and is non-circular. The
    fraction is reported up front.
- term: End-to-end hallucination-reduction headline (H2)
  definition: >-
    Promoted from a Tier-2 echo to a co-headline because it is the umbrella pipeline's actual deliverable: on the deduction-required
    / absent-relation subset, the closure pipeline's CONFIDENT-WRONG (non-abstained gold-mismatch) rate is lower than a raw
    LLM forced to a single relation, by at least a PRE-REGISTERED minimum effect, adjusted-CI-separated. A gateway test of
    the confirmatory family.
- term: Real-text iteration stratum (H3 on real text)
  definition: >-
    The dense corpus's >=3-edge/cyclic constraint structures, whose prevalence T0 computes a-priori (zero LLM spend). Length-2
    real queries still tie naive intersection (as predicted), but on this stratum full ITERATED closure can beat naive single-pass
    intersection -- bringing part of the iteration win onto real text instead of confining it to synthetic networks. If the
    stratum is empty/tiny, the iteration claim honestly stays synthetic-only.
- term: Applicability-envelope threshold (concrete number)
  definition: >-
    The pre-registered NUMBER distinguishing a 'general mechanism' from a 'niche safety-net': the deduction-required multi-path-with-bite
    fraction of evaluable held-out edges is scored >=10% = general mechanism, 5-10% = useful module, <5% = niche safety-net.
    Fixed before any LLM spend and reported from T0, so the contribution's reach is declared, not argued post-hoc.
- term: Multiplicity policy (confirmatory vs exploratory)
  definition: >-
    A pre-registered stance against the garden-of-forking-paths objection: the CONFIRMATORY family is H1 (narrowing), H2 (hallucination
    reduction), H3 (iteration gap grows), H4 (redundancy inverted-U disconfirmer), tested with Holm-Bonferroni / hierarchical
    gatekeeping (H1/H2 gateways) and ADJUSTED CIs; all strata, per-bin curves, reader-agnosticity, Mode-B, and secondary corpora
    are EXPLORATORY with nominal CIs.
- term: Recall-and-rho-matched reader-agnosticity
  definition: >-
    The protocol for the alternative-edge-reader test: each reader (METRE-style trained multi-label head; a second LLM/prompt
    family) is tuned to a MATCHED per-edge recall AND its measured cross-edge error correlation rho is reported, with the
    agnosticity verdict interpreted conditional on BOTH (conditioning on rho if it differs materially). Prevents 'the win
    is in the algebra' from being confounded by a reader whose F1-oriented training gives the same recall but different error
    correlation.
- term: Empirical joint soundness J(E)
  definition: >-
    The realized fraction of E-edge constraining subnetworks in which ALL edges are sound, MEASURED directly from data, replacing
    the independence product prod_e r_e. The zero-FP audit's reliability curve is pre-registered against J(E); the inverted-U
    cost term is 1 - J(E); positive cross-edge correlation rho makes J(E) decay slower than r^E so the predicted peak sits
    further out than an independence model says.
- term: Sound narrowing (Mode A, primary)
  definition: >-
    The zero-false-positive value mode: when every contributing LLM edge set is SOUND (contains its gold relation) but sub-universal,
    intersecting the compositions arriving at a query pair from MULTIPLE non-universal paths yields a set that still contains
    gold yet is strictly tighter than any single path. Requires breadth + multi-path bite, NOT over-commitment; its zero-FP
    guarantee SURVIVES PC incompleteness; inert only in the degenerate all-universal limit.
- term: Singleton-resolution-to-correct yield (headline metric)
  definition: >-
    The load-bearing Mode-A metric: the fraction of multi-path SOUND-input query pairs whose cross-path intersection collapses
    the query to the single CORRECT relation. Distinguished from STRICT-TIGHTENING yield (any reduction), which does NOT move
    matched-coverage selective accuracy nor the hallucination-rate metric. Both reported; singleton-resolution is load-bearing.
- term: Inverted-U redundancy optimum
  definition: >-
    Net Mode-A selective-accuracy gain RISES then FALLS as path redundancy/hop-count increases at fixed per-edge recall: more
    paths add narrowing benefit, but each added contributing edge lowers empirical joint soundness J(E), so silent-narrowing
    cost (1 - J(E)) eventually dominates. Peak location increases with recall; the recall-floor gate shifts it outward. Established
    only at a pre-registered estimation precision; otherwise reported as 'directionally consistent.'
- term: Naive-intersection baseline
  definition: >-
    Intersect the compositions arriving at the query pair in a SINGLE pass, without iterating to a fixpoint and without algebra-seeded
    converse propagation -- i.e. 'Path-of-Thoughts plus one obvious intersection step.' It COINCIDES with full closure on
    length-2 multi-path queries (so Mode A is predicted to TIE it on the real-text length-2 stratum) but diverges on longer/cyclic
    networks, where the full-minus-naive gap GROWS -- the iteration claim, tested on synthetic AND the real >=3-edge/cyclic
    stratum.
- term: Detection/repair (Mode B, secondary)
  definition: >-
    The collapse-based value mode: an empty closure certifies that some LLM edge is UNSOUND -- a gold-free zero-FP DETECTION
    flag (conditional on recall). Requires at least one over-committed/recall-failed edge to fire, supports Reiter-style minimal-hitting-set
    localisation/repair (which can mislocalise), and carries the silent-wrong-narrowing dual. Reported distinctly from Mode
    A; magnitude tracks the measured over-commitment rate.
- term: Recall-bite frontier
  definition: >-
    The curve, traced by sweeping the prompt-elicited breadth knob from 'name the relation' to 'name the maximal sound set,'
    of per-edge recall against singleton-resolution-to-correct yield and collapse rate. Recall and bite are in direct tension
    on the SAME knob, so a single operating point cannot establish viability; we map the frontier and pre-register that the
    main run proceeds only if a region clears a recall gate AND yields non-trivial singleton-resolution-to-correct.
- term: Deduction-required vs directly-readable stratification
  definition: >-
    A LOCAL-ONLY READER probe predicts each held-out edge from ONLY the minimal local span(s) where its two events co-occur
    (or flags 'no shared span'). Edges it confidently and correctly names are DIRECTLY-READABLE; the rest are DEDUCTION-REQUIRED
    (obtainable only by composing >=2 edges). We foreground the deduction-required fraction, stratify the headline by it,
    and draw the primary subset preferentially from deduction-required triangles. The T0 gate uses a structural proxy (no
    shared local span) computable without the LLM.
- term: Convex point algebra (NarrativeTime start-point arm)
  definition: >-
    The relation algebra over a single time point per event with convex base relations <=, =, >= (and disjunctions). NarrativeTime's
    timeline yields start-points whose ordering instantiates this algebra, for which path-consistency is provably COMPLETE
    and the table exact. We widen non-convex {<,>} (genuine !=) to VAGUE to preserve completeness and MEASURE the bite lost;
    if non-trivial we add a full-interval Allen arm scored as a lower-bound detector.
- term: Silent wrong narrowing (pre-registered failure mode)
  definition: >-
    When a contributing set OMITS gold (unsound), closure can narrow the query to a confident WRONG singleton with NO empty
    collapse -- a certified-LOOKING hallucination the mechanism actively endorses. Its rate is bounded per-edge by (1-recall)
    and per-network by (1 - J(E)); reported in the decomposition of gold-wrong non-abstained predictions; the recall-floor
    gate is tested as a mitigation and as the lever that shifts the inverted-U redundancy peak.
- term: Matched-coverage selective comparison
  definition: >-
    The protocol for comparing an abstaining method against baselines: each baseline is given its own abstention/confidence
    signal (vote margin, verbalised confidence, vote agreement, path-agreement), thresholds are swept so every method reports
    at the SAME coverage using the SAME coverage object (single-relation resolution), and selective accuracy is compared with
    paired-bootstrap CIs -- preventing the headline from conflating 'closure' with 'closure has a better-calibrated abstain.'
- term: Trace-graph
  definition: >-
    A human-auditable record: the QCN, which composition entries fired on which paths during closure, any minimal repairs,
    and optionally an equivalent SWI-Prolog/ASP proof discharged from the closed table for replay -- the connective tissue
    to the umbrella text-to-logic pipeline's auditability and quantified-hallucination-reduction requirements.
summary: >-
  We import exact relation-algebra path consistency (Allen interval, convex point algebra, RCC-8) into the deduction module
  of a text-to-logic pipeline and -- fixing the prior version's fatal corpus choice -- relocate the real-text headline from
  MATRES (adjacent-sentence-only, deduction-required envelope empty by construction) to a DENSE direct-human-gold corpus (NarrativeTime,
  full TLink coverage, human-timeline gold), corroborated on TDDMan whose gold is provably non-closure-derived: cross-path
  SOUND NARROWING of the LLM's high-recall disjunctive sets beats path-isolated reasoning and voting at matched coverage AND
  cuts the hallucination rate versus a raw LLM, while iterated closure beats naive single-pass intersection on long-hop/cyclic
  structures both synthetic AND real, and the recall-bounded inverted-U redundancy optimum is audited via empirical joint
  soundness J(E). An a-priori, zero-LLM-spend envelope gate (with a concrete applicability threshold), a confirmatory-vs-exploratory
  multiplicity policy, and recall-and-rho-matched reader-agnosticity make every headline falsifiable before any model is called.
_relation_rationale: >-
  Same certificate frame; collapsed two co-headline theses to one (certificate); cross-path coding demoted to a negative.
_confidence_delta: decreased
_key_changes:
- >-
  COLLAPSED to ONE thesis (reviewer clarity + novelty MAJORs): the training-free/gold-free/per-edge abstain-on-collapse CERTIFICATE
  is the sole headline; the prior co-headline 'two-condition characterization' is demoted to a single supporting negative
  subsection.
- >-
  Made the certificate's CONFIDENCE-THRESHOLD-BEATING evidence load-bearing (reviewer novelty MAJOR): reframed the distinctive
  value as reducing confident-wrong on NO-DERIVATION/absent-relation queries where confidence thresholds structurally cannot
  (high-confidence hallucinations), with the CLUTRR 0.444 absent-relation reduction as the lead.
- >-
  Added a CONFIDENCE-THRESHOLDED RAW-ABSTAIN baseline as a REQUIRED comparison everywhere (reviewer evidence MAJOR), replacing
  the always-answer commit-argmax-only benchmark in the fuzzy-unification table and the absent-relation pool; pre-registered
  that the certificate beats it on the no-derivation stratum and ties/loses on ordinary deduction (honest scope).
- >-
  TEMPERED the 'two necessary conditions'/'two-condition law'/'sharp characterization' framing to 'two conditions each independently
  violated in the two real venues we could a-priori-gate, with synthetic controls confirming the mechanism when both hold'
  — an explanatory account of two negatives, not a predictive law (reviewer rigor MAJOR).
- >-
  Absorbed the iter-5 spatial RCC-8 negative (art_i53dBKgGY3Ig): cross-path coding is now SYNTHETIC-ONLY on BOTH gated real
  venues (temporal near-universe reads; spatial containment-tree gold); the 27.4% GENERAL-band flag was purely structural.
  Did NOT re-propose RCC-8 (reviewer: experiment done, negative clean).
- >-
  Set the iter-6 DECISIVE experiment to (A) add fair confidence-thresholded baselines to all existing certificate comparisons
  and (B) demonstrate the certificate's edge over a confidence-thresholded abstainer on >=1 additional GENUINELY NATURAL corpus'
  no-derivation stratum, with an honest scope-down fork if no clean natural corpus exists.
- >-
  Reframed the genuine fuzzy-unification result (art_I22c-J7-OcXl) honestly: its certificate edge over a fair neural abstainer
  rests on ~5 Mode-B sound-violation catches (0 untested on kinship), framed as 'faithful abstention that additionally catches
  sound-violations confidence cannot' rather than '0.000 vs 0.364'.
- >-
  Re-targeted the primary venue from ACL Knowledge Extraction to NeSy / temporal-and-qualitative-reasoning (reviewer scope
  MINOR) and labeled the operational ~3000-char docs as bracket-selected (temporal) and concatenation-constructed (kinship).
- >-
  DEMOTED the algebra-richness scaling law, inherited/novel decomposition, zero-FP theorem, and synthetic inverted-U to a
  compact appendix/half-page (reviewer clarity MINOR); kept the corrected marginal-temporal statistics as a supporting (non-headline)
  section.
- >-
  Lowered overall confidence: the novel mechanism is now negative on both gated real venues and the reviewer caps the transferable
  positive as incremental, so the paper's ceiling rests entirely on proving the certificate beats a confidence-thresholded
  baseline.
relation_type: evolution
</hypothesis>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: evaluation_iter6_dir3
type: evaluation
objective: >-
  At ZERO LLM spend, retire the reviewer's MAJOR #2 (fuzzy fair baseline), MAJOR #3 (temper the two-condition framing), and
  MINORs #4/#5 (venue reposition + one-thesis consolidation), handing GEN_PAPER_TEXT a single load-bearing thesis with the
  cross-path negative demoted to one honestly-bounded subsection and the mechanism analysis pushed to an appendix. This is
  the framing spine that makes the paper read as ONE crisp advance the reader can repeat verbatim.
approach: >-
  Pure re-analysis (numpy+scipy only, seed-fixed paired bootstrap B=10000, ~seconds CPU; $0 LLM, no OpenRouter client). Extend
  the prior re-analyses by reading their workspaces directly via filesystem (they are not depends_on because evaluations cannot
  depend on evaluations): iter-5 re-analysis at /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_5/gen_art/gen_art_evaluation_1
  (eval_out.json: one_thesis_contribution_table, small-bite block) and iter-4 re-analysis at /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1
  (eval_out.json: corrected_temporal, contribution split); reproduce-and-verify before extending. TASK 1 (MAJOR #2 -- fuzzy
  fair baseline, $0 from stored confidences): from the fuzzy experiment [ARTIFACT:art_I22c-J7-OcXl] (per-record metadata_top1_conf/metadata_sound/metadata_top1_correct/metadata_gold
  are stored; read full_method_out.json or the workspace) construct a CONFIDENCE-THRESHOLDED TOP-1 baseline = commit top-1
  iff top1_conf >= tau else abstain, sweeping tau to MATCH the certificate coverage (0.535 spatial / 0.314 kinship); compute
  its confident-wrong, doc-clustered Delta-CI vs the certificate's 0.000, and REPORT WHETHER THE CERTIFICATE BEATS IT. Because
  the fuzzy reads are calibrated (ECE 0.11-0.14), the thresholded top-1 may also achieve low confident-wrong -- so QUANTIFY
  the certificate's distinctive edge precisely: the ~5 genuinely-unsound spatial reads CAUGHT by Mode-B collapse (e.g. 'around'
  -> {NTPPi,TPPi} dropping gold EC) vs 0 catchable on kinship (0 unsound reads -> untested). FRAME the contribution honestly
  as 'auditable, faithful abstention that ADDITIONALLY catches sound-violations confidence cannot', with the catch count carrying
  the section rather than '0.000 vs 0.364'. Rebuild Table 3 with the confidence-thresholded column added. TASK 2 (MAJOR #3
  -- temper the two-condition framing): rewrite the sec:decisive language from 'two NECESSARY conditions / sharp, general
  characterization / two-condition LAW' to an EXPLANATORY ACCOUNT: 'two conditions -- informative sub-universal reads AND
  same-algebra structural redundancy -- that were each INDEPENDENTLY VIOLATED in the two real venues we could a-priori-gate
  (temporal Allen near-universe reads; spatial RCC-8 containment-tree gold), with synthetic controls confirming the mechanism
  when both hold.' State explicitly it is NOT a predictive law and NOT a co-equal headline; mark it ONE subordinate subsection.
  Provide the exact tempered paragraph. TASK 3 (MINOR #5 -- one thesis): produce ONE contribution table whose COLUMNS are
  {claim, evidence-class tag, where-it-holds, status}, with a SINGLE SPINE ROW = the training-free/gold-free/per-edge abstain-on-collapse
  CERTIFICATE and its confidence-threshold-beating value on no-derivation hallucinations; the cross-path coding negative =
  ONE supporting row; the algebra-richness scaling law, inherited/novel decomposition (+0.673 inherited / +0.0025 novel),
  redundancy inverted-U (+0.024 bite), and zero-FP theorem = APPENDIX rows. Supply the one-line thesis statement to repeat
  verbatim in abstract + conclusion ('A structural, label-free certificate that catches confident relational hallucinations
  that confidence cannot see'). Leave a clearly-LABELED PENDING slot for STEP A's CLUTRR/spatial confidence-abstainer result
  and iter-7's natural-corpus STEP-B result. TASK 4 (MINOR #4 -- venue + scope): write the justification for repositioning
  the primary venue from ACL Knowledge Extraction to a NeSy / temporal-and-qualitative-reasoning track (contribution is deduction/consistency,
  not extraction); enumerate the deduction-sub-module scope boundaries (atomic extraction measured-not-improved ~0.53 F1;
  OpenCyc out of scope; hand-supplied tables; extraction-limited ~19% coverage) as abstract-front-matter; and label the operational
  ~3000-char docs as bracket-selected (temporal) and concatenation-constructed (kinship) -- noting the iter-6 Re-DocRED corpus
  will supply genuinely-natural ~3000-char documents. OUTPUT eval_out.json (aii-json exp_eval_sol_out; all derived numbers
  under metadata) + eval_digest.md with the rebuilt fuzzy Table 3 (confidence-thresholded column + Mode-B catch count), the
  tempered two-condition paragraph, the one-thesis tags-in-columns table with the pending slot, the venue-reposition text,
  and explicit headline-structure guidance for GEN_PAPER_TEXT. Every number carries an evidence tag.
depends_on:
- id: art_I22c-J7-OcXl
  label: fuzzy
  relation_type:
  relation_rationale:
- id: art_i53dBKgGY3Ig
  label: spatial-crosspath
  relation_type:
  relation_rationale:
- id: art_0a7i481ZRwS1
  label: clutrr
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
id: art_0a7i481ZRwS1
type: experiment
title: >-
  CLUTRR kinship closure-certificate pipeline: atomic P/R, multi-hop accuracy, Prolog trace
summary: "End-to-end neuro-symbolic experiment on the prepared CLUTRR kinship gold graphs (dependency art_HS7-lxhZnU9m; clutrr_gen\
  \ + clutrr_disc), delivering all four umbrella goal items on real (non-synthetic, non-temporal) text in ONE run with an\
  \ explicit CONFIRM verdict. A cheap LLM (google/gemini-3.1-flash-lite, automatic deepseek-v3.2 fallback on rate-limit) reads\
  \ atomic kinship triples from each de-bracketed story; a finite-composition-table closure engine recovers the held-out query\
  \ relation and emits a certificate.\n\nKEY ENGINEERING RESULT (load-bearing): CLUTRR's kinship table is a finite composition\
  \ table, NOT a relation algebra. Porting the iter-2 PC-2 (Mackworth converse-INTERSECTION) closure is UNSOUND here -- it\
  \ collapses ~13% of GOLD-clean chains to EMPTY. The SOUND closure is a forward least-fixpoint UNION derivation over DEFINED\
  \ compositions only (mirrors CLUTRR's own gold_proof backward-chaining and the emitted Prolog derive/solve predicate). Output\
  \ contract: |D[query]|==1 -> EMIT; >1 -> ABSTAIN (Mode-B conflict); ==0 -> ABSTAIN (no path = absent-relation, hallucination-safe).\
  \ Decisive 0-LLM go/no-go on ALL 16,131 clean gen rows: 100% accuracy on every emitted answer (soundness) at 98.5% singleton-rate;\
  \ the ~1.5% abstentions are a genuine table ambiguity (inv-child vs inv-in-law: the same surface chain 'husband-son-grandmother'\
  \ yields gold 'mother' for one story and 'mother-in-law' for another -> the table provably cannot disambiguate), so Mode-A\
  \ abstains rather than guess.\n\nRESULTS (scored set: 102 present + 180 absent queries spanning hops 2..10; all baselines\
  \ thresholded to the SAME matched-coverage object; doc-clustered paired bootstrap; Holm over {H1_pot,H1_sc,H2}):\n(i) Atomic-extraction\
  \ P/R/F1 = 0.536 / 0.532 / 0.534 (doc-clustered CIs; stable ~0.5 recall across hops; disc by-noise breakdown). \n(ii) H1\
  \ CONFIRMED -- Mode-A selective accuracy 0.886 at matched coverage 0.686 vs Path-of-Thoughts 0.457 (gap +0.429, CI [0.298,0.557],\
  \ p_adj=0.0015), self-consistency 0.557 (gap +0.329, CI [0.205,0.458]), raw-LLM 0.543, naive single-pass 0.229, off 0.0.\
  \ Accuracy-vs-chain-length: Mode-A stays ~1.0 selective accuracy through hop-10 while raw->0.0 / PoT->0.2. H3 CONFIRMED\
  \ -- full-minus-naive coverage gap is ~0 at hop-2 (naive ties full, as predicted) and grows to 0.6-0.9 for hop>=3 (naive\
  \ resolves only hop-2; full PC derives the rest). Gold-read ORACLE (0-LLM upper bound): Mode-A 1.00 selective accuracy at\
  \ 0.951 coverage -> the bottleneck is the neural READ (atomic recall ~0.53), not the symbolic closure (the iter-1 read-soundness\
  \ localization, reproduced on real text).\n(iii) Trace-graph ACTUALLY discharged in SWI-Prolog (v9.0.4): 40/40 sampled queries\
  \ executed in-engine (subprocess; pyswip also verified), 40/40 match the Python reference, 39/40 match gold; a worked 3-entity\
  \ example records the extracted atomics, the Mode-A composition trace (fired t1 o t2 -> t3 steps), the Prolog proof, and\
  \ one Mode-B collapse.\n(iv) H2 CONFIRMED -- absent-relation confident-wrong (hallucination) rate at matched coverage: raw-LLM\
  \ 0.472 vs Mode-A 0.028 = 0.444 absolute reduction (CI [0.317,0.583], meets the pre-registered >=0.20 bar, CI excludes 0);\
  \ full risk-coverage curves reported per method with abstention stated alongside every number, plus a mixed present/absent\
  \ pool so abstain-on-everything cannot win.\n\nCROSS-FAMILY (reader-agnostic): with deepseek-v3.2 as the reader at matched\
  \ per-edge recall (0.51), Mode-A selective accuracy 0.867 vs raw 0.511 -- the closure gain is not an artifact of one reader.\n\
  \nFILES: method.py orchestrator (+ kinship.py forward-closure engine, dataio.py loader/go-no-go, readers.py LLM prompts+parsers,\
  \ baselines.py matched-coverage/risk-coverage stats, prolog.py SWI-Prolog discharge, figures.py, tests.py 0-LLM unit tests;\
  \ engine.py/llm.py/stats.py reused verbatim from iter-2). method_out.json (exp_gen_sol_out, schema-validated) carries per-query\
  \ predict_modeA/modeA_goldread/naive/raw/sc/pot/off + gold and all metadata tables (atomic_pr, deduction_matched_coverage,\
  \ deduction_goldread_oracle, accuracy_vs_hop, absent_relation_h2, risk_coverage curves, holm_family, prolog_discharge, worked_example_3entity,\
  \ cross_family_sensitivity, gold_atomic_engine_sanity, verdict). Four figures in results/.\n\nHONEST CAVEATS: CLUTRR stories\
  \ are short (max 871 chars; none reach the umbrella's ~3000-char target -- longer documents live only in the temporal corpora);\
  \ entity grounding + gender use gold for surface realization (NOT the contribution); a minority of raw/SC/PoT baseline queries\
  \ fell back to deepseek during a gemini rate-limit window (both cheap readers; cross-family confirms reader-agnosticity).\
  \ Total LLM spend well under the $9 hard cap (sha256-cached, cost-guarded). Verdict: CONFIRM (H1, H2, H3)."
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Dependency 2 ---
id: art_i53dBKgGY3Ig
type: experiment
title: >-
  Spatial RCC-8 cross-path test: structural scope-boundary + closure hallucination audit
summary: |-
  Decisive iter-5 experiment on SpaRTUN/SpaRP-PS1 (the strongest real spatial venue, 27.4% structurally-flagged 'tight multipath'), resolving two pre-registered questions. CPU-only; total LLM spend $0.225 (< $9 cap, gemini-3.1-flash-lite primary + deepseek-v3.2 cross-family); cached reruns $0. All four method_out variants validate against exp_gen_sol_out.

  ENGINE (new, self-tested, reusable): RCC-8 (8-relation, 64-cell GQR table) AND a Cardinal Direction Calculus (CDC, 9-relation) built as the product of two convex point algebras (reproduces GQR cd.comp per dossier art_2Xp7DiYUxoNo) -- 81 cells. Both pass a blocking self-test; closure unit tests verify naive==full@len-2, naive!=full@>=3-hop chain, Mode-B inconsistency collapse, non-symmetric orientation (TPP<->TPPi), and a multi-path intersection narrowing.

  Q1 (cross-path-intersection FORK) = SCOPE-BOUNDARY, gold-structural, $0. A zero-LLM a-priori gate over VERIFIED gold composition shows the error-correcting-code mechanism cannot realize on the real gold graphs of EITHER single algebra: the RCC-8 subgraph is a containment TREE (all 228 RCC-8 deduction queries have exactly 1 edge-disjoint path), and the cardinal subgraph's 57 >=2-short-path queries already compose to a SINGLETON on the best single path (best_single_len_hist={1:54,2:2,3:1}), leaving no room for intersection bite. The corpus's 27.4% flag is purely STRUCTURAL (undirected, mixed-algebra, no composition); the genuine redundancy is CROSS-ALGEBRA (topology vs direction), not intersectable in one calculus. This empirically vindicates the dataset card's own 'verify, don't trust noise labels' caveat at a deeper level, and is a SHARPER negative than the iter-4 temporal one: it needs no LLM reads. The mechanism IS real when same-algebra redundancy + sound reads exist -- the synthetic RCC-8 positive control (1-D interval model) at recall 0.95 gives intersection selective-acc 0.89 > best-single 0.80 (+0.093, mean bite 1.23), degrading correctly as recall drops.

  Q2 (real-venue closure-certified deduction vs neural baselines) = ABSTENTION-DRIVEN HALLUCINATION REDUCTION. On the 228 single-path RCC-8 deduction queries SpaRP-PS1 hosts (gold-singleton, gold-sound, hops 2-3), the neuro-symbolic method (read local stated RCC-8 constituents -> exact GQR-table compose -> abstain on collapse/non-singleton) cuts confident-wrong (hallucination) from raw-LLM 0.193 / chain-of-thought 0.123 to 0.022 (reduction 0.171, 95% CI [0.118,0.228], Holm-significant), with auditable Prolog trace-graphs. HONEST framing surfaced prominently: this is a COVERAGE tradeoff, not an accuracy gain -- the method answers only 15% of queries; at MATCHED coverage the raw LLM is NOT less accurate (method 0.853 vs raw 0.941, gap CI [-0.22,0.04]); and a neural baseline given the same abstention signal (raw-abstain: hallucination 0.035 @ coverage 0.285) is competitive/dominant. The gold-read ORACLE resolves 0.89 at 0 hallucination -> the symbolic engine is SOUND and not the bottleneck; the binding constraint is constituent-read recall (0.55) under a coverage-vs-soundness tradeoff. Spatial RCC-8 reads are FAR more informative than temporal-Allen reads (breadth 2.1/8 vs 11.5/13; underdetermined 0.04 vs 0.87), so the spatial negative is STRUCTURAL, not a read-quality failure -- a distinct second binding mode from the temporal venue. SpaRP object descriptions were recovered 100% from the raw symbolic_entity_map (resolving the #1 mention-recovery risk). Cross-family (deepseek-v3.2) corroborates (constituent recall 0.585, method hallucination 0.0). Prolog audit (python-checked, swipl unavailable) emits a synthetic 2-path narrowing (5-set ∩ 3-set -> {DC}), two real single-path closure traces, and a Mode-B collapse ({NTPP} ∩ {DC} = empty); python==engine on all.

  For downstream paper-writing: lead Q1 as a clean $0 gold-structural scope-boundary (mechanism synthetic-only, proven real by the control); present Q2 as an honest interpretability result (certified abstain-on-collapse converts confident-wrong outputs into auditable abstentions but does not beat a confidence-thresholded neural baseline). The transferable contribution is the training-free, gold-free abstain-on-collapse certificate + sound exact-table composition; the cross-path error-correcting-code thesis remains synthetic-only.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_5/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Dependency 3 ---
id: art_I22c-J7-OcXl
type: experiment
title: Genuine LLM Fuzzy-Unification with a Certificate-Bounded Hallucination Guarantee
summary: |-
  Converts reviewer MAJOR #2 (the iter-4 Mode-P 'fuzzy unification' was circular memorized-table recall at confidence exactly 1.0) into a real, measured contribution. method.py builds GENUINELY-fuzzy LLM reads from existing gold in two labeled settings and shows a training-free abstain-on-collapse CERTIFICATE bounds the hallucination cost of feeding them into a sound closure engine.

  SETTING 1 (vague spatial RCC-8, SpaRP-PS1, art_f-ofxduZjwSM): a KNOWN RCC-8 relation is rendered with a vague preposition (near/touching/around/inside/overlapping) that has no single RCC-8 answer; gemini-3.1-flash-lite (temp 0) emits a calibrated sub-1.0 disjunction over the 8 base relations. SETTING 2 (ambiguous kinship, CLUTRR, art_HS7-lxhZnU9m): an atomic fact is replaced by an informal term (guardian/descendant/family elder/sibling-figure/relative by marriage/younger relative) mapping to a type-disjunction.

  MEASURED (cap 1500/setting; total real spend $0.0029 over 22 sha256-cached calls; warm reruns $0): (i) CALIBRATION - frac_conf_1p0=0.00 in BOTH settings vs the memorized Mode-P's 1.00 (the headline honesty contrast, loaded from the iter-4 method_out.json); per-candidate ECE 0.142 (spatial)/0.111 (kinship), top-1 ECE 0.286/0.051; spatial read soundness 0.93 (genuine unsound reads), kinship 1.00. (ii) CERTIFICATE-BOUNDED CLOSURE - fuzzy disjunction + exact-table reads fed into qcn.algebras RCC-8 path composition+intersection and a new disjunctive-seed kinship forward-union closure; output contract COMMIT(|D|=1)/COLLAPSE(|D|=0,Mode-B)/ABSTAIN(|D|>1). Risk-coverage vs commit-argmax (point estimate, always answers) and abstain-always: certificate confident-wrong=0.000 at coverage 0.54 (spatial, n=228 all deduction-required RCC-8 queries, 38 multipath) and 0.31 (kinship, n=1013 clean multi-hop) vs commit-argmax 0.364/0.216 (doc-clustered paired-bootstrap Delta-CI [0.30,0.43] and [0.17,0.26], both exclude 0). The read-soundness-conditional ZERO-FP invariant (sound read => no confident-wrong) is proved by construction and ASSERTED (0 violations); spatial unsound reads caught 1.0 (0 silent-wrong missed). (iii) AUDITABLE TRACE-GRAPHS tag every step exact_table vs llm_fuzzy with the emitted set + per-relation p + gold-retained flag + final certificate decision, including the honest unsound-read-caught case (around -> {NTPPi,TPPi} drops gold EC => certificate ABSTAINs instead of committing wrong DC).

  Also: cross-family sensitivity (deepseek-v3.2 hedges broader, breadth 4.6/6.1, still calibrated frac_conf_1p0=0.00); symbolic self-tests T1/T2 (200/200 spatial exact-path soundness, 200/200 kinship gold-clean recovery, disjunctive-seed zero-FP unit test); VERDICT YES for both settings.

  BASELINES: commit-argmax and abstain-always on the identical query pool, plus the memorized Mode-P calibration contrast. Reuses iter-4 engines (llm.py sha256 cache + $9 hard guard, kinship.py, stats.py, dataio.py, qcn/). HONEST CAVEATS recorded: reads are term-conditioned (the vague term is the unit of fuzziness; ~6 distinct reads drive hundreds of per-edge calibration records, empirical per-term gold mix is the target); SpaRP uses symbolic ids + templated text; CLUTRR <=871 chars; kinship had 0 unsound reads so its certificate-catch is untested (zero confident-wrong holds trivially there). Files: method.py, figures.py (4 PNGs: calibration contrast, reliability diagrams, risk-coverage frontier, breadth-vs-confidence), method_out.json (aii exp_gen_sol_out validated) + mini/preview/full. method_out.json datasets: spatial_fuzzy_rcc8 (1728 ex) and kinship_fuzzy_paraphrase (2513 ex) with predict_certificate/predict_commit_argmax/predict_abstain_always.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_5/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle
</artifact_executor_scope>

<artifact_planning_rules>
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for evaluation artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for an EVALUATION artifact.",
  "properties": {
    "title": {
      "description": "Short title for the plan",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "metrics_descriptions": {
      "description": "What metrics will be computed and how they're defined",
      "title": "Metrics Descriptions",
      "type": "string"
    },
    "metrics_justification": {
      "description": "Why these metrics are the right ones - what do they tell us about the hypothesis",
      "title": "Metrics Justification",
      "type": "string"
    }
  },
  "required": [
    "title",
    "metrics_descriptions",
    "metrics_justification"
  ],
  "title": "EvaluationPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-18 00:28:01 UTC

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
