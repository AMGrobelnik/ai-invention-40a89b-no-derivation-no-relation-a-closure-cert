#!/usr/bin/env python3
"""
Optional SECONDARY generality arm: the Allen Interval Algebra.

The 13x13 composition table is DERIVED programmatically from the convex point
algebra over the four interval endpoints (6-point path-consistency), then
SELF-VERIFIED against canonical entries (equals is the identity; precedes o
precedes = precedes; precedes o preceded-by = universal; converse involution;
r o conv(r) contains equals). If any check fails, the caller DROPS this arm.

We then re-run the H4 redundancy curve on Allen networks (richer 13-relation
gradient => smoother inverted-U). Path-consistency is SOUND but INCOMPLETE for
the full Allen algebra, so the closure-detected contradiction rate is reported
as a LOWER BOUND; the convex point arm remains the exact deliverable.
"""
from __future__ import annotations
import numpy as np

# Reuse the verified convex point algebra + closure from method.py
from method import (LT, EQ, GT, U as PU, EMPTY as PEMPTY, COMP as PCOMP, CONV as PCONV,
                    closure_FULL as point_closure, CORRECT, WRONG, ABSTAIN, COLLAPSE,
                    boot_diff_ci, boot_mean_ci)

ALLEN_NAMES = ["p", "m", "o", "F", "D", "s", "e", "S", "d", "f", "O", "M", "P"]
NREL = 13
AU = (1 << NREL) - 1          # universal (all 13 bits)
AEMPTY = 0

# endpoint sign patterns (sign(a0,b0), sign(a0,b1), sign(a1,b0), sign(a1,b1))
PATTERNS = {
    "p": (LT, LT, LT, LT), "m": (LT, LT, EQ, LT), "o": (LT, LT, GT, LT),
    "F": (LT, LT, GT, EQ), "D": (LT, LT, GT, GT), "s": (EQ, LT, GT, LT),
    "e": (EQ, LT, GT, EQ), "S": (EQ, LT, GT, GT), "d": (GT, LT, GT, LT),
    "f": (GT, LT, GT, EQ), "O": (GT, LT, GT, GT), "M": (GT, EQ, GT, GT),
    "P": (GT, GT, GT, GT),
}
PAT2IDX = {PATTERNS[n]: i for i, n in enumerate(ALLEN_NAMES)}
IDX = {n: i for i, n in enumerate(ALLEN_NAMES)}


def _point_net_from_patterns(pat_ab, pat_bc, pat_ac):
    """6-point convex-point matrix: a0=0,a1=1,b0=2,b1=3,c0=4,c1=5."""
    M = [[PU] * 6 for _ in range(6)]
    for x in range(6):
        M[x][x] = EQ

    def setrel(i, j, r):
        M[i][j] = r
        M[j][i] = PCONV[r]
    # interval validity
    setrel(0, 1, LT); setrel(2, 3, LT); setrel(4, 5, LT)
    if pat_ab is not None:
        setrel(0, 2, pat_ab[0]); setrel(0, 3, pat_ab[1]); setrel(1, 2, pat_ab[2]); setrel(1, 3, pat_ab[3])
    if pat_bc is not None:
        setrel(2, 4, pat_bc[0]); setrel(2, 5, pat_bc[1]); setrel(3, 4, pat_bc[2]); setrel(3, 5, pat_bc[3])
    if pat_ac is not None:
        setrel(0, 4, pat_ac[0]); setrel(0, 5, pat_ac[1]); setrel(1, 4, pat_ac[2]); setrel(1, 5, pat_ac[3])
    return M


def derive_allen_tables():
    """Return (ACOMP, ACONV) as 13x... bit tables, or raise on self-verify failure."""
    # converse
    ACONV = [0] * NREL
    for n in ALLEN_NAMES:
        s00, s01, s10, s11 = PATTERNS[n]
        conv_pat = (PCONV[s00], PCONV[s10], PCONV[s01], PCONV[s11])
        ACONV[IDX[n]] = 1 << PAT2IDX[conv_pat]
    # composition of base relations via 6-point closure feasibility
    base_comp = [[0] * NREL for _ in range(NREL)]
    for r1 in ALLEN_NAMES:
        for r2 in ALLEN_NAMES:
            mask = 0
            for r3 in ALLEN_NAMES:
                M = _point_net_from_patterns(PATTERNS[r1], PATTERNS[r2], PATTERNS[r3])
                status, _ = point_closure(M, 6)
                if status != "COLLAPSE":
                    mask |= (1 << IDX[r3])
            base_comp[IDX[r1]][IDX[r2]] = mask

    def acompose(r, s):
        m = 0
        for a in range(NREL):
            if r & (1 << a):
                for b in range(NREL):
                    if s & (1 << b):
                        m |= base_comp[a][b]
        return m

    def aconv(r):
        m = 0
        for a in range(NREL):
            if r & (1 << a):
                m |= ACONV[a]
        return m

    # ---- SELF-VERIFY canonical entries ----
    p, m, o, e, P = (1 << IDX[x] for x in ("p", "m", "o", "e", "P"))
    assert base_comp[IDX["p"]][IDX["p"]] == p, "p.p must be {p}"
    assert base_comp[IDX["p"]][IDX["m"]] == p, "p.m must be {p}"
    assert base_comp[IDX["m"]][IDX["m"]] == p, "m.m must be {p}"
    assert base_comp[IDX["p"]][IDX["P"]] == AU, "p.P must be universal"
    # equals is the composition identity
    for r in range(NREL):
        assert base_comp[IDX["e"]][r] == (1 << r), "e is identity"
        assert base_comp[r][IDX["e"]] == (1 << r), "e is identity"
    # converse involution
    for r in range(NREL):
        assert aconv(aconv(1 << r)) == (1 << r), "conv involution"
    # r o conv(r) contains equals
    for r in range(NREL):
        assert acompose(1 << r, ACONV[r]) & e, "r.conv(r) contains e"
    return base_comp, ACONV, acompose, aconv


def _closure_generic(M, n, base_comp, aconv_arr):
    """Path-consistency on Allen bitmask matrix (sound, incomplete for full Allen)."""
    def comp(r, s):
        out = 0
        for a in range(NREL):
            if r & (1 << a):
                row = base_comp[a]
                for b in range(NREL):
                    if s & (1 << b):
                        out |= row[b]
        return out

    def conv(r):
        out = 0
        for a in range(NREL):
            if r & (1 << a):
                out |= aconv_arr[a]
        return out

    changed = True
    while changed:
        changed = False
        for k in range(n):
            for i in range(n):
                if i == k or M[i][k] == AU:
                    continue
                for j in range(n):
                    if j == i or j == k or M[k][j] == AU:
                        continue
                    new = M[i][j] & comp(M[i][k], M[k][j])
                    if new != M[i][j]:
                        M[i][j] = new
                        M[j][i] = conv(new)
                        if new == AEMPTY:
                            return "COLLAPSE", M
                        changed = True
    return "OK", M


# Allen reader: gold relation = precedes ('p'); sound supersets contain p along
# the conceptual-neighbour chain p-m-o; unsound sets exclude p.
P_BIT = 1 << IDX["p"]
SOUND_OPTS = [P_BIT, P_BIT | (1 << IDX["m"]), P_BIT | (1 << IDX["m"]) | (1 << IDX["o"]), AU]
UNSOUND_OPTS = [1 << IDX["m"], 1 << IDX["o"], 1 << IDX["d"], 1 << IDX["e"], 1 << IDX["s"]]


def simulate_allen_R(K, r, rho, n_net, seed, breadth_w, base_comp, ACONV):
    rng = np.random.default_rng(seed)
    from scipy.stats import norm
    qn = norm.ppf(min(max(r, 1e-9), 1 - 1e-9))
    correct = np.zeros(n_net, bool); wrong = np.zeros(n_net, bool)
    collapse = np.zeros(n_net, bool); all_sound = np.zeros(n_net, bool)
    sq_rho = np.sqrt(rho); sq_1 = np.sqrt(1 - rho)
    for t in range(n_net):
        nnode = 2 + K
        M = [[AU] * nnode for _ in range(nnode)]
        for x in range(nnode):
            M[x][x] = 1 << IDX["e"]
        u = rng.standard_normal()
        snd_flags = []
        for k in range(K):
            mk = 2 + k
            for (a, b) in ((0, mk), (mk, 1)):       # both edges gold 'precedes'
                z = sq_rho * u + sq_1 * rng.standard_normal()
                is_sound = z <= qn
                snd_flags.append(is_sound)
                if is_sound:
                    s_e = int(rng.choice(SOUND_OPTS, p=breadth_w))
                else:
                    s_e = int(rng.choice(UNSOUND_OPTS))
                M[a][b] = s_e
                # converse
                cv = 0
                for ai in range(NREL):
                    if s_e & (1 << ai):
                        cv |= ACONV[ai]
                M[b][a] = cv
        status, M = _closure_generic(M, nnode, base_comp, ACONV)
        all_sound[t] = all(snd_flags)
        if status == "COLLAPSE":
            collapse[t] = True
            continue
        rq = M[0][1]
        if rq == AEMPTY:
            collapse[t] = True
        elif bin(rq).count("1") == 1:
            if rq == P_BIT:
                correct[t] = True
            else:
                wrong[t] = True
        # else abstain
    return {"correct": correct, "wrong": wrong, "collapse": collapse, "all_sound": all_sound}


def run_allen_arm(cfg, point_pass):
    if not point_pass:
        return {"status": "skipped", "reason": "gated behind point-algebra PASS"}
    try:
        base_comp, ACONV, _, _ = derive_allen_tables()      # validates the table
    except AssertionError as e:
        return {"status": "dropped", "reason": f"composition-table self-verify failed: {e}"}

    # vaguer reads ({p} rarely a singleton) so redundancy is NEEDED to narrow,
    # exposing the inverted-U more clearly on the richer 13-relation gradient.
    breadth_w = np.array([0.20, 0.40, 0.25, 0.15]); breadth_w = breadth_w / breadth_w.sum()
    Ks = cfg["K"]
    recalls = [0.6, 0.9]
    rho = 0.5
    n_net = min(cfg["N"], 400)
    rng = np.random.default_rng(424242)
    curves = []
    cell = {}
    for r in recalls:
        for k in Ks:
            seed = int((424242 + (int(r * 100) * 1000 + k)) % (2 ** 32))
            out = simulate_allen_R(k, r, rho, n_net, seed, breadth_w, base_comp, ACONV)
            ben = float(out["correct"].mean()); cst = float(out["wrong"].mean())
            col = float(out["collapse"].mean()); je = float(out["all_sound"].mean())
            curves.append({"recall": r, "K": k, "benefit": ben, "cost": cst,
                           "collapse_rate_lower_bound": col, "net": ben - cst,
                           "J_E": je, "n": n_net})
            cell[(r, k)] = out

    # inverted-U on benefit at the low-recall arm
    inv = {}
    for r in recalls:
        b = np.array([cell[(r, k)]["correct"].mean() for k in Ks])
        pk = int(np.argmax(b))
        interior = 0 < pk < len(Ks) - 1
        d_rise, rl, _ = boot_diff_ci(cell[(r, Ks[pk])]["correct"], cell[(r, Ks[0])]["correct"], 800, rng)
        d_fall, fl, _ = boot_diff_ci(cell[(r, Ks[pk])]["correct"], cell[(r, Ks[-1])]["correct"], 800, rng)
        inv[f"{r:.2f}"] = {"peak_K": int(Ks[pk]), "interior": bool(interior),
                           "rises": bool(rl > 0), "falls": bool(fl > 0),
                           "inverted_U": bool(interior and rl > 0 and fl > 0)}
    # zero-FP on Allen: all-sound -> never collapse, never wrong (lower-bound certificate)
    asc = 0; asn = 0; asw = 0
    for r in recalls:
        for k in Ks:
            m = cell[(r, k)]["all_sound"]
            asn += int(m.sum())
            asc += int(cell[(r, k)]["collapse"][m].sum())
            asw += int(cell[(r, k)]["wrong"][m].sum())
    return {
        "status": "ok", "exploratory": True, "algebra": "allen_interval_13",
        "table_derivation": "6-point convex-point path-consistency; self-verified",
        "note": ("PC is sound-but-incomplete for full Allen; collapse rates are a LOWER "
                 "BOUND on detectable contradictions. The convex point arm is exact."),
        "n_per_cell": n_net, "rho": rho, "recalls": recalls,
        "curves": curves, "inverted_U": inv,
        "zero_FP_all_sound": {"n_all_sound": asn, "collapse_when_all_sound": asc,
                              "wrong_when_all_sound": asw,
                              "certificate_holds": bool(asc == 0 and asw == 0)},
    }
