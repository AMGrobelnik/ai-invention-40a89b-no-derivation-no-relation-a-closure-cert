# Synthetic QCN Backbone

Controlled, **globally-consistent** Qualitative Constraint Networks (QCNs) over three
relation algebras, with exact gold relations and template natural-language realizations.
This is the *clean-ground-truth backbone* for the redundancy (H4: inverted-U) and
iteration (H3) claims of the Closure-Cert hypothesis — the structural analogue of the
real-text corpora (NarrativeTime / TDDMan / MATRES, delivered by sibling artifacts).
A controlled QCN sweep **cannot be found, only generated**: no real corpus independently
exposes redundancy, hop-count, cyclomatic number, density and node count with exact,
consistent gold.

## Why purely synthetic is correct here

The entire value is *independently controlling* structural parameters that no real corpus
exposes, with ground truth that is **exact and consistent by construction**: every network
is a realizable geometric model (integer points / integer-grid intervals / collinear
integer discs), so the gold atomic relation on each edge is read directly off the model
and the whole scenario is globally consistent — **no constraint solver is needed to certify
consistency**.

## Contents

| Path | What |
|---|---|
| `full_data_out/full_data_out_{1,2}.json` | The full dataset, split into <100 MB parts (concatenate datasets with the same name across parts to reconstruct). 35,100 networks, ~153 MB total. |
| `mini_data_out.json` | 3 examples per algebra (9 total). |
| `preview_data_out.json` | 10 examples per algebra (30 total), strings truncated to 200 chars. |
| `results/dataset_metadata.json` | Full QA / provenance / dataset-card metadata (also embedded in part 1). |
| `method.py`, `qcn/`, `tests/`, `pyproject.toml` | Generator + algebra package + verification suite. |

Schema: every file validates against the aii `exp_sel_data_out` schema.

## Three relation algebras

| algebra | role | base relations | model |
|---|---|---|---|
| `point` (convex Point Algebra) | primary | `< = >` | integer coordinates; gold = `sign(x_i - x_j)`. Non-convex `!=` (`{<,>}`) is **forbidden** in any disjunctive label (path-consistency is complete only on the convex fragment). |
| `allen` (Allen Interval Algebra) | primary | `b bi m mi o oi d di s si f fi eq` | integer-grid intervals `(s,e)`, `s<e`; gold = 13-case endpoint comparison. |
| `rcc8` (Region Connection Calculus) | secondary | `DC EC PO EQ TPP NTPP TPPi NTPPi` | collinear integer discs `(cx,0,r)`; gold via exact `d²` integer comparison (collinear placement realizes internal/external tangency EC/TPP and equality EQ exactly). |

**Composition tables** are loaded from the authoritative `alreich/qualreas` definitions
(bundled in `qcn/algebra_tables/`: `Linear_Point_Algebra.json`,
`Linear_Interval_Algebra.json`, `RCC8_Algebra.json`). They are cross-checked in
`tests/test_qcn.py` by **three independent derivations** — point composition vs. direct
sign reasoning; Allen composition vs. exhaustive endpoint-CSP enumeration (full table
match); RCC-8 reader soundness vs. exhaustive disc-triple enumeration — plus
relation-algebra axioms (identity, converse-distributivity / involution). **All 436 checks
pass.**

## Controlled topology (the design)

The constraint graph **excludes** the held-out query edge `(s,t)`; the query relation
starts universal and is obtainable only by composing ≥1 multi-edge path. `s` and `t` share
no edge and never co-occur in a single verbalized sentence (**deduction-required**).
`mu = E - V + C` (cyclomatic number).

* **Family 1 — generalized THETA**: `P` internally vertex-disjoint `s→t` paths of length
  `L` ⇒ redundancy `P`, hop `L`, `V = P·(L-1)+2`, `mu = P-1`.
* **Family 2 — cyclomatic augmentation**: theta base + chords between intermediates of
  *different* paths (each chord raises `mu` by 1 and creates new `s→t` paths — the
  cross-links that let *iterated* propagation tighten the query beyond one naive pass).
* **Family 3 — random Renz & Nebel A(n,d)**: `G(n, p=d/(n-1))`, query = a far-apart
  non-adjacent pair (edge probability capped just below 1 so a deduction pair always
  exists; realized average degree is recorded).

### Grid (27 structural cells × 3 algebras; ≥500/cell primary, 300/cell secondary)

* Redundancy: `P∈{1,2,3,4,6,8}` at `L=2`, `P∈{1,2,3,4}` at `L=3`
* Hop: `L∈{2,3,4,5}` at `P=2`
* Cyclomatic: target `mu∈{0,1,2,3}` from a `P=2,L=3` base
* Node-count: `small/medium/large` distractor regimes at `P=3,L=3`
* Random: `(n,d) ∈ {8,12}×{3,6,9}`

The intended structural signal is present and clean (see `results/dataset_metadata.json →
cell_summary`): `singleton_resolved` rises monotonically with redundancy `P`
(allen 0.40→0.89), bite decays with hop length, cyclomatic augmentation adds paths, and the
random family spans broad `mu` distributions.

## Row schema

```jsonc
{
  "input":  "<one sentence per non-query edge> ... \nQuery: what is the temporal|spatial relation between <s> and <t>?",
  "output": "{\"edges\":[{\"source\",\"target\",\"relation\"}...],\"query_edge\":{...,\"is_query\":true}}",  // JSON string; canonical GT = gold ATOMIC graph
  "metadata_fold": "pilot|dev|test",            // md5(seed)%100 within every cell: <10 / 10-29 / >=30
  "metadata_algebra": "point|allen|rcc8",
  "metadata_cell": {cell_id, generator_family, redundancy_P, hop_count_L, cyclomatic_target, node_count_regime, n, d},
  "metadata_query": {source, target, relation},
  "metadata_structure": {num_nodes, num_edges, avg_degree, cyclomatic_number, cycle_basis_size,
                          num_simple_paths_s_t, paths_truncated, contributing_edge_count, ...},
  "metadata_paths": {path_list, path_compositions, naive_intersection, has_bite, singleton_resolved},
  "metadata_abstract_graph": {nodes, edges:[[u,v,rel]], query_edge:[s,t]},
  "metadata_reference_disjunctive_labels": [[u,v,[rels]] ...],  // SOUND superset per edge (convenience; convex-only for point)
  "metadata_entity_map": {node_id: phrase},
  "metadata_templates_used": {"u-v": paraphrase_index},
  "metadata_model_embedding": [...],            // aligned to abstract_graph.nodes
  "metadata_seed": int
}
```

The canonical ground truth is the gold **atomic** graph (`output`). `path_compositions` /
`naive_intersection` give the one-pass certificate per network; the recall-controlled
weakening that the experiments need is the *experiment's* job — the
`reference_disjunctive_labels` are only a convenience.

## Correctness gate (asserted on every network)

For every enumerated `s→t` path, the composition (via the authoritative tables) of the
gold atomic relations along it **must contain** the gold query relation. This holds for any
realizable scenario; a violation would mean a buggy table or reader and fails loudly. **All
35,100 networks passed.**

## Pre-registered realism thresholds (recorded, `validated=false`)

`results/dataset_metadata.json → realism_preregistration`: per-edge error-type TV-distance
≤ 0.15, cross-edge error-correlation ρ match ≤ 0.10, topology-histogram EMD ≤ 0.10 — fixed
now to inoculate against post-hoc tuning, to be checked **next iteration** against the real
frontier-pilot error distributions.

## Reproduce

```bash
uv venv .venv --python=3.12 && uv pip install --python .venv/bin/python numpy networkx loguru
.venv/bin/python tests/test_qcn.py    # 436 checks, must pass
uv run data.py                        # entry point: builds the full corpus (== method.py at full scale)
# or, equivalently:
.venv/bin/python method.py --networks-primary 500 --networks-secondary 300 --tag full
```

`data.py` is the build entry point. Because this dataset is **synthetic**, there is nothing
to load from `temp/datasets/`; `data.py` runs the generator (`qcn/` + `method.py`) and emits
the schema-valid rows directly.

Generation is fully deterministic and resumable: per-`(algebra, cell, index)` md5 seeds,
independent of per-cell counts (changing `--networks-*` does not perturb existing networks).
~35k networks in ~18 s on 4 cores.
