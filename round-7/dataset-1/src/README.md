# Natural-Text Absent-Relation Located-In (Administrative Containment) Corpus (Re-DocRED + DocRED)

A document-level **geographic / administrative containment ("located-in")** corpus built from
**genuinely-natural Wikipedia introductory prose** (no templating, no concatenation, no
padding), standardized to the `exp_sel_data_out` schema — **one row per document** — and
**drop-in compatible** with the iter-6 kinship engine: it reuses the *same* forward
least-fixpoint UNION closure engine (`kinship.py`) **verbatim**, parameterized by a
**degenerate single-relation transitive** composition table.

It is the **structural twin** of the natural-kinship corpus (`art_NUWTxBVWENIJ`): a **second
genuinely-natural absent-relation domain**, built to show the closure-certificate
confidence-blindness diagnostic (a system that abstains *structurally* on facts with no
derivation path, regardless of model confidence) is **not kinship-specific**. Consumed by
iter-8's domain-generality experiment. **$0 LLM spend** (deterministic cue check passes 100%).

## Why a degenerate transitive table (the engine runs unchanged)
`kinship.py`'s `forward_closure` is a generic finite-composition least-fixpoint UNION engine,
parameterized entirely by a composition-table JSON. We supply `containment_composition_table.json`:

```
located_in o located_in = located_in     (transitive, descendant -> ancestor)
contains   o contains   = contains       (the converse, ancestor -> descendant)
EVERYTHING ELSE         = UNDEFINED       => adds nothing  (SOUND)
```

With `inverse_pairs={located_in: contains}`, the engine seeds each edge `a located_in b` plus
its converse `b contains a`; the fixpoint composes `located_in` chains downward and `contains`
chains upward, while `located_in o contains` is **undefined**, so **no spurious cross-links**
appear. Therefore:
- `D[(a,b)]={located_in}` ⟺ *a* is a transitive descendant (sub-region) of *b*;
- `D[(a,b)]={contains}`   ⟺ *a* is a transitive ancestor of *b*;
- `D[(a,b)]=∅`            ⟺ **sibling/cousin** places **and different-component** places (the absent regime);
- `|D[(a,b)]|>1`          ⟺ an annotation **cycle** (a Mode-B conflict; **0** in this corpus).

This is **NOT a relation algebra** (no intersection/converse closure, no disjunctive relations).

## Sources & provenance
| slice | source | commit | docs (containment-bearing) | paper | license |
|---|---|---|---|---|---|
| `re-docred` (primary) | `tonytan48/Re-DocRED` | `e0ab3489…` | **2,604** | Tan et al. 2022, EMNLP, arXiv:2205.12696 | MIT (text CC BY-SA) |
| `docred` (secondary) | `thunlp/docred` | `7985b4e0…` | 2,080 | Yao et al. 2019, ACL, arXiv:1906.06127 | MIT (text CC BY-SA) |

The containment primitive comes from the Wikidata properties DocRED annotates (below); **no
CLUTRR kinship table is used** — only the kinship.py **engine** is reused.

## Direction convention (fixed once)
An edge `source → target` with primitive `located_in` means **"source is located in target"**
(source = the sub-region / descendant). DocRED triple `{h, t, r}` ⇒

| property | meaning | edge |
|---|---|---|
| **P131** located in admin. territorial entity | h in t | `h located_in t` |
| **P17** country | h's country t | `h located_in t` |
| **P1376** capital of | h is capital of t | `h located_in t` |
| **P150** contains admin. territorial entity | h contains t | **invert** → `t located_in h` |
| **P36** capital | t is capital of h | **invert** → `t located_in h` |
| P276 location *(lower precision)* | h's location t | `h located_in t` (≈0 LOC-LOC on re-docred) |

Both endpoints must be majority NER type **LOC** (entity-type filter). Consistent edges from
different properties (e.g. P131 `h→t` and P150 `t→h`) **dedup**; true 2-cycles are dropped as
contradictions (44 on re-docred).

## Three strata
1. **Atomic (readable)** — every kept `located_in` edge seeds the closure; flagged
   `locally_justifiable` iff the two mentions co-occur within adjacent sentences **and** a
   surface containment cue (`in / located / district / province / capital / contains / …`) is
   present in the support span. ~**0.59** of edges (re-docred). A span-local reader can extract
   these; the rest are KB-implied (the readability / non-circularity audit).
2. **Present (deduction-required)** — held-out multi-hop `located_in` queries, gold = certain.
   Two honest sub-types (see the **domain-difference note** below):
   - `never_annotated` (118 re-docred): the pair is **never a directly-annotated edge** and is
     non-local → `composed_only=True` (provably non-circular, the strict kinship analog). Rare.
   - `held_out` (3,392 re-docred): a directly-annotated `located_in` edge that is **also
     independently derivable via an alternative ≥2-hop path** (a *redundant* edge) and is
     **non-local**. The consumer **ablates the single edge** before querying; the engine must
     then **deduce** it. Gold is **doubly certified** (annotated *and* derivable). Removing a
     redundant edge **preserves the full transitive closure**, so all absent/other-present gold
     is unchanged.
3. **Absent (no-derivation)** — both entities participate in the `located_in` graph but have
   **no containment path in either direction** (closed-world within the document). Two regimes:
   - `different_component` (3,274 re-docred): totally unrelated places — the clean kinship-analog.
   - `same_component_sibling` (20,814 re-docred): under a common container but neither inside the
     other (e.g. two cities in one country) — the **containment-specific, reviewer-named** regime.

### The present-stratum domain difference (a reportable generality finding)
Unlike kinship — whose composite types (*grandfather/uncle/…*) are **outside DocRED's relation
inventory**, yielding abundant never-annotated present queries — `located_in` is a **single
relation that DocRED annotates near-transitively** (a place's country `P17` is almost always
stated directly). Measured: of ~2,000 derivable singleton `located_in` pairs in a 267-doc
sample, **~1,997 are directly annotated**; only **~9** are never-annotated. Hence the present
stratum is built **primarily from the held-out sub-type**. **The absent regime transfers
cleanly across domains; the present-*derivation* regime is domain-shaped** — itself a finding.

## Drop-in engine usage (iter-8 runs `kinship.py` unchanged)
```python
from kinship import Kinship, forward_closure
KIN = Kinship(full["metadata"]["composition_table"])
gg = json.loads(row["output"])
edges = [{"a": e["source"], "b": e["target"], "type": e["primitive"]} for e in gg["atomic_edges"]]

# never_annotated present  &  absent : run on the FULL edge set
D, nbrs, n_fired = forward_closure(KIN, edges)
#   present  : D[(s,t)] == {"located_in"}     (EMIT)
#   absent   : D[(s,t)] == ∅ and D[(t,s)] == ∅ (ABSTAIN, both directions)

# held_out present : DROP the single (s,t) atomic edge first, then derive
seed_wo = [e for e in edges if (e["a"], e["b"]) != (q["source"], q["target"])]
Dw, _, _ = forward_closure(KIN, seed_wo)        # Dw[(s,t)] == {"located_in"}
```
**Verified round-trip (`verify.py`):** never_annotated **367/367**, held_out **4,357/4,357**
(deduced after ablation), absent **41,100/41,100** empty in both directions, every
`derivation_path` is a valid **directed** `located_in` chain, cue-present **19,885/19,885**,
Mode-B conflicts **0**.

## Honest stats (report actuals, no padding)
| | re-docred | docred |
|---|---|---|
| documents | **2,604** | 2,080 |
| atomic located-in edges | 20,825 | 11,784 |
| present queries (target ≥150) | **3,510** | 1,214 |
| — never_annotated (non-circular) | 118 | 249 |
| — held_out (ablated redundant) | 3,392 | 965 |
| absent pairs (target ≥300) | **24,088** | 17,012 |
| — different_component | 3,274 | 2,130 |
| — same_component_sibling | 20,814 | 14,882 |
| hop histogram | 2:3,508 / 3:2 | 2:1,201 / 3:13 |
| locally-justifiable frac | 0.588 | 0.649 |
| mention offset_ok frac | 0.988 | 0.990 |
| Mode-B / contradiction pairs | 0 / 44 | 0 / 22 |

### Completeness correction (why Re-DocRED is load-bearing)
On the **2,079 shared titles**, Re-DocRED carries **19,738** located-in edges vs DocRED's
**11,783** — **+7,955 (+67.5%)** edges DocRED missed (false negatives) — and derives **3,444**
present queries vs **1,214**. Those missing edges would otherwise (a) turn genuinely-contained
pairs into **spurious absent** pairs and (b) erase derivable present queries. **Only on the
completeness-corrected Re-DocRED slice is "no containment" defensible**; the `docred` slice's
**absent** gold is **downgraded** (kept to corroborate atomic/present strata and to *demonstrate*
this effect — note its inflated `never_annotated` count is itself a symptom of missing edges).

### Char-length honesty
DocRED intro prose averages **~1,025 chars** (median 934, max 2,969); **no** document reaches
3,000 chars and only ~1.8% reach 2,000 (47 docs in [2000,4000], flagged). We do **not**
concatenate or pad. The **natural-text + absent-relation** regime is the load-bearing property,
**not** the 3,000-char target.

## Caveats
- **Absent = closed-world within the document.** Trustworthy on `re-docred`; downgraded on `docred`.
- **`composed_only` is pair-level here** (the pair is never an annotated edge), *not* type-level
  as in kinship (where the relation type is out-of-inventory) — `located_in` is in DocRED's
  inventory. Held-out queries are `composed_only=False` (annotated but withheld + non-local).
- **Multi-parent DAG**: a place may sit in several containers; the closure is a partial order over
  a DAG, handled correctly by the union fixpoint. `admin_level` is best-effort, non-load-bearing.
- **P276** "location" is lower precision (≈0 LOC-LOC on re-docred; 41 edges on docred), tagged
  `core_property=False`. P30/P706/P205 are unused (fallback F1; CORE is already dense).

## Files
- `full_data_out.json` (37 MB) — full corpus (4,684 rows / 2 slices). `mini_/preview_` variants.
- `containment_composition_table.json` — the degenerate transitive table (also in metadata).
- `kinship.py`, `detok.py` — reused **verbatim** from the iter-6 kinship corpus.
- `build.py`, `assemble.py`, `verify.py`, `data.py` — the reproducible pipeline.
- `dataset_card.md` — coverage table, templated-vs-natural ledger, full caveats.
- `temp/datasets/` — raw Re-DocRED/DocRED downloads (**excluded from upload**).

## Reproduce
```bash
python build.py --sources re-docred --max-docs 60   # quick test
python assemble.py                                   # full build + metadata
python verify.py                                     # drop-in engine round-trip gate
```
`uv run data.py` downloads (if needed) + builds + verifies end-to-end. **$0 LLM spend.**
