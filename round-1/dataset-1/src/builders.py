#!/usr/bin/env python3
"""Per-corpus gold temporal relation graph builders.

Each builder returns a list of per-document records:
    {"doc_id", "corpus", "fold", "text", "nodes": [...], "edges": [...], "warnings": [...]}

Canonical mappings (documented in the data card):

  NarrativeTime  -> relations derived by the AUTHORS' OWN code (narrative_time package),
                    reproducing the shipped nt_converted_to_tml TLINKs exactly. 7-way
                    relation mapped to SOUND Allen base-relation sets; start-point point
                    relation computed exactly from timeline coordinates when finite (else
                    sound mapping with non-convex {<,>} widened to {<,=,>}).
  TDDMan         -> {b,a,s,i,ii} mapped to tightest Allen base relation + coarse superset +
                    convex start-point relation.
  MATRES         -> event START-POINTS => point algebra; {BEFORE,AFTER,EQUAL,VAGUE}.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

from loguru import logger

import common as C

# --------------------------------------------------------------------------------------
# NarrativeTime
# --------------------------------------------------------------------------------------

# 7-way NarrativeTime relation -> SOUND Allen interval base-relation set.
NT_ALLEN_MAP = {
    "BEFORE": ["b", "m"],
    "AFTER": ["bi", "mi"],
    "INCLUDES": ["di", "si", "fi"],
    "IS_INCLUDED": ["d", "s", "f"],
    "SIMULTANEOUS": ["eq"],
    "OVERLAP": ["o", "oi"],
    "VAGUE": list(C.ALLEN_FULL),
}
# 7-way NarrativeTime relation -> SOUND start-point (point algebra) set (pre convex-closure).
NT_POINT_MAP = {
    "BEFORE": ["<", "="],
    "AFTER": [">", "="],
    "INCLUDES": ["<", "="],
    "IS_INCLUDED": [">", "="],
    "SIMULTANEOUS": ["="],
    "OVERLAP": ["<", ">"],       # non-convex -> widened to {<,=,>}
    "VAGUE": ["<", "=", ">"],
}


def _nt_token_offsets(text: str) -> list[int]:
    """Char start offset of each whitespace token (text.split(' ')); split(' ')+join(' ')
    is identity, so offsets are exact."""
    tokens = text.split(" ")
    offsets = []
    running = 0
    for i, tok in enumerate(tokens):
        offsets.append(running)
        running += len(tok) + 1  # token + the single separating space
    return offsets


def _load_nt_annotations(nt_root: Path, annotator: str):
    """Load NarrativeTime annotations (timeline) and merge TimeML refs (eid/eiid/class/DCT)
    from tbd_tml_metadata.jsonl, which carries refs for all 36 docs (the per-annotator
    _tml file ships refs for only one). Word spans match, so refs align by event index."""
    import json
    from narrative_time import conversion_utils as U   # type: ignore

    jsonl = nt_root / "corpus" / "timebank" / "nt_format" / f"tbd_{annotator}_tml.jsonl"
    anns = U.get_annotations(str(jsonl))  # renames event_order "type" -> "event_type"

    meta_path = nt_root / "corpus" / "timebank" / "nt_format" / "tbd_tml_metadata.jsonl"
    meta = {json.loads(l)["id"]: json.loads(l) for l in meta_path.read_text().splitlines()}
    merged = 0
    for ann in anns:
        md = meta.get(ann["id"])
        if md is None:
            continue
        if "event_refs" not in ann and "event_refs" in md and md.get("events") == ann.get("events"):
            ann["event_refs"] = md["event_refs"]
            merged += 1
        if "timex_refs" not in ann and "timex_refs" in md and md.get("timex") == ann.get("timex"):
            ann["timex_refs"] = md["timex_refs"]
        # Normalize optional ref fields to a uniform key set per doc. The authors'
        # add_invisible_events_to_event_order asserts coreferent events share identical
        # keys; heterogeneous optional fields (e.g. 'modality' present on only some events)
        # break it. These fields do not affect relation extraction (which uses only
        # event_type/time/branch), so filling missing ones is safe.
        OPT = ["class", "comment", "eventID", "signalID", "pos", "tense", "aspect",
               "cardinality", "polarity", "modality"]
        if "event_refs" in ann:
            present = {k for ref in ann["event_refs"].values() for k in ref if k in OPT}
            for ref in ann["event_refs"].values():
                for k in present:
                    ref.setdefault(k, "")
    logger.info(f"[NarrativeTime] merged TimeML refs into {merged} annotations from metadata")
    return anns


def build_narrativetime(nt_root: Path, fold_map: dict[str, str], segmenter: C.SentenceSegmenter,
                        annotator: str = "a1") -> list[dict]:
    sys.path.insert(0, str(nt_root))
    from narrative_time import conversion_utils as U   # type: ignore
    from narrative_time import event_relations as ER   # type: ignore

    anns = _load_nt_annotations(nt_root, annotator)
    logger.info(f"[NarrativeTime] loaded {len(anns)} annotations (annotator={annotator})")

    def start_coord(ev):
        try:
            iv = ER.to_interval(ev["time"], type_=ev["event_type"])
            return iv.start, iv.end
        except Exception:
            return None, None

    records = []
    for ann in anns:
        docid = ann["id"]
        text = ann["text"]
        tok_off = _nt_token_offsets(text)
        spans, omap = segmenter.assign(text)

        ev = U.get_events_and_timexes(ann, corpus_offset=0)

        # ----- nodes -----
        nodes = {}
        for nid, e in ev.items():
            l, r = e["span"]  # word indices into text.split(' ')
            cs = tok_off[l] if l < len(tok_off) else None
            if cs is not None and r < len(tok_off):
                ce = tok_off[r] + len(text.split(" ")[r])
            else:
                ce = cs
            sidx = omap.index_for(cs)
            is_timex = e.get("is_timex", False)
            func = e.get("functionInDocument")
            if is_timex and func == "CREATION_TIME":
                ntype = "dct"
            elif is_timex:
                ntype = "timex"
            else:
                ntype = "event"
            s0, e0 = start_coord(e)
            nodes[nid] = {
                "node_id": f"{docid}::{nid}",
                "node_type": ntype,
                "surface": e.get("text") or " ".join(text.split(" ")[l:r + 1]),
                "char_start": cs,
                "char_end": ce,
                "global_token_index": l,
                "sentence_index": sidx,
                "eiid": None if is_timex else nid,
                "tid": nid if is_timex else None,
                "eid": e.get("eid"),
                "event_class": e.get("class"),
                "nt_event_type": e.get("event_type"),
                "nt_time": e.get("time"),
                "nt_branch": e.get("branch"),
                "nt_start": (s0 if (s0 is not None and math.isfinite(s0)) else None),
                "nt_end": (e0 if (e0 is not None and math.isfinite(e0)) else None),
            }

        # order nodes canonically by (char_start, node id)
        order = sorted(nodes.keys(), key=lambda k: ((nodes[k]["char_start"] if nodes[k]["char_start"] is not None else 1 << 30), k))

        # ----- edges (full coverage: all unordered pairs) -----
        edges = []
        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                a, b = order[i], order[j]
                e1, e2 = ev[a], ev[b]
                same_branch = (e1["branch"] == e2["branch"])
                if same_branch:
                    nt_rel = ER.get_event_relation(e1, e2)
                else:
                    nt_rel = ER.get_event_relation_separate_branches(e1, e2)

                # start-point relation: exact from coordinates when finite & same branch
                sp_set = None
                vague_widened = False
                if same_branch:
                    s1, _ = start_coord(e1)
                    s2, _ = start_coord(e2)
                    if s1 is not None and s2 is not None and math.isfinite(s1) and math.isfinite(s2):
                        sp_set = ["<"] if s1 < s2 else (["="] if s1 == s2 else [">"])
                if sp_set is None:
                    sp_set, vague_widened = C.widen_if_nonconvex(NT_POINT_MAP[nt_rel])

                na, nb = nodes[a], nodes[b]
                loc = C.locality_fields(na["sentence_index"], nb["sentence_index"])
                edges.append({
                    "source": na["node_id"],
                    "target": nb["node_id"],
                    "native_relation": nt_rel,
                    "canonical_algebra": "interval_allen",
                    "canonical_relation_set": NT_ALLEN_MAP[nt_rel],
                    "startpoint_relation_set": sp_set,
                    "vague_widened": vague_widened,
                    "coarse_superset_set": None,
                    "edge_fold": fold_map.get(C.normalize_docid(docid), "train"),
                    **loc,
                })

        records.append({
            "doc_id": docid, "corpus": "narrativetime",
            "fold": fold_map.get(C.normalize_docid(docid), "train"),
            "text": text, "nodes": list(nodes.values()), "edges": edges, "warnings": [],
        })
    return records


# --------------------------------------------------------------------------------------
# TDDMan
# --------------------------------------------------------------------------------------

TDD_CODE_MAP = {
    "b":  {"native": "before",       "allen": ["b"],  "superset": ["b", "m"],         "point": ["<"]},
    "a":  {"native": "after",        "allen": ["bi"], "superset": ["bi", "mi"],       "point": [">"]},
    "s":  {"native": "simultaneous", "allen": ["eq"], "superset": ["eq"],             "point": ["="]},
    "i":  {"native": "includes",     "allen": ["di"], "superset": ["di", "si", "fi"], "point": ["<", "="]},
    "ii": {"native": "is_included",  "allen": ["d"],  "superset": ["d", "s", "f"],    "point": ["=", ">"]},
}


def _read_tdd_tsv(path: Path, split: str) -> list[tuple]:
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        p = line.rstrip("\n").split("\t")
        if len(p) < 4 or not p[0]:
            continue
        rows.append((p[0], p[1], p[2], p[3], split, (p[4].strip() if len(p) > 4 else None)))
    return rows


def build_tddman(tdd_dir: Path, tml_by_norm: dict[str, C.TmlDoc], fold_map: dict[str, str],
                 segmenter: C.SentenceSegmenter) -> tuple[list[dict], list[dict]]:
    """Returns (records, unmatched) where unmatched lists (docid, eid) pairs not found in .tml."""
    rows = []
    rows += _read_tdd_tsv(tdd_dir / "TDDManTrain.tsv", "train")
    rows += _read_tdd_tsv(tdd_dir / "TDDManDev.tsv", "dev")
    rows += _read_tdd_tsv(tdd_dir / "TDDManTest.tsv", "test")
    # phenomena annotations (test only): (docid,e1,e2) -> tag string
    phen = {}
    pf = tdd_dir / "TDDManTestPhenomena.tsv"
    if pf.exists():
        for line in pf.read_text(encoding="utf-8", errors="replace").splitlines():
            p = line.rstrip("\n").split("\t")
            if len(p) >= 5:
                phen[(p[0], p[1], p[2])] = p[4].strip()
    logger.info(f"[TDDMan] {len(rows)} gold pairs across train/dev/test; {len(phen)} phenomena-tagged test pairs")

    by_doc: dict[str, list] = {}
    for r in rows:
        by_doc.setdefault(r[0], []).append(r)

    records = []
    unmatched_counts: dict[tuple, int] = {}

    def note_unmatched(docid, eid, reason):
        unmatched_counts[(docid, eid, reason)] = unmatched_counts.get((docid, eid, reason), 0) + 1

    for docid, pairs in by_doc.items():
        norm = C.normalize_docid(docid)
        tml = tml_by_norm.get(norm)
        if tml is None:
            logger.warning(f"[TDDMan] no .tml for doc {docid}; skipping {len(pairs)} pairs")
            note_unmatched(docid, "*", "no_tml")
            continue
        text = tml.text
        spans, omap = segmenter.assign(text)
        eid2node = C.eid_to_event_node(tml)

        # ----- nodes: all events + timexes from the .tml -----
        nodes = {}
        for ev in tml.events:
            eid = ev.attrib.get("eid")
            sidx = omap.index_for(ev.char_start)
            nodes[f"e:{eid}"] = {
                "node_id": f"{docid}::{eid}", "node_type": "event", "surface": ev.surface,
                "char_start": ev.char_start, "char_end": ev.char_end,
                "global_token_index": None, "sentence_index": sidx,
                "eiid": None, "tid": None, "eid": eid,
                "event_class": ev.attrib.get("class"),
            }
        for tx in tml.timexes:
            tid = tx.attrib.get("tid")
            sidx = omap.index_for(tx.char_start)
            nodes[f"t:{tid}"] = {
                "node_id": f"{docid}::{tid}", "node_type": "timex", "surface": tx.surface,
                "char_start": tx.char_start, "char_end": tx.char_end,
                "global_token_index": None, "sentence_index": sidx,
                "eiid": None, "tid": tid, "eid": None,
                "event_class": None, "timex_type": tx.attrib.get("type"),
                "timex_value": tx.attrib.get("value"),
            }
        if tml.dct:
            nodes[f"t:{tml.dct['tid']}"] = {
                "node_id": f"{docid}::{tml.dct['tid']}", "node_type": "dct",
                "surface": tml.dct.get("surface"), "char_start": None, "char_end": None,
                "global_token_index": None, "sentence_index": None,
                "eiid": None, "tid": tml.dct["tid"], "eid": None, "event_class": None,
                "timex_value": tml.dct.get("value"),
            }

        # ----- edges: TDDMan gold (event-event) -----
        edges = []
        for (_, e1, e2, code, split, _native_phen) in pairs:
            n1, n2 = eid2node.get(e1), eid2node.get(e2)
            if n1 is None:
                note_unmatched(docid, e1, "eid_not_in_tml")
            if n2 is None:
                note_unmatched(docid, e2, "eid_not_in_tml")
            if n1 is None or n2 is None:
                continue
            m = TDD_CODE_MAP.get(code)
            if m is None:
                logger.warning(f"[TDDMan] unknown relation code {code!r} in {docid}")
                continue
            s1 = omap.index_for(n1.char_start)
            s2 = omap.index_for(n2.char_start)
            loc = C.locality_fields(s1, s2)
            sp_set, vw = C.widen_if_nonconvex(m["point"])
            edges.append({
                "source": f"{docid}::{e1}", "target": f"{docid}::{e2}",
                "native_relation": m["native"], "native_code": code,
                "canonical_algebra": "coarse_interval",
                "canonical_relation_set": m["allen"],
                "coarse_superset_set": m["superset"],
                "startpoint_relation_set": sp_set,
                "vague_widened": vw,
                "edge_fold": split,
                "phenomena": phen.get((docid, e1, e2)),
                **loc,
            })

        records.append({
            "doc_id": docid, "corpus": "tddman", "fold": fold_map.get(norm, "train"),
            "text": text, "nodes": list(nodes.values()), "edges": edges, "warnings": [],
        })
    unmatched = [{"doc_id": d, "eid": e, "reason": r, "n_pairs_dropped": c}
                 for (d, e, r), c in sorted(unmatched_counts.items())]
    return records, unmatched


# --------------------------------------------------------------------------------------
# MATRES
# --------------------------------------------------------------------------------------

MATRES_POINT_MAP = {
    "BEFORE": ["<"], "AFTER": [">"], "EQUAL": ["="], "VAGUE": ["<", "=", ">"],
}
_SENT_RE = re.compile(r'<SENTENCE ([^>]*)>(.*)</SENTENCE>')
_ATTR_RE = re.compile(r'(\w+)="([^"]*)"')
_END_PUNCT = re.compile(r'^[.!?]+$')


def _parse_qiangning(path: Path) -> dict[str, list[dict]]:
    """Parse a qiangning *-temprel.xml into {docid: [pair, ...]}."""
    by_doc: dict[str, list[dict]] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = _SENT_RE.match(line.strip())
        if not m:
            continue
        attrs = dict(_ATTR_RE.findall(m.group(1)))
        toks = []
        for t in m.group(2).split():
            if "///" not in t:
                continue
            parts = t.split("///")
            word = parts[0]
            pos = parts[2] if len(parts) > 2 else ""
            marker = parts[-1]
            toks.append((word, pos, marker))
        docid = attrs["DOCID"]
        by_doc.setdefault(docid, []).append({
            "source_g": int(re.sub(r"\D", "", attrs["SOURCE"])),
            "target_g": int(re.sub(r"\D", "", attrs["TARGET"])),
            "ssid": int(attrs["SOURCE_SENTID"]),
            "tsid": int(attrs["TARGET_SENTID"]),
            "label": attrs["LABEL"],
            "sentdiff": int(attrs["SENTDIFF"]),
            "toks": toks,
        })
    return by_doc


def _find_boundary(toks, p1, p2):
    """Index (exclusive) ending the first sentence in a SENTDIFF==1 span: just after the
    first sentence-final punctuation strictly after the E1 token."""
    for i in range(p1 + 1, min(p2 + 1, len(toks))):
        if _END_PUNCT.match(toks[i][0]):
            return i + 1
    return p2  # fallback: target token starts the second sentence


def build_matres(qiangning_dir: Path) -> list[dict]:
    train = _parse_qiangning(qiangning_dir / "trainset-temprel.xml")  # TimeBank + AQUAINT
    test = _parse_qiangning(qiangning_dir / "testset-temprel.xml")    # Platinum
    logger.info(f"[MATRES] trainset docs={len(train)} testset docs={len(test)}")

    def build_split(by_doc: dict[str, list[dict]], fold: str) -> list[dict]:
        recs = []
        for docid, pairs in by_doc.items():
            # Reconstruct sentences using LOCAL marker positions. MATRES SOURCE/TARGET ids
            # are the corpus's native event indices, NOT raw token positions, so we anchor
            # on the E1/E2 marker positions within each qiangning sentence instead. For a
            # SENTDIFF==1 span the boundary lies at the end of the source sentence, so the
            # left part equals the complete source sentence and the right part the complete
            # target sentence -> local positions transfer to the full sentence.
            sentences: dict[int, list[str]] = {}
            event_local: dict[int, tuple] = {}  # g -> (sid, local_pos, surface, pos)

            # process intra-sentence pairs first so full sentences are canonical
            for pr in sorted(pairs, key=lambda p: p["sentdiff"]):
                toks = pr["toks"]
                markers = [t[2] for t in toks]
                try:
                    p1 = markers.index("E1")
                    p2 = markers.index("E2")
                except ValueError:
                    continue
                g1, g2 = pr["source_g"], pr["target_g"]
                ssid, tsid, sdiff = pr["ssid"], pr["tsid"], pr["sentdiff"]
                words = [t[0] for t in toks]
                if sdiff == 0:
                    if ssid not in sentences or len(words) > len(sentences[ssid]):
                        sentences[ssid] = words
                    event_local.setdefault(g1, (ssid, p1, toks[p1][0], toks[p1][1]))
                    event_local.setdefault(g2, (ssid, p2, toks[p2][0], toks[p2][1]))
                else:
                    b = _find_boundary(toks, p1, p2)
                    left, right = words[:b], words[b:]
                    if ssid not in sentences or len(left) > len(sentences[ssid]):
                        sentences[ssid] = left
                    if tsid not in sentences or len(right) > len(sentences[tsid]):
                        sentences[tsid] = right
                    event_local.setdefault(g1, (ssid, p1, toks[p1][0], toks[p1][1]))
                    if p2 - b >= 0:
                        event_local.setdefault(g2, (tsid, p2 - b, toks[p2][0], toks[p2][1]))

            # assemble document text + per-sentence char starts --------------------------
            sent_char_start: dict[int, int] = {}
            running = 0
            for sid in sorted(sentences.keys()):
                sent_char_start[sid] = running
                running += len(" ".join(sentences[sid])) + 1
            doc_text = " ".join(" ".join(sentences[sid]) for sid in sorted(sentences.keys()))

            # nodes (char offset from LOCAL position; verified against the surface) -------
            nodes = {}
            n_null = 0
            for g, (sid, lp, surface, pos) in event_local.items():
                words = sentences.get(sid)
                cs = ce = None
                if words is not None and 0 <= lp < len(words) and words[lp] == surface:
                    cs = sent_char_start[sid] + len(" ".join(words[:lp])) + (1 if lp > 0 else 0)
                    ce = cs + len(surface)
                else:
                    n_null += 1
                nodes[g] = {
                    "node_id": f"{docid}::tok{g}", "node_type": "event",
                    "surface": surface, "char_start": cs, "char_end": ce,
                    "global_token_index": g, "sentence_index": sid,
                    "eiid": None, "tid": None, "eid": None, "event_class": None,
                    "pos": pos,
                }

            # edges ----------------------------------------------------------------------
            edges = []
            seen = set()
            for pr in pairs:
                key = (pr["source_g"], pr["target_g"])
                if key in seen:
                    continue
                seen.add(key)
                label = pr["label"]
                pt = MATRES_POINT_MAP.get(label, ["<", "=", ">"])
                sp_set, vw = C.widen_if_nonconvex(pt)
                loc = C.locality_fields(pr["ssid"], pr["tsid"])
                # SENTDIFF is the authoritative distance; cross-check
                if loc["sentence_distance"] != pr["sentdiff"]:
                    loc["sentence_distance"] = pr["sentdiff"]
                    loc["locality_class"] = C.locality_class(pr["sentdiff"])
                    loc["structural_deduction_required_proxy"] = pr["sentdiff"] >= 2
                    loc["locally_justifiable_proxy"] = pr["sentdiff"] <= 1
                edges.append({
                    "source": f"{docid}::tok{pr['source_g']}",
                    "target": f"{docid}::tok{pr['target_g']}",
                    "native_relation": label,
                    "canonical_algebra": "point",
                    "canonical_relation_set": pt,
                    "startpoint_relation_set": sp_set,
                    "vague_widened": vw,
                    "coarse_superset_set": None,
                    "edge_fold": fold,
                    **loc,
                })

            warns = []
            if not doc_text:
                warns.append("empty_reconstructed_text")
            if n_null:
                warns.append(f"{n_null}_events_without_char_offset")
            recs.append({
                "doc_id": docid, "corpus": "matres", "fold": fold,
                "text": doc_text, "nodes": list(nodes.values()), "edges": edges,
                "warnings": warns,
            })
        return recs

    return build_split(train, "train") + build_split(test, "test")


# --------------------------------------------------------------------------------------
# Optional 4th corpus: TimeBank-Dense gold (muk343 TLINKs) -- near-free
# --------------------------------------------------------------------------------------

# TimeBank-Dense relation labels -> canonical sets (point + Allen).
TBD_MAP = {
    "BEFORE":       {"allen": ["b"],  "superset": ["b", "m"],         "point": ["<"]},
    "AFTER":        {"allen": ["bi"], "superset": ["bi", "mi"],       "point": [">"]},
    "INCLUDES":     {"allen": ["di"], "superset": ["di", "si", "fi"], "point": ["<", "="]},
    "IS_INCLUDED":  {"allen": ["d"],  "superset": ["d", "s", "f"],    "point": ["=", ">"]},
    "SIMULTANEOUS": {"allen": ["eq"], "superset": ["eq"],             "point": ["="]},
    "VAGUE":        {"allen": list(C.ALLEN_FULL), "superset": list(C.ALLEN_FULL), "point": ["<", "=", ">"]},
}


def build_timebank_dense(tml_by_norm: dict[str, C.TmlDoc], fold_map: dict[str, str],
                         segmenter: C.SentenceSegmenter) -> list[dict]:
    records = []
    for norm, tml in tml_by_norm.items():
        docid = tml.docid
        text = tml.text
        spans, omap = segmenter.assign(text)
        eid2node = C.eid_to_event_node(tml)
        # eiid -> eid via MAKEINSTANCE
        eiid2eid = {eiid: a.get("eventID") for eiid, a in tml.makeinstance.items()}

        nodes = {}
        for ev in tml.events:
            eid = ev.attrib.get("eid")
            nodes[eid] = {
                "node_id": f"{docid}::{eid}", "node_type": "event", "surface": ev.surface,
                "char_start": ev.char_start, "char_end": ev.char_end,
                "global_token_index": None, "sentence_index": omap.index_for(ev.char_start),
                "eiid": None, "tid": None, "eid": eid, "event_class": ev.attrib.get("class"),
            }
        for tx in tml.timexes:
            tid = tx.attrib.get("tid")
            nodes[tid] = {
                "node_id": f"{docid}::{tid}", "node_type": "timex", "surface": tx.surface,
                "char_start": tx.char_start, "char_end": tx.char_end,
                "global_token_index": None, "sentence_index": omap.index_for(tx.char_start),
                "eiid": None, "tid": tid, "eid": None, "event_class": None,
            }
        if tml.dct and tml.dct.get("tid"):
            tid = tml.dct["tid"]
            nodes[tid] = {
                "node_id": f"{docid}::{tid}", "node_type": "dct", "surface": tml.dct.get("surface"),
                "char_start": None, "char_end": None, "global_token_index": None,
                "sentence_index": None, "eiid": None, "tid": tid, "eid": None,
                "event_class": None, "timex_value": tml.dct.get("value"),
            }

        edges = []
        for tl in tml.tlinks:
            rel = (tl.get("relType") or "").upper()
            src = tl.get("eventInstanceID") or tl.get("timeID")
            tgt = tl.get("relatedToEventInstance") or tl.get("relatedToTime")
            # resolve to eid / tid
            def resolve(x):
                if x is None:
                    return None
                if x in eiid2eid and eiid2eid[x]:
                    return eiid2eid[x]
                return x  # already an eid/tid (timeID)
            seid, teid = resolve(src), resolve(tgt)
            if seid not in nodes or teid not in nodes:
                continue
            m = TBD_MAP.get(rel)
            if m is None:
                continue
            s1 = nodes[seid]["sentence_index"]
            s2 = nodes[teid]["sentence_index"]
            loc = C.locality_fields(s1, s2)
            sp_set, vw = C.widen_if_nonconvex(m["point"])
            edges.append({
                "source": nodes[seid]["node_id"], "target": nodes[teid]["node_id"],
                "native_relation": rel, "canonical_algebra": "coarse_interval",
                "canonical_relation_set": m["allen"], "coarse_superset_set": m["superset"],
                "startpoint_relation_set": sp_set, "vague_widened": vw,
                "edge_fold": fold_map.get(norm, "train"), **loc,
            })

        records.append({
            "doc_id": docid, "corpus": "timebank_dense", "fold": fold_map.get(norm, "train"),
            "text": text, "nodes": list(nodes.values()), "edges": edges, "warnings": [],
        })
    return records
