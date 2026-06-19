#!/usr/bin/env python3
"""Feasibility probe: measure PRESENT multi-hop and ABSENT yields over the real
closure engine, before committing to the full build. Pure-CPU, no LLM."""
import json, sys
from collections import deque
from kinship import Kinship, forward_closure

CT = json.load(open("clutrr_composition_table.json"))
KIN = Kinship(CT)

# DocRED family Wikidata property -> CLUTRR primitive for directed edge h->t
# convention: edge a->b:type means "b is a's type". {h,t,r} => "t is h's r".
PROP2PRIM = {
    "P22": "inv-child",   # t is h's father  (parent)
    "P25": "inv-child",   # t is h's mother  (parent)
    "P40": "child",       # t is h's child
    "P26": "SO",          # spouse (symmetric)
    "P3373": "sibling",   # sibling (symmetric)
}
FAM = set(PROP2PRIM)
# composed types NOT in DocRED's relation inventory => provably non-circular gold
COMPOSED_ONLY = {"grand", "inv-grand", "un", "inv-un", "in-law", "inv-in-law", "sibling-in-law"}


def undirected_dist(edges, src, tgt):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    if src not in adj:
        return None
    dq = deque([(src, 0)]); seen = {src}
    while dq:
        n, d = dq.popleft()
        if n == tgt:
            return d
        for m in adj.get(n, ()):
            if m not in seen:
                seen.add(m); dq.append((m, d + 1))
    return None


def components(nodes, edges):
    par = {n: n for n in nodes}
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for a, b in edges:
        if a in par and b in par:
            par[f(a)] = f(b)
    comp = {}
    for n in nodes:
        comp.setdefault(f(n), []).append(n)
    return list(comp.values())


def analyze(docs):
    tot_present = 0; tot_absent = 0
    hop_hist = {}; type_hist = {}; composed_only_present = 0; fully_readable = 0
    docs_present = 0; docs_absent = 0
    for doc in docs:
        labs = doc.get("labels", [])
        fam = [(L["h"], L["t"], L["r"]) for L in labs if L["r"] in FAM]
        if not fam:
            continue
        # direct annotated family pairs (unordered) -> excluded from query/absent
        direct = set()
        atomic = []  # [{a,b,type}]
        undirected = []
        partic = set()
        for h, t, r in fam:
            prim = PROP2PRIM[r]
            atomic.append({"a": h, "b": t, "type": prim})
            undirected.append((h, t))
            direct.add(frozenset((h, t)))
            partic.add(h); partic.add(t)
        # closure over full annotated family graph
        D, nbrs, _ = forward_closure(KIN, atomic)
        # PRESENT multi-hop queries: derivable singleton, no direct edge, hop>=2
        present_pairs = set()
        for (a, b), ts in D.items():
            key = frozenset((a, b))
            if a == b or key in direct or key in present_pairs:
                continue
            if len(ts) != 1:
                continue
            d = undirected_dist(undirected, a, b)
            if d is None or d < 2:
                continue
            t = next(iter(ts))
            present_pairs.add(key)
            tot_present += 1
            hop_hist[d] = hop_hist.get(d, 0) + 1
            type_hist[t] = type_hist.get(t, 0) + 1
            if t in COMPOSED_ONLY:
                composed_only_present += 1
        if present_pairs:
            docs_present += 1
        # ABSENT: different-component family-participating pairs
        comps = components(partic, undirected)
        if len(comps) >= 2:
            docs_absent += 1
            for i in range(len(comps)):
                for j in range(i + 1, len(comps)):
                    tot_absent += len(comps[i]) * len(comps[j])
    return dict(tot_present=tot_present, tot_absent=tot_absent, hop_hist=hop_hist,
                type_hist=type_hist, composed_only_present=composed_only_present,
                docs_present=docs_present, docs_absent=docs_absent)


if __name__ == "__main__":
    allres = {}
    docs_all = []
    for f in ["train_revised.json", "dev_revised.json", "test_revised.json"]:
        docs = json.load(open(f"temp/datasets/{f}"))
        docs_all.extend(docs)
        allres[f] = analyze(docs)
    print("=== per-split ===")
    for f, r in allres.items():
        print(f, json.dumps(r))
    print("\n=== Re-DocRED TOTAL ===")
    print(json.dumps(analyze(docs_all), indent=1))
