#!/usr/bin/env python3
"""$0 SYNTHETIC ALLEN positive control / NO-GO backstop.

Consistent-by-construction Allen QCNs (random proper intervals -> EXACT atomic Allen
relations between every pair) are read through a noisy channel with an EXACT recall knob;
the SAME five-method comparison the real-text pipeline runs (cross-path full-PC
INTERSECTION vs BEST-SINGLE-PATH vs naive vs raw) is applied. When reads are sound
(recall ~0.95) the intersection must resolve strictly MORE query singletons correctly than
the best single path -- a positive control that the comparison code can detect a true
effect, and the publishable backstop if the real-text gate is NO-GO.
"""
from __future__ import annotations

import numpy as np

import engine

AL = engine.build_allen_algebra()


def _atomic(intervals, a, b):
    (xs, xe), (ys, ye) = intervals[a], intervals[b]
    return engine._allen_rel(xs, xe, ys, ye)


def gen_network(n_events, rng):
    """Random proper intervals -> exact atomic Allen relation for every pair (consistent)."""
    pts = rng.integers(0, 40, size=(n_events, 2))
    intervals = []
    for s, e in pts:
        lo, hi = (int(s), int(e)) if s != e else (int(s), int(s) + 1)
        if lo > hi:
            lo, hi = hi, lo
        if lo == hi:
            hi += 1
        intervals.append((lo, hi))
    return intervals


def simulate_read(true_sym, r, rng, breadth=(0.45, 0.4, 0.15)):
    """Emit a relation SET for an edge whose atomic truth is true_sym. With prob r the read
    is SOUND (contains the truth, optionally widened); else UNSOUND (excludes truth)."""
    base = list(AL.base)
    if rng.random() < r:
        # sound: include the truth + (breadth) extra relations
        roll = rng.random()
        if roll < breadth[0]:
            return frozenset({true_sym})
        elif roll < breadth[0] + breadth[1]:
            extra = rng.choice([x for x in base if x != true_sym], size=1, replace=False)
            return frozenset({true_sym, *extra})
        else:
            k = int(rng.integers(2, 5))
            extra = rng.choice([x for x in base if x != true_sym],
                               size=min(k, len(base) - 1), replace=False)
            return frozenset({true_sym, *extra})
    else:
        # unsound: a random non-empty set NOT containing the truth
        pool = [x for x in base if x != true_sym]
        k = int(rng.integers(1, 3))
        return frozenset(rng.choice(pool, size=min(k, len(pool)), replace=False).tolist())


def run_one(n_events, r, rng):
    intervals = gen_network(n_events, rng)
    nodes = list(range(n_events))
    s, t = 0, 1
    vias = nodes[2:]
    true_q = _atomic(intervals, s, t)
    qcn = engine.QCN(AL, nodes)
    reads = {}
    confs = {}
    induced = [(s, w) for w in vias] + [(w, t) for w in vias]
    # include via-via edges for iteration
    for i in range(len(vias)):
        for j in range(i + 1, len(vias)):
            induced.append((vias[i], vias[j]))
    for (a, b) in induced:
        tr = _atomic(intervals, a, b)
        rd = simulate_read(tr, r, rng)
        reads[(a, b)] = rd
        confs[(a, b)] = float(min(1.0, max(0.0, rng.normal(0.7, 0.15))))
        qcn.set_edge(qcn.index[a], qcn.index[b], rd)
    qi, qj = qcn.index[s], qcn.index[t]
    path_conf = float(min(confs.values())) if confs else 0.0
    naive_set = engine.naive_single_pass(qcn, qi, qj)
    per_path = []
    for w in vias:
        per_path.append(AL.compose(reads[(s, w)], reads[(w, t)]))
    best = min(per_path, key=len) if per_path else AL.universe
    ok, _ = engine.pc2_full(qcn)
    inter = AL.empty if not ok else qcn.get(qi, qj)

    def rec(R):
        if not R:
            return {"answered": False, "correct": None, "conf": path_conf}
        if len(R) == 1:
            return {"answered": True, "correct": int(next(iter(R)) == true_q), "conf": path_conf}
        return {"answered": False, "correct": None, "conf": path_conf}
    return {"intersection": rec(inter), "best_single": rec(best), "naive": rec(naive_set),
            "bite": len(best) - len(inter), "singleton_resolved": int(len(inter) == 1)}


def run_control(n_net=600, n_events=6, r=0.95, seed=12345):
    rng = np.random.default_rng(seed)
    rows = {m: [] for m in ("intersection", "best_single", "naive")}
    bites, res = [], 0
    for _ in range(n_net):
        out = run_one(n_events, r, rng)
        for m in rows:
            rows[m].append(out[m])
        bites.append(out["bite"])
        res += out["singleton_resolved"]

    def cov_acc(recs):
        ans = [x for x in recs if x["answered"]]
        cov = len(ans) / len(recs) if recs else float("nan")
        acc = float(np.mean([x["correct"] for x in ans])) if ans else float("nan")
        return cov, acc
    out = {}
    for m in rows:
        cov, acc = cov_acc(rows[m])
        out[m] = {"coverage": cov, "selective_acc": acc}
    inter_cov = out["intersection"]["coverage"]
    best_cov = out["best_single"]["coverage"]
    return {"n_net": n_net, "n_events": n_events, "recall": r,
            "per_method": out, "mean_bite": float(np.mean(bites)),
            "intersection_resolves_more_than_best_single": bool(inter_cov > best_cov + 1e-9),
            "coverage_gain_intersection_vs_best": float(inter_cov - best_cov),
            "singleton_resolved_rate": res / n_net, "tag": "SYNTHETIC-ALLEN-CONTROL"}


if __name__ == "__main__":
    import json
    for r in (0.95, 0.85, 0.7):
        print(json.dumps(run_control(n_net=400, r=r), indent=2, default=str))
