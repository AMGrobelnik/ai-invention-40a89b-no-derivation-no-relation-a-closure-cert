# Canonical fold-split gold temporal relation graphs

**Real-text TimeML corpora → schema-validated, document-level gold temporal relation graphs.**

This artifact builds three (+1 optional) frozen, reusable per-document gold temporal relation
graphs that all real-text closure experiments downstream (the T0 envelope go/no-go pilot now;
later T2/T2b/T4 arms) consume. Each row is one `(corpus, document)`: `input` = the document
text, `output` = a JSON gold graph (nodes + edges with canonical relation-algebra sets, locality
metadata and folds). **Only DESCRIPTIVE structural counts are computed here** — the gated
statistics (deduction-required `N*`, bite-after-widening, singleton-resolution) require
composition-table closure / held-out-edge resolution and are the downstream experiment's job.

## Deliverables

| file | contents |
|---|---|
| `data_out.json` | full dataset, top-level `{metadata, datasets}` (schema `exp_sel_data_out`) |
| `full_data_out.json` | identical to `data_out.json` (aii-json full variant) |
| `mini_data_out.json` | first 3 examples per corpus |
| `preview_data_out.json` | mini + strings truncated to 200 chars |
| `descriptive_counts.json` | aggregate + per-document structural descriptors |
| `overlap_table.json` | doc-id overlap across the corpora |
| `common.py`,`builders.py`,`counts.py`,`build_dataset.py` | fully reproducible build pipeline |

Each example: `input` (string, document text), `output` (string, `json.dumps(gold_graph)`),
and `metadata_*` keys (`metadata_corpus`, `metadata_doc_id`, `metadata_fold`, `metadata_n_nodes`,
`metadata_n_edges`, `metadata_n_events`, `metadata_long_distance_edges`, `metadata_descriptive_counts`).
Parse the gold graph with `json.loads(example["output"])`.

### Gold graph schema (`output`)
```
{ doc_id, corpus, fold,
  nodes: [ { node_id, node_type ∈ {event,timex,dct}, surface, char_start, char_end,
             global_token_index, sentence_index, eiid?, tid?, eid?, event_class?,
             nt_event_type?, nt_time?, nt_branch?, nt_start?, nt_end?, pos? } ],
  edges: [ { source, target, native_relation, canonical_algebra,
             canonical_relation_set, coarse_superset_set?, startpoint_relation_set,
             vague_widened, src_sentence_index, tgt_sentence_index, sentence_distance,
             locality_class ∈ {intra,adjacent,long_distance}, structural_deduction_required_proxy,
             locally_justifiable_proxy, edge_fold, phenomena? } ],
  per_doc_descriptive_counts: {...}, warnings: [...] }
```
`structural_deduction_required_proxy` = `sentence_distance ≥ 2`; `locally_justifiable_proxy` =
same/adjacent sentence. These are *structural* proxies (sentence-distance based), not the gated
deduction statistic.

## Corpora

### 1. NarrativeTime (`narrativetime`) — DENSE co-primary headline host
- **Source:** `github.com/text-machine-lab/narrative_time` (Rogers et al., *NarrativeTime: Dense
  Temporal Annotation on a Timeline*, arXiv:1908.11443). A full re-annotation of the 36
  TimeBank-Dense documents on an integer timeline (full TLink coverage; Krippendorff α ≈ 0.68).
- **Relations are derived by the authors' OWN code** (`narrative_time.event_relations` +
  `conversion_utils`), reproducing the shipped `nt_converted_to_tml/a1` TLINKs **exactly**
  (BLOCKING gate: 207,496 TLINK relation-multisets + node counts match across all 36 docs). This
  makes the gold **non-circular** — it is the corpus authors' validated converter, not our
  re-derivation. Annotator **a1**; TimeML refs (eid/eiid/class/DCT) merged from
  `tbd_tml_metadata.jsonl` (the per-annotator file ships refs for only one doc).
- **Coverage:** all unordered pairs over events + timexes + DCT (the corpus's defining
  full-coverage property). Filter by `node_type` for event-event only.
- 36 docs · 1,715 events · 253 timex · 36 DCT · **103,748 edges** (79,001 event-event).
  Event-event informative graph: 53,322 edges, 1,581,149 triangles. `canonical_algebra="interval_allen"`.

### 2. TDDMan (`tddman`) — non-circularity anchor (long-distance)
- **Source:** `github.com/aakanksha19/TDDiscourse`, `TDDMan/` **manual** subset only (NOT
  auto-derived TDDAuto — that would be exactly the circularity we avoid). Text substrate = the
  36 TimeBank-Dense `.tml` (`github.com/muk343/TimeBank-dense`).
- Codes `{b,a,s,i,ii}` → `{before,after,simultaneous,includes,is_included}`.
- **99.9% of pairs are long-distance (≥2 sentences apart)** — manually annotated, provably not
  auto-inferable from local windows: the non-circularity anchor.
- 34 docs · 6,137 gold pairs (all event-event). 107 test pairs carry the TDDiscourse
  *phenomena-required* tags (`edge.phenomena`). `canonical_algebra="coarse_interval"`.

### 3. MATRES (`matres`) — gate-validation control (near-empty deduction envelope)
- **Source:** `github.com/CogComp/MATRES` (Ning et al., ACL 2018) via the preprocessed XML of
  `github.com/qiangning/NeuralTemporalRelation-EMNLP19` (trainset = TimeBank+AQUAINT, 12,740 pairs;
  testset = Platinum, 837 pairs — exact match to the CogComp `.txt`). Real `.tml` text in
  TempEval-3 `TBAQ-cleaned`.
- MATRES annotates event **start-points** ⇒ **point algebra**, naturally convex:
  `BEFORE→{<}`, `AFTER→{>}`, `EQUAL→{=}`, `VAGUE→{<,=,>}` (no non-convex `{<,>}`, so PC-complete).
- **0% long-distance**: every pair is intra (30%) or adjacent (70%) sentence — this is *why* it
  is the control whose deduction-required envelope is near-empty by construction.
- 275 docs · 6,099 events · 13,577 edges. `canonical_algebra="point"`.

### (optional) TimeBank-Dense — NOT emitted
The pipeline can also build a TimeBank-Dense corpus from the muk343 dense gold TLINKs over the
same 36 docs (`builders.build_timebank_dense`, a documented Tier-2 *noisy-read vs clean-read*
arm). Per the deliverable spec the released dataset contains only the **3 named corpora**; the
TimeBank-Dense builder remains available for downstream use but is not in `data_out.json`.

## Canonical relation mappings (sound)

`canonical_relation_set` is the tightest **sound** base-relation set (the true relation is
guaranteed ∈ set); `coarse_superset_set` (when present) is a coarser still-sound alternative;
`startpoint_relation_set` is the convex point-algebra relation over event start-points.

| corpus | native | canonical (Allen / point) | superset | start-point |
|---|---|---|---|---|
| NarrativeTime | BEFORE | `{b,m}` | – | `{<,=}` |
| | AFTER | `{bi,mi}` | – | `{>,=}` |
| | INCLUDES | `{di,si,fi}` | – | `{<,=}` |
| | IS_INCLUDED | `{d,s,f}` | – | `{>,=}` |
| | SIMULTANEOUS | `{eq}` | – | `{=}` |
| | OVERLAP | `{o,oi}` | – | `{<,>}`→widened `{<,=,>}` |
| | VAGUE | all 13 | – | `{<,=,>}` |
| TDDMan | before | `{b}` | `{b,m}` | `{<}` |
| | after | `{bi}` | `{bi,mi}` | `{>}` |
| | simultaneous | `{eq}` | `{eq}` | `{=}` |
| | includes | `{di}` | `{di,si,fi}` | `{<,=}` |
| | is_included | `{d}` | `{d,s,f}` | `{=,>}` |
| MATRES | BEFORE/AFTER/EQUAL/VAGUE | point `{<}/{>}/{=}/{<,=,>}` | – | same |

For NarrativeTime, the start-point set is computed **exactly from the timeline coordinates**
when both events are finite and on the same branch (a convex singleton, no widening); otherwise
the sound mapping is used and the only non-convex set (`{<,>}` from OVERLAP) is widened to
`{<,=,>}` with `vague_widened=true` (124 edges). `nt_start`/`nt_end` store the raw timeline
interval per node.

## Folds
Document-level fold = the TimeBank-Dense **22/5/9** train/dev/test split (NarrativeTime, TDDMan,
TimeBank-Dense). MATRES fold = `train` (TimeBank+AQUAINT) / `test` (Platinum). TDDMan edges also
carry their native per-edge split in `edge_fold`.

## Sentence segmentation
One frozen segmenter is reused across NarrativeTime, TDDMan and TimeBank-Dense: NLTK
`PunktSentenceTokenizer` (pre-trained English; `nltk` version recorded in
`metadata.builder_versions`). MATRES instead uses the **canonical per-token sentence ids** from
the qiangning preprocessing, with `SENTDIFF` as the authoritative sentence distance. Each
corpus's locality flags are therefore internally consistent; cross-corpus comparison is at the
document level (see `overlap_table.json` — **33 docs shared by NarrativeTime, TDDMan and MATRES**).

## Known coverage gaps / caveats
- **TDDMan:** 1 referenced eid is absent from the muk343 `.tml` version
  (`APW19980213.1310/e257`, 13 pairs dropped) — a known annotation-version mismatch; reported in
  `metadata.coverage_gaps`, not silently dropped.
- **MATRES:** 238/6,099 events (3.9%) lack a char offset where the local marker did not align
  with the reconstructed sentence (boundary-detection edge cases); these retain
  `sentence_index` + `global_token_index` and are flagged in `warnings`. Every non-null offset is
  surface-exact by construction (BLOCKING gate). The MATRES `input` text is reconstructed from the
  qiangning tokenized sentences (so node offsets are internally exact); `global_token_index` is
  the corpus's native event index, not a raw character/token position.
- **NarrativeTime** gold uses annotator **a1**; annotator a2 ships separately in the source repo.

## Reproduce
```bash
uv venv .venv --python=3.12 && source .venv/bin/activate
uv pip install loguru networkx lxml beautifulsoup4 nltk numpy pandas tqdm
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
# clone the 6 source repos into temp/datasets/ (see metadata.sources), then:
python build_dataset.py
```
Blocking gates: NarrativeTime reproduces shipped TLINKs exactly; MATRES char offsets are
surface-exact with ≥95% coverage; the closure/composition statistics are intentionally NOT
computed here.

## Citations
- Rogers, Karpinska, Gupta, Lialin, Smelkov, Rumshisky. *NarrativeTime: Dense Temporal Annotation on a Timeline.* arXiv:1908.11443.
- Naik, Breitfeller, Rosé. *TDDiscourse: A Dataset for Discourse-Level Temporal Ordering of Events.* SIGDIAL 2019.
- Ning, Wu, Roth. *A Multi-Axis Annotation Scheme for Event Temporal Relations (MATRES).* ACL 2018.
- Ning, Subramanian, Roth. *An Improved Neural Baseline for Temporal Relation Extraction.* EMNLP 2019 (preprocessed XML).
- Cassidy, McDowell, Chambers, Bethard. *An Annotation Framework for Dense Event Ordering (TimeBank-Dense).* ACL 2014.
- UzZaman et al. *SemEval-2013 Task 1: TempEval-3* (TBAQ-cleaned TimeML text).
