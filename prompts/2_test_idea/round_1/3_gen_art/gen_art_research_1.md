# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 13:39:13 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
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
id: gen_plan_research_1_idx1
type: research
title: >-
  Implementation/Resource Dossier for the Closure-Certified Text-to-Logic Deduction Module
summary: >-
  A web-research plan producing a single structured dossier that resolves every implementation/resource decision the dataset,
  experiment, and evaluation executors need: exact access + parse specs for the three temporal corpora (NarrativeTime/TimeBankNT,
  TDDMan, MATRES), machine-readable composition tables (Allen IA, convex point algebra, RCC-8) with the exact non-convex->VAGUE
  widening rule, the Mackworth PC-2 iterated-fixpoint spec and the naive single-pass-intersection variant plus tractability
  facts, the Renz-Nebel A(n,d,l) random consistent QCN generator with independently controllable redundancy/density/hop/cyclomatic
  knobs, baseline specs each with a matched abstention signal, the cheapest capable OpenRouter model + caching strategy to
  stay well under $10, and an operationalization of the extended realism-matching statistic. Delivered as a decision table
  + gotchas list with exact URLs, repo paths, and citations.
runpod_compute_profile: cpu_light
question: >-
  What are the exact, verified implementation specifications and resources (corpus access/formats, composition tables, path-consistency
  algorithm, synthetic QCN generator, baseline configs, OpenRouter model/caching, and realism-matching statistic) required
  to build the closure-certified deduction module, so the downstream dataset/experiment/evaluation executors can implement
  from specifications rather than guesses?
research_plan: |-
  GOAL: Produce ONE structured dossier (research_out.json + research_report.md) that an executor with NO further research access could implement the whole pipeline from. Every claim must carry an exact URL / repo path / arXiv ID. Where a resource cannot be verified, say so explicitly and give the best fallback. Organize the report into the 8 SECTIONS below (7 topics from the direction + a decision table + gotchas). Use the aii-web-tools skill: search -> fetch (understand) -> fetch_grep (extract exact numbers/tables/formats). Parallelize independent searches.

  ==================================================
  SECTION 1 -- CORPORA ACCESS + PARSE FORMAT (highest priority; gates T0 and all real-text arms)
  ==================================================
  Deliver, PER CORPUS: (a) canonical download URL (GitHub/LDC/anthology), (b) license + whether the underlying TimeBank source text is needed and how to obtain it, (c) exact on-disk file format with column/field semantics, (d) how to recover {event nodes, gold relation edges, per-pair sentence distance/locality, document grouping}, (e) the relation label inventory and its mapping to an algebra, (f) any known parsing gotcha.

  1A. NarrativeTime / TimeBankNT (DENSE CO-PRIMARY). Already confirmed: ACL Anthology https://aclanthology.org/2024.lrec-main.1054/ ; arXiv:1908.11443 (PDF https://arxiv.org/pdf/1908.11443 ); authors Rogers, Karpinska, Gupta, Lialin, Smelkov, Rumshisky; full re-annotation of TimeBank-Dense, IAA Krippendorff alpha ~0.68, timeline-based with full TLink coverage, ships TimeML-conversion tools. ACTION: (i) fetch_grep the arXiv PDF and the ACL anthology page for the strings 'github', 'github.com', 'code', 'available at', 'release', 'http' to recover the repository/data URL (the search engine did not surface it; it is almost certainly stated in the paper's footnote/abstract/resources section). (ii) Also try a direct GitHub search via web search for 'NarrativeTime' under the authors' handles (annargrs / Anna Rogers, Vladislav Lialin, Marzena Karpinska, text-machine-lab UMass Lowell -- Rumshisky's lab is 'text-machine-lab'); fetch the candidate repo's README and report the directory layout (annotation files, TimeML XML, conversion scripts). (iii) Document the TIMELINE -> START-POINT extraction path: NarrativeTime places events on a timeline, so each event has a start (and end) coordinate; the convex point-algebra arm uses START-POINTS. Confirm from the paper how timeline coordinates are stored (integer time-slots? intervals?) and how to derive a pairwise gold point relation (<, =, >) between two events' start points. Cross-reference TLEX (arXiv:2406.05265, 'TLEX: Extracting Exact Timelines from TimeML Temporal Graphs') as a worked example of TimeML-graph->timeline extraction and report whether its method/code is reusable for deriving start-point orderings. (iv) Record how full-interval Allen relations are recoverable (start+end points) for the 'lower-bound detector' arm. FALLBACK if no repo is found: report that the dataset may require emailing authors / using the TimeML conversion on TimeBank-Dense source, and flag this as a procurement risk for the dataset executor.

  1B. TDDMan / TDDiscourse (NON-CIRCULARITY ANCHOR). Confirmed: GitHub https://github.com/aakanksha19/TDDiscourse , subfolder TDDMan/ with TDDManTrain.tsv / TDDManDev.tsv / TDDManTest.tsv (anthology W19-5929 https://aclanthology.org/W19-5929/ ). ACTION: (i) fetch the repo README and one TSV (e.g. https://github.com/aakanksha19/TDDiscourse/blob/master/TDDMan/TDDManDev.tsv via the raw URL https://raw.githubusercontent.com/aakanksha19/TDDiscourse/master/TDDMan/TDDManDev.tsv ) and report the EXACT columns. Expected: (event1_id, event2_id, relation) where event ids are TimeBank EIIDs/event-instance ids referencing TimeBank documents -- CONFIRM this and state explicitly that TDDiscourse ships only (eventpair, label) triples and that the RAW TEXT + event offsets must be joined from the original TimeBank-Dense / TimeBank 1.2 (timeml.github.io) corpus. Document how to obtain TimeBank source (TimeML site / LDC TimeBank 1.2) and how event ids map to text spans. (ii) Confirm the label set {before, after, simultaneous, includes, is_included}, mutually exclusive, NO vague. (iii) Map this 5-relation coarse set onto an interval algebra: before/after = Allen b/bi; includes/is_included = Allen di/d (or contains/during); simultaneous = equals (or a coarse 'same-extent' set). Report the exact coarse-interval composition implied and whether GQR's allen table can be restricted to these. (iv) Confirm 'long-distance / >1 sentence apart / cannot be inferred automatically from existing annotations' claim from the paper (fetch_grep W19-5929 PDF for 'cannot be inferred', 'automatically', 'sentence apart'). (v) Note TDDAuto exists (auto-derived) and is NOT to be used for the non-circularity arm -- only TDDMan (manual).

  1C. MATRES (GATE-VALIDATION CONTROL). Ning, Wu & Roth 2018, ACL, 'A Multi-Axis Annotation Scheme for Event Temporal Relations'. ACTION: (i) find the official repo (CogComp -- github.com/CogComp/MATRES or qatemp; search 'MATRES temporal CogComp github'). (ii) Confirm label set {before, after, equal, vague} and the multi-axis design; confirm annotation is restricted to events in the SAME or ADJACENT sentences (fetch_grep the paper for 'same sentence', 'adjacent', 'window', 'consecutive') -- this is the structural reason its deduction-required envelope is ~empty (T0 N* ~ 0), so VERIFY the locality claim precisely (e.g. 'within a window of N sentences'). (iii) Report file format (typically TSV: docid, token offsets, e1, e2, relation) and that source text is TempEval-3 / TimeBank+AQUAINT (TBAQ) platinum.

  For ALL THREE: produce a small comparison sub-table {corpus | #docs | #event-pairs (gold edges) | label set | algebra | locality (same/adj/long) | density | gold provenance (human-timeline vs manual-pair vs adjacent) | source-text procurement | parse entrypoint file}.

  ==================================================
  SECTION 2 -- EXACT COMPOSITION TABLES (Allen IA, convex point algebra, RCC-8)
  ==================================================
  The single most reusable deliverable: machine-readable tables the algebra executor can load verbatim. PRIMARY SOURCE = GQR (confirmed github.com/m-westphal/gqr ; data/ dir contains allen/ point/ rcc8/ with .spec files and .combination composition tables; also point-branching, rcc5, rcc23). ACTION:
  2A. Fetch the RAW GQR spec + combination files and report their EXACT grammar so the executor can parse them: (i) https://raw.githubusercontent.com/m-westphal/gqr/master/data/allen/allen.spec and the Allen composition file in data/allen/ (look for allen.comp / allen+allen.combination -- list the actual filenames by fetching https://github.com/m-westphal/gqr/tree/master/data/allen ). (ii) Same for data/point/ (point.spec + point composition) and data/rcc8/ (rcc8.spec + rcc8 composition). Report: how base relations are named (Allen: eq, b, bi, m, mi, o, oi, d, di, s, si, f, fi -- CONFIRM GQR's exact tokens), how converse is encoded, how composition is encoded (line format: 'rel1 rel2 : {result-set}'), and identity. Provide a short verbatim excerpt of each file (5-10 lines) so the executor sees the literal syntax.
  2B. Cross-check the Allen 13x13 composition table against an independent authoritative source so a parse bug is catchable: Allen 1983 CACM 'Maintaining Knowledge about Temporal Intervals' (Table); the Wikipedia 'Allen's interval algebra' composition table; and the Thomas Alspaugh reference table (search 'Allen interval algebra composition table Alspaugh'). Report at least 3-4 canonical cells (e.g. b.b=b ; b.d={b,o,m,d,s} ; o.o={b,o,m} ; d.di=full) so the executor can unit-test its loaded table. State that converses and identity must be SEEDED FROM THE ALGEBRA, never from an LLM.
  2C. CONVEX POINT ALGEBRA (NarrativeTime start-point arm) -- the completeness-critical detail. Document: base point relations {<, =, >}; the full PA relation lattice (subsets): {}, {<}, {=}, {>}, {<,=}=<=, {=,>}=>=, {<,>}=!=, {<,=,>}=? (universal). CONVEX relations = those whose point-set is an interval on the order: <, =, >, <=, >=, ? (i.e. ALL subsets EXCEPT the non-convex {<,>}=!=). STATE THE WIDENING RULE EXPLICITLY: the ONLY non-convex relation is != ({<,>}); to keep PC complete, any emitted/derived != is WIDENED to ? (universal/VAGUE), and the bite lost by this widening must be measured. Cite the tractability result: PC is COMPLETE (decides consistency) for the convex point algebra / pointizable / ORD-Horn classes (Vilain & Kautz 1986 'Constraint Propagation Algorithms for Temporal Reasoning'; van Beek & Cohen; Nebel & Burckert 1995 ORD-Horn JACM 42(1)). Provide the point-algebra composition table (9 cells over {<,=,>} composing, extended to subsets by union) -- verify against GQR point.spec.
  2D. RCC-8 (second algebra, Tier-2). Confirm the 8 base relations {DC, EC, PO, EQ, TPP, NTPP, TPPi, NTPPi} and that GQR ships the rcc8 composition table; note RCC-8 consistency is NP-complete in general but PC is complete for the maximal tractable subclasses (Renz & Nebel H8 / the three maximal tractable subsets). One canonical composition cell for unit-testing.
  DELIVERABLE: for each algebra, a pointer to the verbatim GQR file + parse grammar + 3-4 unit-test cells + the widening rule (point algebra). If GQR files are unreachable, fall back to the QAT / SparQ (qsr.informatik.uni-freiburg.de) distributions or the Wikipedia/Alspaugh tables, and say which was used.

  ==================================================
  SECTION 3 -- PATH-CONSISTENCY SPEC + THE NAIVE-INTERSECTION CONTRAST + TRACTABILITY
  ==================================================
  3A. FULL ITERATED PC: specify Mackworth (1977) PC-2 and the standard van Beek queue-based path-consistency used for QCNs: initialize edge(i,j) to the LLM-read set (query/held-out edge = universal); for every triple (i,k,j) refine R_ij <- R_ij INTERSECT (R_ik COMPOSE R_kj); re-queue affected edges until FIXPOINT or some R_ij = {} (empty => inconsistency certificate, Mode B). Seed converses (R_ji = converse(R_ij)) and identity (R_ii = {eq}/{=}) FROM THE ALGEBRA. Report pseudocode-level detail (the exact triple-update + queue rule) and cite a clean reference (Renz & Nebel survey arXiv:1606.00133 'A Survey of Qualitative Spatial and Temporal Calculi'; or the GQR paper). Confirm closure runs in milliseconds on small networks (O(n^3) per pass, n = #events in a document/sub-network, small).
  3B. NAIVE SINGLE-PASS INTERSECTION (the iteration-isolation baseline, H3): define it precisely as -- at the QUERY pair only, intersect the compositions arriving along each identified path in a SINGLE pass, WITHOUT iterating to a fixpoint and WITHOUT algebra-seeded converse propagation (i.e. 'Path-of-Thoughts + one obvious intersection step'). Document the theorem the claim rests on: on LENGTH-2 (single intermediate node) acyclic multi-path queries, naive single-pass intersection == full PC (so Mode A ties naive on the length-2 stratum); divergence requires path length >=3 and/or cycles (cyclomatic number >=1) where re-propagation tightens upstream edges. State how to compute hop-count and cyclomatic number (m - n + c on the constraint subgraph) for stratification.
  3C. TRACTABILITY FACTS to report crisply (for the honesty/scope claims): PC is SOUND for all these algebras; PC is COMPLETE (decides consistency) ONLY for convex point algebra and ORD-Horn (point) and the maximal tractable subclasses of RCC-8/Allen; FULL Allen IA consistency and full RCC-8 consistency are NP-complete (Vilain-Kautz; Nebel-Burckert ORD-Horn; Renz-Nebel). Consequence to state: closure-detectable hallucination rate is a LOWER BOUND on full Allen/RCC-8, EXACT on the NarrativeTime convex-point-algebra arm. Provide the citations with arXiv/DOI.
  3D. REPAIR (Mode B, Tier-2): point to Reiter (1987) 'A Theory of Diagnosis from First Principles' for minimal-hitting-set diagnosis and note a MaxSAT/hitting-set formulation over the conflict (empty-collapse) set, preferring retraction of lowest-confidence edges. Just enough for the executor to know the algorithm name + reference; no implementation.

  ==================================================
  SECTION 4 -- RENZ-NEBEL RANDOM CONSISTENT QCN GENERATOR A(n,d,l)
  ==================================================
  Deliver the generative recipe so the experiment executor can produce synthetic networks with INDEPENDENTLY controllable redundancy / density / hop-count / cyclomatic number, AT GUARANTEED-CONSISTENT ground truth (needed so 'gold' is well-defined). ACTION: (i) Identify the canonical model: Renz & Nebel's random instance model, usually written A(n, d, l) = n nodes, average degree d (controls density/redundancy), label-size parameter l (average #base relations per constraint). Fetch the Renz & Nebel 'Efficient Methods for Qualitative Spatial Reasoning' (JAIR / arXiv:1106.0679) and fetch_grep for 'A(n', 'average degree', 'random', 'phase transition' to extract the EXACT parameter definitions and the typical hard-region (phase transition d ~ 8-10). (ii) CRITICAL DISTINCTION to document: the standard A(n,d,l) generates random (possibly inconsistent) networks; the experiment needs CONSISTENT ground truth. Specify the standard recipe for generating a RANDOM CONSISTENT network with KNOWN solution: draw a random scenario (assign each node a concrete interval/point => a single base relation per pair = the gold atomic graph), then OPTIONALLY weaken some edges to larger sound sets to create the 'LLM-read' inputs; the gold pairwise relation between any two nodes is read off the concrete realization. Document this 'random scenario then qualitative-abstraction' approach (this is how to GUARANTEE consistency + recover gold for held-out edges). (iii) Map the four control knobs to generator parameters: density/redundancy <- d (average degree) and #independent paths between a query pair; hop-count <- graph diameter / shortest constraining path length (control by building layered/chain structures); cyclomatic number <- m-n+c (control by adding chords/cycles); per-edge recall/breadth <- the abstraction step (how many extra base relations are unioned onto the gold). Recommend >=500 networks/cell and >=4 fixed per-edge-recall levels (from the success criteria). (iv) Note GQR ships a generator and SparQ has random-network tooling; report whether a ready Python QCN generator exists (search 'qualitative constraint network random generator python', and check whether libraries like 'pyRCC8' / 'allen interval python' exist) -- if not, the executor will implement the scenario-based generator from the recipe above, so make the recipe self-contained.

  ==================================================
  SECTION 5 -- BASELINE SPECS, EACH WITH A MATCHED ABSTENTION SIGNAL
  ==================================================
  For EACH baseline deliver: {what it does, the exact paper/repo, the abstention/confidence signal to threshold to the SAME coverage object (single-relation resolution), and any prompt/algorithm detail}. The coverage object is identical for all: a method 'answers' a query pair iff it commits to a single relation; threshold each method's confidence so all report at MATCHED coverage.
  5A. Path-of-Thoughts (PRIMARY real-text baseline) -- arXiv:2412.17963 (confirmed: graph extraction -> path identification -> per-path INDEPENDENT reasoning). fetch_grep the HTML (https://arxiv.org/html/2412.17963 ) to CONFIRM and quote: (i) that each reasoning path is reasoned INDEPENDENTLY by an external reasoner, (ii) that it does NOT intersect relations across paths / does NOT detect cross-path contradictions, (iii) what it does when paths DISAGREE (outputs multiple relations, does not abstain). Matched abstention signal = PATH-AGREEMENT (answer only if all/most paths agree on one relation). Check for an official repo (search 'Path-of-Thoughts github').
  5B. Self-consistency voting -- abstention signal = VOTE MARGIN over k sampled single-relation answers; threshold the margin. (Wang et al. self-consistency, arXiv:2203.11171, for the citation.)
  5C. LINC -- arXiv:2310.15164 (Olausson 2023): multiple formalizations -> solver -> MAJORITY VOTE of answers. Abstention signal = vote agreement across formalizations. Note its limitation to state: answer-level voting cannot see that individually-popular composition steps are JOINTLY inconsistent. Repo: github.com/benlipkin/linc (verify).
  5D. DSR-LM / 'LLMs can Learn Rules' -- arXiv:2305.03742 (Yang 2023) and arXiv:2310.07064 (Zhu 2023): induce weighted/symbolic composition rules, Prolog/Scallop reasoning, NO closure. Report what to reuse (induced-rule Prolog answer + its confidence as abstention signal). Note the table-held-fixed ablation isolates PC from 'a fixed consistent table exists'.
  5E. TempRel COMMIT baseline via ILP -- arXiv:2502.11114 (EMNLP 2025 global zero-shot temporal graph: LLM generates whole graph, aggregate M=5, enforce uniqueness/symmetry/transitivity by ILP) and Knez & Sun arXiv:2406.11486 (zero-shot LLMs assign >1 relation for >=50% up to 97% of pairs; ILP consistency does NOT improve F1). fetch_grep both for the exact numbers (M=5; the >=50%/97% figures; 'does not improve F1') -- these anchor the motivation. This baseline COMMITS to one label/pair (no disjunction, no abstention); its 'confidence' = the ILP-committed label's score.
  5F. METRE (alternative edge-reader, Tier-2) -- arXiv:2408.07353 (Hu, Huang & Feng 2024): TRAINED multi-LABEL classifier predicting possibility of each temporal relation independently; treats VAGUE as >1 possible relation; on TB-Dense/MATRES/UDS-T. Report: is there a repo / checkpoint to reuse, or must it be approximated? Document that it is F1-trained (not recall-oriented) so for the reader-agnosticity test its threshold must be tuned to MATCHED per-edge recall and its measured cross-edge error correlation rho reported.
  5G. (mention only, for completeness) raw LLM (verbalized confidence), CoT, a soft-unification neural theorem prover (e.g. NTP/CTP) -- give one citation each; these are lower-priority.

  ==================================================
  SECTION 6 -- OPENROUTER MODEL CHOICE + CACHING (stay well under $10)
  ==================================================
  Deliver a concrete recommendation. Constraints: short docs (~3000 chars), per-edge disjunctive relation reading (small structured output), thousands of calls across corpora x frontier-sweep x baselines. ACTION: (i) Use the aii-openrouter-llms skill knowledge + fetch https://openrouter.ai/models (and the pricing guide pages) to list the CHEAPEST CAPABLE models with reliable structured/JSON output: candidates -- google/gemini-2.5-flash-lite (or current Flash-Lite), google/gemini-2.0-flash, deepseek/deepseek-chat (V3), meta-llama/llama-3.3-70b-instruct, qwen/qwen-2.5-72b-instruct, and any strong FREE-tier (:free) models (note free-tier rate limits + data-retention caveats). Report per-model input/output $/Mtok and note the ':floor' suffix routes to cheapest provider. (ii) Recommend a PRIMARY (cheap, capable, structured-output-reliable -- likely a Gemini Flash-Lite or DeepSeek-V3 class) and a SECOND, DIFFERENT-FAMILY model for the reader-agnosticity arm (different vendor to get genuinely different error correlation rho). (iii) COST BUDGET: estimate tokens/call (~1k in + ~0.3k out), multiply by expected #calls, show the arithmetic demonstrating << $10; recommend reserving the bulk of calls for T1/T2 after T0 (T0 is zero-LLM-spend). (iv) CACHING strategy: (a) deterministic prompt+model -> response cache keyed by hash of (doc_span, prompt_template, model, temperature=0) stored on disk so reruns cost $0; (b) batch per-document edge reads to reuse the document context; (c) note OpenRouter / provider prompt-caching for repeated document prefixes if available. (v) State: all LLM calls go through OpenRouter only (no direct OpenAI/Anthropic), and a hard cumulative-cost tracker stopping before $10.

  ==================================================
  SECTION 7 -- OPERATIONALIZE THE EXTENDED REALISM-MATCHING STATISTIC
  ==================================================
  The synthetic NL-realization must be VALIDATED to resemble real corpus reads before the redundancy curve is trusted. Specify EXACTLY how to compute the three-part statistic + thresholds. (i) PER-EDGE ERROR-TYPE DISTRIBUTION + TOTAL-VARIATION DISTANCE: define the error-type categories for a read edge vs gold (e.g. SOUND-tight, SOUND-loose/under-specified, OVER-COMMITTED/unsound-omits-gold, exact-correct); estimate the categorical distribution on REAL corpus reads and on SYNTHETIC reads; TV distance = 0.5 * sum_k |p_real(k) - p_synth(k)|; recommend a pre-registered threshold (e.g. TV <= 0.1). (ii) CROSS-EDGE ERROR-CORRELATION rho MATCH: define rho = within-document correlation of the soundness indicator across edges (e.g. Pearson/phi between per-edge 'is-sound' indicators of edge pairs sharing a document, or an intraclass correlation); require |rho_real - rho_synth| below a fixed bound. (iii) REDUNDANCY/TOPOLOGY HISTOGRAM MATCH: histograms of contributing-edge-count per query and of cycle-structure (cyclomatic number) for real vs synthetic; match via a histogram distance (TV or chi-square) below a fixed bound. Report standard estimators (numpy/scipy) and that ALL thresholds are FIXED BEFORE generating the redundancy curve. Also define J(E) (empirical joint soundness = realized fraction of E-edge subnetworks where ALL edges sound) and how rho makes J(E) decay slower than r^E -- these are computed from the same per-edge soundness indicators.

  ==================================================
  SECTION 8 -- DECISION TABLE + GOTCHAS (synthesis)
  ==================================================
  Close with: (A) a DECISION TABLE -- rows = {corpus to host headline (recommend NarrativeTime, corroborate TDDMan, control MATRES), primary algebra per corpus, composition-table source file, PC algorithm, naive-baseline definition, synthetic generator recipe, primary OpenRouter model, second-family reader model, realism thresholds}; columns = {decision | chosen value | source URL/citation | confidence | fallback}. (B) GOTCHAS list, e.g.: TDDiscourse ships only (pair,label) triples -> must join raw text + event offsets from TimeBank source; NarrativeTime repo URL must be dug from the PDF; convex point algebra requires widening the ONLY non-convex relation != to universal (measure bite lost); converses/identity must be algebra-seeded NEVER LLM-read; full Allen/RCC-8 PC is sound-but-INCOMPLETE (lower-bound), point-algebra arm is EXACT; naive==full on length-2 is a PREDICTION not a bug; T0 is zero-LLM-spend and runs first; METRE is F1-trained so match recall + report rho; free-tier OpenRouter models have rate-limit/retention caveats. (C) FOLLOW-UP QUESTIONS the executor could not fully resolve (e.g. exact NarrativeTime timeline coordinate schema; whether a METRE checkpoint is downloadable).

  OUTPUT FORMAT: research_out.json {answer: full dossier text; sources: [{title,url} for EVERY cited resource -- corpora repos, GQR, all arXiv IDs, OpenRouter pricing]; follow_up_questions: the Section 8C list}. PLUS research_report.md mirroring Sections 1-8 with the decision table and verbatim file-format excerpts. Cite an exact URL or arXiv ID for every factual claim; explicitly flag anything unverified rather than guessing.
explanation: >-
  This is the foundational research artifact (depends_on: []) for the entire iter-1 investigation: the dataset, experiment,
  and evaluation executors all consume its specifications. The hypothesis is unusually implementation-dense -- it stands or
  falls on getting EXACT resources right: the wrong corpus (MATRES, whose deduction-required envelope is empty by construction)
  already sank the prior iteration, so verifying NarrativeTime/TimeBankNT access and its timeline->start-point->convex-point-algebra
  path is mission-critical and gating. The composition tables (Allen/point/RCC-8) must be byte-exact and algebra-seeded, because
  the whole zero-false-positive narrowing guarantee (Mode A) and the soundness/completeness honesty claims depend on the table
  being mathematical ground truth, not LLM-supplied. The path-consistency spec plus the precisely-defined naive-single-pass-intersection
  contrast is what isolates the ITERATION claim (H3) from 'any intersection.' The Renz-Nebel generator recipe is what lets
  the synthetic arm independently sweep redundancy/density/hop/cyclomatic to locate the inverted-U redundancy optimum (H4).
  The baseline specs with matched abstention signals are required for the matched-coverage selective-accuracy comparison (H1)
  to be fair. The OpenRouter model + caching decision keeps the run feasible under the hard $10 cap. And operationalizing
  the realism-matching statistic is what makes the synthetic redundancy curve credible enough to anchor a headline. Delivering
  all of this as a verified decision table + gotchas list means the downstream executors implement from specifications rather
  than guesses -- the difference between a clean execution and a wasted iteration. Pure web research, no code execution, so
  cpu_light suffices.
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

### [2] HUMAN-USER prompt · 2026-06-17 13:39:13 UTC

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

### [3] SKILL-INPUT — aii-web-tools · 2026-06-17 13:39:25 UTC

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
