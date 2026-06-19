"""Synthetic QCN Backbone generator.

Builds controlled, globally-consistent qualitative constraint networks over three
relation algebras (convex Point, Allen Interval, RCC-8) with model-based exact gold,
controlled query topology (redundancy / hop / cyclomatic / node-count / random A(n,d)),
and template NL realizations.  Emits an aii ``exp_sel_data_out`` dataset.

Run a pilot then the full corpus:
    .venv/bin/python method.py --networks-primary 5  --networks-secondary 5  --tag pilot
    .venv/bin/python method.py --networks-primary 500 --networks-secondary 300 --tag full
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from itertools import islice
from pathlib import Path

import networkx as nx
import numpy as np
from loguru import logger

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from qcn.algebras import load_algebras, convex_supersets_of  # noqa: E402
from qcn.realize import realize, relation, planted_pair  # noqa: E402
from qcn import topology  # noqa: E402
from qcn import verbalize  # noqa: E402

# ------------------------------------------------------------------------------- config
PATH_CAP = 64                 # max enumerated s-t paths per network
LEN_CUTOFF = 8                # max simple-path length explored
PRIMARY = ("point", "allen")  # full grid, 500/cell
SECONDARY = ("rcc8",)         # 300/cell
REF_LABEL_L = {"point": None, "allen": 6.5, "rcc8": 4.0}  # avg disjunctive-label size

REALISM_PREREG = {
    "validated": False,
    "note": ("Pre-registered realism-matching thresholds, fixed now to inoculate "
             "against post-hoc tuning. To be checked NEXT iteration against the real "
             "frontier-pilot (NarrativeTime/TDDMan/MATRES) error distributions."),
    "tv_distance_max": 0.15,          # per-edge error-type distribution (TV distance)
    "rho_match_tol": 0.10,            # cross-edge error-correlation rho match tolerance
    "topology_histogram_emd_max": 0.10,  # contributing-edge-count + cycle-structure EMD
}

ALG = load_algebras()


# ----------------------------------------------------------------------------- the grid
def build_grid():
    """Return {algebra: [cell, ...]}. Same 27 structural cells per algebra."""
    cells = []
    # (i) REDUNDANCY sweep (Family 1 theta)
    for P in (1, 2, 3, 4, 6, 8):
        cells.append(dict(cell_id=f"red_P{P}_L2", family="theta", P=P, L=2))
    for P in (1, 2, 3, 4):
        cells.append(dict(cell_id=f"red_P{P}_L3", family="theta", P=P, L=3))
    # (ii) HOP sweep (Family 1 theta) at P=2
    for L in (2, 3, 4, 5):
        cells.append(dict(cell_id=f"hop_L{L}_P2", family="theta", P=2, L=L))
    # (iii) CYCLOMATIC sweep (Family 2) from a P=2,L=3 base
    for mu in (0, 1, 2, 3):
        cells.append(dict(cell_id=f"cyc_mu{mu}", family="cyclo_aug", P=2, L=3,
                          cyclomatic_target=mu))
    # (iv) NODE-COUNT robustness (Family 1 theta P=3,L=3 + distractors)
    for regime, k in (("small", 0), ("medium", 8), ("large", 20)):
        cells.append(dict(cell_id=f"nodes_{regime}", family="theta_distract", P=3, L=3,
                          k=k, node_count_regime=regime))
    # (v) RANDOM Renz-Nebel A(n,d) (Family 3)
    for n in (8, 12):
        for d in (3, 6, 9):
            cells.append(dict(cell_id=f"rand_n{n}_d{d}", family="random_andl", n=n, d=d))
    return {alg: [dict(c) for c in cells] for alg in ("point", "allen", "rcc8")}


def cell_labels(cell):
    """Normalized cell-label block recorded on every row."""
    return {
        "cell_id": cell["cell_id"],
        "generator_family": cell["family"],
        "redundancy_P": cell.get("P"),
        "hop_count_L": cell.get("L"),
        "cyclomatic_target": cell.get("cyclomatic_target"),
        "node_count_regime": cell.get("node_count_regime"),
        "n": cell.get("n"),
        "d": cell.get("d"),
    }


# --------------------------------------------------------------------------- graph build
def build_graph(cell, rng):
    fam = cell["family"]
    if fam == "theta":
        return topology.theta(rng, cell["P"], cell["L"])
    if fam == "cyclo_aug":
        if cell["cyclomatic_target"] == 0:
            return topology.single_path(rng, cell["L"])
        return topology.cyclo_aug(rng, cell["P"], cell["L"], cell["cyclomatic_target"] - 1)
    if fam == "theta_distract":
        G, s, t = topology.theta(rng, cell["P"], cell["L"])
        G = topology.add_distractors(G, s, t, rng, cell["k"])
        return G, s, t
    if fam == "random_andl":
        return topology.random_andl(rng, cell["n"], cell["d"])
    raise ValueError(fam)


def reference_label(algebra, gold, rng):
    """A SOUND disjunctive superset of `gold` (avg size REF_LABEL_L). Convex for point."""
    if algebra == "point":
        opts = convex_supersets_of(gold)
        return ALG[algebra].sorted_label(opts[int(rng.randint(0, len(opts)))])
    base = ALG[algebra].base
    l = REF_LABEL_L[algebra]
    size = int(np.clip(round(rng.normal(l, 1.5)), 1, len(base)))
    others = [r for r in base if r != gold]
    rng.shuffle(others)
    chosen = set([gold]) | set(others[: size - 1])
    return ALG[algebra].sorted_label(chosen)


def fold_of(seed):
    h = int(hashlib.md5(str(seed).encode()).hexdigest(), 16) % 100
    return "pilot" if h < 10 else ("dev" if h < 30 else "test")


# ---------------------------------------------------------------------- single network
def build_network(algebra, cell, seed, index):
    rng = np.random.RandomState(seed)
    G, s, t = build_graph(cell, rng)
    nodes = sorted(G.nodes())
    objs_list = realize(algebra, len(nodes), rng)
    objs = {n: objs_list[i] for i, n in enumerate(nodes)}
    return _finish(algebra, cell, seed, G, s, t, objs, nodes, rng)


def _finish(algebra, cell, seed, G, s, t, objs, nodes, rng):
    alg = ALG[algebra]
    # gold atomic relations (canonical orientation u<v), query held out
    gold_edges = []
    for (u, v) in G.edges():
        a, b = (u, v) if u < v else (v, u)
        gold_edges.append((a, b, relation(algebra, objs[a], objs[b])))
    gold_edges.sort()
    gold_query = relation(algebra, objs[s], objs[t])

    # structural measures
    V, E = G.number_of_nodes(), G.number_of_edges()
    C = nx.number_connected_components(G)
    mu = E - V + C
    cycle_basis_size = len(nx.cycle_basis(G))
    assert cycle_basis_size == mu, (cell["cell_id"], "mu mismatch", mu, cycle_basis_size)

    # enumerate (capped) deduction paths s->t
    raw_paths = list(islice(nx.all_simple_paths(G, s, t, cutoff=LEN_CUTOFF), PATH_CAP + 1))
    paths_truncated = len(raw_paths) > PATH_CAP
    paths = raw_paths[:PATH_CAP]
    assert len(paths) >= 1, (cell["cell_id"], "deduction-required: no s-t path")

    # per-path composition + correctness GATE
    path_compositions = []
    contributing_edges = set()
    naive = set(alg.base)  # universe
    for path in paths:
        rels = [relation(algebra, objs[path[i]], objs[path[i + 1]])
                for i in range(len(path) - 1)]
        composed = alg.compose_path(rels)
        # GATE: realizable scenario => gold query must lie in every path's composition
        assert gold_query in composed, (
            algebra, cell["cell_id"], seed, "GATE FAIL", path, rels, sorted(composed))
        path_compositions.append(alg.sorted_label(composed))
        naive &= composed
        for i in range(len(path) - 1):
            a, b = path[i], path[i + 1]
            contributing_edges.add((a, b) if a < b else (b, a))
    assert gold_query in naive, "naive intersection lost gold query"
    has_bite = frozenset(naive) != alg.universe
    singleton_resolved = frozenset(naive) == frozenset([gold_query])

    # reference SOUND disjunctive labels (convenience; canonical GT is the atomic graph)
    ref_labels = [[a, b, reference_label(algebra, r, rng)] for (a, b, r) in gold_edges]

    # NL realization
    entity_map = verbalize.assign_entities(algebra, nodes, rng)
    edges_for_text = [(a, b, r) for (a, b, r) in gold_edges]
    document, templates_used = verbalize.realize_text(
        algebra, edges_for_text, entity_map, s, t, rng)
    # deduction-required guard (structural): the query pair is never a verbalized edge,
    # so the two query entities never co-occur in any single sentence.
    assert not G.has_edge(s, t), "deduction-required violated: query pair is an edge"

    # serialized gold graph (output is a STRING per schema)
    out_obj = {
        "edges": [{"source": a, "target": b, "relation": r} for (a, b, r) in gold_edges],
        "query_edge": {"source": s, "target": t, "relation": gold_query, "is_query": True},
    }
    output_str = json.dumps(out_obj, separators=(",", ":"))

    # compact model embedding aligned to abstract-graph node order
    if algebra == "point":
        model = [int(objs[n]) for n in nodes]
    elif algebra == "allen":
        model = [[int(objs[n][0]), int(objs[n][1])] for n in nodes]
    else:
        model = [[int(objs[n][0]), int(objs[n][1]), int(objs[n][2])] for n in nodes]

    row = {
        "input": document,
        "output": output_str,
        "metadata_fold": fold_of(seed),
        "metadata_algebra": algebra,
        "metadata_cell": cell_labels(cell),
        "metadata_query": {"source": s, "target": t, "relation": gold_query},
        "metadata_structure": {
            "num_nodes": V, "num_edges": E, "avg_degree": round(2 * E / V, 3),
            "cyclomatic_number": mu, "cycle_basis_size": cycle_basis_size,
            "num_simple_paths_s_t": len(paths), "paths_truncated": paths_truncated,
            "contributing_edge_count": len(contributing_edges),
            "len_cutoff": LEN_CUTOFF, "path_cap": PATH_CAP,
        },
        "metadata_paths": {
            "path_list": [list(map(int, p)) for p in paths],
            "path_compositions": path_compositions,
            "naive_intersection": alg.sorted_label(naive),
            "has_bite": bool(has_bite),
            "singleton_resolved": bool(singleton_resolved),
        },
        "metadata_abstract_graph": {
            "nodes": [int(n) for n in nodes],
            "edges": [[a, b, r] for (a, b, r) in gold_edges],
            "query_edge": [int(s), int(t)],
        },
        "metadata_reference_disjunctive_labels": ref_labels,
        "metadata_entity_map": {str(n): entity_map[n] for n in nodes},
        "metadata_templates_used": templates_used,
        "metadata_model_embedding": model,
        "metadata_seed": int(seed),
    }
    stats = {
        "algebra": algebra, "cell_id": cell["cell_id"], "fold": row["metadata_fold"],
        "rel_counts": Counter([r for (_, _, r) in gold_edges] + [gold_query]),
        "has_bite": bool(has_bite), "singleton_resolved": bool(singleton_resolved),
        "mu": mu, "num_paths": len(paths), "num_nodes": V,
    }
    return row, stats


# ------------------------------------------------------------------------- worker bridge
def _job(spec):
    algebra, cell, seed, index = spec
    try:
        return build_network(algebra, cell, seed, index)
    except Exception as e:  # noqa: BLE001 - fail loud with context
        logger.error(f"build failed alg={algebra} cell={cell['cell_id']} seed={seed}: {e!r}")
        raise


def net_seed(algebra, cell_id, i):
    """Deterministic 32-bit seed per (algebra, cell, network-index).

    Independent of per-cell counts -> reproducible AND resumable (changing
    --networks-* does not perturb the seeds of already-generated networks).
    """
    return int(hashlib.md5(f"{algebra}|{cell_id}|{i}".encode()).hexdigest()[:8], 16)


# ----------------------------------------------------------------------- coverage plant
def _line_graph_3():
    G = nx.Graph()
    G.add_edges_from([(0, 2), (2, 1)])  # s=0, t=1, intermediate=2
    return G


def build_coverage_row(algebra, rel, seed):
    """Minimal planted network guaranteeing base relation `rel` appears in the corpus.

    s=0 -m=2- t=1 chain; the edge (0,2) is forced (via a concrete model fragment) to
    realize `rel`; node 1 is placed far away so (2,1) is a clean separating relation.
    Routed through the SAME metadata pipeline (_finish) as ordinary networks.
    """
    G, s, t = _line_graph_3(), 0, 1
    oi, oj = planted_pair(algebra, rel)  # relation(oi, oj) == rel  -> assign to (0, 2)
    if algebra == "point":
        objs = {0: int(oi), 2: int(oj), 1: int(max(oi, oj)) + 5}
    elif algebra == "allen":
        shift = max(oi[1], oj[1]) + 10
        objs = {0: tuple(oi), 2: tuple(oj), 1: (shift, shift + 2)}
    else:
        shift = max(oi[0], oj[0]) + 100
        objs = {0: tuple(oi), 2: tuple(oj), 1: (shift, 0, 1)}
    cell = dict(cell_id=f"coverage_{rel}", family="coverage", P=1, L=2)
    return _finish(algebra, cell, seed, G, s, t, objs, sorted(G.nodes()),
                   np.random.RandomState(seed))[0]


def build_qa(all_stats, rel_hist, rows, args):
    """Dataset-level metadata: provenance, coverage tables, histograms, pre-registration."""
    per_cell = defaultdict(lambda: {"count": 0, "has_bite": 0, "singleton": 0,
                                    "mu": Counter(), "paths": [], "nodes": []})
    fold = defaultdict(Counter)
    for st in all_stats:
        key = f"{st['algebra']}/{st['cell_id']}"
        c = per_cell[key]
        c["count"] += 1
        c["has_bite"] += int(st["has_bite"])
        c["singleton"] += int(st["singleton_resolved"])
        c["mu"][st["mu"]] += 1
        c["paths"].append(st["num_paths"])
        c["nodes"].append(st["num_nodes"])
        fold[st["algebra"]][st["fold"]] += 1

    cell_summary = {}
    for key, c in sorted(per_cell.items()):
        n = c["count"]
        cell_summary[key] = {
            "count": n,
            "has_bite_frac": round(c["has_bite"] / n, 4),
            "singleton_resolved_frac": round(c["singleton"] / n, 4),
            "mu_distribution": dict(sorted(c["mu"].items())),
            "mean_num_simple_paths": round(float(np.mean(c["paths"])), 3),
            "mean_num_nodes": round(float(np.mean(c["nodes"])), 3),
        }

    return {
        "name": "Synthetic QCN Backbone",
        "description": (
            "Controlled, globally-consistent qualitative constraint networks over three "
            "relation algebras (convex Point, Allen Interval, RCC-8) built by model-based "
            "realization (integer points / integer-grid intervals / collinear integer "
            "discs), with controlled query topology (redundancy P, hop L, cyclomatic mu, "
            "node count, random Renz-Nebel A(n,d)) and template NL realizations. The "
            "canonical ground truth is the gold ATOMIC graph; every network is realizable "
            "hence globally consistent, and the gold relation on each edge is exact."),
        "algebras": {
            "point": {"role": "primary", "base_relations": ALG["point"].base,
                      "convex_only": True,
                      "note": "non-convex '!=' ({<,>}) forbidden in disjunctive labels"},
            "allen": {"role": "primary", "base_relations": ALG["allen"].base},
            "rcc8": {"role": "secondary", "base_relations": ALG["rcc8"].base,
                     "embedding": "collinear integer discs (exact integer tangency)"},
        },
        "composition_tables": {
            "source": "alreich/qualreas (authoritative TransTable + Converse)",
            "files": ["Linear_Point_Algebra.json", "Linear_Interval_Algebra.json",
                      "RCC8_Algebra.json"],
            "verification": ("Cross-checked in tests/test_qcn.py by 3 independent "
                             "derivations: point composition vs direct sign reasoning; "
                             "Allen composition vs exhaustive endpoint-CSP enumeration "
                             "(full table match); RCC-8 reader soundness vs disc-triple "
                             "enumeration; plus identity + converse-distributivity axioms. "
                             "All 436 checks pass."),
        },
        "generation": {
            "tag": args.tag,
            "networks_per_cell_primary": args.networks_primary,
            "networks_per_cell_secondary": args.networks_secondary,
            "path_cap": PATH_CAP, "len_cutoff": LEN_CUTOFF,
            "total_networks": len(all_stats),
            "correctness_gate": ("PASSED: for every enumerated s-t path, the composition "
                                 "of gold atomic relations contains the gold query "
                                 "relation (asserted on all networks)."),
            "deduction_required": ("query pair (s,t) shares no edge and never co-occurs in "
                                   "a single verbalized sentence"),
            "reproducible": "per (algebra, cell, index) md5 seeds; resumable",
        },
        "splits": {"scheme": "deterministic md5(seed)%100 within every cell",
                   "pilot": "<10", "dev": "10-29", "test": ">=30",
                   "fold_counts": {a: dict(fc) for a, fc in fold.items()}},
        "relation_histograms": {a: dict(rel_hist[a]) for a in rel_hist},
        "cell_summary": cell_summary,
        "realism_preregistration": REALISM_PREREG,
        "row_field_guide": {
            "input": "NL realization (one sentence per non-query edge + Query line)",
            "output": "JSON string: {edges:[{source,target,relation}], query_edge:{...,is_query}}",
            "metadata_paths": "enumerated s-t paths, per-path gold composition, naive "
                              "intersection, has_bite, singleton_resolved",
            "metadata_structure": "num_nodes/edges, cyclomatic_number, cycle_basis_size, "
                                  "num_simple_paths_s_t, paths_truncated, contributing_edge_count",
            "metadata_reference_disjunctive_labels": "SOUND superset per edge (convenience; "
                                                     "convex-only for point)",
        },
    }


def _truncate_strings(o, n=200):
    if isinstance(o, str):
        return o[:n]
    if isinstance(o, list):
        return [_truncate_strings(x, n) for x in o]
    if isinstance(o, dict):
        return {k: _truncate_strings(v, n) for k, v in o.items()}
    return o


def _split_object(obj, root, limit_mb):
    limit = limit_mb * 1e6 * 0.95
    outdir = root / "full_data_out"
    outdir.mkdir(exist_ok=True)
    state = {"part": 1, "cur": defaultdict(list), "size": 200_000}

    def flush():
        if not any(state["cur"].values()):
            return
        ds = [{"dataset": k, "examples": v} for k, v in state["cur"].items() if v]
        # part 1 carries the full QA/provenance metadata; later parts carry a stub.
        if state["part"] == 1:
            meta = dict(obj["metadata"])
            meta["split"] = {"part": 1, "note": "concatenate datasets with the same name "
                             "across all full_data_out/full_data_out_*.json parts to reconstruct"}
        else:
            meta = {"part": state["part"],
                    "note": "split part of full_data_out; concatenate datasets with the "
                            "same name across all parts to reconstruct; full QA metadata "
                            "is in part 1 and in dataset_metadata.json",
                    "realism_preregistration": REALISM_PREREG}
        p = {"metadata": meta, "datasets": ds}
        fp = outdir / f"full_data_out_{state['part']}.json"
        fp.write_text(json.dumps(p, separators=(",", ":")))
        logger.info(f"  wrote {fp.name}: {fp.stat().st_size / 1e6:.1f} MB")
        state["part"] += 1
        state["cur"] = defaultdict(list)
        state["size"] = 200_000

    for d in obj["datasets"]:
        for ex in d["examples"]:
            sz = len(json.dumps(ex, separators=(",", ":")))
            if state["size"] + sz > limit and any(state["cur"].values()):
                flush()
            state["cur"][d["dataset"]].append(ex)
            state["size"] += sz
    flush()
    return state["part"] - 1


def write_outputs(obj, root, limit_mb):
    # standalone QA / provenance / dataset-card metadata (small, always preserved)
    (root / "results").mkdir(exist_ok=True)
    (root / "results" / "dataset_metadata.json").write_text(
        json.dumps(obj["metadata"], indent=2))

    full_path = root / "full_data_out.json"
    full_path.write_text(json.dumps(obj, separators=(",", ":")))
    size_mb = full_path.stat().st_size / 1e6
    total = sum(len(d["examples"]) for d in obj["datasets"])
    logger.info(f"full_data_out.json: {size_mb:.1f} MB, {total} examples")

    # mini = 3 examples/dataset; preview = 10 examples/dataset with strings truncated.
    mini = {"metadata": obj["metadata"],
            "datasets": [{"dataset": d["dataset"], "examples": d["examples"][:3]}
                         for d in obj["datasets"]]}
    (root / "mini_data_out.json").write_text(json.dumps(mini))
    preview = {"metadata": _truncate_strings(obj["metadata"]),
               "datasets": [{"dataset": d["dataset"],
                             "examples": _truncate_strings(d["examples"][:10])}
                            for d in obj["datasets"]]}
    (root / "preview_data_out.json").write_text(json.dumps(preview))
    logger.info("wrote mini_data_out.json (3/dataset) + preview_data_out.json (10/dataset)")

    if size_mb > limit_mb:
        nparts = _split_object(obj, root, limit_mb)
        full_path.unlink()
        logger.info(f"full_data_out.json ({size_mb:.1f} MB) > {limit_mb} MB limit -> split into "
                    f"{nparts} parts under full_data_out/ (removed monolithic full_data_out.json)")
        return nparts
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--networks-primary", type=int, default=500)
    ap.add_argument("--networks-secondary", type=int, default=300)
    ap.add_argument("--procs", type=int, default=4)
    ap.add_argument("--tag", type=str, default="full")
    ap.add_argument("--out", type=str, default=str(ROOT / "data_out.json"))
    # split so every published part stays safely under the 100 MB single-file limit
    ap.add_argument("--split-limit-mb", type=float, default=95.0)
    args = ap.parse_args()

    logger.remove()
    logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
    logger.add(str(ROOT / "logs" / f"run_{args.tag}.log"), rotation="50 MB", level="DEBUG")

    import multiprocessing as mp

    grid = build_grid()
    jobs = []
    for algebra, cells in grid.items():
        n_per = args.networks_primary if algebra in PRIMARY else args.networks_secondary
        for cell in cells:
            for i in range(n_per):
                jobs.append((algebra, cell, net_seed(algebra, cell["cell_id"], i), i))
    logger.info(f"[{args.tag}] {len(jobs)} networks queued "
                f"(primary={args.networks_primary}/cell, secondary={args.networks_secondary}/cell)")

    rows = {alg: [] for alg in grid}
    all_stats = []
    ctx = mp.get_context("fork")
    done = 0
    with ctx.Pool(args.procs) as pool:
        for row, stats in pool.imap_unordered(_job, jobs, chunksize=64):
            rows[stats["algebra"]].append((stats["cell_id"], stats["fold"], row))
            all_stats.append(stats)
            done += 1
            if done % 2000 == 0:
                logger.info(f"  generated {done}/{len(jobs)}")
    logger.info(f"GATE: all {done} networks passed the path-composition correctness gate")

    # ---- relation-coverage check + planting fallback -------------------------------
    rel_hist = {alg: Counter() for alg in grid}
    for st in all_stats:
        rel_hist[st["algebra"]].update(st["rel_counts"])
    for algebra in grid:
        missing = [r for r in ALG[algebra].base if rel_hist[algebra][r] < 3]
        for r in missing:
            logger.warning(f"planting under-represented {algebra} relation {r!r}")
            for k in range(5):
                prow = build_coverage_row(algebra, r, net_seed(algebra, f"cov_{r}", k))
                rows[algebra].append((f"coverage_{r}", prow["metadata_fold"], prow))
                rel_hist[algebra].update(
                    Counter([e[2] for e in prow["metadata_abstract_graph"]["edges"]]
                            + [prow["metadata_query"]["relation"]]))
        still = [r for r in ALG[algebra].base if rel_hist[algebra][r] == 0]
        assert not still, f"{algebra} relations never realized: {still}"

    # ---- assemble dataset object ---------------------------------------------------
    datasets = []
    for algebra in ("point", "allen", "rcc8"):
        examples = [row for (_cid, _f, row) in rows[algebra]]
        datasets.append({"dataset": f"synthetic_qcn_{algebra}", "examples": examples})

    qa = build_qa(all_stats, rel_hist, rows, args)
    obj = {"metadata": qa, "datasets": datasets}
    logger.info(f"assembled: point={len(datasets[0]['examples'])}, "
                f"allen={len(datasets[1]['examples'])}, rcc8={len(datasets[2]['examples'])} examples")
    write_outputs(obj, ROOT, args.split_limit_mb)
    logger.info("DONE")


if __name__ == "__main__":
    main()
