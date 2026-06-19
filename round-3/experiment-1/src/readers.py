#!/usr/bin/env python3
"""LLM readers: atomic-fact extraction (the NEURAL READ) + the learned-composition
baselines (raw forced-single, self-consistency, Path-of-Thoughts).

The extraction call is the only place the neural model touches the document for OUR
method: it returns directly-stated kinship triples, which the symbolic forward-closure
engine then composes. The raw / self-consistency / PoT readers are the purely-neural
multi-hop baselines, each given a matched single-relation abstention signal so the
matched-coverage showdown is fair.
"""
from __future__ import annotations

import json
import re

# Canonical surface vocabulary (22 gendered kinship words) the model is restricted to.
CANON_SURFACES = [
    "son", "daughter", "father", "mother", "husband", "wife", "brother", "sister",
    "grandson", "granddaughter", "grandfather", "grandmother",
    "son-in-law", "daughter-in-law", "father-in-law", "mother-in-law",
    "brother-in-law", "sister-in-law", "nephew", "niece", "uncle", "aunt",
]

# colloquial synonyms -> canonical surface word
_SURF_SYN = {
    "mom": "mother", "mum": "mother", "mommy": "mother", "mama": "mother", "ma": "mother",
    "dad": "father", "daddy": "father", "papa": "father", "pa": "father", "pop": "father",
    "grandpa": "grandfather", "granddad": "grandfather", "grandad": "grandfather",
    "gramps": "grandfather", "grandpapa": "grandfather",
    "grandma": "grandmother", "granny": "grandmother", "nana": "grandmother", "grandmom": "grandmother",
    "sis": "sister", "bro": "brother", "sibling": "sibling",
    "stepfather": "father", "stepmother": "mother", "stepson": "son", "stepdaughter": "daughter",
    "stepbrother": "brother", "stepsister": "sister",
    "grandchild": "grandson", "grandkid": "grandson",
}
_NO_REL = {"no-relation", "no relation", "norelation", "none", "unrelated", "not related",
           "no kinship", "no relationship", "stranger", "unknown", "n/a", "na"}

# longest-first so multiword surfaces ("father-in-law") match before "father"
_ALL_SURF_SORTED = sorted(set(CANON_SURFACES) | set(_SURF_SYN), key=len, reverse=True)


def normalize_surface(word: str):
    """Map any relation word/phrase to a canonical surface, 'no-relation', or None."""
    if word is None:
        return None
    w = str(word).strip().lower()
    w = w.replace("–", "-").replace("—", "-")
    w = re.sub(r"\s*-\s*", "-", w)         # 'father - in - law' -> 'father-in-law'
    w = re.sub(r"\s+in\s+law", "-in-law", w)
    w = re.sub(r"[.;,!?'\"]", "", w).strip()
    if w in _NO_REL:
        return "no-relation"
    if w in CANON_SURFACES:
        return w
    if w in _SURF_SYN:
        return _SURF_SYN[w]
    # substring scan (longest surface first)
    for s in _ALL_SURF_SORTED:
        if re.search(r"\b" + re.escape(s) + r"\b", w):
            return _SURF_SYN.get(s, s)
    if "no" in w and "rel" in w:
        return "no-relation"
    return None


# --------------------------------------------------------------------------- #
# JSON helpers
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
    "You extract family relationships from a short story. Output ONLY a JSON object "
    '{"relations": [{"a": <name>, "relation": <word>, "b": <name>}, ...]}.\n'
    'Each triple means "b is a\'s relation" (e.g. {"a":"Mary","relation":"father","b":"Tom"} '
    'means Tom is Mary\'s father).\n'
    "Use ONLY these relation words: son, daughter, father, mother, husband, wife, brother, "
    "sister, grandson, granddaughter, grandfather, grandmother, son-in-law, daughter-in-law, "
    "father-in-law, mother-in-law, brother-in-law, sister-in-law, nephew, niece, uncle, aunt.\n"
    "Extract ONLY relationships the text states DIRECTLY between two named people. Do NOT infer "
    "indirect or composed relationships (e.g. do not output a grandparent link unless the text "
    "literally says 'grandfather'/'grandmother'). If a relationship word is ambiguous, pick the "
    "single most direct stated word. Use exactly the names as written."
)


def extraction_item(story: str, story_id: str) -> dict:
    user = f"Story:\n{story}\n\nReturn the JSON object of directly-stated family relationships."
    return {"id": f"extract::{story_id}", "system": _EXTRACT_SYSTEM, "user": user,
            "max_tokens": 700, "temperature": 0.0}


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
    "You answer a single kinship question about a short story. Respond ONLY with a JSON "
    'object {"relation": <word>, "confidence": <0..1>}.\n'
    'The relation is what the SECOND person is to the FIRST: {"relation":"grandfather"} for '
    '"What is Tom to Mary?" means Tom is Mary\'s grandfather.\n'
    "Use ONE of: son, daughter, father, mother, husband, wife, brother, sister, grandson, "
    "granddaughter, grandfather, grandmother, son-in-law, daughter-in-law, father-in-law, "
    "mother-in-law, brother-in-law, sister-in-law, nephew, niece, uncle, aunt, or 'no-relation' "
    "if the two people have no family relationship. confidence is your probability the answer is "
    "correct (0..1)."
)


def raw_query_item(story: str, qsrc: str, qtgt: str, story_id: str, tag: str = "raw",
                   temperature: float = 0.0) -> dict:
    user = (f"Story:\n{story}\n\nQuestion: What is {qtgt} to {qsrc}? "
            f"(i.e. {qtgt} is {qsrc}'s ___) Answer with the JSON object.")
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
    "You compute a kinship relation by composing a chain of family links described in a story. "
    "You are given an ordered chain of people connecting two of them. Read each consecutive "
    "relationship FROM THE STORY and compose them step by step to get the final relation of the "
    "last person to the first. Respond ONLY with a JSON object "
    '{"relation": <word>, "confidence": <0..1>}. Use one of: son, daughter, father, mother, '
    "husband, wife, brother, sister, grandson, granddaughter, grandfather, grandmother, "
    "son-in-law, daughter-in-law, father-in-law, mother-in-law, brother-in-law, sister-in-law, "
    "nephew, niece, uncle, aunt, or 'no-relation'."
)


def pot_item(story: str, path_names: list, story_id: str, path_idx: int) -> dict:
    chain = " -> ".join(path_names)
    qsrc, qtgt = path_names[0], path_names[-1]
    user = (f"Story:\n{story}\n\nChain of people: {chain}\n"
            f"Compose the consecutive relationships along this chain. "
            f"What is {qtgt} to {qsrc}? Answer with the JSON object.")
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
