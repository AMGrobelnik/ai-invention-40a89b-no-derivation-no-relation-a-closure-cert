#!/usr/bin/env python3
"""Build the Natural-Text Absent-Relation Located-In (Administrative Containment) Corpus
from Re-DocRED (+ vanilla DocRED as a labelled secondary slice). One row per document,
exp_sel_data_out schema, DROP-IN compatible with the iter-6 kinship engine: it reuses
kinship.py (the CLUTRR finite-composition forward least-fixpoint UNION closure) UNCHANGED,
parameterized by a DEGENERATE single-relation transitive composition table
(containment_composition_table.json):

    located_in o located_in = located_in   (transitive, downward)
    contains   o contains   = contains     (converse, upward)
    EVERYTHING else UNDEFINED              => sibling/cousin places derive EMPTY (sound)

This is the structural twin of the kinship corpus (art_NUWTxBVWENIJ): same detok/offset
machinery, same three strata, same round-trip gate.

Strata per document:
  (a) atomic located_in edges (the KB / proof chain), each flagged locally_justifiable
      (local co-occurrence + a surface containment cue) -> a span-local reader can extract it;
  (b) PRESENT deduction-required query edges (no direct annotated edge, no local span,
      derivable by >=2-hop located_in transitivity); composed_only (never itself an
      annotated edge) => non-circular;
  (c) ABSENT no-derivation pairs (no containment path in EITHER direction), split into
      'different_component' (totally unrelated places, the clean kinship-analog) and
      'same_component_sibling' (two places under a common container, neither inside the
      other -- the containment-specific, reviewer-named absent regime). Trustworthy under
      Re-DocRED's completeness correction; DOWNGRADED on vanilla DocRED.

Direction convention (fixed once): an edge source->target with primitive located_in means
"source is located in target" (source is the sub-region / descendant).
"""
from __future__ import annotations
import argparse, hashlib, json, logging, os, resource, time
from collections import deque

from detok import detokenize, mention_char_span, sent_char_span
from kinship import Kinship, forward_closure

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("build")

WORK = os.path.dirname(os.path.abspath(__file__))
CT = json.load(open(os.path.join(WORK, "containment_composition_table.json")))
KIN = Kinship(CT)

# ---- DocRED located-in / administrative-containment Wikidata property -> (direction) ----
# Edge convention: (source, located_in, target) == "source is located in target".
#   P131 'located in the administrative territorial entity' : h located_in t  -> (h, t)
#   P17  'country'                                          : h located_in t  -> (h, t)
#   P276 'location'                                         : h located_in t  -> (h, t)  (lower precision)
#   P1376'capital of'      (h is the capital of t)          : h located_in t  -> (h, t)
#   P150 'contains administrative territorial entity' (h contains t)          -> INVERT (t, h)
#   P36  'capital'         (t is the capital of h)                            -> INVERT (t, h)
CORE_PROPS = {"P131", "P17", "P150", "P1376", "P36"}      # unambiguous admin containment
OPT_PROPS = {"P276"}                                       # lower-precision 'location' (drops to ~0 LOC-LOC on re-docred)
DIRECT_PROPS = {"P131", "P17", "P276", "P1376"}            # source=h, target=t
INVERT_PROPS = {"P150", "P36"}                             # source=t, target=h (annotated as container->contained)
LOC_PROPS = CORE_PROPS | OPT_PROPS
PRIM = "located_in"

# surface containment cues (token-level, lowercased) that locally justify a located_in edge.
# 'in' is the weak high-frequency workhorse cue ('X, a city in Y') -- required ALONGSIDE
# adjacent-sentence co-occurrence (locality), exactly mirroring the kinship 'born/married/...' cues.
GENERAL_CUES = {
    "in", "located", "situated", "within", "part", "district", "province", "county",
    "region", "municipality", "city", "town", "village", "borough", "prefecture",
    "commune", "near", "area", "territory", "department", "state", "country", "island",
    "suburb", "neighbourhood", "neighborhood", "quarter", "arrondissement", "canton",
    "ward", "zone", "county", "principality", "kingdom", "republic", "metropolitan",
}
PROP_CUES = {
    "P1376": {"capital", "capital of", "seat"},
    "P36": {"capital", "capital of", "seat"},
    "P150": {"contains", "includes", "comprises", "consists", "encompasses", "covers"},
}
# light admin-LEVEL keywords (best-effort node stratification metadata; non-load-bearing)
LEVEL_CUES = [
    ("country", {"country", "nation", "republic", "kingdom", "state", "empire", "principality"}),
    ("region", {"region", "province", "state", "county", "district", "department", "prefecture",
                "canton", "oblast", "territory", "land", "governorate", "voivodeship"}),
    ("city", {"city", "town", "village", "municipality", "borough", "commune", "suburb",
              "hamlet", "settlement", "neighbourhood", "neighborhood", "ward", "quarter"}),
]


# --------------------------------------------------------------------------- helpers
def entity_type(mentions):
    cnt = {}
    for m in mentions:
        cnt[m.get("type", "?")] = cnt.get(m.get("type", "?"), 0) + 1
    return max(cnt, key=cnt.get)


def longest_name(mentions):
    return max((m["name"] for m in mentions), key=lambda s: (len(s), s))


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


def admin_level(sents, mentions):
    """Best-effort {country|region|city|other} from the mention name tokens + the 2 tokens
    preceding each mention (e.g. 'the city of', 'X Province'). Non-load-bearing stratifier."""
    votes = {"country": 0, "region": 0, "city": 0}
    toks = set()
    for m in mentions:
        for w in str(m["name"]).lower().replace(",", " ").split():
            toks.add(w.strip(".,;:'\"()"))
        s_id, s = m["sent_id"], m["pos"][0]
        if s_id < len(sents):
            sent = sents[s_id]
            for k in range(max(0, s - 2), min(len(sent), m["pos"][1] + 1)):
                toks.add(str(sent[k]).lower().strip(".,;:'\"()"))
    for level, kw in LEVEL_CUES:
        if toks & kw:
            votes[level] += 1
    best = max(votes, key=votes.get)
    return best if votes[best] > 0 else "other"


def span_text(text, span):
    return text[span[0]:span[1]].lower() if span else ""


# --------------------------------------------------------------------------- per-doc
def build_doc(doc, source, split, absent_cap=30, present_cap=40, atomic_cap=80):
    title = doc["title"]
    sents = doc["sents"]
    text, offsets = detokenize(sents)
    vertexSet = doc["vertexSet"]
    labels = doc.get("labels", [])
    etypes = [entity_type(v) for v in vertexSet]

    # ---- collect directed located_in edges (LOC-LOC only), dedup, detect contradictions ----
    # edge_props[(src,tgt)] = {wikidata properties contributing this located_in edge}
    # edge_labels[(src,tgt)] = list of (h, t, r, evidence) contributing labels
    edge_props = {}
    edge_labels = {}
    for L in labels:
        r = L["r"]
        if r not in LOC_PROPS:
            continue
        h, t = L["h"], L["t"]
        if etypes[h] != "LOC" or etypes[t] != "LOC":          # LOC-LOC entity-type filter
            continue
        if r in INVERT_PROPS:
            src, tgt = t, h
        else:
            src, tgt = h, t
        if src == tgt:
            continue
        edge_props.setdefault((src, tgt), set()).add(r)
        edge_labels.setdefault((src, tgt), []).append((h, t, r, L.get("evidence", []) or []))

    if not edge_props:
        return None

    # drop true 2-cycles (a located_in b AND b located_in a) -> contradiction
    contradictions = []
    dropped = set()
    for (a, b) in list(edge_props):
        if (b, a) in edge_props and (a, b) not in dropped:
            contradictions.append({"pair": [a, b],
                                   "props_ab": sorted(edge_props[(a, b)]),
                                   "props_ba": sorted(edge_props[(b, a)])})
            dropped.add((a, b)); dropped.add((b, a))
    for p in dropped:
        edge_props.pop(p, None); edge_labels.pop(p, None)
    if not edge_props:
        return None

    # participating entities
    partic = set()
    for (a, b) in edge_props:
        partic.add(a); partic.add(b)

    # mention char spans + offset QA
    offok = 0; offtot = 0
    node_spans = {}
    for eid in partic:
        spans = []
        for m in vertexSet[eid]:
            sp = mention_char_span(offsets, m["sent_id"], m["pos"])
            if sp:
                spans.append(list(sp))
                got = " ".join(text[sp[0]:sp[1]].split())
                want = " ".join(str(m["name"]).split())
                offtot += 1
                if got == want:
                    offok += 1
        node_spans[eid] = spans

    sent_of = {eid: sorted({m["sent_id"] for m in vertexSet[eid]}) for eid in partic}

    # ---- atomic edges (the KB), each with readability metadata ----
    atomic_edges = []
    closure_input = []
    undirected = []
    direct_pairs = set()
    n_just = 0
    for (src, tgt) in sorted(edge_props):
        props = sorted(edge_props[(src, tgt)])
        is_core = any(p in CORE_PROPS for p in props)
        inverted = all(p in INVERT_PROPS for p in props) and not any(p in DIRECT_PROPS for p in props)
        # locality: a mention of src and a mention of tgt within adjacent sentences
        best = None
        for ss in sent_of[src]:
            for st in sent_of[tgt]:
                d = abs(ss - st)
                if best is None or d < best[0]:
                    best = (d, ss, st)
        locality = best is not None and best[0] <= 1
        # support span: union of evidence sents across contributing labels, else closest co-occ
        ev = sorted({s for (_, _, _, evs) in edge_labels[(src, tgt)] for s in evs if s < len(sents)})
        if ev:
            sids = ev
        elif best is not None:
            lo, hi = sorted((best[1], best[2]))
            sids = list(range(lo, hi + 1))
        else:
            sids = sorted(set(sent_of[src]) | set(sent_of[tgt]))
        sids = sids or [0]
        spans = [sent_char_span(offsets, s) for s in sids if sent_char_span(offsets, s)]
        sp_lo = min(s[0] for s in spans); sp_hi = max(s[1] for s in spans)
        support_span = [sp_lo, sp_hi]
        toks = set(span_text(text, support_span).replace(",", " ").replace(".", " ").split())
        cueset = set(GENERAL_CUES)
        for p in props:
            cueset |= PROP_CUES.get(p, set())
        cue_hit = sorted(cueset & toks)
        surface_cue = cue_hit[0] if cue_hit else None
        locally_justifiable = bool(locality and surface_cue)
        if locally_justifiable:
            n_just += 1
        atomic_edges.append({
            "source": src, "target": tgt,
            "relation_surface": "located in", "primitive": PRIM, "relation_type": PRIM,
            "is_query": False, "hop_count": 1,
            "support_span": support_span, "surface_cue": surface_cue,
            "evidence_sent_ids": sids,
            "locality": bool(locality), "has_cue": bool(surface_cue),
            "locally_justifiable": locally_justifiable,
            "wikidata_property": props[0], "wikidata_properties": props,
            "core_property": bool(is_core), "inverted": bool(inverted),
        })
        closure_input.append({"a": src, "b": tgt, "type": PRIM})
        undirected.append((src, tgt))
        direct_pairs.add(frozenset((src, tgt)))

    # cap atomic edges deterministically (core-first, then by ids) so a geography article
    # cannot dominate; recompute participating set from the kept edges.
    atomic_truncated = len(atomic_edges) > atomic_cap
    if atomic_truncated:
        atomic_edges.sort(key=lambda e: (0 if e["core_property"] else 1, e["source"], e["target"]))
        atomic_edges = atomic_edges[:atomic_cap]
        closure_input = [{"a": e["source"], "b": e["target"], "type": PRIM} for e in atomic_edges]
        undirected = [(e["source"], e["target"]) for e in atomic_edges]
        direct_pairs = {frozenset((e["source"], e["target"])) for e in atomic_edges}
        partic = set()
        for e in atomic_edges:
            partic.add(e["source"]); partic.add(e["target"])
        n_just = sum(1 for e in atomic_edges if e["locally_justifiable"])

    # core-ness of an unordered pair (any contributing core property) -> path optionality audit
    pair_core = {}
    for e in atomic_edges:
        k = frozenset((e["source"], e["target"]))
        pair_core[k] = pair_core.get(k, False) or e["core_property"]

    justifiable_pairs = {frozenset((e["source"], e["target"]))
                         for e in atomic_edges if e["locally_justifiable"]}

    def min_sent_dist(a, b):
        best = None
        for sa in sent_of[a]:
            for sb in sent_of[b]:
                d = abs(sa - sb)
                best = d if best is None else min(best, d)
        return best

    # ---- closure -> PRESENT deduction-required located_in query edges ----
    # DocRED annotates geographic containment near-TRANSITIVELY (a place's country P17 is
    # almost always stated directly), so -- unlike kinship, whose grand/uncle composites are
    # OUTSIDE DocRED's inventory -- pure never-annotated transitive pairs are RARE here.
    # We therefore build the present stratum from TWO honest sub-types:
    #   (i)  never_annotated : pairs NOT in the annotated edge set, derivable >=2-hop, non-local.
    #        composed_only in the STRICT sense (never an annotated edge => non-circular), the
    #        direct kinship analog. Rare but pure.
    #   (ii) held_out : a directly-annotated located_in edge (a,b) that is ALSO independently
    #        derivable via an ALTERNATIVE >=2-hop directed path through OTHER edges (a REDUNDANT
    #        edge), with a,b NON-LOCAL (min_sent_dist>=2 => the fact is not readable off one
    #        span). Gold is DOUBLY certified (annotated AND derivable). The edge stays in
    #        atomic_edges (drop-in KB unchanged); the consumer ABLATES the single edge (a,b)
    #        before querying, then the engine must DEDUCE it. SOUND: removing a redundant edge
    #        preserves the full transitive closure, so all absent/other-present gold is unchanged.
    D, nbrs, n_fired = forward_closure(KIN, closure_input)
    n_modeb = sum(1 for ts in D.values() if len(ts) > 1)

    # directed located_in adjacency (a->b) for held-out alternative-path reachability
    dir_adj = {}
    for e in atomic_edges:
        dir_adj.setdefault(e["source"], set()).add(e["target"])

    def dir_path(a, b, exclude_direct=False):
        """Shortest DIRECTED located_in path a->..->b (the actual derivation, descendant->ancestor),
        optionally EXCLUDING the direct (a,b) edge (for held-out queries). Returns node list or None.
        Soundness: D[(a,b)]=={located_in} is derived ONLY by located_in o located_in, so a directed
        located_in path a->..->b must exist -- this reconstructs it (vs an undirected path, which
        could traverse a 'contains' edge backwards and misrepresent the derivation)."""
        prev = {a: None}; dq = deque([a])
        while dq:
            n = dq.popleft()
            for m in dir_adj.get(n, ()):
                if exclude_direct and n == a and m == b:   # skip the direct edge under test
                    continue
                if m not in prev:
                    prev[m] = n
                    if m == b:
                        path = [b]
                        while prev[path[-1]] is not None:
                            path.append(prev[path[-1]])
                        return path[::-1]
                    dq.append(m)
        return None

    def present_record(a, b, path, kind, held):
        path_edges = [frozenset((path[i], path[i + 1])) for i in range(len(path) - 1)]
        return {
            "source": a, "target": b,
            "relation_surface": "located in", "primitive": PRIM, "relation_type": PRIM,
            "is_query": True, "hop_count": len(path) - 1,
            "derivation_path": path[1:-1],
            "query_kind": kind,
            "held_out_edge": held,                 # consumer must drop the (source,target) atomic edge before querying
            "composed_only": (kind == "never_annotated"),
            "fully_readable": all(e in justifiable_pairs for e in path_edges),
            "path_uses_optional_property": any(not pair_core.get(e, False) for e in path_edges),
        }

    never_ann = []
    for (a, b), ts in D.items():
        if a == b or ts != {PRIM}:
            continue
        if frozenset((a, b)) in direct_pairs:      # this sub-type is NOT directly annotated
            continue
        msd = min_sent_dist(a, b)
        if msd is not None and msd <= 1:           # locally readable -> not deduction-required
            continue
        path = dir_path(a, b)                       # the actual DIRECTED located_in derivation
        if not path or len(path) - 1 < 2:
            continue
        never_ann.append(present_record(a, b, path, "never_annotated", False))

    held_out = []
    for (a, b) in sorted((e["source"], e["target"]) for e in atomic_edges):
        msd = min_sent_dist(a, b)
        if msd is not None and msd <= 1:           # held-out fact must be non-local
            continue
        seed_wo = [{"a": e["source"], "b": e["target"], "type": PRIM}
                   for e in atomic_edges if (e["source"], e["target"]) != (a, b)]
        Dw, _, _ = forward_closure(KIN, seed_wo)    # authoritative: derivable WITHOUT the direct edge?
        if Dw.get((a, b)) != {PRIM}:
            continue
        path = dir_path(a, b, exclude_direct=True)
        if not path or len(path) - 1 < 2:
            continue
        held_out.append(present_record(a, b, path, "held_out", True))

    never_ann.sort(key=lambda q: (q["hop_count"], q["source"], q["target"]))
    held_out.sort(key=lambda q: (q["hop_count"], q["source"], q["target"]))
    n_present_full = len(never_ann) + len(held_out)
    present_truncated = n_present_full > present_cap
    present = never_ann[:present_cap]              # keep ALL never_annotated (rare, valuable) first
    present += held_out[:max(0, present_cap - len(present))]

    # ---- ABSENT no-derivation pairs (no containment path in EITHER direction) ----
    comps = components(partic, undirected)
    comp_of = {}
    for ci, c in enumerate(comps):
        for n in c:
            comp_of[n] = ci
    pl = sorted(partic)
    cross, sib = [], []
    for i in range(len(pl)):
        for j in range(i + 1, len(pl)):
            a, b = pl[i], pl[j]
            if D.get((a, b)) or D.get((b, a)):   # some containment path one way -> NOT absent
                continue
            if comp_of[a] != comp_of[b]:
                cross.append((a, b))
            else:
                sib.append((a, b))
    # stratified deterministic cap: interleave cross-component & sibling pairs
    absent = []
    ic = isb = 0
    while len(absent) < absent_cap and (ic < len(cross) or isb < len(sib)):
        if ic < len(cross) and (len(absent) % 2 == 0 or isb >= len(sib)):
            a, b = cross[ic]; ic += 1
            absent.append({"source": a, "target": b, "reason": "different_component",
                           "is_absent": True, "same_component": False})
        elif isb < len(sib):
            a, b = sib[isb]; isb += 1
            absent.append({"source": a, "target": b, "reason": "same_component_sibling",
                           "is_absent": True, "same_component": True})
    absent_truncated = (len(cross) + len(sib)) > absent_cap
    n_abs_diff = sum(1 for p in absent if p["reason"] == "different_component")
    n_abs_sib = sum(1 for p in absent if p["reason"] == "same_component_sibling")

    # ---- nodes ----
    nodes = []
    for eid in sorted(partic):
        nodes.append({
            "entity_id": eid,
            "surface": longest_name(vertexSet[eid]),
            "type": entity_type(vertexSet[eid]),
            "admin_level": admin_level(sents, vertexSet[eid]),
            "mention_spans": node_spans[eid],
            "wikidata_qid": None,
        })

    hop_hist = {}
    for q in present:
        hop_hist[str(q["hop_count"])] = hop_hist.get(str(q["hop_count"]), 0) + 1
    char_len = len(text)
    n_tokens = sum(len(s) for s in sents)
    offset_ok_frac = round(offok / offtot, 4) if offtot else 1.0
    rel_set = sorted({p for e in atomic_edges for p in e["wikidata_properties"]})

    gold_graph = {
        "doc_id": title, "source": source, "split": split,
        "nodes": nodes,
        "atomic_edges": atomic_edges,
        "query_edges": present,
        "absent_relation_pairs": absent,
        "absent_pairs_source": "structural_closure",
        "contradiction_pairs": contradictions,
    }
    row = {
        "input": text,
        "output": json.dumps(gold_graph, ensure_ascii=False),
        "metadata_doc_id": title,
        "metadata_source": source,
        "metadata_split": split,
        "metadata_fold": int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 5,
        "metadata_n_entities": len(vertexSet),
        "metadata_n_loc_entities": len(partic),
        "metadata_n_atomic_edges": len(atomic_edges),
        "metadata_n_core_atomic_edges": sum(1 for e in atomic_edges if e["core_property"]),
        "metadata_atomic_truncated": atomic_truncated,
        "metadata_n_locally_justifiable_edges": n_just,
        "metadata_locally_justifiable_frac": round(n_just / len(atomic_edges), 4) if atomic_edges else 0.0,
        "metadata_n_components": len(comps),
        "metadata_present_query_count": len(present),
        "metadata_present_never_annotated_count": sum(1 for q in present if q["query_kind"] == "never_annotated"),
        "metadata_present_held_out_count": sum(1 for q in present if q["query_kind"] == "held_out"),
        "metadata_composed_only_present_count": sum(1 for q in present if q["composed_only"]),
        "metadata_present_truncated": present_truncated,
        "metadata_absent_pair_count": len(absent),
        "metadata_absent_different_component_count": n_abs_diff,
        "metadata_absent_same_component_count": n_abs_sib,
        "metadata_absent_truncated": absent_truncated,
        "metadata_n_mode_b_conflicts": n_modeb,
        "metadata_n_contradiction_pairs": len(contradictions),
        "metadata_char_len": char_len,
        "metadata_n_tokens": n_tokens,
        "metadata_hop_histogram": json.dumps(hop_hist),
        "metadata_n_ge_2500_chars": int(char_len >= 2500),
        "metadata_has_3000_char": bool(char_len >= 3000),
        "metadata_offset_ok_frac": offset_ok_frac,
        "metadata_n_fired_closure": n_fired,
        "metadata_relation_set": json.dumps(rel_set),
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
        present_na_total = present_ho_total = 0
        abs_diff_total = abs_sib_total = modeb_total = contra_total = 0
        offoks = []; justs = []
        hop_all = {}; prop_all = {}; level_all = {}
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
                present_na_total += row["metadata_present_never_annotated_count"]
                present_ho_total += row["metadata_present_held_out_count"]
                abs_diff_total += row["metadata_absent_different_component_count"]
                abs_sib_total += row["metadata_absent_same_component_count"]
                modeb_total += row["metadata_n_mode_b_conflicts"]
                contra_total += row["metadata_n_contradiction_pairs"]
                offoks.append(row["metadata_offset_ok_frac"])
                if row["metadata_n_atomic_edges"]:
                    justs.append(row["metadata_n_locally_justifiable_edges"] / row["metadata_n_atomic_edges"])
                for q in gg["query_edges"]:
                    hop_all[str(q["hop_count"])] = hop_all.get(str(q["hop_count"]), 0) + 1
                for e in gg["atomic_edges"]:
                    for p in e["wikidata_properties"]:
                        prop_all[p] = prop_all.get(p, 0) + 1
                for n in gg["nodes"]:
                    level_all[n["admin_level"]] = level_all.get(n["admin_level"], 0) + 1
            if max_docs and ndoc >= max_docs:
                break
        rows_by_source[source] = rows
        stats[source] = dict(
            n_docs=len(rows), present_total=present_total,
            present_never_annotated=present_na_total, present_held_out=present_ho_total,
            absent_total=absent_total,
            absent_different_component=abs_diff_total, absent_same_component_sibling=abs_sib_total,
            composed_only_present=comp_present, mode_b_conflicts=modeb_total,
            contradiction_pairs=contra_total, hop_hist=hop_all, property_hist=prop_all,
            admin_level_hist=level_all,
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
