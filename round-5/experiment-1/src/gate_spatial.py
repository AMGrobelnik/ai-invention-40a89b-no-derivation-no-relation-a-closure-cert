#!/usr/bin/env python3
"""STEP 1 -- a-priori multi-path gate (ZERO LLM) for the SPATIAL venue.

Decides GO / LOW-POWER / NO-GO BEFORE any LLM spend, SEPARATELY for the RCC-8 (topological)
and the CARDINAL (directional, CDC) arms, on the frozen SpaRP-PS1 + SpartQA-Human gold
graphs -- using VERIFIED COMPOSITION (not the corpus's purely-structural undirected flag).

A query (s,t) is MULTIPATH-WITH-BITE in algebra X iff, on the X-ONLY subgraph (root '-1'
excluded), it is NOT directly stated AND has >=2 edge-disjoint constraining paths each
length 2..L AND, composing X-gold along those paths, |best_single_path| >= 2 (non-singleton)
AND full intersection STRICT subset of best_single AND query-gold subset of the intersection
(soundness). HEADLINE additionally requires query-gold to be a SINGLETON.

The cascade is reported in FULL (best_single_len_hist etc.) so a NO-GO is causally
attributed (e.g. 'short cardinal paths already compose to singletons' / 'RCC-8 subgraph is a
containment tree') rather than asserted.
"""
from __future__ import annotations

from collections import Counter

import networkx as nx

import engine
import rcc8_layer as RL
import spatial_adapter as SA

RCC8 = engine.build_rcc8_algebra()
CDC = engine.build_cardinal_algebra()

# algebra registry: (gold_algebra_string, engine_algebra, subgraph_builder, gold_canon_fn)
ALGEBRAS = {
    "rcc8": (RCC8, SA.build_rcc8_subgraph, RL.canon_rcc8_set),
    "cardinal_direction": (CDC, SA.build_cardinal_subgraph, RL.canon_cdc_set),
}
SHORT_MAX = 4          # 'tight' path-length ceiling
HEADLINE_GO_N = 100
LOW_POWER_N = 40


def _compose_path(alg, by_pair, path):
    R = None
    for a, b in zip(path[:-1], path[1:]):
        g = SA.dgold(alg.converse, by_pair, a, b)
        if g is None:
            return None
        R = g if R is None else alg.compose(R, g)
        if not R:
            return alg.empty
    return R


def gate_arm(ds_name, algebra_key, short_max=SHORT_MAX, collect_eligible=True):
    alg, build_sub, canon_fn = ALGEBRAS[algebra_key]
    st = {"corpus": ds_name, "algebra": algebra_key, "n_scenes": 0, "n_query_gold": 0,
          "n_deduction_required": 0, "n_ge2_short_paths": 0,
          "best_single_len_hist": Counter(), "inter_len_hist": Counter(),
          "n_best_single_nonsingleton": 0, "n_inter_strict_subset_best": 0,
          "n_gold_subset_inter": 0, "n_multipath_with_bite": 0,
          "n_headline_gold_singleton": 0, "n_ge3_cyclic": 0,
          "bite_hist": Counter(), "headline_bite_hist": Counter(),
          "maxdisjoint_hist": Counter()}
    eligible = []
    for docid, story, G in SA.load_spatial(ds_name):
        st["n_scenes"] += 1
        q = G["query_edge"]
        if q.get("gold_algebra") != algebra_key:
            continue
        gold = canon_fn(q.get("gold_canonical", []))
        if not gold:
            continue
        st["n_query_gold"] += 1
        s, t = q["src"], q["dst"]
        by_pair, g = build_sub(G)
        if s not in g or t not in g or tuple(sorted((s, t))) in by_pair:
            continue
        if not nx.has_path(g, s, t):
            continue
        st["n_deduction_required"] += 1
        try:
            paths = [list(p) for p in nx.edge_disjoint_paths(g, s, t)]
        except nx.NetworkXNoPath:
            paths = []
        st["maxdisjoint_hist"][len(paths)] += 1
        short = [p for p in paths if 2 <= (len(p) - 1) <= short_max]
        if len(short) < 2:
            continue
        st["n_ge2_short_paths"] += 1
        per_path = [r for r in (_compose_path(alg, by_pair, p) for p in short) if r is not None]
        if len(per_path) < 2:
            continue
        best_single = min(per_path, key=len)
        inter = per_path[0]
        for r in per_path[1:]:
            inter = inter & r
        st["best_single_len_hist"][len(best_single)] += 1
        st["inter_len_hist"][len(inter)] += 1
        if len(best_single) >= 2:
            st["n_best_single_nonsingleton"] += 1
        if inter < best_single:
            st["n_inter_strict_subset_best"] += 1
        if gold <= inter:
            st["n_gold_subset_inter"] += 1
        if not (len(best_single) >= 2 and inter < best_single and gold <= inter):
            continue
        bite = len(best_single) - len(inter)
        st["n_multipath_with_bite"] += 1
        st["bite_hist"][bite] += 1
        sub = nx.Graph()
        for p in short:
            for a, b in zip(p[:-1], p[1:]):
                sub.add_edge(a, b)
        mu = sub.number_of_edges() - sub.number_of_nodes() + nx.number_connected_components(sub)
        longest = max(len(p) - 1 for p in short)
        stratum = "ge3_cyclic" if (mu >= 1 or longest >= 3) else "len2"
        if stratum == "ge3_cyclic":
            st["n_ge3_cyclic"] += 1
        is_singleton = (len(gold) == 1)
        if is_singleton:
            st["n_headline_gold_singleton"] += 1
            st["headline_bite_hist"][bite] += 1
        if collect_eligible:
            vias = sorted({n for p in short for n in p[1:-1]})
            path_edges = sorted({tuple(sorted((a, b))) for p in short
                                 for a, b in zip(p[:-1], p[1:])})
            eligible.append({
                "corpus": ds_name, "algebra": algebra_key, "docid": docid, "s": s, "t": t,
                "vias": vias, "path_edges": [list(e) for e in path_edges], "short_paths": short,
                "gold_canon": sorted(gold), "gold_is_singleton": is_singleton,
                "gold_best_single": sorted(best_single), "gold_inter": sorted(inter),
                "gold_bite": bite, "stratum": stratum, "n_disjoint_paths": len(short),
                "disjoint_path_lengths": sorted(len(p) - 1 for p in short)})
    # finalize counters -> dicts
    out = {k: (dict(sorted(v.items())) if isinstance(v, Counter) else v) for k, v in st.items()}
    out["decision"] = ("GO" if out["n_headline_gold_singleton"] >= HEADLINE_GO_N
                       else "LOW-POWER" if out["n_headline_gold_singleton"] >= LOW_POWER_N
                       else "NO-GO")
    return out, eligible


def collect_deduction_queries(ds_name, algebra_key, max_hop=4, cap=None):
    """Collect ALL deduction-required queries in algebra X (regardless of redundancy) with
    their SHORTEST constituent path (node sequence) -- the substrate for the real-venue
    SINGLE-PATH closure-certified-deduction arm (read constituents -> compose -> commit)."""
    alg, build_sub, canon_fn = ALGEBRAS[algebra_key]
    out = []
    for docid, story, G in SA.load_spatial(ds_name):
        q = G["query_edge"]
        if q.get("gold_algebra") != algebra_key:
            continue
        gold = canon_fn(q.get("gold_canonical", []))
        if not gold:
            continue
        s, t = q["src"], q["dst"]
        by_pair, g = build_sub(G)
        if s not in g or t not in g or tuple(sorted((s, t))) in by_pair:
            continue
        if not nx.has_path(g, s, t):
            continue
        path = nx.shortest_path(g, s, t)
        hop = len(path) - 1
        if hop < 2 or hop > max_hop:
            continue
        # verify gold soundness: composing gold along the path CONTAINS the query gold
        comp = _compose_path(alg, by_pair, path)
        gold_sound = bool(comp is not None and gold <= comp)
        path_edges = sorted({tuple(sorted((a, b))) for a, b in zip(path[:-1], path[1:])})
        out.append({
            "corpus": ds_name, "algebra": algebra_key, "docid": docid, "s": s, "t": t,
            "path": path, "vias": path[1:-1], "path_edges": [list(e) for e in path_edges],
            "hop": hop, "gold_canon": sorted(gold), "gold_is_singleton": len(gold) == 1,
            "gold_path_composition": sorted(comp) if comp is not None else None,
            "gold_sound": gold_sound, "story": story,
            "stratum": "ge3" if hop >= 3 else "len2"})
    out.sort(key=lambda d: (d["docid"], d["s"], d["t"]))
    if cap:
        out = out[:cap]
    return out


def run_gate(short_max=SHORT_MAX):
    """Run all (corpus, algebra) arms. Returns (gate_dict, eligible_by_arm)."""
    arms = {}
    eligible = {}
    for ds_name in ("SpaRP-PS1", "SpartQA-Human"):
        for algebra_key in ("rcc8", "cardinal_direction"):
            st, elig = gate_arm(ds_name, algebra_key, short_max=short_max)
            arms[f"{ds_name}|{algebra_key}"] = st
            eligible[f"{ds_name}|{algebra_key}"] = elig
    # combined headline N for the PRIMARY (RCC-8) arm and an OPTIONAL cardinal arm
    rcc8_head = sum(arms[k]["n_headline_gold_singleton"] for k in arms if k.endswith("rcc8"))
    card_head = sum(arms[k]["n_headline_gold_singleton"] for k in arms
                    if k.endswith("cardinal_direction"))
    primary_decision = ("GO" if rcc8_head >= HEADLINE_GO_N
                       else "LOW-POWER" if rcc8_head >= LOW_POWER_N else "NO-GO")
    cardinal_decision = ("GO" if card_head >= HEADLINE_GO_N
                        else "LOW-POWER" if card_head >= LOW_POWER_N else "NO-GO")
    # overall: any arm GO/LOW-POWER -> can attempt; else structural NO-GO
    overall = "GO" if "GO" in (primary_decision, cardinal_decision) else \
              ("LOW-POWER" if "LOW-POWER" in (primary_decision, cardinal_decision) else "NO-GO")
    gate = {"arms": arms, "rcc8_headline_N": rcc8_head, "cardinal_headline_N": card_head,
            "rcc8_decision": primary_decision, "cardinal_decision": cardinal_decision,
            "overall_decision": overall, "headline_go_threshold": HEADLINE_GO_N,
            "low_power_threshold": LOW_POWER_N, "short_path_max": short_max,
            "tag": "GOLD-ONLY-GATE"}
    return gate, eligible


if __name__ == "__main__":
    import json
    g, _ = run_gate()
    print(json.dumps(g, indent=2))
