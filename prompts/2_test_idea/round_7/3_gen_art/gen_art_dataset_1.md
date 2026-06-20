# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 7 · `gen_art`
> Run: `run_IuSkWzF0As-P` — No Derivation, No Relation: A Closure Certificate for Compositional Absent-Relat
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-18 02:22:28 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/results/out.json`
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
  Natural-Text Absent-Relation Located-In (Administrative Containment) Corpus from Re-DocRED + DocRED
summary: >-
  A SECOND genuinely-natural absent-relation domain (geographic / administrative containment, 'located-in') built from Re-DocRED
  Wikipedia prose, to show the confidence-blindness diagnostic (FACT A + FACT B) is NOT kinship-specific. It is the structural
  twin of the iter-6 natural kinship corpus (art_NUWTxBVWENIJ): same exp_sel_data_out schema (one row per document), same
  drop-in forward-closure engine pattern (kinship.py REUSED VERBATIM with a new degenerate transitive composition table),
  same three strata (atomic located-in edges / present multi-hop transitive-deduction query edges / absent no-containment
  pairs). The composition is the single transitive rule located_in(A,B) AND located_in(B,C) => located_in(A,C) (explicitly
  tagged NOT a relation algebra). Consumed by iter-8's domain-generality confidence-blindness experiment. $0 LLM (deterministic
  cue check; optional <$2 LLM judge, skippable). Compute: cpu_heavy.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  GOAL: a document-level GEOGRAPHIC / ADMINISTRATIVE CONTAINMENT (located-in) corpus over GENUINELY-NATURAL Wikipedia introductory
  prose (no templating, no concatenation, no padding), standardized to the exp_sel_data_out schema (ONE ROW PER DOCUMENT)
  and DROP-IN compatible with the iter-6 kinship engine + the iter-7/iter-8 four-signal battery experiment loaders. Each document
  yields a gold containment graph with: (1) NODES = place / administrative entities with surface form, NER type, and per-mention
  char-offset spans verified against the detokenized text (offset_ok_frac >= ~0.98); (2) ATOMIC located-in EDGES = locally-stated
  containment edges (adjacent-sentence co-occurrence + a surface cue such as 'in / located in / capital of / part of / district
  of / province of'), each flagged locally_justifiable so a span-local reader could plausibly extract it; (3) PRESENT query_edges
  = HELD-OUT multi-hop ancestor pairs with NO direct annotated edge and NO local co-occurrence, derivable >=2-hop by located-in
  transitivity (fields: hop_count, derivation_path, fully_readable, composed_only) -- the deduction-required, NON-CIRCULAR
  present stratum; (4) ABSENT_RELATION_PAIRS = entity pairs with NO containment path in EITHER direction (closed-world within
  the document), spanning two structurally-sound regimes: (a) DIFFERENT connected components (totally unrelated places --
  the clean kinship-analog), and (b) SAME component but no ancestor-descendant path (sibling / cousin places, e.g. two cities
  in one country, neither located in the other -- the containment-specific absent regime, which is the exact 'natural spatial-containment
  absent pairs' the reviewer named). CRITICAL PROPERTY: the absent gold must be TRUSTWORTHY -- this requires Re-DocRED (the
  completeness-corrected re-annotation of DocRED that recovers ~64.6% of triples DocRED missed), because vanilla DocRED false-negatives
  would turn genuinely-contained pairs into SPURIOUS absent pairs. Vanilla DocRED is kept ONLY as a clearly-labelled secondary
  slice whose absent gold is DOWNGRADED (corroborates the atomic/present strata + demonstrates the completeness-correction
  effect). HONESTY: report ACTUAL char lengths (DocRED intros average ~1000 chars; essentially none reach 3000 -- do NOT pad/concatenate;
  the natural-text + absent-relation regime is the load-bearing property, not the 3000-char target), the docred-absent false-negative
  downgrade, and located-in-specific caveats (administrative-hierarchy ambiguity; entities with multiple containers/parents
  = DAG not strict tree; country-vs-region granularity; P276 'location' lower precision). SIZE: geographic relations (P131,
  P17) are among DocRED's MOST FREQUENT, so this corpus should be SUBSTANTIALLY DENSER than the kinship corpus (which yielded
  360 present / 368 absent on re-docred) -- expect many hundreds-to-thousands of atomic edges, hundreds-plus of present multi-hop
  queries, and a large absent set (siblings are abundant); apply per-document caps so no single document dominates. The whole
  build is deterministic ($0 LLM) and must pass a round-trip GATE: the transitive-closure engine reproduces EVERY emitted
  present gold as a singleton and derives EMPTY for EVERY absent pair.
dataset_search_plan: |-
  This corpus is a deterministic TRANSFORMATION of an already-pinned source (Re-DocRED + DocRED) reusing a frozen pipeline; it is NOT an open-ended dataset search. Follow these steps.

  === STEP 0: READ THE FROZEN KINSHIP PIPELINE (the template to mirror) ===
  Direct filesystem-read (do NOT re-download, do NOT wire as a formal dependency -- it is a sibling dataset) the iter-6 kinship corpus workspace at:
    /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/
  Key files to copy/adapt: detok.py (REUSE VERBATIM -- detokenize(sents)->(text,offsets), mention_char_span(offsets,sent_id,pos), sent_char_span(offsets,sent_id)); kinship.py (REUSE VERBATIM as the closure engine -- see STEP 3 for why a new table makes it work unchanged); build.py (ADAPT -- this is the per-document graph builder, the main work); assemble.py + verify.py + probe.py (ADAPT -- corpus assembly, round-trip QA, optional cue probe); clutrr_composition_table.json + README.md (reference for schema/metadata fields). The raw Re-DocRED/DocRED JSON is already cached under that workspace's temp/datasets/ (train_revised.json/dev_revised.json/test_revised.json for re-docred; train_annotated.json/dev.json/rel_info.json for docred) -- you may copy these into your own temp/ to avoid re-download, but re-pin commits per STEP 1.

  === STEP 1: ACQUIRE SOURCES (pin commits) ===
  PRIMARY: tonytan48/Re-DocRED (HuggingFace dataset), commit e0ab3489edfe72c968261bffed5243b6fefddd22, MIT license (Wikipedia text CC BY-SA), arXiv:2205.12696 (Tan et al., EMNLP 2022). Files: train_revised.json (3,053 docs), dev_revised.json (500), test_revised.json (500). SECONDARY (labelled, absent-gold DOWNGRADED): thunlp/docred, commit 7985b4e0371e6c61a756feb41b7b27becf71c666, MIT, arXiv:1906.06127 (Yao et al., ACL 2019). Files: train_annotated.json, dev.json, rel_info.json (the 96-relation id->name map). Each doc = {title, sents (list of tokenized sentences), vertexSet (list of entities; each a list of mentions {name, sent_id, pos:[start,end], type}), labels (list of {h, t, r, evidence})}. Use the aii-hf-datasets skill or direct HF download; verify total size << 300MB.

  === STEP 2: VERIFY & REPORT LOCATED-IN PROPERTY COVERAGE ===
  Confirmed in rel_info.json (already inspected): the located-in / administrative-containment Wikidata properties DocRED annotates are -- P131 'located in the administrative territorial entity', P17 'country', P150 'contains administrative territorial entity', P276 'location', P1376 'capital of', P36 'capital', and (optional, top-level) P30 'continent', P706 'located on terrain feature', P205 'basin country'. CORE VOCABULARY (use these): {P131, P17, P150, P1376, P36}. OPTIONAL/lower-precision (include only with LOC-LOC endpoints + a distinct provenance tag, report counts separately so iter-8 can ablate): {P276, P30, P706}. Web-confirmed: P131 and P17 are among DocRED's MOST FREQUENT relations (geographic relations dominate), so expect high volume. ACTION: compute and report, per slice (re-docred / docred) and per split, the per-property edge counts (LOC-LOC and all-endpoint), the number of family-of-containment-bearing documents, and the resulting atomic-edge / present-query / absent-pair totals -- this is the sizing/power check, analogous to the kinship README's 'Honest stats' table.

  === STEP 3: BUILD THE CONTAINMENT COMPOSITION TABLE (so kinship.py runs UNCHANGED) ===
  Key realization: kinship.py's Kinship class + forward_closure() is a GENERIC finite-composition least-fixpoint UNION engine parameterized entirely by the composition-table JSON (relation_types, symmetric_types, inverse_pairs, composition_rules, surface_forms, label_map). It needs NO code change for located-in. Write containment_composition_table.json with a SINGLE transitive relation plus its converse:
    relation_types: {"located_in": {"symmetric": false, "inverse": "contains"}, "contains": {"symmetric": false, "inverse": "located_in"}}
    symmetric_types: []
    inverse_pairs: {"located_in": "contains"}
    composition_rules: {"located_in": {"located_in": "located_in"}, "contains": {"contains": "contains"}}  // ONLY these two rules; every other composition (e.g. located_in o contains) is UNDEFINED => adds nothing => SOUND
    surface_forms: {"located_in": {"male": "located in", "female": "located in"}, "contains": {"male": "contains", "female": "contains"}}  (gender-trivial; places have no gender)
    surface_reverse / label_map / label_map_reverse: trivial 2-entry maps.
    note (verbatim, load-bearing honesty tag): "DEGENERATE single-relation TRANSITIVE composition table. located_in is a strict partial order (antisymmetric, transitive) over place/administrative entities; 'contains' is its converse. The ONLY defined compositions are located_in o located_in = located_in and contains o contains = contains. This is NOT a relation algebra (no general intersection/converse closure, no disjunctive relations). Emitted verbatim once in metadata.composition_table."
  WHY THIS WORKS (verify, then state in the card): with inverse_pairs set, kinship.py conv_type(located_in)='contains' and conv_type(contains)='located_in'; _seed adds each located_in edge a->b AND its converse contains edge b->a; the fixpoint composes located_in chains downward (descendant->ancestor) and contains chains upward, while located_in o contains is UNDEFINED so NO spurious cross-links appear. Therefore D[(a,b)]={located_in} iff a is a transitive descendant of b; D[(a,b)]={contains} iff a is a transitive ancestor of b; D[(a,b)]=EMPTY for sibling/cousin pairs AND different-component pairs (the absent regime); D[(a,b)] with |.|>1 (i.e. both located_in and contains) only on an annotation CYCLE (a<->b contradiction) -> a Mode-B conflict certificate (report the count).

  === STEP 4: ADAPT build.py (per-document graph builder) ===
  Start from kinship build.py and change ONLY the relation-specific parts; keep the detok/offset/locality/component/caps machinery. Concretely:
  (4a) PROPERTY -> PRIMITIVE + DIRECTION CONVENTION (edge source->target:located_in means 'source is located in target'). For DocRED triple {h, t, r}: P131 -> source=h, target=t (h located_in t); P17 -> source=h, target=t; P276 -> source=h, target=t; P1376 ('h is capital of t') -> source=h, target=t (a capital is located in its territory); P150 ('h contains t') -> INVERT: source=t, target=h; P36 ('h's capital is t') -> INVERT: source=t, target=h. Record the originating wikidata_property on every atomic edge for ablation. DEDUP consistent edges (P131 h->t and P150 t->h collapse to the same located_in(h,t)); if a doc asserts BOTH located_in(a,b) and located_in(b,a) (a true 2-cycle, e.g. P131 and P150 disagreeing), DROP the pair from atomics and log it as a contradiction (also surfaces as a Mode-B conflict if kept).
  (4b) ENTITY-TYPE FILTER: keep only edges whose BOTH endpoints have majority NER type LOC (DocRED types include PER/ORG/LOC/TIME/NUM/MISC). This keeps a pure place-containment graph; report how many edges this drops per property (P131/P17/P150/P1376/P36 are ~always LOC-LOC; P276 is the main one that drops).
  (4c) DROP gender derivation entirely (derive_genders + appositive vote tables) -- not applicable to places. surface word for an edge is just 'located in' / 'contains'. (OPTIONAL, non-load-bearing: a light admin-LEVEL tag {country/region/city/other} from surface cues like 'country','province','state','county','district','city','town','village','capital' for stratification metadata; skip if time-constrained.)
  (4d) SURFACE CUES for locally_justifiable (token-level, lowercased, within the support span): general containment cues {'in','located','situated','within','part','district','province','county','region','municipality','city','town','village','borough','prefecture','county','commune','near'} plus property-specific {P1376/P36: 'capital','capital of'; P150: 'contains','includes','comprises','consists'}. NOTE 'in' is the weak high-frequency workhorse cue (the canonical 'X, a city in Y' Wikipedia pattern) -- require it ALONGSIDE adjacent-sentence co-occurrence (locality) to set locally_justifiable=True, exactly mirroring kinship.
  (4e) ATOMIC EDGES: every kept located_in edge seeds the closure; flag locality (a mention of source and of target within adjacent sentences) + has_cue + locally_justifiable; record support_span (evidence sents if given else closest co-occurrence sents), evidence_sent_ids, wikidata_property. (Expected locally_justifiable_frac similar to or higher than kinship's ~0.62, since 'X in Y' geographic phrasing is dense.)
  (4f) PRESENT query_edges (deduction-required, NON-CIRCULAR): from forward_closure, take directed pairs (a,b) with D[(a,b)]=={'located_in'} singleton, NO direct annotated edge, NO local co-occurrence (min_sent_dist>=2 OR no shared span), BFS hop_count>=2. Fields: source, target, primitive='located_in', relation_type='located_in', is_query=True, hop_count, derivation_path (intermediate container ids), fully_readable (all path edges locally_justifiable), composed_only=True (a transitively-implied containment that is NEVER itself an annotated edge -> provably non-circular, the analog of kinship's grand/uncle types). Deterministic cap present_cap (e.g. 40), shortest-hops-first; set present_truncated flag.
  (4g) ABSENT_RELATION_PAIRS (no-derivation, the headline absent regime): a directed/unordered pair {a,b} of containment-participating entities is ABSENT iff D[(a,b)]==EMPTY AND D[(b,a)]==EMPTY (no containment EITHER direction). Tag reason: 'different_component' (a,b in different undirected components -- the clean kinship-analog) vs 'same_component_sibling' (a,b in the SAME component but no ancestor-descendant path -- e.g. two cities in one country; the containment-specific, reviewer-named regime). Both round-trip to EMPTY under the engine (VERIFY: located_in o contains is UNDEFINED, so siblings derive nothing). Record num_components and, per pair, whether it is same- or cross-component, so iter-8 can stratify. Siblings are combinatorially abundant -> apply a per-document absent_cap (e.g. 30) with STRATIFIED sampling (mix cross-component and sibling pairs; deterministic sort then cap) and set absent_truncated. Closed-world caveat applies (open-world distant containment may exist but is not derivable from the text); TRUSTWORTHY on re-docred, DOWNGRADED on docred.
  (4h) NODES + flat metadata_* exactly mirroring the kinship row schema, swapping kinship-specific fields: metadata_fold = SHA-256(input)%5, metadata_source, metadata_split, metadata_doc_id, metadata_n_entities, metadata_n_loc_entities, metadata_n_atomic_edges, metadata_n_locally_justifiable_edges, metadata_locally_justifiable_frac, metadata_n_components, metadata_present_query_count, metadata_composed_only_present_count, metadata_present_truncated, metadata_absent_pair_count, metadata_absent_different_component_count, metadata_absent_same_component_count, metadata_absent_truncated, metadata_char_len, metadata_n_tokens, metadata_hop_histogram (json), metadata_n_ge_2500_chars, metadata_has_3000_char, metadata_offset_ok_frac, metadata_n_fired_closure, metadata_relation_set (the located-in properties present in the doc). output = json.dumps(gold_graph) with {doc_id, source, split, nodes, atomic_edges, query_edges, absent_relation_pairs, absent_pairs_source='structural_closure'}.

  === STEP 5: CLOSURE / round-trip ===
  Run kinship.py forward_closure(KIN, [{a:source,b:target,type:'located_in'} for atomic edges]) per doc to derive present queries and validate absent emptiness in the same pass build.py already uses for kinship.

  === STEP 6: ADAPT assemble.py ===
  Build full corpus (all docs with >=1 located-in edge), emit the top-level metadata block: name/description/schema, gold_graph_field_spec, composition_table (the containment table verbatim) + composition_table_note (NOT-a-relation-algebra tag), engine_edge_mapping ({a:source,b:target,type:'located_in'}), docred_locatedin_properties map, provenance (both commits, papers, licenses, CLUTRR-free since no kinship table needed here), char_length_distribution (per slice: min/median/mean/max, frac>=2000/2500/3000 -- expect ~0 at 3000), completeness_correction_evidence (located-in edges recovered by re-docred vs docred on shared titles; spurious-absent reduction), build_stats (per slice: n_docs, present_total, absent_total split by reason, composed_only_present, hop_hist, type/property hist, mean_offset_ok, mean_locally_justifiable_frac), qa (cue-present pass rate), plan_corrections, caveats. Write full_data_out.json + mini_data_out.json + preview_data_out.json (use aii-json to generate mini/preview).

  === STEP 7: ROUND-TRIP GATE (adapt verify.py) ===
  For every row: reload gold_graph, feed atomic_edges to forward_closure, assert (i) EVERY present query_edge (source,target) yields D==={'located_in'} (singleton EMIT); (ii) EVERY absent pair yields D[(a,b)]==EMPTY AND D[(b,a)]==EMPTY (ABSTAIN); (iii) report any Mode-B conflicts (|D|>1 from annotation cycles). Print verified counts (e.g. 'NNN/NNN present golds reproduced, MMM/MMM absent pairs empty') and FAIL loudly on any mismatch. This is the same engine the iter-8 battery experiment loads, so passing the gate guarantees drop-in compatibility.

  === STEP 8: VALIDATE + SIZE-SPLIT + CARD ===
  Validate full/mini/preview against the exp_sel_data_out schema via aii-json. Run the aii-file-size-limit procedure; split full_data_out.json if oversized. Write dataset_card.md with: a located-in coverage table (per-property counts per slice), provenance/licenses/commits, the templated-vs-natural ledger (this is GENUINELY NATURAL Wikipedia prose -- contrast with templated CLUTRR), char-length honesty (report actuals; NO doc reaches 3000; do NOT pad/concatenate), present/absent prevalence (split absent by reason), the transitivity-table note (NOT a relation algebra), and located-in-specific caveats (admin-hierarchy ambiguity; multi-parent DAG nodes; country/region granularity; P276 lower precision; closed-world absent on re-docred / DOWNGRADED on docred).

  === OPTIONAL LLM JUDGE (<$2, SKIPPABLE) ===
  Mirror the kinship build: if the deterministic surface-cue check passes ~100%, SKIP the LLM judge ($0). Otherwise, sample atomic edges and ask a cheap OpenRouter model (with SHA-256 response cache) to confirm the support span states the containment; report agreement. Track cumulative spend; never approach $10.

  === FAILURE / FALLBACK SCENARIOS ===
  (F1) If LOC-LOC filtering leaves too few multi-hop present queries (unlikely given P131/P17 density), RELAX by adding P276/P30/P706 LOC-LOC edges and/or lowering the present-query minimum, reporting the relaxation. (F2) If absent siblings explode the file size, tighten absent_cap and/or down-sample sibling pairs while keeping all cross-component pairs (report sampling). (F3) If re-docred located-in coverage is unexpectedly thin in some split, build from ALL splits (train+dev+test) -- splits are recorded in metadata, the experiment slices by them. (F4) NO concatenation/padding to hit 3000 chars under ANY circumstance -- report actual lengths honestly; the natural + absent-relation property is load-bearing, not the length. (F5) There is NO better natural located-in host than Re-DocRED (the iter-5 spatial work already showed symbolic SpaRTUN/RCC-8 corpora are not natural prose; CustFRE is kinship-only); do not search for one -- Re-DocRED IS the host.
target_num_datasets: 2
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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

### [2] HUMAN-USER prompt · 2026-06-18 02:22:28 UTC

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

### [3] SKILL-INPUT — aii-json · 2026-06-18 02:25:50 UTC

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

### [4] SKILL-INPUT — aii-file-size-limit · 2026-06-18 02:39:44 UTC

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

### [5] SYSTEM-USER prompt · 2026-06-18 02:47:28 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/results/out.json`
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
  Natural-Text Absent-Relation Located-In (Administrative Containment) Corpus from Re-DocRED + DocRED
summary: >-
  A SECOND genuinely-natural absent-relation domain (geographic / administrative containment, 'located-in') built from Re-DocRED
  Wikipedia prose, to show the confidence-blindness diagnostic (FACT A + FACT B) is NOT kinship-specific. It is the structural
  twin of the iter-6 natural kinship corpus (art_NUWTxBVWENIJ): same exp_sel_data_out schema (one row per document), same
  drop-in forward-closure engine pattern (kinship.py REUSED VERBATIM with a new degenerate transitive composition table),
  same three strata (atomic located-in edges / present multi-hop transitive-deduction query edges / absent no-containment
  pairs). The composition is the single transitive rule located_in(A,B) AND located_in(B,C) => located_in(A,C) (explicitly
  tagged NOT a relation algebra). Consumed by iter-8's domain-generality confidence-blindness experiment. $0 LLM (deterministic
  cue check; optional <$2 LLM judge, skippable). Compute: cpu_heavy.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  GOAL: a document-level GEOGRAPHIC / ADMINISTRATIVE CONTAINMENT (located-in) corpus over GENUINELY-NATURAL Wikipedia introductory
  prose (no templating, no concatenation, no padding), standardized to the exp_sel_data_out schema (ONE ROW PER DOCUMENT)
  and DROP-IN compatible with the iter-6 kinship engine + the iter-7/iter-8 four-signal battery experiment loaders. Each document
  yields a gold containment graph with: (1) NODES = place / administrative entities with surface form, NER type, and per-mention
  char-offset spans verified against the detokenized text (offset_ok_frac >= ~0.98); (2) ATOMIC located-in EDGES = locally-stated
  containment edges (adjacent-sentence co-occurrence + a surface cue such as 'in / located in / capital of / part of / district
  of / province of'), each flagged locally_justifiable so a span-local reader could plausibly extract it; (3) PRESENT query_edges
  = HELD-OUT multi-hop ancestor pairs with NO direct annotated edge and NO local co-occurrence, derivable >=2-hop by located-in
  transitivity (fields: hop_count, derivation_path, fully_readable, composed_only) -- the deduction-required, NON-CIRCULAR
  present stratum; (4) ABSENT_RELATION_PAIRS = entity pairs with NO containment path in EITHER direction (closed-world within
  the document), spanning two structurally-sound regimes: (a) DIFFERENT connected components (totally unrelated places --
  the clean kinship-analog), and (b) SAME component but no ancestor-descendant path (sibling / cousin places, e.g. two cities
  in one country, neither located in the other -- the containment-specific absent regime, which is the exact 'natural spatial-containment
  absent pairs' the reviewer named). CRITICAL PROPERTY: the absent gold must be TRUSTWORTHY -- this requires Re-DocRED (the
  completeness-corrected re-annotation of DocRED that recovers ~64.6% of triples DocRED missed), because vanilla DocRED false-negatives
  would turn genuinely-contained pairs into SPURIOUS absent pairs. Vanilla DocRED is kept ONLY as a clearly-labelled secondary
  slice whose absent gold is DOWNGRADED (corroborates the atomic/present strata + demonstrates the completeness-correction
  effect). HONESTY: report ACTUAL char lengths (DocRED intros average ~1000 chars; essentially none reach 3000 -- do NOT pad/concatenate;
  the natural-text + absent-relation regime is the load-bearing property, not the 3000-char target), the docred-absent false-negative
  downgrade, and located-in-specific caveats (administrative-hierarchy ambiguity; entities with multiple containers/parents
  = DAG not strict tree; country-vs-region granularity; P276 'location' lower precision). SIZE: geographic relations (P131,
  P17) are among DocRED's MOST FREQUENT, so this corpus should be SUBSTANTIALLY DENSER than the kinship corpus (which yielded
  360 present / 368 absent on re-docred) -- expect many hundreds-to-thousands of atomic edges, hundreds-plus of present multi-hop
  queries, and a large absent set (siblings are abundant); apply per-document caps so no single document dominates. The whole
  build is deterministic ($0 LLM) and must pass a round-trip GATE: the transitive-closure engine reproduces EVERY emitted
  present gold as a singleton and derives EMPTY for EVERY absent pair.
dataset_search_plan: |-
  This corpus is a deterministic TRANSFORMATION of an already-pinned source (Re-DocRED + DocRED) reusing a frozen pipeline; it is NOT an open-ended dataset search. Follow these steps.

  === STEP 0: READ THE FROZEN KINSHIP PIPELINE (the template to mirror) ===
  Direct filesystem-read (do NOT re-download, do NOT wire as a formal dependency -- it is a sibling dataset) the iter-6 kinship corpus workspace at:
    /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/
  Key files to copy/adapt: detok.py (REUSE VERBATIM -- detokenize(sents)->(text,offsets), mention_char_span(offsets,sent_id,pos), sent_char_span(offsets,sent_id)); kinship.py (REUSE VERBATIM as the closure engine -- see STEP 3 for why a new table makes it work unchanged); build.py (ADAPT -- this is the per-document graph builder, the main work); assemble.py + verify.py + probe.py (ADAPT -- corpus assembly, round-trip QA, optional cue probe); clutrr_composition_table.json + README.md (reference for schema/metadata fields). The raw Re-DocRED/DocRED JSON is already cached under that workspace's temp/datasets/ (train_revised.json/dev_revised.json/test_revised.json for re-docred; train_annotated.json/dev.json/rel_info.json for docred) -- you may copy these into your own temp/ to avoid re-download, but re-pin commits per STEP 1.

  === STEP 1: ACQUIRE SOURCES (pin commits) ===
  PRIMARY: tonytan48/Re-DocRED (HuggingFace dataset), commit e0ab3489edfe72c968261bffed5243b6fefddd22, MIT license (Wikipedia text CC BY-SA), arXiv:2205.12696 (Tan et al., EMNLP 2022). Files: train_revised.json (3,053 docs), dev_revised.json (500), test_revised.json (500). SECONDARY (labelled, absent-gold DOWNGRADED): thunlp/docred, commit 7985b4e0371e6c61a756feb41b7b27becf71c666, MIT, arXiv:1906.06127 (Yao et al., ACL 2019). Files: train_annotated.json, dev.json, rel_info.json (the 96-relation id->name map). Each doc = {title, sents (list of tokenized sentences), vertexSet (list of entities; each a list of mentions {name, sent_id, pos:[start,end], type}), labels (list of {h, t, r, evidence})}. Use the aii-hf-datasets skill or direct HF download; verify total size << 300MB.

  === STEP 2: VERIFY & REPORT LOCATED-IN PROPERTY COVERAGE ===
  Confirmed in rel_info.json (already inspected): the located-in / administrative-containment Wikidata properties DocRED annotates are -- P131 'located in the administrative territorial entity', P17 'country', P150 'contains administrative territorial entity', P276 'location', P1376 'capital of', P36 'capital', and (optional, top-level) P30 'continent', P706 'located on terrain feature', P205 'basin country'. CORE VOCABULARY (use these): {P131, P17, P150, P1376, P36}. OPTIONAL/lower-precision (include only with LOC-LOC endpoints + a distinct provenance tag, report counts separately so iter-8 can ablate): {P276, P30, P706}. Web-confirmed: P131 and P17 are among DocRED's MOST FREQUENT relations (geographic relations dominate), so expect high volume. ACTION: compute and report, per slice (re-docred / docred) and per split, the per-property edge counts (LOC-LOC and all-endpoint), the number of family-of-containment-bearing documents, and the resulting atomic-edge / present-query / absent-pair totals -- this is the sizing/power check, analogous to the kinship README's 'Honest stats' table.

  === STEP 3: BUILD THE CONTAINMENT COMPOSITION TABLE (so kinship.py runs UNCHANGED) ===
  Key realization: kinship.py's Kinship class + forward_closure() is a GENERIC finite-composition least-fixpoint UNION engine parameterized entirely by the composition-table JSON (relation_types, symmetric_types, inverse_pairs, composition_rules, surface_forms, label_map). It needs NO code change for located-in. Write containment_composition_table.json with a SINGLE transitive relation plus its converse:
    relation_types: {"located_in": {"symmetric": false, "inverse": "contains"}, "contains": {"symmetric": false, "inverse": "located_in"}}
    symmetric_types: []
    inverse_pairs: {"located_in": "contains"}
    composition_rules: {"located_in": {"located_in": "located_in"}, "contains": {"contains": "contains"}}  // ONLY these two rules; every other composition (e.g. located_in o contains) is UNDEFINED => adds nothing => SOUND
    surface_forms: {"located_in": {"male": "located in", "female": "located in"}, "contains": {"male": "contains", "female": "contains"}}  (gender-trivial; places have no gender)
    surface_reverse / label_map / label_map_reverse: trivial 2-entry maps.
    note (verbatim, load-bearing honesty tag): "DEGENERATE single-relation TRANSITIVE composition table. located_in is a strict partial order (antisymmetric, transitive) over place/administrative entities; 'contains' is its converse. The ONLY defined compositions are located_in o located_in = located_in and contains o contains = contains. This is NOT a relation algebra (no general intersection/converse closure, no disjunctive relations). Emitted verbatim once in metadata.composition_table."
  WHY THIS WORKS (verify, then state in the card): with inverse_pairs set, kinship.py conv_type(located_in)='contains' and conv_type(contains)='located_in'; _seed adds each located_in edge a->b AND its converse contains edge b->a; the fixpoint composes located_in chains downward (descendant->ancestor) and contains chains upward, while located_in o contains is UNDEFINED so NO spurious cross-links appear. Therefore D[(a,b)]={located_in} iff a is a transitive descendant of b; D[(a,b)]={contains} iff a is a transitive ancestor of b; D[(a,b)]=EMPTY for sibling/cousin pairs AND different-component pairs (the absent regime); D[(a,b)] with |.|>1 (i.e. both located_in and contains) only on an annotation CYCLE (a<->b contradiction) -> a Mode-B conflict certificate (report the count).

  === STEP 4: ADAPT build.py (per-document graph builder) ===
  Start from kinship build.py and change ONLY the relation-specific parts; keep the detok/offset/locality/component/caps machinery. Concretely:
  (4a) PROPERTY -> PRIMITIVE + DIRECTION CONVENTION (edge source->target:located_in means 'source is located in target'). For DocRED triple {h, t, r}: P131 -> source=h, target=t (h located_in t); P17 -> source=h, target=t; P276 -> source=h, target=t; P1376 ('h is capital of t') -> source=h, target=t (a capital is located in its territory); P150 ('h contains t') -> INVERT: source=t, target=h; P36 ('h's capital is t') -> INVERT: source=t, target=h. Record the originating wikidata_property on every atomic edge for ablation. DEDUP consistent edges (P131 h->t and P150 t->h collapse to the same located_in(h,t)); if a doc asserts BOTH located_in(a,b) and located_in(b,a) (a true 2-cycle, e.g. P131 and P150 disagreeing), DROP the pair from atomics and log it as a contradiction (also surfaces as a Mode-B conflict if kept).
  (4b) ENTITY-TYPE FILTER: keep only edges whose BOTH endpoints have majority NER type LOC (DocRED types include PER/ORG/LOC/TIME/NUM/MISC). This keeps a pure place-containment graph; report how many edges this drops per property (P131/P17/P150/P1376/P36 are ~always LOC-LOC; P276 is the main one that drops).
  (4c) DROP gender derivation entirely (derive_genders + appositive vote tables) -- not applicable to places. surface word for an edge is just 'located in' / 'contains'. (OPTIONAL, non-load-bearing: a light admin-LEVEL tag {country/region/city/other} from surface cues like 'country','province','state','county','district','city','town','village','capital' for stratification metadata; skip if time-constrained.)
  (4d) SURFACE CUES for locally_justifiable (token-level, lowercased, within the support span): general containment cues {'in','located','situated','within','part','district','province','county','region','municipality','city','town','village','borough','prefecture','county','commune','near'} plus property-specific {P1376/P36: 'capital','capital of'; P150: 'contains','includes','comprises','consists'}. NOTE 'in' is the weak high-frequency workhorse cue (the canonical 'X, a city in Y' Wikipedia pattern) -- require it ALONGSIDE adjacent-sentence co-occurrence (locality) to set locally_justifiable=True, exactly mirroring kinship.
  (4e) ATOMIC EDGES: every kept located_in edge seeds the closure; flag locality (a mention of source and of target within adjacent sentences) + has_cue + locally_justifiable; record support_span (evidence sents if given else closest co-occurrence sents), evidence_sent_ids, wikidata_property. (Expected locally_justifiable_frac similar to or higher than kinship's ~0.62, since 'X in Y' geographic phrasing is dense.)
  (4f) PRESENT query_edges (deduction-required, NON-CIRCULAR): from forward_closure, take directed pairs (a,b) with D[(a,b)]=={'located_in'} singleton, NO direct annotated edge, NO local co-occurrence (min_sent_dist>=2 OR no shared span), BFS hop_count>=2. Fields: source, target, primitive='located_in', relation_type='located_in', is_query=True, hop_count, derivation_path (intermediate container ids), fully_readable (all path edges locally_justifiable), composed_only=True (a transitively-implied containment that is NEVER itself an annotated edge -> provably non-circular, the analog of kinship's grand/uncle types). Deterministic cap present_cap (e.g. 40), shortest-hops-first; set present_truncated flag.
  (4g) ABSENT_RELATION_PAIRS (no-derivation, the headline absent regime): a directed/unordered pair {a,b} of containment-participating entities is ABSENT iff D[(a,b)]==EMPTY AND D[(b,a)]==EMPTY (no containment EITHER direction). Tag reason: 'different_component' (a,b in different undirected components -- the clean kinship-analog) vs 'same_component_sibling' (a,b in the SAME component but no ancestor-descendant path -- e.g. two cities in one country; the containment-specific, reviewer-named regime). Both round-trip to EMPTY under the engine (VERIFY: located_in o contains is UNDEFINED, so siblings derive nothing). Record num_components and, per pair, whether it is same- or cross-component, so iter-8 can stratify. Siblings are combinatorially abundant -> apply a per-document absent_cap (e.g. 30) with STRATIFIED sampling (mix cross-component and sibling pairs; deterministic sort then cap) and set absent_truncated. Closed-world caveat applies (open-world distant containment may exist but is not derivable from the text); TRUSTWORTHY on re-docred, DOWNGRADED on docred.
  (4h) NODES + flat metadata_* exactly mirroring the kinship row schema, swapping kinship-specific fields: metadata_fold = SHA-256(input)%5, metadata_source, metadata_split, metadata_doc_id, metadata_n_entities, metadata_n_loc_entities, metadata_n_atomic_edges, metadata_n_locally_justifiable_edges, metadata_locally_justifiable_frac, metadata_n_components, metadata_present_query_count, metadata_composed_only_present_count, metadata_present_truncated, metadata_absent_pair_count, metadata_absent_different_component_count, metadata_absent_same_component_count, metadata_absent_truncated, metadata_char_len, metadata_n_tokens, metadata_hop_histogram (json), metadata_n_ge_2500_chars, metadata_has_3000_char, metadata_offset_ok_frac, metadata_n_fired_closure, metadata_relation_set (the located-in properties present in the doc). output = json.dumps(gold_graph) with {doc_id, source, split, nodes, atomic_edges, query_edges, absent_relation_pairs, absent_pairs_source='structural_closure'}.

  === STEP 5: CLOSURE / round-trip ===
  Run kinship.py forward_closure(KIN, [{a:source,b:target,type:'located_in'} for atomic edges]) per doc to derive present queries and validate absent emptiness in the same pass build.py already uses for kinship.

  === STEP 6: ADAPT assemble.py ===
  Build full corpus (all docs with >=1 located-in edge), emit the top-level metadata block: name/description/schema, gold_graph_field_spec, composition_table (the containment table verbatim) + composition_table_note (NOT-a-relation-algebra tag), engine_edge_mapping ({a:source,b:target,type:'located_in'}), docred_locatedin_properties map, provenance (both commits, papers, licenses, CLUTRR-free since no kinship table needed here), char_length_distribution (per slice: min/median/mean/max, frac>=2000/2500/3000 -- expect ~0 at 3000), completeness_correction_evidence (located-in edges recovered by re-docred vs docred on shared titles; spurious-absent reduction), build_stats (per slice: n_docs, present_total, absent_total split by reason, composed_only_present, hop_hist, type/property hist, mean_offset_ok, mean_locally_justifiable_frac), qa (cue-present pass rate), plan_corrections, caveats. Write full_data_out.json + mini_data_out.json + preview_data_out.json (use aii-json to generate mini/preview).

  === STEP 7: ROUND-TRIP GATE (adapt verify.py) ===
  For every row: reload gold_graph, feed atomic_edges to forward_closure, assert (i) EVERY present query_edge (source,target) yields D==={'located_in'} (singleton EMIT); (ii) EVERY absent pair yields D[(a,b)]==EMPTY AND D[(b,a)]==EMPTY (ABSTAIN); (iii) report any Mode-B conflicts (|D|>1 from annotation cycles). Print verified counts (e.g. 'NNN/NNN present golds reproduced, MMM/MMM absent pairs empty') and FAIL loudly on any mismatch. This is the same engine the iter-8 battery experiment loads, so passing the gate guarantees drop-in compatibility.

  === STEP 8: VALIDATE + SIZE-SPLIT + CARD ===
  Validate full/mini/preview against the exp_sel_data_out schema via aii-json. Run the aii-file-size-limit procedure; split full_data_out.json if oversized. Write dataset_card.md with: a located-in coverage table (per-property counts per slice), provenance/licenses/commits, the templated-vs-natural ledger (this is GENUINELY NATURAL Wikipedia prose -- contrast with templated CLUTRR), char-length honesty (report actuals; NO doc reaches 3000; do NOT pad/concatenate), present/absent prevalence (split absent by reason), the transitivity-table note (NOT a relation algebra), and located-in-specific caveats (admin-hierarchy ambiguity; multi-parent DAG nodes; country/region granularity; P276 lower precision; closed-world absent on re-docred / DOWNGRADED on docred).

  === OPTIONAL LLM JUDGE (<$2, SKIPPABLE) ===
  Mirror the kinship build: if the deterministic surface-cue check passes ~100%, SKIP the LLM judge ($0). Otherwise, sample atomic edges and ask a cheap OpenRouter model (with SHA-256 response cache) to confirm the support span states the containment; report agreement. Track cumulative spend; never approach $10.

  === FAILURE / FALLBACK SCENARIOS ===
  (F1) If LOC-LOC filtering leaves too few multi-hop present queries (unlikely given P131/P17 density), RELAX by adding P276/P30/P706 LOC-LOC edges and/or lowering the present-query minimum, reporting the relaxation. (F2) If absent siblings explode the file size, tighten absent_cap and/or down-sample sibling pairs while keeping all cross-component pairs (report sampling). (F3) If re-docred located-in coverage is unexpectedly thin in some split, build from ALL splits (train+dev+test) -- splits are recorded in metadata, the experiment slices by them. (F4) NO concatenation/padding to hit 3000 chars under ANY circumstance -- report actual lengths honestly; the natural + absent-relation property is load-bearing, not the length. (F5) There is NO better natural located-in host than Re-DocRED (the iter-5 spatial work already showed symbolic SpaRTUN/RCC-8 corpora are not natural prose; CustFRE is kinship-only); do not search for one -- Re-DocRED IS the host.
target_num_datasets: 2
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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

### [6] SYSTEM-USER prompt · 2026-06-18 02:48:12 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_7/gen_art/gen_art_dataset_1/results/out.json`
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
  Natural-Text Absent-Relation Located-In (Administrative Containment) Corpus from Re-DocRED + DocRED
summary: >-
  A SECOND genuinely-natural absent-relation domain (geographic / administrative containment, 'located-in') built from Re-DocRED
  Wikipedia prose, to show the confidence-blindness diagnostic (FACT A + FACT B) is NOT kinship-specific. It is the structural
  twin of the iter-6 natural kinship corpus (art_NUWTxBVWENIJ): same exp_sel_data_out schema (one row per document), same
  drop-in forward-closure engine pattern (kinship.py REUSED VERBATIM with a new degenerate transitive composition table),
  same three strata (atomic located-in edges / present multi-hop transitive-deduction query edges / absent no-containment
  pairs). The composition is the single transitive rule located_in(A,B) AND located_in(B,C) => located_in(A,C) (explicitly
  tagged NOT a relation algebra). Consumed by iter-8's domain-generality confidence-blindness experiment. $0 LLM (deterministic
  cue check; optional <$2 LLM judge, skippable). Compute: cpu_heavy.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  GOAL: a document-level GEOGRAPHIC / ADMINISTRATIVE CONTAINMENT (located-in) corpus over GENUINELY-NATURAL Wikipedia introductory
  prose (no templating, no concatenation, no padding), standardized to the exp_sel_data_out schema (ONE ROW PER DOCUMENT)
  and DROP-IN compatible with the iter-6 kinship engine + the iter-7/iter-8 four-signal battery experiment loaders. Each document
  yields a gold containment graph with: (1) NODES = place / administrative entities with surface form, NER type, and per-mention
  char-offset spans verified against the detokenized text (offset_ok_frac >= ~0.98); (2) ATOMIC located-in EDGES = locally-stated
  containment edges (adjacent-sentence co-occurrence + a surface cue such as 'in / located in / capital of / part of / district
  of / province of'), each flagged locally_justifiable so a span-local reader could plausibly extract it; (3) PRESENT query_edges
  = HELD-OUT multi-hop ancestor pairs with NO direct annotated edge and NO local co-occurrence, derivable >=2-hop by located-in
  transitivity (fields: hop_count, derivation_path, fully_readable, composed_only) -- the deduction-required, NON-CIRCULAR
  present stratum; (4) ABSENT_RELATION_PAIRS = entity pairs with NO containment path in EITHER direction (closed-world within
  the document), spanning two structurally-sound regimes: (a) DIFFERENT connected components (totally unrelated places --
  the clean kinship-analog), and (b) SAME component but no ancestor-descendant path (sibling / cousin places, e.g. two cities
  in one country, neither located in the other -- the containment-specific absent regime, which is the exact 'natural spatial-containment
  absent pairs' the reviewer named). CRITICAL PROPERTY: the absent gold must be TRUSTWORTHY -- this requires Re-DocRED (the
  completeness-corrected re-annotation of DocRED that recovers ~64.6% of triples DocRED missed), because vanilla DocRED false-negatives
  would turn genuinely-contained pairs into SPURIOUS absent pairs. Vanilla DocRED is kept ONLY as a clearly-labelled secondary
  slice whose absent gold is DOWNGRADED (corroborates the atomic/present strata + demonstrates the completeness-correction
  effect). HONESTY: report ACTUAL char lengths (DocRED intros average ~1000 chars; essentially none reach 3000 -- do NOT pad/concatenate;
  the natural-text + absent-relation regime is the load-bearing property, not the 3000-char target), the docred-absent false-negative
  downgrade, and located-in-specific caveats (administrative-hierarchy ambiguity; entities with multiple containers/parents
  = DAG not strict tree; country-vs-region granularity; P276 'location' lower precision). SIZE: geographic relations (P131,
  P17) are among DocRED's MOST FREQUENT, so this corpus should be SUBSTANTIALLY DENSER than the kinship corpus (which yielded
  360 present / 368 absent on re-docred) -- expect many hundreds-to-thousands of atomic edges, hundreds-plus of present multi-hop
  queries, and a large absent set (siblings are abundant); apply per-document caps so no single document dominates. The whole
  build is deterministic ($0 LLM) and must pass a round-trip GATE: the transitive-closure engine reproduces EVERY emitted
  present gold as a singleton and derives EMPTY for EVERY absent pair.
dataset_search_plan: |-
  This corpus is a deterministic TRANSFORMATION of an already-pinned source (Re-DocRED + DocRED) reusing a frozen pipeline; it is NOT an open-ended dataset search. Follow these steps.

  === STEP 0: READ THE FROZEN KINSHIP PIPELINE (the template to mirror) ===
  Direct filesystem-read (do NOT re-download, do NOT wire as a formal dependency -- it is a sibling dataset) the iter-6 kinship corpus workspace at:
    /ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_6/gen_art/gen_art_dataset_1/
  Key files to copy/adapt: detok.py (REUSE VERBATIM -- detokenize(sents)->(text,offsets), mention_char_span(offsets,sent_id,pos), sent_char_span(offsets,sent_id)); kinship.py (REUSE VERBATIM as the closure engine -- see STEP 3 for why a new table makes it work unchanged); build.py (ADAPT -- this is the per-document graph builder, the main work); assemble.py + verify.py + probe.py (ADAPT -- corpus assembly, round-trip QA, optional cue probe); clutrr_composition_table.json + README.md (reference for schema/metadata fields). The raw Re-DocRED/DocRED JSON is already cached under that workspace's temp/datasets/ (train_revised.json/dev_revised.json/test_revised.json for re-docred; train_annotated.json/dev.json/rel_info.json for docred) -- you may copy these into your own temp/ to avoid re-download, but re-pin commits per STEP 1.

  === STEP 1: ACQUIRE SOURCES (pin commits) ===
  PRIMARY: tonytan48/Re-DocRED (HuggingFace dataset), commit e0ab3489edfe72c968261bffed5243b6fefddd22, MIT license (Wikipedia text CC BY-SA), arXiv:2205.12696 (Tan et al., EMNLP 2022). Files: train_revised.json (3,053 docs), dev_revised.json (500), test_revised.json (500). SECONDARY (labelled, absent-gold DOWNGRADED): thunlp/docred, commit 7985b4e0371e6c61a756feb41b7b27becf71c666, MIT, arXiv:1906.06127 (Yao et al., ACL 2019). Files: train_annotated.json, dev.json, rel_info.json (the 96-relation id->name map). Each doc = {title, sents (list of tokenized sentences), vertexSet (list of entities; each a list of mentions {name, sent_id, pos:[start,end], type}), labels (list of {h, t, r, evidence})}. Use the aii-hf-datasets skill or direct HF download; verify total size << 300MB.

  === STEP 2: VERIFY & REPORT LOCATED-IN PROPERTY COVERAGE ===
  Confirmed in rel_info.json (already inspected): the located-in / administrative-containment Wikidata properties DocRED annotates are -- P131 'located in the administrative territorial entity', P17 'country', P150 'contains administrative territorial entity', P276 'location', P1376 'capital of', P36 'capital', and (optional, top-level) P30 'continent', P706 'located on terrain feature', P205 'basin country'. CORE VOCABULARY (use these): {P131, P17, P150, P1376, P36}. OPTIONAL/lower-precision (include only with LOC-LOC endpoints + a distinct provenance tag, report counts separately so iter-8 can ablate): {P276, P30, P706}. Web-confirmed: P131 and P17 are among DocRED's MOST FREQUENT relations (geographic relations dominate), so expect high volume. ACTION: compute and report, per slice (re-docred / docred) and per split, the per-property edge counts (LOC-LOC and all-endpoint), the number of family-of-containment-bearing documents, and the resulting atomic-edge / present-query / absent-pair totals -- this is the sizing/power check, analogous to the kinship README's 'Honest stats' table.

  === STEP 3: BUILD THE CONTAINMENT COMPOSITION TABLE (so kinship.py runs UNCHANGED) ===
  Key realization: kinship.py's Kinship class + forward_closure() is a GENERIC finite-composition least-fixpoint UNION engine parameterized entirely by the composition-table JSON (relation_types, symmetric_types, inverse_pairs, composition_rules, surface_forms, label_map). It needs NO code change for located-in. Write containment_composition_table.json with a SINGLE transitive relation plus its converse:
    relation_types: {"located_in": {"symmetric": false, "inverse": "contains"}, "contains": {"symmetric": false, "inverse": "located_in"}}
    symmetric_types: []
    inverse_pairs: {"located_in": "contains"}
    composition_rules: {"located_in": {"located_in": "located_in"}, "contains": {"contains": "contains"}}  // ONLY these two rules; every other composition (e.g. located_in o contains) is UNDEFINED => adds nothing => SOUND
    surface_forms: {"located_in": {"male": "located in", "female": "located in"}, "contains": {"male": "contains", "female": "contains"}}  (gender-trivial; places have no gender)
    surface_reverse / label_map / label_map_reverse: trivial 2-entry maps.
    note (verbatim, load-bearing honesty tag): "DEGENERATE single-relation TRANSITIVE composition table. located_in is a strict partial order (antisymmetric, transitive) over place/administrative entities; 'contains' is its converse. The ONLY defined compositions are located_in o located_in = located_in and contains o contains = contains. This is NOT a relation algebra (no general intersection/converse closure, no disjunctive relations). Emitted verbatim once in metadata.composition_table."
  WHY THIS WORKS (verify, then state in the card): with inverse_pairs set, kinship.py conv_type(located_in)='contains' and conv_type(contains)='located_in'; _seed adds each located_in edge a->b AND its converse contains edge b->a; the fixpoint composes located_in chains downward (descendant->ancestor) and contains chains upward, while located_in o contains is UNDEFINED so NO spurious cross-links appear. Therefore D[(a,b)]={located_in} iff a is a transitive descendant of b; D[(a,b)]={contains} iff a is a transitive ancestor of b; D[(a,b)]=EMPTY for sibling/cousin pairs AND different-component pairs (the absent regime); D[(a,b)] with |.|>1 (i.e. both located_in and contains) only on an annotation CYCLE (a<->b contradiction) -> a Mode-B conflict certificate (report the count).

  === STEP 4: ADAPT build.py (per-document graph builder) ===
  Start from kinship build.py and change ONLY the relation-specific parts; keep the detok/offset/locality/component/caps machinery. Concretely:
  (4a) PROPERTY -> PRIMITIVE + DIRECTION CONVENTION (edge source->target:located_in means 'source is located in target'). For DocRED triple {h, t, r}: P131 -> source=h, target=t (h located_in t); P17 -> source=h, target=t; P276 -> source=h, target=t; P1376 ('h is capital of t') -> source=h, target=t (a capital is located in its territory); P150 ('h contains t') -> INVERT: source=t, target=h; P36 ('h's capital is t') -> INVERT: source=t, target=h. Record the originating wikidata_property on every atomic edge for ablation. DEDUP consistent edges (P131 h->t and P150 t->h collapse to the same located_in(h,t)); if a doc asserts BOTH located_in(a,b) and located_in(b,a) (a true 2-cycle, e.g. P131 and P150 disagreeing), DROP the pair from atomics and log it as a contradiction (also surfaces as a Mode-B conflict if kept).
  (4b) ENTITY-TYPE FILTER: keep only edges whose BOTH endpoints have majority NER type LOC (DocRED types include PER/ORG/LOC/TIME/NUM/MISC). This keeps a pure place-containment graph; report how many edges this drops per property (P131/P17/P150/P1376/P36 are ~always LOC-LOC; P276 is the main one that drops).
  (4c) DROP gender derivation entirely (derive_genders + appositive vote tables) -- not applicable to places. surface word for an edge is just 'located in' / 'contains'. (OPTIONAL, non-load-bearing: a light admin-LEVEL tag {country/region/city/other} from surface cues like 'country','province','state','county','district','city','town','village','capital' for stratification metadata; skip if time-constrained.)
  (4d) SURFACE CUES for locally_justifiable (token-level, lowercased, within the support span): general containment cues {'in','located','situated','within','part','district','province','county','region','municipality','city','town','village','borough','prefecture','county','commune','near'} plus property-specific {P1376/P36: 'capital','capital of'; P150: 'contains','includes','comprises','consists'}. NOTE 'in' is the weak high-frequency workhorse cue (the canonical 'X, a city in Y' Wikipedia pattern) -- require it ALONGSIDE adjacent-sentence co-occurrence (locality) to set locally_justifiable=True, exactly mirroring kinship.
  (4e) ATOMIC EDGES: every kept located_in edge seeds the closure; flag locality (a mention of source and of target within adjacent sentences) + has_cue + locally_justifiable; record support_span (evidence sents if given else closest co-occurrence sents), evidence_sent_ids, wikidata_property. (Expected locally_justifiable_frac similar to or higher than kinship's ~0.62, since 'X in Y' geographic phrasing is dense.)
  (4f) PRESENT query_edges (deduction-required, NON-CIRCULAR): from forward_closure, take directed pairs (a,b) with D[(a,b)]=={'located_in'} singleton, NO direct annotated edge, NO local co-occurrence (min_sent_dist>=2 OR no shared span), BFS hop_count>=2. Fields: source, target, primitive='located_in', relation_type='located_in', is_query=True, hop_count, derivation_path (intermediate container ids), fully_readable (all path edges locally_justifiable), composed_only=True (a transitively-implied containment that is NEVER itself an annotated edge -> provably non-circular, the analog of kinship's grand/uncle types). Deterministic cap present_cap (e.g. 40), shortest-hops-first; set present_truncated flag.
  (4g) ABSENT_RELATION_PAIRS (no-derivation, the headline absent regime): a directed/unordered pair {a,b} of containment-participating entities is ABSENT iff D[(a,b)]==EMPTY AND D[(b,a)]==EMPTY (no containment EITHER direction). Tag reason: 'different_component' (a,b in different undirected components -- the clean kinship-analog) vs 'same_component_sibling' (a,b in the SAME component but no ancestor-descendant path -- e.g. two cities in one country; the containment-specific, reviewer-named regime). Both round-trip to EMPTY under the engine (VERIFY: located_in o contains is UNDEFINED, so siblings derive nothing). Record num_components and, per pair, whether it is same- or cross-component, so iter-8 can stratify. Siblings are combinatorially abundant -> apply a per-document absent_cap (e.g. 30) with STRATIFIED sampling (mix cross-component and sibling pairs; deterministic sort then cap) and set absent_truncated. Closed-world caveat applies (open-world distant containment may exist but is not derivable from the text); TRUSTWORTHY on re-docred, DOWNGRADED on docred.
  (4h) NODES + flat metadata_* exactly mirroring the kinship row schema, swapping kinship-specific fields: metadata_fold = SHA-256(input)%5, metadata_source, metadata_split, metadata_doc_id, metadata_n_entities, metadata_n_loc_entities, metadata_n_atomic_edges, metadata_n_locally_justifiable_edges, metadata_locally_justifiable_frac, metadata_n_components, metadata_present_query_count, metadata_composed_only_present_count, metadata_present_truncated, metadata_absent_pair_count, metadata_absent_different_component_count, metadata_absent_same_component_count, metadata_absent_truncated, metadata_char_len, metadata_n_tokens, metadata_hop_histogram (json), metadata_n_ge_2500_chars, metadata_has_3000_char, metadata_offset_ok_frac, metadata_n_fired_closure, metadata_relation_set (the located-in properties present in the doc). output = json.dumps(gold_graph) with {doc_id, source, split, nodes, atomic_edges, query_edges, absent_relation_pairs, absent_pairs_source='structural_closure'}.

  === STEP 5: CLOSURE / round-trip ===
  Run kinship.py forward_closure(KIN, [{a:source,b:target,type:'located_in'} for atomic edges]) per doc to derive present queries and validate absent emptiness in the same pass build.py already uses for kinship.

  === STEP 6: ADAPT assemble.py ===
  Build full corpus (all docs with >=1 located-in edge), emit the top-level metadata block: name/description/schema, gold_graph_field_spec, composition_table (the containment table verbatim) + composition_table_note (NOT-a-relation-algebra tag), engine_edge_mapping ({a:source,b:target,type:'located_in'}), docred_locatedin_properties map, provenance (both commits, papers, licenses, CLUTRR-free since no kinship table needed here), char_length_distribution (per slice: min/median/mean/max, frac>=2000/2500/3000 -- expect ~0 at 3000), completeness_correction_evidence (located-in edges recovered by re-docred vs docred on shared titles; spurious-absent reduction), build_stats (per slice: n_docs, present_total, absent_total split by reason, composed_only_present, hop_hist, type/property hist, mean_offset_ok, mean_locally_justifiable_frac), qa (cue-present pass rate), plan_corrections, caveats. Write full_data_out.json + mini_data_out.json + preview_data_out.json (use aii-json to generate mini/preview).

  === STEP 7: ROUND-TRIP GATE (adapt verify.py) ===
  For every row: reload gold_graph, feed atomic_edges to forward_closure, assert (i) EVERY present query_edge (source,target) yields D==={'located_in'} (singleton EMIT); (ii) EVERY absent pair yields D[(a,b)]==EMPTY AND D[(b,a)]==EMPTY (ABSTAIN); (iii) report any Mode-B conflicts (|D|>1 from annotation cycles). Print verified counts (e.g. 'NNN/NNN present golds reproduced, MMM/MMM absent pairs empty') and FAIL loudly on any mismatch. This is the same engine the iter-8 battery experiment loads, so passing the gate guarantees drop-in compatibility.

  === STEP 8: VALIDATE + SIZE-SPLIT + CARD ===
  Validate full/mini/preview against the exp_sel_data_out schema via aii-json. Run the aii-file-size-limit procedure; split full_data_out.json if oversized. Write dataset_card.md with: a located-in coverage table (per-property counts per slice), provenance/licenses/commits, the templated-vs-natural ledger (this is GENUINELY NATURAL Wikipedia prose -- contrast with templated CLUTRR), char-length honesty (report actuals; NO doc reaches 3000; do NOT pad/concatenate), present/absent prevalence (split absent by reason), the transitivity-table note (NOT a relation algebra), and located-in-specific caveats (admin-hierarchy ambiguity; multi-parent DAG nodes; country/region granularity; P276 lower precision; closed-world absent on re-docred / DOWNGRADED on docred).

  === OPTIONAL LLM JUDGE (<$2, SKIPPABLE) ===
  Mirror the kinship build: if the deterministic surface-cue check passes ~100%, SKIP the LLM judge ($0). Otherwise, sample atomic edges and ask a cheap OpenRouter model (with SHA-256 response cache) to confirm the support span states the containment; report agreement. Track cumulative spend; never approach $10.

  === FAILURE / FALLBACK SCENARIOS ===
  (F1) If LOC-LOC filtering leaves too few multi-hop present queries (unlikely given P131/P17 density), RELAX by adding P276/P30/P706 LOC-LOC edges and/or lowering the present-query minimum, reporting the relaxation. (F2) If absent siblings explode the file size, tighten absent_cap and/or down-sample sibling pairs while keeping all cross-component pairs (report sampling). (F3) If re-docred located-in coverage is unexpectedly thin in some split, build from ALL splits (train+dev+test) -- splits are recorded in metadata, the experiment slices by them. (F4) NO concatenation/padding to hit 3000 chars under ANY circumstance -- report actual lengths honestly; the natural + absent-relation property is load-bearing, not the length. (F5) There is NO better natural located-in host than Re-DocRED (the iter-5 spatial work already showed symbolic SpaRTUN/RCC-8 corpora are not natural prose; CustFRE is kinship-only); do not search for one -- Re-DocRED IS the host.
target_num_datasets: 2
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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
