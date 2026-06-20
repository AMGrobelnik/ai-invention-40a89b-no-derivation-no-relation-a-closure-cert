# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 6 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 00:39:04 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx1
type: dataset
title: >-
  Natural-Text Absent-Relation Kinship Corpus from Re-DocRED (STEP-B host for the certificate-vs-confidence-thresholded-abstainer
  experiment)
summary: >-
  Build ONE genuinely-natural (no templating, no concatenation) document-level kinship corpus from Re-DocRED (completeness-corrected
  DocRED Wikipedia prose), standardized to the exp_sel_data_out schema, one row per document, drop-in compatible with the
  CLUTRR kinship dataset so iter-7 reuses the forward-union least-fixpoint closure engine verbatim. Each document yields:
  (a) atomic span-local kinship edges (readable), (b) deduction-required multi-hop PRESENT query edges (gold = CLUTRR-table
  composition, non-circular because composed relations like grandfather/uncle are absent from DocRED's inventory), and (c)
  genuine within-document ABSENT (no-derivation) entity pairs from disconnected kinship components. Completeness-correction
  is the load-bearing reason for the source: it makes 'absent = truly no relation' defensible where vanilla DocRED's false
  negatives would corrupt absent gold. Honestly report char-length distribution (most docs are ~1200 chars; flag/prefer the
  [2000,4000] subset rather than forcing it).
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  GOAL: a corpus of genuinely-natural professional documents (Wikipedia introductory prose) carrying document-level KINSHIP relations, with three populated query strata for iter-7's certificate experiment: derivable multi-hop PRESENT pairs, genuine ABSENT (no-derivation) pairs, and atomic readable edges, plus a hand-supplied kinship composition table.

  WHAT MAKES IT IDEAL:
  1. NATURAL TEXT, NOT TEMPLATED/CONCATENATED. Real Wikipedia prose (the whole point: replace templated CLUTRR and symbolic-id SpaRP). One document = one contiguous natural article; never concatenate sub-stories.
  2. COMPLETENESS-CORRECTED GOLD so 'absent' is defensible. Re-DocRED (tonytan48/Re-DocRED) is preferred over vanilla DocRED precisely because its re-annotation removes DocRED's false-negative relations; an entity pair labeled 'no family relation' is then trustworthy within the document's closed world. This is THE reason absent-relation gold is credible.
  3. GENUINE ABSENT PAIRS. Within-document entity pairs where BOTH entities participate in >=1 annotated family relation (so both are 'in the kinship context') but lie in DIFFERENT connected components of the document's kinship graph => no direct relation and no derivable kinship path. Conservatively labeled (closed-world within the document; open-world caveat documented in the card).
  4. RECOVERABLE GOLD. Atomic edges = family relations whose two entity mentions co-occur in a local span (same/adjacent sentence) AND whose surface kinship cue ('son','daughter','father','mother','brother','sister','wife','husband','married','grandson',...) is textually present near both mentions, so a span-local reader can plausibly extract them. PRESENT query gold = composition over atomic edges via the hand-supplied CLUTRR finite kinship table (forward-union least fixpoint). Composed relations (grandfather/grandmother/uncle/aunt/nephew/niece/in-laws/cousins) are OUTSIDE DocRED's relation inventory, so multi-hop gold is provably non-circular (never an annotated edge).
  5. HAND-SUPPLIED COMPOSITION TABLE (reused, not invented). The CLUTRR rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender map (documented in dependency art_Dm5vYXmD1R8h), emitted verbatim ONCE in top-level metadata and explicitly labeled NOT a relation algebra (a finite kinship table). This is the SAME table every kinship arm uses, so iter-7's engine runs unchanged.
  6. SCHEMA PARITY. exp_sel_data_out schema, ONE ROW per document, drop-in compatible with the CLUTRR kinship dataset (art_HS7-lxhZnU9m) so iter-7 reuses loaders/closure verbatim.
  7. CHAR-LENGTH HONESTY. Report per-document char length; PREFER/flag documents in [2000,4000] chars to supply genuinely-natural ~3000-char professional documents (addresses the scope MINOR with NON-constructed text). DocRED docs average ~196.7 words (~1200 chars), so do NOT hard-filter to >=3000 (that would gut the corpus) -- keep all docs with usable kinship structure, flag the long subset, and report the fraction reaching the target.
  8. COMMODITY-SCALE. The whole corpus (4,053 docs, small graphs) is < 50MB raw; well under the 300MB cap; full/mini/preview variants.
  9. $0 LLM (pure data construction). An OPTIONAL small-LLM judge to confirm atomic kinship cues are textually present is capped well under $2 with a SHA-256 prompt cache.

  SCALE TARGETS (report actuals; do not pad): aim across the whole corpus for >=150 derivable PRESENT multi-hop query edges and >=300 ABSENT pairs spread over as many documents as yield them; if PRESENT queries are scarce (family relations are sparse in DocRED), the corpus still primarily serves the ABSENT-relation experiment (the load-bearing one for iter-7) -- report counts honestly and let iter-7's fork decide scope.
dataset_search_plan: |-
  Compute profile: cpu_heavy (pure CPU JSON/graph processing on ~4k small docs; no GPU; the only non-GPU dataset profile offered). Read dependency art_Dm5vYXmD1R8h/research_out.json FIRST (it pins the CLUTRR kinship table = rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender map, and the absent-relation construction recipe). If the sibling CLUTRR kinship dataset art_HS7-lxhZnU9m is present in this run's workspace, READ its data.py/schema for exact field parity; otherwise use the self-contained schema spec in STEP 6 below.

  === STEP 0: SOURCE SELECTION (prefer ready-made natural; default Re-DocRED) ===
  0a. FIRST search HuggingFace (aii-hf-datasets skill) and the web for any ready-made GENUINELY-NATURAL genealogy/kinship/family-relation corpus with (i) natural prose, (ii) gold kinship relations, (iii) genuine absent pairs, (iv) recoverable multi-hop structure. Concrete candidates to inspect and either adopt-if-cleaner or reject-with-reason: 'VLyb/Kinship' (LIKELY an image kinship-verification set, e.g. Families-In-the-Wild -- reject if not TEXT), the 'Sefika/relation-extraction-datasets' collection, and any 'family/genealogy QA' text corpus. Reject templated (CLUTRR-like) or symbolic-id (SpaRP-like) sources -- the whole point is natural text. Most likely none beats Re-DocRED; document the rejection reasons in the card.
  0b. PRIMARY SOURCE = Re-DocRED (HuggingFace 'tonytan48/Re-DocRED'; the completeness-corrected re-annotation of DocRED, Tan et al. 2022, arXiv:2205.12696). Splits: train 3,053 / dev 500 / test 500 = 4,053 docs. Download via aii-hf-datasets / huggingface_hub snapshot_download (json files under ./data: train_revised.json, dev_revised.json, test_revised.json or similar -- inspect the repo tree for exact filenames). FALLBACK if Re-DocRED is unavailable or malformed: vanilla DocRED (thunlp/docred: train_annotated.json, dev.json, test.json) -- but then DOWNGRADE absent-pair confidence in the card (DocRED false negatives corrupt absent gold) and prefer using DocRED only to enlarge the ATOMIC/PRESENT strata, not the ABSENT stratum.
  0c. SECONDARY (target_num_datasets=2): to maximize yield and corroborate, ALSO process the union of Re-DocRED + any vanilla-DocRED docs NOT in Re-DocRED, OR a ready-made natural genealogy corpus if STEP 0a found one. Emit the secondary as a clearly-labeled slice (metadata source field) so iter-7 can include/exclude it. Both share the identical schema.
  0d. Get rel_info.json from the DocRED/Re-DocRED repo to confirm the P-code->name mapping. CONFIRMED family Wikidata properties present in DocRED's 96-relation inventory: P22 (father), P25 (mother), P26 (spouse), P40 (child), P3373 (sibling), P1038 (relative). Use exactly these.

  === STEP 1: PARSE + DETOKENIZE (record char offsets) ===
  DocRED/Re-DocRED ships TOKENIZED 'sents' (list of sentences, each a list of word tokens), NOT raw text. Detokenize to natural prose: join tokens with single spaces and join sentences with a single space, OR use a light detokenizer (e.g. fix spacing before punctuation). CRITICAL: while detokenizing, RECORD per-(sent_id,token_index) character offsets in the reconstructed document so every entity mention's char span can be computed (mirror the char-offset marking in iter-5's data_adapter.py mark_local/local_span). 'input' = this detokenized document text. Compute char_len on it. Note in the card that text is detokenized Wikipedia prose (still natural content, reconstructed from tokens).

  === STEP 2: BUILD THE PER-DOCUMENT KINSHIP GRAPH ===
  For each document: entities = vertexSet (each entity = list of mention dicts {name, sent_id, pos:[tok_start,tok_end], type}); keep PER entities for kinship. Family edges = labels with r in {P22,P25,P26,P40,P3373,P1038}. Direction convention (FIX ONCE, document it): adopt edge(source S, target T, relation) meaning 'T is S's <relation>'. Wikidata semantics for a triple {h, t, r}: P22 father => t is h's father; P25 mother => t is h's mother; P40 child => t is h's child; P26 spouse => symmetric; P3373 sibling => symmetric; P1038 relative => generic, symmetric. Map each to the CLUTRR primitive + gender (from the dependency's relations_store map): father=(inv-child,m), mother=(inv-child,f), child=(child, gender-unknown unless surface cue son/daughter), spouse=(SO, gender unknown unless husband/wife cue), sibling=(sibling, gender unknown unless brother/sister cue). Seed the converse edge from the table (father<->child, mother<->child, etc.), never from an LLM. SPECIAL HANDLING of P1038 'relative': it is too vague to give a precise composable primitive => DO NOT add it as an atomic composable edge, but DO use it to mark the two entities as RELATED so they are EXCLUDED from the absent set. Derive per-entity GENDER from any kinship role/cue that fixes it (object of P22=male, P25=female; surface tokens 'son/brother/husband'=male, 'daughter/sister/wife'=female); leave undetermined otherwise and emit the gender-neutral primitive for composed gold when the final target's gender is unknown.

  === STEP 3: ATOMIC (readable) EDGES -- is_query:false, hop_count:1 ===
  An annotated family edge becomes an ATOMIC edge iff BOTH conditions hold: (i) LOCALITY -- the two entities have mentions co-occurring within a local span (same sentence, or adjacent sentences; also accept the relation's 'evidence' sentence_ids as the supporting span); (ii) SURFACE CUE -- a kinship keyword ('father','mother','son','daughter','brother','sister','wife','husband','married','spouse','grandson','granddaughter',...) appears in that span near both mentions. Record per atomic edge: source, target, kinship_relation (surface, e.g. 'father'), primitive (e.g. 'inv-child'), target_gender, support_span (char span of the evidence sentence(s)), surface_cue (the matched token), evidence_sent_ids. These are the edges a span-local reader is expected to extract; they seed the closure.

  === STEP 4: PRESENT (deduction-required) QUERY EDGES -- is_query:true, hop_count>=2 ===
  Over the atomic-edge graph (undirected for pathfinding, directed for composition), find entity pairs (A,Z) with NO direct annotated family edge AND NO co-occurring local span, but a derivable kinship path of length >=2 whose CLUTRR-table composition yields a DEFINED relation. gold = the composed surface relation (gendered via Z's gender, else neutral primitive); record hop_count (path length), derivation_path (list of intermediate entity_ids), primitive, relation_type. Prefer shortest path; if multiple paths give the SAME composition keep it, if they conflict (should not happen for consistent kinship) drop the pair and log it. NON-CIRCULARITY (state in card): composed relations (grandparent/uncle/aunt/nephew/niece/cousin/in-laws) are NOT in DocRED's relation set, so this gold is never an annotated edge -- it is recoverable ONLY by composition, exactly the held-out multi-hop regime mirroring CLUTRR on natural text. Record hop histogram.

  === STEP 5: ABSENT / NO-DERIVATION QUERY EDGES -- is_absent:true ===
  Within each document, take entity pairs (A,B) where BOTH A and B participate in >=1 annotated family relation (both in the kinship context) AND lie in DIFFERENT connected components of the kinship graph (no direct edge, no derivable path). reason='different_component' (or 'no_path'). Restrict to Re-DocRED so 'no relation' is supported by completeness-corrected gold; EXCLUDE any pair linked by P1038 'relative'. Conservative closed-world label; document the open-world caveat. Cap absent pairs per document (e.g. <=30, sampled to balance against present/atomic counts) to avoid one large article dominating. These are the genuine natural no-relation regime the certificate must beat a confidence-thresholded abstainer on.

  === STEP 6: SCHEMA (exp_sel_data_out; ONE ROW per document) ===
  If art_HS7-lxhZnU9m is available, match its fields EXACTLY; otherwise emit: input = detokenized document text; output = json.dumps(gold_graph) where gold_graph = {
    nodes: [{entity_id, surface (canonical/longest mention name), mention_spans:[[char_start,char_end],...], type:'PER', gender?:'m'|'f'|null, wikidata_qid?:null (DocRED vertexSet has no QIDs -- emit null/omit)}],
    atomic_edges: [{source, target, kinship_relation, primitive, relation_type, target_gender, is_query:false, hop_count:1, support_span:[cs,ce], surface_cue, evidence_sent_ids}],
    query_edges: [{source, target, kinship_relation (gold), primitive, relation_type, target:int? (optional CLUTRR-style numeric id), is_query:true, hop_count (>=2), derivation_path:[entity_id,...]}],
    absent_relation_pairs: [{source, target, reason:'different_component'|'no_path', is_absent:true}]
  }.
  FLAT metadata_* columns per row: metadata_fold (deterministic by doc-text SHA hash, e.g. 5 folds), metadata_source ('re-docred'|'docred'|<ready-made>), metadata_split ('train'|'dev'|'test'), metadata_doc_id (title), metadata_n_entities, metadata_n_per_entities, metadata_n_atomic_edges, metadata_n_family_components, metadata_present_query_count, metadata_absent_pair_count, metadata_char_len, metadata_n_tokens, metadata_hop_histogram (json), metadata_n_ge_2500_chars (int/bool), metadata_has_3000_char (bool), metadata_locally_justifiable_frac. Emit ONCE in TOP-LEVEL dataset metadata: the hand-supplied kinship COMPOSITION TABLE verbatim (CLUTRR rules_store primitive compositions + relations_store surface<->primitive<->gender map), explicitly tagged 'finite kinship composition table, NOT a relation algebra'; plus provenance, license, source repo commit SHA, the open-world absent caveat, and the corpus-level char-length distribution summary (min/median/mean/max, fraction >=2000, fraction >=2500, fraction in [2000,4000]).

  === STEP 7: QA / HONESTY ===
  7a. Verify a random sample (>=50) of atomic edges have their surface cue textually present in the support span; report the pass rate. Report the LOCALLY-JUSTIFIABLE (surface cue stated) vs PURELY-KB-IMPLIED fraction of family edges (non-circularity audit analog).
  7b. Report the fraction of documents reaching ~3000 chars and the [2000,4000] count; if it is small (expected, since avg ~1200 chars), state plainly that natural ~3000-char docs are a minority -- do NOT concatenate or pad.
  7c. OPTIONAL small-LLM judge (via OpenRouter only, e.g. a cheap model) to confirm atomic kinship cues are textually present on a subsample; HARD-CAP well under $2 with SHA-256 prompt cache and a cumulative cost guard. Skip if the deterministic cue check suffices.
  7d. Validate every emitted JSON row against the schema (aii-json). Generate full/mini/preview variants (aii-json); confirm <300MB (aii-file-size-limit). Sanity-check that iter-5's/CLUTRR's loader can parse a sample (json.loads(output) yields nodes/atomic_edges/query_edges/absent_relation_pairs).

  === FAILURE SCENARIOS + FALLBACKS ===
  F1 (KINSHIP TOO SPARSE -> few PRESENT multi-hop queries): family relations are sparse in DocRED. MITIGATE by (i) using ALL 4,053 Re-DocRED docs + non-overlapping vanilla-DocRED docs; (ii) accepting hop_count==2 queries (not only longer chains); (iii) if still <~50 present queries, KEEP the corpus -- the ABSENT-relation stratum is the load-bearing one for iter-7's certificate-vs-confidence claim. Report present-query scarcity honestly; iter-7's pre-registered fork already scopes to absent-only if needed.
  F2 (ABSENT PAIRS SCARCE: single-family biographies have one component): many docs have only one kinship component => no different-component pairs. MITIGATE by scanning all docs and keeping those with >=2 family-participating components; report how many docs/pairs qualify. Do NOT manufacture absent pairs by pairing a family entity with a no-family entity (weakens the 'in kinship context' guarantee) unless flagged separately.
  F3 (CHAR LENGTH BELOW TARGET): expected -- flag/report, do not force. The natural-text requirement matters more than the 3000-char target for iter-7's claim.
  F4 (Re-DocRED LOAD ISSUE): fall back to vanilla DocRED (downgrade absent confidence in card) or the kliang5-style direct-file download; never block on load_dataset script breakage -- read the json files directly.
  F5 (GENDER UNDETERMINED for composed gold): emit gender-neutral primitive (e.g. 'grandparent','sibling','parent','child') and flag; iter-7 can score at primitive level. Keep gendered surface only when the target's gender is fixed by a role/cue.
  F6 (DETOKENIZATION MISALIGNS char offsets): verify a sample of mention char spans equal the mention surface (as iter-5 does with offset_ok_frac); if misaligned, fall back to ordered surface search to locate spans, and report offset_ok_frac in metadata.
target_num_datasets: 2
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_Dm5vYXmD1R8h
type: research
title: Iter-2 Local-Reader / Prolog-Discharge / CLUTRR Implementation-Decision Dossier
summary: >-
  Executor-ready, web-verified resolution of the six NEW implementation decisions the iter-2 closure-certified text-to-logic
  experiments need (beyond the iter-1 dossier art_aQ2Rf8rwqteI). (1) LOCAL-READER PROTOCOL: minimal-span unit = the single
  sentence containing each event mention (default; +/-1 sentence as a sensitivity arm), grounded in TimeBank-Dense's own annotation
  window (same-sentence + immediately-following-sentence + DCT; 5 relations BEFORE/AFTER/INCLUDES/IS_INCLUDED/SIMULTANEOUS
  + VAGUE=underdetermined); 'no shared span' = mentions never co-occur within the window => DEDUCTION-REQUIRED, computable
  WITHOUT the LLM (T0-safe); disjunctive Pairwise read prompt adapted from Wei et al. arXiv:2407.19568 (Bulk/Iterative/Event-Ranking/Pairwise)
  + METRE arXiv:2408.07353 multi-label, enumerate base relations + explicit UNIVERSAL option, 'name every relation the text
  does NOT rule out'. (2) DISCHARGE: SWI-Prolog via pyswip v0.3.3 (class-method Prolog.assertz/query, Python>=3.9, needs apt
  swi-prolog>=8.4.2, ctypes shared-lib + SWI_HOME_DIR/LIBSWIPL_PATH) PRIMARY, robust subprocess fallback `swipl -s f.pl -g
  goal -t halt` (exit 0/1/2), clingo 5.8.0 ASP as secondary; QCN encoded as edge(E1,E2,RelSet) + algebra-seeded compose/3,converse/2;
  readback |R|==1 emit / |R|>1 ABSTAIN / |R|==0 unsound-flag; CONFIDENT-WRONG = nonabstained-single-relation-mismatch-rate
  on the deduction-required/absent subset, matched-coverage, paired-bootstrap CI, pre-registered MDE, aligned to Logic-LM/LINC
  executable-rate practice. (3) CLUTRR: HF CLUTRR/v1 (14 configs, target 0-20 mapping, fields incl proof_state/f_comb/story_edges/edge_types)
  BUT datasets>=4.0 dropped scripts => load via huggingface_hub snapshot_download of the per-task CSVs (git-LFS) or pin datasets<4.0
  + trust_remote_code; kinship composition table = rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender
  map (no-relation is a native primitive); absent-relation pairs CONSTRUCTED from rob_train_disc disconnected components /
  cross-family pairs; atomic-gold = story_edges+edge_types. (4) STRONGER READER: weak anchor = iter-1 google/gemini-3.1-flash-lite
  ($0.25/$1.50); recommend deepseek/deepseek-v3.2 ($0.2288/$0.3432, cross-family, CHEAPER, gate test ~$1.3) as budget-optimal
  stronger reader, google/gemini-3-flash-preview ($0.50/$3.00 thinking) as the clear capability-jump option on a stratified
  subsample; total two-reader run < $10 with disk cache + prompt caching + hard cost-guard. (5) SEVEN local-regime baselines
  each re-specified to read ONLY local spans with a matched single-relation abstention signal (raw verbalized-confidence,
  CoT, self-consistency vote-margin, LINC formalization-agreement, PoT path-agreement [confirmed per-path INDEPENDENT, no
  cross-path intersection], ILP-commit Eirew M=5, naive single-pass intersection), all thresholded to the SAME coverage object.
  (6) Four recent temporal/logical-consistency citations pinned (arXiv:2510.15513, 2502.11425, 2412.16100, 2409.14065) + a
  crisp novelty statement (disjunction-preserving abstain-on-collapse OUTPUT CONTRACT + gold-free closure CERTIFICATE + redundancy-as-coding-rate,
  NOT the algebra). Includes a consolidated decision table, exact IDs/URLs, and a 12-item gotchas list.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1
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
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 16 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 8 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 4 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [2] HUMAN-USER prompt · 2026-06-18 00:39:04 UTC

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

### [3] SKILL-INPUT — aii-hf-datasets · 2026-06-18 00:43:44 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-18 00:43:44 UTC

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

### [5] SKILL-INPUT — aii-json · 2026-06-18 00:43:52 UTC

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

### [6] SKILL-INPUT — aii-file-size-limit · 2026-06-18 00:43:52 UTC

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

### [7] SYSTEM-USER prompt · 2026-06-18 01:00:57 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx1
type: dataset
title: >-
  Natural-Text Absent-Relation Kinship Corpus from Re-DocRED (STEP-B host for the certificate-vs-confidence-thresholded-abstainer
  experiment)
summary: >-
  Build ONE genuinely-natural (no templating, no concatenation) document-level kinship corpus from Re-DocRED (completeness-corrected
  DocRED Wikipedia prose), standardized to the exp_sel_data_out schema, one row per document, drop-in compatible with the
  CLUTRR kinship dataset so iter-7 reuses the forward-union least-fixpoint closure engine verbatim. Each document yields:
  (a) atomic span-local kinship edges (readable), (b) deduction-required multi-hop PRESENT query edges (gold = CLUTRR-table
  composition, non-circular because composed relations like grandfather/uncle are absent from DocRED's inventory), and (c)
  genuine within-document ABSENT (no-derivation) entity pairs from disconnected kinship components. Completeness-correction
  is the load-bearing reason for the source: it makes 'absent = truly no relation' defensible where vanilla DocRED's false
  negatives would corrupt absent gold. Honestly report char-length distribution (most docs are ~1200 chars; flag/prefer the
  [2000,4000] subset rather than forcing it).
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  GOAL: a corpus of genuinely-natural professional documents (Wikipedia introductory prose) carrying document-level KINSHIP relations, with three populated query strata for iter-7's certificate experiment: derivable multi-hop PRESENT pairs, genuine ABSENT (no-derivation) pairs, and atomic readable edges, plus a hand-supplied kinship composition table.

  WHAT MAKES IT IDEAL:
  1. NATURAL TEXT, NOT TEMPLATED/CONCATENATED. Real Wikipedia prose (the whole point: replace templated CLUTRR and symbolic-id SpaRP). One document = one contiguous natural article; never concatenate sub-stories.
  2. COMPLETENESS-CORRECTED GOLD so 'absent' is defensible. Re-DocRED (tonytan48/Re-DocRED) is preferred over vanilla DocRED precisely because its re-annotation removes DocRED's false-negative relations; an entity pair labeled 'no family relation' is then trustworthy within the document's closed world. This is THE reason absent-relation gold is credible.
  3. GENUINE ABSENT PAIRS. Within-document entity pairs where BOTH entities participate in >=1 annotated family relation (so both are 'in the kinship context') but lie in DIFFERENT connected components of the document's kinship graph => no direct relation and no derivable kinship path. Conservatively labeled (closed-world within the document; open-world caveat documented in the card).
  4. RECOVERABLE GOLD. Atomic edges = family relations whose two entity mentions co-occur in a local span (same/adjacent sentence) AND whose surface kinship cue ('son','daughter','father','mother','brother','sister','wife','husband','married','grandson',...) is textually present near both mentions, so a span-local reader can plausibly extract them. PRESENT query gold = composition over atomic edges via the hand-supplied CLUTRR finite kinship table (forward-union least fixpoint). Composed relations (grandfather/grandmother/uncle/aunt/nephew/niece/in-laws/cousins) are OUTSIDE DocRED's relation inventory, so multi-hop gold is provably non-circular (never an annotated edge).
  5. HAND-SUPPLIED COMPOSITION TABLE (reused, not invented). The CLUTRR rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender map (documented in dependency art_Dm5vYXmD1R8h), emitted verbatim ONCE in top-level metadata and explicitly labeled NOT a relation algebra (a finite kinship table). This is the SAME table every kinship arm uses, so iter-7's engine runs unchanged.
  6. SCHEMA PARITY. exp_sel_data_out schema, ONE ROW per document, drop-in compatible with the CLUTRR kinship dataset (art_HS7-lxhZnU9m) so iter-7 reuses loaders/closure verbatim.
  7. CHAR-LENGTH HONESTY. Report per-document char length; PREFER/flag documents in [2000,4000] chars to supply genuinely-natural ~3000-char professional documents (addresses the scope MINOR with NON-constructed text). DocRED docs average ~196.7 words (~1200 chars), so do NOT hard-filter to >=3000 (that would gut the corpus) -- keep all docs with usable kinship structure, flag the long subset, and report the fraction reaching the target.
  8. COMMODITY-SCALE. The whole corpus (4,053 docs, small graphs) is < 50MB raw; well under the 300MB cap; full/mini/preview variants.
  9. $0 LLM (pure data construction). An OPTIONAL small-LLM judge to confirm atomic kinship cues are textually present is capped well under $2 with a SHA-256 prompt cache.

  SCALE TARGETS (report actuals; do not pad): aim across the whole corpus for >=150 derivable PRESENT multi-hop query edges and >=300 ABSENT pairs spread over as many documents as yield them; if PRESENT queries are scarce (family relations are sparse in DocRED), the corpus still primarily serves the ABSENT-relation experiment (the load-bearing one for iter-7) -- report counts honestly and let iter-7's fork decide scope.
dataset_search_plan: |-
  Compute profile: cpu_heavy (pure CPU JSON/graph processing on ~4k small docs; no GPU; the only non-GPU dataset profile offered). Read dependency art_Dm5vYXmD1R8h/research_out.json FIRST (it pins the CLUTRR kinship table = rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender map, and the absent-relation construction recipe). If the sibling CLUTRR kinship dataset art_HS7-lxhZnU9m is present in this run's workspace, READ its data.py/schema for exact field parity; otherwise use the self-contained schema spec in STEP 6 below.

  === STEP 0: SOURCE SELECTION (prefer ready-made natural; default Re-DocRED) ===
  0a. FIRST search HuggingFace (aii-hf-datasets skill) and the web for any ready-made GENUINELY-NATURAL genealogy/kinship/family-relation corpus with (i) natural prose, (ii) gold kinship relations, (iii) genuine absent pairs, (iv) recoverable multi-hop structure. Concrete candidates to inspect and either adopt-if-cleaner or reject-with-reason: 'VLyb/Kinship' (LIKELY an image kinship-verification set, e.g. Families-In-the-Wild -- reject if not TEXT), the 'Sefika/relation-extraction-datasets' collection, and any 'family/genealogy QA' text corpus. Reject templated (CLUTRR-like) or symbolic-id (SpaRP-like) sources -- the whole point is natural text. Most likely none beats Re-DocRED; document the rejection reasons in the card.
  0b. PRIMARY SOURCE = Re-DocRED (HuggingFace 'tonytan48/Re-DocRED'; the completeness-corrected re-annotation of DocRED, Tan et al. 2022, arXiv:2205.12696). Splits: train 3,053 / dev 500 / test 500 = 4,053 docs. Download via aii-hf-datasets / huggingface_hub snapshot_download (json files under ./data: train_revised.json, dev_revised.json, test_revised.json or similar -- inspect the repo tree for exact filenames). FALLBACK if Re-DocRED is unavailable or malformed: vanilla DocRED (thunlp/docred: train_annotated.json, dev.json, test.json) -- but then DOWNGRADE absent-pair confidence in the card (DocRED false negatives corrupt absent gold) and prefer using DocRED only to enlarge the ATOMIC/PRESENT strata, not the ABSENT stratum.
  0c. SECONDARY (target_num_datasets=2): to maximize yield and corroborate, ALSO process the union of Re-DocRED + any vanilla-DocRED docs NOT in Re-DocRED, OR a ready-made natural genealogy corpus if STEP 0a found one. Emit the secondary as a clearly-labeled slice (metadata source field) so iter-7 can include/exclude it. Both share the identical schema.
  0d. Get rel_info.json from the DocRED/Re-DocRED repo to confirm the P-code->name mapping. CONFIRMED family Wikidata properties present in DocRED's 96-relation inventory: P22 (father), P25 (mother), P26 (spouse), P40 (child), P3373 (sibling), P1038 (relative). Use exactly these.

  === STEP 1: PARSE + DETOKENIZE (record char offsets) ===
  DocRED/Re-DocRED ships TOKENIZED 'sents' (list of sentences, each a list of word tokens), NOT raw text. Detokenize to natural prose: join tokens with single spaces and join sentences with a single space, OR use a light detokenizer (e.g. fix spacing before punctuation). CRITICAL: while detokenizing, RECORD per-(sent_id,token_index) character offsets in the reconstructed document so every entity mention's char span can be computed (mirror the char-offset marking in iter-5's data_adapter.py mark_local/local_span). 'input' = this detokenized document text. Compute char_len on it. Note in the card that text is detokenized Wikipedia prose (still natural content, reconstructed from tokens).

  === STEP 2: BUILD THE PER-DOCUMENT KINSHIP GRAPH ===
  For each document: entities = vertexSet (each entity = list of mention dicts {name, sent_id, pos:[tok_start,tok_end], type}); keep PER entities for kinship. Family edges = labels with r in {P22,P25,P26,P40,P3373,P1038}. Direction convention (FIX ONCE, document it): adopt edge(source S, target T, relation) meaning 'T is S's <relation>'. Wikidata semantics for a triple {h, t, r}: P22 father => t is h's father; P25 mother => t is h's mother; P40 child => t is h's child; P26 spouse => symmetric; P3373 sibling => symmetric; P1038 relative => generic, symmetric. Map each to the CLUTRR primitive + gender (from the dependency's relations_store map): father=(inv-child,m), mother=(inv-child,f), child=(child, gender-unknown unless surface cue son/daughter), spouse=(SO, gender unknown unless husband/wife cue), sibling=(sibling, gender unknown unless brother/sister cue). Seed the converse edge from the table (father<->child, mother<->child, etc.), never from an LLM. SPECIAL HANDLING of P1038 'relative': it is too vague to give a precise composable primitive => DO NOT add it as an atomic composable edge, but DO use it to mark the two entities as RELATED so they are EXCLUDED from the absent set. Derive per-entity GENDER from any kinship role/cue that fixes it (object of P22=male, P25=female; surface tokens 'son/brother/husband'=male, 'daughter/sister/wife'=female); leave undetermined otherwise and emit the gender-neutral primitive for composed gold when the final target's gender is unknown.

  === STEP 3: ATOMIC (readable) EDGES -- is_query:false, hop_count:1 ===
  An annotated family edge becomes an ATOMIC edge iff BOTH conditions hold: (i) LOCALITY -- the two entities have mentions co-occurring within a local span (same sentence, or adjacent sentences; also accept the relation's 'evidence' sentence_ids as the supporting span); (ii) SURFACE CUE -- a kinship keyword ('father','mother','son','daughter','brother','sister','wife','husband','married','spouse','grandson','granddaughter',...) appears in that span near both mentions. Record per atomic edge: source, target, kinship_relation (surface, e.g. 'father'), primitive (e.g. 'inv-child'), target_gender, support_span (char span of the evidence sentence(s)), surface_cue (the matched token), evidence_sent_ids. These are the edges a span-local reader is expected to extract; they seed the closure.

  === STEP 4: PRESENT (deduction-required) QUERY EDGES -- is_query:true, hop_count>=2 ===
  Over the atomic-edge graph (undirected for pathfinding, directed for composition), find entity pairs (A,Z) with NO direct annotated family edge AND NO co-occurring local span, but a derivable kinship path of length >=2 whose CLUTRR-table composition yields a DEFINED relation. gold = the composed surface relation (gendered via Z's gender, else neutral primitive); record hop_count (path length), derivation_path (list of intermediate entity_ids), primitive, relation_type. Prefer shortest path; if multiple paths give the SAME composition keep it, if they conflict (should not happen for consistent kinship) drop the pair and log it. NON-CIRCULARITY (state in card): composed relations (grandparent/uncle/aunt/nephew/niece/cousin/in-laws) are NOT in DocRED's relation set, so this gold is never an annotated edge -- it is recoverable ONLY by composition, exactly the held-out multi-hop regime mirroring CLUTRR on natural text. Record hop histogram.

  === STEP 5: ABSENT / NO-DERIVATION QUERY EDGES -- is_absent:true ===
  Within each document, take entity pairs (A,B) where BOTH A and B participate in >=1 annotated family relation (both in the kinship context) AND lie in DIFFERENT connected components of the kinship graph (no direct edge, no derivable path). reason='different_component' (or 'no_path'). Restrict to Re-DocRED so 'no relation' is supported by completeness-corrected gold; EXCLUDE any pair linked by P1038 'relative'. Conservative closed-world label; document the open-world caveat. Cap absent pairs per document (e.g. <=30, sampled to balance against present/atomic counts) to avoid one large article dominating. These are the genuine natural no-relation regime the certificate must beat a confidence-thresholded abstainer on.

  === STEP 6: SCHEMA (exp_sel_data_out; ONE ROW per document) ===
  If art_HS7-lxhZnU9m is available, match its fields EXACTLY; otherwise emit: input = detokenized document text; output = json.dumps(gold_graph) where gold_graph = {
    nodes: [{entity_id, surface (canonical/longest mention name), mention_spans:[[char_start,char_end],...], type:'PER', gender?:'m'|'f'|null, wikidata_qid?:null (DocRED vertexSet has no QIDs -- emit null/omit)}],
    atomic_edges: [{source, target, kinship_relation, primitive, relation_type, target_gender, is_query:false, hop_count:1, support_span:[cs,ce], surface_cue, evidence_sent_ids}],
    query_edges: [{source, target, kinship_relation (gold), primitive, relation_type, target:int? (optional CLUTRR-style numeric id), is_query:true, hop_count (>=2), derivation_path:[entity_id,...]}],
    absent_relation_pairs: [{source, target, reason:'different_component'|'no_path', is_absent:true}]
  }.
  FLAT metadata_* columns per row: metadata_fold (deterministic by doc-text SHA hash, e.g. 5 folds), metadata_source ('re-docred'|'docred'|<ready-made>), metadata_split ('train'|'dev'|'test'), metadata_doc_id (title), metadata_n_entities, metadata_n_per_entities, metadata_n_atomic_edges, metadata_n_family_components, metadata_present_query_count, metadata_absent_pair_count, metadata_char_len, metadata_n_tokens, metadata_hop_histogram (json), metadata_n_ge_2500_chars (int/bool), metadata_has_3000_char (bool), metadata_locally_justifiable_frac. Emit ONCE in TOP-LEVEL dataset metadata: the hand-supplied kinship COMPOSITION TABLE verbatim (CLUTRR rules_store primitive compositions + relations_store surface<->primitive<->gender map), explicitly tagged 'finite kinship composition table, NOT a relation algebra'; plus provenance, license, source repo commit SHA, the open-world absent caveat, and the corpus-level char-length distribution summary (min/median/mean/max, fraction >=2000, fraction >=2500, fraction in [2000,4000]).

  === STEP 7: QA / HONESTY ===
  7a. Verify a random sample (>=50) of atomic edges have their surface cue textually present in the support span; report the pass rate. Report the LOCALLY-JUSTIFIABLE (surface cue stated) vs PURELY-KB-IMPLIED fraction of family edges (non-circularity audit analog).
  7b. Report the fraction of documents reaching ~3000 chars and the [2000,4000] count; if it is small (expected, since avg ~1200 chars), state plainly that natural ~3000-char docs are a minority -- do NOT concatenate or pad.
  7c. OPTIONAL small-LLM judge (via OpenRouter only, e.g. a cheap model) to confirm atomic kinship cues are textually present on a subsample; HARD-CAP well under $2 with SHA-256 prompt cache and a cumulative cost guard. Skip if the deterministic cue check suffices.
  7d. Validate every emitted JSON row against the schema (aii-json). Generate full/mini/preview variants (aii-json); confirm <300MB (aii-file-size-limit). Sanity-check that iter-5's/CLUTRR's loader can parse a sample (json.loads(output) yields nodes/atomic_edges/query_edges/absent_relation_pairs).

  === FAILURE SCENARIOS + FALLBACKS ===
  F1 (KINSHIP TOO SPARSE -> few PRESENT multi-hop queries): family relations are sparse in DocRED. MITIGATE by (i) using ALL 4,053 Re-DocRED docs + non-overlapping vanilla-DocRED docs; (ii) accepting hop_count==2 queries (not only longer chains); (iii) if still <~50 present queries, KEEP the corpus -- the ABSENT-relation stratum is the load-bearing one for iter-7's certificate-vs-confidence claim. Report present-query scarcity honestly; iter-7's pre-registered fork already scopes to absent-only if needed.
  F2 (ABSENT PAIRS SCARCE: single-family biographies have one component): many docs have only one kinship component => no different-component pairs. MITIGATE by scanning all docs and keeping those with >=2 family-participating components; report how many docs/pairs qualify. Do NOT manufacture absent pairs by pairing a family entity with a no-family entity (weakens the 'in kinship context' guarantee) unless flagged separately.
  F3 (CHAR LENGTH BELOW TARGET): expected -- flag/report, do not force. The natural-text requirement matters more than the 3000-char target for iter-7's claim.
  F4 (Re-DocRED LOAD ISSUE): fall back to vanilla DocRED (downgrade absent confidence in card) or the kliang5-style direct-file download; never block on load_dataset script breakage -- read the json files directly.
  F5 (GENDER UNDETERMINED for composed gold): emit gender-neutral primitive (e.g. 'grandparent','sibling','parent','child') and flag; iter-7 can score at primitive level. Keep gendered surface only when the target's gender is fixed by a role/cue.
  F6 (DETOKENIZATION MISALIGNS char offsets): verify a sample of mention char spans equal the mention surface (as iter-5 does with offset_ok_frac); if misaligned, fall back to ordered surface search to locate spans, and report offset_ok_frac in metadata.
target_num_datasets: 2
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_Dm5vYXmD1R8h
type: research
title: Iter-2 Local-Reader / Prolog-Discharge / CLUTRR Implementation-Decision Dossier
summary: >-
  Executor-ready, web-verified resolution of the six NEW implementation decisions the iter-2 closure-certified text-to-logic
  experiments need (beyond the iter-1 dossier art_aQ2Rf8rwqteI). (1) LOCAL-READER PROTOCOL: minimal-span unit = the single
  sentence containing each event mention (default; +/-1 sentence as a sensitivity arm), grounded in TimeBank-Dense's own annotation
  window (same-sentence + immediately-following-sentence + DCT; 5 relations BEFORE/AFTER/INCLUDES/IS_INCLUDED/SIMULTANEOUS
  + VAGUE=underdetermined); 'no shared span' = mentions never co-occur within the window => DEDUCTION-REQUIRED, computable
  WITHOUT the LLM (T0-safe); disjunctive Pairwise read prompt adapted from Wei et al. arXiv:2407.19568 (Bulk/Iterative/Event-Ranking/Pairwise)
  + METRE arXiv:2408.07353 multi-label, enumerate base relations + explicit UNIVERSAL option, 'name every relation the text
  does NOT rule out'. (2) DISCHARGE: SWI-Prolog via pyswip v0.3.3 (class-method Prolog.assertz/query, Python>=3.9, needs apt
  swi-prolog>=8.4.2, ctypes shared-lib + SWI_HOME_DIR/LIBSWIPL_PATH) PRIMARY, robust subprocess fallback `swipl -s f.pl -g
  goal -t halt` (exit 0/1/2), clingo 5.8.0 ASP as secondary; QCN encoded as edge(E1,E2,RelSet) + algebra-seeded compose/3,converse/2;
  readback |R|==1 emit / |R|>1 ABSTAIN / |R|==0 unsound-flag; CONFIDENT-WRONG = nonabstained-single-relation-mismatch-rate
  on the deduction-required/absent subset, matched-coverage, paired-bootstrap CI, pre-registered MDE, aligned to Logic-LM/LINC
  executable-rate practice. (3) CLUTRR: HF CLUTRR/v1 (14 configs, target 0-20 mapping, fields incl proof_state/f_comb/story_edges/edge_types)
  BUT datasets>=4.0 dropped scripts => load via huggingface_hub snapshot_download of the per-task CSVs (git-LFS) or pin datasets<4.0
  + trust_remote_code; kinship composition table = rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender
  map (no-relation is a native primitive); absent-relation pairs CONSTRUCTED from rob_train_disc disconnected components /
  cross-family pairs; atomic-gold = story_edges+edge_types. (4) STRONGER READER: weak anchor = iter-1 google/gemini-3.1-flash-lite
  ($0.25/$1.50); recommend deepseek/deepseek-v3.2 ($0.2288/$0.3432, cross-family, CHEAPER, gate test ~$1.3) as budget-optimal
  stronger reader, google/gemini-3-flash-preview ($0.50/$3.00 thinking) as the clear capability-jump option on a stratified
  subsample; total two-reader run < $10 with disk cache + prompt caching + hard cost-guard. (5) SEVEN local-regime baselines
  each re-specified to read ONLY local spans with a matched single-relation abstention signal (raw verbalized-confidence,
  CoT, self-consistency vote-margin, LINC formalization-agreement, PoT path-agreement [confirmed per-path INDEPENDENT, no
  cross-path intersection], ILP-commit Eirew M=5, naive single-pass intersection), all thresholded to the SAME coverage object.
  (6) Four recent temporal/logical-consistency citations pinned (arXiv:2510.15513, 2502.11425, 2412.16100, 2409.14065) + a
  crisp novelty statement (disjunction-preserving abstain-on-collapse OUTPUT CONTRACT + gold-free closure CERTIFICATE + redundancy-as-coding-rate,
  NOT the algebra). Includes a consolidated decision table, exact IDs/URLs, and a 12-item gotchas list.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1
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

### [8] SYSTEM-USER prompt · 2026-06-18 01:02:19 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx1
type: dataset
title: >-
  Natural-Text Absent-Relation Kinship Corpus from Re-DocRED (STEP-B host for the certificate-vs-confidence-thresholded-abstainer
  experiment)
summary: >-
  Build ONE genuinely-natural (no templating, no concatenation) document-level kinship corpus from Re-DocRED (completeness-corrected
  DocRED Wikipedia prose), standardized to the exp_sel_data_out schema, one row per document, drop-in compatible with the
  CLUTRR kinship dataset so iter-7 reuses the forward-union least-fixpoint closure engine verbatim. Each document yields:
  (a) atomic span-local kinship edges (readable), (b) deduction-required multi-hop PRESENT query edges (gold = CLUTRR-table
  composition, non-circular because composed relations like grandfather/uncle are absent from DocRED's inventory), and (c)
  genuine within-document ABSENT (no-derivation) entity pairs from disconnected kinship components. Completeness-correction
  is the load-bearing reason for the source: it makes 'absent = truly no relation' defensible where vanilla DocRED's false
  negatives would corrupt absent gold. Honestly report char-length distribution (most docs are ~1200 chars; flag/prefer the
  [2000,4000] subset rather than forcing it).
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  GOAL: a corpus of genuinely-natural professional documents (Wikipedia introductory prose) carrying document-level KINSHIP relations, with three populated query strata for iter-7's certificate experiment: derivable multi-hop PRESENT pairs, genuine ABSENT (no-derivation) pairs, and atomic readable edges, plus a hand-supplied kinship composition table.

  WHAT MAKES IT IDEAL:
  1. NATURAL TEXT, NOT TEMPLATED/CONCATENATED. Real Wikipedia prose (the whole point: replace templated CLUTRR and symbolic-id SpaRP). One document = one contiguous natural article; never concatenate sub-stories.
  2. COMPLETENESS-CORRECTED GOLD so 'absent' is defensible. Re-DocRED (tonytan48/Re-DocRED) is preferred over vanilla DocRED precisely because its re-annotation removes DocRED's false-negative relations; an entity pair labeled 'no family relation' is then trustworthy within the document's closed world. This is THE reason absent-relation gold is credible.
  3. GENUINE ABSENT PAIRS. Within-document entity pairs where BOTH entities participate in >=1 annotated family relation (so both are 'in the kinship context') but lie in DIFFERENT connected components of the document's kinship graph => no direct relation and no derivable kinship path. Conservatively labeled (closed-world within the document; open-world caveat documented in the card).
  4. RECOVERABLE GOLD. Atomic edges = family relations whose two entity mentions co-occur in a local span (same/adjacent sentence) AND whose surface kinship cue ('son','daughter','father','mother','brother','sister','wife','husband','married','grandson',...) is textually present near both mentions, so a span-local reader can plausibly extract them. PRESENT query gold = composition over atomic edges via the hand-supplied CLUTRR finite kinship table (forward-union least fixpoint). Composed relations (grandfather/grandmother/uncle/aunt/nephew/niece/in-laws/cousins) are OUTSIDE DocRED's relation inventory, so multi-hop gold is provably non-circular (never an annotated edge).
  5. HAND-SUPPLIED COMPOSITION TABLE (reused, not invented). The CLUTRR rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender map (documented in dependency art_Dm5vYXmD1R8h), emitted verbatim ONCE in top-level metadata and explicitly labeled NOT a relation algebra (a finite kinship table). This is the SAME table every kinship arm uses, so iter-7's engine runs unchanged.
  6. SCHEMA PARITY. exp_sel_data_out schema, ONE ROW per document, drop-in compatible with the CLUTRR kinship dataset (art_HS7-lxhZnU9m) so iter-7 reuses loaders/closure verbatim.
  7. CHAR-LENGTH HONESTY. Report per-document char length; PREFER/flag documents in [2000,4000] chars to supply genuinely-natural ~3000-char professional documents (addresses the scope MINOR with NON-constructed text). DocRED docs average ~196.7 words (~1200 chars), so do NOT hard-filter to >=3000 (that would gut the corpus) -- keep all docs with usable kinship structure, flag the long subset, and report the fraction reaching the target.
  8. COMMODITY-SCALE. The whole corpus (4,053 docs, small graphs) is < 50MB raw; well under the 300MB cap; full/mini/preview variants.
  9. $0 LLM (pure data construction). An OPTIONAL small-LLM judge to confirm atomic kinship cues are textually present is capped well under $2 with a SHA-256 prompt cache.

  SCALE TARGETS (report actuals; do not pad): aim across the whole corpus for >=150 derivable PRESENT multi-hop query edges and >=300 ABSENT pairs spread over as many documents as yield them; if PRESENT queries are scarce (family relations are sparse in DocRED), the corpus still primarily serves the ABSENT-relation experiment (the load-bearing one for iter-7) -- report counts honestly and let iter-7's fork decide scope.
dataset_search_plan: |-
  Compute profile: cpu_heavy (pure CPU JSON/graph processing on ~4k small docs; no GPU; the only non-GPU dataset profile offered). Read dependency art_Dm5vYXmD1R8h/research_out.json FIRST (it pins the CLUTRR kinship table = rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender map, and the absent-relation construction recipe). If the sibling CLUTRR kinship dataset art_HS7-lxhZnU9m is present in this run's workspace, READ its data.py/schema for exact field parity; otherwise use the self-contained schema spec in STEP 6 below.

  === STEP 0: SOURCE SELECTION (prefer ready-made natural; default Re-DocRED) ===
  0a. FIRST search HuggingFace (aii-hf-datasets skill) and the web for any ready-made GENUINELY-NATURAL genealogy/kinship/family-relation corpus with (i) natural prose, (ii) gold kinship relations, (iii) genuine absent pairs, (iv) recoverable multi-hop structure. Concrete candidates to inspect and either adopt-if-cleaner or reject-with-reason: 'VLyb/Kinship' (LIKELY an image kinship-verification set, e.g. Families-In-the-Wild -- reject if not TEXT), the 'Sefika/relation-extraction-datasets' collection, and any 'family/genealogy QA' text corpus. Reject templated (CLUTRR-like) or symbolic-id (SpaRP-like) sources -- the whole point is natural text. Most likely none beats Re-DocRED; document the rejection reasons in the card.
  0b. PRIMARY SOURCE = Re-DocRED (HuggingFace 'tonytan48/Re-DocRED'; the completeness-corrected re-annotation of DocRED, Tan et al. 2022, arXiv:2205.12696). Splits: train 3,053 / dev 500 / test 500 = 4,053 docs. Download via aii-hf-datasets / huggingface_hub snapshot_download (json files under ./data: train_revised.json, dev_revised.json, test_revised.json or similar -- inspect the repo tree for exact filenames). FALLBACK if Re-DocRED is unavailable or malformed: vanilla DocRED (thunlp/docred: train_annotated.json, dev.json, test.json) -- but then DOWNGRADE absent-pair confidence in the card (DocRED false negatives corrupt absent gold) and prefer using DocRED only to enlarge the ATOMIC/PRESENT strata, not the ABSENT stratum.
  0c. SECONDARY (target_num_datasets=2): to maximize yield and corroborate, ALSO process the union of Re-DocRED + any vanilla-DocRED docs NOT in Re-DocRED, OR a ready-made natural genealogy corpus if STEP 0a found one. Emit the secondary as a clearly-labeled slice (metadata source field) so iter-7 can include/exclude it. Both share the identical schema.
  0d. Get rel_info.json from the DocRED/Re-DocRED repo to confirm the P-code->name mapping. CONFIRMED family Wikidata properties present in DocRED's 96-relation inventory: P22 (father), P25 (mother), P26 (spouse), P40 (child), P3373 (sibling), P1038 (relative). Use exactly these.

  === STEP 1: PARSE + DETOKENIZE (record char offsets) ===
  DocRED/Re-DocRED ships TOKENIZED 'sents' (list of sentences, each a list of word tokens), NOT raw text. Detokenize to natural prose: join tokens with single spaces and join sentences with a single space, OR use a light detokenizer (e.g. fix spacing before punctuation). CRITICAL: while detokenizing, RECORD per-(sent_id,token_index) character offsets in the reconstructed document so every entity mention's char span can be computed (mirror the char-offset marking in iter-5's data_adapter.py mark_local/local_span). 'input' = this detokenized document text. Compute char_len on it. Note in the card that text is detokenized Wikipedia prose (still natural content, reconstructed from tokens).

  === STEP 2: BUILD THE PER-DOCUMENT KINSHIP GRAPH ===
  For each document: entities = vertexSet (each entity = list of mention dicts {name, sent_id, pos:[tok_start,tok_end], type}); keep PER entities for kinship. Family edges = labels with r in {P22,P25,P26,P40,P3373,P1038}. Direction convention (FIX ONCE, document it): adopt edge(source S, target T, relation) meaning 'T is S's <relation>'. Wikidata semantics for a triple {h, t, r}: P22 father => t is h's father; P25 mother => t is h's mother; P40 child => t is h's child; P26 spouse => symmetric; P3373 sibling => symmetric; P1038 relative => generic, symmetric. Map each to the CLUTRR primitive + gender (from the dependency's relations_store map): father=(inv-child,m), mother=(inv-child,f), child=(child, gender-unknown unless surface cue son/daughter), spouse=(SO, gender unknown unless husband/wife cue), sibling=(sibling, gender unknown unless brother/sister cue). Seed the converse edge from the table (father<->child, mother<->child, etc.), never from an LLM. SPECIAL HANDLING of P1038 'relative': it is too vague to give a precise composable primitive => DO NOT add it as an atomic composable edge, but DO use it to mark the two entities as RELATED so they are EXCLUDED from the absent set. Derive per-entity GENDER from any kinship role/cue that fixes it (object of P22=male, P25=female; surface tokens 'son/brother/husband'=male, 'daughter/sister/wife'=female); leave undetermined otherwise and emit the gender-neutral primitive for composed gold when the final target's gender is unknown.

  === STEP 3: ATOMIC (readable) EDGES -- is_query:false, hop_count:1 ===
  An annotated family edge becomes an ATOMIC edge iff BOTH conditions hold: (i) LOCALITY -- the two entities have mentions co-occurring within a local span (same sentence, or adjacent sentences; also accept the relation's 'evidence' sentence_ids as the supporting span); (ii) SURFACE CUE -- a kinship keyword ('father','mother','son','daughter','brother','sister','wife','husband','married','spouse','grandson','granddaughter',...) appears in that span near both mentions. Record per atomic edge: source, target, kinship_relation (surface, e.g. 'father'), primitive (e.g. 'inv-child'), target_gender, support_span (char span of the evidence sentence(s)), surface_cue (the matched token), evidence_sent_ids. These are the edges a span-local reader is expected to extract; they seed the closure.

  === STEP 4: PRESENT (deduction-required) QUERY EDGES -- is_query:true, hop_count>=2 ===
  Over the atomic-edge graph (undirected for pathfinding, directed for composition), find entity pairs (A,Z) with NO direct annotated family edge AND NO co-occurring local span, but a derivable kinship path of length >=2 whose CLUTRR-table composition yields a DEFINED relation. gold = the composed surface relation (gendered via Z's gender, else neutral primitive); record hop_count (path length), derivation_path (list of intermediate entity_ids), primitive, relation_type. Prefer shortest path; if multiple paths give the SAME composition keep it, if they conflict (should not happen for consistent kinship) drop the pair and log it. NON-CIRCULARITY (state in card): composed relations (grandparent/uncle/aunt/nephew/niece/cousin/in-laws) are NOT in DocRED's relation set, so this gold is never an annotated edge -- it is recoverable ONLY by composition, exactly the held-out multi-hop regime mirroring CLUTRR on natural text. Record hop histogram.

  === STEP 5: ABSENT / NO-DERIVATION QUERY EDGES -- is_absent:true ===
  Within each document, take entity pairs (A,B) where BOTH A and B participate in >=1 annotated family relation (both in the kinship context) AND lie in DIFFERENT connected components of the kinship graph (no direct edge, no derivable path). reason='different_component' (or 'no_path'). Restrict to Re-DocRED so 'no relation' is supported by completeness-corrected gold; EXCLUDE any pair linked by P1038 'relative'. Conservative closed-world label; document the open-world caveat. Cap absent pairs per document (e.g. <=30, sampled to balance against present/atomic counts) to avoid one large article dominating. These are the genuine natural no-relation regime the certificate must beat a confidence-thresholded abstainer on.

  === STEP 6: SCHEMA (exp_sel_data_out; ONE ROW per document) ===
  If art_HS7-lxhZnU9m is available, match its fields EXACTLY; otherwise emit: input = detokenized document text; output = json.dumps(gold_graph) where gold_graph = {
    nodes: [{entity_id, surface (canonical/longest mention name), mention_spans:[[char_start,char_end],...], type:'PER', gender?:'m'|'f'|null, wikidata_qid?:null (DocRED vertexSet has no QIDs -- emit null/omit)}],
    atomic_edges: [{source, target, kinship_relation, primitive, relation_type, target_gender, is_query:false, hop_count:1, support_span:[cs,ce], surface_cue, evidence_sent_ids}],
    query_edges: [{source, target, kinship_relation (gold), primitive, relation_type, target:int? (optional CLUTRR-style numeric id), is_query:true, hop_count (>=2), derivation_path:[entity_id,...]}],
    absent_relation_pairs: [{source, target, reason:'different_component'|'no_path', is_absent:true}]
  }.
  FLAT metadata_* columns per row: metadata_fold (deterministic by doc-text SHA hash, e.g. 5 folds), metadata_source ('re-docred'|'docred'|<ready-made>), metadata_split ('train'|'dev'|'test'), metadata_doc_id (title), metadata_n_entities, metadata_n_per_entities, metadata_n_atomic_edges, metadata_n_family_components, metadata_present_query_count, metadata_absent_pair_count, metadata_char_len, metadata_n_tokens, metadata_hop_histogram (json), metadata_n_ge_2500_chars (int/bool), metadata_has_3000_char (bool), metadata_locally_justifiable_frac. Emit ONCE in TOP-LEVEL dataset metadata: the hand-supplied kinship COMPOSITION TABLE verbatim (CLUTRR rules_store primitive compositions + relations_store surface<->primitive<->gender map), explicitly tagged 'finite kinship composition table, NOT a relation algebra'; plus provenance, license, source repo commit SHA, the open-world absent caveat, and the corpus-level char-length distribution summary (min/median/mean/max, fraction >=2000, fraction >=2500, fraction in [2000,4000]).

  === STEP 7: QA / HONESTY ===
  7a. Verify a random sample (>=50) of atomic edges have their surface cue textually present in the support span; report the pass rate. Report the LOCALLY-JUSTIFIABLE (surface cue stated) vs PURELY-KB-IMPLIED fraction of family edges (non-circularity audit analog).
  7b. Report the fraction of documents reaching ~3000 chars and the [2000,4000] count; if it is small (expected, since avg ~1200 chars), state plainly that natural ~3000-char docs are a minority -- do NOT concatenate or pad.
  7c. OPTIONAL small-LLM judge (via OpenRouter only, e.g. a cheap model) to confirm atomic kinship cues are textually present on a subsample; HARD-CAP well under $2 with SHA-256 prompt cache and a cumulative cost guard. Skip if the deterministic cue check suffices.
  7d. Validate every emitted JSON row against the schema (aii-json). Generate full/mini/preview variants (aii-json); confirm <300MB (aii-file-size-limit). Sanity-check that iter-5's/CLUTRR's loader can parse a sample (json.loads(output) yields nodes/atomic_edges/query_edges/absent_relation_pairs).

  === FAILURE SCENARIOS + FALLBACKS ===
  F1 (KINSHIP TOO SPARSE -> few PRESENT multi-hop queries): family relations are sparse in DocRED. MITIGATE by (i) using ALL 4,053 Re-DocRED docs + non-overlapping vanilla-DocRED docs; (ii) accepting hop_count==2 queries (not only longer chains); (iii) if still <~50 present queries, KEEP the corpus -- the ABSENT-relation stratum is the load-bearing one for iter-7's certificate-vs-confidence claim. Report present-query scarcity honestly; iter-7's pre-registered fork already scopes to absent-only if needed.
  F2 (ABSENT PAIRS SCARCE: single-family biographies have one component): many docs have only one kinship component => no different-component pairs. MITIGATE by scanning all docs and keeping those with >=2 family-participating components; report how many docs/pairs qualify. Do NOT manufacture absent pairs by pairing a family entity with a no-family entity (weakens the 'in kinship context' guarantee) unless flagged separately.
  F3 (CHAR LENGTH BELOW TARGET): expected -- flag/report, do not force. The natural-text requirement matters more than the 3000-char target for iter-7's claim.
  F4 (Re-DocRED LOAD ISSUE): fall back to vanilla DocRED (downgrade absent confidence in card) or the kliang5-style direct-file download; never block on load_dataset script breakage -- read the json files directly.
  F5 (GENDER UNDETERMINED for composed gold): emit gender-neutral primitive (e.g. 'grandparent','sibling','parent','child') and flag; iter-7 can score at primitive level. Keep gendered surface only when the target's gender is fixed by a role/cue.
  F6 (DETOKENIZATION MISALIGNS char offsets): verify a sample of mention char spans equal the mention surface (as iter-5 does with offset_ok_frac); if misaligned, fall back to ordered surface search to locate spans, and report offset_ok_frac in metadata.
target_num_datasets: 2
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_Dm5vYXmD1R8h
type: research
title: Iter-2 Local-Reader / Prolog-Discharge / CLUTRR Implementation-Decision Dossier
summary: >-
  Executor-ready, web-verified resolution of the six NEW implementation decisions the iter-2 closure-certified text-to-logic
  experiments need (beyond the iter-1 dossier art_aQ2Rf8rwqteI). (1) LOCAL-READER PROTOCOL: minimal-span unit = the single
  sentence containing each event mention (default; +/-1 sentence as a sensitivity arm), grounded in TimeBank-Dense's own annotation
  window (same-sentence + immediately-following-sentence + DCT; 5 relations BEFORE/AFTER/INCLUDES/IS_INCLUDED/SIMULTANEOUS
  + VAGUE=underdetermined); 'no shared span' = mentions never co-occur within the window => DEDUCTION-REQUIRED, computable
  WITHOUT the LLM (T0-safe); disjunctive Pairwise read prompt adapted from Wei et al. arXiv:2407.19568 (Bulk/Iterative/Event-Ranking/Pairwise)
  + METRE arXiv:2408.07353 multi-label, enumerate base relations + explicit UNIVERSAL option, 'name every relation the text
  does NOT rule out'. (2) DISCHARGE: SWI-Prolog via pyswip v0.3.3 (class-method Prolog.assertz/query, Python>=3.9, needs apt
  swi-prolog>=8.4.2, ctypes shared-lib + SWI_HOME_DIR/LIBSWIPL_PATH) PRIMARY, robust subprocess fallback `swipl -s f.pl -g
  goal -t halt` (exit 0/1/2), clingo 5.8.0 ASP as secondary; QCN encoded as edge(E1,E2,RelSet) + algebra-seeded compose/3,converse/2;
  readback |R|==1 emit / |R|>1 ABSTAIN / |R|==0 unsound-flag; CONFIDENT-WRONG = nonabstained-single-relation-mismatch-rate
  on the deduction-required/absent subset, matched-coverage, paired-bootstrap CI, pre-registered MDE, aligned to Logic-LM/LINC
  executable-rate practice. (3) CLUTRR: HF CLUTRR/v1 (14 configs, target 0-20 mapping, fields incl proof_state/f_comb/story_edges/edge_types)
  BUT datasets>=4.0 dropped scripts => load via huggingface_hub snapshot_download of the per-task CSVs (git-LFS) or pin datasets<4.0
  + trust_remote_code; kinship composition table = rules_store.yaml primitive compositions + relations_store.yaml surface<->primitive<->gender
  map (no-relation is a native primitive); absent-relation pairs CONSTRUCTED from rob_train_disc disconnected components /
  cross-family pairs; atomic-gold = story_edges+edge_types. (4) STRONGER READER: weak anchor = iter-1 google/gemini-3.1-flash-lite
  ($0.25/$1.50); recommend deepseek/deepseek-v3.2 ($0.2288/$0.3432, cross-family, CHEAPER, gate test ~$1.3) as budget-optimal
  stronger reader, google/gemini-3-flash-preview ($0.50/$3.00 thinking) as the clear capability-jump option on a stratified
  subsample; total two-reader run < $10 with disk cache + prompt caching + hard cost-guard. (5) SEVEN local-regime baselines
  each re-specified to read ONLY local spans with a matched single-relation abstention signal (raw verbalized-confidence,
  CoT, self-consistency vote-margin, LINC formalization-agreement, PoT path-agreement [confirmed per-path INDEPENDENT, no
  cross-path intersection], ILP-commit Eirew M=5, naive single-pass intersection), all thresholded to the SAME coverage object.
  (6) Four recent temporal/logical-consistency citations pinned (arXiv:2510.15513, 2502.11425, 2412.16100, 2409.14065) + a
  crisp novelty statement (disjunction-preserving abstain-on-collapse OUTPUT CONTRACT + gold-free closure CERTIFICATE + redundancy-as-coding-rate,
  NOT the algebra). Includes a consolidated decision table, exact IDs/URLs, and a 12-item gotchas list.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/gen_art/gen_art_research_1
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
