#!/usr/bin/env python3
"""STEP-1 diagnostic v2 (ZERO LLM): SOUND-representation multi-path bite measurement.

Path composition uses the SOUND Allen set per edge (coarse_superset_set when present,
else canonical_relation_set) -- this mirrors the BROAD high-recall disjunctive sets the
LLM reads will emit, so the gold-only gate does NOT over-predict bite. The query GOLD
TARGET stays the canonical (tightest, atomic) annotation -- for TDDMan that is a singleton
ground truth; for NarrativeTime it is the start-point-derived disjunctive set.
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict

import data_adapter as DA
import engine

AL = engine.build_allen_algebra()
VIA_CAP = 24

ALLEN_TOK = {'b': 'B', 'bi': 'BI', 'd': 'D', 'di': 'DI', 'o': 'O', 'oi': 'OI',
             'm': 'M', 'mi': 'MI', 's': 'S', 'si': 'SI', 'f': 'F', 'fi': 'FI',
             'eq': 'E', 'e': 'E'}


def _map(toks):
    out = [ALLEN_TOK[t.lower()] for t in toks if t.lower() in ALLEN_TOK]
    if len(out) != len(toks):
        return None
    return frozenset(out)


def canon_allen(edge):
    crs = edge.get("canonical_relation_set")
    return _map(crs) if crs else None


def sound_allen(edge):
    css = edge.get("coarse_superset_set")
    if css:
        m = _map(css)
        if m:
            return m
    return canon_allen(edge)


def _dir(by_pair, a, b, fn):
    e = by_pair[tuple(sorted((a, b)))]
    g = fn(e)
    if g is None:
        return None
    return g if (e["u"], e["v"]) == (a, b) else AL.converse(g)


def compose_path(by_pair, path):
    comp = _dir(by_pair, path[0], path[1], sound_allen)
    for k in range(1, len(path) - 1):
        nxt = _dir(by_pair, path[k], path[k + 1], sound_allen)
        if comp is None or nxt is None:
            return None
        comp = AL.compose(comp, nxt)
    return comp


def main():
    corpora = sys.argv[1:] or ["narrativetime", "tddman"]
    by_corpus = defaultdict(list)
    for (corpus, docid, text, G) in DA.load_dataset():
        by_corpus[corpus].append((docid, text, G))

    for corpus in corpora:
        rows = by_corpus.get(corpus, [])
        docs, off = DA.build_corpus(corpus, rows)
        n_eval = n_have = n_mp = n_head = n_singres = 0
        viol_inter = 0
        inter_tighter_than_direct = 0
        bites = []
        for docid, d in docs.items():
            by_pair = {}
            adj = defaultdict(set)
            for ed in d["edges"]:
                key = tuple(sorted((ed["u"], ed["v"])))
                if key in by_pair:
                    continue
                sg = sound_allen(ed)
                if sg is None:
                    continue
                by_pair[key] = ed
                if len(sg) < 13:
                    adj[ed["u"]].add(ed["v"]); adj[ed["v"]].add(ed["u"])
            for ed in d["edges"]:
                if not ed["deduction_required"]:
                    continue
                s, t = ed["u"], ed["v"]
                cq = _dir(by_pair, s, t, canon_allen)        # canonical (target) gold, oriented
                sq = _dir(by_pair, s, t, sound_allen)        # sound direct gold, oriented
                if cq is None or len(cq) >= 13:
                    continue
                if s not in adj or t not in adj:
                    continue
                vias = sorted((adj[s] & adj[t]) - {s, t})[:VIA_CAP]
                if len(vias) < 2:
                    n_eval += 1
                    continue
                comps = [compose_path(by_pair, [s, w, t]) for w in vias]
                comps = [c for c in comps if c is not None]
                n_eval += 1
                if len(comps) < 2:
                    continue
                n_have += 1
                best_single = min(comps, key=len)
                inter = comps[0]
                for c in comps[1:]:
                    inter = inter & c
                if not (cq <= inter):
                    viol_inter += 1
                if sq is not None and inter < sq:
                    inter_tighter_than_direct += 1
                is_mp = (len(best_single) >= 2) and (inter < best_single) and (cq <= inter)
                if is_mp:
                    n_mp += 1
                    bites.append(len(best_single) - len(inter))
                    if len(cq) == 1:
                        n_head += 1
                    if len(inter) == 1 and inter == cq:
                        n_singres += 1
        print(f"\n==== {corpus} (SOUND repr; docs={len(docs)}) ====")
        print(f"  n_eval(dedreq,informative)                 = {n_eval}")
        print(f"  n_have(>=2 vias)                            = {n_have}")
        print(f"  MULTIPATH-WITH-BITE (sound)     n_mp        = {n_mp}")
        print(f"     gold_is_singleton (HEADLINE) n_head      = {n_head}")
        print(f"     singleton_resolvable         n_singres   = {n_singres}")
        print(f"  inter NOT superset of canon gold viol_inter = {viol_inter}  "
              f"(excluded from n_mp by construction)")
        print(f"  inter strictly tighter than DIRECT gold     = {inter_tighter_than_direct}")
        print(f"  bite dist: {dict(sorted(Counter(bites).items()))}")


if __name__ == "__main__":
    main()
