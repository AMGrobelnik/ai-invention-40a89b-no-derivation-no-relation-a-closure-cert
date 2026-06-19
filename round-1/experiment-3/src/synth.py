#!/usr/bin/env python3
"""Synthetic clean-ground-truth battery (scenario-then-abstract consistent QCNs).

For each network we draw a concrete realization (point coords or nested/disjoint
intervals) -> the gold relation of EVERY pair is read off the realization (globally
consistent by construction). We then realize a short clean English document that states
the relation of a spanning subset of pairs (a chain + a few extra edges) with surface
variation, leaving other pairs implicit. This gives:
  * a clean-text RECALL reference (stated edges -> should be read correctly),
  * clean-text DEDUCTION triangles (implicit query edge resolved by closure),
  * an error-type distribution to compare (TV) against the real corpora.

Events are referred to by unique placeholder tokens (EVT0, EVT1, ...) to avoid
mention-ambiguity; marking wraps the token.
"""
from __future__ import annotations

import random

# coarse-relation surface realizations (the breadth knob is applied at elicitation time;
# here we just state the gold relation in clean prose with surface variation)
CONNECTIVES = {
    "before": ["happened before", "occurred earlier than", "took place prior to", "came before"],
    "after": ["happened after", "occurred later than", "took place after", "came after"],
    "simultaneous": ["happened at the same time as", "occurred simultaneously with",
                     "coincided with", "happened concurrently with"],
    "includes": ["was ongoing throughout the whole period of", "spanned the entire time of",
                 "lasted through all of"],
    "is_included": ["happened during", "occurred in the middle of", "took place within the span of"],
}


def _point_gold(a: float, b: float) -> str:
    if a < b:
        return "before"
    if a > b:
        return "after"
    return "simultaneous"


def _interval_coarse(ai, bi) -> str:
    """Coarse Allen relation for nested/disjoint/equal intervals (no partial overlap)."""
    (as_, ae), (bs, be) = ai, bi
    if ae < bs:
        return "before"
    if be < as_:
        return "after"
    if as_ == bs and ae == be:
        return "simultaneous"
    if as_ <= bs and be <= ae:
        return "includes"
    if bs <= as_ and ae <= be:
        return "is_included"
    return "before" if as_ < bs else "after"  # fallback (shouldn't happen with our generator)


def gen_networks(n_networks: int, algebra: str, seed: int):
    """Yield network dicts: {nodes, coords/intervals, doc_text, edges, triangles}.

    edges: list of {u,v,gold,stated(bool),deduction_required,marked_text}
    """
    rng = random.Random(seed)
    nets = []
    for ni in range(n_networks):
        k = rng.choice([4, 4, 5, 5, 6])
        nodes = [f"EVT{i}" for i in range(k)]
        if algebra == "POINT":
            coords = {}
            xs = rng.sample(range(0, 40), k)
            # inject occasional ties (simultaneous)
            if rng.random() < 0.3 and k >= 3:
                i, j = rng.sample(range(k), 2)
                xs[j] = xs[i]
            for i, nd in enumerate(nodes):
                coords[nd] = xs[i]
            def gold(u, v):
                return _point_gold(coords[u], coords[v])
        else:
            intervals = {}
            # build nested/disjoint intervals via a recursive layout
            cursor = [0]
            def place(width):
                s = cursor[0] + rng.randint(1, 3)
                e = s + width
                cursor[0] = e + rng.randint(0, 2)
                return (s, e)
            for nd in nodes:
                w = rng.randint(2, 8)
                intervals[nd] = place(w)
            # occasionally nest one inside another / make equal
            if k >= 3:
                a, b = rng.sample(nodes, 2)
                s, e = intervals[a]
                if e - s >= 4:
                    intervals[b] = (s + 1, e - 1)  # b inside a
            if rng.random() < 0.25:
                a, b = rng.sample(nodes, 2)
                intervals[b] = intervals[a]  # equal
            def gold(u, v):
                return _interval_coarse(intervals[u], intervals[v])

        # stated spanning edges: a chain + a couple of random extra edges
        stated = set()
        order = nodes[:]
        rng.shuffle(order)
        for i in range(len(order) - 1):
            stated.add(tuple(sorted((order[i], order[i + 1]))))
        n_extra = rng.randint(1, 2)
        all_pairs = [tuple(sorted((nodes[i], nodes[j]))) for i in range(k) for j in range(i + 1, k)]
        for p in rng.sample([p for p in all_pairs if p not in stated],
                            min(n_extra, len(all_pairs) - len(stated))):
            stated.add(p)

        # build doc: one sentence per stated edge, surface-varied
        sentences = []
        for (u, v) in sorted(stated):
            g = gold(u, v)
            conn = rng.choice(CONNECTIVES[g])
            sentences.append(f"{u} {conn} {v}.")
        rng.shuffle(sentences)
        doc = " ".join(sentences)

        def mark(u, v):
            t = doc.replace(u, f"[[E1]]{u}[[/E1]]", 1).replace(v, f"[[E2]]{v}[[/E2]]", 1)
            return t

        edges = []
        for (u, v) in all_pairs:
            is_stated = (u, v) in stated
            edges.append({"u": u, "v": v, "gold": gold(u, v), "stated": is_stated,
                          "deduction_required": not is_stated, "sentdiff": 0 if is_stated else 2,
                          "marked_text": mark(u, v)})
        nets.append({"net_id": f"{algebra.lower()}_net{ni}", "algebra": algebra,
                     "nodes": nodes, "edges": edges})
    return nets


def build_synthetic_arm(n_networks: int, seed: int, max_tri: int = 50, max_edges: int = 120):
    """Return a standardized arm dict (same shape as corpora arms) for POINT+ALLEN synth.

    Budget-bounded like the real arms: keep all triangle edges, harvest up to max_tri
    triangles, then top up standalone edges to max_edges (balanced stated/unstated)."""
    from corpora import harvest_triangles
    rng = random.Random(seed)
    all_tasks = {}
    cand_tris = []
    for algebra in ("POINT", "ALLEN"):
        nets = gen_networks(n_networks, algebra, seed + (0 if algebra == "POINT" else 777))
        for net in nets:
            nid = net["net_id"]
            for ed in net["edges"]:
                key = (nid,) + tuple(sorted((ed["u"], ed["v"])))
                all_tasks[key] = {"arm": "synthetic", "algebra": algebra, "docid": nid,
                                  "u": ed["u"], "v": ed["v"], "gold": ed["gold"],
                                  "sentdiff": ed["sentdiff"],
                                  "deduction_required": ed["deduction_required"],
                                  "stated": ed["stated"], "marked_text": ed["marked_text"]}
            for t in harvest_triangles(net["edges"], 10_000, rng):
                t2 = dict(t); t2["docid"] = nid; t2["arm"] = "synthetic"; t2["algebra"] = algebra
                cand_tris.append(t2)
    rng.shuffle(cand_tris)
    edge_tasks = {}
    triangles = []
    for t in cand_tris:
        if len(triangles) >= max_tri:
            break
        keys = [(t["docid"],) + tuple(sorted((u, v))) for (u, v) in t["edges"]]
        new = [k for k in keys if k not in edge_tasks]
        if len(edge_tasks) + len(new) > max_edges:
            continue
        for k in keys:
            edge_tasks[k] = all_tasks[k]
        triangles.append(t)
    # top up standalone edges
    rest = [k for k in all_tasks if k not in edge_tasks]
    rng.shuffle(rest)
    for k in rest:
        if len(edge_tasks) >= max_edges:
            break
        edge_tasks[k] = all_tasks[k]
    return {"arm": "synthetic", "algebra": "MIXED", "provenance": "scenario-then-abstract consistent QCNs",
            "edge_tasks": edge_tasks, "triangles": triangles,
            "n_docs": 2 * n_networks, "n_edges": len(edge_tasks), "n_triangles": len(triangles)}


if __name__ == "__main__":
    arm = build_synthetic_arm(n_networks=20, seed=20260617)
    print(f"synthetic: edges={arm['n_edges']} tri={arm['n_triangles']}")
    k = next(iter(arm["edge_tasks"]))
    print("sample:", arm["edge_tasks"][k]["gold"], "|", arm["edge_tasks"][k]["marked_text"][:200])
    stated = sum(1 for t in arm["edge_tasks"].values() if t.get("stated"))
    print("stated edges:", stated, "/ total", arm["n_edges"])
