# Dataset Card — Natural-Text Absent-Relation Located-In (Administrative Containment) Corpus

**ID:** `gen_plan_dataset_1_idx2` (iter-7) · **Schema:** `exp_sel_data_out` (one row per document)
**Compute:** cpu_heavy · **LLM spend:** **$0** (deterministic; cue check passes 100%, LLM judge skipped)
**Consumed by:** iter-8 domain-generality confidence-blindness experiment.

This is the **structural twin** of the natural-kinship corpus (`art_NUWTxBVWENIJ`): a *second*
genuinely-natural absent-relation domain (geographic / administrative containment), built so the
closure-certificate diagnostic can be shown **domain-general**, not kinship-specific. It reuses
the kinship closure engine (`kinship.py`) **verbatim** under a **degenerate single-relation
transitive** composition table.

---

## 1. Located-in property coverage (LOC–LOC edge contributions used in the build)

| Wikidata property | meaning | direction | tier | re-docred | docred |
|---|---|---|---|---:|---:|
| **P131** | located in the administrative territorial entity | `h located_in t` | CORE | 20,497 | 4,795 |
| **P17** | country | `h located_in t` | CORE | 12,260 | 8,206 |
| **P150** | contains administrative territorial entity | invert → `t located_in h` | CORE | 4,614 | 2,528 |
| **P1376** | capital of | `h located_in t` | CORE | 229 | 89 |
| **P36** | capital | invert → `t located_in h` | CORE | 229 | 101 |
| P276 | location | `h located_in t` | OPTIONAL (low-prec) | **0** | 41 |

*(Counts are property→edge contributions; a single deduped edge may be backed by several
properties, e.g. P131+P150. P276 yields **0** LOC–LOC edges on re-docred — the entity-type
filter cleanly removes the lowest-precision property there. P30/P706/P205 are **not used**
(fallback F1 only); CORE is already dense.)*

After LOC–LOC filtering, dedup, and dropping true 2-cycles (44 re-docred / 22 docred), the corpus
has **20,825** atomic located-in edges on re-docred (**11,784** on docred).

---

## 2. Provenance, licenses, commits

| | primary | secondary |
|---|---|---|
| source | `tonytan48/Re-DocRED` (HF dataset) | `thunlp/docred` (HF dataset) |
| commit | `e0ab3489edfe72c968261bffed5243b6fefddd22` | `7985b4e0371e6c61a756feb41b7b27becf71c666` |
| paper | Tan et al. 2022, *Revisiting DocRED*, EMNLP, arXiv:2205.12696 | Yao et al. 2019, *DocRED*, ACL, arXiv:1906.06127 |
| license | MIT (Wikipedia text CC BY-SA) | MIT (Wikipedia text CC BY-SA) |
| files | `train/dev/test_revised.json` (3,053/500/500) | `train_annotated.json`, `dev.json`, `rel_info.json` |
| role | **primary**, trustworthy absent gold | **secondary**, absent gold **downgraded** |

**Composition table:** a degenerate single-relation transitive table authored here
(`containment_composition_table.json`); **no CLUTRR kinship table is used**. The kinship.py
**engine** is reused verbatim. **Text substrate:** detokenized DocRED tokenized `sents`
(Wikipedia introductory prose); per-token char offsets recorded; mention spans verified
(`offset_ok_frac` = 0.988 re-docred / 0.990 docred).

---

## 3. Templated-vs-natural ledger

| property | CLUTRR (prior host) | **this corpus** |
|---|---|---|
| text | **synthesized** from templates over a sampled family graph | **genuine Wikipedia prose** (human-written intros) |
| entities | placeholder names | real places (cities, regions, countries) |
| relation phrasing | fixed template slots | free-form ("a city in …", "the capital of …", "part of …") |
| graph origin | sampler with a known answer | **human relation annotations** (DocRED/Re-DocRED) |
| absent pairs | n/a (single chain) | **structural**: no containment path either way |
| reading difficulty | trivial (surface pattern) | NER + coreference + multi-sentence synthesis |

This corpus is **genuinely natural** prose — the load-bearing contrast with templated CLUTRR.
The relation **gold** is human-annotated (then transitively closed by the sound engine), not
generated.

---

## 4. Char-length honesty (NO padding, NO concatenation)

| slice | n_docs | min | median | mean | max | ≥2000 | ≥2500 | **≥3000** | in[2000,4000] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| re-docred | 2,604 | 554 | 933.5 | 1,024.8 | 2,969 | 1.8% | 0.4% | **0%** | 47 |
| docred | 2,080 | 567 | 926.5 | 1,017.3 | 2,811 | 1.7% | 0.3% | **0%** | 35 |

**No document reaches the 3,000-char target.** We do **not** pad or concatenate — that would
defeat the natural-text purpose. The **natural-text + absent-relation** regime is the
load-bearing property. Per-doc `metadata_char_len`, `metadata_n_ge_2500_chars`,
`metadata_has_3000_char` are flagged for the experiment to slice/select on length.

---

## 5. Present / absent prevalence

| stratum | re-docred | docred | notes |
|---|---:|---:|---|
| **present** total | 3,510 | 1,214 | held-out multi-hop `located_in`, gold certain |
| — `never_annotated` | 118 | 249 | never a direct edge → `composed_only=True`, non-circular |
| — `held_out` | 3,392 | 965 | redundant edge ablated at query time; doubly-certified gold |
| **absent** total | 24,088 | 17,012 | no path either direction (closed-world) |
| — `different_component` | 3,274 | 2,130 | totally unrelated places (clean kinship-analog) |
| — `same_component_sibling` | 20,814 | 14,882 | co-component, no ancestor/descendant (reviewer-named) |

Per-document caps: `present_cap=40`, `absent_cap=30` (stratified, interleaving cross-component
and sibling pairs), `atomic_cap=80` (core-first). `*_truncated` flags mark capped documents.
Hops are almost all 2 (a handful of 3); held-out alternative paths and never-annotated chains
are short because admin hierarchies are shallow in intro prose.

**Completeness correction** (2,079 shared titles): Re-DocRED **19,738** vs DocRED **11,783**
located-in edges (**+67.5%** recovered false negatives); **3,444** vs **1,214** present queries.
Missing edges would turn contained pairs into **spurious absent** and erase present queries —
hence absent gold is trustworthy only on Re-DocRED; the docred slice is downgraded (its inflated
`never_annotated` count is itself a missing-edge symptom).

---

## 6. The transitivity table — NOT a relation algebra

```
located_in o located_in = located_in     contains o contains = contains
located_in o contains   = UNDEFINED       contains o located_in = UNDEFINED
```
`located_in` is a strict partial order (antisymmetric, transitive); `contains` is its converse.
The **only** defined compositions are the two transitive ones; everything else is undefined and
adds nothing (SOUND). There is **no** general intersection/converse closure, **no** disjunctive
relations, **no** point/interval algebra. Consequence (verified): `D[(a,b)]=∅` for sibling and
different-component pairs (siblings derive nothing because `located_in o contains` is undefined),
so the engine **abstains structurally** on absent pairs — never inventing a containment. Emitted
verbatim in `metadata.composition_table` / `metadata.composition_table_note`.

---

## 7. Located-in-specific caveats

- **Admin-hierarchy ambiguity** — administrative (P131) vs by-country (P17) containment are both
  collapsed to `located_in`; the closure unions them.
- **Multi-parent DAG** — an entity may be located in several containers (admin parent *and*
  country); the closure is a partial order over a DAG, not a strict tree. Handled by the union
  fixpoint; reported via `metadata_n_components`.
- **Country-vs-region granularity** is not normalized; `node.admin_level` is a best-effort,
  **non-load-bearing** cue heuristic (it mis-tags some entities — e.g. "Kansas" → city — and is
  for descriptive stratification only).
- **P276** "location" is lower precision (`core_property=False`; ≈0 LOC–LOC on re-docred).
- **Closed-world absent**: defensible on completeness-corrected Re-DocRED; **downgraded** on
  vanilla DocRED (false negatives).
- **`composed_only` is pair-level**, not type-level as in kinship — `located_in` is in DocRED's
  inventory, so non-circularity for held-out queries rests on *withholding the edge + non-locality*,
  not on the relation type being out-of-inventory. Stated plainly so iter-8 does not over-claim.

---

## 8. Round-trip gate (drop-in guarantee)

`verify.py` reloads every row, rebuilds the closure input via the documented
`engine_edge_mapping {a:source, b:target, type:primitive}`, runs `kinship.py` **unchanged**, and
asserts: never_annotated **367/367** EMIT, held_out **4,357/4,357** deduced after ablating the
single direct edge (and that edge is present in `atomic_edges`), absent **41,100/41,100** empty in
**both** directions, every `derivation_path` a valid **directed** `located_in` chain,
cue-present **19,885/19,885**, Mode-B conflicts **0**. Passing the gate guarantees the iter-8
battery experiment (which loads this exact engine) is drop-in compatible.
