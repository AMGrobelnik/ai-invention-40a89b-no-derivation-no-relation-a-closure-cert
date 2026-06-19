# Natural-Text Absent-Relation Kinship Corpus (Re-DocRED + DocRED)

A document-level **kinship** corpus built from **genuinely-natural Wikipedia introductory
prose** (no templating, no concatenation), standardized to the `exp_sel_data_out` schema —
**one row per document** — and **drop-in compatible** with the CLUTRR kinship dataset: it
reuses the *same* finite composition table and the *same* forward least-fixpoint UNION
closure engine (`kinship.py`) verbatim.

It is the STEP-B host for iter-7's experiment: *does a closure certificate beat a
confidence-thresholded abstainer on a genuine, natural-text **absent-relation** regime?*
It replaces templated CLUTRR and symbolic-id spatial corpora with real prose.

## Why Re-DocRED (the load-bearing reason)
`tonytan48/Re-DocRED` is the **completeness-corrected** re-annotation of DocRED. Vanilla
DocRED has many **false-negative** relations, which would corrupt "absent = no relation"
gold. Concretely, on the **400 documents shared** by both slices, Re-DocRED carries
**3,087** family edges vs DocRED's **1,716** — recovering **1,371 (+80%)** family edges
DocRED missed. Only with that correction is a within-document "no kinship relation" label
defensible. The vanilla `docred` slice is kept (clearly labelled) to corroborate the
atomic/present strata and to *demonstrate* this effect; its absent gold is **downgraded**.

## Sources & provenance
| slice | source | commit | docs (family-bearing) | paper | license |
|---|---|---|---|---|---|
| `re-docred` (primary) | `tonytan48/Re-DocRED` | `e0ab3489…` | 575 | Tan et al. 2022, arXiv:2205.12696 | MIT (text CC BY-SA) |
| `docred` (secondary) | `thunlp/docred` | `7985b4e0…` | 400 | Yao et al. 2019, ACL, arXiv:1906.06127 | MIT (text CC BY-SA) |

Composition table = CLUTRR (`rules_store.yaml` + `relations_store.yaml`; Sinha et al. 2019,
arXiv:1908.06177), via dependency `art_Dm5vYXmD1R8h`, emitted verbatim once in
`metadata.composition_table`.

## Schema (`exp_sel_data_out`, one row per document)
- `input` = detokenized document text (Wikipedia prose; per-token char offsets recorded).
- `output` = `json.dumps(gold_graph)` where `gold_graph` =
  - `nodes`: `[{entity_id, surface, type, gender, mention_spans:[[char_start,char_end)…], wikidata_qid:null}]`
  - `atomic_edges` (the KB / proof chain): `{source, target, kinship_relation, primitive, relation_type(=primitive), target_gender, is_query:false, hop_count:1, support_span, surface_cue, evidence_sent_ids, locality, has_cue, locally_justifiable, wikidata_property}`
  - `query_edges` (held-out PRESENT, deduction-required): `{source, target, kinship_relation(gold surface|null), primitive(robust gold), relation_type, target_gender, target_int, is_query:true, hop_count(≥2), derivation_path, composed_only, fully_readable}`
  - `absent_relation_pairs`: `{source, target, reason:'different_component', is_absent:true}`
  - `absent_pairs_source: 'structural_components'`
- Flat `metadata_*` columns: `fold` (SHA-256(input)%5), `source`, `split`, `doc_id`,
  `n_entities`, `n_per_entities`, `n_atomic_edges`, `n_locally_justifiable_edges`,
  `locally_justifiable_frac`, `n_family_components`, `present_query_count`,
  `composed_only_present_count`, `absent_pair_count`, `char_len`, `n_tokens`,
  `hop_histogram`, `n_ge_2500_chars`, `has_3000_char`, `offset_ok_frac`, …

### Direction convention (fixed once)
An edge `source → target` with type `primitive` means **"target is source's primitive"**.
DocRED triple `{h, t, r}` ⇒ `source=h, target=t`: P22→`inv-child`(parent, target male),
P25→`inv-child`(target female), P40→`child`, P26→`SO`(symmetric), P3373→`sibling`(symmetric).

### Three strata
1. **Atomic (readable)** — every annotated family edge seeds the closure; each is flagged
   `locally_justifiable` iff the two mentions co-occur within adjacent sentences **and** a
   surface kinship cue (`son/daughter/father/mother/brother/sister/wife/husband/married/…`)
   is present in the support span (≈62% on `re-docred`). A span-local reader can plausibly
   extract these; the rest are KB-implied (the non-circularity / readability audit).
2. **Present (deduction-required)** — pairs with **no** direct annotated edge and **no**
   local co-occurrence, whose ≥2-hop composition yields a unique relation. `composed_only`
   types (`grand/inv-grand/un/inv-un/in-law/inv-in-law/sibling-in-law`) are **outside
   DocRED's relation inventory** ⇒ provably non-circular (never an annotated edge).
3. **Absent (no-derivation)** — both entities are family-participating but lie in
   **different connected components** ⇒ no kinship path. Conservative closed-world label.

## Drop-in engine usage (iter-7 runs `kinship.py` unchanged)
```python
from kinship import Kinship, forward_closure
KIN = Kinship(full["metadata"]["composition_table"])
gg = json.loads(row["output"])
edges = [{"a": e["source"], "b": e["target"], "type": e["primitive"]} for e in gg["atomic_edges"]]
D, nbrs, n_fired = forward_closure(KIN, edges)         # |D[(s,t)]|==1 emit, ==0 abstain (absent), >1 conflict
```
**Verified round-trip:** the engine reproduces **476/476** emitted present-query golds and
derives EMPTY for **577/577** absent pairs (`verify.py`).

## Honest stats (report actuals, no padding)
| | re-docred | docred |
|---|---|---|
| documents | 575 | 400 |
| present multi-hop queries (target ≥150) | **360** | 116 |
| — composed-only (non-circular) | 222 | 74 |
| absent pairs (target ≥300) | **368** | 209 |
| hop histogram | 2:318 / 3:38 / 4:4 | 2:102 / 3:14 |
| locally-justifiable frac | 0.622 | 0.682 |
| mention offset_ok frac | 0.982 | 0.989 |

### Char-length honesty (plan F3)
DocRED intro prose at this annotation density averages **~1,020 chars**; **no**
family-bearing document reaches 3,000 chars and only **~2.6%** reach 2,000 (15 docs in
[2000,4000], flagged via `metadata_n_ge_2500_chars`/`metadata_has_3000_char`). We do **not**
concatenate or pad. The natural-text + absent-relation regime is the load-bearing property,
not the 3,000-char target.

## Plan corrections (verified against the data)
1. **P1038 ('relative') is NOT in DocRED's inventory** (`rel_info.json` has no P1038; 0
   edges). The plan listed it as present; it is unused (so no P1038-exclusion is needed).
2. **DocRED adds 0 family-bearing titles absent from Re-DocRED** (Re-DocRED re-annotates all
   4,052 titles). The secondary slice is therefore vanilla-DocRED annotations on the *same*
   docs — used for corroboration + the completeness-correction demonstration above.
3. **No ready-made natural kinship corpus beat Re-DocRED**: `VLyb/Kinship` is symbolic ids
   (`person100`/`term6`, rejected — non-text); HF `genealogy` hits are tiny (<50 downloads)
   or synthetic. Re-DocRED is the right host.

## Caveats
- **Absent = closed-world within the document** (open-world distant kinship may exist but is
  not derivable from the text). Trustworthy on `re-docred`; downgraded on `docred`.
- **Gender is best-effort** (P22→male / P25→female + reliable appositive cues); when unknown,
  `kinship_relation` is null and the **primitive** is the robust gold (score at primitive level).
- `target_gender`-driven surface words occasionally differ from a perfect rendering; the
  primitive is always correct.

## Files
- `full_data_out.json` (4.5 MB) — full corpus (975 rows across 2 slices). `mini_/preview_` variants.
- `clutrr_composition_table.json` — the finite kinship table (also embedded in metadata).
- `kinship.py` — the closure engine (copied verbatim from iter-5; reused by iter-7).
- `detok.py`, `build.py`, `assemble.py`, `probe.py`, `verify.py` — reproducible pipeline.
- `temp/datasets/` — raw Re-DocRED/DocRED downloads (excluded from upload).

## Reproduce
```bash
.venv/bin/python build.py --sources re-docred --max-docs 30   # quick test
.venv/bin/python assemble.py                                  # full build + metadata
.venv/bin/python verify.py                                    # drop-in engine round-trip QA
```
$0 LLM spend — pure deterministic data construction; the optional LLM cue-judge was skipped
because the deterministic cue check passes 100%.
