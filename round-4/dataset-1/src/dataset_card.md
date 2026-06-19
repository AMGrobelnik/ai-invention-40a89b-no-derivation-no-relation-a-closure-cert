# SPATIAL multi-path-redundant gold-QCN corpus

**Artifact:** `gen_art_dataset_1` (run `run_IuSkWzF0As-P`, invention-loop iter-4)
**Purpose:** an **a-priori, descriptive** multi-path-redundancy *prevalence gate* that tells iter-5,
**before any LLM spend**, whether published spatial-reasoning corpora structurally HOST the paper's
signature-but-still-synthetic-only mechanism — query pairs reachable via **≥2 edge-disjoint constraining
paths** whose single-path compositions leave disjunctions that *cross-path intersection* narrows. This is
the **spatial analog of the temporal a-priori N\* gate** (dossier `art_aQ2Rf8rwqteI`).

**Strictly $0, no LLM, descriptive-only.** No closure, no derived precision/recall. The metrics below are
**structural annotations of the data** (like StepGame's existing `k_hop` field), not experimental results.

**BEST-4 standardized corpora** (the four qualitatively distinct text-type × structure regimes the gate must
characterize): **`SpaRP-PS1`** (dense-templated, high redundancy) · **`SpartQA-Human`** (semi-natural, modest) ·
**`StepGame-clean`** (single-chain, zero-by-construction) · **`ReSQ`** (genuinely-natural anchor, no recoverable
graph). **Evaluated extras** (also in the file, for the ledger): `SpaRP-PS2`, `SpartQA-Auto`. All 6 carry the full
prevalence annotation.

---

## 1. What is in the corpus

One row per **(scene, held-out query)**. Each row reconstructs a **gold relation-graph** from a published
spatial-QA item and annotates the structural multi-path redundancy of one query pair.

Stored in the `exp_sel_data_out` schema:
- `input` — the full story/scene text.
- `output` — JSON `{nodes, edges, query_edge}` (the gold graph; see below).
- `metadata_*` — provenance + the structural metrics surfaced as flat fields.

`output.nodes[i]` = `{node_id, surface, char_spans, mention_count, node_type}`.
`output.edges[i]` = `{src, dst, native_relation, algebra ∈ {rcc8, cardinal_direction, mixed}, canonical,
subtypes, is_root_edge, src_span, rel_span, dst_span}` — every **stated** relation an honest local reader
would extract (the KB edges).
`output.query_edge` = `{src, dst, gold_native_relation, gold_canonical, gold_algebra, answer_kind,
query_kind, gold_recoverable, is_universal_option, dataset_num_hop, hop_length, num_edge_disjoint_paths,
num_edge_disjoint_paths_with_root, num_disjoint_paths_len_ge2, disjoint_path_lengths, second_path_length,
cyclomatic_number, deduction_required, genuine_multipath_with_bite, genuine_multipath_with_bite_tight}`.

The query edge is **held-out / universal** (`is_universal_option: true`): the high-recall LLM-read
disjunction is produced later by the iter-5 EXPERIMENT, not here. `canonical` here holds the **gold** atomic
relation(s) (singleton/small for designed queries; not-derived for enumerated SpartQA pairs — see §6).

### Structural metric definitions (computed with `networkx`)
- `hop_length` — shortest-path length (#edges) between the query endpoints on the undirected projection of the stated edges.
- `num_edge_disjoint_paths` — max number of edge-disjoint paths (Menger / max-flow).
- `cyclomatic_number μ` — `E − V + C` on the subgraph induced by the union of those edge-disjoint paths.
- `deduction_required` — the query pair is **not** a directly-stated edge.
- `genuine_multipath_with_bite` — `deduction_required AND ≥2 edge-disjoint paths each of length ≥2`. **The spatial N\* analog.**
- `genuine_multipath_with_bite_tight` — additionally requires **≥2 of those disjoint paths to be SHORT (length ≤4)**. A long cardinal-composition path tends to compose toward the *universal* relation (no narrowing), so the tight variant is the *deductively meaningful* redundancy. **Read this one for go/no-go.**

> **Root-node handling.** The world/image-container node (SpaRP/SpaRTUN id `-1`, "object X is inside the
> image") is **excluded from the primary structural graph**: it is a near-universal containment relation that
> composes to the universal relation (no deductive bite) and would only spuriously inflate redundancy. Root
> containment edges are **kept in `output.edges`** (flagged `is_root_edge: true`) and a root-included
> disjoint-path count is reported (`num_edge_disjoint_paths_with_root`) for transparency.

---

## 2. CRUCIAL DELIVERABLE — multi-path-redundancy prevalence table

Prevalence is computed on the **FULL processed population** per corpus (not just the emitted subsample).
Headline fraction denominator = **deduction-required queries**. Applicability bands (pre-stated, matching the
hypothesis): **≥10% = general · 5–10% = useful module · <5% = niche.**

| Corpus | text | #scenes | #queries | %ded. | %≥2 disjoint | **%bite** | band (bite) | **%bite-TIGHT** | band (tight) | mean hop | mean μ | %hop≥3∨cyclic |
|---|---|--:|--:|--:|--:|--:|---|--:|---|--:|--:|--:|
| **SpaRP-PS1 (SpaRTUN)** | templated | 2 316 | 2 316 | 49.8 | 55.9 | **27.4** | **general** | **27.4** | **general** | 1.67 | 0.81 | 71.8 |
| SpaRP-PS2 (StepGame-Ext) | templated | 15 000 | 15 000 | 59.5 | 13.3 | 10.4 | general | **0.9** | niche | 2.46 | 0.13 | 47.9 |
| **SpartQA-Human** | **semi-natural** | 68 | 3 613 | 100 | 5.3 | **5.3** | **useful module** | 4.5 | niche* | 3.66 | 0.08 | 77.1 |
| SpartQA-Auto | templated | 3 148 | 68 365 | 100 | 3.5 | 3.5 | niche | 3.5 | niche | 2.71 | 0.05 | 62.1 |
| StepGame-clean | templated | 2 500 | 2 500 | 43.4 | 0.0 | **0.0** | niche | 0.0 | niche | 1.69 | 0.00 | 18.1 |
| ReSQ | natural | 499 | 1 951 | 100 | 0.0 | **0.0** | niche | 0.0 | niche | n/a | 0.00 | 0.0 |

\* SpartQA-Human is right at the 5%/4.5% band boundary.

### Go/no-go reading for iter-5
1. **SpaRP-PS1 (SpaRTUN) is the high-redundancy synthetic-but-realistic-text venue.** 27.4% of deduction-required
   queries are genuine multi-path *with tight bite* (general band, and **all** its bite is tight). Within/across
   block object pairs are connected by ≥2 short edge-disjoint constraining paths over an **RCC-8 + directional**
   graph the engine already validates for RCC-8. **This is the recommended primary real-venue arm.**
2. **Semi-natural human text hosts *some* genuine redundancy.** SpartQA-Human reaches the useful-module band on
   raw bite (5.3%) and sits at the niche/useful boundary on tight bite (4.5%). Natural multi-path redundancy is
   **rare but non-zero** in human-authored spatial descriptions.
3. **The "redundancy" of StepGame-Ext is mostly an artifact of LONG loose paths.** SpaRP-PS2 shows 10.4% raw bite
   but only **0.9%** tight bite: its second disjoint path is typically very long (a tour around the whole chain),
   which composes toward the universal cardinal relation and does not narrow. This vindicates the plan's
   instruction to **verify redundancy empirically rather than trust noise-type labels.**
4. **Single-chain and natural-QA corpora are the scope boundary.** StepGame-clean (single linear chain by
   construction) and ReSQ (no recoverable scene graph; see §6) host **zero** recoverable multi-path redundancy.

**Bottom line:** genuine, *tight*, deductively-meaningful spatial multi-path redundancy is **abundant only in the
dense templated SpaRTUN/SpaRP-PS1 graphs**, **modest in semi-natural SpartQA-Human**, and **absent in single-chain
StepGame and natural ReSQ**. Iter-5's cross-path-intersection mechanism therefore has a strong synthetic-but-realistic
venue (SpaRP-PS1) and a thin-but-real natural-ish venue (SpartQA-Human); it remains scoped away from single-chain and
unannotated-natural text.

---

## 3. Provenance, licenses, commits

| Corpus | source | license | acquisition |
|---|---|---|---|
| SpaRP-PS1 / PS2 | HF `UKPLab/sparp`, configs `SpaRP-PS1 (SpaRTUN)` / `SpaRP-PS2 (StepGame)`, split `test` | CC-BY-SA-4.0 (code Apache-2.0); repo `github.com/UKPLab/acl2024-sparc-and-sparp` | `aii-hf-datasets` download |
| SpaRTUN (raw) | `github.com/HLR/SpaRTUN` @ `ab924d2` | MIT | git clone (cross-check / NLVR scene graphs) |
| SpartQA-Auto | `cse.msu.edu/~kordjams/data/SpartQA_Auto.zip` (`annotation_{train,dev,test}.json`) | MIT (`github.com/HLR/SpartQA_generation` @ `9892ed1`) | direct download |
| SpartQA-Human | `cse.msu.edu/~kordjams/data/SpartQA_Human.zip` (`human_{split}_annotation.json`) | MIT | direct download |
| StepGame-clean | HF `michaelszx/StepGame`, split `train` (TrainVersion, k=1..5, no noise) | research-use (CC-BY-4.0 per HF card) | `aii-hf-datasets` download |
| ReSQ | `cse.msu.edu/~kordjams/data/ReSQ.zip` (built on mSpRL) | research-use (HLR/MSU release) | direct download |

**SpaRP** = Mirzaee & Kordjamshidi, ACL 2024 (Spatial Reasoning Path). **SpaRTUN/SpartQA** = Mirzaee &
Kordjamshidi EMNLP 2022 / Mirzaee et al. NAACL 2021. **StepGame** = Shi et al. AAAI 2022. **ReSQ** = HLR group
(real-image mSpRL descriptions + human YN questions).

### Reconstruction method per corpus
- **SpaRP-PS1/PS2**: `symbolic_context` gives the stated KB edges **directly** (`"A-->B": [relations]`); entity ids:
  integer = block, `AxB` = object B in block A, `-1` = world root. Query = `symbolic_question` pair, gold = `targets`,
  `dataset_num_hop` = `num_hop`. **No NL parsing needed.**
- **SpartQA-Auto**: from the block-format annotation (`relations_between_blocks`, per-block `relations_between_objects`,
  `rel_with_block`) with char offsets (`SOT_text`).
- **SpartQA-Human**: from the per-sentence SpRL-triple annotation (`spatial_description`: trajector/landmark
  `entity_id`, `spatial_value`, `s_type`, char offsets). 1 negative ("not …") relation excluded from the positive
  constraint graph.
- **StepGame-clean**: structural graph from single-letter agents co-stated in each sentence (clean stories are single
  linear chains: `#sentences == k_hop`). Query parsed from "agent X to the agent K"; gold = `label`.
- **ReSQ**: natural stories + YN questions; **no reusable scene-graph triples** in the release → see §6.

---

## 4. Templated-vs-natural ledger & document length vs the 3000-char target

| Corpus | is_templated | is_natural_text | char-spans recoverable | gold recoverable | query_kind | mean / median / max chars |
|---|---|---|---|---|---|---|
| SpaRP-PS1 | ✓ | ✗ | ✗ (symbolic ids) | ✓ (`targets`) | designed | 472 / 464 / 1170 |
| SpaRP-PS2 | ✓ | ✗ | ✗ (symbolic ids) | ✓ (`targets`) | designed | 472 / 489 / 1191 |
| SpartQA-Auto | ✓ | ✗ | ✓ (SOT offsets) | ✗ (enumerated) | enumerated deduction pair | 536 / 503 / 1338 |
| SpartQA-Human | ✗ | ✓ | ✓ (SOT offsets) | ✗ (enumerated) | enumerated deduction pair | 563 / 569 / 950 |
| StepGame-clean | ✓ | ✗ | ✓ (single letters) | ✓ (`label`) | designed | 130 / 127 / 347 |
| ReSQ | ✗ | ✓ | ✗ | ✗ (YN only) | natural YN | 184 / 170 / 693 |

**Document length caveat (honest).** **Every** spatial corpus falls far short of the project's ~3000-char target
(`frac_reaching_3000_char_target = 0.0` for all). Spatial scenes are short (130–1338 chars; max 1338 in SpartQA-Auto).
Iter-5 should treat document length as a known limitation of spatial venues — concatenation or multi-scene packing
would be needed to approach 3000 chars.

---

## 5. Per-algebra relation-vocabulary coverage

Native relations are split into two calculi: **rcc8** (mereotopological — engine-validated, usable for closure in
iter-5) and **cardinal_direction** (directional / distance / depth — the engine does **not** yet implement CDC; the
vocabulary is recorded for next-iter engine extension). `mixed` = an edge carrying both (e.g. SpaRP `below, dc, front`).

| Corpus | #edges | rcc8 | cardinal_direction | mixed | unmapped |
|---|--:|--:|--:|--:|--:|
| SpaRP-PS1 | 24 648 | 17 078 | 6 500 | 1 070 | 0 |
| SpaRP-PS2 | 161 979 | 0 | 161 979 | 0 | 0 |
| SpartQA-Auto | 35 777 | 18 340 | 17 362 | 75 | 0 |
| SpartQA-Human | 1 185 | 441 | 744 | 0 | 0 |
| StepGame-clean | 7 457 | 0 | 7 457 | 0 | 0 |

- **RCC-8 tokens used** (engine-ready): `in/ntpp, ntppi, touching-the-*-edge-of/tpp, tppi, ec, dc, po, touching`. (No `EQ` observed.)
- **Cardinal-direction tokens**: `below(S), above(N), right(E), left(W)` + StepGame diagonals `NE/NW/SE/SW`.
- **Distance tokens** (recorded under CDC family, *not* a direction): `near/near to, far/far from`.
- **Depth tokens — OUT OF STANDARD 2-D CDC** (flagged): `front, behind` (3-D, not in standard cardinal-direction calculus).
- **Unmapped: 0** across all corpora after mapping (the "touching the {left,right,top,bottom} edge of" phrasings map to TPP).
- **StepGame tokeniser coverage**: 7 101 / 7 457 edges (95.2%) got a best-effort cardinal canonical; 356 keep only the raw
  sentence. StepGame uses ~100 crowdsourced paraphrase templates (incl. clock positions), so its edge relation is stored as
  the **raw sentence** in `native_relation` with a best-effort `canonical`; this does not affect the structural finding
  (StepGame is the single-chain contrast, bite = 0 regardless of relation).

**Engine-extension priority signal:** SpaRP-PS2 and StepGame multi-path bite lives **entirely in the not-yet-supported
cardinal-direction algebra**; SpaRP-PS1's bite spans **RCC-8 + directional**. The RCC-8 portion of SpaRP-PS1 is
immediately usable by the iter-5 engine; full exploitation of PS1/PS2/SpartQA directional bite requires the CDC engine
extension.

---

## 6. Honest caveats (read before using)

1. **ReSQ ships NO reusable scene-graph triples.** The public release gives natural stories + YN questions only; a gold
   stated-relation graph is **not recoverable without an LLM** (out of scope, $0). ReSQ rows therefore carry an **empty
   stated graph** (`metadata_stated_graph_recoverable = false`), one query per YN question (relation + yes/no), and
   `genuine_multipath_with_bite = false` by construction. This is the **honest natural-text scope boundary**, not a bug:
   natural spatial descriptions do not expose reusable multi-object relation graphs.
2. **SpartQA queries are ENUMERATED, not the dataset's FR questions.** SpartQA FR questions reference objects by long
   compositional descriptions ("the blue object that is above a blue thing touching the bottom edge of a block") that
   cannot be resolved to annotation ids without an LLM. We instead enumerate **all connected, not-directly-stated node
   pairs** = the deduction-required query population (`query_kind = enumerated_deduction_pair`, `gold_recoverable = false`).
   This is a well-defined **structural-capacity** measure; gold relations for these pairs are not derived (that would need
   closure). SpaRP and StepGame use the dataset's **designed** query with gold.
3. **StepGame-clean has no multi-path by construction** (single linear k-hop chain). It is included only as the contrast arm.
4. **SpaRP/SpaRTUN are templated**, not natural language; SpartQA-Human is the genuinely human-authored arm.
5. **front/behind is out-of-standard-2-D-CDC** (3-D depth) — recorded but flagged.
6. **YN queries (ReSQ) give a pair+label, not always a clean FR gold relation.**
7. **`networkx.edge_disjoint_paths` returns A maximal edge-disjoint set via max-flow** (shorter augmenting paths first but
   **not provably length-minimal**). So `disjoint_path_lengths` / `second_path_length` are a near-tight upper bound on the
   tightest redundancy; the `*_tight` flag (≥2 disjoint paths of length ≤4) is consequently a **lower bound** on tight
   redundancy. This conservative bias understates rather than inflates bite.
8. **Char-offset spans** are emitted only where the source provides them (SpartQA `SOT_text`; StepGame single-letter agents
   by exact search). SpaRP exposes **symbolic entity ids** (no reliable surface→offset map) → `char_spans = []`,
   `metadata_char_spans_recoverable = false`. **No offsets were fabricated.**

### Subsampling & emission (full prevalence is on the full population; emission is a subsample)
- **SpaRP-PS2** prevalence computed on a deterministic **stride sample of 15 000 / 99 299** test rows (spanning all hop
  levels — head-sampling would bias toward k=1 direct edges and *understate* multi-hop; the stride fixed this, raising raw
  bite from 0.0 to 10.4%).
- **SpartQA-Auto** prevalence on **68 365** enumerated deduction pairs from 3 148 scenes (train/dev capped to 600 scenes each
  + full test 1 948).
- **All 6 corpora are EVALUATED** for the prevalence table; **only the 4 STANDARDIZED corpora are EMITTED** into
  `datasets[]` (`SpaRP-PS1`, `SpartQA-Human`, `StepGame-clean`, `ReSQ`). `SpaRP-PS2` / `SpartQA-Auto` are evaluated
  extras (prevalence row only, role `evaluated_extra`, NOT emitted).
- **Emission is stratified**: **all** `genuine_multipath_with_bite` rows are kept (the rows iter-5 needs to run the
  cross-path test on) + a deterministic stride sample of the rest, capped per corpus. Emitted: SpaRP-PS1 2 316,
  SpartQA-Human 1 600, StepGame-clean 1 500, ReSQ 1 951 = **7 367 rows** (507 with bite = 316 SpaRP-PS1 + 191 SpartQA-Human).
  Full `full_data_out.json` ≈ 40 MB (< 100 MB → not split). `mini_data_out.json` = 3 rows/corpus; `preview_data_out.json`
  = 10 rows/corpus (strings truncated).

---

## 7. Files & reproduction
- `data.py` — end-to-end pipeline (acquire → reconstruct → multi-path annotate → schema emit). Deterministic, `$0`, no LLM.
  `src/algebra.py` (relation→algebra map), `src/loaders.py` (per-corpus loaders), `src/graphmetrics.py` (networkx metrics),
  `src/make_variants.py` (mini/preview).
- `full_data_out.json` (full, schema `exp_sel_data_out`) + `mini_data_out.json` + `preview_data_out.json` + `analysis_out.json`
  (full prevalence table + relation-vocab ledger).
- Reproduce: `uv run data.py` then `uv run python src/make_variants.py` (raw downloads cached under `temp/`, listed in upload-ignore).
