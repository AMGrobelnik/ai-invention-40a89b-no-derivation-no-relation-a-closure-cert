#!/usr/bin/env python3
"""Build LLM-elicitation tasks (text + marked event pair + gold) and harvested
closure triangles for the three real temporal corpora.

  dense (NarrativeTime stand-in)  = TimeBank-Dense  (ALLEN, coarse)   <- .tml TLINKs
  noncirc (deduction anchor)      = TDDMan          (ALLEN, coarse)   <- TSV + .tml text
  gate (control, expect N*~0)     = MATRES          (POINT)           <- qiangning XML

Every emitted/gold relation is expressed in a shared COARSE vocabulary
{before, after, includes, is_included, simultaneous} (+ VAGUE/underdetermined) and
mapped to the arm's algebra (POINT or ALLEN). Recall is computed at the coarse-label
level; closure uses the mapped algebra sets.
"""
from __future__ import annotations

import random
import re
from collections import defaultdict
from pathlib import Path

from engine import build_allen_algebra, build_point_algebra

DATA = Path(__file__).parent / "data"

# ----------------------------------------------------------------------------------
# shared coarse vocabulary <-> algebra mappings
# ----------------------------------------------------------------------------------
COARSE_VOCAB_ALLEN = ["before", "after", "includes", "is_included", "simultaneous"]
COARSE_VOCAB_POINT = ["before", "after", "simultaneous"]

# coarse label -> POINT start-point set
COARSE_TO_POINT = {
    "before": frozenset({"<"}), "after": frozenset({">"}),
    "simultaneous": frozenset({"="}),
    "includes": frozenset({"<", "="}), "is_included": frozenset({"=", ">"}),
}
# coarse label -> ALLEN base set (strict atomic map; dossier Section 1B)
COARSE_TO_ALLEN = {
    "before": frozenset({"B"}), "after": frozenset({"BI"}),
    "includes": frozenset({"DI"}), "is_included": frozenset({"D"}),
    "simultaneous": frozenset({"E"}),
}
# atomic gold base symbol for recall (POINT arms only use the 3 point coarse labels)
COARSE_TO_POINT_ATOM = {"before": "<", "after": ">", "simultaneous": "="}

# corpus gold-label normalisation -> coarse vocab (or 'VAGUE')
TBDENSE_REL = {"BEFORE": "before", "AFTER": "after", "INCLUDES": "includes",
               "IS_INCLUDED": "is_included", "SIMULTANEOUS": "simultaneous",
               "IDENTITY": "simultaneous", "NONE": "VAGUE"}
TDDMAN_REL = {"b": "before", "a": "after", "i": "includes", "ii": "is_included", "s": "simultaneous"}
MATRES_REL = {"BEFORE": "before", "AFTER": "after", "EQUAL": "simultaneous", "VAGUE": "VAGUE"}


def coarse_to_set(coarse: str, algebra: str):
    """Map one coarse label to the arm's algebra relation set."""
    if coarse in ("VAGUE", "underdetermined", "UNDERDETERMINED"):
        return universe_set(algebra)
    if algebra == "POINT":
        return COARSE_TO_POINT[coarse]
    return COARSE_TO_ALLEN[coarse]


def universe_set(algebra: str):
    return (build_point_algebra() if algebra == "POINT" else build_allen_algebra()).universe


def emitted_set(coarse_labels, underdetermined: bool, algebra: str):
    """Union of coarse labels -> algebra set. underdetermined/empty -> universe."""
    if underdetermined or not coarse_labels:
        return universe_set(algebra)
    out = set()
    for c in coarse_labels:
        out |= set(coarse_to_set(c, algebra))
    return frozenset(out) if out else universe_set(algebra)


def gold_atom(coarse: str, algebra: str):
    """Atomic gold base symbol used for the recall indicator (None for VAGUE)."""
    if coarse == "VAGUE":
        return None
    if algebra == "POINT":
        return COARSE_TO_POINT_ATOM[coarse]
    return next(iter(COARSE_TO_ALLEN[coarse]))


# ----------------------------------------------------------------------------------
# .tml parsing (TimeBank-Dense / used for both dense + noncirc text)
# ----------------------------------------------------------------------------------
_TEXT_RE = re.compile(r"<TEXT>(.*?)</TEXT>", re.S)
_SEG_RE = re.compile(r'<EVENT\b[^>]*\beid="([^"]+)"[^>]*>(.*?)</EVENT>|<[^>]+>', re.S)
_MKI_RE = re.compile(r"<MAKEINSTANCE\b[^>]*>")
_TLINK_RE = re.compile(r"<TLINK\b[^>]*>")
_ATTR_RE = re.compile(r'(\w+)="([^"]*)"')


def _attrs(tag: str) -> dict:
    return dict(_ATTR_RE.findall(tag))


def parse_tml(path: Path) -> dict:
    """Return {plain_text, events:{eid:(start,end,word)}, sent_bounds, eiid2eid, tlinks}.

    Plain text is reconstructed from the <TEXT> block with all tags removed; a single
    space is inserted wherever tag removal would merge two non-space characters, so
    event char-spans are exact in the returned plain_text.
    """
    raw = path.read_text(errors="ignore")
    m = _TEXT_RE.search(raw)
    body = m.group(1) if m else raw
    buf: list[str] = []
    cur = 0
    events: dict[str, tuple] = {}

    def emit(seg: str):
        nonlocal cur
        if not seg:
            return
        if buf and buf[-1] and not buf[-1][-1].isspace() and not seg[0].isspace():
            buf.append(" "); cur += 1
        buf.append(seg); cur += len(seg)

    last = 0
    for mt in _SEG_RE.finditer(body):
        emit(body[last:mt.start()])
        last = mt.end()
        if mt.group(1) is not None:  # an EVENT
            eid = mt.group(1)
            word = re.sub(r"\s+", " ", mt.group(2)).strip()
            # ensure separation before the event word
            if buf and buf[-1] and not buf[-1][-1].isspace():
                buf.append(" "); cur += 1
            start = cur
            buf.append(word); cur += len(word)
            end = cur
            events[eid] = (start, end, word)
        else:
            emit(" ")  # other tag -> separator
    emit(body[last:])
    text = "".join(buf)
    text = re.sub(r"[ \t]+", " ", text)  # tidy horizontal whitespace (offsets recomputed below)

    # offsets above were computed on the untidied buffer; recompute events by exact word search
    # to stay robust to the tidy step (words are distinctive enough with position hints).
    # Simpler+robust: rebuild offsets from the tidy text using ordered word search.
    events_fixed: dict[str, tuple] = {}
    search_from = 0
    for eid, (s, e, word) in sorted(events.items(), key=lambda kv: kv[1][0]):
        if not word:
            continue
        idx = text.find(word, search_from)
        if idx < 0:
            idx = text.find(word)  # fall back to first occurrence
        if idx < 0:
            continue
        events_fixed[eid] = (idx, idx + len(word), word)
        search_from = idx + len(word)

    eiid2eid = {}
    for mt in _MKI_RE.finditer(raw):
        a = _attrs(mt.group(0))
        if "eiid" in a and "eventID" in a:
            eiid2eid[a["eiid"]] = a["eventID"]
    tlinks = []
    for mt in _TLINK_RE.finditer(raw):
        a = _attrs(mt.group(0))
        if "relatedToEventInstance" in a and "eventInstanceID" in a:
            tlinks.append((a["eventInstanceID"], a["relatedToEventInstance"], a.get("relType", "NONE")))

    sent_bounds = _sentence_bounds(text)
    return {"plain_text": text, "events": events_fixed, "sent_bounds": sent_bounds,
            "eiid2eid": eiid2eid, "tlinks": tlinks}


def _sentence_bounds(text: str) -> list[int]:
    """Return sorted char offsets that START each sentence (0 first)."""
    bounds = [0]
    for mt in re.finditer(r"[.!?]+[\s\"')\]]+", text):
        bounds.append(mt.end())
    if bounds[-1] != len(text):
        bounds.append(len(text))
    return sorted(set(bounds))


def _sent_idx(offset: int, bounds: list[int]) -> int:
    lo = 0
    for i in range(len(bounds) - 1):
        if bounds[i] <= offset < bounds[i + 1]:
            return i
    return max(0, len(bounds) - 2)


def mark_text(text: str, span1: tuple, span2: tuple, max_chars: int = 6000) -> str:
    """Insert [[E1]]..[[/E1]] / [[E2]]..[[/E2]] around the two event spans.

    If the doc is long, window to a contiguous slice containing both events.
    """
    (s1, e1, _), (s2, e2, _) = span1, span2
    spans = sorted([(s1, e1, "E1"), (s2, e2, "E2")])
    # build marked text by splicing from right to left so earlier offsets stay valid
    out = text
    for s, e, tag in sorted(spans, reverse=True):
        out = out[:s] + f"[[{tag}]]" + out[s:e] + f"[[/{tag}]]" + out[e:]
    if len(out) <= max_chars:
        return out.strip()
    # window around both events
    lo = max(0, min(s1, s2) - max_chars // 3)
    hi = min(len(out), max(e1, e2) + 200 + max_chars // 3)
    # recompute on marked text indices is messy; just window the ORIGINAL then re-mark
    lo0 = max(0, min(s1, s2) - max_chars // 3)
    hi0 = min(len(text), max(e1, e2) + max_chars // 3)
    sub = text[lo0:hi0]
    ns = [(s1 - lo0, e1 - lo0, "E1"), (s2 - lo0, e2 - lo0, "E2")]
    for s, e, tag in sorted(ns, reverse=True):
        sub = sub[:s] + f"[[{tag}]]" + sub[s:e] + f"[[/{tag}]]" + sub[e:]
    return ("... " + sub.strip() + " ...")


# ----------------------------------------------------------------------------------
# triangle harvesting
# ----------------------------------------------------------------------------------
def harvest_triangles(edges: list[dict], max_per_doc: int, rng: random.Random) -> list[dict]:
    """edges: list of {u,v,gold,sentdiff,deduction_required}. Build undirected gold graph;
    enumerate triples with all 3 pairwise gold edges. Query = max-sentdiff edge of the triple.
    Returns triangle dicts referencing the three edges by (u,v) keys.
    """
    by_pair = {}
    adj = defaultdict(set)
    for ed in edges:
        key = tuple(sorted((ed["u"], ed["v"])))
        by_pair[key] = ed
        adj[ed["u"]].add(ed["v"]); adj[ed["v"]].add(ed["u"])
    nodes = list(adj.keys())
    tris = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            a, b = nodes[i], nodes[j]
            if b not in adj[a]:
                continue
            for c in adj[a] & adj[b]:
                if c in (a, b):
                    continue
                trio = tuple(sorted((a, b, c)))
                tris.append(trio)
    tris = sorted(set(tris))
    rng.shuffle(tris)
    tris = tris[:max_per_doc]
    out = []
    for (a, b, c) in tris:
        e_ab = by_pair[tuple(sorted((a, b)))]
        e_bc = by_pair[tuple(sorted((b, c)))]
        e_ac = by_pair[tuple(sorted((a, c)))]
        trip = [e_ab, e_bc, e_ac]
        # query = edge with max sentdiff (most likely deduction-required); via = third node
        def sd(ed):
            return ed["sentdiff"] if ed["sentdiff"] is not None else -1
        query = max(trip, key=sd)
        others = [e for e in trip if e is not query]
        qnodes = {query["u"], query["v"]}
        via = ({a, b, c} - qnodes).pop()
        out.append({
            "query": (query["u"], query["v"]), "via": via,
            "edge_qx": tuple(sorted((min(qnodes), via))),
            "edge_xy": tuple(sorted((via, max(qnodes)))),
            "edges": [(e["u"], e["v"]) for e in trip],
            "query_gold": query["gold"], "query_sentdiff": query["sentdiff"],
            "query_deduction_required": bool(query.get("deduction_required")),
        })
    return out


# ----------------------------------------------------------------------------------
# corpus loaders -> standardized arm dict
# ----------------------------------------------------------------------------------
def _finalize_doc_edges(doc, info, rng, all_classes=True):
    """Attach sentdiff/deduction_required to edges from event spans + sentence bounds."""
    ev = info["events"]; bounds = info["sent_bounds"]
    out = []
    for ed in doc:
        u, v = ed["u"], ed["v"]
        if u not in ev or v not in ev:
            continue
        su = _sent_idx(ev[u][0], bounds); sv = _sent_idx(ev[v][0], bounds)
        sd = abs(su - sv)
        ed = dict(ed); ed["sentdiff"] = sd
        ed["deduction_required"] = ed.get("deduction_required", sd > 1) or sd > 1
        out.append(ed)
    return out


def load_tbdense(max_docs: int, max_edges: int, max_tri: int, seed: int) -> dict:
    rng = random.Random(seed)
    tml_dir = DATA / "TimeBank-dense" / "tml"
    files = sorted(tml_dir.glob("*.tml"))
    docs = {}
    for f in files:
        info = parse_tml(f)
        docid = f.stem
        ev = info["events"]; e2e = info["eiid2eid"]
        raw_edges = []
        seen = set()
        for (eiid1, eiid2, rt) in info["tlinks"]:
            rt = rt.upper()
            if rt not in TBDENSE_REL:
                continue
            e1 = e2e.get(eiid1); e2 = e2e.get(eiid2)
            if not e1 or not e2 or e1 == e2 or e1 not in ev or e2 not in ev:
                continue
            key = tuple(sorted((e1, e2)))
            if key in seen:
                continue
            seen.add(key)
            raw_edges.append({"u": e1, "v": e2, "gold": TBDENSE_REL[rt]})
        edges = _finalize_doc_edges(raw_edges, info, rng)
        if len(edges) < 2:
            continue
        docs[docid] = {"info": info, "edges": edges}
    return _assemble_arm("TBDense_dense", "ALLEN", docs, max_docs, max_edges,
                         max_tri, rng,
                         provenance="TimeBank-Dense (.tml TLINKs) -- NarrativeTime stand-in for pilot")


def load_tddman(max_docs: int, max_edges: int, max_tri: int, seed: int) -> dict:
    rng = random.Random(seed + 1)
    # gold pairs
    gold = defaultdict(list)
    for fn in ["TDDManTrain.tsv", "TDDManDev.tsv", "TDDManTest.tsv"]:
        p = DATA / "TDDiscourse" / fn
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            docid, e1, e2, rel = parts[:4]
            rel = rel.strip()
            if rel in TDDMAN_REL and e1 != e2:
                gold[docid].append({"u": e1, "v": e2, "gold": TDDMAN_REL[rel],
                                    "deduction_required": True})  # all >1 sentence by construction
    tml_dir = DATA / "TimeBank-dense" / "tml"
    tml_by_doc = {f.stem: f for f in tml_dir.glob("*.tml")}
    docs = {}
    for docid, raw in gold.items():
        f = tml_by_doc.get(docid)
        if f is None:
            continue
        info = parse_tml(f)
        edges = _finalize_doc_edges(raw, info, rng)
        if len(edges) < 2:
            continue
        docs[docid] = {"info": info, "edges": edges}
    return _assemble_arm("TDDMan_noncirc", "ALLEN", docs, max_docs, max_edges,
                         max_tri, rng,
                         provenance="TDDMan (manual >1-sentence pairs) + TimeBank-Dense .tml text join")


def load_matres(max_docs: int, max_edges: int, max_tri: int, seed: int) -> dict:
    """MATRES via qiangning EMNLP-19 XML (self-contained text+markers+gold+locality)."""
    rng = random.Random(seed + 2)
    docs = defaultdict(lambda: {"edges": [], "marked": {}})
    files = [DATA / "MATRES_qiangning" / "testset-temprel.xml",
             DATA / "MATRES_qiangning" / "trainset-temprel.xml"]
    for p in files:
        if not p.exists():
            continue
        for line in p.read_text(errors="ignore").splitlines():
            line = line.strip()
            if not line.startswith("<SENTENCE"):
                continue
            head = line.split(">", 1)[0]
            a = _attrs(head)
            inner = line[len(head) + 1:].rsplit("</SENTENCE>", 1)[0]
            try:
                src = int(a["SOURCE"][1:]); tgt = int(a["TARGET"][1:])
            except (KeyError, ValueError):
                continue
            lab = MATRES_REL.get(a.get("LABEL", "VAGUE"), "VAGUE")
            sd = int(a.get("SENTDIFF", -1))
            docid = a["DOCID"]
            # reconstruct text + mark E1/E2 tokens
            toks = inner.split()
            words = []
            for tk in toks:
                parts = tk.split("///")
                w = parts[0]; marker = parts[-1] if len(parts) >= 4 else ""
                if marker == "E1":
                    w = f"[[E1]]{w}[[/E1]]"
                elif marker == "E2":
                    w = f"[[E2]]{w}[[/E2]]"
                words.append(w)
            marked = " ".join(words)
            u = f"t{src}"; v = f"t{tgt}"
            ed = {"u": u, "v": v, "gold": lab, "sentdiff": sd,
                  "deduction_required": sd > 1}
            docs[docid]["edges"].append(ed)
            docs[docid]["marked"][tuple(sorted((u, v)))] = marked
    # dedup edges per doc (keep first)
    fixed = {}
    for docid, d in docs.items():
        seen = set(); eds = []
        for ed in d["edges"]:
            k = tuple(sorted((ed["u"], ed["v"])))
            if k in seen:
                continue
            seen.add(k); eds.append(ed)
        if len(eds) >= 2:
            fixed[docid] = {"edges": eds, "marked": d["marked"], "info": None}
    return _assemble_arm("MATRES_gate", "POINT", fixed, max_docs, max_edges,
                         max_tri, rng, premarked=True,
                         provenance="MATRES (qiangning EMNLP-19 XML, start-point convex point algebra)")


def _assemble_arm(name, algebra, docs, max_docs, max_edges, max_tri, rng,
                  premarked=False, provenance=""):
    """BUDGET-FIRST assembly: cap the number of distinct elicited EDGES per arm (this is
    what is billed), preferring triangle-forming edges so closure has material, then top up
    with stratified standalone edges for relation-class + sentence-distance coverage.
    Triangles are harvested ONLY among kept edges (so they cost no extra calls).
    """
    docids = list(docs.keys())
    rng.shuffle(docids)
    docids = docids[:max_docs]

    def make_task(docid, ed, d):
        key = tuple(sorted((ed["u"], ed["v"])))
        task = {"arm": name, "algebra": algebra, "docid": docid,
                "u": ed["u"], "v": ed["v"], "gold": ed["gold"],
                "sentdiff": ed["sentdiff"], "deduction_required": bool(ed["deduction_required"])}
        if premarked:
            task["marked_text"] = d["marked"].get(key, "")
        else:
            ev = d["info"]["events"]
            if ed["u"] not in ev or ed["v"] not in ev:
                return None
            task["marked_text"] = mark_text(d["info"]["plain_text"], ev[ed["u"]], ev[ed["v"]])
        if not task["marked_text"]:
            return None
        return task

    edge_tasks: dict = {}
    triangles: list = []
    # Pass 1: triangle-driven edges (round-robin across docs to spread coverage)
    doc_tris = {}
    for docid in docids:
        doc_tris[docid] = harvest_triangles(docs[docid]["edges"], 10_000, rng)
    n_tri = 0
    progress = True
    rounds = 0
    while progress and n_tri < max_tri and len(edge_tasks) < max_edges:
        progress = False
        rounds += 1
        for docid in docids:
            if n_tri >= max_tri or len(edge_tasks) >= max_edges:
                break
            tris = doc_tris.get(docid)
            if not tris:
                continue
            t = tris.pop()
            d = docs[docid]
            edmap = {tuple(sorted((e["u"], e["v"]))): e for e in d["edges"]}
            keys = [tuple(sorted((u, v))) for (u, v) in t["edges"]]
            # only add if we can afford the new edges
            new_keys = [k for k in keys if (docid,) + k not in edge_tasks]
            if len(edge_tasks) + len(new_keys) > max_edges:
                continue
            ok = True
            staged = {}
            for k in keys:
                tk = (docid,) + k
                if tk not in edge_tasks:
                    task = make_task(docid, edmap[k], d)
                    if task is None:
                        ok = False; break
                    staged[tk] = task
            if not ok:
                continue
            edge_tasks.update(staged)
            t2 = dict(t); t2["docid"] = docid; t2["arm"] = name; t2["algebra"] = algebra
            triangles.append(t2); n_tri += 1; progress = True

    # Pass 2: top up with stratified standalone edges (relation class x distance bin)
    pool = []
    for docid in docids:
        d = docs[docid]
        for ed in d["edges"]:
            tk = (docid,) + tuple(sorted((ed["u"], ed["v"])))
            if tk not in edge_tasks:
                pool.append((docid, ed))
    def dbin(sd):
        return "same" if sd == 0 else ("adj" if sd == 1 else "far")
    by_strat = defaultdict(list)
    for (docid, ed) in pool:
        by_strat[(ed["gold"], dbin(ed["sentdiff"]))].append((docid, ed))
    for v in by_strat.values():
        rng.shuffle(v)
    strata = list(by_strat.keys())
    rng.shuffle(strata)
    si = 0
    while len(edge_tasks) < max_edges and any(by_strat[s] for s in strata):
        s = strata[si % len(strata)]; si += 1
        if by_strat[s]:
            docid, ed = by_strat[s].pop()
            task = make_task(docid, ed, docs[docid])
            if task is not None:
                edge_tasks[(docid,) + tuple(sorted((ed["u"], ed["v"])))] = task

    return {"arm": name, "algebra": algebra, "provenance": provenance,
            "edge_tasks": edge_tasks, "triangles": triangles,
            "n_docs": len(docids), "n_edges": len(edge_tasks), "n_triangles": len(triangles)}


if __name__ == "__main__":
    import json
    for loader in (load_matres, load_tddman, load_tbdense):
        arm = loader(max_docs=12, max_edges=150, max_tri=120, seed=20260617)
        ded = sum(1 for t in arm["edge_tasks"].values() if t["deduction_required"])
        print(f"{arm['arm']:16s} algebra={arm['algebra']:5s} docs={arm['n_docs']:3d} "
              f"edges={arm['n_edges']:4d} tri={arm['n_triangles']:4d} ded_edges={ded}")
        # show one marked sample
        k = next(iter(arm["edge_tasks"]))
        t = arm["edge_tasks"][k]
        print("   sample gold=", t["gold"], "sd=", t["sentdiff"], "| text:", repr(t["marked_text"][:160]))
