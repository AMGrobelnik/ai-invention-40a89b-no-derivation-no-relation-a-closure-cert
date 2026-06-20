# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 7 · `gen_plan`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 02:14:15 UTC

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
You are expanding an artifact direction of type: EXPERIMENT

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance
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

The experiment executor has 6h total (including writing code, debugging, testing, and fixing errors).

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
  The Confidence/Uncertainty Family Is Structurally Blind to Confident Absent-Relation Hallucinations, but a Gold-Free Structural
  Certificate Is Not: An Empirical Isolation in the Deduction Sub-Module of Text-to-Logic Pipelines (the natural-corpus run
  is the decisive open test; closure-abstention on disconnected pairs is conceded structural-by-construction; cross-path qualitative-algebra
  coding is synthetic-channel-only)
hypothesis: |-
  ONE THESIS, REFRAMED AS AN EMPIRICAL / DIAGNOSTIC CONTRIBUTION (reviewer novelty MAJOR + rigor MAJOR, both this round). We STOP positioning the certificate's machinery as the novelty and concede this up-front, as the paper's FRAMING rather than a footnote: keeping the LLM a high-recall disjunctive reader, composing ONLY through exact relation-algebra tables, EMITting a singleton / ABSTAINing on a residual disjunction / FLAGging an unsound read on empty collapse is the STANDARD neuro-symbolic premise -- 'a sound reasoner abstains when it cannot derive an answer' is the default behavior of any sound NeSy system, worth +0.673 inherited vs only +0.0025 novel on selective accuracy (art_D0cHQUJ8kY75). The genuine, defensible, NON-INCREMENTAL new KNOWLEDGE is an EMPIRICAL ISOLATION, not a mechanism: the ENTIRE confidence/uncertainty selective-prediction family -- verbalized confidence, self-consistency vote-margin, Kadavath P(True), semantic-entropy negentropy -- is STRUCTURALLY BLIND to a confident, self-consistent ABSENT-RELATION hallucination (a fabricated relation between entities the document does not connect), whereas a gold-free, training-free STRUCTURAL signal ('no derivation path => abstain') is not, because the absent-relation hallucination is HIGH-confidence and low-dispersion by construction. One sentence a reader repeats: 'The confidence family cannot see the relational hallucinations that matter most -- confident fabrications of relations that do not exist -- but a structural no-derivation certificate can.' Keep evidence-class tags in TABLE COLUMNS, not inline hedging. Everything else (cross-path coding thesis, algebra-richness scaling, inherited/novel decomposition, redundancy inverted-U, zero-FP theorem, fuzzy unification, operational case study, marginal natural-temporal result) is SUPPORTING, demoted to one subsection or a compact appendix.

      THE LOAD-BEARING CLAIM IS THE TWO NON-CIRCULAR FACTS, NOT THE CERTIFICATE'S ABSTENTION RATE (reviewer rigor MAJOR, accepted in full). We now state explicitly, in its own paragraph, that the certificate's near-zero confident-wrong on the ABSENT stratum is LARGELY STRUCTURAL-BY-CONSTRUCTION and must NOT be allowed to carry the section: CLUTRR absent pairs are DEFINED as entities in different connected components, so a sound forward-closure over the extracted graph derives the empty set (and abstains) on disconnected pairs almost by definition, and imperfect extraction (recall ~0.53) only INCREASES apparent disconnection, so the certificate's 2.8% confident-wrong on CLUTRR absent pairs (art_LeRQRGHJZcdQ) is near-tautological given the setup -- one side of the comparison is handed the answer. The genuinely non-circular empirical content, which becomes the headline, is two measured facts about the RAW LLM and the confidence family (both independent of the certificate): (FACT A) the raw LLM fabricates a relation on 47.2% of disconnected/absent CLUTRR pairs (cross-family deepseek-v3.2 48.3%) at HIGH confidence; and (FACT B) NO member of the best four-signal confidence/uncertainty battery removes these at the LLM's natural coverage, and at matched coverage 0.435/0.718/0.247/0.718 of them SURVIVE (verbalized/sc_margin/P(True)/negent; deepseek 0.672/0.224/0.103/0.224), so >=2 signals keep a strong majority -- a confident self-consistent fabrication is invisible to dispersion by construction. These two facts are what make the structural certificate's success informative; we tie this DIRECTLY to why extraction recall and the natural-corpus run are LOAD-BEARING: on a NATURAL corpus the extracted graph (and hence absent-detection) is no longer trivially correct -- extraction errors can make the certificate OVER-abstain on PRESENT pairs -- which is precisely what converts the natural-corpus experiment from confirmatory to DECISIVE.

      OPERATIONAL CEILING + VENUE, IN THE FIRST PARAGRAPH OF THE ABSTRACT (reviewer scope MINOR). State up-front: this is a closure-certified DEDUCTION SUB-MODULE, NOT the umbrella's operational pipeline. Explicitly OUT OF SCOPE and named as FUTURE WORK THIS PAPER DOES NOT CLAIM TO DELIVER: (a) upper-ontology / OpenCyc grounding; (b) general fuzzy unification over arbitrary predicates (we scope fuzzy to disjunctions over a KNOWN base vocabulary); (c) atomic re-extraction (extraction is MEASURED not improved: CLUTRR P/R/F1 ~= 0.536/0.532/0.534); (d) genuine ~3000-char NATURAL professional documents (no benchmark doc reaches it; the operational ~3000-char study is bracket-selected (temporal; none in [2500,3500]) and concatenation-constructed (kinship; 56/56 cross-story absent pairs trivially abstained by construction), so it shows the pipeline RUNS at length, not that it is USEFUL at length). RE-TARGET the primary venue from ACL Knowledge Extraction to a NeSy / temporal-and-qualitative-reasoning track and SAY SO; report real-text utility as structurally EXTRACTION-LIMITED (~0.53 atomic recall => ~19% Mode-A coverage on dense prose).

      ----- CLAIM 1 (THE SINGLE HEADLINE, EMPIRICAL ISOLATION): CONFIDENCE-BLINDNESS TO CONFIDENT ABSENT-RELATION HALLUCINATION, vs THE BEST 4-SIGNAL BATTERY. TAG: REAL-LLM-READ. -----
      The portable, demonstrated-at-power result, now stated as a DIAGNOSTIC about the confidence family (FACT A + FACT B) rather than as a property of the certificate mechanism. STEP A is EXECUTED (art_LeRQRGHJZcdQ, VERDICT=CONFIRM, ~$0.30): against verbalized confidence, self-consistency vote-margin@k=10, Kadavath P(True), and semantic-entropy negentropy -- the BEST available battery, not a strawman -- the raw LLM is confidently wrong on 47.2% of CLUTRR absent pairs and the certificate 2.8% (reduction 0.444, CI [0.317,0.583]); at the LLM's natural coverage NO signal removes any of these; the crux-survival table shows 0.435/0.718/0.247/0.718 surviving at matched coverage (only P(True) partially separates, median 0.0, yet 24.7% survive). The DECISIVE mixed present/absent pool (n=282, so abstain-on-everything cannot win) at matched coverage 0.266: certificate selective accuracy 0.827 vs every signal 0.37-0.44 (~2x); Holm-adjusted confident-wrong reductions 0.103-0.121, all CIs exclude 0; cross-family deepseek-v3.2 reproduces the edge. HONESTY, FOREGROUNDED: the CLUTRR-absent abstention is structural-by-construction (above); the non-circular content is FACT A and FACT B; the multi-hop PRESENT selective-accuracy win (CLUTRR 0.886 vs 0.543 at matched coverage 0.686) is the INHERITED NeSy premise, labeled as such wherever it appears.

      ----- CLAIM 2 (THE SINGLE DECISIVE OPEN EXPERIMENT for iter-7 = RUN STEP B ON THE BUILT NATURAL CORPUS). TAG: REAL-LLM-READ. -----
      This is the reviewer's #1 action (evidence MAJOR) and the paper's path above the bar; the corpus is ALREADY built and gold-verified (art_NUWTxBVWENIJ), the analogous CLUTRR battery cost ~$0.30, and the corpus is drop-in engine-compatible, so this is a cheap, in-scope experiment whose ABSENCE is the only thing keeping the central claim on templated data. iter-7 MUST run the four-signal fair-baseline experiment (verbalized, sc_margin, P(True), semantic entropy) on the Re-DocRED natural Wikipedia present/absent pools at matched coverage, reporting -- exactly as in the CLUTRR section -- (i) the raw-LLM absent-hallucination rate (FACT A), (ii) the crux-survival table (FACT B), (iii) the mixed-pool selective-accuracy showdown, and (iv) the Holm-adjusted confident-wrong reductions, on a STRONGER reader if affordable, and including >=1 ADDITIONAL relation DOMAIN or reader (reviewer novelty MAJOR-ii) -- e.g. confirm FACT A/FACT B on natural spatial-containment absent pairs or temporal no-relation queries -- to show the confidence-blindness finding is NOT kinship-specific (cross-family deepseek already supplies reader diversity). CRITICAL NATURAL-CORPUS NUANCE (ties CLAIM 2 to the rigor MAJOR): on Re-DocRED the certificate is NO LONGER handed the structural answer -- because extraction recall is imperfect, the certificate can over-abstain on PRESENT multi-hop pairs (missing connecting edges look disconnected), so the genuine test is whether it STILL answers present pairs while abstaining on absent ones in the MIXED regime. FORK (both publishable): IF the certificate beats the four-signal battery on the Re-DocRED MIXED pool at matched coverage with Holm-adjusted CIs excluding 0 -> MAKE THAT THE HEADLINE and demote CLUTRR to a TEMPLATED companion; IF extraction recall on natural prose is so low that the certificate over-abstains and TIES/LOSES the mixed-pool showdown -> report it HONESTLY as the extraction-limited boundary, while preserving the DIAGNOSTIC contribution (FACT A + FACT B are properties of the raw LLM and the confidence signals, NOT the certificate, and are expected to reproduce on natural prose regardless of the certificate's net utility) -- i.e. confidence-blindness is corpus-robust even where the certificate's net utility is gated by extraction. EITHER outcome is more valuable than the current deferral.

      ----- CLAIM 3 (GENUINE FUZZY UNIFICATION, SUPPORTING, NOW DOWNWEIGHTED; reviewer evidence MINOR). TAG: REAL-LLM-READ. -----
      The genuine fuzzy-unification experiment (art_I22c-J7-OcXl) retired the iter-4 circular Mode-P: rendering a known relation with a VAGUE preposition (near/touching/around) or an INFORMAL kinship term (guardian/family elder/relative by marriage) yields CALIBRATED sub-1.0 disjunctions (fraction-at-1.0 = 0.00 in both vs Mode-P's 1.00; per-candidate ECE 0.142 spatial / 0.111 kinship). The certificate's confident-wrong is 0.000 at coverage 0.535/0.314 vs a confidence-thresholded top-1 abstainer 0.415 [0.376,0.457] / 0.346 [0.293,0.413] (art_0MDLD-w-RXOu). UNIT-OF-ANALYSIS FIX (reviewer evidence MINOR): the 0.000-vs-0.415 contrast is APPLES-TO-ORANGES -- certificate confident-wrong is measured at the closure-QUERY level while the confidence baseline is at the edge-READ level, matched only on coverage fraction. iter-7 SHOULD either build a TRUE query-level confidence abstainer on the fuzzy pools (mirroring CLAIM 1) so the comparison is apples-to-apples, OR FURTHER downweight the fuzzy section relative to CLAIM 1 and LEAD its framing with the honestly-quantified Mode-B sound-violation catch as the distinctive contribution rather than the 0.000-vs-0.415 number. Keep the caveat but do NOT let it undercut a headline table. The DISTINCTIVE same-object edge is the Mode-B catch (around -> {NTPPi,TPPi} drops gold EC => collapse => abstain instead of committing wrong DC): 5/5 sound-violating spatial reads caught, 0 silent-wrong missed; kinship UNTESTED (0 unsound reads -- the catch holds trivially). This is a SUPPORTING subsection under the CLAIM 1 headline.

      ----- CLAIM 4 (SUPPORTING NEGATIVE, ONE SUBSECTION): CROSS-PATH CODING IS SYNTHETIC-CHANNEL-ONLY. TAG: REAL-LLM-READ + GOLD-ONLY-GATE + SYNTHETIC-CONTROL. -----
      The signature cross-path-intersection mechanism (multi-path redundancy as an error-correcting code over LLM reads) is established at power ONLY on synthetic channels, and FAILED on BOTH a-priori-gated real venues for OPPOSITE reasons: temporal Allen reads are near-universe (event-local underdetermined 0.87; intersection/best-single/naive all resolve 0/125; stronger deepseek-v3.2 MORE conservative at 0.99 -- not a weak-model artifact, art_0AIWMhwc1pJM), and spatial RCC-8 reads informatively (breadth 2.1/8, underdetermined 0.036) but its gold is a containment TREE (all 228 deduction queries have exactly one edge-disjoint path; the cardinal subgraph composes to a singleton on the best single path), so the corpus's 27.4% 'tight-multipath' flag was purely STRUCTURAL and the genuine redundancy is CROSS-algebra, not intersectable in one calculus (art_i53dBKgGY3Ig, a $0 gold-structural negative). Synthetic positive controls satisfying both conditions confirm the mechanism is real (Allen recall_95 selective accuracy 0.976 vs best-single 0.717, +0.259, CI [0.177,0.349]; RCC-8 0.890 vs 0.797). TEMPER (reviewer rigor, carried): present as 'two conditions -- informative sub-universal reads AND same-algebra structural redundancy -- each INDEPENDENTLY violated in the two real venues we could a-priori-gate, with synthetic controls confirming the mechanism when both hold' -- an EXPLANATORY ACCOUNT of two negatives, NOT a predictive law. Even where it works the realized cross-path COVERAGE bite is tiny (+0.024 over best-single, CI includes 0); the gain is precision-of-commitments (+0.259), not coverage. ONE honestly-bounded subsection, explicitly subordinate to the certificate headline; do NOT re-run RCC-8 (the negative is clean and needs no LLM).

      ----- CLAIM 5 (NATURAL TEMPORAL TEXT: certificate only WEAKLY protective; corrected statistics). TAG: REAL-LLM-READ. -----
      On natural temporal text the raw LLM OUT-ACCURACIES Mode-A at matched coverage (0.699 vs 0.575, gap -0.124); among ~19% Mode-A commits it is CONFIDENT-WRONG 42.5% (48/113), ALL silent-wrong-narrowing (gold omitted from a contributing read => confident wrong singleton with NO collapse, UNDETECTABLE at ~0.85 recall). The corrected FIXED-operating-point H1 CIs INCLUDE ZERO (vs PoT +0.027 [-0.088,0.140] p=0.33; vs SC +0.035 [-0.061,0.135] p=0.26; neither clears Holm; the earlier CONFIRM was a bootstrap artifact, art_Vc1UBGIVSi0T). State plainly: the natural-text temporal comparative advantage is MARGINAL and not robustly significant; the certificate's value there is the gold-free certificate + abstention-as-an-OPTION, bounded by read recall (end-to-end confident-wrong reduction 0.61->0.425 = 0.185, CI [0.087,0.280], read alongside Mode-A's 0.188 coverage vs raw 1.0). Read-soundness is the binding, CORPUS-SPECIFIC constraint (NarrativeTime stronger reader 0.932, CI [0.888,0.967] straddles the 0.90 gate; TDDMan below). A $0 synthetic backstop (recall 0.96) gives Mode-A +0.225 over raw, isolating read-soundness, not closure, as the gate. Supporting, not a headline.

      ----- CLAIM 6 (OPERATIONAL CASE STUDY, SUPPORTING, COMPRESSED; reviewer scope MINOR). TAG: REAL-LLM-READ. -----
      COMPRESS this section (its concatenated kinship arm and bracket-selected temporal arm add little beyond 'it runs') to buy space for the natural-corpus result (CLAIM 2). The first end-to-end ~3000-char run (art_WQoePKrpsTPo) is an OPERATIONAL CASE STUDY (per-document operating points, not a powered test): temporal arm = 5 NarrativeTime news articles BRACKET-selected around 3000 chars (NONE in [2500,3500]; mean 3050, range 2197-4293), kinship arm = 3 docs CONCATENATED from disjoint-entity CLUTRR sub-stories (cross-story pairs absent-by-construction => trivially abstained). 95 Prolog programs discharged AND executed in swipl 9.0.4; hallucination reduction vs whole-document raw 0.27-0.60 (mean 0.45) at Mode-A coverage 0-0.33 vs raw 1.0; atomic recall ~0.49 isolated as the binding ceiling. LABEL the documents bracket-selected/concatenation-constructed; keep as a short demonstration that the pipeline is operational at length and that EXTRACTION (not closure) is the ceiling.

      ----- CLAIM 7 (MECHANISM ANALYSIS / APPENDIX, DEMOTED). TAG: REAL-LLM-READ-ON-SYNTHETIC + SYNTHETIC-CHANNEL + THEOREM. -----
      Compress into a COMPACT half-page/APPENDIX, labeled inherited/synthetic/textbook: (7a) ALGEBRA-RICHNESS SCALING with real LLM reads on synthetic NL (point(3) +0.043 -> RCC-8(8) +0.448 -> Allen(13) +0.676; INHERITED table-vs-LLM-composition at recall ~1.0); (7b) the REDUNDANCY INVERTED-U on a realism-matched channel (Page p ~= 5e-4 corrected from the paper's mis-stated 1e-13; peak K* = 2,4,7,10,16 for recall 0.5->0.95; silent-wrong 0.006->0.146 bounded by (1-r)) with the small-bite caveat (+0.024 coverage); (7c) the ZERO-FP soundness THEOREM (all-sound contributing edges => gold in Mode-A output with probability 1.0; verified on 100,296 networks) -- a textbook PC invariant; recall and rho are INPUTS so it characterizes, not predicts a real-text operating point. None competes with the certificate headline.

      ----- CLARITY FIX (reviewer clarity MINOR): RE-DOCRED COUNTS PER-DATASET. -----
      State the per-dataset breakdown explicitly to remove the 360!=476 / 368!=577 apparent inconsistency: the re-docred PRIMARY slice is 360 present multi-hop queries (222 composed-only / non-circular) and 368 absent pairs; the 476/476 present and 577/577 absent engine round-trip is the COMBINED re-docred (360 present / 368 absent) + docred (116 present / 209 absent) verification (docred absent gold DOWNGRADED due to ~64.6% false-negatives; only the re-docred slice yields a defensible within-document absent label). One added clause removes the confusion.

      ----- METHOD CORE (unchanged in substance; re-scoped). -----
      MODE A (SOUND NARROWING / no-derivation abstention, PRIMARY, READ-SOUNDNESS-CONDITIONAL zero-FP). The local reader emits per span a high-recall sub-universal disjunction; composing+intersecting through the EXACT table either resolves a singleton (EMIT), leaves a disjunction (ABSTAIN), or finds NO derivation path (ABSTAIN 'no relation' -- the absent-relation behavior, conceded structural-by-construction on disconnected pairs). zero-FP survives PC incompleteness but is CONDITIONAL on every contributing read being sound. The cross-path-INTERSECTION variant is SYNTHETIC-ONLY-at-power (CLAIM 4); CLUTRR uses a union-fixpoint, not intersection.
      MODE B (DETECTION/REPAIR, SECONDARY). An empty closure certifies an UNSOUND read -- a gold-free, zero-FP DETECTION flag (conditional on recall) -- carrying the SILENT-WRONG-NARROWING dual (an unsound set OMITTING gold drives a confident WRONG singleton with no collapse; CLAIM 5's 42.5%). The fuzzy Mode-B catches (5/5 spatial) are the certificate's distinctive edge over a fair neural abstainer (CLAIM 3). Reiter-style minimal-hitting-set repair is future work.
      BASELINES: every certificate comparison includes the CONFIDENCE-THRESHOLDED RAW-ABSTAIN battery (verbalized + sc_margin + P(True) + semantic-entropy negentropy) thresholded to MATCHED coverage, alongside always-answer commit-the-argmax/raw-forced-single, PoT, and self-consistency. The claim is specifically that the confidence FAMILY is blind on the NO-DERIVATION/absent stratum.
      GENERALITY, TEMPERED. EXACT only on the convex point algebra (PC complete); Allen IA and RCC-8 are SOUND LOWER BOUNDS; CLUTRR kinship is a finite UNION composition table, NOT a relation algebra, NOT a cross-path-intersection venue.

      ----- HONESTY COMMITMENTS. -----
      (1) TAG every number THEOREM / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / REAL-LLM-READ / REAL-LLM-READ-ON-SYNTHETIC in TABLE COLUMNS. (2) Do NOT call CLUTRR natural -- it is TEMPLATED (<=871 chars, gold surface forms, hand-supplied table). (3) The certificate MECHANISM is the INHERITED NeSy premise (+0.673 inherited / +0.0025 novel); the NOVELTY is the EMPIRICAL ISOLATION (confidence-blindness), not the closure/abstention mechanism -- make the concession the framing. (4) The CLUTRR-absent abstention is STRUCTURAL-BY-CONSTRUCTION (disconnected components); the non-circular content is FACT A (47% high-confidence hallucination) + FACT B (confidence-blindness); the natural-corpus run is DECISIVE because there the extracted graph is not trivially correct. (5) Cross-path coding is SYNTHETIC-CHANNEL-ONLY -- one bounded negative subsection, an explanatory account of two gated-venue negatives, NOT a 'law'. (6) zero-FP is READ-SOUNDNESS-CONDITIONAL. (7) The fuzzy-unification certificate edge has a unit-of-analysis mismatch (query-level vs edge-read level); fix it with a query-level abstainer or lead with the 5/5 Mode-B catch; the kinship catch is untested (0 unsound reads). (8) Report every hallucination number WITH coverage/abstention. (9) SWI-Prolog execution reported truthfully (40/40 engine, 39/40 gold; 95 programs in the operational study). (10) DEDUCTION SUB-MODULE only -- OpenCyc grounding, atomic re-extraction, general fuzzy unification, and genuine ~3000-char natural professional documents are explicitly FUTURE WORK THIS PAPER DOES NOT CLAIM TO DELIVER; extraction-limited (~0.53 recall => ~19% coverage). (11) RE-TARGET venue to NeSy / temporal-and-qualitative-reasoning, with the deduction-sub-module scope stated in the FIRST paragraph of the abstract. (12) Include one worked Mode-A no-derivation abstention + one Mode-B collapse + a compact notation/metric table.

      SUCCESS / DISCONFIRM (re-centered on the empirical isolation + the natural-corpus run). CONFIRM if: (i) FACT A and FACT B reproduce on the natural Re-DocRED corpus and >=1 additional relation domain/reader (the raw LLM confidently hallucinates absent relations and the four-signal battery cannot filter them, crux-survival high) -- this is the corpus-robust DIAGNOSTIC contribution; AND (ii) the certificate beats the four-signal battery on the Re-DocRED MIXED pool at matched coverage with Holm-adjusted CIs excluding 0 (MET on CLUTRR + suggestive; the natural-corpus version is the iter-7 test), with the CLUTRR-absent structural-by-construction caveat stated; AND a SWI-Prolog-executed pipeline reports atomic P/R, multi-hop accuracy, trace-graphs, and abstention beside every hallucination number. DISCONFIRM / SCOPE-BOUNDARY (each publishable): FACT B fails (some confidence signal DOES filter confident absent hallucinations at matched coverage on a real venue => the empirical isolation is weaker than claimed -- an honest negative); OR the certificate ties/loses the Re-DocRED mixed-pool showdown because extraction recall is too low (=> certificate net utility is extraction-limited on natural text, while the DIAGNOSTIC FACT A+B survives); OR cross-path intersection never beats single-path on any real multi-path stratum at power (already observed on both gated venues => coding mechanism honestly synthetic-only).
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
  Same certificate frame; novelty reframed to confidence-blindness isolation; absent-win conceded by-construction.
_confidence_delta: unchanged
_key_changes:
- >-
  REFRAMED the headline novelty (reviewer novelty MAJOR) from 'the certificate mechanism' to an EMPIRICAL/DIAGNOSTIC contribution:
  the entire confidence/uncertainty family is structurally blind to confident absent-relation hallucination while a gold-free
  structural signal is not. Conceded up-front (as framing, not footnote) that compose-through-table + abstain-on-collapse
  is the inherited NeSy premise (+0.673 inherited / +0.0025 novel).
- >-
  ACCEPTED the structural-by-construction critique (reviewer rigor MAJOR): CLUTRR absent pairs are disconnected components,
  so the certificate's 2.8% confident-wrong on them is near-tautological; re-centered the load-bearing claim on the two NON-CIRCULAR
  facts — FACT A (raw LLM confidently hallucinates on 47.2% of absent pairs) and FACT B (the 4-signal battery cannot filter
  them, crux-survival 0.435/0.718/0.247/0.718).
- >-
  Made RUNNING STEP B the single decisive iter-7 experiment (reviewer evidence MAJOR): the four-signal fair-baseline on the
  already-built natural Re-DocRED present/absent pools at matched coverage (crux-survival + mixed-pool showdown + Holm-adjusted
  CW reductions), on a stronger reader, with a publishable honest fork. Tied this to the rigor critique: on natural prose
  the extracted graph is not trivially correct (imperfect extraction can over-abstain on present pairs), which makes the experiment
  DECISIVE not confirmatory.
- >-
  Added a SECOND-DOMAIN/READER generality requirement (reviewer novelty MAJOR-ii): confirm FACT A + FACT B on >=1 additional
  relation domain (spatial/temporal absent) or reader so confidence-blindness is shown not kinship-specific (cross-family
  deepseek already supplies reader diversity).
- >-
  Distinguished the corpus-robust DIAGNOSTIC contribution (FACT A + FACT B, properties of the raw LLM and signals) from the
  certificate's NET UTILITY (extraction-limited on natural text), so the contribution survives even if the natural-corpus
  mixed-pool win is gated by extraction recall.
- >-
  Fuzzy section (reviewer evidence MINOR): flagged the query-level vs edge-read unit-of-analysis mismatch in the 0.000-vs-0.415
  contrast; directed iter-7 to build a true query-level confidence abstainer OR downweight the section and lead with the 5/5
  Mode-B sound-violation catch.
- >-
  Scope (reviewer scope MINOR): moved the deduction-sub-module scoping (OpenCyc/general-fuzzy/atomic-re-extraction/3000-char-natural
  OUT, named as future work not claimed) to the FIRST paragraph of the abstract; directed compression of the bracket-selected/concatenation-constructed
  operational case study to buy space for the natural-corpus result.
- >-
  Clarity (reviewer clarity MINOR): added the per-dataset Re-DocRED breakdown — 360 present / 368 absent on the re-docred
  primary slice; 476/577 round-trip is the combined re-docred + docred verification — to remove the 360!=476 / 368!=577 apparent
  inconsistency.
- >-
  Confidence held unchanged: STEP A CONFIRM strengthens the diagnostic core, but the sharpened structural-by-construction
  rigor concern and the still-unrun natural-corpus experiment (the binding magnitude/locus gap) offset it; the path to clearing
  the bar is now cheap and well-specified.
relation_type: evolution
</hypothesis>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter7_dir1
type: experiment
objective: >-
  THE decisive iter-7 result (reviewer evidence MAJOR + the hypothesis CLAIM-2 open test): run the four-signal confidence/uncertainty
  fair-baseline against the closure certificate on the GENUINELY-NATURAL Re-DocRED Wikipedia present/absent kinship pools
  at matched coverage, reporting -- exactly as in the CLUTRR Section 6.1 -- the two NON-CIRCULAR facts (FACT A: raw-LLM high-confidence
  absent-relation hallucination rate; FACT B: crux-survival of those hallucinations under every signal), the mixed-pool selective-accuracy
  showdown, and Holm-adjusted confident-wrong reductions, with a publishable pre-registered FORK for the natural-prose extraction-limited
  regime. This moves the paper's load-bearing claim off templated data onto natural prose and is what converts the central
  contribution from asserted-by-structural-argument to MEASURED.
approach: >-
  INPUT = the built, gold-verified natural kinship corpus [ARTIFACT:art_NUWTxBVWENIJ] (formal dataset dependency; re-docred
  PRIMARY slice: 360 present multi-hop / 368 absent pairs over 575 family-bearing Wikipedia docs; top-level metadata.composition_table
  = CLUTRR finite kinship table verbatim; verified engine reproduces present + derives empty on absent). REUSE verbatim by
  reading the FROZEN WORKSPACES of two existing experiments directly via filesystem (they cannot be formal experiment->experiment
  deps): the four-signal battery builder + matched-coverage / crux-survival / mixed-pool / Holm statistics from the CLUTRR
  battery experiment art_LeRQRGHJZcdQ at /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_experiment_1
  (signals (a) verbalized confidence, (b) self-consistency vote-margin@k=10, (c) Kadavath P(True), (d) semantic-entropy negentropy
  over k=10 relation-clustered samples; story/doc-clustered paired bootstrap B=10000, Holm/4; cache/ for warm reruns); and
  the kinship forward-union least-fixpoint closure engine + readers + risk-coverage harness + Prolog discharge from the CLUTRR
  pipeline art_0a7i481ZRwS1 at /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
  (kinship.py, readers.py, baselines.py, stats.py, prolog.py). PIPELINE: (1) span-local atomic kinship reads of each natural
  Wikipedia doc via OpenRouter -- PRIMARY google/gemini-3.1-flash-lite (temp 0) AND cross-family deepseek/deepseek-v3.2 BOTH
  run full as the reader-diversity generality evidence (reviewer novelty MAJOR-ii), with an OPTIONAL stronger google/gemini-3-flash-preview
  on a stratified subsample only if budget allows; SHA-256 disk cache + hard $9 cost-guard; gradual mini->full scaling. Atomic
  edges -> forward-union closure recovers each held-out PRESENT query / derives empty on ABSENT pairs -> certificate EMITs
  singleton / ABSTAINs on disjunction / ABSTAINs 'no relation' on no-derivation. (2) For the RAW-LLM answerer build the four
  confidence-thresholded raw-abstain baselines, sweeping tau to MATCH the certificate's coverage on the absent stratum, the
  present stratum, AND the mixed pool. REPORT (mirror CLUTRR Section 6.1; every number tagged REAL-LLM-READ and tagged NATURAL-PROSE
  vs templated): (i) FACT A -- raw-LLM confident-wrong hallucination rate on the 368 NATURAL absent pairs + confidence distribution,
  both readers; (ii) FACT B -- crux-survival table: fraction of absent hallucinations surviving each signal's certificate-matched
  rule, both readers; (iii) the DECISIVE mixed present/absent pool selective-accuracy showdown at matched coverage (certificate
  vs each signal) so abstain-on-everything cannot win; (iv) Holm-adjusted confident-wrong reductions with clustered-bootstrap
  CIs. CRITICAL DECISIVE NUANCE (ties to reviewer rigor MAJOR): on natural prose the extracted graph is NO LONGER trivially
  correct -- measure natural-prose atomic kinship P/R/F1 (expected below CLUTRR's 0.53), and explicitly DECOMPOSE certificate
  abstentions into (correct) absent-pair abstentions vs (over-abstention) present-pair extraction-failure abstentions, then
  measure whether the certificate STILL answers present pairs (coverage + selective accuracy) while abstaining on absent ones
  in the MIXED regime. PRE-REGISTERED FORK, both publishable: IF certificate beats the four-signal battery on the Re-DocRED
  MIXED pool at matched coverage with Holm-adjusted CIs excluding 0 -> flag NEW HEADLINE (CLUTRR -> templated companion);
  IF natural-prose recall is so low the certificate over-abstains and TIES/LOSES -> report HONESTLY as the extraction-limited
  boundary WHILE preserving the corpus-robust DIAGNOSTIC (FACT A + FACT B survive regardless, being properties of the raw
  LLM + signals, not the certificate). Use the confidence-family signal specs + reader recommendations pinned in the research
  dependency [ARTIFACT:art_dA_3iFe_7fn_]. OUTPUT method_out.json (aii exp_gen_sol_out, schema-validated; full/mini/preview)
  grouping per-query rows into redocred_present / redocred_absent / mixed pools with predict_certificate / predict_ct_<signal>
  / predict_raw / gold + per-signal confidences + metadata_stratum / metadata_is_absent / metadata_reader; the FACT-A table,
  FACT-B crux-survival table, mixed-pool leaderboard with Holm CIs, the abstention decomposition (correct-absent vs over-abstain-present),
  natural-prose atomic P/R, cross-reader comparison, cost ledger, and an explicit CONFIRM-HEADLINE / EXTRACTION-LIMITED-BOUNDARY
  verdict per the FORK; include one worked Mode-A no-derivation abstention trace + one over-abstention-on-present trace, Prolog-discharged
  if swipl available else python-checked truthfully.
depends_on:
- id: art_NUWTxBVWENIJ
  label: dataset
  relation_type:
  relation_rationale:
- id: art_dA_3iFe_7fn_
  label: methodology
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

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
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
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
out_expected_files:
- research_out.json
out_dependency_files:
  file_list:
  - research_out.json
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

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
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
  "description": "Plan for an EXPERIMENT artifact.",
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
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-18 02:14:15 UTC

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
