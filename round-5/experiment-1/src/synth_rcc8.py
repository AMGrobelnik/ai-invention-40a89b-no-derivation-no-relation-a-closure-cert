#!/usr/bin/env python3
"""$0 SYNTHETIC RCC-8 positive control / publishable backstop.

Consistent-by-construction RCC-8 QCNs: random 1-D intervals (regions on a line) realise
ALL 8 RCC-8 base relations exactly and consistently (interval containment/overlap is a
faithful RCC-8 model). Each interval pair's atomic RCC-8 relation is read off the model;
the network is globally consistent by construction. The reads pass through a noisy channel
with an EXACT recall knob, and the SAME five-method comparison the real pipeline runs
(cross-path full-PC INTERSECTION vs BEST-SINGLE-PATH vs naive vs raw) is applied.

PRE-REGISTERED: at recall ~0.95 the intersection must resolve strictly MORE query
singletons (higher coverage) than the best single path -- proving the comparison code +
RCC-8 wiring detect a TRUE cross-path coding effect when same-algebra redundancy exists
and reads are sound. This is the positive control AND the publishable backstop for the
(structurally NO-GO) real spatial venue.
"""
from __future__ import annotations

import numpy as np

import engine

RCC8 = engine.build_rcc8_algebra()


def _rcc8_atomic(a, b):
    """Atomic RCC-8 relation of 1-D region A=(a1,a2) to B=(b1,b2) (proper intervals)."""
    a1, a2 = a
    b1, b2 = b
    if a1 == b1 and a2 == b2:
        return "EQ"
    if a2 < b1 or b2 < a1:
        return "DC"
    if a2 == b1 or b2 == a1:                      # touch at a single boundary point
        return "EC"
    # overlap region exists; classify containment
    if b1 <= a1 and a2 <= b2:                     # A inside B
        return "NTPP" if (b1 < a1 and a2 < b2) else "TPP"
    if a1 <= b1 and b2 <= a2:                     # B inside A
        return "NTPPi" if (a1 < b1 and b2 < a2) else "TPPi"
    return "PO"                                   # proper partial overlap


def gen_intervals(n, rng):
    out = []
    for _ in range(n):
        lo = int(rng.integers(0, 36))
        ln = int(rng.integers(1, 10))
        out.append((lo, lo + ln))
    return out


def simulate_read(true_sym, r, rng):
    """SOUND with prob r (contains truth, maybe widened); else UNSOUND (excludes truth)."""
    base = list(RCC8.base)
    if rng.random() < r:
        roll = rng.random()
        if roll < 0.45:
            return frozenset({true_sym})
        elif roll < 0.85:
            extra = rng.choice([x for x in base if x != true_sym], size=1, replace=False)
            return frozenset({true_sym, *extra})
        k = int(rng.integers(2, 4))
        extra = rng.choice([x for x in base if x != true_sym],
                           size=min(k, len(base) - 1), replace=False)
        return frozenset({true_sym, *extra})
    pool = [x for x in base if x != true_sym]
    k = int(rng.integers(1, 3))
    return frozenset(rng.choice(pool, size=min(k, len(pool)), replace=False).tolist())


def run_one(n_events, r, rng):
    iv = gen_intervals(n_events, rng)
    nodes = list(range(n_events))
    s, t = 0, 1
    vias = nodes[2:]
    true_q = _rcc8_atomic(iv[s], iv[t])
    qcn = engine.QCN(RCC8, nodes)
    reads, confs = {}, {}
    induced = [(s, w) for w in vias] + [(w, t) for w in vias]
    for i in range(len(vias)):
        for j in range(i + 1, len(vias)):
            induced.append((vias[i], vias[j]))
    for (a, b) in induced:
        tr = _rcc8_atomic(iv[a], iv[b])
        rd = simulate_read(tr, r, rng)
        reads[(a, b)] = rd
        confs[(a, b)] = float(min(1.0, max(0.0, rng.normal(0.7, 0.15))))
        qcn.set_edge(qcn.index[a], qcn.index[b], rd)
    qi, qj = qcn.index[s], qcn.index[t]
    path_conf = float(min(confs.values())) if confs else 0.0
    naive_set = engine.naive_single_pass(qcn, qi, qj)
    per_path = [RCC8.compose(reads[(s, w)], reads[(w, t)]) for w in vias]
    best = min(per_path, key=len) if per_path else RCC8.universe
    ok, _ = engine.pc2_full(qcn)
    inter = RCC8.empty if not ok else qcn.get(qi, qj)

    def rec(R):
        if not R:
            return {"answered": False, "correct": None, "conf": path_conf}
        if len(R) == 1:
            return {"answered": True, "correct": int(next(iter(R)) == true_q), "conf": path_conf}
        return {"answered": False, "correct": None, "conf": path_conf}
    return {"intersection": rec(inter), "best_single": rec(best), "naive": rec(naive_set),
            "bite": len(best) - len(inter), "singleton_resolved": int(len(inter) == 1)}


def find_audit_instance(seed=777, max_try=4000):
    """Find ONE consistent network with a genuine cross-path narrowing for the Prolog audit:
    two edge-disjoint length-2 paths s-w-t whose SOUND reads compose to constraints whose
    INTERSECTION is a singleton (== true query) while the best single path is NON-singleton.
    Returns (paths, gold, best_single, inter) or None. Uses r=1.0 (always-sound reads)."""
    rng = np.random.default_rng(seed)
    for _ in range(max_try):
        iv = gen_intervals(4, rng)
        s, t, w1, w2 = 0, 1, 2, 3
        true_q = _rcc8_atomic(iv[s], iv[t])
        reads = {}
        for (a, b) in [(s, w1), (w1, t), (s, w2), (w2, t)]:
            reads[(a, b)] = simulate_read(_rcc8_atomic(iv[a], iv[b]), 1.0, rng)
        p1 = RCC8.compose(reads[(s, w1)], reads[(w1, t)])
        p2 = RCC8.compose(reads[(s, w2)], reads[(w2, t)])
        inter = p1 & p2
        best = min((p1, p2), key=len)
        if len(best) >= 2 and len(inter) == 1 and next(iter(inter)) == true_q:
            paths = [[("S", "W1", sorted(reads[(s, w1)])), ("W1", "T", sorted(reads[(w1, t)]))],
                     [("S", "W2", sorted(reads[(s, w2)])), ("W2", "T", sorted(reads[(w2, t)]))]]
            return {"paths": paths, "gold": [true_q], "best_single": sorted(best),
                    "inter": sorted(inter), "p1": sorted(p1), "p2": sorted(p2)}
    return None


def run_control(n_net=500, n_events=6, r=0.95, seed=12345):
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
    inter_acc = out["intersection"]["selective_acc"]
    best_acc = out["best_single"]["selective_acc"]
    return {"n_net": n_net, "n_events": n_events, "recall": r, "per_method": out,
            "mean_bite": float(np.mean(bites)),
            "intersection_resolves_more_than_best_single": bool(inter_cov > best_cov + 1e-9),
            "coverage_gain_intersection_vs_best": float(inter_cov - best_cov),
            "selective_acc_gain_intersection_vs_best":
                float((inter_acc - best_acc)) if (inter_acc == inter_acc and best_acc == best_acc) else float("nan"),
            "singleton_resolved_rate": res / n_net, "tag": "SYNTHETIC-RCC8-CONTROL"}


if __name__ == "__main__":
    import json
    for r in (0.95, 0.85, 0.70):
        print(json.dumps(run_control(n_net=400, r=r), indent=2, default=str))
