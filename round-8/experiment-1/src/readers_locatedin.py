#!/usr/bin/env python3
"""LLM readers for the LOCATED-IN domain: atomic geographic/administrative-containment
extraction (the NEURAL READ) + the learned-composition baselines (raw forced-single,
self-consistency, Path-of-Thoughts). Drop-in twin of iter-7 readers.py with the kinship
surface vocabulary REPLACED by the containment vocabulary {located in, contains}.

The extraction call is the only place the neural model touches the document for OUR method:
it returns directly-stated located_in/contains triples, which the symbolic forward-closure
engine then composes. The raw / self-consistency / PoT readers are the purely-neural
multi-hop baselines, each given a matched single-relation abstention signal so the
matched-coverage showdown is fair.

normalize_surface returns a CANONICAL SURFACE STRING ('located in' | 'contains' |
'no-relation' | None); kin.surface_to_type('located in')=='located_in', etc.
"""
from __future__ import annotations

import json
import re

# Canonical containment surface vocabulary the model is restricted to.
CANON_SURFACES = ["located in", "contains"]

# phrase / colloquial synonyms -> canonical surface string
_SURF_SYN = {
    # located_in family
    "located in": "located in", "located": "located in", "is located in": "located in",
    "part of": "located in", "a part of": "located in", "is part of": "located in",
    "in": "located in", "within": "located in", "inside": "located in", "is in": "located in",
    "situated in": "located in", "lies in": "located in", "lie in": "located in",
    "subdivision of": "located in", "a subdivision of": "located in",
    "administrative subdivision of": "located in", "belongs to": "located in",
    "a city in": "located in", "a town in": "located in", "a village in": "located in",
    "a district of": "located in", "a region of": "located in", "a suburb of": "located in",
    "a neighborhood of": "located in", "a neighbourhood of": "located in",
    "capital of": "located in", "is the capital of": "located in", "the capital of": "located in",
    "located within": "located in", "located inside": "located in", "found in": "located in",
    # contains family
    "contains": "contains", "contain": "contains", "includes": "contains", "include": "contains",
    "encloses": "contains", "enclose": "contains", "comprises": "contains", "comprise": "contains",
    "encompasses": "contains", "encompass": "contains", "has within it": "contains",
    "is home to": "contains", "home to": "contains", "contains the": "contains",
    "has the": "contains", "covers": "contains", "spans": "contains",
}
_NO_REL = {"no-relation", "no relation", "norelation", "none", "unrelated", "not related",
           "no containment", "no relationship", "neither", "unknown", "n/a", "na", "no"}

# longest-first so multiword surfaces match before single tokens
_ALL_SURF_SORTED = sorted(set(CANON_SURFACES) | set(_SURF_SYN), key=len, reverse=True)


def normalize_surface(word: str):
    """Map any containment relation word/phrase to 'located in', 'contains', 'no-relation',
    or None (unrecognized)."""
    if word is None:
        return None
    w = str(word).strip().lower()
    w = w.replace("–", "-").replace("—", "-")
    w = re.sub(r"[.;,!?'\"]", "", w).strip()
    w = re.sub(r"\s+", " ", w)
    if not w:
        return None
    if w in _NO_REL:
        return "no-relation"
    if w in CANON_SURFACES:
        return w
    if w in _SURF_SYN:
        return _SURF_SYN[w]
    # phrase substring scan (longest synonym first)
    for s in _ALL_SURF_SORTED:
        if re.search(r"\b" + re.escape(s) + r"\b", w):
            return _SURF_SYN.get(s, s)
    # coarse keyword fallback
    if "contain" in w or "includ" in w or "compris" in w or "encompass" in w or "home to" in w:
        return "contains"
    if ("locat" in w or "within" in w or "inside" in w or "part of" in w or "subdivision" in w
            or "capital of" in w or "situated" in w):
        return "located in"
    if ("no" in w and "rel" in w) or w in ("not", "no path", "nopath"):
        return "no-relation"
    return None


# --------------------------------------------------------------------------- #
# JSON helpers (verbatim from iter-7 readers.py)
# --------------------------------------------------------------------------- #
def _strip_fences(txt: str) -> str:
    txt = txt.strip()
    txt = re.sub(r"^```(?:json)?", "", txt, flags=re.M)
    txt = re.sub(r"```$", "", txt, flags=re.M)
    return txt.strip()


def _load_json(txt: str):
    if not txt:
        return None
    txt = _strip_fences(txt)
    for cand in (txt, _first_json_block(txt, "{"), _first_json_block(txt, "[")):
        if cand is None:
            continue
        try:
            return json.loads(cand)
        except Exception:
            continue
    return None


def _first_json_block(txt: str, opener: str):
    closer = "}" if opener == "{" else "]"
    start = txt.find(opener)
    if start < 0:
        return None
    depth = 0
    for i in range(start, len(txt)):
        if txt[i] == opener:
            depth += 1
        elif txt[i] == closer:
            depth -= 1
            if depth == 0:
                return txt[start:i + 1]
    return None


# --------------------------------------------------------------------------- #
# (i) ATOMIC EXTRACTION
# --------------------------------------------------------------------------- #
_EXTRACT_SYSTEM = (
    "You extract DIRECTLY-STATED geographic / administrative containment relations between two "
    "named places from a short document. Output ONLY a JSON object "
    '{"relations": [{"a": <place>, "relation": "located in"|"contains", "b": <place>}, ...]}.\n'
    '"a located in b" means place a is inside / part of / an administrative subdivision of place b '
    '(e.g. {"a":"Pasay City","relation":"located in","b":"Metro Manila"}). '
    '"a contains b" means a geographically contains b (the converse).\n'
    "Extract ONLY containment relations the text states DIRECTLY between two named places. Do NOT "
    "infer transitive / composed containment (e.g. do not output a city-to-country link unless the "
    "text literally places the city in that country). Use exactly the place names as written."
)


def extraction_item(story: str, story_id: str) -> dict:
    user = f"Document:\n{story}\n\nReturn the JSON object of directly-stated containment relations between named places."
    return {"id": f"extract::{story_id}", "system": _EXTRACT_SYSTEM, "user": user,
            "max_tokens": 700, "temperature": 0.0}


_EXTRACT_BEST_SYSTEM = (
    _EXTRACT_SYSTEM + "\n\nExamples:\n"
    'Document: "Pasay City is in Metro Manila in the Philippines."  -> '
    '{"relations":[{"a":"Pasay City","relation":"located in","b":"Metro Manila"},'
    '{"a":"Metro Manila","relation":"located in","b":"Philippines"}]}\n'
    'Document: "Queensland, a state of Australia, contains the Gold Coast." -> '
    '{"relations":[{"a":"Queensland","relation":"located in","b":"Australia"},'
    '{"a":"Queensland","relation":"contains","b":"Gold Coast"}]}\n'
    "Extract EVERY directly-stated containment, including ones mentioned only in passing."
)


def extraction_item_best(story: str, story_id: str, inventory: list[str]) -> dict:
    """Best-effort extraction arm (PATH-2 hedge): few-shot + the document's place inventory."""
    inv = ", ".join(sorted({s for s in inventory if s}))
    user = (f"Document:\n{story}\n\nThe named places in this document are: {inv}.\n"
            "Return the JSON object of directly-stated containment relations between these places "
            "(use the names exactly as listed).")
    return {"id": f"extract_best::{story_id}", "system": _EXTRACT_BEST_SYSTEM, "user": user,
            "max_tokens": 800, "temperature": 0.0, "tag": "extract_best"}


def parse_extraction(content: str, kin) -> dict:
    """Parse an extraction response into typed directed atomic edges.
    Returns {edges:[{a,b,type,surface}], n_raw, parse_fail}."""
    obj = _load_json(content)
    rels = None
    if isinstance(obj, dict):
        rels = obj.get("relations", obj.get("relation"))
    elif isinstance(obj, list):
        rels = obj
    if rels is None:
        return {"edges": [], "n_raw": 0, "parse_fail": True}
    edges = []
    n_raw = 0
    for r in rels:
        if not isinstance(r, dict):
            continue
        a = r.get("a") or r.get("source") or r.get("h") or r.get("head")
        b = r.get("b") or r.get("target") or r.get("t") or r.get("tail")
        rel = r.get("relation") or r.get("rel") or r.get("r") or r.get("type") or r.get("label")
        if not a or not b or rel is None:
            continue
        n_raw += 1
        surf = normalize_surface(rel)
        if surf is None or surf == "no-relation":
            continue
        mapped = kin.surface_to_type(surf)
        if mapped is None:
            continue
        rtype, _gender = mapped
        edges.append({"a": str(a).strip(), "b": str(b).strip(), "type": rtype, "surface": surf})
    return {"edges": edges, "n_raw": n_raw, "parse_fail": False}


# --------------------------------------------------------------------------- #
# (ii) RAW forced-single  /  SELF-CONSISTENCY  /  PATH-OF-THOUGHTS baselines
# --------------------------------------------------------------------------- #
_RAW_SYSTEM = (
    "You answer a single geographic-containment question about a short document. Respond ONLY with "
    'a JSON object {"relation": "located in"|"contains"|"no-relation", "confidence": <0..1>}.\n'
    'The relation is what the FIRST place is to the SECOND: "located in" means the first place is '
    "inside / part of the second; \"contains\" means the first place contains the second; "
    '"no-relation" if neither place is inside the other. confidence is your probability the answer '
    "is correct (0..1)."
)


def raw_query_item(story: str, qsrc: str, qtgt: str, story_id: str, tag: str = "raw",
                   temperature: float = 0.0) -> dict:
    user = (f"Document:\n{story}\n\nQuestion: What is the geographic relationship of {qsrc} to {qtgt}? "
            f"(Is {qsrc} located in {qtgt}, does {qsrc} contain {qtgt}, or no-relation?) "
            f"Answer with the JSON object.")
    return {"id": f"{tag}::{story_id}::{qsrc}->{qtgt}", "system": _RAW_SYSTEM, "user": user,
            "max_tokens": 60, "temperature": temperature, "tag": tag}


def parse_raw(content: str) -> dict:
    """Return {surface, confidence, abstain}."""
    obj = _load_json(content)
    surf, conf = None, None
    if isinstance(obj, dict):
        surf = normalize_surface(obj.get("relation") or obj.get("answer") or obj.get("rel"))
        c = obj.get("confidence", obj.get("conf"))
        try:
            conf = float(c)
        except (TypeError, ValueError):
            conf = None
    if surf is None:
        surf = normalize_surface(content)
    if conf is None:
        m = re.search(r"(\d*\.\d+|\d+)", content or "")
        conf = float(m.group(1)) if m else 0.5
        if conf > 1.0:
            conf = min(1.0, conf / 100.0)
    conf = max(0.0, min(1.0, conf))
    abstain = (surf is None) or (surf == "no-relation")
    return {"surface": surf, "confidence": conf, "abstain": abstain}


def sc_items(story: str, qsrc: str, qtgt: str, story_id: str, k: int = 5,
             temperature: float = 0.7) -> list[dict]:
    """k self-consistency samples (tag-keyed so they cache separately)."""
    items = []
    for s in range(k):
        it = raw_query_item(story, qsrc, qtgt, story_id, tag=f"sc{s}", temperature=temperature)
        items.append(it)
    return items


def aggregate_sc(parsed_list: list[dict]) -> dict:
    """Modal vote across samples; conf = vote margin (top fraction). Abstain words count
    as a 'no-relation' vote so unanimous-abstain abstains."""
    votes = {}
    for p in parsed_list:
        key = p["surface"] if p["surface"] else "no-relation"
        votes[key] = votes.get(key, 0) + 1
    if not votes:
        return {"surface": None, "confidence": 0.0, "abstain": True}
    total = sum(votes.values())
    top_surf, top_n = max(votes.items(), key=lambda kv: kv[1])
    conf = top_n / total
    abstain = (top_surf == "no-relation") or (top_surf is None)
    return {"surface": (None if abstain else top_surf), "confidence": conf, "abstain": abstain}


_POT_SYSTEM = (
    "You compute a geographic-containment relation by composing a chain of places described in a "
    "document. You are given an ordered chain of places connecting two of them. Read each "
    "consecutive containment relationship FROM THE DOCUMENT and compose them step by step to get "
    "the final relation of the FIRST place to the LAST. Respond ONLY with a JSON object "
    '{"relation": "located in"|"contains"|"no-relation", "confidence": <0..1>}.'
)


def pot_item(story: str, path_names: list, story_id: str, path_idx: int) -> dict:
    chain = " -> ".join(path_names)
    qsrc, qtgt = path_names[0], path_names[-1]
    user = (f"Document:\n{story}\n\nChain of places: {chain}\n"
            f"Compose the consecutive containment relationships along this chain. "
            f"What is the geographic relationship of {qsrc} to {qtgt}? Answer with the JSON object.")
    return {"id": f"pot{path_idx}::{story_id}::{qsrc}->{qtgt}", "system": _POT_SYSTEM,
            "user": user, "max_tokens": 200, "temperature": 0.0, "tag": f"pot{path_idx}"}


def aggregate_pot(parsed_list: list[dict]) -> dict:
    """Modal vote across independent path compositions; conf = path-agreement fraction;
    abstain when no majority (paths disagree) or all abstain."""
    if not parsed_list:
        return {"surface": None, "confidence": 0.0, "abstain": True}
    votes = {}
    for p in parsed_list:
        key = p["surface"] if p["surface"] else "no-relation"
        votes[key] = votes.get(key, 0) + 1
    total = sum(votes.values())
    top_surf, top_n = max(votes.items(), key=lambda kv: kv[1])
    conf = top_n / total
    abstain = (top_surf == "no-relation") or (top_surf is None)
    return {"surface": (None if abstain else top_surf), "confidence": conf, "abstain": abstain}
