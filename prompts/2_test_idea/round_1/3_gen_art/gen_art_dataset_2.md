# gen_art_dataset_2 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_2` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 13:39:23 UTC

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

<task>
Find, evaluate, and prepare high-quality datasets for the research experiment.
Adapt your search strategy based on the hypothesis and domain requirements.
</task>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. MUST check for and avoid each one.

**1. Picking Obscure or Unusable Datasets**
Do NOT select datasets just because they match a keyword. Red flags: very few downloads (<100), no documentation (dataset card, paper, or GitHub page). Prefer well-used datasets (not necessarily popular or widely known) with clear documentation.
CHECK: >100 downloads? Has documentation? If any "no" → find a better dataset.

**2. Fabricating Dataset Provenance**
Do NOT invent justifications for why a dataset is relevant. If a dataset name contains a number (e.g., "797"), do NOT assume it refers to a specific benchmark suite, OpenML ID, or paper without verification. In past runs, an agent assumed "797" referred to "OpenML benchmark suite 797" with zero evidence, then fabricated a rationale. This was completely false.
CHECK: Can you cite a specific, verifiable source (paper, benchmark page, dataset card) confirming this dataset is what you claim? If not, do not make provenance claims.

**3. Not Verifying Dataset Usefulness**
Always sanity-check that a dataset is actually suitable for the task before committing. Download a sample, inspect the features, and run a quick baseline appropriate for the domain. If the dataset lacks signal or structure for the hypothesis being tested, the entire experiment is wasted.

**4. Settling for the Only Search Result**
If your search returns only 1-2 results, your search terms are too narrow. Broaden your queries, try different keyword combinations, or search for well-known benchmark datasets in the domain. A single obscure result from a narrow query should never be your final choice.
CHECK: Fewer than 5 candidate datasets? Run additional searches with broader or different terms before making a selection.
</common_mistakes_to_avoid>

<critical_requirements>
- Keep final response under 300 characters
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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/results/out.json`
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
id: gen_plan_dataset_2_idx3
type: dataset
title: >-
  Synthetic QCN Backbone: Controlled Consistent Qualitative Constraint Networks (Allen / Convex-Point / RCC-8) with NL Realizations
summary: >-
  Generate the clean-ground-truth synthetic corpus for the redundancy (H4) and iteration (H3) claims: random CONSISTENT qualitative
  constraint networks over three relation algebras (Allen interval, convex point, RCC-8) built by model-based realization
  (so the gold atomic scenario is globally consistent and the gold relation on every edge is known), with controlled query
  topology that sweeps redundancy (number of constraining paths), hop-count, cyclomatic number and node count, >=500 networks
  per cell. Each network ships TWO views: an abstract graph (for simulated-reader experiments) and a template NL realization
  (so an LLM reader can later be run on synthetic text). Records gold graph, held-out query edge, enumerated constraining
  paths, contributing-edge counts and cycle structure, plus PRE-REGISTERED (recorded, not yet validated) realism-matching
  thresholds. Schema-valid via aii-json, full/mini/preview splits, <=300MB.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  PURELY SYNTHETIC AND THAT IS CORRECT HERE: this artifact is the clean-ground-truth backbone whose entire value is INDEPENDENTLY
  controlling structural parameters (redundancy, hop-count, cyclomatic number, density, node count) that no real corpus exposes.
  The real-text corpora (NarrativeTime, TDDMan, MATRES) are delivered by SIBLING dataset artifacts; do NOT duplicate them
  here. Prefer-real does not apply: a controlled QCN sweep cannot be found, only generated. Ideal properties: (1) GROUND TRUTH
  IS EXACT AND CONSISTENT BY CONSTRUCTION -- every network is a realizable model (points/intervals/discs), so the gold atomic
  relation on each edge is read off the model and the whole scenario is globally consistent (no solver needed to certify consistency).
  (2) THREE ALGEBRAS: Allen interval algebra (13 base relations) and convex point algebra (base {<,=,>}) as PRIMARY (full
  grid, >=500/cell); RCC-8 (8 base relations) as the SECONDARY second-algebra arm (>=500/cell where size permits, else >=300/cell).
  (3) DEDUCTION-REQUIRED QUERY STRUCTURE: each network has a designated held-out query pair (s,t) whose two endpoints share
  NO direct edge and never co-occur in a single verbalized sentence, so the query relation is obtainable only by composing
  >=1 multi-edge path -- the structural analogue of the real-corpus 'deduction-required' subset. (4) INDEPENDENTLY SWEPT STRUCTURE:
  redundancy P in {1,2,3,4,6,8}; hop-count L in {2,3,4,5}; cyclomatic number swept by chord augmentation; node-count regimes
  small/medium/large; plus a random Renz-Nebel A(n,d,l) family for the natural joint distribution. >=500 networks per grid
  cell. (5) TWO VIEWS PER NETWORK: an abstract graph (nodes, edges, gold relation sets, query edge) for simulated-reader experiments
  AND a short professional-prose NL realization (one sentence per non-query edge, paraphrase-varied) so an LLM reader can
  be run later. (6) RICH RECORDED METADATA per network: gold relation on every edge, query edge, full enumerated set of constraining
  s-t paths through distinct intermediates (capped), contributing-edge count, measured cyclomatic number and cycle basis,
  target vs realized structural labels, RNG seed, entity-name map, and (recommended) the per-path composition of gold atomic
  relations + their naive intersection with a 'has-bite' flag. (7) PRE-REGISTERED realism-matching thresholds recorded as
  metadata with validated=false (TV distance of per-edge error-type distributions, cross-edge error-correlation rho match,
  redundancy/topology histogram match) to be checked next iteration against the real frontier-pilot error distributions. (8)
  Schema-valid rows {input: NL realization, output: gold graph, metadata_fold, algebra, cell labels, structural metadata};
  deterministic pilot/dev/test fold partition; full/mini/preview variants; total <=300MB.
dataset_search_plan: >-
  GENERATION PLAN (this is a SYNTHETIC generator, not a download). Python 3.12 + UV. Core deps: numpy, networkx (graph build,
  simple-path enumeration, cyclomatic number, cycle basis), and OPTIONAL `qualreas` (clone https://github.com/alreich/qualreas
  + `pip install bitsets`) to load AUTHORITATIVE composition tables and cross-check consistency. Use aii-parallel-computing
  (multiprocessing over network seeds) and aii-json for validation. Generation is milliseconds/network; cpu_heavy + multiprocessing
  finishes ~30-40k networks in minutes.\n\n=== STEP 1: DEFINE THE THREE ALGEBRAS ===\n(a) CONVEX POINT ALGEBRA (PA): base
  relations {'<','=','>'}. Convex disjunctions allowed = {'<','=','>','<=' (={<,=}),'>=' (={>,=}),'?' (={<,=,>})}; the NON-convex
  '!=' (={<,>}) is FORBIDDEN in any disjunctive label for this arm (path-consistency is complete only on the convex/pointisable
  fragment -- confirmed: van Beek/Vilain-Kautz). Composition computed directly by point reasoning. (b) ALLEN INTERVAL ALGEBRA
  (IA): 13 base relations {b,bi,m,mi,o,oi,d,di,s,si,f,fi,eq}. Load the exact 13x13 composition table from qualreas (`Algebras/*Interval*`
  JSON) OR hardcode the standard Allen-1983 table; cross-check the two on a few entries. (c) RCC-8: 8 base relations {DC,EC,PO,EQ,TPP,NTPP,TPPi,NTPPi};
  load 8x8 table from qualreas `RCC8_Algebra` JSON or hardcode published table. Store each algebra as: base-relation list,
  converse map, and composition dict comp[(r1,r2)] -> frozenset(base relations). Provide intersection (set), composition-of-sets
  (union of pairwise comps), and converse helpers.\n\n=== STEP 2: MODEL-BASED CONSISTENT SCENARIO (guarantees gold + global
  consistency) ===\nFor a fixed node set, embed every node in a concrete model, then READ OFF the gold atomic relation per
  pair. Realizable => globally consistent, no solver needed.\n - PA: assign each node an INTEGER coordinate x_i drawn from
  a SMALL grid (e.g. 0..K with K ~ node_count) so collisions occur => '=' relations appear; gold(i,j)=sign(x_i-x_j) -> '<','=','>'.\n
  - IA: assign each interval [s_i,e_i] with s_i<e_i from a small INTEGER grid (so endpoint coincidences occur, realizing the
  degenerate relations m,mi,s,si,f,fi,eq); gold = standard 13-case endpoint comparison. After a batch, compute the base-relation
  histogram; if any of {m,mi,s,si,f,fi,eq} is under-represented, PLANT it by explicitly constructing endpoint-coincident intervals
  so all 13 relations appear with non-trivial frequency. Record the histogram.\n - RCC-8: assign each region a DISC (center
  c_i in R^2 on an integer grid, radius r_i integer). Confirmed: closed discs in the plane realize exactly the 8 RCC-8 relations.
  Let d=|c_i-c_j|: DC if d>r_i+r_j; EC if d==r_i+r_j; PO if |r_i-r_j|<d<r_i+r_j; EQ if d==0 and r_i==r_j; (i inside j) TPP
  if d==r_j-r_i and r_i<r_j, NTPP if d<r_j-r_i and r_i<r_j; TPPi/NTPPi symmetric. Integer grid makes tangency (EC,TPP) and
  equality (EQ) hit with positive probability; plant under-represented relations as above; record histogram.\nCRITICAL CORRECTNESS
  GATE (assert on all networks): for every constraining path, the composition (via the table) of the gold ATOMIC relations
  along it MUST contain the gold query relation. This must ALWAYS hold for a realizable scenario; a violation means a buggy
  composition table or model -- fail loudly. Optionally also run path-consistency (qualreas or own PC) on the atomic scenario
  and assert no edge collapses to empty.\n\n=== STEP 3: TOPOLOGY CONTROL (the core design) ===\nThe constraint graph EXCLUDES
  the held-out query edge (query starts universal). Cyclomatic number mu = E - V + C (C=#components; connected => mu=E-V+1).\nFAMILY
  1 -- GENERALIZED THETA (controls redundancy P and hop-count L cleanly): designate query pair (s,t); build P internally VERTEX-DISJOINT
  s->t paths, each of L edges (L-1 distinct intermediates). Then redundancy=P, hop-count=L, node count V=P*(L-1)+2, derived
  mu=P-1. Embed all V nodes in the model (Step 2), read gold per edge; gold query=relation(s,t). s and t share no edge =>
  deduction-required by construction.\nFAMILY 2 -- CYCLOMATIC AUGMENTATION (sweep cyclomatic): start from a theta base, add
  k CHORD edges among intermediates (each added edge to a connected graph raises mu by exactly 1). HONESTY NOTE: in simple
  graphs cyclomatic and 'number of s-t paths' are algebraically linked (mu=E-V+1) and cross-link chords generally create new
  s-t paths, so PERFECT redundancy<>cyclomatic orthogonality is NOT achievable -- DESIGN the clean axes (P via theta, L via
  path length) and MEASURE cyclomatic + realized path count, recording BOTH target and realized values so the experiment can
  stratify/regress on measured quantities. Add cross-link chords between intermediates of DIFFERENT paths (these are the cycles
  that let iterated propagation tighten the query beyond a single intersection pass -- exactly what H3 needs).\nFAMILY 3 --
  RANDOM RENZ-NEBEL A(n,d,l) (natural joint distribution): n nodes, each pair constrained with prob giving average degree
  d in {3,6,9} (phase transition ~8-10), pick a query pair and hold it out; gold from the model embedding; MEASURE redundancy/hop/cyclomatic.
  Provides unstructured coverage + the natural topology reference for next-iteration realism matching. Use networkx to enumerate
  simple s-t paths (`nx.all_simple_paths`, cutoff on length and a max-count cap e.g. 64; set a 'paths_truncated' flag if capped)
  and to compute mu and a cycle basis.\n\n=== STEP 4: GRID / SWEEP (>=500 networks per cell) ===\nFor each algebra in {point,
  allen, rcc8}: (i) REDUNDANCY sweep (Family 1): P in {1,2,3,4,6,8} at L=2, plus P in {1,2,3,4} at L=3. (ii) HOP sweep (Family
  1): L in {2,3,4,5} at P=2. (iii) CYCLOMATIC sweep (Family 2): target mu in {0,1,2,3} built from a P=2,L=3 base via chords
  (record realized mu + realized path count). (iv) NODE-COUNT robustness (Family 1): small/medium/large node regimes at P=3,L=3.
  (v) RANDOM (Family 3): (n,d) in {8,12} x {3,6,9}. ~20-24 cells/algebra x 3 = ~60-72 cells x 500 = ~30-36k networks. point+allen
  are PRIMARY (full grid, 500/cell); RCC-8 SECONDARY (500/cell if size allows, else 300/cell or fewer random cells). Each
  cell gets a deterministic distinct seed base so generation is reproducible and resumable.\n\n=== STEP 5: NL REALIZATION
  (template verbalization) ===\nAssign each node a generic professional entity phrase from a pool (>=50 distinct each; reuse
  none within a network). Temporal pool (PA/IA): events like 'the merger announcement','the board meeting','the product launch','the
  regulatory filing','the press briefing','the audit','the shareholder vote',... Spatial pool (RCC-8): regions like 'the industrial
  zone','the flood plain','the conservation area','the harbor district','Parcel A',... For each NON-query edge, verbalize
  its GOLD relation with a template chosen at random among 2-3 PARAPHRASES per relation (record the template index per edge
  for later error analysis). Templates (one set per relation): PA: '<' -> '{A} occurred before {B}.'; '=' -> '{A} happened
  at the same time as {B}.'; '>' -> '{A} occurred after {B}.'. IA examples: b -> '{A} ended before {B} began.'; m -> '{A}
  ended exactly as {B} began.'; o -> '{A} began before {B} and the two overlapped, with {A} finishing first.'; d -> '{A} took
  place entirely during {B}.'; s -> '{A} and {B} began together, but {A} ended first.'; f -> '{A} and {B} ended together,
  but {A} began later.'; di -> '{A} began before {B} and ended after it.'; eq -> '{A} and {B} spanned exactly the same period.';
  (provide all 13). RCC-8 examples: DC -> '{A} is completely separate from {B}.'; EC -> '{A} touches {B} along its boundary
  without overlapping.'; PO -> '{A} and {B} partially overlap.'; TPP -> '{A} lies inside {B} and touches its boundary.'; NTPP
  -> '{A} lies strictly inside {B}.'; EQ -> '{A} occupies exactly the same area as {B}.'; (provide converses). Order sentences
  in a shuffled but readable sequence. The query edge is NEVER verbalized. The `input` string = the document (joined sentences)
  + a final line 'Query: what is the {temporal|spatial} relation between {entity_s} and {entity_t}?'. Verify s,t do not co-occur
  in any single sentence.\n\n=== STEP 6: ROW SCHEMA (emit per network) ===\n`input`: NL realization string (Step 5). `output`:
  gold graph = {edges: [{source, target, relation}], query_edge: {source, target, relation, is_query: true}} using canonical
  relation strings. `metadata_fold`: deterministic by hash(seed) WITHIN each cell -> 'pilot' (10%) / 'dev' (20%) / 'test'
  (70%) so every cell appears in all folds (pilot/dev for frontier-pilot prompt tuning, test for confirmatory runs). Additional
  top-level row fields/metadata: algebra; cell labels {redundancy_P, hop_count_L, cyclomatic_target, node_count, generator_family
  in ['theta','cyclo_aug','random_andl'], cell_id}; MEASURED structure {cyclomatic_number, cycle_basis_size, num_simple_paths_s_t,
  paths_truncated, contributing_edge_count, path_list (node-id sequences, capped)}; abstract_graph {nodes:[ids], edges:[[u,v,relation]],
  query_edge:[s,t]}; entity_map {node_id -> phrase}; seed; model_embedding (coords/intervals/discs OR just seed for replay);
  RECOMMENDED per-path analytics {path_compositions: composed gold base-relation set per path, naive_intersection: intersection
  across paths, has_bite: naive_intersection != universal, singleton_resolved: naive_intersection == {gold}}; templates_used
  {edge -> paraphrase index}. Also include a SOUND reference disjunctive labeling `reference_disjunctive_labels` (each non-query
  edge given a random SOUND superset of its gold of average size l~6.5 for IA / proportional for PA,RCC-8 -- the Renz-Nebel
  A(n,d,l) 'weakened' network; query edge = universal). FOR THE POINT ARM ONLY, restrict these supersets to CONVEX relations
  (never '!='). Clearly document that the canonical ground truth is the gold ATOMIC graph and that recall-controlled weakening
  is the EXPERIMENT's job; the reference labels are a convenience.\n\n=== STEP 7: PRE-REGISTERED REALISM THRESHOLDS (record,
  do NOT validate) ===\nStore once at dataset level (and/or per row) a block realism_preregistration = {validated: false,
  tv_distance_max: 0.15 (per-edge error-type distribution), rho_match_tol: 0.10 (cross-edge error-correlation), topology_histogram_emd_max:
  0.10 (contributing-edge-count + cycle-structure histograms)} with a note that these are to be checked NEXT iteration against
  the real frontier-pilot error distributions. These are placeholders fixed now to inoculate against post-hoc tuning.\n\n===
  STEP 8: QA, VALIDATION, SPLITS ===\n(1) Assert the Step-2 correctness gate on ALL networks (path composition contains gold
  query relation). (2) On a sample, run path-consistency (qualreas) on the atomic scenario to confirm consistency. (3) Assert
  deduction-required (s,t never co-occur in a sentence). (4) Report per-algebra relation histograms, per-cell counts, and
  the joint (redundancy x hop x cyclomatic) coverage table. (5) Validate data_out.json against the AII row schema with aii-json;
  produce full/mini/preview variants. (6) Keep <=300MB: monitor file size; if over, trim RCC-8 cell counts first, then compact
  verbose fields (store model_embedding as seed-only, cap path_list length), then use aii-file-size-limit to split. Estimate
  ~2-4KB/row x ~33k rows ~ 100-150MB (safe).\n\n=== FAILURE SCENARIOS + MITIGATIONS ===\n - Simple-path enumeration blow-up
  on random/augmented graphs: cap by length cutoff + max-count, set paths_truncated flag. - Degenerate relations never realized
  by continuous reals: use INTEGER grids + explicit planting; verify via histogram. - Convex-PA violated by '!=': forbid non-convex
  supersets in reference labels for the point arm. - Composition-table bug: cross-check qualreas vs hardcoded on sampled entries;
  the Step-2 gate catches systematic errors. - Cyclomatic<>redundancy non-orthogonality: design clean P,L axes, MEASURE cyclomatic,
  record target+realized, supply random family for joint coverage. - Size overflow: trimming ladder above. - Resumability:
  per-cell deterministic seeds so a re-run reproduces byte-identically and can skip completed cells.\n\n=== WHY SYNTHETIC
  IS RIGHT HERE === No real corpus exposes independently-controlled redundancy/hop/cyclomatic with exact, consistent gold;
  the real-text headline corpora are delivered by sibling artifacts. This backbone is explicitly mandated by the hypothesis
  (Renz-Nebel A(n,d,l) generator, >=500 networks/cell, second algebra RCC-8) for the H3 (iteration) and H4 (redundancy inverted-U)
  claims and for future LLM-on-synthetic reading.
target_num_datasets: 3
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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
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
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 24 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 12 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 6 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-17 13:39:23 UTC

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

### [3] SKILL-INPUT — aii-json · 2026-06-17 13:44:33 UTC

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

### [4] SYSTEM-USER prompt · 2026-06-17 14:12:24 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/results/out.json`
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
id: gen_plan_dataset_2_idx3
type: dataset
title: >-
  Synthetic QCN Backbone: Controlled Consistent Qualitative Constraint Networks (Allen / Convex-Point / RCC-8) with NL Realizations
summary: >-
  Generate the clean-ground-truth synthetic corpus for the redundancy (H4) and iteration (H3) claims: random CONSISTENT qualitative
  constraint networks over three relation algebras (Allen interval, convex point, RCC-8) built by model-based realization
  (so the gold atomic scenario is globally consistent and the gold relation on every edge is known), with controlled query
  topology that sweeps redundancy (number of constraining paths), hop-count, cyclomatic number and node count, >=500 networks
  per cell. Each network ships TWO views: an abstract graph (for simulated-reader experiments) and a template NL realization
  (so an LLM reader can later be run on synthetic text). Records gold graph, held-out query edge, enumerated constraining
  paths, contributing-edge counts and cycle structure, plus PRE-REGISTERED (recorded, not yet validated) realism-matching
  thresholds. Schema-valid via aii-json, full/mini/preview splits, <=300MB.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  PURELY SYNTHETIC AND THAT IS CORRECT HERE: this artifact is the clean-ground-truth backbone whose entire value is INDEPENDENTLY
  controlling structural parameters (redundancy, hop-count, cyclomatic number, density, node count) that no real corpus exposes.
  The real-text corpora (NarrativeTime, TDDMan, MATRES) are delivered by SIBLING dataset artifacts; do NOT duplicate them
  here. Prefer-real does not apply: a controlled QCN sweep cannot be found, only generated. Ideal properties: (1) GROUND TRUTH
  IS EXACT AND CONSISTENT BY CONSTRUCTION -- every network is a realizable model (points/intervals/discs), so the gold atomic
  relation on each edge is read off the model and the whole scenario is globally consistent (no solver needed to certify consistency).
  (2) THREE ALGEBRAS: Allen interval algebra (13 base relations) and convex point algebra (base {<,=,>}) as PRIMARY (full
  grid, >=500/cell); RCC-8 (8 base relations) as the SECONDARY second-algebra arm (>=500/cell where size permits, else >=300/cell).
  (3) DEDUCTION-REQUIRED QUERY STRUCTURE: each network has a designated held-out query pair (s,t) whose two endpoints share
  NO direct edge and never co-occur in a single verbalized sentence, so the query relation is obtainable only by composing
  >=1 multi-edge path -- the structural analogue of the real-corpus 'deduction-required' subset. (4) INDEPENDENTLY SWEPT STRUCTURE:
  redundancy P in {1,2,3,4,6,8}; hop-count L in {2,3,4,5}; cyclomatic number swept by chord augmentation; node-count regimes
  small/medium/large; plus a random Renz-Nebel A(n,d,l) family for the natural joint distribution. >=500 networks per grid
  cell. (5) TWO VIEWS PER NETWORK: an abstract graph (nodes, edges, gold relation sets, query edge) for simulated-reader experiments
  AND a short professional-prose NL realization (one sentence per non-query edge, paraphrase-varied) so an LLM reader can
  be run later. (6) RICH RECORDED METADATA per network: gold relation on every edge, query edge, full enumerated set of constraining
  s-t paths through distinct intermediates (capped), contributing-edge count, measured cyclomatic number and cycle basis,
  target vs realized structural labels, RNG seed, entity-name map, and (recommended) the per-path composition of gold atomic
  relations + their naive intersection with a 'has-bite' flag. (7) PRE-REGISTERED realism-matching thresholds recorded as
  metadata with validated=false (TV distance of per-edge error-type distributions, cross-edge error-correlation rho match,
  redundancy/topology histogram match) to be checked next iteration against the real frontier-pilot error distributions. (8)
  Schema-valid rows {input: NL realization, output: gold graph, metadata_fold, algebra, cell labels, structural metadata};
  deterministic pilot/dev/test fold partition; full/mini/preview variants; total <=300MB.
dataset_search_plan: >-
  GENERATION PLAN (this is a SYNTHETIC generator, not a download). Python 3.12 + UV. Core deps: numpy, networkx (graph build,
  simple-path enumeration, cyclomatic number, cycle basis), and OPTIONAL `qualreas` (clone https://github.com/alreich/qualreas
  + `pip install bitsets`) to load AUTHORITATIVE composition tables and cross-check consistency. Use aii-parallel-computing
  (multiprocessing over network seeds) and aii-json for validation. Generation is milliseconds/network; cpu_heavy + multiprocessing
  finishes ~30-40k networks in minutes.\n\n=== STEP 1: DEFINE THE THREE ALGEBRAS ===\n(a) CONVEX POINT ALGEBRA (PA): base
  relations {'<','=','>'}. Convex disjunctions allowed = {'<','=','>','<=' (={<,=}),'>=' (={>,=}),'?' (={<,=,>})}; the NON-convex
  '!=' (={<,>}) is FORBIDDEN in any disjunctive label for this arm (path-consistency is complete only on the convex/pointisable
  fragment -- confirmed: van Beek/Vilain-Kautz). Composition computed directly by point reasoning. (b) ALLEN INTERVAL ALGEBRA
  (IA): 13 base relations {b,bi,m,mi,o,oi,d,di,s,si,f,fi,eq}. Load the exact 13x13 composition table from qualreas (`Algebras/*Interval*`
  JSON) OR hardcode the standard Allen-1983 table; cross-check the two on a few entries. (c) RCC-8: 8 base relations {DC,EC,PO,EQ,TPP,NTPP,TPPi,NTPPi};
  load 8x8 table from qualreas `RCC8_Algebra` JSON or hardcode published table. Store each algebra as: base-relation list,
  converse map, and composition dict comp[(r1,r2)] -> frozenset(base relations). Provide intersection (set), composition-of-sets
  (union of pairwise comps), and converse helpers.\n\n=== STEP 2: MODEL-BASED CONSISTENT SCENARIO (guarantees gold + global
  consistency) ===\nFor a fixed node set, embed every node in a concrete model, then READ OFF the gold atomic relation per
  pair. Realizable => globally consistent, no solver needed.\n - PA: assign each node an INTEGER coordinate x_i drawn from
  a SMALL grid (e.g. 0..K with K ~ node_count) so collisions occur => '=' relations appear; gold(i,j)=sign(x_i-x_j) -> '<','=','>'.\n
  - IA: assign each interval [s_i,e_i] with s_i<e_i from a small INTEGER grid (so endpoint coincidences occur, realizing the
  degenerate relations m,mi,s,si,f,fi,eq); gold = standard 13-case endpoint comparison. After a batch, compute the base-relation
  histogram; if any of {m,mi,s,si,f,fi,eq} is under-represented, PLANT it by explicitly constructing endpoint-coincident intervals
  so all 13 relations appear with non-trivial frequency. Record the histogram.\n - RCC-8: assign each region a DISC (center
  c_i in R^2 on an integer grid, radius r_i integer). Confirmed: closed discs in the plane realize exactly the 8 RCC-8 relations.
  Let d=|c_i-c_j|: DC if d>r_i+r_j; EC if d==r_i+r_j; PO if |r_i-r_j|<d<r_i+r_j; EQ if d==0 and r_i==r_j; (i inside j) TPP
  if d==r_j-r_i and r_i<r_j, NTPP if d<r_j-r_i and r_i<r_j; TPPi/NTPPi symmetric. Integer grid makes tangency (EC,TPP) and
  equality (EQ) hit with positive probability; plant under-represented relations as above; record histogram.\nCRITICAL CORRECTNESS
  GATE (assert on all networks): for every constraining path, the composition (via the table) of the gold ATOMIC relations
  along it MUST contain the gold query relation. This must ALWAYS hold for a realizable scenario; a violation means a buggy
  composition table or model -- fail loudly. Optionally also run path-consistency (qualreas or own PC) on the atomic scenario
  and assert no edge collapses to empty.\n\n=== STEP 3: TOPOLOGY CONTROL (the core design) ===\nThe constraint graph EXCLUDES
  the held-out query edge (query starts universal). Cyclomatic number mu = E - V + C (C=#components; connected => mu=E-V+1).\nFAMILY
  1 -- GENERALIZED THETA (controls redundancy P and hop-count L cleanly): designate query pair (s,t); build P internally VERTEX-DISJOINT
  s->t paths, each of L edges (L-1 distinct intermediates). Then redundancy=P, hop-count=L, node count V=P*(L-1)+2, derived
  mu=P-1. Embed all V nodes in the model (Step 2), read gold per edge; gold query=relation(s,t). s and t share no edge =>
  deduction-required by construction.\nFAMILY 2 -- CYCLOMATIC AUGMENTATION (sweep cyclomatic): start from a theta base, add
  k CHORD edges among intermediates (each added edge to a connected graph raises mu by exactly 1). HONESTY NOTE: in simple
  graphs cyclomatic and 'number of s-t paths' are algebraically linked (mu=E-V+1) and cross-link chords generally create new
  s-t paths, so PERFECT redundancy<>cyclomatic orthogonality is NOT achievable -- DESIGN the clean axes (P via theta, L via
  path length) and MEASURE cyclomatic + realized path count, recording BOTH target and realized values so the experiment can
  stratify/regress on measured quantities. Add cross-link chords between intermediates of DIFFERENT paths (these are the cycles
  that let iterated propagation tighten the query beyond a single intersection pass -- exactly what H3 needs).\nFAMILY 3 --
  RANDOM RENZ-NEBEL A(n,d,l) (natural joint distribution): n nodes, each pair constrained with prob giving average degree
  d in {3,6,9} (phase transition ~8-10), pick a query pair and hold it out; gold from the model embedding; MEASURE redundancy/hop/cyclomatic.
  Provides unstructured coverage + the natural topology reference for next-iteration realism matching. Use networkx to enumerate
  simple s-t paths (`nx.all_simple_paths`, cutoff on length and a max-count cap e.g. 64; set a 'paths_truncated' flag if capped)
  and to compute mu and a cycle basis.\n\n=== STEP 4: GRID / SWEEP (>=500 networks per cell) ===\nFor each algebra in {point,
  allen, rcc8}: (i) REDUNDANCY sweep (Family 1): P in {1,2,3,4,6,8} at L=2, plus P in {1,2,3,4} at L=3. (ii) HOP sweep (Family
  1): L in {2,3,4,5} at P=2. (iii) CYCLOMATIC sweep (Family 2): target mu in {0,1,2,3} built from a P=2,L=3 base via chords
  (record realized mu + realized path count). (iv) NODE-COUNT robustness (Family 1): small/medium/large node regimes at P=3,L=3.
  (v) RANDOM (Family 3): (n,d) in {8,12} x {3,6,9}. ~20-24 cells/algebra x 3 = ~60-72 cells x 500 = ~30-36k networks. point+allen
  are PRIMARY (full grid, 500/cell); RCC-8 SECONDARY (500/cell if size allows, else 300/cell or fewer random cells). Each
  cell gets a deterministic distinct seed base so generation is reproducible and resumable.\n\n=== STEP 5: NL REALIZATION
  (template verbalization) ===\nAssign each node a generic professional entity phrase from a pool (>=50 distinct each; reuse
  none within a network). Temporal pool (PA/IA): events like 'the merger announcement','the board meeting','the product launch','the
  regulatory filing','the press briefing','the audit','the shareholder vote',... Spatial pool (RCC-8): regions like 'the industrial
  zone','the flood plain','the conservation area','the harbor district','Parcel A',... For each NON-query edge, verbalize
  its GOLD relation with a template chosen at random among 2-3 PARAPHRASES per relation (record the template index per edge
  for later error analysis). Templates (one set per relation): PA: '<' -> '{A} occurred before {B}.'; '=' -> '{A} happened
  at the same time as {B}.'; '>' -> '{A} occurred after {B}.'. IA examples: b -> '{A} ended before {B} began.'; m -> '{A}
  ended exactly as {B} began.'; o -> '{A} began before {B} and the two overlapped, with {A} finishing first.'; d -> '{A} took
  place entirely during {B}.'; s -> '{A} and {B} began together, but {A} ended first.'; f -> '{A} and {B} ended together,
  but {A} began later.'; di -> '{A} began before {B} and ended after it.'; eq -> '{A} and {B} spanned exactly the same period.';
  (provide all 13). RCC-8 examples: DC -> '{A} is completely separate from {B}.'; EC -> '{A} touches {B} along its boundary
  without overlapping.'; PO -> '{A} and {B} partially overlap.'; TPP -> '{A} lies inside {B} and touches its boundary.'; NTPP
  -> '{A} lies strictly inside {B}.'; EQ -> '{A} occupies exactly the same area as {B}.'; (provide converses). Order sentences
  in a shuffled but readable sequence. The query edge is NEVER verbalized. The `input` string = the document (joined sentences)
  + a final line 'Query: what is the {temporal|spatial} relation between {entity_s} and {entity_t}?'. Verify s,t do not co-occur
  in any single sentence.\n\n=== STEP 6: ROW SCHEMA (emit per network) ===\n`input`: NL realization string (Step 5). `output`:
  gold graph = {edges: [{source, target, relation}], query_edge: {source, target, relation, is_query: true}} using canonical
  relation strings. `metadata_fold`: deterministic by hash(seed) WITHIN each cell -> 'pilot' (10%) / 'dev' (20%) / 'test'
  (70%) so every cell appears in all folds (pilot/dev for frontier-pilot prompt tuning, test for confirmatory runs). Additional
  top-level row fields/metadata: algebra; cell labels {redundancy_P, hop_count_L, cyclomatic_target, node_count, generator_family
  in ['theta','cyclo_aug','random_andl'], cell_id}; MEASURED structure {cyclomatic_number, cycle_basis_size, num_simple_paths_s_t,
  paths_truncated, contributing_edge_count, path_list (node-id sequences, capped)}; abstract_graph {nodes:[ids], edges:[[u,v,relation]],
  query_edge:[s,t]}; entity_map {node_id -> phrase}; seed; model_embedding (coords/intervals/discs OR just seed for replay);
  RECOMMENDED per-path analytics {path_compositions: composed gold base-relation set per path, naive_intersection: intersection
  across paths, has_bite: naive_intersection != universal, singleton_resolved: naive_intersection == {gold}}; templates_used
  {edge -> paraphrase index}. Also include a SOUND reference disjunctive labeling `reference_disjunctive_labels` (each non-query
  edge given a random SOUND superset of its gold of average size l~6.5 for IA / proportional for PA,RCC-8 -- the Renz-Nebel
  A(n,d,l) 'weakened' network; query edge = universal). FOR THE POINT ARM ONLY, restrict these supersets to CONVEX relations
  (never '!='). Clearly document that the canonical ground truth is the gold ATOMIC graph and that recall-controlled weakening
  is the EXPERIMENT's job; the reference labels are a convenience.\n\n=== STEP 7: PRE-REGISTERED REALISM THRESHOLDS (record,
  do NOT validate) ===\nStore once at dataset level (and/or per row) a block realism_preregistration = {validated: false,
  tv_distance_max: 0.15 (per-edge error-type distribution), rho_match_tol: 0.10 (cross-edge error-correlation), topology_histogram_emd_max:
  0.10 (contributing-edge-count + cycle-structure histograms)} with a note that these are to be checked NEXT iteration against
  the real frontier-pilot error distributions. These are placeholders fixed now to inoculate against post-hoc tuning.\n\n===
  STEP 8: QA, VALIDATION, SPLITS ===\n(1) Assert the Step-2 correctness gate on ALL networks (path composition contains gold
  query relation). (2) On a sample, run path-consistency (qualreas) on the atomic scenario to confirm consistency. (3) Assert
  deduction-required (s,t never co-occur in a sentence). (4) Report per-algebra relation histograms, per-cell counts, and
  the joint (redundancy x hop x cyclomatic) coverage table. (5) Validate data_out.json against the AII row schema with aii-json;
  produce full/mini/preview variants. (6) Keep <=300MB: monitor file size; if over, trim RCC-8 cell counts first, then compact
  verbose fields (store model_embedding as seed-only, cap path_list length), then use aii-file-size-limit to split. Estimate
  ~2-4KB/row x ~33k rows ~ 100-150MB (safe).\n\n=== FAILURE SCENARIOS + MITIGATIONS ===\n - Simple-path enumeration blow-up
  on random/augmented graphs: cap by length cutoff + max-count, set paths_truncated flag. - Degenerate relations never realized
  by continuous reals: use INTEGER grids + explicit planting; verify via histogram. - Convex-PA violated by '!=': forbid non-convex
  supersets in reference labels for the point arm. - Composition-table bug: cross-check qualreas vs hardcoded on sampled entries;
  the Step-2 gate catches systematic errors. - Cyclomatic<>redundancy non-orthogonality: design clean P,L axes, MEASURE cyclomatic,
  record target+realized, supply random family for joint coverage. - Size overflow: trimming ladder above. - Resumability:
  per-cell deterministic seeds so a re-run reproduces byte-identically and can skip completed cells.\n\n=== WHY SYNTHETIC
  IS RIGHT HERE === No real corpus exposes independently-controlled redundancy/hop/cyclomatic with exact, consistent gold;
  the real-text headline corpora are delivered by sibling artifacts. This backbone is explicitly mandated by the hypothesis
  (Renz-Nebel A(n,d,l) generator, >=500 networks/cell, second algebra RCC-8) for the H3 (iteration) and H4 (redundancy inverted-U)
  claims and for future LLM-on-synthetic reading.
target_num_datasets: 3
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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
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
TODO 1. For the top 6 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

Each data ROW must be a separate example — do NOT create one example per dataset or per fold. Each data point (row, sample, instance) = one example. 500 rows → 500 examples. The output is GROUPED BY DATASET:
```json
{
  "datasets": [
    {
      "dataset": "iris",
      "examples": [
        {"input": "...", "output": "...", "metadata_fold": 2, "metadata_feature_names": [...]},
        ...
      ]
    },
    {
      "dataset": "adult_census",
      "examples": [...]
    }
  ]
}
```
Per-example required fields:
- `input`: input features/text (tabular: JSON string of feature values)
- `output`: target/label (as string)
Per-example optional metadata via `metadata_<name>` fields (flat, not nested object):
- `metadata_fold`: fold assignment (int), `metadata_feature_names`: feature name list, `metadata_task_type`: "classification"/"regression", `metadata_n_classes`: number of classes, `metadata_row_index`: original row index, etc.
Do NOT use `split`, `dataset`, or `context` as per-example fields. Dataset name goes at the group level, metadata goes in `metadata_*` fields.
TODO 2. Run 'uv run data.py' and fix errors. Validate full_data_out.json against exp_sel_data_out.json schema (aii-json skill) — fix errors. Generate preview, mini, full versions with aii-json skill's format script.
TODO 3. Read preview to inspect examples. Choose THE BEST 3 DATASETS based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [5] SYSTEM-USER prompt · 2026-06-17 14:16:18 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_1/gen_art/gen_art_dataset_2/results/out.json`
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
id: gen_plan_dataset_2_idx3
type: dataset
title: >-
  Synthetic QCN Backbone: Controlled Consistent Qualitative Constraint Networks (Allen / Convex-Point / RCC-8) with NL Realizations
summary: >-
  Generate the clean-ground-truth synthetic corpus for the redundancy (H4) and iteration (H3) claims: random CONSISTENT qualitative
  constraint networks over three relation algebras (Allen interval, convex point, RCC-8) built by model-based realization
  (so the gold atomic scenario is globally consistent and the gold relation on every edge is known), with controlled query
  topology that sweeps redundancy (number of constraining paths), hop-count, cyclomatic number and node count, >=500 networks
  per cell. Each network ships TWO views: an abstract graph (for simulated-reader experiments) and a template NL realization
  (so an LLM reader can later be run on synthetic text). Records gold graph, held-out query edge, enumerated constraining
  paths, contributing-edge counts and cycle structure, plus PRE-REGISTERED (recorded, not yet validated) realism-matching
  thresholds. Schema-valid via aii-json, full/mini/preview splits, <=300MB.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  PURELY SYNTHETIC AND THAT IS CORRECT HERE: this artifact is the clean-ground-truth backbone whose entire value is INDEPENDENTLY
  controlling structural parameters (redundancy, hop-count, cyclomatic number, density, node count) that no real corpus exposes.
  The real-text corpora (NarrativeTime, TDDMan, MATRES) are delivered by SIBLING dataset artifacts; do NOT duplicate them
  here. Prefer-real does not apply: a controlled QCN sweep cannot be found, only generated. Ideal properties: (1) GROUND TRUTH
  IS EXACT AND CONSISTENT BY CONSTRUCTION -- every network is a realizable model (points/intervals/discs), so the gold atomic
  relation on each edge is read off the model and the whole scenario is globally consistent (no solver needed to certify consistency).
  (2) THREE ALGEBRAS: Allen interval algebra (13 base relations) and convex point algebra (base {<,=,>}) as PRIMARY (full
  grid, >=500/cell); RCC-8 (8 base relations) as the SECONDARY second-algebra arm (>=500/cell where size permits, else >=300/cell).
  (3) DEDUCTION-REQUIRED QUERY STRUCTURE: each network has a designated held-out query pair (s,t) whose two endpoints share
  NO direct edge and never co-occur in a single verbalized sentence, so the query relation is obtainable only by composing
  >=1 multi-edge path -- the structural analogue of the real-corpus 'deduction-required' subset. (4) INDEPENDENTLY SWEPT STRUCTURE:
  redundancy P in {1,2,3,4,6,8}; hop-count L in {2,3,4,5}; cyclomatic number swept by chord augmentation; node-count regimes
  small/medium/large; plus a random Renz-Nebel A(n,d,l) family for the natural joint distribution. >=500 networks per grid
  cell. (5) TWO VIEWS PER NETWORK: an abstract graph (nodes, edges, gold relation sets, query edge) for simulated-reader experiments
  AND a short professional-prose NL realization (one sentence per non-query edge, paraphrase-varied) so an LLM reader can
  be run later. (6) RICH RECORDED METADATA per network: gold relation on every edge, query edge, full enumerated set of constraining
  s-t paths through distinct intermediates (capped), contributing-edge count, measured cyclomatic number and cycle basis,
  target vs realized structural labels, RNG seed, entity-name map, and (recommended) the per-path composition of gold atomic
  relations + their naive intersection with a 'has-bite' flag. (7) PRE-REGISTERED realism-matching thresholds recorded as
  metadata with validated=false (TV distance of per-edge error-type distributions, cross-edge error-correlation rho match,
  redundancy/topology histogram match) to be checked next iteration against the real frontier-pilot error distributions. (8)
  Schema-valid rows {input: NL realization, output: gold graph, metadata_fold, algebra, cell labels, structural metadata};
  deterministic pilot/dev/test fold partition; full/mini/preview variants; total <=300MB.
dataset_search_plan: >-
  GENERATION PLAN (this is a SYNTHETIC generator, not a download). Python 3.12 + UV. Core deps: numpy, networkx (graph build,
  simple-path enumeration, cyclomatic number, cycle basis), and OPTIONAL `qualreas` (clone https://github.com/alreich/qualreas
  + `pip install bitsets`) to load AUTHORITATIVE composition tables and cross-check consistency. Use aii-parallel-computing
  (multiprocessing over network seeds) and aii-json for validation. Generation is milliseconds/network; cpu_heavy + multiprocessing
  finishes ~30-40k networks in minutes.\n\n=== STEP 1: DEFINE THE THREE ALGEBRAS ===\n(a) CONVEX POINT ALGEBRA (PA): base
  relations {'<','=','>'}. Convex disjunctions allowed = {'<','=','>','<=' (={<,=}),'>=' (={>,=}),'?' (={<,=,>})}; the NON-convex
  '!=' (={<,>}) is FORBIDDEN in any disjunctive label for this arm (path-consistency is complete only on the convex/pointisable
  fragment -- confirmed: van Beek/Vilain-Kautz). Composition computed directly by point reasoning. (b) ALLEN INTERVAL ALGEBRA
  (IA): 13 base relations {b,bi,m,mi,o,oi,d,di,s,si,f,fi,eq}. Load the exact 13x13 composition table from qualreas (`Algebras/*Interval*`
  JSON) OR hardcode the standard Allen-1983 table; cross-check the two on a few entries. (c) RCC-8: 8 base relations {DC,EC,PO,EQ,TPP,NTPP,TPPi,NTPPi};
  load 8x8 table from qualreas `RCC8_Algebra` JSON or hardcode published table. Store each algebra as: base-relation list,
  converse map, and composition dict comp[(r1,r2)] -> frozenset(base relations). Provide intersection (set), composition-of-sets
  (union of pairwise comps), and converse helpers.\n\n=== STEP 2: MODEL-BASED CONSISTENT SCENARIO (guarantees gold + global
  consistency) ===\nFor a fixed node set, embed every node in a concrete model, then READ OFF the gold atomic relation per
  pair. Realizable => globally consistent, no solver needed.\n - PA: assign each node an INTEGER coordinate x_i drawn from
  a SMALL grid (e.g. 0..K with K ~ node_count) so collisions occur => '=' relations appear; gold(i,j)=sign(x_i-x_j) -> '<','=','>'.\n
  - IA: assign each interval [s_i,e_i] with s_i<e_i from a small INTEGER grid (so endpoint coincidences occur, realizing the
  degenerate relations m,mi,s,si,f,fi,eq); gold = standard 13-case endpoint comparison. After a batch, compute the base-relation
  histogram; if any of {m,mi,s,si,f,fi,eq} is under-represented, PLANT it by explicitly constructing endpoint-coincident intervals
  so all 13 relations appear with non-trivial frequency. Record the histogram.\n - RCC-8: assign each region a DISC (center
  c_i in R^2 on an integer grid, radius r_i integer). Confirmed: closed discs in the plane realize exactly the 8 RCC-8 relations.
  Let d=|c_i-c_j|: DC if d>r_i+r_j; EC if d==r_i+r_j; PO if |r_i-r_j|<d<r_i+r_j; EQ if d==0 and r_i==r_j; (i inside j) TPP
  if d==r_j-r_i and r_i<r_j, NTPP if d<r_j-r_i and r_i<r_j; TPPi/NTPPi symmetric. Integer grid makes tangency (EC,TPP) and
  equality (EQ) hit with positive probability; plant under-represented relations as above; record histogram.\nCRITICAL CORRECTNESS
  GATE (assert on all networks): for every constraining path, the composition (via the table) of the gold ATOMIC relations
  along it MUST contain the gold query relation. This must ALWAYS hold for a realizable scenario; a violation means a buggy
  composition table or model -- fail loudly. Optionally also run path-consistency (qualreas or own PC) on the atomic scenario
  and assert no edge collapses to empty.\n\n=== STEP 3: TOPOLOGY CONTROL (the core design) ===\nThe constraint graph EXCLUDES
  the held-out query edge (query starts universal). Cyclomatic number mu = E - V + C (C=#components; connected => mu=E-V+1).\nFAMILY
  1 -- GENERALIZED THETA (controls redundancy P and hop-count L cleanly): designate query pair (s,t); build P internally VERTEX-DISJOINT
  s->t paths, each of L edges (L-1 distinct intermediates). Then redundancy=P, hop-count=L, node count V=P*(L-1)+2, derived
  mu=P-1. Embed all V nodes in the model (Step 2), read gold per edge; gold query=relation(s,t). s and t share no edge =>
  deduction-required by construction.\nFAMILY 2 -- CYCLOMATIC AUGMENTATION (sweep cyclomatic): start from a theta base, add
  k CHORD edges among intermediates (each added edge to a connected graph raises mu by exactly 1). HONESTY NOTE: in simple
  graphs cyclomatic and 'number of s-t paths' are algebraically linked (mu=E-V+1) and cross-link chords generally create new
  s-t paths, so PERFECT redundancy<>cyclomatic orthogonality is NOT achievable -- DESIGN the clean axes (P via theta, L via
  path length) and MEASURE cyclomatic + realized path count, recording BOTH target and realized values so the experiment can
  stratify/regress on measured quantities. Add cross-link chords between intermediates of DIFFERENT paths (these are the cycles
  that let iterated propagation tighten the query beyond a single intersection pass -- exactly what H3 needs).\nFAMILY 3 --
  RANDOM RENZ-NEBEL A(n,d,l) (natural joint distribution): n nodes, each pair constrained with prob giving average degree
  d in {3,6,9} (phase transition ~8-10), pick a query pair and hold it out; gold from the model embedding; MEASURE redundancy/hop/cyclomatic.
  Provides unstructured coverage + the natural topology reference for next-iteration realism matching. Use networkx to enumerate
  simple s-t paths (`nx.all_simple_paths`, cutoff on length and a max-count cap e.g. 64; set a 'paths_truncated' flag if capped)
  and to compute mu and a cycle basis.\n\n=== STEP 4: GRID / SWEEP (>=500 networks per cell) ===\nFor each algebra in {point,
  allen, rcc8}: (i) REDUNDANCY sweep (Family 1): P in {1,2,3,4,6,8} at L=2, plus P in {1,2,3,4} at L=3. (ii) HOP sweep (Family
  1): L in {2,3,4,5} at P=2. (iii) CYCLOMATIC sweep (Family 2): target mu in {0,1,2,3} built from a P=2,L=3 base via chords
  (record realized mu + realized path count). (iv) NODE-COUNT robustness (Family 1): small/medium/large node regimes at P=3,L=3.
  (v) RANDOM (Family 3): (n,d) in {8,12} x {3,6,9}. ~20-24 cells/algebra x 3 = ~60-72 cells x 500 = ~30-36k networks. point+allen
  are PRIMARY (full grid, 500/cell); RCC-8 SECONDARY (500/cell if size allows, else 300/cell or fewer random cells). Each
  cell gets a deterministic distinct seed base so generation is reproducible and resumable.\n\n=== STEP 5: NL REALIZATION
  (template verbalization) ===\nAssign each node a generic professional entity phrase from a pool (>=50 distinct each; reuse
  none within a network). Temporal pool (PA/IA): events like 'the merger announcement','the board meeting','the product launch','the
  regulatory filing','the press briefing','the audit','the shareholder vote',... Spatial pool (RCC-8): regions like 'the industrial
  zone','the flood plain','the conservation area','the harbor district','Parcel A',... For each NON-query edge, verbalize
  its GOLD relation with a template chosen at random among 2-3 PARAPHRASES per relation (record the template index per edge
  for later error analysis). Templates (one set per relation): PA: '<' -> '{A} occurred before {B}.'; '=' -> '{A} happened
  at the same time as {B}.'; '>' -> '{A} occurred after {B}.'. IA examples: b -> '{A} ended before {B} began.'; m -> '{A}
  ended exactly as {B} began.'; o -> '{A} began before {B} and the two overlapped, with {A} finishing first.'; d -> '{A} took
  place entirely during {B}.'; s -> '{A} and {B} began together, but {A} ended first.'; f -> '{A} and {B} ended together,
  but {A} began later.'; di -> '{A} began before {B} and ended after it.'; eq -> '{A} and {B} spanned exactly the same period.';
  (provide all 13). RCC-8 examples: DC -> '{A} is completely separate from {B}.'; EC -> '{A} touches {B} along its boundary
  without overlapping.'; PO -> '{A} and {B} partially overlap.'; TPP -> '{A} lies inside {B} and touches its boundary.'; NTPP
  -> '{A} lies strictly inside {B}.'; EQ -> '{A} occupies exactly the same area as {B}.'; (provide converses). Order sentences
  in a shuffled but readable sequence. The query edge is NEVER verbalized. The `input` string = the document (joined sentences)
  + a final line 'Query: what is the {temporal|spatial} relation between {entity_s} and {entity_t}?'. Verify s,t do not co-occur
  in any single sentence.\n\n=== STEP 6: ROW SCHEMA (emit per network) ===\n`input`: NL realization string (Step 5). `output`:
  gold graph = {edges: [{source, target, relation}], query_edge: {source, target, relation, is_query: true}} using canonical
  relation strings. `metadata_fold`: deterministic by hash(seed) WITHIN each cell -> 'pilot' (10%) / 'dev' (20%) / 'test'
  (70%) so every cell appears in all folds (pilot/dev for frontier-pilot prompt tuning, test for confirmatory runs). Additional
  top-level row fields/metadata: algebra; cell labels {redundancy_P, hop_count_L, cyclomatic_target, node_count, generator_family
  in ['theta','cyclo_aug','random_andl'], cell_id}; MEASURED structure {cyclomatic_number, cycle_basis_size, num_simple_paths_s_t,
  paths_truncated, contributing_edge_count, path_list (node-id sequences, capped)}; abstract_graph {nodes:[ids], edges:[[u,v,relation]],
  query_edge:[s,t]}; entity_map {node_id -> phrase}; seed; model_embedding (coords/intervals/discs OR just seed for replay);
  RECOMMENDED per-path analytics {path_compositions: composed gold base-relation set per path, naive_intersection: intersection
  across paths, has_bite: naive_intersection != universal, singleton_resolved: naive_intersection == {gold}}; templates_used
  {edge -> paraphrase index}. Also include a SOUND reference disjunctive labeling `reference_disjunctive_labels` (each non-query
  edge given a random SOUND superset of its gold of average size l~6.5 for IA / proportional for PA,RCC-8 -- the Renz-Nebel
  A(n,d,l) 'weakened' network; query edge = universal). FOR THE POINT ARM ONLY, restrict these supersets to CONVEX relations
  (never '!='). Clearly document that the canonical ground truth is the gold ATOMIC graph and that recall-controlled weakening
  is the EXPERIMENT's job; the reference labels are a convenience.\n\n=== STEP 7: PRE-REGISTERED REALISM THRESHOLDS (record,
  do NOT validate) ===\nStore once at dataset level (and/or per row) a block realism_preregistration = {validated: false,
  tv_distance_max: 0.15 (per-edge error-type distribution), rho_match_tol: 0.10 (cross-edge error-correlation), topology_histogram_emd_max:
  0.10 (contributing-edge-count + cycle-structure histograms)} with a note that these are to be checked NEXT iteration against
  the real frontier-pilot error distributions. These are placeholders fixed now to inoculate against post-hoc tuning.\n\n===
  STEP 8: QA, VALIDATION, SPLITS ===\n(1) Assert the Step-2 correctness gate on ALL networks (path composition contains gold
  query relation). (2) On a sample, run path-consistency (qualreas) on the atomic scenario to confirm consistency. (3) Assert
  deduction-required (s,t never co-occur in a sentence). (4) Report per-algebra relation histograms, per-cell counts, and
  the joint (redundancy x hop x cyclomatic) coverage table. (5) Validate data_out.json against the AII row schema with aii-json;
  produce full/mini/preview variants. (6) Keep <=300MB: monitor file size; if over, trim RCC-8 cell counts first, then compact
  verbose fields (store model_embedding as seed-only, cap path_list length), then use aii-file-size-limit to split. Estimate
  ~2-4KB/row x ~33k rows ~ 100-150MB (safe).\n\n=== FAILURE SCENARIOS + MITIGATIONS ===\n - Simple-path enumeration blow-up
  on random/augmented graphs: cap by length cutoff + max-count, set paths_truncated flag. - Degenerate relations never realized
  by continuous reals: use INTEGER grids + explicit planting; verify via histogram. - Convex-PA violated by '!=': forbid non-convex
  supersets in reference labels for the point arm. - Composition-table bug: cross-check qualreas vs hardcoded on sampled entries;
  the Step-2 gate catches systematic errors. - Cyclomatic<>redundancy non-orthogonality: design clean P,L axes, MEASURE cyclomatic,
  record target+realized, supply random family for joint coverage. - Size overflow: trimming ladder above. - Resumability:
  per-cell deterministic seeds so a re-run reproduces byte-identically and can skip completed cells.\n\n=== WHY SYNTHETIC
  IS RIGHT HERE === No real corpus exposes independently-controlled redundancy/hop/cyclomatic with exact, consistent gold;
  the real-text headline corpora are delivered by sibling artifacts. This backbone is explicitly mandated by the hypothesis
  (Renz-Nebel A(n,d,l) generator, >=500 networks/cell, second algebra RCC-8) for the H3 (iteration) and H4 (redundancy inverted-U)
  claims and for future LLM-on-synthetic reading.
target_num_datasets: 3
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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
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
TODO 1. Update data.py to only include the chosen 3 datasets and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
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
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
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
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````
