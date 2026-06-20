# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-17 15:37:59 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
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
  CLUTRR kinship gold graphs as the clean end-to-end venue (frozen, schema-validated, hop-stratified, with absent-relation
  pairs)
summary: >-
  Acquire the CLUTRR (Sinha et al. 2019) systematic-generalization and disconnected-noise splits and standardize them to the
  exp_sel_data_out JSON schema, ONE row per story. Each row carries input=the de-bracketed narrative and output=json.dumps(gold_graph)
  where the gold graph = entity nodes (with surface name, gender, mention char-spans) + atomic kinship edges (story_edges
  x edge_types, each a 1-hop directly-stated fact) + the held-out QUERY edge (is_query=true, hop_count=chain length, gold
  relation) + a set of structurally ABSENT-relation entity pairs (different connected components => no kinship path) for the
  hallucination demo. Per-row metadata carries hop-count, the constituent atomic facts (for atomic-extraction P/R), the gold
  backward-chaining proof chain (the human-auditable trace-graph gold), noise type, genders, graph descriptors, and a train/dev/test
  fold. Top-level metadata carries the finite kinship COMPOSITION TABLE (abstract relation types + gendered surface map +
  composition rules read verbatim from facebookresearch/clutrr's rules_store.yaml / relations_store.yaml), explicitly noting
  it is a composition table, NOT a full relation algebra. Acquisition is bulletproof: download the CSVs directly from the
  GitHub raw mirror that HF's own loader points at; no datasets-script trust_remote_code needed. Report DESCRIPTIVE counts
  only (stories, entities, edges, hop-count and relation-label distributions, component counts, absent-pair counts, story
  char-lengths). Do NOT run any composition/closure or compute derived statistics. Reproduce via data.py + pinned pyproject.toml.
  Tiny (<60MB total), trivially under 300MB. Sits beside the iter-1 temporal (NarrativeTime/TDDMan/MATRES) and synthetic-QCN
  corpora as the third corpus family.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  An ideal delivered CLUTRR corpus is a per-story gold KINSHIP relation graph over short, professionally-readable family narratives,
  standardized so iter-3 can deliver — in ONE setting — all four numbers the umbrella paper names: (i) atomic-extraction precision/recall,
  (ii) multi-hop deduction accuracy vs chain length, (iii) a human-auditable trace-graph, and (iv) a quantified hallucination-rate
  reduction on absent-relation queries. Concretely each delivered example must have: (1) input = the natural-language story
  (entity-bracket markers REMOVED, natural prose), ~tens-to-~3000 chars (longer chains approach the umbrella's ~3000-char
  target); (2) recoverable ENTITY NODES, each carrying a stable integer entity_id (the CLUTRR graph node index), surface name,
  gender (male/female), and the list of mention character-spans into the input text; (3) ATOMIC EDGES = the directly-stated
  kinship facts (one per story_edges entry), each {source_id, target_id, kinship_relation (gendered surface form, e.g. 'father','sister'),
  relation_type (abstract type, e.g. inv-child, sibling), is_query=false, hop_count=1}; (4) exactly ONE held-out QUERY edge
  {source_id, target_id, kinship_relation=target_text, target_int, is_query=true, hop_count=chain length} whose relation is
  NOT stated in the story and must be deduced by composing >=2 atomic edges; (5) a set of ABSENT-RELATION query pairs = entity
  pairs lying in DIFFERENT connected components of the story graph (no kinship path => honest gold label 'no-relation'), present
  in disconnected-noise stories, for the hallucination demo; (6) the gold backward-chaining PROOF chain (ordered atomic triples
  that compose to the query) as trace-graph gold; (7) per-example metadata: hop_count, noise_type {none,irrelevant,supporting,disconnected},
  task_name, f_comb (relation chain), genders map, graph descriptors (n_entities, n_edges, n_components), absent_pair_count;
  (8) a documented train/dev/test fold (each story is an independent document, so the native CLUTRR split is already document-disjoint).
  Top-level (shared, emitted ONCE): the finite kinship composition table = the 10-11 abstract relation TYPES (child, inv-child,
  SO, sibling, grand, inv-grand, un, inv-un, in-law, inv-in-law, sibling-in-law) with inverse/symmetry flags; the (type x
  gender)->surface-word map; the composition rules rules[t1][t2]=t3 (A t1 B, B t2 C => A t3 C; surface of t3 uses gender of
  C); and the int<->text label map (0..20). The data must span hop-counts 2..10 (for the multi-hop-vs-length curve) and include
  a disconnected-noise slice (for genuine within-document absent pairs). All CLUTRR splits are tiny (a few thousand rows,
  ~15-30MB each), trivially under 300MB. Prefer the canonical kliang5/CLUTRR_huggingface_dataset CSV mirror (the exact source
  HF's CLUTRR/v1 loader downloads) so the gold graph fields (story_edges, edge_types, query_edge, genders, proof_state) come
  pre-parsed rather than re-derived.
dataset_search_plan: "Deliver EXACTLY 2 CLUTRR slices as separate dataset entries (one optional 3rd noted at the end). Both\
  \ come from the SAME source and share schema/composition-table; they differ only in role. CORE = gen_train234_test2to10\
  \ (clean, hop-counts 2-10 in test; hosts atomic-extraction P/R + multi-hop-accuracy-vs-length + trace-graph). ABSENT = rob_train_disc_23_test_all_23\
  \ (disconnected-noise; supplies genuine within-document absent-relation pairs for the hallucination demo). The hard part\
  \ is NOT downloading (CSV is trivial) — it is faithfully reconstructing the per-story gold graph (node_id->name mapping,\
  \ mention spans, atomic facts, proof chain, absent pairs) and emitting the canonical composition table.\n\n=== STEP 0: ACQUISITION\
  \ (bulletproof; no datasets-library script loading) ===\nHF dataset CLUTRR/v1 ships ONLY a loader script v1.py and NO data\
  \ files; v1.py downloads CSVs from the raw GitHub mirror: _URL='https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/'\
  \ and for each config fetches {config}/train.csv, {config}/validation.csv, {config}/test.csv. PRIMARY PATH (use this): download\
  \ those CSVs DIRECTLY with requests + pandas.read_csv — NO datasets library, NO trust_remote_code. URLs:\n  base = 'https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/'\n\
  \  for config in ['gen_train234_test2to10','rob_train_disc_23_test_all_23']:\n    for split in ['train','validation','test']:\
  \ df = pd.read_csv(base + config + '/' + split + '.csv')\nColumns (CONFIRMED, all strings except target=int32): id, story,\
  \ query, target, target_text, clean_story, proof_state, f_comb, task_name, story_edges, edge_types, query_edge, genders,\
  \ task_split. Sizes (CONFIRMED): gen_train234_test2to10 = train 12064 / val 3019 / test 1048 (~30MB); rob_train_disc_23_test_all_23\
  \ = train 8080 / val 2020 / test 445 (~17MB). FALLBACK A: load_dataset('CLUTRR/v1', config, trust_remote_code=True) with\
  \ datasets pinned <3.0 (e.g. datasets==2.21.0) — works but heavier. FALLBACK B: clone the kliang5 repo via git or huggingface_hub\
  \ if raw.githubusercontent rate-limits. FALLBACK C: the original facebookresearch/clutrr generator + its pre-generated Google-Drive\
  \ zip (fragile in headless; last resort). Verify row counts against the CONFIRMED sizes above; if a config 404s, re-fetch\
  \ v1.py (https://huggingface.co/datasets/CLUTRR/v1/raw/main/v1.py) to recheck the path scheme.\n\n=== STEP 1: PARSE THE\
  \ STRING-ENCODED GRAPH FIELDS (use ast.literal_eval; they are Python reprs) ===\nFor each row (example values shown for\
  \ the verified row id f4161421...): \n  story = \"[Dorothy]'s brother [Michael] and her went to get ice cream. [Michael]\
  \ is the proud father of the lovely [Donald]\"\n  query = ast.literal_eval(\"('Donald', 'Dorothy')\")            # (name_s,\
  \ name_t): query asks 'what is name_t to name_s'\n  target = 0 ; target_text = 'aunt'\n  f_comb = 'father-sister'      \
  \                               # hyphen-joined relation chain; hop_count = f_comb.count('-')+1 = len(edge_types)\n  story_edges\
  \ = ast.literal_eval(\"[(0, 1), (1, 2)]\")           # list of (src_id, tgt_id) graph edges, in proof order\n  edge_types\
  \  = ast.literal_eval(\"['father', 'sister']\")       # gendered surface relation per story_edge, aligned by index\n  query_edge\
  \  = ast.literal_eval(\"(0, 2)\")                     # (src_id, tgt_id) of the held-out query\n  genders     = dict(p.split(':')\
  \ for p in \"Donald:male,Michael:male,Dorothy:female\".split(','))\n  proof_state = ast.literal_eval(\"[{('Donald','aunt','Dorothy'):\
  \ [('Donald','father','Michael'),('Michael','sister','Dorothy')]}]\")\nproof_state is a list of dicts {goal_triple: [sub_triples...]}\
  \ from backward chaining; a triple (h, r, t) reads 't is h's r' (h's r is t). The LEAF atomic triples equal the story edges;\
  \ for multi-hop chains proof_state has several dicts (recursive decomposition) — collect ALL triples, the leaves are those\
  \ whose relation is in edge_types.\n\n=== STEP 2: RECONSTRUCT node_id -> entity name (deterministic, with verification +\
  \ fallback) ===\nPRIMARY: the proof leaf triples are emitted in the SAME ORDER as story_edges/edge_types, so zip them: for\
  \ k,((s_id,t_id),(h,r,t)) in enumerate(zip(story_edges, leaf_triples)): node2name[s_id]=h; node2name[t_id]=t; assert r==edge_types[k].\
  \ Then node2name[query_edge[0]]=query[0]; node2name[query_edge[1]]=query[1]. VERIFY: every story_edge relation matches edge_types,\
  \ and query maps consistently. FALLBACK (if the zip assertion ever fails): treat it as a tiny labeling CSP — fix the two\
  \ query anchors, then for each story_edge (s_id,t_id,rel) find the unique proof triple (h,rel,t) consistent with already-assigned\
  \ ids and propagate; graphs are <=~12 nodes so this is trivial. NOISE ENTITIES: in the disc config the story mentions extra\
  \ [Name] entities that may NOT appear in story_edges; after the above, scan the story for all bracketed names via regex\
  \ \\[([^\\]]+)\\] and assign any UNSEEN name a fresh sequential entity_id (>= max existing id+1). genders covers all named\
  \ entities; cross-check every bracketed name appears in genders.\n\n=== STEP 3: BUILD input TEXT + MENTION SPANS (brackets\
  \ removed, offsets recorded) ===\nProduce input_text by removing the literal '[' and ']' characters from story, while recording,\
  \ for each bracketed mention, the [start,end) char span of the NAME within input_text. Robust method: walk story char-by-char\
  \ building input_text; when a '[name]' marker is consumed, record (entity_name, start_in_input, end_in_input). Accumulate\
  \ spans per entity: mention_spans[name] = [[s0,e0],[s1,e1],...]. (input_text is natural prose, e.g. \"Dorothy's brother\
  \ Michael and her went to get ice cream. Michael is the proud father of the lovely Donald\".) Use the de-bracketed `story`\
  \ (the actually-presented narrative incl. any noise) as input; keep the de-bracketed `clean_story` in metadata. Verify each\
  \ recorded span substring == the entity name.\n\n=== STEP 4: ASSEMBLE THE PER-STORY gold_graph (output = json.dumps(gold_graph))\
  \ ===\ngold_graph = {\n  'doc_id': row.id, 'corpus': corpus_name ('clutrr_gen' | 'clutrr_disc'),\n  'nodes': [ {'entity_id':\
  \ nid, 'surface': name, 'gender': genders[name], 'mention_spans': mention_spans.get(name, [])} for nid,name in sorted(node2name)\
  \ ],\n  'edges': [ {'source': s_id, 'target': t_id, 'kinship_relation': edge_types[k], 'relation_type': abstract_type_of(edge_types[k],\
  \ gender_of_target), 'is_query': False, 'hop_count': 1} for k,(s_id,t_id) in enumerate(story_edges) ],\n  'query_edge':\
  \ {'source': query_edge[0], 'target': query_edge[1], 'kinship_relation': target_text, 'target_int': int(target), 'is_query':\
  \ True, 'hop_count': hop_count},\n  'absent_relation_pairs': [ {'source': a, 'target': b, 'gold': 'no-relation'} ...]  \
  \ # from STEP 5\n}\nALSO append the query_edge object into 'edges' (with is_query=True) so the graph is self-contained,\
  \ OR keep it only under query_edge — pick one and document it; recommended: keep edges = atomic story edges only, and the\
  \ held-out query under query_edge (cleaner for iter-3). relation_type lookup uses the gendered-surface->(type,gender) reverse\
  \ map from the composition table (STEP 6); store relation_type for each edge so the closure engine can compose over abstract\
  \ types and re-genderize.\n\n=== STEP 5: ABSENT-RELATION PAIRS (pure connectivity; NO composition) ===\nBuild an UNDIRECTED\
  \ networkx graph over ALL entity_ids using story_edges (atomic facts) as edges; add every story-mentioned entity as a node\
  \ (so isolated noise entities are singleton components). Compute connected_components. The query pair lies in the 'main'\
  \ component. ABSENT pairs = entity pairs (a,b) in DIFFERENT components (=> provably no kinship path => honest gold 'no-relation').\
  \ Emit them, prioritising pairs that include a main-component entity, capped (e.g. <=20 per story) to bound size; record\
  \ absent_pair_count. For the CLEAN gen config most stories are a single connected chain => absent_relation_pairs = [] (expected\
  \ — note this; the hallucination demo draws absent pairs from clutrr_disc). CAVEAT to record per row: CLUTRR noise edges\
  \ may be incompletely captured in story_edges (cf. facebookresearch/clutrr issue #20); since we only label STRUCTURALLY\
  \ disconnected pairs as absent (never a same-component pair), this is conservative and sound — set a flag absent_pairs_source='structural_components'.\
  \ Do NOT attempt to label same-component non-stated pairs (that needs composition = forbidden here / iter-3's job).\n\n\
  === STEP 6: CANONICAL KINSHIP COMPOSITION TABLE (top-level metadata, emitted ONCE) ===\nRead the AUTHORITATIVE definitions\
  \ verbatim from facebookresearch/clutrr (raw): https://raw.githubusercontent.com/facebookresearch/clutrr/main/clutrr/store/rules_store.yaml\
  \ and .../clutrr/store/relations_store.yaml (parse with pyyaml). Emit under metadata.composition_table: (a) relation_types\
  \ = the abstract family types with inverse/symmetry flags {child<->inv-child, grand<->inv-grand, un<->inv-un, in-law<->inv-in-law;\
  \ symmetric: sibling, SO}; (b) surface_forms = (type,gender)->word AND reverse word->(type,gender), VERIFIED seed from relations_store.yaml:\
  \ child={male:son,female:daughter}, inv-child={male:father,female:mother}, SO={male:husband,female:wife}, sibling={male:brother,female:sister},\
  \ grand={male:grandson,female:granddaughter}, inv-grand={male:grandfather,female:grandmother}, in-law={male:son-in-law,female:daughter-in-law},\
  \ inv-in-law={male:father-in-law,female:mother-in-law}, sibling-in-law={male:brother-in-law,female:sister-in-law}, un={male:nephew,female:niece},\
  \ inv-un={male:uncle,female:aunt}, no-relation={male:no-relation,female:no-relation}; (c) composition_rules = dict-of-dicts\
  \ rules[t1][t2]=t3 with semantics 'A t1 B and B t2 C => A t3 C; the surface form of t3 uses the gender of C' (VERIFIED on\
  \ the real row: father=inv-child, sister=sibling, rules[inv-child][sibling]=inv-un, inv-un+female=aunt = target_text). VERIFIED\
  \ seed (CROSS-CHECK against the yaml, which is authoritative — add any entries the yaml has that this seed misses, and DROP\
  \ the commented-out 'problematic' entries such as grand+inv-child): child:{child:grand, SO:in-law, sibling:child, inv-un:sibling,\
  \ inv-grand:inv-child}; inv-child:{child:sibling, inv-child:inv-grand, sibling:inv-un}; SO:{inv-child:inv-in-law, grand:grand,\
  \ child:child}; sibling:{sibling:sibling, inv-grand:inv-grand, child:un, inv-child:inv-child}; grand:{sibling:grand}. (d)\
  \ label_map = int<->text for 0..20, DERIVED empirically from the data's (target,target_text) pairs and cross-checked against\
  \ the canonical order [0 aunt,1 son-in-law,2 grandfather,3 brother,4 sister,5 father,6 mother,7 grandmother,8 uncle,9 daughter-in-law,10\
  \ grandson,11 granddaughter,12 father-in-law,13 mother-in-law,14 nephew,15 son,16 daughter,17 niece,18 husband,19 wife,20\
  \ sister-in-law]. (e) note = 'Finite composition table over kinship relation TYPES (CLUTRR rules_store.yaml). NOT a full\
  \ relation algebra: no general intersection/converse closure beyond these rules; some compositions yield no-relation; ambiguous\
  \ compositions (e.g. grand o inv-child) are intentionally excluded. Use to temper the generality claim.' ALSO emit a DERIVED\
  \ gendered surface-level composition table (compose two surface relations by mapping to types, applying rules, re-genderizing\
  \ with the end entity's gender) as a convenience, clearly marked derived.\n\n=== STEP 7: PER-ROW metadata FIELDS (flat,\
  \ metadata_ prefixed, matching the iter-1 row shape) ===\nmetadata_fold (train/dev/test; map CLUTRR split: train->train,\
  \ validation->dev, test->test), metadata_corpus, metadata_hop_count (int 2..10), metadata_noise_type (parse task_name 'task_<n1>.<n2>':\
  \ n1 1=none,2=irrelevant,3=supporting,4=disconnected; n2=chain length — cross-check n2==hop_count), metadata_task_name (raw),\
  \ metadata_f_comb, metadata_query {source_name, target_name, relation: target_text, target_int}, metadata_atomic_facts (list\
  \ of {source_id, target_id, source_name, target_name, kinship_relation, relation_type}), metadata_gold_proof (the parsed\
  \ ordered atomic-triple chain = trace-graph gold), metadata_genders (name->gender map), metadata_num_entities, metadata_num_atomic_edges,\
  \ metadata_num_components, metadata_absent_pair_count, metadata_story_char_len. (input/output are the STRING fields per\
  \ the schema gotcha below; everything structured goes under metadata_ or inside the json.dumps'd output.)\n\n=== STEP 8:\
  \ OUTPUT STRUCTURE, SCHEMA VALIDATION, VARIANTS, SIZE ===\nEmit data_out.json shaped like the iter-1 datasets: top-level\
  \ {'metadata': {...}, 'datasets': [{'dataset':'clutrr_gen','examples':[rows...]}, {'dataset':'clutrr_disc','examples':[rows...]}]}.\
  \ SCHEMA GOTCHA (confirmed from prior AII dataset builds + the sibling temporal/synthetic artifacts): the validator requires\
  \ input and output to be STRINGS — set input=input_text (str) and output=json.dumps(gold_graph); keep all structured per-row\
  \ data under metadata_ keys (scalars/short lists) or inside output. Use the aii-json skill to fetch the canonical exp_sel_data_out\
  \ schema, validate every row, and generate full/mini/preview variants (mini ~ a few hundred rows balanced across hop-counts\
  \ and both corpora; preview ~ 10-20 rows incl. >=1 multi-hop and >=1 with absent pairs). Run the aii-file-size-limit check\
  \ at the end and split full_data_out into parts if any file exceeds the limit (mirror the iter-1 dataset_2 layout: full_data_out/full_data_out_1.json\
  \ etc.). Total well under 300MB.\n\n=== STEP 9: DESCRIPTIVE COUNTS (ALLOWED) vs DERIVED STATS (FORBIDDEN HERE) ===\nReport,\
  \ per corpus and overall, DESCRIPTIVE counts ONLY into metadata + a results/dataset_metadata.json card: #stories, #entities,\
  \ #atomic edges, hop-count distribution, target_text (relation-label) distribution, noise-type distribution, connected-component-count\
  \ distribution, #stories with >=1 absent pair + total absent pairs, story char-length distribution (confirm multi-hop stories\
  \ approach the umbrella's ~3000-char target), and the fold counts. These are pure tallies / networkx graph descriptors.\
  \ FORBIDDEN (these are iter-3's experiment, not the dataset): running the composition table / path-consistency closure;\
  \ computing all-pair relations or labeling same-component pairs; computing atomic-extraction P/R, multi-hop accuracy, singleton-resolution,\
  \ N*, or any hallucination-rate number; calling any LLM. The boundary: dataset = gold graphs + labels + folds + structural\
  \ descriptors + the static composition table; experiment = anything requiring composition, deduction, an LLM read, or held-out-edge\
  \ resolution.\n\n=== STEP 10: REPRODUCIBILITY + DATA CARD ===\nWrite data.py (single entry point: download CSVs -> parse\
  \ -> reconstruct graphs -> emit data_out.json + variants) and a pinned pyproject.toml (python 3.12; pandas, networkx, pyyaml,\
  \ requests, and optionally datasets==2.21.0 + huggingface_hub only for FALLBACK A). Make it deterministic (sort rows by\
  \ id; fixed caps; no randomness, or seed any sampling). Cite in the data card: CLUTRR (Sinha, Sodhani, Dong, Pineau, Hamilton,\
  \ EMNLP 2019, arXiv:1908.06177), the HF CLUTRR/v1 mirror, the kliang5/CLUTRR_huggingface_dataset CSV source, and facebookresearch/clutrr\
  \ (rules_store.yaml / relations_store.yaml). Note license (CLUTRR is released under Facebook's CC-BY-NC / research license\
  \ — record exact terms from the repo LICENSE).\n\n=== FAILURE / FALLBACK HANDLING ===\n(1) raw.githubusercontent 404/rate-limit\
  \ -> re-fetch v1.py for the current path; use datasets+trust_remote_code (Fallback A) or git-clone the kliang5 repo (Fallback\
  \ B). (2) ast.literal_eval fails on a malformed cell -> log the row id, attempt a tolerant parse, else drop the row and\
  \ report the count (never silently). (3) node2name zip-assertion fails -> use the labeling-CSP fallback (STEP 2). (4) a\
  \ bracketed name missing from genders, or a span substring mismatch -> log + flag the row, keep it but mark mention_spans\
  \ incomplete. (5) hop_count from f_comb disagrees with len(edge_types) or task_name n2 -> trust len(edge_types) (the actual\
  \ edge list), record all three, flag the discrepancy. (6) if rob_train_disc yields very few/no multi-component stories (unexpected)\
  \ -> additionally mine absent pairs from rob_train_irr (irrelevant-fact noise) the same way, and report. (7) if total size\
  \ unexpectedly large -> it won't be (<60MB), but still run the size check and split.\n\nOPTIONAL 3rd slice (only if time\
  \ permits, low cost ~18MB): rob_train_sup_23_test_all_23 (supporting-fact distractors) standardized identically, to give\
  \ iter-3 a distractor-robustness arm for the atomic-extraction P/R claim. Not required."
target_num_datasets: 2
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
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 16 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 8 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 4 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-17 15:37:59 UTC

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

### [3] SKILL-INPUT — aii-json · 2026-06-17 15:38:13 UTC

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

### [4] SKILL-INPUT — aii-file-size-limit · 2026-06-17 15:38:13 UTC

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

### [5] SKILL-INPUT — aii-python · 2026-06-17 15:38:13 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [6] SKILL-INPUT — aii-web-tools · 2026-06-17 15:48:29 UTC

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

### [7] SYSTEM-USER prompt · 2026-06-17 16:01:03 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
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
  CLUTRR kinship gold graphs as the clean end-to-end venue (frozen, schema-validated, hop-stratified, with absent-relation
  pairs)
summary: >-
  Acquire the CLUTRR (Sinha et al. 2019) systematic-generalization and disconnected-noise splits and standardize them to the
  exp_sel_data_out JSON schema, ONE row per story. Each row carries input=the de-bracketed narrative and output=json.dumps(gold_graph)
  where the gold graph = entity nodes (with surface name, gender, mention char-spans) + atomic kinship edges (story_edges
  x edge_types, each a 1-hop directly-stated fact) + the held-out QUERY edge (is_query=true, hop_count=chain length, gold
  relation) + a set of structurally ABSENT-relation entity pairs (different connected components => no kinship path) for the
  hallucination demo. Per-row metadata carries hop-count, the constituent atomic facts (for atomic-extraction P/R), the gold
  backward-chaining proof chain (the human-auditable trace-graph gold), noise type, genders, graph descriptors, and a train/dev/test
  fold. Top-level metadata carries the finite kinship COMPOSITION TABLE (abstract relation types + gendered surface map +
  composition rules read verbatim from facebookresearch/clutrr's rules_store.yaml / relations_store.yaml), explicitly noting
  it is a composition table, NOT a full relation algebra. Acquisition is bulletproof: download the CSVs directly from the
  GitHub raw mirror that HF's own loader points at; no datasets-script trust_remote_code needed. Report DESCRIPTIVE counts
  only (stories, entities, edges, hop-count and relation-label distributions, component counts, absent-pair counts, story
  char-lengths). Do NOT run any composition/closure or compute derived statistics. Reproduce via data.py + pinned pyproject.toml.
  Tiny (<60MB total), trivially under 300MB. Sits beside the iter-1 temporal (NarrativeTime/TDDMan/MATRES) and synthetic-QCN
  corpora as the third corpus family.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  An ideal delivered CLUTRR corpus is a per-story gold KINSHIP relation graph over short, professionally-readable family narratives,
  standardized so iter-3 can deliver — in ONE setting — all four numbers the umbrella paper names: (i) atomic-extraction precision/recall,
  (ii) multi-hop deduction accuracy vs chain length, (iii) a human-auditable trace-graph, and (iv) a quantified hallucination-rate
  reduction on absent-relation queries. Concretely each delivered example must have: (1) input = the natural-language story
  (entity-bracket markers REMOVED, natural prose), ~tens-to-~3000 chars (longer chains approach the umbrella's ~3000-char
  target); (2) recoverable ENTITY NODES, each carrying a stable integer entity_id (the CLUTRR graph node index), surface name,
  gender (male/female), and the list of mention character-spans into the input text; (3) ATOMIC EDGES = the directly-stated
  kinship facts (one per story_edges entry), each {source_id, target_id, kinship_relation (gendered surface form, e.g. 'father','sister'),
  relation_type (abstract type, e.g. inv-child, sibling), is_query=false, hop_count=1}; (4) exactly ONE held-out QUERY edge
  {source_id, target_id, kinship_relation=target_text, target_int, is_query=true, hop_count=chain length} whose relation is
  NOT stated in the story and must be deduced by composing >=2 atomic edges; (5) a set of ABSENT-RELATION query pairs = entity
  pairs lying in DIFFERENT connected components of the story graph (no kinship path => honest gold label 'no-relation'), present
  in disconnected-noise stories, for the hallucination demo; (6) the gold backward-chaining PROOF chain (ordered atomic triples
  that compose to the query) as trace-graph gold; (7) per-example metadata: hop_count, noise_type {none,irrelevant,supporting,disconnected},
  task_name, f_comb (relation chain), genders map, graph descriptors (n_entities, n_edges, n_components), absent_pair_count;
  (8) a documented train/dev/test fold (each story is an independent document, so the native CLUTRR split is already document-disjoint).
  Top-level (shared, emitted ONCE): the finite kinship composition table = the 10-11 abstract relation TYPES (child, inv-child,
  SO, sibling, grand, inv-grand, un, inv-un, in-law, inv-in-law, sibling-in-law) with inverse/symmetry flags; the (type x
  gender)->surface-word map; the composition rules rules[t1][t2]=t3 (A t1 B, B t2 C => A t3 C; surface of t3 uses gender of
  C); and the int<->text label map (0..20). The data must span hop-counts 2..10 (for the multi-hop-vs-length curve) and include
  a disconnected-noise slice (for genuine within-document absent pairs). All CLUTRR splits are tiny (a few thousand rows,
  ~15-30MB each), trivially under 300MB. Prefer the canonical kliang5/CLUTRR_huggingface_dataset CSV mirror (the exact source
  HF's CLUTRR/v1 loader downloads) so the gold graph fields (story_edges, edge_types, query_edge, genders, proof_state) come
  pre-parsed rather than re-derived.
dataset_search_plan: "Deliver EXACTLY 2 CLUTRR slices as separate dataset entries (one optional 3rd noted at the end). Both\
  \ come from the SAME source and share schema/composition-table; they differ only in role. CORE = gen_train234_test2to10\
  \ (clean, hop-counts 2-10 in test; hosts atomic-extraction P/R + multi-hop-accuracy-vs-length + trace-graph). ABSENT = rob_train_disc_23_test_all_23\
  \ (disconnected-noise; supplies genuine within-document absent-relation pairs for the hallucination demo). The hard part\
  \ is NOT downloading (CSV is trivial) — it is faithfully reconstructing the per-story gold graph (node_id->name mapping,\
  \ mention spans, atomic facts, proof chain, absent pairs) and emitting the canonical composition table.\n\n=== STEP 0: ACQUISITION\
  \ (bulletproof; no datasets-library script loading) ===\nHF dataset CLUTRR/v1 ships ONLY a loader script v1.py and NO data\
  \ files; v1.py downloads CSVs from the raw GitHub mirror: _URL='https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/'\
  \ and for each config fetches {config}/train.csv, {config}/validation.csv, {config}/test.csv. PRIMARY PATH (use this): download\
  \ those CSVs DIRECTLY with requests + pandas.read_csv — NO datasets library, NO trust_remote_code. URLs:\n  base = 'https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/'\n\
  \  for config in ['gen_train234_test2to10','rob_train_disc_23_test_all_23']:\n    for split in ['train','validation','test']:\
  \ df = pd.read_csv(base + config + '/' + split + '.csv')\nColumns (CONFIRMED, all strings except target=int32): id, story,\
  \ query, target, target_text, clean_story, proof_state, f_comb, task_name, story_edges, edge_types, query_edge, genders,\
  \ task_split. Sizes (CONFIRMED): gen_train234_test2to10 = train 12064 / val 3019 / test 1048 (~30MB); rob_train_disc_23_test_all_23\
  \ = train 8080 / val 2020 / test 445 (~17MB). FALLBACK A: load_dataset('CLUTRR/v1', config, trust_remote_code=True) with\
  \ datasets pinned <3.0 (e.g. datasets==2.21.0) — works but heavier. FALLBACK B: clone the kliang5 repo via git or huggingface_hub\
  \ if raw.githubusercontent rate-limits. FALLBACK C: the original facebookresearch/clutrr generator + its pre-generated Google-Drive\
  \ zip (fragile in headless; last resort). Verify row counts against the CONFIRMED sizes above; if a config 404s, re-fetch\
  \ v1.py (https://huggingface.co/datasets/CLUTRR/v1/raw/main/v1.py) to recheck the path scheme.\n\n=== STEP 1: PARSE THE\
  \ STRING-ENCODED GRAPH FIELDS (use ast.literal_eval; they are Python reprs) ===\nFor each row (example values shown for\
  \ the verified row id f4161421...): \n  story = \"[Dorothy]'s brother [Michael] and her went to get ice cream. [Michael]\
  \ is the proud father of the lovely [Donald]\"\n  query = ast.literal_eval(\"('Donald', 'Dorothy')\")            # (name_s,\
  \ name_t): query asks 'what is name_t to name_s'\n  target = 0 ; target_text = 'aunt'\n  f_comb = 'father-sister'      \
  \                               # hyphen-joined relation chain; hop_count = f_comb.count('-')+1 = len(edge_types)\n  story_edges\
  \ = ast.literal_eval(\"[(0, 1), (1, 2)]\")           # list of (src_id, tgt_id) graph edges, in proof order\n  edge_types\
  \  = ast.literal_eval(\"['father', 'sister']\")       # gendered surface relation per story_edge, aligned by index\n  query_edge\
  \  = ast.literal_eval(\"(0, 2)\")                     # (src_id, tgt_id) of the held-out query\n  genders     = dict(p.split(':')\
  \ for p in \"Donald:male,Michael:male,Dorothy:female\".split(','))\n  proof_state = ast.literal_eval(\"[{('Donald','aunt','Dorothy'):\
  \ [('Donald','father','Michael'),('Michael','sister','Dorothy')]}]\")\nproof_state is a list of dicts {goal_triple: [sub_triples...]}\
  \ from backward chaining; a triple (h, r, t) reads 't is h's r' (h's r is t). The LEAF atomic triples equal the story edges;\
  \ for multi-hop chains proof_state has several dicts (recursive decomposition) — collect ALL triples, the leaves are those\
  \ whose relation is in edge_types.\n\n=== STEP 2: RECONSTRUCT node_id -> entity name (deterministic, with verification +\
  \ fallback) ===\nPRIMARY: the proof leaf triples are emitted in the SAME ORDER as story_edges/edge_types, so zip them: for\
  \ k,((s_id,t_id),(h,r,t)) in enumerate(zip(story_edges, leaf_triples)): node2name[s_id]=h; node2name[t_id]=t; assert r==edge_types[k].\
  \ Then node2name[query_edge[0]]=query[0]; node2name[query_edge[1]]=query[1]. VERIFY: every story_edge relation matches edge_types,\
  \ and query maps consistently. FALLBACK (if the zip assertion ever fails): treat it as a tiny labeling CSP — fix the two\
  \ query anchors, then for each story_edge (s_id,t_id,rel) find the unique proof triple (h,rel,t) consistent with already-assigned\
  \ ids and propagate; graphs are <=~12 nodes so this is trivial. NOISE ENTITIES: in the disc config the story mentions extra\
  \ [Name] entities that may NOT appear in story_edges; after the above, scan the story for all bracketed names via regex\
  \ \\[([^\\]]+)\\] and assign any UNSEEN name a fresh sequential entity_id (>= max existing id+1). genders covers all named\
  \ entities; cross-check every bracketed name appears in genders.\n\n=== STEP 3: BUILD input TEXT + MENTION SPANS (brackets\
  \ removed, offsets recorded) ===\nProduce input_text by removing the literal '[' and ']' characters from story, while recording,\
  \ for each bracketed mention, the [start,end) char span of the NAME within input_text. Robust method: walk story char-by-char\
  \ building input_text; when a '[name]' marker is consumed, record (entity_name, start_in_input, end_in_input). Accumulate\
  \ spans per entity: mention_spans[name] = [[s0,e0],[s1,e1],...]. (input_text is natural prose, e.g. \"Dorothy's brother\
  \ Michael and her went to get ice cream. Michael is the proud father of the lovely Donald\".) Use the de-bracketed `story`\
  \ (the actually-presented narrative incl. any noise) as input; keep the de-bracketed `clean_story` in metadata. Verify each\
  \ recorded span substring == the entity name.\n\n=== STEP 4: ASSEMBLE THE PER-STORY gold_graph (output = json.dumps(gold_graph))\
  \ ===\ngold_graph = {\n  'doc_id': row.id, 'corpus': corpus_name ('clutrr_gen' | 'clutrr_disc'),\n  'nodes': [ {'entity_id':\
  \ nid, 'surface': name, 'gender': genders[name], 'mention_spans': mention_spans.get(name, [])} for nid,name in sorted(node2name)\
  \ ],\n  'edges': [ {'source': s_id, 'target': t_id, 'kinship_relation': edge_types[k], 'relation_type': abstract_type_of(edge_types[k],\
  \ gender_of_target), 'is_query': False, 'hop_count': 1} for k,(s_id,t_id) in enumerate(story_edges) ],\n  'query_edge':\
  \ {'source': query_edge[0], 'target': query_edge[1], 'kinship_relation': target_text, 'target_int': int(target), 'is_query':\
  \ True, 'hop_count': hop_count},\n  'absent_relation_pairs': [ {'source': a, 'target': b, 'gold': 'no-relation'} ...]  \
  \ # from STEP 5\n}\nALSO append the query_edge object into 'edges' (with is_query=True) so the graph is self-contained,\
  \ OR keep it only under query_edge — pick one and document it; recommended: keep edges = atomic story edges only, and the\
  \ held-out query under query_edge (cleaner for iter-3). relation_type lookup uses the gendered-surface->(type,gender) reverse\
  \ map from the composition table (STEP 6); store relation_type for each edge so the closure engine can compose over abstract\
  \ types and re-genderize.\n\n=== STEP 5: ABSENT-RELATION PAIRS (pure connectivity; NO composition) ===\nBuild an UNDIRECTED\
  \ networkx graph over ALL entity_ids using story_edges (atomic facts) as edges; add every story-mentioned entity as a node\
  \ (so isolated noise entities are singleton components). Compute connected_components. The query pair lies in the 'main'\
  \ component. ABSENT pairs = entity pairs (a,b) in DIFFERENT components (=> provably no kinship path => honest gold 'no-relation').\
  \ Emit them, prioritising pairs that include a main-component entity, capped (e.g. <=20 per story) to bound size; record\
  \ absent_pair_count. For the CLEAN gen config most stories are a single connected chain => absent_relation_pairs = [] (expected\
  \ — note this; the hallucination demo draws absent pairs from clutrr_disc). CAVEAT to record per row: CLUTRR noise edges\
  \ may be incompletely captured in story_edges (cf. facebookresearch/clutrr issue #20); since we only label STRUCTURALLY\
  \ disconnected pairs as absent (never a same-component pair), this is conservative and sound — set a flag absent_pairs_source='structural_components'.\
  \ Do NOT attempt to label same-component non-stated pairs (that needs composition = forbidden here / iter-3's job).\n\n\
  === STEP 6: CANONICAL KINSHIP COMPOSITION TABLE (top-level metadata, emitted ONCE) ===\nRead the AUTHORITATIVE definitions\
  \ verbatim from facebookresearch/clutrr (raw): https://raw.githubusercontent.com/facebookresearch/clutrr/main/clutrr/store/rules_store.yaml\
  \ and .../clutrr/store/relations_store.yaml (parse with pyyaml). Emit under metadata.composition_table: (a) relation_types\
  \ = the abstract family types with inverse/symmetry flags {child<->inv-child, grand<->inv-grand, un<->inv-un, in-law<->inv-in-law;\
  \ symmetric: sibling, SO}; (b) surface_forms = (type,gender)->word AND reverse word->(type,gender), VERIFIED seed from relations_store.yaml:\
  \ child={male:son,female:daughter}, inv-child={male:father,female:mother}, SO={male:husband,female:wife}, sibling={male:brother,female:sister},\
  \ grand={male:grandson,female:granddaughter}, inv-grand={male:grandfather,female:grandmother}, in-law={male:son-in-law,female:daughter-in-law},\
  \ inv-in-law={male:father-in-law,female:mother-in-law}, sibling-in-law={male:brother-in-law,female:sister-in-law}, un={male:nephew,female:niece},\
  \ inv-un={male:uncle,female:aunt}, no-relation={male:no-relation,female:no-relation}; (c) composition_rules = dict-of-dicts\
  \ rules[t1][t2]=t3 with semantics 'A t1 B and B t2 C => A t3 C; the surface form of t3 uses the gender of C' (VERIFIED on\
  \ the real row: father=inv-child, sister=sibling, rules[inv-child][sibling]=inv-un, inv-un+female=aunt = target_text). VERIFIED\
  \ seed (CROSS-CHECK against the yaml, which is authoritative — add any entries the yaml has that this seed misses, and DROP\
  \ the commented-out 'problematic' entries such as grand+inv-child): child:{child:grand, SO:in-law, sibling:child, inv-un:sibling,\
  \ inv-grand:inv-child}; inv-child:{child:sibling, inv-child:inv-grand, sibling:inv-un}; SO:{inv-child:inv-in-law, grand:grand,\
  \ child:child}; sibling:{sibling:sibling, inv-grand:inv-grand, child:un, inv-child:inv-child}; grand:{sibling:grand}. (d)\
  \ label_map = int<->text for 0..20, DERIVED empirically from the data's (target,target_text) pairs and cross-checked against\
  \ the canonical order [0 aunt,1 son-in-law,2 grandfather,3 brother,4 sister,5 father,6 mother,7 grandmother,8 uncle,9 daughter-in-law,10\
  \ grandson,11 granddaughter,12 father-in-law,13 mother-in-law,14 nephew,15 son,16 daughter,17 niece,18 husband,19 wife,20\
  \ sister-in-law]. (e) note = 'Finite composition table over kinship relation TYPES (CLUTRR rules_store.yaml). NOT a full\
  \ relation algebra: no general intersection/converse closure beyond these rules; some compositions yield no-relation; ambiguous\
  \ compositions (e.g. grand o inv-child) are intentionally excluded. Use to temper the generality claim.' ALSO emit a DERIVED\
  \ gendered surface-level composition table (compose two surface relations by mapping to types, applying rules, re-genderizing\
  \ with the end entity's gender) as a convenience, clearly marked derived.\n\n=== STEP 7: PER-ROW metadata FIELDS (flat,\
  \ metadata_ prefixed, matching the iter-1 row shape) ===\nmetadata_fold (train/dev/test; map CLUTRR split: train->train,\
  \ validation->dev, test->test), metadata_corpus, metadata_hop_count (int 2..10), metadata_noise_type (parse task_name 'task_<n1>.<n2>':\
  \ n1 1=none,2=irrelevant,3=supporting,4=disconnected; n2=chain length — cross-check n2==hop_count), metadata_task_name (raw),\
  \ metadata_f_comb, metadata_query {source_name, target_name, relation: target_text, target_int}, metadata_atomic_facts (list\
  \ of {source_id, target_id, source_name, target_name, kinship_relation, relation_type}), metadata_gold_proof (the parsed\
  \ ordered atomic-triple chain = trace-graph gold), metadata_genders (name->gender map), metadata_num_entities, metadata_num_atomic_edges,\
  \ metadata_num_components, metadata_absent_pair_count, metadata_story_char_len. (input/output are the STRING fields per\
  \ the schema gotcha below; everything structured goes under metadata_ or inside the json.dumps'd output.)\n\n=== STEP 8:\
  \ OUTPUT STRUCTURE, SCHEMA VALIDATION, VARIANTS, SIZE ===\nEmit data_out.json shaped like the iter-1 datasets: top-level\
  \ {'metadata': {...}, 'datasets': [{'dataset':'clutrr_gen','examples':[rows...]}, {'dataset':'clutrr_disc','examples':[rows...]}]}.\
  \ SCHEMA GOTCHA (confirmed from prior AII dataset builds + the sibling temporal/synthetic artifacts): the validator requires\
  \ input and output to be STRINGS — set input=input_text (str) and output=json.dumps(gold_graph); keep all structured per-row\
  \ data under metadata_ keys (scalars/short lists) or inside output. Use the aii-json skill to fetch the canonical exp_sel_data_out\
  \ schema, validate every row, and generate full/mini/preview variants (mini ~ a few hundred rows balanced across hop-counts\
  \ and both corpora; preview ~ 10-20 rows incl. >=1 multi-hop and >=1 with absent pairs). Run the aii-file-size-limit check\
  \ at the end and split full_data_out into parts if any file exceeds the limit (mirror the iter-1 dataset_2 layout: full_data_out/full_data_out_1.json\
  \ etc.). Total well under 300MB.\n\n=== STEP 9: DESCRIPTIVE COUNTS (ALLOWED) vs DERIVED STATS (FORBIDDEN HERE) ===\nReport,\
  \ per corpus and overall, DESCRIPTIVE counts ONLY into metadata + a results/dataset_metadata.json card: #stories, #entities,\
  \ #atomic edges, hop-count distribution, target_text (relation-label) distribution, noise-type distribution, connected-component-count\
  \ distribution, #stories with >=1 absent pair + total absent pairs, story char-length distribution (confirm multi-hop stories\
  \ approach the umbrella's ~3000-char target), and the fold counts. These are pure tallies / networkx graph descriptors.\
  \ FORBIDDEN (these are iter-3's experiment, not the dataset): running the composition table / path-consistency closure;\
  \ computing all-pair relations or labeling same-component pairs; computing atomic-extraction P/R, multi-hop accuracy, singleton-resolution,\
  \ N*, or any hallucination-rate number; calling any LLM. The boundary: dataset = gold graphs + labels + folds + structural\
  \ descriptors + the static composition table; experiment = anything requiring composition, deduction, an LLM read, or held-out-edge\
  \ resolution.\n\n=== STEP 10: REPRODUCIBILITY + DATA CARD ===\nWrite data.py (single entry point: download CSVs -> parse\
  \ -> reconstruct graphs -> emit data_out.json + variants) and a pinned pyproject.toml (python 3.12; pandas, networkx, pyyaml,\
  \ requests, and optionally datasets==2.21.0 + huggingface_hub only for FALLBACK A). Make it deterministic (sort rows by\
  \ id; fixed caps; no randomness, or seed any sampling). Cite in the data card: CLUTRR (Sinha, Sodhani, Dong, Pineau, Hamilton,\
  \ EMNLP 2019, arXiv:1908.06177), the HF CLUTRR/v1 mirror, the kliang5/CLUTRR_huggingface_dataset CSV source, and facebookresearch/clutrr\
  \ (rules_store.yaml / relations_store.yaml). Note license (CLUTRR is released under Facebook's CC-BY-NC / research license\
  \ — record exact terms from the repo LICENSE).\n\n=== FAILURE / FALLBACK HANDLING ===\n(1) raw.githubusercontent 404/rate-limit\
  \ -> re-fetch v1.py for the current path; use datasets+trust_remote_code (Fallback A) or git-clone the kliang5 repo (Fallback\
  \ B). (2) ast.literal_eval fails on a malformed cell -> log the row id, attempt a tolerant parse, else drop the row and\
  \ report the count (never silently). (3) node2name zip-assertion fails -> use the labeling-CSP fallback (STEP 2). (4) a\
  \ bracketed name missing from genders, or a span substring mismatch -> log + flag the row, keep it but mark mention_spans\
  \ incomplete. (5) hop_count from f_comb disagrees with len(edge_types) or task_name n2 -> trust len(edge_types) (the actual\
  \ edge list), record all three, flag the discrepancy. (6) if rob_train_disc yields very few/no multi-component stories (unexpected)\
  \ -> additionally mine absent pairs from rob_train_irr (irrelevant-fact noise) the same way, and report. (7) if total size\
  \ unexpectedly large -> it won't be (<60MB), but still run the size check and split.\n\nOPTIONAL 3rd slice (only if time\
  \ permits, low cost ~18MB): rob_train_sup_23_test_all_23 (supporting-fact distractors) standardized identically, to give\
  \ iter-3 a distractor-robustness arm for the atomic-extraction P/R claim. Not required."
target_num_datasets: 2
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
TODO 1. For the top 4 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

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
TODO 3. Read preview to inspect examples. Choose THE BEST 2 DATASETS based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [8] SYSTEM-USER prompt · 2026-06-17 16:07:53 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
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
  CLUTRR kinship gold graphs as the clean end-to-end venue (frozen, schema-validated, hop-stratified, with absent-relation
  pairs)
summary: >-
  Acquire the CLUTRR (Sinha et al. 2019) systematic-generalization and disconnected-noise splits and standardize them to the
  exp_sel_data_out JSON schema, ONE row per story. Each row carries input=the de-bracketed narrative and output=json.dumps(gold_graph)
  where the gold graph = entity nodes (with surface name, gender, mention char-spans) + atomic kinship edges (story_edges
  x edge_types, each a 1-hop directly-stated fact) + the held-out QUERY edge (is_query=true, hop_count=chain length, gold
  relation) + a set of structurally ABSENT-relation entity pairs (different connected components => no kinship path) for the
  hallucination demo. Per-row metadata carries hop-count, the constituent atomic facts (for atomic-extraction P/R), the gold
  backward-chaining proof chain (the human-auditable trace-graph gold), noise type, genders, graph descriptors, and a train/dev/test
  fold. Top-level metadata carries the finite kinship COMPOSITION TABLE (abstract relation types + gendered surface map +
  composition rules read verbatim from facebookresearch/clutrr's rules_store.yaml / relations_store.yaml), explicitly noting
  it is a composition table, NOT a full relation algebra. Acquisition is bulletproof: download the CSVs directly from the
  GitHub raw mirror that HF's own loader points at; no datasets-script trust_remote_code needed. Report DESCRIPTIVE counts
  only (stories, entities, edges, hop-count and relation-label distributions, component counts, absent-pair counts, story
  char-lengths). Do NOT run any composition/closure or compute derived statistics. Reproduce via data.py + pinned pyproject.toml.
  Tiny (<60MB total), trivially under 300MB. Sits beside the iter-1 temporal (NarrativeTime/TDDMan/MATRES) and synthetic-QCN
  corpora as the third corpus family.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  An ideal delivered CLUTRR corpus is a per-story gold KINSHIP relation graph over short, professionally-readable family narratives,
  standardized so iter-3 can deliver — in ONE setting — all four numbers the umbrella paper names: (i) atomic-extraction precision/recall,
  (ii) multi-hop deduction accuracy vs chain length, (iii) a human-auditable trace-graph, and (iv) a quantified hallucination-rate
  reduction on absent-relation queries. Concretely each delivered example must have: (1) input = the natural-language story
  (entity-bracket markers REMOVED, natural prose), ~tens-to-~3000 chars (longer chains approach the umbrella's ~3000-char
  target); (2) recoverable ENTITY NODES, each carrying a stable integer entity_id (the CLUTRR graph node index), surface name,
  gender (male/female), and the list of mention character-spans into the input text; (3) ATOMIC EDGES = the directly-stated
  kinship facts (one per story_edges entry), each {source_id, target_id, kinship_relation (gendered surface form, e.g. 'father','sister'),
  relation_type (abstract type, e.g. inv-child, sibling), is_query=false, hop_count=1}; (4) exactly ONE held-out QUERY edge
  {source_id, target_id, kinship_relation=target_text, target_int, is_query=true, hop_count=chain length} whose relation is
  NOT stated in the story and must be deduced by composing >=2 atomic edges; (5) a set of ABSENT-RELATION query pairs = entity
  pairs lying in DIFFERENT connected components of the story graph (no kinship path => honest gold label 'no-relation'), present
  in disconnected-noise stories, for the hallucination demo; (6) the gold backward-chaining PROOF chain (ordered atomic triples
  that compose to the query) as trace-graph gold; (7) per-example metadata: hop_count, noise_type {none,irrelevant,supporting,disconnected},
  task_name, f_comb (relation chain), genders map, graph descriptors (n_entities, n_edges, n_components), absent_pair_count;
  (8) a documented train/dev/test fold (each story is an independent document, so the native CLUTRR split is already document-disjoint).
  Top-level (shared, emitted ONCE): the finite kinship composition table = the 10-11 abstract relation TYPES (child, inv-child,
  SO, sibling, grand, inv-grand, un, inv-un, in-law, inv-in-law, sibling-in-law) with inverse/symmetry flags; the (type x
  gender)->surface-word map; the composition rules rules[t1][t2]=t3 (A t1 B, B t2 C => A t3 C; surface of t3 uses gender of
  C); and the int<->text label map (0..20). The data must span hop-counts 2..10 (for the multi-hop-vs-length curve) and include
  a disconnected-noise slice (for genuine within-document absent pairs). All CLUTRR splits are tiny (a few thousand rows,
  ~15-30MB each), trivially under 300MB. Prefer the canonical kliang5/CLUTRR_huggingface_dataset CSV mirror (the exact source
  HF's CLUTRR/v1 loader downloads) so the gold graph fields (story_edges, edge_types, query_edge, genders, proof_state) come
  pre-parsed rather than re-derived.
dataset_search_plan: "Deliver EXACTLY 2 CLUTRR slices as separate dataset entries (one optional 3rd noted at the end). Both\
  \ come from the SAME source and share schema/composition-table; they differ only in role. CORE = gen_train234_test2to10\
  \ (clean, hop-counts 2-10 in test; hosts atomic-extraction P/R + multi-hop-accuracy-vs-length + trace-graph). ABSENT = rob_train_disc_23_test_all_23\
  \ (disconnected-noise; supplies genuine within-document absent-relation pairs for the hallucination demo). The hard part\
  \ is NOT downloading (CSV is trivial) — it is faithfully reconstructing the per-story gold graph (node_id->name mapping,\
  \ mention spans, atomic facts, proof chain, absent pairs) and emitting the canonical composition table.\n\n=== STEP 0: ACQUISITION\
  \ (bulletproof; no datasets-library script loading) ===\nHF dataset CLUTRR/v1 ships ONLY a loader script v1.py and NO data\
  \ files; v1.py downloads CSVs from the raw GitHub mirror: _URL='https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/'\
  \ and for each config fetches {config}/train.csv, {config}/validation.csv, {config}/test.csv. PRIMARY PATH (use this): download\
  \ those CSVs DIRECTLY with requests + pandas.read_csv — NO datasets library, NO trust_remote_code. URLs:\n  base = 'https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main/'\n\
  \  for config in ['gen_train234_test2to10','rob_train_disc_23_test_all_23']:\n    for split in ['train','validation','test']:\
  \ df = pd.read_csv(base + config + '/' + split + '.csv')\nColumns (CONFIRMED, all strings except target=int32): id, story,\
  \ query, target, target_text, clean_story, proof_state, f_comb, task_name, story_edges, edge_types, query_edge, genders,\
  \ task_split. Sizes (CONFIRMED): gen_train234_test2to10 = train 12064 / val 3019 / test 1048 (~30MB); rob_train_disc_23_test_all_23\
  \ = train 8080 / val 2020 / test 445 (~17MB). FALLBACK A: load_dataset('CLUTRR/v1', config, trust_remote_code=True) with\
  \ datasets pinned <3.0 (e.g. datasets==2.21.0) — works but heavier. FALLBACK B: clone the kliang5 repo via git or huggingface_hub\
  \ if raw.githubusercontent rate-limits. FALLBACK C: the original facebookresearch/clutrr generator + its pre-generated Google-Drive\
  \ zip (fragile in headless; last resort). Verify row counts against the CONFIRMED sizes above; if a config 404s, re-fetch\
  \ v1.py (https://huggingface.co/datasets/CLUTRR/v1/raw/main/v1.py) to recheck the path scheme.\n\n=== STEP 1: PARSE THE\
  \ STRING-ENCODED GRAPH FIELDS (use ast.literal_eval; they are Python reprs) ===\nFor each row (example values shown for\
  \ the verified row id f4161421...): \n  story = \"[Dorothy]'s brother [Michael] and her went to get ice cream. [Michael]\
  \ is the proud father of the lovely [Donald]\"\n  query = ast.literal_eval(\"('Donald', 'Dorothy')\")            # (name_s,\
  \ name_t): query asks 'what is name_t to name_s'\n  target = 0 ; target_text = 'aunt'\n  f_comb = 'father-sister'      \
  \                               # hyphen-joined relation chain; hop_count = f_comb.count('-')+1 = len(edge_types)\n  story_edges\
  \ = ast.literal_eval(\"[(0, 1), (1, 2)]\")           # list of (src_id, tgt_id) graph edges, in proof order\n  edge_types\
  \  = ast.literal_eval(\"['father', 'sister']\")       # gendered surface relation per story_edge, aligned by index\n  query_edge\
  \  = ast.literal_eval(\"(0, 2)\")                     # (src_id, tgt_id) of the held-out query\n  genders     = dict(p.split(':')\
  \ for p in \"Donald:male,Michael:male,Dorothy:female\".split(','))\n  proof_state = ast.literal_eval(\"[{('Donald','aunt','Dorothy'):\
  \ [('Donald','father','Michael'),('Michael','sister','Dorothy')]}]\")\nproof_state is a list of dicts {goal_triple: [sub_triples...]}\
  \ from backward chaining; a triple (h, r, t) reads 't is h's r' (h's r is t). The LEAF atomic triples equal the story edges;\
  \ for multi-hop chains proof_state has several dicts (recursive decomposition) — collect ALL triples, the leaves are those\
  \ whose relation is in edge_types.\n\n=== STEP 2: RECONSTRUCT node_id -> entity name (deterministic, with verification +\
  \ fallback) ===\nPRIMARY: the proof leaf triples are emitted in the SAME ORDER as story_edges/edge_types, so zip them: for\
  \ k,((s_id,t_id),(h,r,t)) in enumerate(zip(story_edges, leaf_triples)): node2name[s_id]=h; node2name[t_id]=t; assert r==edge_types[k].\
  \ Then node2name[query_edge[0]]=query[0]; node2name[query_edge[1]]=query[1]. VERIFY: every story_edge relation matches edge_types,\
  \ and query maps consistently. FALLBACK (if the zip assertion ever fails): treat it as a tiny labeling CSP — fix the two\
  \ query anchors, then for each story_edge (s_id,t_id,rel) find the unique proof triple (h,rel,t) consistent with already-assigned\
  \ ids and propagate; graphs are <=~12 nodes so this is trivial. NOISE ENTITIES: in the disc config the story mentions extra\
  \ [Name] entities that may NOT appear in story_edges; after the above, scan the story for all bracketed names via regex\
  \ \\[([^\\]]+)\\] and assign any UNSEEN name a fresh sequential entity_id (>= max existing id+1). genders covers all named\
  \ entities; cross-check every bracketed name appears in genders.\n\n=== STEP 3: BUILD input TEXT + MENTION SPANS (brackets\
  \ removed, offsets recorded) ===\nProduce input_text by removing the literal '[' and ']' characters from story, while recording,\
  \ for each bracketed mention, the [start,end) char span of the NAME within input_text. Robust method: walk story char-by-char\
  \ building input_text; when a '[name]' marker is consumed, record (entity_name, start_in_input, end_in_input). Accumulate\
  \ spans per entity: mention_spans[name] = [[s0,e0],[s1,e1],...]. (input_text is natural prose, e.g. \"Dorothy's brother\
  \ Michael and her went to get ice cream. Michael is the proud father of the lovely Donald\".) Use the de-bracketed `story`\
  \ (the actually-presented narrative incl. any noise) as input; keep the de-bracketed `clean_story` in metadata. Verify each\
  \ recorded span substring == the entity name.\n\n=== STEP 4: ASSEMBLE THE PER-STORY gold_graph (output = json.dumps(gold_graph))\
  \ ===\ngold_graph = {\n  'doc_id': row.id, 'corpus': corpus_name ('clutrr_gen' | 'clutrr_disc'),\n  'nodes': [ {'entity_id':\
  \ nid, 'surface': name, 'gender': genders[name], 'mention_spans': mention_spans.get(name, [])} for nid,name in sorted(node2name)\
  \ ],\n  'edges': [ {'source': s_id, 'target': t_id, 'kinship_relation': edge_types[k], 'relation_type': abstract_type_of(edge_types[k],\
  \ gender_of_target), 'is_query': False, 'hop_count': 1} for k,(s_id,t_id) in enumerate(story_edges) ],\n  'query_edge':\
  \ {'source': query_edge[0], 'target': query_edge[1], 'kinship_relation': target_text, 'target_int': int(target), 'is_query':\
  \ True, 'hop_count': hop_count},\n  'absent_relation_pairs': [ {'source': a, 'target': b, 'gold': 'no-relation'} ...]  \
  \ # from STEP 5\n}\nALSO append the query_edge object into 'edges' (with is_query=True) so the graph is self-contained,\
  \ OR keep it only under query_edge — pick one and document it; recommended: keep edges = atomic story edges only, and the\
  \ held-out query under query_edge (cleaner for iter-3). relation_type lookup uses the gendered-surface->(type,gender) reverse\
  \ map from the composition table (STEP 6); store relation_type for each edge so the closure engine can compose over abstract\
  \ types and re-genderize.\n\n=== STEP 5: ABSENT-RELATION PAIRS (pure connectivity; NO composition) ===\nBuild an UNDIRECTED\
  \ networkx graph over ALL entity_ids using story_edges (atomic facts) as edges; add every story-mentioned entity as a node\
  \ (so isolated noise entities are singleton components). Compute connected_components. The query pair lies in the 'main'\
  \ component. ABSENT pairs = entity pairs (a,b) in DIFFERENT components (=> provably no kinship path => honest gold 'no-relation').\
  \ Emit them, prioritising pairs that include a main-component entity, capped (e.g. <=20 per story) to bound size; record\
  \ absent_pair_count. For the CLEAN gen config most stories are a single connected chain => absent_relation_pairs = [] (expected\
  \ — note this; the hallucination demo draws absent pairs from clutrr_disc). CAVEAT to record per row: CLUTRR noise edges\
  \ may be incompletely captured in story_edges (cf. facebookresearch/clutrr issue #20); since we only label STRUCTURALLY\
  \ disconnected pairs as absent (never a same-component pair), this is conservative and sound — set a flag absent_pairs_source='structural_components'.\
  \ Do NOT attempt to label same-component non-stated pairs (that needs composition = forbidden here / iter-3's job).\n\n\
  === STEP 6: CANONICAL KINSHIP COMPOSITION TABLE (top-level metadata, emitted ONCE) ===\nRead the AUTHORITATIVE definitions\
  \ verbatim from facebookresearch/clutrr (raw): https://raw.githubusercontent.com/facebookresearch/clutrr/main/clutrr/store/rules_store.yaml\
  \ and .../clutrr/store/relations_store.yaml (parse with pyyaml). Emit under metadata.composition_table: (a) relation_types\
  \ = the abstract family types with inverse/symmetry flags {child<->inv-child, grand<->inv-grand, un<->inv-un, in-law<->inv-in-law;\
  \ symmetric: sibling, SO}; (b) surface_forms = (type,gender)->word AND reverse word->(type,gender), VERIFIED seed from relations_store.yaml:\
  \ child={male:son,female:daughter}, inv-child={male:father,female:mother}, SO={male:husband,female:wife}, sibling={male:brother,female:sister},\
  \ grand={male:grandson,female:granddaughter}, inv-grand={male:grandfather,female:grandmother}, in-law={male:son-in-law,female:daughter-in-law},\
  \ inv-in-law={male:father-in-law,female:mother-in-law}, sibling-in-law={male:brother-in-law,female:sister-in-law}, un={male:nephew,female:niece},\
  \ inv-un={male:uncle,female:aunt}, no-relation={male:no-relation,female:no-relation}; (c) composition_rules = dict-of-dicts\
  \ rules[t1][t2]=t3 with semantics 'A t1 B and B t2 C => A t3 C; the surface form of t3 uses the gender of C' (VERIFIED on\
  \ the real row: father=inv-child, sister=sibling, rules[inv-child][sibling]=inv-un, inv-un+female=aunt = target_text). VERIFIED\
  \ seed (CROSS-CHECK against the yaml, which is authoritative — add any entries the yaml has that this seed misses, and DROP\
  \ the commented-out 'problematic' entries such as grand+inv-child): child:{child:grand, SO:in-law, sibling:child, inv-un:sibling,\
  \ inv-grand:inv-child}; inv-child:{child:sibling, inv-child:inv-grand, sibling:inv-un}; SO:{inv-child:inv-in-law, grand:grand,\
  \ child:child}; sibling:{sibling:sibling, inv-grand:inv-grand, child:un, inv-child:inv-child}; grand:{sibling:grand}. (d)\
  \ label_map = int<->text for 0..20, DERIVED empirically from the data's (target,target_text) pairs and cross-checked against\
  \ the canonical order [0 aunt,1 son-in-law,2 grandfather,3 brother,4 sister,5 father,6 mother,7 grandmother,8 uncle,9 daughter-in-law,10\
  \ grandson,11 granddaughter,12 father-in-law,13 mother-in-law,14 nephew,15 son,16 daughter,17 niece,18 husband,19 wife,20\
  \ sister-in-law]. (e) note = 'Finite composition table over kinship relation TYPES (CLUTRR rules_store.yaml). NOT a full\
  \ relation algebra: no general intersection/converse closure beyond these rules; some compositions yield no-relation; ambiguous\
  \ compositions (e.g. grand o inv-child) are intentionally excluded. Use to temper the generality claim.' ALSO emit a DERIVED\
  \ gendered surface-level composition table (compose two surface relations by mapping to types, applying rules, re-genderizing\
  \ with the end entity's gender) as a convenience, clearly marked derived.\n\n=== STEP 7: PER-ROW metadata FIELDS (flat,\
  \ metadata_ prefixed, matching the iter-1 row shape) ===\nmetadata_fold (train/dev/test; map CLUTRR split: train->train,\
  \ validation->dev, test->test), metadata_corpus, metadata_hop_count (int 2..10), metadata_noise_type (parse task_name 'task_<n1>.<n2>':\
  \ n1 1=none,2=irrelevant,3=supporting,4=disconnected; n2=chain length — cross-check n2==hop_count), metadata_task_name (raw),\
  \ metadata_f_comb, metadata_query {source_name, target_name, relation: target_text, target_int}, metadata_atomic_facts (list\
  \ of {source_id, target_id, source_name, target_name, kinship_relation, relation_type}), metadata_gold_proof (the parsed\
  \ ordered atomic-triple chain = trace-graph gold), metadata_genders (name->gender map), metadata_num_entities, metadata_num_atomic_edges,\
  \ metadata_num_components, metadata_absent_pair_count, metadata_story_char_len. (input/output are the STRING fields per\
  \ the schema gotcha below; everything structured goes under metadata_ or inside the json.dumps'd output.)\n\n=== STEP 8:\
  \ OUTPUT STRUCTURE, SCHEMA VALIDATION, VARIANTS, SIZE ===\nEmit data_out.json shaped like the iter-1 datasets: top-level\
  \ {'metadata': {...}, 'datasets': [{'dataset':'clutrr_gen','examples':[rows...]}, {'dataset':'clutrr_disc','examples':[rows...]}]}.\
  \ SCHEMA GOTCHA (confirmed from prior AII dataset builds + the sibling temporal/synthetic artifacts): the validator requires\
  \ input and output to be STRINGS — set input=input_text (str) and output=json.dumps(gold_graph); keep all structured per-row\
  \ data under metadata_ keys (scalars/short lists) or inside output. Use the aii-json skill to fetch the canonical exp_sel_data_out\
  \ schema, validate every row, and generate full/mini/preview variants (mini ~ a few hundred rows balanced across hop-counts\
  \ and both corpora; preview ~ 10-20 rows incl. >=1 multi-hop and >=1 with absent pairs). Run the aii-file-size-limit check\
  \ at the end and split full_data_out into parts if any file exceeds the limit (mirror the iter-1 dataset_2 layout: full_data_out/full_data_out_1.json\
  \ etc.). Total well under 300MB.\n\n=== STEP 9: DESCRIPTIVE COUNTS (ALLOWED) vs DERIVED STATS (FORBIDDEN HERE) ===\nReport,\
  \ per corpus and overall, DESCRIPTIVE counts ONLY into metadata + a results/dataset_metadata.json card: #stories, #entities,\
  \ #atomic edges, hop-count distribution, target_text (relation-label) distribution, noise-type distribution, connected-component-count\
  \ distribution, #stories with >=1 absent pair + total absent pairs, story char-length distribution (confirm multi-hop stories\
  \ approach the umbrella's ~3000-char target), and the fold counts. These are pure tallies / networkx graph descriptors.\
  \ FORBIDDEN (these are iter-3's experiment, not the dataset): running the composition table / path-consistency closure;\
  \ computing all-pair relations or labeling same-component pairs; computing atomic-extraction P/R, multi-hop accuracy, singleton-resolution,\
  \ N*, or any hallucination-rate number; calling any LLM. The boundary: dataset = gold graphs + labels + folds + structural\
  \ descriptors + the static composition table; experiment = anything requiring composition, deduction, an LLM read, or held-out-edge\
  \ resolution.\n\n=== STEP 10: REPRODUCIBILITY + DATA CARD ===\nWrite data.py (single entry point: download CSVs -> parse\
  \ -> reconstruct graphs -> emit data_out.json + variants) and a pinned pyproject.toml (python 3.12; pandas, networkx, pyyaml,\
  \ requests, and optionally datasets==2.21.0 + huggingface_hub only for FALLBACK A). Make it deterministic (sort rows by\
  \ id; fixed caps; no randomness, or seed any sampling). Cite in the data card: CLUTRR (Sinha, Sodhani, Dong, Pineau, Hamilton,\
  \ EMNLP 2019, arXiv:1908.06177), the HF CLUTRR/v1 mirror, the kliang5/CLUTRR_huggingface_dataset CSV source, and facebookresearch/clutrr\
  \ (rules_store.yaml / relations_store.yaml). Note license (CLUTRR is released under Facebook's CC-BY-NC / research license\
  \ — record exact terms from the repo LICENSE).\n\n=== FAILURE / FALLBACK HANDLING ===\n(1) raw.githubusercontent 404/rate-limit\
  \ -> re-fetch v1.py for the current path; use datasets+trust_remote_code (Fallback A) or git-clone the kliang5 repo (Fallback\
  \ B). (2) ast.literal_eval fails on a malformed cell -> log the row id, attempt a tolerant parse, else drop the row and\
  \ report the count (never silently). (3) node2name zip-assertion fails -> use the labeling-CSP fallback (STEP 2). (4) a\
  \ bracketed name missing from genders, or a span substring mismatch -> log + flag the row, keep it but mark mention_spans\
  \ incomplete. (5) hop_count from f_comb disagrees with len(edge_types) or task_name n2 -> trust len(edge_types) (the actual\
  \ edge list), record all three, flag the discrepancy. (6) if rob_train_disc yields very few/no multi-component stories (unexpected)\
  \ -> additionally mine absent pairs from rob_train_irr (irrelevant-fact noise) the same way, and report. (7) if total size\
  \ unexpectedly large -> it won't be (<60MB), but still run the size check and split.\n\nOPTIONAL 3rd slice (only if time\
  \ permits, low cost ~18MB): rob_train_sup_23_test_all_23 (supporting-fact distractors) standardized identically, to give\
  \ iter-3 a distractor-robustness arm for the atomic-extraction P/R claim. Not required."
target_num_datasets: 2
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
TODO 1. Update data.py to only include the chosen 2 datasets and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
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
