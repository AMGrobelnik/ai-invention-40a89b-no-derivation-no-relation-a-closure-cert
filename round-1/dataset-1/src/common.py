#!/usr/bin/env python3
"""Shared infrastructure for building gold temporal relation graphs.

Provides:
  - A robust TimeML (.tml) parser (stripped text + inline EVENT/TIMEX3 char spans + DCT + MAKEINSTANCE).
  - One frozen, deterministic sentence segmentation (NLTK Punkt) applied identically across corpora.
  - Canonical relation-algebra constants (Allen 13-relation, point algebra) and locality helpers.
  - Doc-id normalization.

These utilities are reused by the NarrativeTime, TDDMan, and MATRES builders so that node
offsets and locality flags are computed consistently.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from lxml import etree
from nltk.tokenize import PunktSentenceTokenizer

# --------------------------------------------------------------------------------------
# Canonical relation algebras
# --------------------------------------------------------------------------------------

# Allen's 13 interval base relations (canonical short names).
ALLEN_RELATIONS = ["b", "bi", "m", "mi", "o", "oi", "s", "si", "d", "di", "f", "fi", "eq"]
ALLEN_FULL = list(ALLEN_RELATIONS)  # full disjunction == no constraint (VAGUE)

# Point algebra base relations.
POINT_RELATIONS = ["<", "=", ">"]
POINT_FULL = list(POINT_RELATIONS)

# A point-algebra relation set is *convex* unless it is exactly the non-convex {<,>} (!=).
NON_CONVEX_POINT = {"<", ">"}


def widen_if_nonconvex(point_set: list[str]) -> tuple[list[str], bool]:
    """Convex-closure of a point-algebra set.

    The only non-convex base-relation set over points is {<,>} (genuine !=). For the
    point-algebra (path-consistency-complete) arm we widen it to {<,=,>}. Returns
    (possibly_widened_set, was_widened).
    """
    s = set(point_set)
    if s == NON_CONVEX_POINT:
        return ["<", "=", ">"], True
    # keep canonical ordering
    return [r for r in POINT_RELATIONS if r in s], False


# --------------------------------------------------------------------------------------
# Locality
# --------------------------------------------------------------------------------------

def locality_class(sentence_distance: Optional[int]) -> str:
    """Structural locality class from the sentence distance between two nodes."""
    if sentence_distance is None:
        return "undefined"
    if sentence_distance == 0:
        return "intra"
    if sentence_distance == 1:
        return "adjacent"
    return "long_distance"


def locality_fields(src_sent: Optional[int], tgt_sent: Optional[int]) -> dict:
    """Per-edge structural metadata derived purely from sentence indices.

    structural_deduction_required_proxy: True iff the two endpoints are >=2 sentences
      apart (a *structural* proxy for "the edge cannot be read off a single local window").
    locally_justifiable_proxy: True iff same or adjacent sentence.
    """
    if src_sent is None or tgt_sent is None:
        dist = None
    else:
        dist = abs(int(src_sent) - int(tgt_sent))
    cls = locality_class(dist)
    return {
        "src_sentence_index": src_sent,
        "tgt_sentence_index": tgt_sent,
        "sentence_distance": dist,
        "locality_class": cls,
        "structural_deduction_required_proxy": (dist is not None and dist >= 2),
        "locally_justifiable_proxy": (dist is not None and dist <= 1),
    }


# --------------------------------------------------------------------------------------
# Doc-id normalization
# --------------------------------------------------------------------------------------

def normalize_docid(docid: str) -> str:
    """Normalize a document id for cross-corpus matching (case/extension-insensitive)."""
    d = docid.strip()
    for ext in (".tml", ".tml.xml", ".xml"):
        if d.lower().endswith(ext):
            d = d[: -len(ext)]
            break
    return d.lower()


# --------------------------------------------------------------------------------------
# Frozen sentence segmentation
# --------------------------------------------------------------------------------------

class SentenceSegmenter:
    """One deterministic sentence segmentation, frozen for the whole build.

    Uses NLTK's pre-trained PunktSentenceTokenizer (English). The exact NLTK version is
    recorded in the data card. The same instance is used for every corpus whose document
    text is segmented here (NarrativeTime, TDDMan, and the optional TimeBank-Dense corpus);
    MATRES instead uses the canonical per-token sentence ids shipped with the qiangning
    preprocessing (recorded as method='qiangning_sentid').
    """

    METHOD = "nltk_punkt_pretrained_english"

    def __init__(self) -> None:
        self._tok = PunktSentenceTokenizer()

    def spans(self, text: str) -> list[tuple[int, int]]:
        """Return list of (char_start, char_end) sentence spans covering `text`."""
        return list(self._tok.span_tokenize(text))

    def assign(self, text: str) -> tuple[list[tuple[int, int]], "OffsetSentenceMap"]:
        spans = self.spans(text)
        return spans, OffsetSentenceMap(spans, len(text))


@dataclass
class OffsetSentenceMap:
    """Maps a character offset to a 0-based sentence index given frozen sentence spans."""

    spans: list[tuple[int, int]]
    text_len: int

    def index_for(self, char_offset: Optional[int]) -> Optional[int]:
        if char_offset is None:
            return None
        # exact containment
        for i, (a, b) in enumerate(self.spans):
            if a <= char_offset < b:
                return i
        # offset in inter-sentence whitespace or at boundary: nearest preceding sentence
        best = None
        for i, (a, b) in enumerate(self.spans):
            if a <= char_offset:
                best = i
            else:
                break
        if best is not None:
            return best
        return 0 if self.spans else None


# --------------------------------------------------------------------------------------
# TimeML (.tml) parsing
# --------------------------------------------------------------------------------------

@dataclass
class TmlNode:
    tag: str                 # EVENT | TIMEX3 | SIGNAL
    attrib: dict
    surface: str
    char_start: int
    char_end: int


@dataclass
class TmlDoc:
    docid: str
    text: str                       # stripped TEXT (inline tags removed)
    events: list[TmlNode] = field(default_factory=list)     # EVENT tags inside <TEXT>
    timexes: list[TmlNode] = field(default_factory=list)    # TIMEX3 tags inside <TEXT>
    signals: list[TmlNode] = field(default_factory=list)
    dct: Optional[dict] = None      # {tid, value, type, surface}
    makeinstance: dict = field(default_factory=dict)         # eiid -> attribs (incl eventID)
    tlinks: list[dict] = field(default_factory=list)         # raw TLINK attribs (cross-check only)


_PARSER = etree.XMLParser(recover=True, resolve_entities=False, huge_tree=True)


def _local(tag) -> str:
    if not isinstance(tag, str):
        return ""
    return tag.split("}", 1)[-1]  # strip namespace if present


def parse_tml(path: Path) -> TmlDoc:
    """Parse a TimeML .tml file.

    Walks the <TEXT> element child-by-child, accumulating the stripped text and recording
    the exact character span of every inline EVENT / TIMEX3 / SIGNAL tag. Also extracts the
    DCT timex, the MAKEINSTANCE table (eiid -> eventID/attribs), and raw TLINKs.
    Robust to the mildly-malformed XML common in TimeML releases (recover=True).
    """
    raw = path.read_bytes()
    root = etree.fromstring(raw, parser=_PARSER)
    if root is None:
        raise ValueError(f"Could not parse {path}")

    docid_el = root.find(".//DOCID")
    docid = (docid_el.text.strip() if docid_el is not None and docid_el.text else path.stem)

    doc = TmlDoc(docid=docid, text="")

    # DCT
    dct_el = root.find(".//DCT")
    if dct_el is not None:
        t = dct_el.find(".//TIMEX3")
        if t is not None:
            doc.dct = {
                "tid": t.get("tid"),
                "value": t.get("value"),
                "type": t.get("type"),
                "functionInDocument": t.get("functionInDocument"),
                "surface": (t.text or "").strip(),
            }

    # TEXT (walk children to recover offsets)
    text_el = None
    for el in root.iter():
        if _local(el.tag) == "TEXT":
            text_el = el
            break
    chunks: list[str] = []
    pos = 0
    if text_el is not None:
        if text_el.text:
            chunks.append(text_el.text)
            pos += len(text_el.text)
        for child in text_el:
            tag = _local(child.tag)
            surface = child.text or ""
            start = pos
            chunks.append(surface)
            pos += len(surface)
            end = pos
            node = TmlNode(tag=tag, attrib=dict(child.attrib), surface=surface,
                           char_start=start, char_end=end)
            if tag == "EVENT":
                doc.events.append(node)
            elif tag == "TIMEX3":
                doc.timexes.append(node)
            elif tag == "SIGNAL":
                doc.signals.append(node)
            if child.tail:
                chunks.append(child.tail)
                pos += len(child.tail)
    doc.text = "".join(chunks)

    # MAKEINSTANCE
    for mi in root.iter():
        if _local(mi.tag) == "MAKEINSTANCE":
            eiid = mi.get("eiid")
            if eiid:
                doc.makeinstance[eiid] = dict(mi.attrib)

    # TLINKs (cross-check only)
    for tl in root.iter():
        if _local(tl.tag) == "TLINK":
            doc.tlinks.append(dict(tl.attrib))

    return doc


def eid_to_event_node(doc: TmlDoc) -> dict[str, TmlNode]:
    """Map EVENT eid -> TmlNode (first occurrence)."""
    out: dict[str, TmlNode] = {}
    for ev in doc.events:
        eid = ev.attrib.get("eid")
        if eid and eid not in out:
            out[eid] = ev
    return out
