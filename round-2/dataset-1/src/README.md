# CLUTRR kinship gold graphs — the clean end-to-end venue

Per-story gold **kinship relation graphs** over short, professionally-readable family
narratives, standardized from **CLUTRR** (Sinha et al., EMNLP 2019) into the aii
`exp_sel_data_out` schema. This is the third corpus family for the closure-certificate
umbrella, beside the iter-1 temporal corpora (NarrativeTime / TDDMan / MATRES) and the
synthetic-QCN backbone. It is the venue where iter-3 can deliver — in **one setting** —
all four numbers the umbrella names:

1. **atomic-extraction precision/recall** (the directly-stated facts = the typed `edges`);
2. **multi-hop deduction accuracy vs chain length** (held-out `query_edge`, hop 2–10);
3. a **human-auditable trace-graph** (`metadata_gold_proof`, the backward-chaining proof);
4. a **quantified hallucination-rate reduction** on **absent-relation** queries
   (`absent_relation_pairs`: entity pairs in different connected components ⇒ provably
   no kinship path ⇒ honest gold `no-relation`).

> **Boundary.** This artifact is a **dataset**: gold graphs + labels + folds + structural
> descriptors + the static composition table. It reports **descriptive counts only**. It does
> **not** run composition/closure, compute P/R or accuracy, label same-component pairs, or call
> any LLM — those are iter-3's experiment.

## Build / reproduce

```bash
uv run data.py               # the best 2 datasets × 3 splits → 26,676 rows (default)
uv run data.py --include-sup # also build the optional 3rd slice clutrr_sup (+10,601 rows)
uv run data.py --limit 50    # smoke test
```

`data.py` downloads the CSVs directly from the GitHub raw mirror that HF's own
`CLUTRR/v1` loader (`v1.py`) points at — **no `datasets` library, no `trust_remote_code`** —
and the composition tables from `facebookresearch/clutrr`. Deterministic (rows sorted by
`id`; fixed caps; no randomness).

## Delivered slices — THE BEST 2 (same source & composition table, differing roles)

| dataset | HF config | role | rows |
|---|---|---|---|
| `clutrr_gen` | `gen_train234_test2to10` | **core, clean.** Train hops 2-3-4, **test hops 2..10** → the multi-hop accuracy-vs-length curve, atomic-extraction P/R, trace-graph. | 16,131 |
| `clutrr_disc` | `rob_train_disc_23_test_all_23` | **disconnected noise** → genuine within-document **absent-relation pairs** for the hallucination demo (10,244 two-component stories → 71,684 absent pairs). | 10,545 |

These two are the best pair because **together they host all four umbrella numbers in one
venue**: `clutrr_gen` gives atomic-extraction P/R + multi-hop accuracy-vs-length (hop 2..10) +
the trace-graph; `clutrr_disc` gives the absent-relation hallucination demo. `clutrr_disc`'s
**test** split additionally mixes clean / supporting / irrelevant / disconnected noise, so
distractor examples for P/R robustness are already present without a third slice.

**Optional 3rd slice** (off by default; `uv run data.py --include-sup`): `clutrr_sup`
(`rob_train_sup_23_test_all_23`, ~10,601 rows) — supporting-fact distractors, a
distractor-robustness *training* arm for atomic-extraction P/R. It is the plan's explicitly
optional slice, kept reproducible behind a flag so the default delivers exactly **2**
(`target_num_datasets = 2`).

(RuleTaker / ProofWriter / FOLIO were considered and rejected: they are *rule-application*
benchmarks where the rules are given in the text, not *extraction + kinship-composition*, so
they cannot host numbers (i)+(iii) in one venue.)

## Row schema (`exp_sel_data_out`)

Each example is one story:

* **`input`** — the de-bracketed natural-language story (the actually-presented narrative,
  incl. any noise facts; `[` / `]` markers removed).
* **`output`** — `json.dumps(gold_graph)`:
  * `nodes` — `[{entity_id, surface, gender, mention_spans=[[start,end), …] into input}]`
  * `edges` — typed **ATOMIC** story facts (the proof chain): `{source, target,
    kinship_relation (gendered surface, e.g. 'father'), relation_type (abstract, e.g.
    'inv-child'), is_query=false, hop_count=1}`. Directed: *t is source's kinship_relation*
    (triple `(h,r,t)` with `h = source`).
  * `noise_edges` — extra `story_edges` CLUTRR does **not** type (disconnected/distractor
    facts); structural only `{source, target, relation_type=null}` (see *Noise edges* below).
  * `query_edge` — the **held-out** relation (NOT stated; must be deduced by composing ≥2
    atomic edges): `{source, target, kinship_relation=gold, relation_type, target_int,
    is_query=true, hop_count}`.
  * `absent_relation_pairs` — entity pairs in **different connected components** ⇒
    `no-relation` (structural, conservative, sound). Capped at 20/story.
* **`metadata_*`** — `fold` (train/dev/test), `corpus`, `hop_count`, `noise_type`,
  `task_name`, `f_comb`, `query`, `atomic_facts`, **`gold_proof`** (backward-chaining
  decomposition = trace-graph gold), `genders`, `num_entities`, `num_atomic_edges`,
  `num_noise_edges`, `num_components`, `absent_pair_count`, `story_char_len`, `clean_story`.

Top-level `metadata.composition_table` is emitted **once**: the abstract relation **types**
(+inverse/symmetry flags), the `(type × gender) → surface-word` map and its reverse, the
composition rules `rules[t1][t2]=t3`, the int↔text `label_map` (0..20), and a derived
gendered surface-level composition table. **It is a finite composition table, NOT a full
relation algebra** (no general intersection/converse closure; some compositions yield
`no-relation`; ambiguous ones such as `grand ∘ inv-child` are intentionally excluded) — this
tempers any generality claim.

## Reconstruction facts (verified on all 26,676 source rows; 0 violations)

* **`node_id → name`**: `genders` is canonically ordered by node id — verified consistent
  with the backward-chaining proof leaves on every row. (A backtracking proof-edge matcher
  independently agrees on 26,674/26,676; the two disagreements are benign symmetric
  relabelings, and `genders`-order is used as the authoritative source.)
* **atomic `edges`** = `story_edges[:len(edge_types)]` zipped with `edge_types` (the proof
  chain is always the **prefix** — verified 0 violations).
* **`noise_edges`** = `story_edges[len(edge_types):]` (untyped in CLUTRR's released fields).
* **leaves** = `proof_state` sub-triples that are never a goal key (= the atomic facts).

## Noise edges are intentionally left untyped (not fabricated)

In noisy configs `story_edges` contains extra edges (disconnected/supporting/irrelevant
facts) for which CLUTRR's `edge_types` provides **no** relation. A word-before-the-bracket
heuristic recovers the relation only ~54 % of the time **even on the known proof edges**, so
fabricating noise-edge types would inject ≥46 % label noise. We therefore keep `noise_edges`
**structural only** (`relation_type=null`) and use them solely for connectivity (absent-pair
detection). Atomic-extraction P/R in iter-3 should be scoped to the reliable typed `edges`.
This matches the plan's caveat (cf. facebookresearch/clutrr issue #20) and is conservative:
we only ever label *structurally disconnected* pairs as `no-relation`, never a same-component
pair (`absent_pairs_source = "structural_components"`).

## `noise_type` ↔ `task_name` mapping (verified)

`task_<n1>.<n2>`: `n1` = noise regime, `n2` = chain length. Mapping established by
config↔task correspondence — `gen`(clean) train is 100 % `task_1`, `rob_train_sup`
(supporting) train is 100 % `task_2`, `rob_train_disc` (disconnected) train is 100 % `task_4`
⇒ `task_3` is the remaining regime (irrelevant, what `rob_train_irr` trains on). Structural
corroboration: only `task_4` produces 2 components.
`{1: none, 2: supporting, 3: irrelevant, 4: disconnected}`.

## Key descriptive counts (default 2 datasets; see `results/dataset_metadata.json` for the full card)

* **26,676 stories**, 124,819 entity nodes, 78,472 typed atomic edges, 10,545 noise edges.
* Folds: train 20,144 / dev 5,039 / test 1,493.
* Hop-count: 2 (10,235), 3 (10,514), 4 (5,101), 5–10 (826) — the long tail (5–10) lives in
  `clutrr_gen` test, giving the accuracy-vs-length curve.
* **Absent pairs**: 10,244 stories carry ≥1 (all `disconnected`, in `clutrr_disc`),
  **71,684 pairs** total; `clutrr_gen` is single-component so it has 0 (expected).
* **Story length**: min 39 / median 201 / max **871** chars. **Honest caveat:** CLUTRR
  stories are short — **none reach the umbrella's ~3000-char target** (`n_ge_3000_chars = 0`);
  longer documents must come from the temporal corpora. Reported, not hidden.
* `empirical_label_map_matches_canonical = true`; **build flags: `{}`** (0 quality issues:
  0 span mismatches, 0 missing genders, 0 hop disagreements, 0 proof-leaf inconsistencies).

## Provenance & license

* **CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text.** Koustuv Sinha,
  Shagun Sodhani, Jin Dong, Joelle Pineau, William L. Hamilton. **EMNLP 2019** (ACL Anthology
  `D19-1458`), arXiv:**1908.06177**.
* CSV source: `https://github.com/kliang5/CLUTRR_huggingface_dataset` (the raw mirror HF
  `CLUTRR/v1`'s `v1.py` downloads). Composition tables: `facebookresearch/clutrr`
  (`clutrr/store/rules_store.yaml`, `relations_store.yaml`).
* **License**: CLUTRR is released by Facebook under a research / non-commercial license
  (CC-BY-NC-style; see the `facebookresearch/clutrr` LICENSE). **Research use only.**
