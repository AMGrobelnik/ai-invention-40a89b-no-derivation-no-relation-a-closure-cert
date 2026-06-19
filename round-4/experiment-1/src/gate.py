#!/usr/bin/env python3
"""STEP 1 -- a-priori multi-path gate (ZERO LLM). Build the eligible query set on the
FROZEN real gold graphs and decide GO / NO-GO BEFORE any LLM spend.

A query edge (s,t) is MULTIPATH-REDUNDANT-WITH-BITE iff, using SOUND gold sets along
>=2 edge-disjoint constraining paths,
   |best_single_path_composition| >= 2  AND  full-PC intersection STRICT subset of it
   AND  canonical (atomic) query gold subset of the intersection (soundness).
The HEADLINE subset additionally requires the canonical query gold to be a SINGLETON
(so 'singleton-resolution-to-correct' is well-defined). MATRES (point algebra) is reported
as gate-discriminativeness validation (expected ~0).
"""
from __future__ import annotations

import math
from collections import Counter, defaultdict

import numpy as np

import data_adapter as DA
import engine
from allen_layer import AL, canon_allen, gold_dir, sound_allen

VIA_CAP = 10          # max vias (length-2 disjoint paths) per query used for reads+closure
HEADLINE_GO_N = 100   # pre-registered GO threshold on combined gold-singleton eligible N


def _induced_edges(by_pair, s, t, vias):
    """All informative-gold induced edges among {s,t}+vias EXCEPT the held-out query (s,t).
    Returns (path_edges:list[(a,b)], has_via_via:bool)."""
    nodes = [s, t] + list(vias)
    path_edges = []
    has_via_via = False
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            a, b = nodes[i], nodes[j]
            if {a, b} == {s, t}:
                continue
            key = tuple(sorted((a, b)))
            if key not in by_pair:
                continue
            g = gold_dir(by_pair, a, b, sound_allen)
            if g in (None, "BADTOK") or len(g) >= 13:
                continue
            path_edges.append((a, b))
            if a in vias and b in vias:
                has_via_via = True
    return path_edges, has_via_via


def _gold_closure(by_pair, s, t, vias, path_edges):
    """Build the gold sound QCN over the induced subgraph (query held at universe), run
    PC-2, return (best_single_set, inter_set, collapsed)."""
    nodes = [s, t] + list(vias)
    qcn = engine.QCN(AL, nodes)
    for (a, b) in path_edges:
        g = gold_dir(by_pair, a, b, sound_allen)
        qcn.set_edge(qcn.index[a], qcn.index[b], g)
    # single-path (length-2) gold compositions per via
    singles = []
    for w in vias:
        gsw = gold_dir(by_pair, s, w, sound_allen)
        gwt = gold_dir(by_pair, w, t, sound_allen)
        if gsw in (None, "BADTOK") or gwt in (None, "BADTOK"):
            continue
        singles.append(AL.compose(gsw, gwt))
    if not singles:
        return None, None, False
    best_single = min(singles, key=len)
    qi, qj = qcn.index[s], qcn.index[t]
    ok, _ = engine.pc2_full(qcn)
    inter = qcn.get(qi, qj) if ok else AL.empty
    return best_single, inter, (not ok)


def build_corpus_gate(corpus, docs, via_cap=VIA_CAP):
    """Enumerate eligible multipath queries for one corpus. Returns (queries, stats)."""
    queries = []
    n_eval = n_have2 = 0
    bites = []
    head_bites = []
    n_singres = n_ge3 = 0
    viol_inter = 0
    inter_tighter_than_direct = 0
    n_paths_dist = []
    for docid, d in docs.items():
        by_pair = {}
        adj = defaultdict(set)
        for ed in d["edges"]:
            key = tuple(sorted((ed["u"], ed["v"])))
            if key in by_pair:
                continue
            sg = sound_allen(ed)
            if sg in (None, "BADTOK"):
                continue
            by_pair[key] = ed
            if len(sg) < 13:
                adj[ed["u"]].add(ed["v"]); adj[ed["v"]].add(ed["u"])
        for ed in d["edges"]:
            if not ed["deduction_required"]:
                continue
            s, t = ed["u"], ed["v"]
            cq = gold_dir(by_pair, s, t, canon_allen)
            sq = gold_dir(by_pair, s, t, sound_allen)
            if cq in (None, "BADTOK") or len(cq) >= 13:
                continue
            if s not in adj or t not in adj:
                continue
            vias = sorted((adj[s] & adj[t]) - {s, t})
            if len(vias) < 2:
                n_eval += 1
                continue
            vias = vias[:via_cap]
            path_edges, has_via_via = _induced_edges(by_pair, s, t, vias)
            best_single, inter, collapsed = _gold_closure(by_pair, s, t, vias, path_edges)
            n_eval += 1
            if best_single is None:
                continue
            n_have2 += 1
            if not (cq <= inter):
                viol_inter += 1
            if sq is not None and inter < sq:
                inter_tighter_than_direct += 1
            is_mp = (len(best_single) >= 2) and (inter < best_single) and (cq <= inter)
            if not is_mp:
                continue
            bite = len(best_single) - len(inter)
            bites.append(bite)
            gold_is_singleton = (len(cq) == 1)
            singleton_resolvable = (len(inter) == 1 and inter == cq)
            if singleton_resolvable:
                n_singres += 1
            stratum = "ge3" if has_via_via else "len2"
            if stratum == "ge3":
                n_ge3 += 1
            n_paths_dist.append(len(vias))
            if gold_is_singleton:
                head_bites.append(bite)
            queries.append({
                "corpus": corpus, "docid": docid, "s": s, "t": t, "vias": vias,
                "path_edges": path_edges, "has_via_via": has_via_via, "stratum": stratum,
                "gold_canon": sorted(cq), "gold_is_singleton": gold_is_singleton,
                "gold_best_single": sorted(best_single), "gold_inter": sorted(inter),
                "gold_bite": bite, "gold_singleton_resolvable": singleton_resolvable,
                "n_disjoint_paths": len(vias),
            })
    n_head = sum(1 for q in queries if q["gold_is_singleton"])
    stats = {
        "n_eval_deduction_required": n_eval,
        "n_with_ge2_disjoint_paths": n_have2,
        "n_multipath_with_bite": len(queries),
        "n_gold_singleton_headline": n_head,
        "n_singleton_resolvable": n_singres,
        "n_ge3_stratum": n_ge3,
        "n_len2_stratum": len(queries) - n_ge3,
        "inter_not_superset_canon_excluded": viol_inter,
        "inter_strictly_tighter_than_direct_annotation": inter_tighter_than_direct,
        "bite_mean": float(np.mean(bites)) if bites else 0.0,
        "bite_median": float(np.median(bites)) if bites else 0.0,
        "bite_hist": dict(sorted(Counter(bites).items())),
        "headline_bite_hist": dict(sorted(Counter(head_bites).items())),
        "n_disjoint_paths_mean": float(np.mean(n_paths_dist)) if n_paths_dist else 0.0,
        "docs_covered": len({q["docid"] for q in queries}),
    }
    return queries, stats


def mde_paired_proportion(n, p_discordant=0.30, alpha=0.05, power=0.80, deff=1.5):
    """A-priori minimum detectable difference in singleton-resolution rate for a paired
    (McNemar) design at the given power, inflated by a doc-clustering design effect.

    p_discordant = assumed fraction of queries where the two methods disagree on
    resolution (intersection resolves, best-single does not). Returns the minimum
    detectable proportion-difference."""
    from scipy.stats import norm
    if n <= 0:
        return float("nan")
    z_a = norm.ppf(1 - alpha / 2)
    z_b = norm.ppf(power)
    n_eff = n / max(deff, 1e-9)
    # McNemar: detectable difference d ~ (z_a+z_b)*sqrt(p_disc)/sqrt(n_eff)
    d = (z_a + z_b) * math.sqrt(max(p_discordant, 1e-6)) / math.sqrt(n_eff)
    return float(min(1.0, d))


def run_gate(dataset_path=None, via_cap=VIA_CAP, limit_docs=None, cache_dir=None):
    """Run STEP 1 over all corpora. Returns dict with per-corpus stats, the eligible query
    lists, the gate decision, and the docs (for downstream read materialization).

    The (expensive) per-corpus ENUMERATION (queries+stats) is cached to JSON keyed by
    (via_cap, limit_docs); docs are always rebuilt (cheap) so reads can be materialized."""
    import json as _json
    from pathlib import Path as _Path
    by_corpus = defaultdict(list)
    for (corpus, docid, text, G) in DA.load_dataset(dataset_path or DA.DEFAULT_DATASET):
        by_corpus[corpus].append((docid, text, G))

    cache_dir = _Path(cache_dir) if cache_dir else _Path(__file__).parent / "gate_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    ckey = cache_dir / f"gate_enum_vc{via_cap}_ld{limit_docs}.json"
    cached = None
    if ckey.exists():
        try:
            cached = _json.loads(ckey.read_text())
        except Exception:
            cached = None

    out = {"per_corpus": {}, "queries": {}, "docs": {}}
    enum_store = {}
    for corpus in ("narrativetime", "tddman"):
        rows = by_corpus.get(corpus, [])
        docs, off = DA.build_corpus(corpus, rows, max_docs=limit_docs)
        out["docs"][corpus] = docs
        if cached and corpus in cached.get("queries", {}):
            queries = [{**q, "path_edges": [tuple(e) for e in q["path_edges"]]}
                       for q in cached["queries"][corpus]]
            stats = cached["per_corpus"][corpus]
        else:
            queries, stats = build_corpus_gate(corpus, docs, via_cap=via_cap)
            stats["offset_alignment_fraction"] = off
        out["per_corpus"][corpus] = stats
        out["queries"][corpus] = queries
        enum_store[corpus] = queries
    if not cached:
        try:
            ckey.write_text(_json.dumps({"per_corpus": out["per_corpus"], "queries": enum_store}))
        except Exception:
            pass

    # MATRES validation (point algebra -> Allen token map fails -> 0; report structural)
    matres_rows = by_corpus.get("matres", [])
    m_docs, _ = DA.build_corpus("matres", matres_rows, max_docs=limit_docs)
    m_dedreq_multipath = 0
    for docid, d in m_docs.items():
        by_pair = {tuple(sorted((e["u"], e["v"]))): e for e in d["edges"]}
        adj = defaultdict(set)
        for e in d["edges"]:
            adj[e["u"]].add(e["v"]); adj[e["v"]].add(e["u"])
        for ed in d["edges"]:
            if not ed["deduction_required"]:
                continue
            vias = (adj[ed["u"]] & adj[ed["v"]]) - {ed["u"], ed["v"]}
            if len(vias) >= 2:
                m_dedreq_multipath += 1
    out["matres_validation"] = {
        "n_deduction_required_multipath_structural": m_dedreq_multipath,
        "allen_token_mappable": False,
        "note": "MATRES is point-algebra start-point gold (tokens <,=,>; not Allen) and "
                "intra/adjacent only -> deduction envelope ~empty. Expected ~0; confirms the "
                "gate is discriminative (does not fire on a corpus with no multi-path structure).",
        "tag": "GOLD-ONLY-GATE",
    }

    combined_head = (out["per_corpus"]["narrativetime"]["n_gold_singleton_headline"]
                     + out["per_corpus"]["tddman"]["n_gold_singleton_headline"])
    decision = "GO" if combined_head >= HEADLINE_GO_N else "NO-GO"
    power_table = {str(n): mde_paired_proportion(n) for n in (50, 100, 150, 200)}
    out["combined_headline_eligible_N"] = combined_head
    out["headline_go_threshold"] = HEADLINE_GO_N
    out["gate_decision"] = decision
    out["power_mde_table"] = power_table
    out["via_cap"] = via_cap
    out["tag"] = "GOLD-ONLY-GATE"
    return out


if __name__ == "__main__":
    import json
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    g = run_gate(limit_docs=limit)
    print(json.dumps({"per_corpus": g["per_corpus"], "matres": g["matres_validation"],
                      "combined_headline_eligible_N": g["combined_headline_eligible_N"],
                      "gate_decision": g["gate_decision"],
                      "power_mde_table": g["power_mde_table"]}, indent=2))
