#!/usr/bin/env python3
"""Per-corpus loaders -> a uniform Scene representation.

A Scene reconstructs ONE gold relation-graph from a published spatial-QA item:
  nodes   : objects/blocks (canonical id -> surface, char_spans, mention_count, type)
  edges   : every STATED native relation (the KB edges an honest local reader
            would extract) split into rcc8 / cardinal_direction by src/algebra.py
  queries : held-out query pair(s) with gold (where recoverable) + provenance.

No closure, no LLM.  Char-offset spans are emitted ONLY where the source provides
them (SpartQA SOT_text offsets; StepGame single-letter agents located by exact
search).  Where surface->offset cannot be recovered without fabrication we set
char_spans=[] and flag char_spans_recoverable=False (per the plan).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from algebra import map_relation, map_relation_list

# ----------------------------------------------------------------------------- #
#  helpers
# ----------------------------------------------------------------------------- #
def _spans_of(text: str, surface: str, max_spans: int = 10):
    """Exact char-offset spans of `surface` in `text` (word-boundary for short ids)."""
    if not surface:
        return []
    if len(surface) <= 2:  # single-letter agents (StepGame) -> word boundary
        pat = re.compile(r"\b" + re.escape(surface) + r"\b")
    else:
        pat = re.compile(re.escape(surface))
    out = [[m.start(), m.end()] for m in pat.finditer(text)]
    return out[:max_spans]


def _sparp_node_type(nid: str) -> str:
    if nid in ("-1",):
        return "world_root"
    if "x" in nid:
        return "object"
    return "block"


# ----------------------------------------------------------------------------- #
#  SpaRP (PS1=SpaRTUN dense RCC-8+directional ; PS2=StepGame cardinal)
#  symbolic_context gives the stated KB edges DIRECTLY (no NL parsing needed).
# ----------------------------------------------------------------------------- #
def load_sparp(rows, *, dataset, split, license, source, is_templated):
    scenes = []
    for i, r in enumerate(rows):
        try:
            sc = json.loads(r["symbolic_context"])
        except (json.JSONDecodeError, KeyError, TypeError):
            continue
        text = r.get("context", "") or ""
        nodes, edges, stated_pairs = {}, [], set()
        for key, rels in sc.items():
            if "-->" not in key:
                continue
            a, b = key.split("-->")
            a, b = a.strip(), b.strip()
            for nid in (a, b):
                if nid not in nodes:
                    nodes[nid] = {"surface": nid, "char_spans": [], "mention_count": 0,
                                  "node_type": _sparp_node_type(nid)}
            m = map_relation_list(rels)
            edges.append({
                "src": a, "dst": b, "native_relation": list(rels),
                "algebra": m["algebra"], "canonical": m["canonical"],
                "subtypes": m["subtypes"], "unmapped": m["unmapped"],
                "is_root_edge": ("-1" in (a, b)),
                "src_span": None, "rel_span": None, "dst_span": None,
            })
            stated_pairs.add(frozenset({a, b}))
        sq = r.get("symbolic_question")
        if not (isinstance(sq, list) and len(sq) == 2):
            continue
        qa, qb = sq[0].strip(), sq[1].strip()
        for nid in (qa, qb):
            if nid not in nodes:
                nodes[nid] = {"surface": nid, "char_spans": [], "mention_count": 0,
                              "node_type": _sparp_node_type(nid)}
        targets = r.get("targets") or []
        gm = map_relation_list(targets)
        scenes.append({
            "dataset": dataset, "doc_id": f"{dataset}_{split}_{i}", "split": split,
            "text": text, "is_templated": is_templated, "is_natural_text": False,
            "license": license, "source": source, "char_spans_recoverable": False,
            "nodes": nodes, "edges": edges, "stated_pairs": stated_pairs,
            "queries": [{
                "src": qa, "dst": qb, "gold_native": list(targets),
                "gold_canonical": gm["canonical"], "gold_algebra": gm["algebra"],
                "answer_kind": r.get("question_type", "FR"), "query_kind": "designed",
                "gold_recoverable": True, "dataset_num_hop": r.get("num_hop"),
            }],
        })
    return scenes


# ----------------------------------------------------------------------------- #
#  StepGame (clean TrainVersion: single linear k-hop chain, 8 cardinal relations)
#  Structural graph reconstructed by extracting the single-letter agents stated
#  in each sentence.  This is the SINGLE-CHAIN CONTRAST arm (expected ~0 bite).
# ----------------------------------------------------------------------------- #
_STEP_Q = re.compile(r"agent\s+([A-Za-z0-9]+)\s+to the agent\s+([A-Za-z0-9]+)", re.I)
_STEP_CARDINAL = ["upper-left", "upper-right", "lower-left", "lower-right",
                  "above", "below", "left", "right"]


def _stepgame_sentence_entities(sent: str):
    return sorted(set(re.findall(r"\b([A-Z])\b", sent)))


# Best-effort cardinal-keyword extraction for StepGame story sentences.  StepGame
# uses ~100 crowdsourced paraphrase templates (incl. clock positions) so this is a
# COVERAGE-LIMITED tokeniser, not a full parser; uncovered sentences keep the raw
# sentence as native_relation.  (The structural single-chain finding does not
# depend on the exact relation -- StepGame is the contrast arm, expected bite=0.)
_STEP_KW = [
    ("upper-left", "NW"), ("upper left", "NW"), ("top-left", "NW"), ("top left", "NW"),
    ("upper-right", "NE"), ("upper right", "NE"), ("top-right", "NE"), ("top right", "NE"),
    ("lower-left", "SW"), ("lower left", "SW"), ("bottom-left", "SW"), ("bottom left", "SW"),
    ("lower-right", "SE"), ("lower right", "SE"), ("bottom-right", "SE"), ("bottom right", "SE"),
    ("above", "N"), ("below", "S"), ("left", "W"), ("right", "E"),
    ("over", "N"), ("under", "S"), ("top", "N"), ("bottom", "S"),
    ("north", "N"), ("south", "S"), ("east", "E"), ("west", "W"),
]
_STEP_CLOCK = {"12": "N", "3": "E", "6": "S", "9": "W"}


def _stepgame_relation(sent: str):
    s = sent.lower()
    canon = []
    for kw, c in _STEP_KW:
        if kw in s and c not in canon:
            canon.append(c)
    m = re.search(r"\b(\d{1,2})\s*(?:o'clock|:00|position)", s)
    if m and m.group(1) in _STEP_CLOCK:
        c = _STEP_CLOCK[m.group(1)]
        if c not in canon:
            canon.append(c)
    return canon


def load_stepgame(rows, *, dataset, split, license, source):
    scenes = []
    for i, r in enumerate(rows):
        story = r.get("story") or []
        if isinstance(story, str):
            story = [story]
        text = " ".join(story)
        nodes, edges, stated_pairs = {}, [], set()
        for sent in story:
            ents = _stepgame_sentence_entities(sent)
            # connect every pair of agents co-stated in the sentence (clean => 2)
            canon = _stepgame_relation(sent)
            for a in range(len(ents)):
                for b in range(a + 1, len(ents)):
                    s, d = ents[a], ents[b]
                    edges.append({
                        "src": s, "dst": d, "native_relation": [sent],
                        "algebra": "cardinal_direction", "canonical": canon,
                        "subtypes": ["direction"], "unmapped": [],
                        "tokenised": bool(canon), "source_sentence": sent,
                        "is_root_edge": False,
                        "src_span": None, "rel_span": None, "dst_span": None,
                    })
                    stated_pairs.add(frozenset({s, d}))
        for nid in {e for sent in story for e in _stepgame_sentence_entities(sent)}:
            sp = _spans_of(text, nid)
            nodes[nid] = {"surface": nid, "char_spans": sp, "mention_count": len(sp),
                          "node_type": "agent"}
        m = _STEP_Q.search(r.get("question", ""))
        if not m:
            continue
        qa, qb = m.group(1), m.group(2)
        for nid in (qa, qb):
            if nid not in nodes:
                nodes[nid] = {"surface": nid, "char_spans": _spans_of(text, nid),
                              "mention_count": 0, "node_type": "agent"}
        label = r.get("label", "")
        gm = map_relation(label)
        scenes.append({
            "dataset": dataset, "doc_id": f"{dataset}_{split}_{i}", "split": split,
            "text": text, "is_templated": True, "is_natural_text": False,
            "license": license, "source": source, "char_spans_recoverable": True,
            "nodes": nodes, "edges": edges, "stated_pairs": stated_pairs,
            "queries": [{
                "src": qa, "dst": qb, "gold_native": [label],
                "gold_canonical": [gm["canonical"]] if gm["canonical"] else [],
                "gold_algebra": gm["algebra"], "answer_kind": "FR",
                "query_kind": "designed", "gold_recoverable": True,
                "dataset_num_hop": r.get("k_hop"),
            }],
        })
    return scenes


# ----------------------------------------------------------------------------- #
#  SpartQA (Auto templated / Human semi-natural): reconstruct from the ANNOTATION
#  scene-graph (blocks + relations_between_blocks + relations_between_objects +
#  rel_with_block) WITH char offsets (SOT_text).  Held-out queries are ENUMERATED
#  deduction-required object/block pairs (the dataset's FR queries reference
#  objects by long compositional descriptions that cannot be resolved to ids
#  without an LLM; enumeration is the well-defined $0 structural-capacity measure).
# ----------------------------------------------------------------------------- #
def _first_span(phrases):
    if not phrases:
        return []
    p0 = phrases[0]
    sot = p0.get("SOT_text") or {}
    if "start" in sot and "end" in sot:
        return [[sot["start"], sot["end"]]]
    return []


def load_spartqa_annotation(ann_data, *, dataset, split, license, source, is_natural):
    scenes = []
    for i, sc in enumerate(ann_data):
        story = sc.get("story") or []
        if isinstance(story, str):
            story = [story]
        text = " ".join(story)
        nodes, edges, stated_pairs = {}, [], set()

        for blk in sc.get("blocks", []):
            bid = str(blk["id"])
            bphr = blk.get("phrases", [])
            nodes[bid] = {
                "surface": blk.get("name") or (bphr[0]["phrase"] if bphr else bid),
                "char_spans": _first_span(bphr),
                "mention_count": len(bphr), "node_type": "block",
            }
            for obj in blk.get("objects", []):
                oid = f"{bid}.{obj['id']}"
                ophr = obj.get("phrases", [])
                desc = " ".join(x for x in [obj.get("size"), obj.get("color"),
                                            obj.get("shape")] if x).strip()
                nodes[oid] = {
                    "surface": (ophr[0]["phrase"] if ophr else desc or oid),
                    "char_spans": _first_span(ophr),
                    "mention_count": len(ophr), "node_type": "object",
                }
                rwb = obj.get("rel_with_block")
                if rwb:
                    m = map_relation(rwb)
                    edges.append({
                        "src": oid, "dst": bid, "native_relation": [rwb],
                        "algebra": m["algebra"],
                        "canonical": [m["canonical"]] if m["canonical"] else [],
                        "subtypes": [m["subtype"]], "unmapped": [] if m["canonical"] else [rwb],
                        "is_root_edge": False,
                        "src_span": None, "rel_span": None, "dst_span": None,
                    })
                    stated_pairs.add(frozenset({oid, bid}))
            for rel in blk.get("relations_between_objects", []):
                s = f"{bid}.{rel['trejector']}"
                d = f"{bid}.{rel['landmark']}"
                ind = rel.get("spatial_indicator") or []
                ind = ind if isinstance(ind, list) else [ind]
                m = map_relation_list(ind)
                edges.append({"src": s, "dst": d, "native_relation": list(ind),
                              "algebra": m["algebra"], "canonical": m["canonical"],
                              "subtypes": m["subtypes"], "unmapped": m["unmapped"],
                              "is_root_edge": False,
                              "src_span": None, "rel_span": None, "dst_span": None})
                stated_pairs.add(frozenset({s, d}))

        for rel in sc.get("relations_between_blocks", []):
            s, d = str(rel["trejector"]), str(rel["landmark"])
            ind = rel.get("spatial_indicator")
            ind = ind if isinstance(ind, list) else [ind]
            m = map_relation_list(ind)
            edges.append({"src": s, "dst": d, "native_relation": list(ind),
                          "algebra": m["algebra"], "canonical": m["canonical"],
                          "subtypes": m["subtypes"], "unmapped": m["unmapped"],
                          "is_root_edge": False,
                          "src_span": None, "rel_span": None, "dst_span": None})
            stated_pairs.add(frozenset({s, d}))

        scenes.append({
            "dataset": dataset, "doc_id": f"{dataset}_{split}_{i}", "split": split,
            "text": text, "is_templated": (not is_natural), "is_natural_text": is_natural,
            "license": license, "source": source, "char_spans_recoverable": True,
            "nodes": nodes, "edges": edges, "stated_pairs": stated_pairs,
            "queries": [],  # filled by enumerate_queries in pipeline
        })
    return scenes


# ----------------------------------------------------------------------------- #
#  ReSQ (genuinely-natural anchor).  The public release ships natural stories +
#  YN questions but NO reusable SpRL scene-graph triples, so a gold stated-
#  relation graph is NOT recoverable without an LLM.  We emit one query per YN
#  question (the asked relation + yes/no) with an EMPTY stated graph and flag
#  stated_graph_recoverable=False -- honestly establishing that natural text
#  hosts no recoverable multi-path redundancy (the expected scope boundary).
# ----------------------------------------------------------------------------- #
def load_resq(data, *, dataset, split, license, source):
    scenes = []
    for i, ctx in enumerate(data):
        story = ctx.get("story") or []
        if isinstance(story, str):
            story = [story]
        text = " ".join(story)
        queries = []
        for q in ctx.get("questions", []):
            ans = q.get("answer") or []
            queries.append({
                "src": "?", "dst": "?", "gold_native": ans,
                "gold_canonical": [], "gold_algebra": "natural_text_unresolved",
                "answer_kind": q.get("q_type", "YN"), "query_kind": "natural_yn",
                "gold_recoverable": False, "dataset_num_hop": q.get("step_of_reasoning"),
                "question_text": q.get("question", ""),
                "commonsense_question": q.get("commonsense_question"),
            })
        scenes.append({
            "dataset": dataset, "doc_id": ctx.get("Context_id", f"{dataset}_{split}_{i}"),
            "split": split, "text": text, "is_templated": False, "is_natural_text": True,
            "license": license, "source": source, "char_spans_recoverable": False,
            "stated_graph_recoverable": False,
            "nodes": {}, "edges": [], "stated_pairs": set(), "queries": queries,
        })
    return scenes


def load_json_relaxed(path: Path):
    """Load a JSON file, falling back to JSONL if it is line-delimited."""
    txt = path.read_text()
    try:
        return json.loads(txt)
    except json.JSONDecodeError:
        return [json.loads(ln) for ln in txt.splitlines() if ln.strip()]


# ----------------------------------------------------------------------------- #
#  SpartQA-Human SpRL-triple annotation (human_{split}_annotation.json).
#  Per-sentence `spatial_description` triples: trajector/landmark entity_ids,
#  spatial_value (already canonical, e.g. NTPP / ABOVE), s_type (RCC8|Relative|..),
#  char offsets (SOT_text).  Entity_ids are scene-global -> natural mention dedup.
#  Negative ("not above") relations are recorded-but-excluded from the constraint
#  graph (they assert a relation does NOT hold; complement-encoding is out of scope).
# ----------------------------------------------------------------------------- #
def _eid(ent):
    ids = ent.get("entity_id") or []
    if not ids:
        return None
    return "e" + "_".join(str(x) for x in ids)


def load_spartqa_human(ann_obj, *, dataset, split, license, source):
    data = ann_obj["data"] if isinstance(ann_obj, dict) and "data" in ann_obj else ann_obj
    items = data.items() if isinstance(data, dict) else enumerate(data)
    scenes = []
    n_negative = 0
    for key, sc in items:
        if not isinstance(sc, dict):
            continue
        st = sc.get("story") or {}
        if not isinstance(st, dict):
            continue
        story_txt = st.get("story") or []
        if isinstance(story_txt, str):
            story_txt = [story_txt]
        text = " ".join(story_txt)
        nodes, edges, stated_pairs = {}, [], set()
        for sent_ann in st.get("annotations", []):
            for sd in sent_ann.get("spatial_description", []):
                tr, lm = sd.get("trajector"), sd.get("landmark")
                if not tr or not lm:
                    continue
                sid, did = _eid(tr), _eid(lm)
                if sid is None or did is None:
                    continue
                for ent, nid in ((tr, sid), (lm, did)):
                    sot = ent.get("SOT_text") or {}
                    span = [[sot["start"], sot["end"]]] if "start" in sot and "end" in sot else []
                    if nid not in nodes:
                        nodes[nid] = {"surface": ent.get("phrase") or ent.get("head") or nid,
                                      "char_spans": span, "mention_count": 1,
                                      "node_type": "object"}
                    else:
                        nodes[nid]["mention_count"] += 1
                        nodes[nid]["char_spans"] += span
                if sd.get("negative"):
                    n_negative += 1
                    continue  # exclude negatives from the positive constraint graph
                val = sd.get("spatial_value")
                if not val:
                    continue
                m = map_relation(str(val))
                ind = sd.get("spatial_indicator") or {}
                isot = ind.get("SOT_text") or {}
                rel_span = [isot["start"], isot["end"]] if "start" in isot else None
                edges.append({
                    "src": sid, "dst": did, "native_relation": [val],
                    "algebra": m["algebra"],
                    "canonical": [m["canonical"]] if m["canonical"] else [],
                    "subtypes": [m["subtype"]], "unmapped": [] if m["canonical"] else [val],
                    "is_root_edge": False,
                    "src_span": None, "rel_span": rel_span, "dst_span": None,
                    "s_type": sd.get("s_type"), "g_type": sd.get("g_type"),
                })
                stated_pairs.add(frozenset({sid, did}))
        scenes.append({
            "dataset": dataset, "doc_id": f"{dataset}_{split}_{key}", "split": split,
            "text": text, "is_templated": False, "is_natural_text": True,
            "license": license, "source": source, "char_spans_recoverable": True,
            "nodes": nodes, "edges": edges, "stated_pairs": stated_pairs, "queries": [],
        })
    return scenes, n_negative
