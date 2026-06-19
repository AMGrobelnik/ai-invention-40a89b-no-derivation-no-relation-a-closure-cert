#!/usr/bin/env python3
"""STEP-1 diagnostic (ZERO LLM): verify the Allen-13 soundness invariant and measure
multi-path INTERSECTION bite on the FROZEN real gold graphs, BEFORE any LLM spend.

This is a fast standalone probe to confirm (a) the token map + converse orientation are
correct (gold_q subset of every comp_path and of the intersection), and (b) whether
multi-path-redundant-WITH-BITE query edges exist on NarrativeTime / TDDMan.
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict

import data_adapter as DA
import engine

VIA_CAP = 24   # cap length-2 vias considered per query edge (compute guard on dense docs)

AL = engine.build_allen_algebra()

ALLEN_TOK = {'b': 'B', 'bi': 'BI', 'd': 'D', 'di': 'DI', 'o': 'O', 'oi': 'OI',
             'm': 'M', 'mi': 'MI', 's': 'S', 'si': 'SI', 'f': 'F', 'fi': 'FI',
             'eq': 'E', 'e': 'E'}


def gold_allen(edge):
    crs = edge.get("canonical_relation_set")
    if not crs:
        return None
    toks = [ALLEN_TOK[t.lower()] for t in crs if t.lower() in ALLEN_TOK]
    if len(toks) != len(crs):
        return "BADTOK"
    return frozenset(toks)


def gold_dir(by_pair, a, b):
    e = by_pair[tuple(sorted((a, b)))]
    g = gold_allen(e)
    if g in (None, "BADTOK"):
        return g
    return g if (e["u"], e["v"]) == (a, b) else AL.converse(g)


def compose_path(by_pair, path):
    comp = gold_dir(by_pair, path[0], path[1])
    for k in range(1, len(path) - 1):
        nxt = gold_dir(by_pair, path[k], path[k + 1])
        comp = AL.compose(comp, nxt)
    return comp


def main():
    corpora = sys.argv[1:] or ["narrativetime", "tddman", "matres"]
    by_corpus = defaultdict(list)
    for (corpus, docid, text, G) in DA.load_dataset():
        by_corpus[corpus].append((docid, text, G))

    for corpus in corpora:
        rows = by_corpus.get(corpus, [])
        docs, off = DA.build_corpus(corpus, rows)
        badtok = 0
        n_eval = 0           # deduction-required, informative-gold candidate query edges
        n_have_2paths = 0    # >=2 edge-disjoint constraining paths
        n_multipath = 0      # multipath redundant WITH bite (inter strict subset best_single)
        n_headline = 0       # + gold_is_singleton
        n_singleton_resolvable = 0
        soundness_viol_path = 0
        soundness_viol_inter = 0
        bites = []
        for di, (docid, d) in enumerate(docs.items()):
            by_pair = {}
            adj = defaultdict(set)
            for ed in d["edges"]:
                key = tuple(sorted((ed["u"], ed["v"])))
                if key in by_pair:
                    continue
                g = gold_allen(ed)
                if g == "BADTOK":
                    badtok += 1
                    continue
                if g is None:
                    continue
                by_pair[key] = ed
                # informative (non-universe) gold edge -> usable in a constraining path
                if len(g) < 13:
                    adj[ed["u"]].add(ed["v"])
                    adj[ed["v"]].add(ed["u"])
            for ed in d["edges"]:
                if not ed["deduction_required"]:
                    continue
                s, t = ed["u"], ed["v"]
                gq = gold_dir(by_pair, s, t)
                if gq in (None, "BADTOK") or len(gq) >= 13:
                    continue
                # common-neighbor length-2 vias (each distinct via => edge-disjoint path)
                if s not in adj or t not in adj:
                    continue
                vias = sorted((adj[s] & adj[t]) - {s, t})[:VIA_CAP]
                paths = [[s, w, t] for w in vias]
                n_eval += 1
                if len(paths) < 2:
                    continue
                comps = []
                ok = True
                for p in paths:
                    cp = compose_path(by_pair, p)
                    if cp in (None, "BADTOK"):
                        ok = False
                        break
                    comps.append(cp)
                    if not (gq <= cp):
                        soundness_viol_path += 1
                if not ok:
                    continue
                n_have_2paths += 1
                best_single = min(comps, key=len)
                inter = comps[0]
                for c in comps[1:]:
                    inter = inter & c
                if not (gq <= inter):
                    soundness_viol_inter += 1
                bite = len(best_single) - len(inter)
                is_mp = (len(best_single) >= 2) and (inter < best_single) and (gq <= inter)
                if is_mp:
                    n_multipath += 1
                    bites.append(bite)
                    if len(gq) == 1:
                        n_headline += 1
                    if len(inter) == 1 and inter == gq:
                        n_singleton_resolvable += 1
            print(f"  [{corpus}] doc {di+1}/{len(docs)} eval={n_eval} mp={n_multipath} "
                  f"headline={n_headline}", flush=True)
        bite_dist = Counter(bites)
        print(f"\n==== {corpus} (docs={len(docs)} offset_ok={off:.3f}) ====")
        print(f"  badtok_edges={badtok}")
        print(f"  deduction-required eval query edges      n_eval         = {n_eval}")
        print(f"  with >=2 edge-disjoint constraining paths n_have_2paths  = {n_have_2paths}")
        print(f"  MULTIPATH-REDUNDANT-WITH-BITE             n_multipath    = {n_multipath}")
        print(f"     of which gold_is_singleton (HEADLINE)  n_headline     = {n_headline}")
        print(f"     singleton_resolvable (inter==gold)     n_singres      = {n_singleton_resolvable}")
        print(f"  soundness violations: path={soundness_viol_path} inter={soundness_viol_inter}")
        print(f"  bite dist (|best_single|-|inter|): {dict(sorted(bite_dist.items()))}")


if __name__ == "__main__":
    main()
