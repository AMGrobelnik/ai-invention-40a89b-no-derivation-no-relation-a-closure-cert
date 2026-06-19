#!/usr/bin/env python3
"""Statistics for the matched-coverage selective-accuracy showdown.

* matched_coverage_set        -- pick a method's covered set at a TARGET coverage c* by
                                 ranking on its abstention score (top-K by confidence).
* selective_accuracy          -- accuracy among the covered set.
* paired_bootstrap_gap        -- 95% CI + one-sided p for selacc(ModeA) - selacc(baseline)
                                 resampling NETWORKS (paired across methods); the covered-set
                                 membership is FIXED on the full sample (fixed-tau, primary),
                                 with an optional re-matched-per-resample sensitivity.
* holm_bonferroni             -- step-down adjustment of a p-value family.
* page_test / jonckheere / spearman_boot_ci -- monotone-trend tests for H3 (reused from the
                                 iter-1 experiment_2 statistics).
* icc_oneway                  -- within-document soundness correlation rho.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.stats import norm, spearmanr

try:
    from scipy.stats import page_trend_test as _scipy_page
    _HAS_SCIPY_PAGE = True
except Exception:
    _HAS_SCIPY_PAGE = False


# --------------------------------------------------------------------------- #
# Matched-coverage selective accuracy
# --------------------------------------------------------------------------- #
def matched_coverage_mask(conf: np.ndarray, target_cov: float) -> np.ndarray:
    """Boolean mask covering the top ceil(target_cov * N) networks by confidence.

    Rank-based (handles discrete/degenerate confidences gracefully): ties broken by index
    so the choice is deterministic. Returns an all-False mask if target_cov<=0."""
    n = len(conf)
    k = int(round(target_cov * n))
    k = max(0, min(n, k))
    mask = np.zeros(n, dtype=bool)
    if k == 0:
        return mask
    # argsort by (-conf, index): highest confidence first, stable
    order = sorted(range(n), key=lambda i: (-conf[i], i))
    for i in order[:k]:
        mask[i] = True
    return mask


def selective_accuracy(correct: np.ndarray, mask: np.ndarray) -> float:
    cov = int(mask.sum())
    if cov == 0:
        return float("nan")
    return float(correct[mask].sum() / cov)


def paired_bootstrap_gap(correct_a: np.ndarray, mask_a: np.ndarray,
                         correct_b: np.ndarray, conf_b: np.ndarray, target_cov: float,
                         B: int = 2000, seed: int = 20260617, alpha: float = 0.05,
                         rematch: bool = False):
    """Paired bootstrap of selacc(A) - selacc(B) at matched coverage c*.

    A is the reference method whose covered set (mask_a) defines c*. B is thresholded to c*.
    PRIMARY (rematch=False): fix mask_b on the full sample (fixed covered-set membership) and
    resample networks. SENSITIVITY (rematch=True): re-rank B inside each resample.
    Returns dict: point gap, ci95, p_one_sided (P(gap*<=0)), selacc_a, selacc_b, cov_a, cov_b.
    """
    correct_a = np.asarray(correct_a, float)
    correct_b = np.asarray(correct_b, float)
    conf_b = np.asarray(conf_b, float)
    n = len(correct_a)
    mask_b0 = matched_coverage_mask(conf_b, target_cov)
    sa = selective_accuracy(correct_a, mask_a)
    sb = selective_accuracy(correct_b, mask_b0)
    point = sa - sb
    rng = np.random.default_rng(seed)
    gaps = []
    for _ in range(B):
        idx = rng.integers(0, n, n)
        ca = correct_a[idx]; ma = mask_a[idx]
        cb = correct_b[idx]
        if rematch:
            mb = matched_coverage_mask(conf_b[idx], target_cov)
        else:
            mb = mask_b0[idx]
        sai = selective_accuracy(ca, ma)
        sbi = selective_accuracy(cb, mb)
        if sai == sai and sbi == sbi:
            gaps.append(sai - sbi)
    gaps = np.array(gaps, float)
    if len(gaps) < 10:
        return {"gap": point, "ci95": [float("nan"), float("nan")], "p_one_sided": float("nan"),
                "selacc_a": sa, "selacc_b": sb, "cov_a": float(mask_a.mean()),
                "cov_b": float(mask_b0.mean()), "n_boot": len(gaps)}
    lo, hi = np.quantile(gaps, [alpha / 2, 1 - alpha / 2])
    p_one = float(np.mean(gaps <= 0.0))  # evidence against a positive gap
    return {"gap": float(point), "ci95": [float(lo), float(hi)], "p_one_sided": p_one,
            "selacc_a": float(sa), "selacc_b": float(sb),
            "cov_a": float(mask_a.mean()), "cov_b": float(mask_b0.mean()),
            "n_boot": int(len(gaps))}


def bonferroni_ci(correct_a, mask_a, correct_b, conf_b, target_cov, m_family,
                  B=2000, seed=20260617, alpha=0.05, rematch=False):
    """Family-wise (Bonferroni) CI at level 1 - alpha/m_family for one comparison."""
    a2 = alpha / max(1, m_family)
    return paired_bootstrap_gap(correct_a, mask_a, correct_b, conf_b, target_cov,
                                B=B, seed=seed, alpha=a2, rematch=rematch)["ci95"]


# --------------------------------------------------------------------------- #
# Holm-Bonferroni
# --------------------------------------------------------------------------- #
def holm_bonferroni(pvals: dict, alpha: float = 0.05):
    """Step-down Holm adjustment. pvals: {name: p}. Returns {name: {p, p_adj, reject}}."""
    items = sorted(pvals.items(), key=lambda kv: (float("inf") if kv[1] != kv[1] else kv[1]))
    m = len(items)
    out = {}
    prev_adj = 0.0
    still_rejecting = True
    for rank, (name, p) in enumerate(items):
        if p != p:  # nan
            out[name] = {"p": p, "p_adj": float("nan"), "reject": False}
            still_rejecting = False
            continue
        adj = min(1.0, (m - rank) * p)
        adj = max(adj, prev_adj)  # enforce monotonicity
        prev_adj = adj
        reject = still_rejecting and (adj <= alpha)
        if not reject:
            still_rejecting = False
        out[name] = {"p": float(p), "p_adj": float(adj), "reject": bool(reject)}
    return out


# --------------------------------------------------------------------------- #
# Within-document soundness correlation (ICC one-way)
# --------------------------------------------------------------------------- #
def icc_oneway(groups):
    """One-way random-effects ICC(1) of a 0/1 indicator grouped by document."""
    groups = [list(g) for g in groups if len(g) >= 2]
    if len(groups) < 2:
        return None
    N = sum(len(g) for g in groups)
    k = len(groups)
    grand = sum(sum(g) for g in groups) / N
    ms_between = sum(len(g) * (np.mean(g) - grand) ** 2 for g in groups) / (k - 1)
    ss_within = sum(sum((x - np.mean(g)) ** 2 for x in g) for g in groups)
    ms_within = ss_within / (N - k) if N > k else 0.0
    sum_n2 = sum(len(g) ** 2 for g in groups)
    n0 = (N - sum_n2 / N) / (k - 1)
    denom = ms_between + (n0 - 1) * ms_within
    if denom == 0:
        return 0.0
    return float((ms_between - ms_within) / denom)


def clustered_bootstrap_ci(doc_to_vals, B=1000, seed=20260617, alpha=0.05):
    """95% CI for the pooled mean of a 0/1 indicator, resampling DOCUMENTS."""
    docs = [d for d, v in doc_to_vals.items() if v]
    if len(docs) < 2:
        allv = [x for v in doc_to_vals.values() for x in v]
        m = float(np.mean(allv)) if allv else float("nan")
        return [m, m]
    rng = np.random.default_rng(seed)
    arrs = {d: np.array(doc_to_vals[d], dtype=float) for d in docs}
    means, nd = [], len(docs)
    for _ in range(B):
        pick = rng.integers(0, nd, nd)
        vals = np.concatenate([arrs[docs[i]] for i in pick])
        means.append(vals.mean())
    lo, hi = np.quantile(means, [alpha / 2, 1 - alpha / 2])
    return [float(lo), float(hi)]


def mean_ci(x, B=2000, seed=20260617, alpha=0.05):
    x = np.asarray(x, float)
    if len(x) == 0:
        return float("nan"), [float("nan"), float("nan")]
    rng = np.random.default_rng(seed)
    bs = x[rng.integers(0, len(x), size=(B, len(x)))].mean(1)
    lo, hi = np.quantile(bs, [alpha / 2, 1 - alpha / 2])
    return float(x.mean()), [float(lo), float(hi)]


# --------------------------------------------------------------------------- #
# Monotone-trend tests (H3): Page / Jonckheere / Spearman-boot
# --------------------------------------------------------------------------- #
def page_trend_manual(matrix):
    data = np.asarray(matrix, float)
    n, k = data.shape
    ranks = np.zeros_like(data)
    for srow in range(n):
        order = np.argsort(data[srow], kind="mergesort")
        rr = np.empty(k)
        rr[order] = np.arange(1, k + 1)
        row = data[srow]
        for v in np.unique(row):
            mask = row == v
            if mask.sum() > 1:
                rr[mask] = rr[mask].mean()
        ranks[srow] = rr
    Rj = ranks.sum(axis=0)
    js = np.arange(1, k + 1)
    Lstat = float((js * Rj).sum())
    EL = n * k * (k + 1) ** 2 / 4.0
    VL = n * (k ** 2) * (k ** 2 - 1) * (k + 1) / 144.0
    z = (Lstat - EL) / math.sqrt(VL) if VL > 0 else 0.0
    p = float(1.0 - norm.cdf(z))
    return Lstat, z, p


def page_test(matrix):
    """Page's L for an ordered (non-decreasing) alternative. matrix=(subjects, conditions)."""
    if _HAS_SCIPY_PAGE:
        try:
            res = _scipy_page(np.asarray(matrix, float), ranked=False)
            return float(res.statistic), float(res.pvalue)
        except Exception:
            pass
    L, z, p = page_trend_manual(matrix)
    return L, p


def jonckheere(groups):
    """Jonckheere-Terpstra (sum of pairwise Mann-Whitney U across ordered groups)."""
    ns = [len(g) for g in groups]
    N = sum(ns)
    k = len(groups)
    JT = 0.0
    for a in range(k):
        for b in range(a + 1, k):
            x = np.asarray(groups[a], float)
            y = np.sort(np.asarray(groups[b], float))
            right = np.searchsorted(y, x, side="right")
            left = np.searchsorted(y, x, side="left")
            gt = (len(y) - right).sum()
            eq = (right - left).sum()
            JT += gt + 0.5 * eq
    mean = (N ** 2 - sum(nn * nn for nn in ns)) / 4.0
    var = (N ** 2 * (2 * N + 3) - sum(nn * nn * (2 * nn + 3) for nn in ns)) / 72.0
    z = (JT - mean) / math.sqrt(var) if var > 0 else 0.0
    p = float(1.0 - norm.cdf(z))
    return float(JT), float(z), p


def spearman_boot_ci(xs, ys_samples, B=2000, seed=20260617, alpha=0.05):
    """Spearman(level, gap) with bootstrap CI. ys_samples: list of per-level arrays of
    per-network gap contributions. Resamples networks within each level."""
    xs = np.asarray(xs, float)
    rng = np.random.default_rng(seed)
    means = np.array([np.mean(s) if len(s) else 0.0 for s in ys_samples])
    if len(xs) < 3:
        return float("nan"), float("nan"), float("nan")
    rho_point = float(spearmanr(xs, means).statistic)
    boot = np.empty(B)
    for bi in range(B):
        bm = np.array([s[rng.integers(0, len(s), len(s))].mean() if len(s) else 0.0
                       for s in ys_samples])
        bm = bm + rng.normal(0, 1e-9, size=bm.shape)
        boot[bi] = spearmanr(xs, bm).statistic
    boot = boot[~np.isnan(boot)]
    if len(boot) == 0:
        return rho_point, float("nan"), float("nan")
    lo, hi = np.quantile(boot, [alpha / 2, 1 - alpha / 2])
    return rho_point, float(lo), float(hi)


def tv_distance(p, q):
    keys = set(p) | set(q)
    return 0.5 * sum(abs(p.get(k, 0) - q.get(k, 0)) for k in keys)
