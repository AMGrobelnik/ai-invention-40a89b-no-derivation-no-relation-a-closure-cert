#!/usr/bin/env python3
"""Corpus parsers -> per-document GOLD GRAPHS (zero LLM, gold annotations only).

Three real temporal corpora, each emitting one "arm" = (algebra, per-doc gold graphs):

  MATRES        POINT algebra on event start-points. Relation + GLOBAL token-id nodes from
                CogComp MATRES txt; per-pair sentence distance (locality) from the
                sentence-aligned qiangning EMNLP-19 XML (SOURCE=E<tok>). Expect all pairs
                same/adjacent sentence -> deduction-required proxy fails for ~all -> N*~0 (control).

  TDDMan        ALLEN-13 (strict atomic map). Manual >1-sentence-apart pairs from TDDiscourse
                TSV; EVERY pair is deduction-required by construction (non-circularity anchor),
                no source text needed.

  NarrativeTime POINT algebra on segment start-coords (PRIMARY, EXACT) + ALLEN interval arm
                (secondary, lower-bound). Dense full-coverage human timeline (every pair of
                main-axis segments has a determinate relation) from the NarrativeTime
                annotator file. Locality from segment sentence index.

Each arm is cached to ./cache/<arm>_graphs.json for reuse by later tiers.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from loguru import logger

DATA = Path(__file__).parent / "data"
CACHE = Path(__file__).parent / "cache"
CACHE.mkdir(exist_ok=True)

# ---- relation maps (relation symbols match qualreas algebra symbols) -----------------
MATRES_POINT = {"BEFORE": ["<"], "AFTER": [">"], "EQUAL": ["="]}  # VAGUE -> not evaluable
TDDMAN_ALLEN_STRICT = {"b": ["B"], "a": ["BI"], "i": ["DI"], "ii": ["D"], "s": ["E"]}
# sensitivity (broad) map for TDDMan robustness
TDDMAN_ALLEN_BROAD = {"b": ["B"], "a": ["BI"], "i": ["DI", "SI", "FI"],
                      "ii": ["D", "S", "F"], "s": ["E", "S", "SI", "F", "FI"]}


def _sentence_token_map(text: str) -> list[int]:
    """Map each whitespace token index -> sentence index (proxy locality segmentation)."""
    toks = text.split()
    sent_of = []
    s = 0
    for t in toks:
        sent_of.append(s)
        # bump sentence after a token ending in sentence-final punctuation
        if re.search(r"[.!?]$", t) and len(t) > 1:
            s += 1
        elif t in (".", "!", "?"):
            s += 1
    return sent_of


# ======================================================================================
# MATRES
# ======================================================================================

def _load_qiangning_pairs(xml_path: Path) -> list[dict]:
    out = []
    for line in xml_path.read_text(errors="ignore").splitlines():
        line = line.strip()
        if not line.startswith("<SENTENCE"):
            continue
        head = line.split(">", 1)[0]
        attrs = dict(re.findall(r'(\w+)="([^"]*)"', head))
        out.append(attrs)
    return out


def parse_matres() -> dict:
    """Return {docid: gold_doc} for the MATRES POINT arm."""
    # locality lookup keyed by (docid, src_tok, tgt_tok) -> sentdiff, from qiangning XML
    loc: dict[tuple, dict] = {}
    for fn in ["trainset-temprel.xml", "testset-temprel.xml"]:
        p = DATA / "NeuralTemporalRelation-EMNLP19" / "data" / fn
        if not p.exists():
            continue
        for a in _load_qiangning_pairs(p):
            try:
                s = int(a["SOURCE"][1:]); t = int(a["TARGET"][1:])
            except (KeyError, ValueError):
                continue
            loc[(a["DOCID"], s, t)] = {
                "sentdiff": int(a.get("SENTDIFF", -1)),
                "s_sent": int(a.get("SOURCE_SENTID", -1)),
                "t_sent": int(a.get("TARGET_SENTID", -1)),
            }
    docs: dict[str, dict] = {}
    matched = 0; total = 0
    for fn in ["timebank.txt", "aquaint.txt", "platinum.txt"]:
        p = DATA / "MATRES" / fn
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            parts = line.split("\t")
            if len(parts) < 6:
                continue
            docid, _v1, _v2, i1, i2, rel = parts[:6]
            try:
                t1 = int(i1); t2 = int(i2)
            except ValueError:
                continue
            total += 1
            if rel not in MATRES_POINT:        # VAGUE -> skip (not evaluable, no constraint)
                continue
            d = docs.setdefault(docid, {"docid": docid, "algebra": "POINT", "edges": []})
            info = loc.get((docid, t1, t2)) or loc.get((docid, t2, t1))
            if info is not None:
                matched += 1
                sd = info["sentdiff"]
            else:
                sd = None
            u = f"E{t1}"; v = f"E{t2}"
            d["edges"].append({"u": u, "v": v, "rels": MATRES_POINT[rel], "gold": rel,
                               "sentdiff": sd, "tok_dist": abs(t1 - t2)})
    logger.info(f"MATRES: {len(docs)} docs, qiangning locality matched {matched}/{total} non-vague pairs")
    return {"arm": "MATRES_point", "algebra": "POINT", "docs": docs,
            "locality_match_rate": (matched / total) if total else 0.0}


# ======================================================================================
# TDDMan
# ======================================================================================

def parse_tddman(broad: bool = False) -> dict:
    rel_map = TDDMAN_ALLEN_BROAD if broad else TDDMAN_ALLEN_STRICT
    docs: dict[str, dict] = {}
    for fn in ["TDDManTrain.tsv", "TDDManDev.tsv", "TDDManTest.tsv"]:
        p = DATA / "TDDiscourse" / "TDDMan" / fn
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            docid, e1, e2, rel = parts[:4]
            rel = rel.strip()
            if rel not in rel_map:
                continue
            d = docs.setdefault(docid, {"docid": docid, "algebra": "ALLEN13", "edges": []})
            d["edges"].append({"u": e1, "v": e2, "rels": rel_map[rel], "gold": rel,
                               "sentdiff": None, "deduction_required": True})  # all non-local
    arm = "TDDMan_allen_broad" if broad else "TDDMan_allen"
    logger.info(f"TDDMan ({'broad' if broad else 'strict'}): {len(docs)} docs")
    return {"arm": arm, "algebra": "ALLEN13", "docs": docs, "all_deduction_required": True}


# ======================================================================================
# NarrativeTime
# ======================================================================================

def _parse_time(t: str):
    """Parse a NarrativeTime timeline coordinate 'a:b' / 'a' / 'a.b' -> (start, end) floats."""
    t = str(t).strip()
    if not t:
        return None
    if ":" in t:
        a, b = t.split(":", 1)
        try:
            return (float(a), float(b))
        except ValueError:
            return None
    try:
        x = float(t)
        return (x, x)
    except ValueError:
        return None


def _allen_from_intervals(a: tuple, b: tuple) -> str | None:
    """Atomic Allen-13 relation between two PROPER intervals (qualreas symbols). None if degenerate."""
    as_, ae = a; bs, be = b
    if not (ae > as_ and be > bs):   # require proper intervals
        return None
    if ae < bs:
        return "B"
    if as_ > be:
        return "BI"
    if ae == bs:
        return "M"
    if as_ == be:
        return "MI"
    # overlapping configurations
    if as_ == bs and ae == be:
        return "E"
    if as_ == bs:
        return "S" if ae < be else "SI"
    if ae == be:
        return "F" if as_ > bs else "FI"
    if as_ < bs and ae > be:
        return "DI"
    if as_ > bs and ae < be:
        return "D"
    if as_ < bs < ae < be:
        return "O"
    if bs < as_ < be < ae:
        return "OI"
    return None


def parse_narrativetime(annotator: str = "a1") -> dict:
    """Dense POINT (start-coord) gold graph + ALLEN interval arm from NarrativeTime."""
    p = DATA / "narrative_time" / "corpus" / "timebank" / "nt_format" / f"tbd_{annotator}.jsonl"
    if not p.exists():
        return {"arm": "NarrativeTime_point", "algebra": "POINT", "docs": {}, "status": "missing"}
    docs_point: dict[str, dict] = {}
    docs_allen: dict[str, dict] = {}
    n_branch = 0; n_main = 0
    for line in p.read_text().splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        docid = rec["id"]
        text = rec.get("text", "")
        sent_of = _sentence_token_map(text)
        ntok = len(sent_of)
        eo = rec.get("event_order", {})
        # collect main-axis segments with a parseable time coordinate
        segs = {}
        for k, v in eo.items():
            if v.get("branch", ""):     # skip hypothetical/branch segments -> keep linear timeline
                n_branch += 1
                continue
            iv = _parse_time(v.get("time", ""))
            if iv is None:
                continue
            n_main += 1
            span = v.get("span", [0, 0])
            tok0 = max(0, min(span[0], ntok - 1)) if ntok else 0
            sent = sent_of[tok0] if ntok else 0
            segs[k] = {"interval": iv, "start": iv[0], "sent": sent, "factuality": v.get("factuality", "")}
        keys = list(segs.keys())
        if len(keys) < 2:
            continue
        pe = []  # point edges
        ae = []  # allen edges
        for ii in range(len(keys)):
            for jj in range(ii + 1, len(keys)):
                ku, kv = keys[ii], keys[jj]
                su, sv = segs[ku]["start"], segs[kv]["start"]
                rel = "<" if su < sv else (">" if su > sv else "=")
                sd = abs(segs[ku]["sent"] - segs[kv]["sent"])
                pe.append({"u": ku, "v": kv, "rels": [rel], "gold": rel, "sentdiff": sd,
                           "deduction_required": sd > 1})
                al = _allen_from_intervals(segs[ku]["interval"], segs[kv]["interval"])
                if al is not None:
                    ae.append({"u": ku, "v": kv, "rels": [al], "gold": al, "sentdiff": sd,
                               "deduction_required": sd > 1})
        docs_point[docid] = {"docid": docid, "algebra": "POINT", "edges": pe,
                             "n_segments": len(keys)}
        docs_allen[docid] = {"docid": docid, "algebra": "ALLEN13", "edges": ae,
                             "n_segments": len(keys)}
    logger.info(f"NarrativeTime[{annotator}]: {len(docs_point)} docs, "
                f"{n_main} main-axis segments, {n_branch} branch segments skipped")
    return {
        "point": {"arm": "NarrativeTime_point", "algebra": "POINT", "docs": docs_point},
        "allen": {"arm": "NarrativeTime_allen", "algebra": "ALLEN13", "docs": docs_allen},
        "n_main_axis_segments": n_main, "n_branch_segments_skipped": n_branch,
    }


def cache_all() -> dict:
    """Parse every arm and cache to ./cache/. Returns a manifest with per-arm doc/edge counts."""
    manifest = {}
    matres = parse_matres()
    tdd = parse_tddman(broad=False)
    tdd_b = parse_tddman(broad=True)
    nt = parse_narrativetime("a1")
    arms = {
        "MATRES_point": matres,
        "TDDMan_allen": tdd,
        "TDDMan_allen_broad": tdd_b,
        "NarrativeTime_point": nt.get("point", {"docs": {}}),
        "NarrativeTime_allen": nt.get("allen", {"docs": {}}),
    }
    for name, arm in arms.items():
        docs = arm.get("docs", {})
        nedges = sum(len(d["edges"]) for d in docs.values())
        (CACHE / f"{name}_graphs.json").write_text(json.dumps(arm))
        manifest[name] = {"n_docs": len(docs), "n_edges": nedges,
                          "algebra": arm.get("algebra", "?")}
    manifest["MATRES_locality_match_rate"] = matres.get("locality_match_rate")
    manifest["NarrativeTime_main_axis_segments"] = nt.get("n_main_axis_segments")
    manifest["NarrativeTime_branch_skipped"] = nt.get("n_branch_segments_skipped")
    return manifest


if __name__ == "__main__":
    import sys
    logger.remove(); logger.add(sys.stdout, level="INFO")
    print(json.dumps(cache_all(), indent=2))
