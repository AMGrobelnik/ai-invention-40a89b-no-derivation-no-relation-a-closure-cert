#!/usr/bin/env python3
"""Build the Natural-Text Absent-Relation Kinship Corpus from Re-DocRED (+ vanilla
DocRED as a labelled secondary slice). One row per document, exp_sel_data_out schema,
drop-in compatible with the CLUTRR kinship dataset (same composition table + forward
least-fixpoint closure engine in kinship.py).

Strata per document:
  (a) atomic family edges (the KB / proof chain), each flagged locally_justifiable
      (local co-occurrence + surface kinship cue) -> a span-local reader can extract it;
  (b) PRESENT deduction-required query edges (no direct annotated edge, no local span,
      derivable by >=2-hop composition; composed_only types are outside DocRED's
      inventory => provably non-circular gold);
  (c) ABSENT no-derivation pairs (both entities family-participating but in different
      connected components => no kinship path; trustworthy under Re-DocRED completeness
      correction).
"""
from __future__ import annotations
import argparse, glob, hashlib, json, logging, os, resource, sys, time
from collections import deque

from detok import detokenize, mention_char_span, sent_char_span
from kinship import Kinship, forward_closure

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("build")

WORK = os.path.dirname(os.path.abspath(__file__))
CT = json.load(open(os.path.join(WORK, "clutrr_composition_table.json")))
KIN = Kinship(CT)

# ---- DocRED family Wikidata property -> CLUTRR primitive (edge a->b:type == "b is a's type") ----
# {h,t,r} => "t is h's r".  P1038 'relative' is NOT in DocRED's 96-relation inventory.
PROP2PRIM = {"P22": "inv-child", "P25": "inv-child", "P40": "child",
             "P26": "SO", "P3373": "sibling"}
PROP_GENDER = {"P22": "male", "P25": "female"}       # gender FIXED on target t
FAM = set(PROP2PRIM)
COMPOSED_ONLY = {"grand", "inv-grand", "un", "inv-un", "in-law", "inv-in-law", "sibling-in-law"}
NEUTRAL = {"inv-child": "parent", "child": "child", "SO": "spouse", "sibling": "sibling"}

# surface kinship cues that locally justify each relation (token-level, lowercased)
CUES = {
    "P22": {"father", "mother", "son", "daughter", "sons", "daughters", "parent", "parents", "born"},
    "P25": {"father", "mother", "son", "daughter", "sons", "daughters", "parent", "parents", "born"},
    "P40": {"son", "daughter", "child", "children", "sons", "daughters", "father", "mother", "parent"},
    "P26": {"husband", "wife", "married", "marry", "marries", "marriage", "wed", "wedded",
            "spouse", "widow", "widower", "remarried"},
    "P3373": {"brother", "sister", "brothers", "sisters", "sibling", "siblings", "twin", "twins"},
}
MALE_APPOS = {"son", "brother", "husband", "father", "grandson", "grandfather", "nephew",
              "uncle", "widower", "twin-brother"}
FEMALE_APPOS = {"daughter", "sister", "wife", "mother", "granddaughter", "grandmother",
                "niece", "aunt", "widow"}


# --------------------------------------------------------------------------- helpers
def entity_type(mentions):
    cnt = {}
    for m in mentions:
        cnt[m.get("type", "?")] = cnt.get(m.get("type", "?"), 0) + 1
    return max(cnt, key=cnt.get)


def longest_name(mentions):
    return max((m["name"] for m in mentions), key=lambda s: (len(s), s))


def bfs_path(adj, src, tgt):
    """Shortest undirected path src..tgt -> list of node ids (inclusive) or None."""
    if src not in adj:
        return None
    prev = {src: None}
    dq = deque([src])
    while dq:
        n = dq.popleft()
        if n == tgt:
            path = [n]
            while prev[path[-1]] is not None:
                path.append(prev[path[-1]])
            return path[::-1]
        for m in adj.get(n, ()):
            if m not in prev:
                prev[m] = n; dq.append(m)
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


def derive_genders(doc_sents, vertexSet, fam_edges):
    """Return {entity_id: 'male'|'female'|None}. Deterministic P22/P25 target votes +
    reliable appositive cue ('his wife Lynn', 'brother Joshua') directly before a mention."""
    male = {}; female = {}
    def vote(eid, g):
        (male if g == "male" else female)[eid] = (male if g == "male" else female).get(eid, 0) + 1
    for (h, t, r) in fam_edges:
        if r in PROP_GENDER:
            vote(t, PROP_GENDER[r])
    # appositive cue immediately preceding any mention
    for eid, mentions in enumerate(vertexSet):
        for m in mentions:
            s_id = m["sent_id"]; s = m["pos"][0]
            if s_id >= len(doc_sents):
                continue
            sent = doc_sents[s_id]
            for k in range(max(0, s - 2), s):
                w = str(sent[k]).lower().strip(".,;:")
                if w in MALE_APPOS:
                    vote(eid, "male")
                elif w in FEMALE_APPOS:
                    vote(eid, "female")
    out = {}
    ids = set(male) | set(female)
    for eid in ids:
        mv, fv = male.get(eid, 0), female.get(eid, 0)
        out[eid] = "male" if mv > fv else "female" if fv > mv else None
    return out


def surface_word(primitive, gender):
    if gender in ("male", "female"):
        sf = CT["surface_forms"].get(primitive, {})
        w = sf.get(gender)
        if w:
            return w
    return NEUTRAL.get(primitive, primitive)


def span_text(text, span):
    return text[span[0]:span[1]].lower() if span else ""


# --------------------------------------------------------------------------- per-doc
def build_doc(doc, source, split, absent_cap=30, present_cap=40):
    title = doc["title"]
    sents = doc["sents"]
    text, offsets = detokenize(sents)
    vertexSet = doc["vertexSet"]
    labels = doc.get("labels", [])

    fam_edges = [(L["h"], L["t"], L["r"]) for L in labels if L["r"] in FAM]
    if not fam_edges:
        return None
    evidence = {}
    for L in labels:
        if L["r"] in FAM:
            evidence[(L["h"], L["t"], L["r"])] = L.get("evidence", []) or []

    genders = derive_genders(sents, vertexSet, fam_edges)

    # participating entities
    partic = set()
    for h, t, r in fam_edges:
        partic.add(h); partic.add(t)

    # mention char spans + offset QA
    offok = 0; offtot = 0
    node_spans = {}
    for eid in partic:
        spans = []
        for m in vertexSet[eid]:
            sp = mention_char_span(offsets, m["sent_id"], m["pos"])
            if sp:
                spans.append(list(sp))
                # offset QA: normalized substring == normalized mention name
                got = " ".join(text[sp[0]:sp[1]].split())
                want = " ".join(str(m["name"]).split())
                offtot += 1
                if got == want:
                    offok += 1
        node_spans[eid] = spans

    # ---- atomic edges (the KB), each with readability metadata ----
    atomic_edges = []
    closure_input = []          # [{a,b,type}] for the engine
    undirected = []
    direct_pairs = set()
    n_just = 0
    sent_of = {eid: sorted({m["sent_id"] for m in vertexSet[eid]}) for eid in partic}
    for (h, t, r) in fam_edges:
        prim = PROP2PRIM[r]
        # locality: a mention of h and a mention of t within adjacent sentences
        best = None
        for sh in sent_of[h]:
            for st in sent_of[t]:
                d = abs(sh - st)
                if best is None or d < best[0]:
                    best = (d, sh, st)
        locality = best is not None and best[0] <= 1
        # support span: evidence sents if given, else the closest co-occurrence sents
        ev = evidence.get((h, t, r), [])
        if ev:
            sids = [s for s in ev if s < len(sents)]
        elif best is not None:
            lo, hi = sorted((best[1], best[2]))
            sids = list(range(lo, hi + 1))
        else:
            sids = sorted(set(sent_of[h]) | set(sent_of[t]))
        sids = sids or [0]
        sp_lo = min(sent_char_span(offsets, s)[0] for s in sids if sent_char_span(offsets, s))
        sp_hi = max(sent_char_span(offsets, s)[1] for s in sids if sent_char_span(offsets, s))
        support_span = [sp_lo, sp_hi]
        toks = set(span_text(text, support_span).replace(",", " ").replace(".", " ").split())
        cue_hit = sorted(CUES[r] & toks)
        surface_cue = cue_hit[0] if cue_hit else None
        locally_justifiable = bool(locality and surface_cue)
        if locally_justifiable:
            n_just += 1
        tgender = genders.get(t)
        atomic_edges.append({
            "source": h, "target": t,
            "kinship_relation": surface_word(prim, tgender),
            "primitive": prim, "relation_type": prim,
            "target_gender": tgender,
            "is_query": False, "hop_count": 1,
            "support_span": support_span, "surface_cue": surface_cue,
            "evidence_sent_ids": sids,
            "locality": bool(locality), "has_cue": bool(surface_cue),
            "locally_justifiable": locally_justifiable,
            "wikidata_property": r,
        })
        closure_input.append({"a": h, "b": t, "type": prim})
        undirected.append((h, t))
        direct_pairs.add(frozenset((h, t)))

    # adjacency for path/min-sent-distance
    adj = {}
    for a, b in undirected:
        adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)
    justifiable_pairs = {frozenset((e["source"], e["target"])) for e in atomic_edges if e["locally_justifiable"]}

    def min_sent_dist(a, b):
        best = None
        for sa in sent_of[a]:
            for sb in sent_of[b]:
                d = abs(sa - sb)
                best = d if best is None else min(best, d)
        return best

    # ---- closure -> PRESENT deduction-required query edges ----
    D, nbrs, n_fired = forward_closure(KIN, closure_input)
    present = []
    seen = set()
    for (a, b), ts in D.items():
        key = frozenset((a, b))
        if a == b or key in direct_pairs or key in seen:
            continue
        if len(ts) != 1:
            continue
        msd = min_sent_dist(a, b)
        if msd is not None and msd <= 1:      # has a local span -> not deduction-required
            continue
        path = bfs_path(adj, a, b)
        if not path or len(path) - 1 < 2:
            continue
        seen.add(key)
        prim = next(iter(ts))
        # direction: D[(a,b)]=prim means "b is a's prim"; gold = (source=a, target=b)
        tgender = genders.get(b)
        kr = surface_word(prim, tgender)
        path_edges_just = all(frozenset((path[i], path[i + 1])) in justifiable_pairs
                              for i in range(len(path) - 1))
        present.append({
            "source": a, "target": b,
            "kinship_relation": kr if tgender in ("male", "female") else None,
            "primitive": prim, "relation_type": prim,
            "target_gender": tgender,
            "target_int": CT.get("label_map", {}).get(kr),
            "is_query": True, "hop_count": len(path) - 1,
            "derivation_path": path[1:-1],
            "composed_only": prim in COMPOSED_ONLY,
            "fully_readable": bool(path_edges_just),
        })
    # deterministic cap: shortest hops first, then by ids
    present.sort(key=lambda q: (q["hop_count"], q["source"], q["target"]))
    present_truncated = len(present) > present_cap
    present = present[:present_cap]

    # ---- ABSENT no-derivation pairs (different components) ----
    comps = components(partic, undirected)
    absent = []
    if len(comps) >= 2:
        ordered = sorted([sorted(c) for c in comps])
        for i in range(len(ordered)):
            for j in range(i + 1, len(ordered)):
                for a in ordered[i]:
                    for b in ordered[j]:
                        absent.append({"source": a, "target": b,
                                       "reason": "different_component", "is_absent": True})
    absent.sort(key=lambda p: (p["source"], p["target"]))
    absent_truncated = len(absent) > absent_cap
    absent = absent[:absent_cap]

    # ---- nodes ----
    nodes = []
    for eid in sorted(partic):
        nodes.append({
            "entity_id": eid,
            "surface": longest_name(vertexSet[eid]),
            "type": entity_type(vertexSet[eid]),
            "gender": genders.get(eid),
            "mention_spans": node_spans[eid],
            "wikidata_qid": None,
        })

    hop_hist = {}
    for q in present:
        hop_hist[str(q["hop_count"])] = hop_hist.get(str(q["hop_count"]), 0) + 1
    char_len = len(text)
    n_tokens = sum(len(s) for s in sents)
    offset_ok_frac = round(offok / offtot, 4) if offtot else 1.0

    gold_graph = {
        "doc_id": title, "source": source, "split": split,
        "nodes": nodes,
        "atomic_edges": atomic_edges,
        "query_edges": present,
        "absent_relation_pairs": absent,
        "absent_pairs_source": "structural_components",
    }
    row = {
        "input": text,
        "output": json.dumps(gold_graph, ensure_ascii=False),
        "metadata_doc_id": title,
        "metadata_source": source,
        "metadata_split": split,
        "metadata_fold": int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 5,
        "metadata_n_entities": len(partic),
        "metadata_n_per_entities": sum(1 for eid in partic if entity_type(vertexSet[eid]) == "PER"),
        "metadata_n_atomic_edges": len(atomic_edges),
        "metadata_n_locally_justifiable_edges": n_just,
        "metadata_locally_justifiable_frac": round(n_just / len(atomic_edges), 4) if atomic_edges else 0.0,
        "metadata_n_family_components": len(comps),
        "metadata_present_query_count": len(present),
        "metadata_present_truncated": present_truncated,
        "metadata_composed_only_present_count": sum(1 for q in present if q["composed_only"]),
        "metadata_absent_pair_count": len(absent),
        "metadata_absent_truncated": absent_truncated,
        "metadata_char_len": char_len,
        "metadata_n_tokens": n_tokens,
        "metadata_hop_histogram": json.dumps(hop_hist),
        "metadata_n_ge_2500_chars": int(char_len >= 2500),
        "metadata_has_3000_char": bool(char_len >= 3000),
        "metadata_offset_ok_frac": offset_ok_frac,
        "metadata_n_fired_closure": n_fired,
    }
    return row, gold_graph


# --------------------------------------------------------------------------- driver
SPLITS = {
    "re-docred": [("train_revised.json", "train"), ("dev_revised.json", "dev"),
                  ("test_revised.json", "test")],
    "docred": [("train_annotated.json", "train"), ("dev.json", "dev")],
}


def run(sources, max_docs=None):
    rows_by_source = {}
    stats = {}
    for source in sources:
        rows = []
        present_total = absent_total = comp_present = 0
        offoks = []; justs = []
        hop_all = {}; type_all = {}
        ndoc = 0
        for fn, split in SPLITS[source]:
            path = os.path.join(WORK, "temp", "datasets", fn)
            docs = json.load(open(path))
            for doc in docs:
                if max_docs and ndoc >= max_docs:
                    break
                res = build_doc(doc, source, split)
                if res is None:
                    continue
                row, gg = res
                rows.append(row); ndoc += 1
                present_total += len(gg["query_edges"])
                absent_total += len(gg["absent_relation_pairs"])
                comp_present += sum(1 for q in gg["query_edges"] if q["composed_only"])
                offoks.append(row["metadata_offset_ok_frac"])
                if row["metadata_n_atomic_edges"]:
                    justs.append(row["metadata_n_locally_justifiable_edges"] / row["metadata_n_atomic_edges"])
                for q in gg["query_edges"]:
                    hop_all[str(q["hop_count"])] = hop_all.get(str(q["hop_count"]), 0) + 1
                    type_all[q["primitive"]] = type_all.get(q["primitive"], 0) + 1
            if max_docs and ndoc >= max_docs:
                break
        rows_by_source[source] = rows
        stats[source] = dict(
            n_docs=len(rows), present_total=present_total, absent_total=absent_total,
            composed_only_present=comp_present, hop_hist=hop_all, type_hist=type_all,
            mean_offset_ok=round(sum(offoks) / len(offoks), 4) if offoks else None,
            mean_locally_justifiable_frac=round(sum(justs) / len(justs), 4) if justs else None,
        )
    return rows_by_source, stats


if __name__ == "__main__":
    resource.setrlimit(resource.RLIMIT_AS, (24 * 1024**3, 24 * 1024**3))
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", default="re-docred,docred")
    ap.add_argument("--max-docs", type=int, default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    t0 = time.time()
    sources = args.sources.split(",")
    rows_by_source, stats = run(sources, args.max_docs)
    dt = time.time() - t0
    log.info("built in %.1fs", dt)
    for s, st in stats.items():
        log.info("%s: %s", s, json.dumps(st))
    if args.out:
        json.dump({"stats": stats, "rows_by_source": {k: len(v) for k, v in rows_by_source.items()}},
                  open(args.out, "w"))
