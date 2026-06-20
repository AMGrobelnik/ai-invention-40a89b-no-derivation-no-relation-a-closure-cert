# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 4 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 20:27:29 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: >-
  SPATIAL multi-path-redundant gold-QCN corpus: a-priori redundancy-prevalence gate for iter-5's second real-venue cross-path-intersection
  test
summary: >-
  Build and standardize a spatial-reasoning corpus whose gold scene-graphs structurally HOST the paper's signature-but-still-synthetic-only
  mechanism: query pairs reachable via >=2 EDGE-DISJOINT constraining paths whose single-path compositions leave disjunctions
  that intersection narrows. Source 4-6 published spatial QA datasets (SpaRTUN/SpaRP-PS1 as the dense RCC-8+directional multi-path
  workhorse; SpartQA-Human as a semi-natural multi-path arm; ReSQ as the genuinely-natural anchor; StepGame as a single-chain
  cardinal-direction contrast/hop-length arm; SpartQA-Auto and SpaRP-PS2 as evaluated extras), reconstruct one gold relation-graph
  per scene (nodes=objects with surface+char-offset spans; edges=stated native relation -> canonical algebra, splitting MEREOTOPOLOGICAL->RCC-8
  [engine-validated] from DIRECTIONAL->cardinal-direction-calculus [vocab recorded for next-iter engine extension]; a held-out
  multi-hop query edge; doc/scene folds), and emit a DESCRIPTIVE-ONLY multi-path-redundancy prevalence table (per query: #edge-disjoint
  constraining paths, hop length, cyclomatic number; per corpus: fraction of deduction-required held-out queries with >=2
  disjoint paths AND each path length>=2 = the spatial analog of the temporal a-priori N* gate). No closure, no LLM, no derived
  P/R. Deliver data.py + full/mini/preview data_out.json (aii-json validated) + a dataset card with the prevalence table,
  provenance, licenses, and honest templated-vs-natural / document-length-vs-3000-char / relation-vocab-coverage caveats.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  An IDEAL source for this corpus is a published spatial-reasoning QA dataset that, per scene/story, lets us reconstruct a GOLD relation-graph rich enough to contain genuine multi-path redundancy. Concretely the criteria, in priority order:

  1. MULTI-PATH-REDUNDANT SCENE GRAPHS (the load-bearing property). The story must STATE many relations among the SAME set of objects so that two query objects are connected by >=2 EDGE-DISJOINT paths, each of length >=2 (so each path requires COMPOSITION, not a directly stated edge). This is the spatial analog of the temporal a-priori gate that dense temporal corpora lack (near-transitively-closed => full==naive, no iteration bite) and sparse ones barely have (~12 edges). DENSE scene graphs (SpaRTUN reports ~10 stated relations per 8-sentence story over NLVR scene graphs; SpartQA scenes have multiple blocks x multiple objects) are far more likely to host this than single-chain corpora (StepGame clean = one linear k-hop chain => exactly one path => NO redundancy by construction).

  2. RICH RELATION ALGEBRA the engine can already use. MEREOTOPOLOGICAL relations mapping to RCC-8 {DC,EC,PO,EQ,TPP,NTPP,TPPI,NTPPI} are immediately usable (the dossier art_aQ2Rf8rwqteI engine already validates RCC-8 composition). SpaRTUN/SpaRP topological relations ARE RCC-8 verbatim -> prioritize these. DIRECTIONAL relations (left/right/above/below + diagonals; cardinal N/S/E/W+NE/NW/SE/SW) map to the cardinal-direction calculus (CDC), which the engine does NOT yet implement -> the vocabulary is recorded for next-iter engine extension, not used for closure here.

  3. RECONSTRUCTABLE GOLD GRAPH WITH GROUND TRUTH. The dataset must expose, per scene: (a) the set of STATED relations (the KB edges an honest local reader would extract) -- ideally as an explicit scene-graph / SpRL-triplet / symbolic annotation, else parseable from templated text; (b) a held-out QUERY pair with a GOLD relation (the answer); (c) entity surface forms locatable in the text for char-offset spans.

  4. NATURAL / HUMAN-AUTHORED TEXT for the 'genuinely natural' claim (ReSQ real mSpRL descriptions; SpartQA-Human human-annotated), BALANCED with TEMPLATED sets for statistical power (SpaRTUN/SpaRP, SpartQA-Auto, StepGame) -- each flagged honestly in metadata. The whole point of the descriptive prevalence table is to tell iter-5, before any LLM spend, WHETHER natural multi-path redundancy exists or whether the mechanism stays synthetic-only.

  5. PRACTICAL: total download <=300MB, permissive license (MIT / CC-BY-SA-4.0 / Apache-2.0 / research-use), JSON or easily-parsed format, $0 (no LLM calls -- this is a pure data + graph-structure-analysis task). Document length should be reported against the project's ~3000-char target; expect ALL spatial corpora to fall short (SpaRP context 108-1270 chars; SpaRTUN ~91 tokens; StepGame short; ReSQ/mSpRL real image descriptions a few hundred chars) -- report this honestly.

  NON-ideal / disqualifying: corpora that only give isolated (premise, hypothesis, label) triples with no recoverable multi-object scene graph; pure single-chain corpora used as the ONLY source (they cannot host redundancy -- keep StepGame only as a contrast arm); image-only datasets with no textual descriptions.
dataset_search_plan: |-
  Compute profile cpu_heavy (4 vCPU/32GB). NO LLM calls anywhere ($0). Target ~6 candidates evaluated, best 4 standardized. Use aii-hf-datasets for HF pulls, direct GitHub/URL downloads otherwise; networkx for the graph-structure analysis; aii-json to validate + make mini/preview.

  === PHASE 0: ACQUIRE + VERIFY CANDIDATES (parallelizable) ===
  Download and inspect these VERIFIED sources (all confirmed to exist June 2026):

  A. SpaRP (PRIMARY easy path; dense, multi-path, scene-graph + symbolic already extracted). HF `UKPLab/sparp`, license cc-by-sa-4.0 (code Apache-2.0, repo github.com/UKPLab/acl2024-sparc-and-sparp). Configs: 'SpaRP-PS1 (SpaRTUN)' ~21.2k, 'SpaRP-PS2 (StepGame)' ~154k, PS3/PS4 (StepGame-Ext), plus 'small-' variants (~3.5k each). Per-row fields: Context (text, 108-1270 chars), Question, Targets (1-4 relations), Reasoning (verbalized deductive CoT), SYMBOLIC representations (context/entity-mappings/reasoning in formal notation) and SCENE-GRAPH relations in structured JSON. ** Use SpaRP-PS1 as the dense RCC-8+directional multi-path workhorse: its symbolic scene-graph gives the stated KB edges directly, no NLVR reconstruction needed.** Verbalized RCC-8 labels map: 'outside'->DC, 'outside and touching'->EC, 'partially overlapping'->PO, 'inside and touching'->TPP, 'inside'->NTPP, 'contains and touches'->TPPI, 'contains'->NTPPI, 'overlapping'/'equal'->EQ (VERIFY exact strings against the data); directional: left/right/above/below/behind/in front + near/far.

  B. SpaRTUN raw (alt source for the FULL stated-relation set if SpaRP's scene-graph is incomplete). GitHub `HLR/SpaRTUN` (MIT) + `HLR/Spatial-QA-tasks` + `HLR/SpaRTUNQChain` (the QChain repo ships reasoning chains + data). Has a `data_format.txt`; external 'Download SpaRTUN' link. Relations: directional LEFT/RIGHT/ABOVE/BELOW/BEHIND/FRONT + distance NEAR/FAR + RCC-8 DC/EC/PO/EQ/TPP/NTPP/TPPI/NTPPI. ~10 stated relations per 8-sentence/91-token story over 6,600 NLVR scene graphs; sizes ~20,334 YN + 18,400 FR train, ~3.1k dev/test each. Multi-hop (authors ignore length-1 paths, select most-step questions) => high multi-path prevalence expected.

  C. SpartQA. GitHub `HLR/SpartQA_generation`. Direct zips: SpartQA_Auto -> https://www.cse.msu.edu/~kordjams/data/SpartQA_Auto.zip ; SpartQA_Human -> https://www.cse.msu.edu/~kordjams/data/SpartQA_Human.zip . Each scene ships an 'Annotation' (scene graph of the scene) + 'SpRL' (spatial role/relation extraction) + main file (stories, questions, answers, candidate answers, consistency/contrast set). Question types: FR (find relation between two objects -- USE FR as the held-out query, its answer IS the relation), FB (find block), CO (choose object), YN (yes/no). Scenes = multiple blocks x multiple objects => dense graphs. Record exact relation vocabulary from the downloaded annotation/data_format files verbatim (directional + distance + topological touching/inside/contains/cover/disjoint). HF mirrors exist (`tasksource/spartqa-yn`, `mteb/SpartQA`) but prefer the official zips because they include the scene-graph annotation needed to reconstruct stated relations. ** SpartQA-Human = the semi-natural multi-path arm; SpartQA-Auto = an evaluated templated extra.**

  D. ReSQ (GENUINELY-NATURAL anchor). HLR group, built on the mSpRL corpus (real image descriptions) with HUMAN-generated YN questions; SpRL triplet annotations inherited from mSpRL give the stated relations. Sizes train 1,008 / dev 333 / test 610. Reasoning depth 1-2 + commonsense (=> EXPECT LOW multi-path prevalence -- report it honestly; this arm's value is establishing whether natural text hosts ANY redundancy). Find the download via HLR/Spatial-QA-tasks or the ReSQ external link on the SpaRTUN repo; mSpRL (SemEval-2012 Task 3 / CLEF IAPR) for the underlying text if needed.

  E. StepGame (single-chain CONTRAST + hop-length). HF `michaelszx/StepGame` and `ZhengyanShi/StepGame`; GitHub `ZhengxiangShi/StepGame` (Dataset/TrainVersion 50k/1k; Dataset/CompleteVersion 30k train/1k val/30k test PER k=1..10). 8 cardinal relations: north, south, east, west, northeast, northwest, southeast, southwest (=> ALL cardinal-direction-calculus, NO mereotopological). Clean test stories = SINGLE LINEAR CHAINS (one path, no cycles) => multi-path prevalence ~0 by construction. Noise types reported as 'disconnected'/'irrelevant'/'supporting'; ** do NOT trust the label 'supporting'=='redundant paths' -- VERIFY EMPIRICALLY by reconstructing the graph and counting edge-disjoint paths.** Keep StepGame primarily as the single-chain contrast that shows where redundancy is absent (the sparse-corpus failure mode). Verify the license on the HF card / repo (research-use; record whatever it states).

  For EACH candidate, verify and log: exact HF id / repo URL + commit, license, on-disk size (<=300MB), file format, fields, splits, native relation vocabulary (verbatim), and whether a per-scene stated-relation set is recoverable. If a primary source is unreachable, fall back: SpaRP<->SpaRTUN raw (same underlying data); SpartQA zips<->HF mirrors; ReSQ<->mSpRL+regenerate; StepGame HF<->GitHub.

  === PHASE 1: RECONSTRUCT GOLD RELATION-GRAPHS ===
  For every scene/story build a directed multigraph G: nodes = objects/entities (dedup mentions to a canonical node id), edges = each STATED relation (the KB edges an honest local reader would extract). Edge attributes: native_relation (verbatim), algebra in {rcc8, cardinal_direction}, canonical base relation(s) under that algebra. SPLIT mereotopological (contains/inside/touching/disjoint/overlap/partially-overlapping -> RCC-8 base symbols) from directional (left/right/above/below/diagonals/cardinals -> CDC tile names). Note: 3D directional front/behind is a separate axis NOT in standard 2D CDC -- record it but flag it as out-of-CDC vocabulary. Compute char-offset spans by locating each entity surface form in the story text (templated: exact string search; natural ReSQ/SpartQA-Human: use the provided SpRL trajector/landmark spans). The HELD-OUT QUERY edge = the dataset's question pair with its gold relation (FR answer for SpartQA; Targets for SpaRP; the YN pair+gold for ReSQ/StepGame -- for YN, record the asked relation + yes/no and, where the gold pairwise relation is recoverable from the scene graph, the gold base relation). Initialize the query edge as universal (it is NOT a stated KB edge if deduction-required).

  === PHASE 2: CRUCIAL DELIVERABLE -- DESCRIPTIVE MULTI-PATH-REDUNDANCY PREVALENCE (no closure, no LLM, no P/R) ===
  These are STRUCTURAL annotations of the data (like StepGame's existing k_hop field), NOT experimental results -- in-scope for a dataset artifact. For each held-out query edge compute, with networkx on G:
    - hop_length = shortest-path length between query endpoints (undirected projection of stated edges).
    - num_edge_disjoint_paths = max number of EDGE-DISJOINT paths between endpoints (networkx.edge_disjoint_paths / Menger max-flow).
    - cyclomatic_number mu = E - V + C on the subgraph induced by the union of the disjoint constraining paths (E edges, V nodes, C components).
    - deduction_required = the query pair is NOT a directly stated edge in G.
    - genuine_multipath_with_bite = deduction_required AND num_edge_disjoint_paths>=2 AND at least 2 of those disjoint paths have length>=2 (each requires composition, not a single stated edge). THIS is the spatial analog of the temporal a-priori N* gate -- it threads the needle between dense-but-trivially-closed and sparse-but-no-redundancy.
  Then emit a CORPUS-LEVEL PREVALENCE TABLE in the dataset card: per corpus (and per split), #evaluable held-out queries, fraction deduction-required, fraction with >=2 edge-disjoint paths, fraction genuine_multipath_with_bite, mean/median hop length, mean cyclomatic number, %>=3-edge-or-cyclic, plus is_templated / is_natural flags. Pre-state the same applicability bands the hypothesis uses (>=10% genuine_multipath_with_bite = general; 5-10% = useful module; <5% = niche) so iter-5 can read go/no-go directly. EXPECTATION (sanity check, not a target): SpaRTUN/SpaRP-PS1 and SpartQA-Auto HIGH; SpartQA-Human moderate; ReSQ LOW; StepGame clean ~0 (single chain). If even the dense templated corpora show low prevalence, that is itself the publishable finding that real multi-path redundancy is rare -- report it, do not massage.

  === PHASE 3: STANDARDIZE TO exp_sel_data_out SCHEMA (one row per scene/story) ===
  Mirror the temporal/CLUTRR gold-graph conventions (dossier art_aQ2Rf8rwqteI). Row schema:
  {
    "id": "<dataset>_<split>_<docid>_<queryidx>",
    "input": { "text": "<full story/scene text>", "doc_id": "<scene/image id>", "dataset": "<name>" },
    "output": {
      "nodes": [ {"node_id":"A", "surface":"the big circle", "char_spans":[[s,e],...], "mention_count":n}, ... ],
      "edges": [ {"src":"A","dst":"B","native_relation":"left of","algebra":"cardinal_direction","canonical":["W"],"is_universal_option":false,"src_span":[s,e],"rel_span":[s,e],"dst_span":[s,e]}, ... ],
      "query_edge": {"src":"X","dst":"Y","gold_native_relation":"...","gold_canonical":["..."],"gold_algebra":"rcc8|cardinal_direction","answer_kind":"FR|YN","yn_label":null|true|false,
                      "hop_length":k,"num_edge_disjoint_paths":p,"cyclomatic_number":mu,"deduction_required":bool,"genuine_multipath_with_bite":bool }
    },
    "metadata": { "is_templated":bool, "is_natural_text":bool, "split":"train|dev|test", "doc_char_len":int, "reaches_3000_char_target":bool,
                   "algebras_present":["rcc8","cardinal_direction"], "native_relation_vocab":[...], "license":"...", "source":"<hf id / url + commit>" },
    "fold": "<doc/scene-level fold id>"
  }
  Notes: canonical_disjunction holds the GOLD atomic relation(s) here (singleton for templated; the SpRL/annotation gold for natural) PLUS an explicit is_universal_option flag -- the LLM-read high-recall disjunction is produced later by the EXPERIMENT, not here. Folds = group by source scene/doc id (no scene spans two folds). Keep a frozen, deterministic fold map.

  === PHASE 4: VALIDATE + EMIT (aii-json, aii-file-size-limit) ===
  Write data.py (acquisition -> graph reconstruction -> multi-path annotation -> schema emit; deterministic, $0, no LLM; idempotent with a local download cache listed in upload-ignore). Emit data_out.json (full), data_out_mini.json, data_out_preview.json via aii-json; validate every row against a JSON Schema for the structure above; keep full output <=300MB (subsample templated giants -- e.g. cap SpaRP-PS2/SpaRTUN to a few thousand multi-path-bearing scenes -- but KEEP ALL natural ReSQ/SpartQA-Human and report any subsampling + the resulting null sizes honestly). Write dataset_card.md: the multi-path-redundancy prevalence table (Phase 2), per-corpus provenance + license + commit, the templated-vs-natural ledger, the document-length distribution vs the 3000-char target, and the per-algebra relation-vocabulary coverage (which native relations mapped to RCC-8 vs CDC vs were unmappable). State all honest caveats: StepGame clean has no multi-path by construction; ReSQ is shallow; SpaRTUN/SpaRP are templated; front/behind is out-of-standard-CDC; YN queries give a pair+label not always a clean FR gold.

  === FAILURE SCENARIOS + MITIGATIONS ===
  1. SpaRP scene-graph relations incomplete/ambiguous -> fall back to raw SpaRTUN (HLR/SpaRTUN, MIT) full stated-relation set; cross-check the two agree on a sample.
  2. mSpRL/ReSQ download gated or SpRL spans missing -> use the HLR-provided ReSQ release directly (questions+answers+context); if char-offsets cannot be recovered for natural text, store node surface forms with mention strings and set char_spans to [] with a metadata flag (do NOT fabricate offsets).
  3. Multi-path prevalence is LOW everywhere (likely for natural corpora) -> this is the expected, publishable a-priori result; ensure the dense templated arms (SpaRTUN/SpaRP-PS1, SpartQA-Auto) are well-sampled so iter-5 still has a high-redundancy synthetic-but-realistic-text venue, and report natural-corpus prevalence as the honest scope boundary.
  4. StepGame noise variants do/do-not add redundant paths -> resolve EMPIRICALLY via the edge-disjoint-path count; report the finding either way; never rely on the noise-type label.
  5. Directional relations dominate and RCC-8 edges are scarce in a corpus -> still record both, but flag in the card that this corpus's multi-path bite is mostly in the not-yet-engine-supported CDC algebra (informs next-iter engine extension priority).
  6. Size > 300MB -> subsample templated corpora to multi-path-bearing scenes first; log exact dropped counts.

  DELIVERABLES: data.py + data_out.json (full) + data_out_mini.json + data_out_preview.json + dataset_card.md (with the multi-path-redundancy prevalence table + provenance/licenses/caveats). Strictly $0, no LLM, descriptive-only.
target_num_datasets: 4
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
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 32 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 16 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 8 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-17 20:27:29 UTC

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

### [3] SYSTEM-USER prompt · 2026-06-17 21:04:38 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: >-
  SPATIAL multi-path-redundant gold-QCN corpus: a-priori redundancy-prevalence gate for iter-5's second real-venue cross-path-intersection
  test
summary: >-
  Build and standardize a spatial-reasoning corpus whose gold scene-graphs structurally HOST the paper's signature-but-still-synthetic-only
  mechanism: query pairs reachable via >=2 EDGE-DISJOINT constraining paths whose single-path compositions leave disjunctions
  that intersection narrows. Source 4-6 published spatial QA datasets (SpaRTUN/SpaRP-PS1 as the dense RCC-8+directional multi-path
  workhorse; SpartQA-Human as a semi-natural multi-path arm; ReSQ as the genuinely-natural anchor; StepGame as a single-chain
  cardinal-direction contrast/hop-length arm; SpartQA-Auto and SpaRP-PS2 as evaluated extras), reconstruct one gold relation-graph
  per scene (nodes=objects with surface+char-offset spans; edges=stated native relation -> canonical algebra, splitting MEREOTOPOLOGICAL->RCC-8
  [engine-validated] from DIRECTIONAL->cardinal-direction-calculus [vocab recorded for next-iter engine extension]; a held-out
  multi-hop query edge; doc/scene folds), and emit a DESCRIPTIVE-ONLY multi-path-redundancy prevalence table (per query: #edge-disjoint
  constraining paths, hop length, cyclomatic number; per corpus: fraction of deduction-required held-out queries with >=2
  disjoint paths AND each path length>=2 = the spatial analog of the temporal a-priori N* gate). No closure, no LLM, no derived
  P/R. Deliver data.py + full/mini/preview data_out.json (aii-json validated) + a dataset card with the prevalence table,
  provenance, licenses, and honest templated-vs-natural / document-length-vs-3000-char / relation-vocab-coverage caveats.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  An IDEAL source for this corpus is a published spatial-reasoning QA dataset that, per scene/story, lets us reconstruct a GOLD relation-graph rich enough to contain genuine multi-path redundancy. Concretely the criteria, in priority order:

  1. MULTI-PATH-REDUNDANT SCENE GRAPHS (the load-bearing property). The story must STATE many relations among the SAME set of objects so that two query objects are connected by >=2 EDGE-DISJOINT paths, each of length >=2 (so each path requires COMPOSITION, not a directly stated edge). This is the spatial analog of the temporal a-priori gate that dense temporal corpora lack (near-transitively-closed => full==naive, no iteration bite) and sparse ones barely have (~12 edges). DENSE scene graphs (SpaRTUN reports ~10 stated relations per 8-sentence story over NLVR scene graphs; SpartQA scenes have multiple blocks x multiple objects) are far more likely to host this than single-chain corpora (StepGame clean = one linear k-hop chain => exactly one path => NO redundancy by construction).

  2. RICH RELATION ALGEBRA the engine can already use. MEREOTOPOLOGICAL relations mapping to RCC-8 {DC,EC,PO,EQ,TPP,NTPP,TPPI,NTPPI} are immediately usable (the dossier art_aQ2Rf8rwqteI engine already validates RCC-8 composition). SpaRTUN/SpaRP topological relations ARE RCC-8 verbatim -> prioritize these. DIRECTIONAL relations (left/right/above/below + diagonals; cardinal N/S/E/W+NE/NW/SE/SW) map to the cardinal-direction calculus (CDC), which the engine does NOT yet implement -> the vocabulary is recorded for next-iter engine extension, not used for closure here.

  3. RECONSTRUCTABLE GOLD GRAPH WITH GROUND TRUTH. The dataset must expose, per scene: (a) the set of STATED relations (the KB edges an honest local reader would extract) -- ideally as an explicit scene-graph / SpRL-triplet / symbolic annotation, else parseable from templated text; (b) a held-out QUERY pair with a GOLD relation (the answer); (c) entity surface forms locatable in the text for char-offset spans.

  4. NATURAL / HUMAN-AUTHORED TEXT for the 'genuinely natural' claim (ReSQ real mSpRL descriptions; SpartQA-Human human-annotated), BALANCED with TEMPLATED sets for statistical power (SpaRTUN/SpaRP, SpartQA-Auto, StepGame) -- each flagged honestly in metadata. The whole point of the descriptive prevalence table is to tell iter-5, before any LLM spend, WHETHER natural multi-path redundancy exists or whether the mechanism stays synthetic-only.

  5. PRACTICAL: total download <=300MB, permissive license (MIT / CC-BY-SA-4.0 / Apache-2.0 / research-use), JSON or easily-parsed format, $0 (no LLM calls -- this is a pure data + graph-structure-analysis task). Document length should be reported against the project's ~3000-char target; expect ALL spatial corpora to fall short (SpaRP context 108-1270 chars; SpaRTUN ~91 tokens; StepGame short; ReSQ/mSpRL real image descriptions a few hundred chars) -- report this honestly.

  NON-ideal / disqualifying: corpora that only give isolated (premise, hypothesis, label) triples with no recoverable multi-object scene graph; pure single-chain corpora used as the ONLY source (they cannot host redundancy -- keep StepGame only as a contrast arm); image-only datasets with no textual descriptions.
dataset_search_plan: |-
  Compute profile cpu_heavy (4 vCPU/32GB). NO LLM calls anywhere ($0). Target ~6 candidates evaluated, best 4 standardized. Use aii-hf-datasets for HF pulls, direct GitHub/URL downloads otherwise; networkx for the graph-structure analysis; aii-json to validate + make mini/preview.

  === PHASE 0: ACQUIRE + VERIFY CANDIDATES (parallelizable) ===
  Download and inspect these VERIFIED sources (all confirmed to exist June 2026):

  A. SpaRP (PRIMARY easy path; dense, multi-path, scene-graph + symbolic already extracted). HF `UKPLab/sparp`, license cc-by-sa-4.0 (code Apache-2.0, repo github.com/UKPLab/acl2024-sparc-and-sparp). Configs: 'SpaRP-PS1 (SpaRTUN)' ~21.2k, 'SpaRP-PS2 (StepGame)' ~154k, PS3/PS4 (StepGame-Ext), plus 'small-' variants (~3.5k each). Per-row fields: Context (text, 108-1270 chars), Question, Targets (1-4 relations), Reasoning (verbalized deductive CoT), SYMBOLIC representations (context/entity-mappings/reasoning in formal notation) and SCENE-GRAPH relations in structured JSON. ** Use SpaRP-PS1 as the dense RCC-8+directional multi-path workhorse: its symbolic scene-graph gives the stated KB edges directly, no NLVR reconstruction needed.** Verbalized RCC-8 labels map: 'outside'->DC, 'outside and touching'->EC, 'partially overlapping'->PO, 'inside and touching'->TPP, 'inside'->NTPP, 'contains and touches'->TPPI, 'contains'->NTPPI, 'overlapping'/'equal'->EQ (VERIFY exact strings against the data); directional: left/right/above/below/behind/in front + near/far.

  B. SpaRTUN raw (alt source for the FULL stated-relation set if SpaRP's scene-graph is incomplete). GitHub `HLR/SpaRTUN` (MIT) + `HLR/Spatial-QA-tasks` + `HLR/SpaRTUNQChain` (the QChain repo ships reasoning chains + data). Has a `data_format.txt`; external 'Download SpaRTUN' link. Relations: directional LEFT/RIGHT/ABOVE/BELOW/BEHIND/FRONT + distance NEAR/FAR + RCC-8 DC/EC/PO/EQ/TPP/NTPP/TPPI/NTPPI. ~10 stated relations per 8-sentence/91-token story over 6,600 NLVR scene graphs; sizes ~20,334 YN + 18,400 FR train, ~3.1k dev/test each. Multi-hop (authors ignore length-1 paths, select most-step questions) => high multi-path prevalence expected.

  C. SpartQA. GitHub `HLR/SpartQA_generation`. Direct zips: SpartQA_Auto -> https://www.cse.msu.edu/~kordjams/data/SpartQA_Auto.zip ; SpartQA_Human -> https://www.cse.msu.edu/~kordjams/data/SpartQA_Human.zip . Each scene ships an 'Annotation' (scene graph of the scene) + 'SpRL' (spatial role/relation extraction) + main file (stories, questions, answers, candidate answers, consistency/contrast set). Question types: FR (find relation between two objects -- USE FR as the held-out query, its answer IS the relation), FB (find block), CO (choose object), YN (yes/no). Scenes = multiple blocks x multiple objects => dense graphs. Record exact relation vocabulary from the downloaded annotation/data_format files verbatim (directional + distance + topological touching/inside/contains/cover/disjoint). HF mirrors exist (`tasksource/spartqa-yn`, `mteb/SpartQA`) but prefer the official zips because they include the scene-graph annotation needed to reconstruct stated relations. ** SpartQA-Human = the semi-natural multi-path arm; SpartQA-Auto = an evaluated templated extra.**

  D. ReSQ (GENUINELY-NATURAL anchor). HLR group, built on the mSpRL corpus (real image descriptions) with HUMAN-generated YN questions; SpRL triplet annotations inherited from mSpRL give the stated relations. Sizes train 1,008 / dev 333 / test 610. Reasoning depth 1-2 + commonsense (=> EXPECT LOW multi-path prevalence -- report it honestly; this arm's value is establishing whether natural text hosts ANY redundancy). Find the download via HLR/Spatial-QA-tasks or the ReSQ external link on the SpaRTUN repo; mSpRL (SemEval-2012 Task 3 / CLEF IAPR) for the underlying text if needed.

  E. StepGame (single-chain CONTRAST + hop-length). HF `michaelszx/StepGame` and `ZhengyanShi/StepGame`; GitHub `ZhengxiangShi/StepGame` (Dataset/TrainVersion 50k/1k; Dataset/CompleteVersion 30k train/1k val/30k test PER k=1..10). 8 cardinal relations: north, south, east, west, northeast, northwest, southeast, southwest (=> ALL cardinal-direction-calculus, NO mereotopological). Clean test stories = SINGLE LINEAR CHAINS (one path, no cycles) => multi-path prevalence ~0 by construction. Noise types reported as 'disconnected'/'irrelevant'/'supporting'; ** do NOT trust the label 'supporting'=='redundant paths' -- VERIFY EMPIRICALLY by reconstructing the graph and counting edge-disjoint paths.** Keep StepGame primarily as the single-chain contrast that shows where redundancy is absent (the sparse-corpus failure mode). Verify the license on the HF card / repo (research-use; record whatever it states).

  For EACH candidate, verify and log: exact HF id / repo URL + commit, license, on-disk size (<=300MB), file format, fields, splits, native relation vocabulary (verbatim), and whether a per-scene stated-relation set is recoverable. If a primary source is unreachable, fall back: SpaRP<->SpaRTUN raw (same underlying data); SpartQA zips<->HF mirrors; ReSQ<->mSpRL+regenerate; StepGame HF<->GitHub.

  === PHASE 1: RECONSTRUCT GOLD RELATION-GRAPHS ===
  For every scene/story build a directed multigraph G: nodes = objects/entities (dedup mentions to a canonical node id), edges = each STATED relation (the KB edges an honest local reader would extract). Edge attributes: native_relation (verbatim), algebra in {rcc8, cardinal_direction}, canonical base relation(s) under that algebra. SPLIT mereotopological (contains/inside/touching/disjoint/overlap/partially-overlapping -> RCC-8 base symbols) from directional (left/right/above/below/diagonals/cardinals -> CDC tile names). Note: 3D directional front/behind is a separate axis NOT in standard 2D CDC -- record it but flag it as out-of-CDC vocabulary. Compute char-offset spans by locating each entity surface form in the story text (templated: exact string search; natural ReSQ/SpartQA-Human: use the provided SpRL trajector/landmark spans). The HELD-OUT QUERY edge = the dataset's question pair with its gold relation (FR answer for SpartQA; Targets for SpaRP; the YN pair+gold for ReSQ/StepGame -- for YN, record the asked relation + yes/no and, where the gold pairwise relation is recoverable from the scene graph, the gold base relation). Initialize the query edge as universal (it is NOT a stated KB edge if deduction-required).

  === PHASE 2: CRUCIAL DELIVERABLE -- DESCRIPTIVE MULTI-PATH-REDUNDANCY PREVALENCE (no closure, no LLM, no P/R) ===
  These are STRUCTURAL annotations of the data (like StepGame's existing k_hop field), NOT experimental results -- in-scope for a dataset artifact. For each held-out query edge compute, with networkx on G:
    - hop_length = shortest-path length between query endpoints (undirected projection of stated edges).
    - num_edge_disjoint_paths = max number of EDGE-DISJOINT paths between endpoints (networkx.edge_disjoint_paths / Menger max-flow).
    - cyclomatic_number mu = E - V + C on the subgraph induced by the union of the disjoint constraining paths (E edges, V nodes, C components).
    - deduction_required = the query pair is NOT a directly stated edge in G.
    - genuine_multipath_with_bite = deduction_required AND num_edge_disjoint_paths>=2 AND at least 2 of those disjoint paths have length>=2 (each requires composition, not a single stated edge). THIS is the spatial analog of the temporal a-priori N* gate -- it threads the needle between dense-but-trivially-closed and sparse-but-no-redundancy.
  Then emit a CORPUS-LEVEL PREVALENCE TABLE in the dataset card: per corpus (and per split), #evaluable held-out queries, fraction deduction-required, fraction with >=2 edge-disjoint paths, fraction genuine_multipath_with_bite, mean/median hop length, mean cyclomatic number, %>=3-edge-or-cyclic, plus is_templated / is_natural flags. Pre-state the same applicability bands the hypothesis uses (>=10% genuine_multipath_with_bite = general; 5-10% = useful module; <5% = niche) so iter-5 can read go/no-go directly. EXPECTATION (sanity check, not a target): SpaRTUN/SpaRP-PS1 and SpartQA-Auto HIGH; SpartQA-Human moderate; ReSQ LOW; StepGame clean ~0 (single chain). If even the dense templated corpora show low prevalence, that is itself the publishable finding that real multi-path redundancy is rare -- report it, do not massage.

  === PHASE 3: STANDARDIZE TO exp_sel_data_out SCHEMA (one row per scene/story) ===
  Mirror the temporal/CLUTRR gold-graph conventions (dossier art_aQ2Rf8rwqteI). Row schema:
  {
    "id": "<dataset>_<split>_<docid>_<queryidx>",
    "input": { "text": "<full story/scene text>", "doc_id": "<scene/image id>", "dataset": "<name>" },
    "output": {
      "nodes": [ {"node_id":"A", "surface":"the big circle", "char_spans":[[s,e],...], "mention_count":n}, ... ],
      "edges": [ {"src":"A","dst":"B","native_relation":"left of","algebra":"cardinal_direction","canonical":["W"],"is_universal_option":false,"src_span":[s,e],"rel_span":[s,e],"dst_span":[s,e]}, ... ],
      "query_edge": {"src":"X","dst":"Y","gold_native_relation":"...","gold_canonical":["..."],"gold_algebra":"rcc8|cardinal_direction","answer_kind":"FR|YN","yn_label":null|true|false,
                      "hop_length":k,"num_edge_disjoint_paths":p,"cyclomatic_number":mu,"deduction_required":bool,"genuine_multipath_with_bite":bool }
    },
    "metadata": { "is_templated":bool, "is_natural_text":bool, "split":"train|dev|test", "doc_char_len":int, "reaches_3000_char_target":bool,
                   "algebras_present":["rcc8","cardinal_direction"], "native_relation_vocab":[...], "license":"...", "source":"<hf id / url + commit>" },
    "fold": "<doc/scene-level fold id>"
  }
  Notes: canonical_disjunction holds the GOLD atomic relation(s) here (singleton for templated; the SpRL/annotation gold for natural) PLUS an explicit is_universal_option flag -- the LLM-read high-recall disjunction is produced later by the EXPERIMENT, not here. Folds = group by source scene/doc id (no scene spans two folds). Keep a frozen, deterministic fold map.

  === PHASE 4: VALIDATE + EMIT (aii-json, aii-file-size-limit) ===
  Write data.py (acquisition -> graph reconstruction -> multi-path annotation -> schema emit; deterministic, $0, no LLM; idempotent with a local download cache listed in upload-ignore). Emit data_out.json (full), data_out_mini.json, data_out_preview.json via aii-json; validate every row against a JSON Schema for the structure above; keep full output <=300MB (subsample templated giants -- e.g. cap SpaRP-PS2/SpaRTUN to a few thousand multi-path-bearing scenes -- but KEEP ALL natural ReSQ/SpartQA-Human and report any subsampling + the resulting null sizes honestly). Write dataset_card.md: the multi-path-redundancy prevalence table (Phase 2), per-corpus provenance + license + commit, the templated-vs-natural ledger, the document-length distribution vs the 3000-char target, and the per-algebra relation-vocabulary coverage (which native relations mapped to RCC-8 vs CDC vs were unmappable). State all honest caveats: StepGame clean has no multi-path by construction; ReSQ is shallow; SpaRTUN/SpaRP are templated; front/behind is out-of-standard-CDC; YN queries give a pair+label not always a clean FR gold.

  === FAILURE SCENARIOS + MITIGATIONS ===
  1. SpaRP scene-graph relations incomplete/ambiguous -> fall back to raw SpaRTUN (HLR/SpaRTUN, MIT) full stated-relation set; cross-check the two agree on a sample.
  2. mSpRL/ReSQ download gated or SpRL spans missing -> use the HLR-provided ReSQ release directly (questions+answers+context); if char-offsets cannot be recovered for natural text, store node surface forms with mention strings and set char_spans to [] with a metadata flag (do NOT fabricate offsets).
  3. Multi-path prevalence is LOW everywhere (likely for natural corpora) -> this is the expected, publishable a-priori result; ensure the dense templated arms (SpaRTUN/SpaRP-PS1, SpartQA-Auto) are well-sampled so iter-5 still has a high-redundancy synthetic-but-realistic-text venue, and report natural-corpus prevalence as the honest scope boundary.
  4. StepGame noise variants do/do-not add redundant paths -> resolve EMPIRICALLY via the edge-disjoint-path count; report the finding either way; never rely on the noise-type label.
  5. Directional relations dominate and RCC-8 edges are scarce in a corpus -> still record both, but flag in the card that this corpus's multi-path bite is mostly in the not-yet-engine-supported CDC algebra (informs next-iter engine extension priority).
  6. Size > 300MB -> subsample templated corpora to multi-path-bearing scenes first; log exact dropped counts.

  DELIVERABLES: data.py + data_out.json (full) + data_out_mini.json + data_out_preview.json + dataset_card.md (with the multi-path-redundancy prevalence table + provenance/licenses/caveats). Strictly $0, no LLM, descriptive-only.
target_num_datasets: 4
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
TODO 1. For the top 8 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

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
TODO 3. Read preview to inspect examples. Choose THE BEST 4 DATASETS based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [4] SYSTEM-USER prompt · 2026-06-17 21:09:09 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_4/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: >-
  SPATIAL multi-path-redundant gold-QCN corpus: a-priori redundancy-prevalence gate for iter-5's second real-venue cross-path-intersection
  test
summary: >-
  Build and standardize a spatial-reasoning corpus whose gold scene-graphs structurally HOST the paper's signature-but-still-synthetic-only
  mechanism: query pairs reachable via >=2 EDGE-DISJOINT constraining paths whose single-path compositions leave disjunctions
  that intersection narrows. Source 4-6 published spatial QA datasets (SpaRTUN/SpaRP-PS1 as the dense RCC-8+directional multi-path
  workhorse; SpartQA-Human as a semi-natural multi-path arm; ReSQ as the genuinely-natural anchor; StepGame as a single-chain
  cardinal-direction contrast/hop-length arm; SpartQA-Auto and SpaRP-PS2 as evaluated extras), reconstruct one gold relation-graph
  per scene (nodes=objects with surface+char-offset spans; edges=stated native relation -> canonical algebra, splitting MEREOTOPOLOGICAL->RCC-8
  [engine-validated] from DIRECTIONAL->cardinal-direction-calculus [vocab recorded for next-iter engine extension]; a held-out
  multi-hop query edge; doc/scene folds), and emit a DESCRIPTIVE-ONLY multi-path-redundancy prevalence table (per query: #edge-disjoint
  constraining paths, hop length, cyclomatic number; per corpus: fraction of deduction-required held-out queries with >=2
  disjoint paths AND each path length>=2 = the spatial analog of the temporal a-priori N* gate). No closure, no LLM, no derived
  P/R. Deliver data.py + full/mini/preview data_out.json (aii-json validated) + a dataset card with the prevalence table,
  provenance, licenses, and honest templated-vs-natural / document-length-vs-3000-char / relation-vocab-coverage caveats.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  An IDEAL source for this corpus is a published spatial-reasoning QA dataset that, per scene/story, lets us reconstruct a GOLD relation-graph rich enough to contain genuine multi-path redundancy. Concretely the criteria, in priority order:

  1. MULTI-PATH-REDUNDANT SCENE GRAPHS (the load-bearing property). The story must STATE many relations among the SAME set of objects so that two query objects are connected by >=2 EDGE-DISJOINT paths, each of length >=2 (so each path requires COMPOSITION, not a directly stated edge). This is the spatial analog of the temporal a-priori gate that dense temporal corpora lack (near-transitively-closed => full==naive, no iteration bite) and sparse ones barely have (~12 edges). DENSE scene graphs (SpaRTUN reports ~10 stated relations per 8-sentence story over NLVR scene graphs; SpartQA scenes have multiple blocks x multiple objects) are far more likely to host this than single-chain corpora (StepGame clean = one linear k-hop chain => exactly one path => NO redundancy by construction).

  2. RICH RELATION ALGEBRA the engine can already use. MEREOTOPOLOGICAL relations mapping to RCC-8 {DC,EC,PO,EQ,TPP,NTPP,TPPI,NTPPI} are immediately usable (the dossier art_aQ2Rf8rwqteI engine already validates RCC-8 composition). SpaRTUN/SpaRP topological relations ARE RCC-8 verbatim -> prioritize these. DIRECTIONAL relations (left/right/above/below + diagonals; cardinal N/S/E/W+NE/NW/SE/SW) map to the cardinal-direction calculus (CDC), which the engine does NOT yet implement -> the vocabulary is recorded for next-iter engine extension, not used for closure here.

  3. RECONSTRUCTABLE GOLD GRAPH WITH GROUND TRUTH. The dataset must expose, per scene: (a) the set of STATED relations (the KB edges an honest local reader would extract) -- ideally as an explicit scene-graph / SpRL-triplet / symbolic annotation, else parseable from templated text; (b) a held-out QUERY pair with a GOLD relation (the answer); (c) entity surface forms locatable in the text for char-offset spans.

  4. NATURAL / HUMAN-AUTHORED TEXT for the 'genuinely natural' claim (ReSQ real mSpRL descriptions; SpartQA-Human human-annotated), BALANCED with TEMPLATED sets for statistical power (SpaRTUN/SpaRP, SpartQA-Auto, StepGame) -- each flagged honestly in metadata. The whole point of the descriptive prevalence table is to tell iter-5, before any LLM spend, WHETHER natural multi-path redundancy exists or whether the mechanism stays synthetic-only.

  5. PRACTICAL: total download <=300MB, permissive license (MIT / CC-BY-SA-4.0 / Apache-2.0 / research-use), JSON or easily-parsed format, $0 (no LLM calls -- this is a pure data + graph-structure-analysis task). Document length should be reported against the project's ~3000-char target; expect ALL spatial corpora to fall short (SpaRP context 108-1270 chars; SpaRTUN ~91 tokens; StepGame short; ReSQ/mSpRL real image descriptions a few hundred chars) -- report this honestly.

  NON-ideal / disqualifying: corpora that only give isolated (premise, hypothesis, label) triples with no recoverable multi-object scene graph; pure single-chain corpora used as the ONLY source (they cannot host redundancy -- keep StepGame only as a contrast arm); image-only datasets with no textual descriptions.
dataset_search_plan: |-
  Compute profile cpu_heavy (4 vCPU/32GB). NO LLM calls anywhere ($0). Target ~6 candidates evaluated, best 4 standardized. Use aii-hf-datasets for HF pulls, direct GitHub/URL downloads otherwise; networkx for the graph-structure analysis; aii-json to validate + make mini/preview.

  === PHASE 0: ACQUIRE + VERIFY CANDIDATES (parallelizable) ===
  Download and inspect these VERIFIED sources (all confirmed to exist June 2026):

  A. SpaRP (PRIMARY easy path; dense, multi-path, scene-graph + symbolic already extracted). HF `UKPLab/sparp`, license cc-by-sa-4.0 (code Apache-2.0, repo github.com/UKPLab/acl2024-sparc-and-sparp). Configs: 'SpaRP-PS1 (SpaRTUN)' ~21.2k, 'SpaRP-PS2 (StepGame)' ~154k, PS3/PS4 (StepGame-Ext), plus 'small-' variants (~3.5k each). Per-row fields: Context (text, 108-1270 chars), Question, Targets (1-4 relations), Reasoning (verbalized deductive CoT), SYMBOLIC representations (context/entity-mappings/reasoning in formal notation) and SCENE-GRAPH relations in structured JSON. ** Use SpaRP-PS1 as the dense RCC-8+directional multi-path workhorse: its symbolic scene-graph gives the stated KB edges directly, no NLVR reconstruction needed.** Verbalized RCC-8 labels map: 'outside'->DC, 'outside and touching'->EC, 'partially overlapping'->PO, 'inside and touching'->TPP, 'inside'->NTPP, 'contains and touches'->TPPI, 'contains'->NTPPI, 'overlapping'/'equal'->EQ (VERIFY exact strings against the data); directional: left/right/above/below/behind/in front + near/far.

  B. SpaRTUN raw (alt source for the FULL stated-relation set if SpaRP's scene-graph is incomplete). GitHub `HLR/SpaRTUN` (MIT) + `HLR/Spatial-QA-tasks` + `HLR/SpaRTUNQChain` (the QChain repo ships reasoning chains + data). Has a `data_format.txt`; external 'Download SpaRTUN' link. Relations: directional LEFT/RIGHT/ABOVE/BELOW/BEHIND/FRONT + distance NEAR/FAR + RCC-8 DC/EC/PO/EQ/TPP/NTPP/TPPI/NTPPI. ~10 stated relations per 8-sentence/91-token story over 6,600 NLVR scene graphs; sizes ~20,334 YN + 18,400 FR train, ~3.1k dev/test each. Multi-hop (authors ignore length-1 paths, select most-step questions) => high multi-path prevalence expected.

  C. SpartQA. GitHub `HLR/SpartQA_generation`. Direct zips: SpartQA_Auto -> https://www.cse.msu.edu/~kordjams/data/SpartQA_Auto.zip ; SpartQA_Human -> https://www.cse.msu.edu/~kordjams/data/SpartQA_Human.zip . Each scene ships an 'Annotation' (scene graph of the scene) + 'SpRL' (spatial role/relation extraction) + main file (stories, questions, answers, candidate answers, consistency/contrast set). Question types: FR (find relation between two objects -- USE FR as the held-out query, its answer IS the relation), FB (find block), CO (choose object), YN (yes/no). Scenes = multiple blocks x multiple objects => dense graphs. Record exact relation vocabulary from the downloaded annotation/data_format files verbatim (directional + distance + topological touching/inside/contains/cover/disjoint). HF mirrors exist (`tasksource/spartqa-yn`, `mteb/SpartQA`) but prefer the official zips because they include the scene-graph annotation needed to reconstruct stated relations. ** SpartQA-Human = the semi-natural multi-path arm; SpartQA-Auto = an evaluated templated extra.**

  D. ReSQ (GENUINELY-NATURAL anchor). HLR group, built on the mSpRL corpus (real image descriptions) with HUMAN-generated YN questions; SpRL triplet annotations inherited from mSpRL give the stated relations. Sizes train 1,008 / dev 333 / test 610. Reasoning depth 1-2 + commonsense (=> EXPECT LOW multi-path prevalence -- report it honestly; this arm's value is establishing whether natural text hosts ANY redundancy). Find the download via HLR/Spatial-QA-tasks or the ReSQ external link on the SpaRTUN repo; mSpRL (SemEval-2012 Task 3 / CLEF IAPR) for the underlying text if needed.

  E. StepGame (single-chain CONTRAST + hop-length). HF `michaelszx/StepGame` and `ZhengyanShi/StepGame`; GitHub `ZhengxiangShi/StepGame` (Dataset/TrainVersion 50k/1k; Dataset/CompleteVersion 30k train/1k val/30k test PER k=1..10). 8 cardinal relations: north, south, east, west, northeast, northwest, southeast, southwest (=> ALL cardinal-direction-calculus, NO mereotopological). Clean test stories = SINGLE LINEAR CHAINS (one path, no cycles) => multi-path prevalence ~0 by construction. Noise types reported as 'disconnected'/'irrelevant'/'supporting'; ** do NOT trust the label 'supporting'=='redundant paths' -- VERIFY EMPIRICALLY by reconstructing the graph and counting edge-disjoint paths.** Keep StepGame primarily as the single-chain contrast that shows where redundancy is absent (the sparse-corpus failure mode). Verify the license on the HF card / repo (research-use; record whatever it states).

  For EACH candidate, verify and log: exact HF id / repo URL + commit, license, on-disk size (<=300MB), file format, fields, splits, native relation vocabulary (verbatim), and whether a per-scene stated-relation set is recoverable. If a primary source is unreachable, fall back: SpaRP<->SpaRTUN raw (same underlying data); SpartQA zips<->HF mirrors; ReSQ<->mSpRL+regenerate; StepGame HF<->GitHub.

  === PHASE 1: RECONSTRUCT GOLD RELATION-GRAPHS ===
  For every scene/story build a directed multigraph G: nodes = objects/entities (dedup mentions to a canonical node id), edges = each STATED relation (the KB edges an honest local reader would extract). Edge attributes: native_relation (verbatim), algebra in {rcc8, cardinal_direction}, canonical base relation(s) under that algebra. SPLIT mereotopological (contains/inside/touching/disjoint/overlap/partially-overlapping -> RCC-8 base symbols) from directional (left/right/above/below/diagonals/cardinals -> CDC tile names). Note: 3D directional front/behind is a separate axis NOT in standard 2D CDC -- record it but flag it as out-of-CDC vocabulary. Compute char-offset spans by locating each entity surface form in the story text (templated: exact string search; natural ReSQ/SpartQA-Human: use the provided SpRL trajector/landmark spans). The HELD-OUT QUERY edge = the dataset's question pair with its gold relation (FR answer for SpartQA; Targets for SpaRP; the YN pair+gold for ReSQ/StepGame -- for YN, record the asked relation + yes/no and, where the gold pairwise relation is recoverable from the scene graph, the gold base relation). Initialize the query edge as universal (it is NOT a stated KB edge if deduction-required).

  === PHASE 2: CRUCIAL DELIVERABLE -- DESCRIPTIVE MULTI-PATH-REDUNDANCY PREVALENCE (no closure, no LLM, no P/R) ===
  These are STRUCTURAL annotations of the data (like StepGame's existing k_hop field), NOT experimental results -- in-scope for a dataset artifact. For each held-out query edge compute, with networkx on G:
    - hop_length = shortest-path length between query endpoints (undirected projection of stated edges).
    - num_edge_disjoint_paths = max number of EDGE-DISJOINT paths between endpoints (networkx.edge_disjoint_paths / Menger max-flow).
    - cyclomatic_number mu = E - V + C on the subgraph induced by the union of the disjoint constraining paths (E edges, V nodes, C components).
    - deduction_required = the query pair is NOT a directly stated edge in G.
    - genuine_multipath_with_bite = deduction_required AND num_edge_disjoint_paths>=2 AND at least 2 of those disjoint paths have length>=2 (each requires composition, not a single stated edge). THIS is the spatial analog of the temporal a-priori N* gate -- it threads the needle between dense-but-trivially-closed and sparse-but-no-redundancy.
  Then emit a CORPUS-LEVEL PREVALENCE TABLE in the dataset card: per corpus (and per split), #evaluable held-out queries, fraction deduction-required, fraction with >=2 edge-disjoint paths, fraction genuine_multipath_with_bite, mean/median hop length, mean cyclomatic number, %>=3-edge-or-cyclic, plus is_templated / is_natural flags. Pre-state the same applicability bands the hypothesis uses (>=10% genuine_multipath_with_bite = general; 5-10% = useful module; <5% = niche) so iter-5 can read go/no-go directly. EXPECTATION (sanity check, not a target): SpaRTUN/SpaRP-PS1 and SpartQA-Auto HIGH; SpartQA-Human moderate; ReSQ LOW; StepGame clean ~0 (single chain). If even the dense templated corpora show low prevalence, that is itself the publishable finding that real multi-path redundancy is rare -- report it, do not massage.

  === PHASE 3: STANDARDIZE TO exp_sel_data_out SCHEMA (one row per scene/story) ===
  Mirror the temporal/CLUTRR gold-graph conventions (dossier art_aQ2Rf8rwqteI). Row schema:
  {
    "id": "<dataset>_<split>_<docid>_<queryidx>",
    "input": { "text": "<full story/scene text>", "doc_id": "<scene/image id>", "dataset": "<name>" },
    "output": {
      "nodes": [ {"node_id":"A", "surface":"the big circle", "char_spans":[[s,e],...], "mention_count":n}, ... ],
      "edges": [ {"src":"A","dst":"B","native_relation":"left of","algebra":"cardinal_direction","canonical":["W"],"is_universal_option":false,"src_span":[s,e],"rel_span":[s,e],"dst_span":[s,e]}, ... ],
      "query_edge": {"src":"X","dst":"Y","gold_native_relation":"...","gold_canonical":["..."],"gold_algebra":"rcc8|cardinal_direction","answer_kind":"FR|YN","yn_label":null|true|false,
                      "hop_length":k,"num_edge_disjoint_paths":p,"cyclomatic_number":mu,"deduction_required":bool,"genuine_multipath_with_bite":bool }
    },
    "metadata": { "is_templated":bool, "is_natural_text":bool, "split":"train|dev|test", "doc_char_len":int, "reaches_3000_char_target":bool,
                   "algebras_present":["rcc8","cardinal_direction"], "native_relation_vocab":[...], "license":"...", "source":"<hf id / url + commit>" },
    "fold": "<doc/scene-level fold id>"
  }
  Notes: canonical_disjunction holds the GOLD atomic relation(s) here (singleton for templated; the SpRL/annotation gold for natural) PLUS an explicit is_universal_option flag -- the LLM-read high-recall disjunction is produced later by the EXPERIMENT, not here. Folds = group by source scene/doc id (no scene spans two folds). Keep a frozen, deterministic fold map.

  === PHASE 4: VALIDATE + EMIT (aii-json, aii-file-size-limit) ===
  Write data.py (acquisition -> graph reconstruction -> multi-path annotation -> schema emit; deterministic, $0, no LLM; idempotent with a local download cache listed in upload-ignore). Emit data_out.json (full), data_out_mini.json, data_out_preview.json via aii-json; validate every row against a JSON Schema for the structure above; keep full output <=300MB (subsample templated giants -- e.g. cap SpaRP-PS2/SpaRTUN to a few thousand multi-path-bearing scenes -- but KEEP ALL natural ReSQ/SpartQA-Human and report any subsampling + the resulting null sizes honestly). Write dataset_card.md: the multi-path-redundancy prevalence table (Phase 2), per-corpus provenance + license + commit, the templated-vs-natural ledger, the document-length distribution vs the 3000-char target, and the per-algebra relation-vocabulary coverage (which native relations mapped to RCC-8 vs CDC vs were unmappable). State all honest caveats: StepGame clean has no multi-path by construction; ReSQ is shallow; SpaRTUN/SpaRP are templated; front/behind is out-of-standard-CDC; YN queries give a pair+label not always a clean FR gold.

  === FAILURE SCENARIOS + MITIGATIONS ===
  1. SpaRP scene-graph relations incomplete/ambiguous -> fall back to raw SpaRTUN (HLR/SpaRTUN, MIT) full stated-relation set; cross-check the two agree on a sample.
  2. mSpRL/ReSQ download gated or SpRL spans missing -> use the HLR-provided ReSQ release directly (questions+answers+context); if char-offsets cannot be recovered for natural text, store node surface forms with mention strings and set char_spans to [] with a metadata flag (do NOT fabricate offsets).
  3. Multi-path prevalence is LOW everywhere (likely for natural corpora) -> this is the expected, publishable a-priori result; ensure the dense templated arms (SpaRTUN/SpaRP-PS1, SpartQA-Auto) are well-sampled so iter-5 still has a high-redundancy synthetic-but-realistic-text venue, and report natural-corpus prevalence as the honest scope boundary.
  4. StepGame noise variants do/do-not add redundant paths -> resolve EMPIRICALLY via the edge-disjoint-path count; report the finding either way; never rely on the noise-type label.
  5. Directional relations dominate and RCC-8 edges are scarce in a corpus -> still record both, but flag in the card that this corpus's multi-path bite is mostly in the not-yet-engine-supported CDC algebra (informs next-iter engine extension priority).
  6. Size > 300MB -> subsample templated corpora to multi-path-bearing scenes first; log exact dropped counts.

  DELIVERABLES: data.py + data_out.json (full) + data_out_mini.json + data_out_preview.json + dataset_card.md (with the multi-path-redundancy prevalence table + provenance/licenses/caveats). Strictly $0, no LLM, descriptive-only.
target_num_datasets: 4
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
TODO 1. Update data.py to only include the chosen 4 datasets and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
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
