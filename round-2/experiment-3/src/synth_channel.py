#!/usr/bin/env python3
"""Synthetic clean-ground-truth reader channel + matched-coverage baseline harness.

The point-algebra bitmask machinery, the consistent-by-construction QCN generators
(gen_family_R = redundancy, gen_family_H = hop/cyclomatic chain), the simulated reader
channel with EXACT recall / breadth / rho knobs, and the three closure variants
(FULL = our iterated PC-2, NAIVE = single-pass, OFF = direct read) are COPIED VERBATIM
from gen_art_experiment_2/method.py (the iter-1 synthetic de-risking experiment).

NEW here (the matched-coverage comparison the iter-2 plan asks for): on top of those
generators+channel we run the SAME five methods compared on real text -- Mode-A FULL
closure, NAIVE single-pass, RAW forced-single, SELF-CONSISTENCY voting, and a
PATH-OF-THOUGHTS analog (per-path composition, modal vote, abstain on disagreement) --
each emitting (answered, prediction, correct, confidence), and we compute risk-coverage
selective accuracy at MATCHED coverage with doc(network)-clustered bootstrap CIs. This is
the $0, fully-powered (N>=600/cell) backstop that carries the matched-coverage mechanism
claim if real text is thin/underpowered.  recall~0.96 => reads are SOUND.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.stats import norm

# --------------------------------------------------------------------------- #
# 1. RELATION ALGEBRA  (convex point algebra) -- VERBATIM from experiment_2
# 3-bit masks: LT=1, EQ=2, GT=4, U=7, EMPTY=0.
# --------------------------------------------------------------------------- #
LT, EQ, GT, U, EMPTY = 1, 2, 4, 7, 0
BASE_BITS = (LT, EQ, GT)
CONVEX = (LT, EQ, GT, LT | EQ, EQ | GT, U)        # {1,2,4,3,6,7}
NONCONVEX = LT | GT                               # 5 == NOT-EQUAL (forbidden as a read)
REL_NAME = {0: "EMPTY", 1: "<", 2: "=", 4: ">", 3: "<=", 6: ">=", 7: "?", 5: "<>"}

BASE_COMP = {
    (LT, LT): LT, (LT, EQ): LT, (LT, GT): U,
    (EQ, LT): LT, (EQ, EQ): EQ, (EQ, GT): GT,
    (GT, LT): U,  (GT, EQ): GT, (GT, GT): GT,
}
CONV_BASE = {LT: GT, EQ: EQ, GT: LT}


def _build_tables():
    comp = [[0] * 8 for _ in range(8)]
    conv = [0] * 8
    for R in range(8):
        m = 0
        for a in BASE_BITS:
            if R & a:
                m |= CONV_BASE[a]
        conv[R] = m
        for S in range(8):
            mm = 0
            for a in BASE_BITS:
                if R & a:
                    for b in BASE_BITS:
                        if S & b:
                            mm |= BASE_COMP[(a, b)]
            comp[R][S] = mm
    return comp, conv


COMP, CONV = _build_tables()


def popcount(x: int) -> int:
    return bin(x).count("1")


def self_verify_point_algebra() -> None:
    assert COMP[LT][LT] == LT
    assert COMP[LT][EQ] == LT
    assert COMP[LT][GT] == U
    assert COMP[EQ][GT] == GT
    assert COMP[GT][LT] == U
    assert COMP[GT][GT] == GT
    assert CONV[LT] == GT and CONV[GT] == LT and CONV[EQ] == EQ
    assert CONV[LT | EQ] == EQ | GT
    assert (LT | EQ) & (EQ | GT) == EQ
    for R in CONVEX:
        assert COMP[EQ][R] == R and COMP[R][EQ] == R
    for R in CONVEX:
        for S in CONVEX:
            assert COMP[R][S] != NONCONVEX
            assert (R & S) != NONCONVEX
    rng = np.random.default_rng(0)
    for _ in range(2000):
        a, b, c = (int(rng.choice(CONVEX)) for _ in range(3))
        assert COMP[COMP[a][b]][c] == COMP[a][COMP[b][c]]


# --------------------------------------------------------------------------- #
# 2. QCN GENERATORS (consistent BY CONSTRUCTION) -- VERBATIM from experiment_2
# --------------------------------------------------------------------------- #
class Net:
    __slots__ = ("n", "edges", "gold", "query", "gold_query")

    def __init__(self, n, edges, gold, query, gold_query):
        self.n = n
        self.edges = edges
        self.gold = gold
        self.query = query
        self.gold_query = gold_query


def _base_from_times(ta, tb):
    if ta < tb:
        return LT
    if ta > tb:
        return GT
    return EQ


def gen_family_R(K: int, rng: np.random.Generator) -> Net:
    """REDUNDANCY family: K parallel length-2 paths i -> m_k -> j (all intermediates
    strictly between i and j => every length-2 composition contains gold LT)."""
    i, j = 0, 1
    t = {i: 0.0, j: 10.0}
    edges = []
    gold = {}
    for k in range(K):
        m = 2 + k
        t[m] = float(rng.uniform(1.0, 9.0))
        edges.append((i, m))
        edges.append((m, j))
    for (a, b) in edges:
        gold[(a, b)] = _base_from_times(t[a], t[b])
    n = 2 + K
    query = (i, j)
    gold_query = _base_from_times(t[i], t[j])
    gold[query] = gold_query
    return Net(n, edges, gold, query, gold_query)


def gen_family_H(L: int, C: int, rng: np.random.Generator):
    """HOP/CYCLOMATIC family: chain of length L plus C interior chords; NO direct
    (i,j) edge, NO consecutive-skip shortcut -> NAIVE gains no length-2 query
    shortcut while FULL still benefits from iteration. cyclomatic = |E|-|V|+1 = C."""
    i, j = 0, L
    t = {node: float(node) for node in range(L + 1)}
    edges = [(n_, n_ + 1) for n_ in range(L)]
    interior = list(range(1, L))
    cand = [(a, b) for ai, a in enumerate(interior) for b in interior[ai + 1:]
            if b - a >= 2]
    rng.shuffle(cand)
    added = 0
    for (a, b) in cand:
        if added >= C:
            break
        if (a, b) in edges or (b, a) in edges:
            continue
        edges.append((a, b))
        added += 1
    gold = {}
    for (a, b) in edges:
        gold[(a, b)] = _base_from_times(t[a], t[b])
    query = (i, j)
    gold_query = _base_from_times(t[i], t[j])
    gold[query] = gold_query
    cyclo = len(edges) - (L + 1) + 1
    return Net(L + 1, edges, gold, query, gold_query), cyclo


# --------------------------------------------------------------------------- #
# 3. SIMULATED READER CHANNEL -- VERBATIM from experiment_2
# --------------------------------------------------------------------------- #
_SOUND = {
    LT: ([LT, LT | EQ, U]),
    EQ: ([EQ, LT | EQ, EQ | GT, U]),
    GT: ([GT, EQ | GT, U]),
}
_UNSOUND = {
    LT: [EQ, GT, EQ | GT],
    EQ: [LT, GT],
    GT: [LT, EQ, LT | EQ],
}


def _sound_weights(g: int, breadth: dict) -> np.ndarray:
    ps, pt, pu = breadth["p_singleton"], breadth["p_two"], breadth["p_univ"]
    if g == EQ:
        w = np.array([ps, pt / 2.0, pt / 2.0, pu], dtype=float)
    else:
        w = np.array([ps, pt, pu], dtype=float)
    s = w.sum()
    return w / s if s > 0 else np.ones_like(w) / len(w)


class ReadResult:
    __slots__ = ("rel", "sound", "conf", "edges", "bite_lost", "kept")

    def __init__(self, rel, sound, conf, edges, bite_lost, kept):
        self.rel = rel
        self.sound = sound
        self.conf = conf
        self.edges = edges
        self.bite_lost = bite_lost
        self.kept = kept


def read_network(net: Net, r: float, rho: float, breadth: dict,
                 rng: np.random.Generator, gate: bool = False, gate_drop: float = 0.0,
                 edges=None) -> ReadResult:
    """Read a chosen edge list (default net.edges) through the noisy channel."""
    qn = norm.ppf(min(max(r, 1e-9), 1.0 - 1e-9))
    u_latent = float(rng.standard_normal())
    sqrt_rho = math.sqrt(rho)
    sqrt_1mrho = math.sqrt(1.0 - rho)
    rel, sound, conf = {}, {}, {}
    bite_lost = 0
    use_edges = list(net.edges if edges is None else edges)
    for (a, b) in use_edges:
        g = net.gold[(a, b)]
        v = float(rng.standard_normal())
        z = sqrt_rho * u_latent + sqrt_1mrho * v
        is_sound = (z <= qn)
        c = float(norm.cdf(-z) + 0.01 * rng.standard_normal())
        if is_sound:
            opts = _SOUND[g]
            w = _sound_weights(g, breadth)
            s_e = int(rng.choice(opts, p=w))
        else:
            opts = _UNSOUND[g]
            s_e = int(rng.choice(opts))
        if s_e == NONCONVEX:
            s_e = U
            bite_lost += 1
        rel[(a, b)] = s_e
        rel[(b, a)] = CONV[s_e]
        sound[(a, b)] = bool(is_sound)
        conf[(a, b)] = c
    kept = {e: True for e in use_edges}
    if gate and use_edges:
        confs = np.array([conf[e] for e in use_edges])
        ndrop = int(math.floor(gate_drop * len(use_edges)))
        if ndrop > 0:
            drop_idx = np.argsort(confs)[:ndrop]
            for di in drop_idx:
                kept[use_edges[int(di)]] = False
    return ReadResult(rel, sound, conf, use_edges, bite_lost, kept)


def _matrix_from_read(net: Net, rd: ReadResult):
    n = net.n
    M = [[U] * n for _ in range(n)]
    for x in range(n):
        M[x][x] = EQ
    for (a, b) in rd.edges:
        if not rd.kept[(a, b)]:
            continue
        M[a][b] = rd.rel[(a, b)]
        M[b][a] = rd.rel[(b, a)]
    return M


def closure_FULL(M, n):
    """Iterated path-consistency (PC-2 / Mackworth). VERBATIM."""
    changed = True
    while changed:
        changed = False
        for k in range(n):
            Mk = M[k]
            for i in range(n):
                if i == k:
                    continue
                rik = M[i][k]
                if rik == U:
                    continue
                Mi = M[i]
                comp_row = COMP[rik]
                for j in range(n):
                    if j == i or j == k:
                        continue
                    rkj = Mk[j]
                    if rkj == U:
                        continue
                    new = Mi[j] & comp_row[rkj]
                    if new != Mi[j]:
                        Mi[j] = new
                        M[j][i] = CONV[new]
                        if new == EMPTY:
                            return "COLLAPSE", M
                        changed = True
    return "OK", M


def closure_NAIVE(rd: ReadResult, n, query):
    """Single pass, NO fixpoint over directly-read length-2 paths. VERBATIM."""
    i, j = query
    res = rd.rel.get((i, j), U) if rd.kept.get((i, j), False) else U
    for k in range(n):
        if k == i or k == j:
            continue
        a = rd.rel.get((i, k))
        b = rd.rel.get((k, j))
        ka = rd.kept.get((i, k), False) or rd.kept.get((k, i), False)
        kb = rd.kept.get((k, j), False) or rd.kept.get((j, k), False)
        if a is not None and b is not None and ka and kb:
            res &= COMP[a][b]
    return res


# --------------------------------------------------------------------------- #
# 4. NEW: matched-coverage five-method comparison on the synthetic channel
# --------------------------------------------------------------------------- #
def _forced_single(relset: int, rng: np.random.Generator) -> int:
    """Commit a (possibly disjunctive) read to ONE base relation (the LLM 'guessing')."""
    members = [b for b in BASE_BITS if relset & b]
    if not members:
        members = list(BASE_BITS)
    return int(rng.choice(members))


def _min_path_conf(net: Net, rd: ReadResult) -> float:
    cs = [rd.conf[e] for e in net.edges if rd.kept.get(e, False)]
    return float(min(cs)) if cs else 0.0


def run_methods_on_net(net: Net, r: float, rho: float, breadth: dict, sc_k: int,
                       rng: np.random.Generator):
    """Return {method: (answered:bool, correct:int|None, conf:float)} for ONE network.

    Path edges are read through the channel and fed to closure (query held out, exactly
    like the real-text local-reader protocol). The query edge is read DIRECTLY (separate
    draw) to give RAW + SELF-CONSISTENCY something to commit to."""
    gq = net.gold_query
    rd = read_network(net, r, rho, breadth, rng)            # path-edge reads
    M = _matrix_from_read(net, rd)
    i, j = net.query

    # --- Mode-A FULL closure (our method): query held at U ---
    status, Mc = closure_FULL([row[:] for row in M], net.n)
    if status == "COLLAPSE":
        modeA = (False, None, _min_path_conf(net, rd))      # abstain (inconsistency)
    else:
        rset = Mc[i][j]
        if popcount(rset) == 1:
            modeA = (True, int(rset == gq), _min_path_conf(net, rd))
        else:
            modeA = (False, None, _min_path_conf(net, rd))  # disjunction -> abstain

    # --- NAIVE single-pass ---
    nres = closure_NAIVE(rd, net.n, net.query)
    if nres != EMPTY and popcount(nres) == 1:
        naive = (True, int(nres == gq), _min_path_conf(net, rd))
    else:
        naive = (False, None, _min_path_conf(net, rd))

    # --- direct query-edge reads (for RAW + SC), same channel ---
    qnet = Net(net.n, [net.query], {net.query: gq, (j, i): CONV[gq]}, net.query, gq)
    q_reads = []
    for _ in range(max(1, sc_k)):
        rq = read_network(qnet, r, rho, breadth, rng, edges=[net.query])
        q_reads.append((rq.rel[net.query], rq.conf[net.query]))
    # RAW = first draw, forced to a single relation
    raw_set, raw_conf = q_reads[0]
    raw_pred = _forced_single(raw_set, rng)
    raw = (True, int(raw_pred == gq), float(raw_conf))
    # SELF-CONSISTENCY = majority vote of forced-singles over k draws
    votes = [_forced_single(s, rng) for (s, _) in q_reads]
    counts = {b: votes.count(b) for b in set(votes)}
    top = max(counts, key=counts.get)
    margin = counts[top] / len(votes)
    sc = (True, int(top == gq), float(margin))

    # --- PATH-OF-THOUGHTS analog: per length-2 path compose, modal vote, abstain on disagreement ---
    path_preds = []
    path_confs = []
    for k in range(net.n):
        if k in (i, j):
            continue
        a = rd.rel.get((i, k)); b = rd.rel.get((k, j))
        ka = rd.kept.get((i, k), False); kb = rd.kept.get((k, j), False)
        if a is not None and b is not None and ka and kb:
            comp = COMP[a][b]
            path_preds.append(_forced_single(comp, rng))     # reason this path INDEPENDENTLY
            path_confs.append(min(rd.conf[(i, k)], rd.conf[(k, j)]))
    if not path_preds:
        pot = (False, None, 0.0)
    else:
        pcounts = {b: path_preds.count(b) for b in set(path_preds)}
        ptop = max(pcounts, key=pcounts.get)
        agree = pcounts[ptop] / len(path_preds)
        if len(pcounts) > 1 and agree < 1.0 - 1e-9 and len(path_preds) > 1:
            # paths DISAGREE -> PoT has no intersection step to reconcile -> abstain
            answered = agree >= 0.5
        else:
            answered = True
        pot = (answered, (int(ptop == gq) if answered else None),
               float(agree * (sum(path_confs) / len(path_confs))))
    return {"modeA_full": modeA, "naive": naive, "raw": raw, "sc": sc, "pot": pot}


def simulate_matched_coverage(family: str, params: dict, n_net: int, r: float, rho: float,
                              breadth: dict, sc_k: int, seed: int):
    """Run n_net networks; return per-method lists of (answered, correct, conf, net_id)."""
    rng = np.random.default_rng(seed)
    rows = {m: [] for m in ("modeA_full", "naive", "raw", "sc", "pot")}
    for ni in range(n_net):
        if family == "R":
            net = gen_family_R(params["K"], rng)
        else:
            net, _ = gen_family_H(params["L"], params.get("C", 0), rng)
        res = run_methods_on_net(net, r, rho, breadth, sc_k, rng)
        for m, (ans, corr, conf) in res.items():
            rows[m].append({"answered": bool(ans), "correct": corr,
                            "conf": float(conf), "net": ni})
    return rows
