#!/usr/bin/env python3
"""RCC-8 (and CDC) gold/read layer for the iter-5 decisive SPATIAL test.

Supplies:
  * dataset RCC-8 token canonicalisation (TPPI/NTPPI -> engine TPPi/NTPPi),
  * the HIGH-RECALL DISJUNCTIVE RCC-8 read prompt + a robust parser,
  * a PoT per-path composition prompt (real-LLM reasoner, no table),
  * orientation helpers (RCC-8 is non-symmetric: TPP != TPPi),
  * the analogous CDC read prompt/parser for the (secondary) cardinal arm.
"""
from __future__ import annotations

import json
import re

import engine

RCC8 = engine.build_rcc8_algebra()
RCC8_BASE = ["DC", "EC", "PO", "EQ", "TPP", "NTPP", "TPPi", "NTPPi"]
CDC = engine.build_cardinal_algebra()
CDC_BASE = ["W", "E", "S", "N", "SW", "SE", "NW", "NE", "EQ"]


# --------------------------------------------------------------------------- #
# RCC-8 canonicalisation + gloss
# --------------------------------------------------------------------------- #
def canon_rcc8_sym(sym: str):
    """Map a single token (any case, TPPI/NTPPI/disconnected/inside/...) -> engine sym."""
    if sym is None:
        return None
    t = str(sym).strip()
    tl = t.lower()
    if tl in _RCC8_WORD2SYM:
        return _RCC8_WORD2SYM[tl]
    return None


_RCC8_WORD2SYM = {w.lower(): w for w in RCC8_BASE}
_RCC8_WORD2SYM.update({
    "tppi": "TPPi", "ntppi": "NTPPi",   # lower-case 'i' canonical
    "disconnected": "DC", "disconnected from": "DC", "outside": "DC", "separate": "DC",
    "externally connected": "EC", "externally-connected": "EC", "touching": "EC",
    "outside and touching": "EC", "touch": "EC", "meets": "EC", "adjacent": "EC",
    "partially overlapping": "PO", "partial overlap": "PO", "overlap": "PO",
    "overlapping": "PO", "overlaps": "PO",
    "equal": "EQ", "equals": "EQ", "same": "EQ", "identical": "EQ", "coincident": "EQ",
    "tangential proper part": "TPP", "inside and touching": "TPP",
    "inside touching": "TPP", "covered by": "TPP", "enclosed and touching": "TPP",
    "non-tangential proper part": "NTPP", "inside": "NTPP", "strictly inside": "NTPP",
    "within": "NTPP", "contained in": "NTPP", "part of": "NTPP", "in": "NTPP",
    "tangential proper part inverse": "TPPi", "contains and touches": "TPPi",
    "contains touching": "TPPi", "covers": "TPPi", "encloses and touching": "TPPi",
    "non-tangential proper part inverse": "NTPPi", "contains": "NTPPi",
    "strictly contains": "NTPPi", "has": "NTPPi", "encloses": "NTPPi",
})
_UNDET = {"underdetermined", "undetermined", "vague", "unknown", "universal", "none",
          "any", "all", "indeterminate", "unclear", "ambiguous", "everything", "unconstrained"}

RCC8_DEFS = [
    ("DC", "disconnected: A and B are separate, with a gap (do not touch)"),
    ("EC", "externally connected: A and B touch only at a boundary, interiors disjoint"),
    ("PO", "partially overlap: A and B share some interior but neither is inside the other"),
    ("EQ", "equal: A and B occupy exactly the same region"),
    ("TPP", "tangential proper part: A is inside B and touches B's boundary"),
    ("NTPP", "non-tangential proper part: A is strictly inside B (no boundary contact)"),
    ("TPPi", "tangential proper part inverse: B is inside A and touches A's boundary (A contains&touches B)"),
    ("NTPPi", "non-tangential proper part inverse: B is strictly inside A (A strictly contains B)"),
]

# CDC parser map
_CDC_WORD2SYM = {w.lower(): w for w in CDC_BASE}
_CDC_WORD2SYM.update({
    "west": "W", "left": "W", "east": "E", "right": "E", "north": "N", "above": "N",
    "up": "N", "south": "S", "below": "S", "down": "S",
    "northeast": "NE", "north-east": "NE", "upper-right": "NE", "upper right": "NE",
    "northwest": "NW", "north-west": "NW", "upper-left": "NW", "upper left": "NW",
    "southeast": "SE", "south-east": "SE", "lower-right": "SE", "lower right": "SE",
    "southwest": "SW", "south-west": "SW", "lower-left": "SW", "lower left": "SW",
    "equal": "EQ", "same": "EQ", "same position": "EQ", "coincident": "EQ",
})


# --------------------------------------------------------------------------- #
# JSON / token helpers
# --------------------------------------------------------------------------- #
def _safe_json(txt: str):
    if not txt:
        return None
    txt = re.sub(r"^```(?:json)?|```$", "", txt, flags=re.M).strip()
    cands = [txt]
    s = txt.find("{")
    if s >= 0:
        depth = 0
        for i in range(s, len(txt)):
            if txt[i] == "{":
                depth += 1
            elif txt[i] == "}":
                depth -= 1
                if depth == 0:
                    cands.append(txt[s:i + 1])
                    break
    for c in cands:
        try:
            return json.loads(c)
        except Exception:
            continue
    return None


def _tok_to_sym(tok, wmap):
    if tok is None:
        return None
    t = str(tok).strip().lower()
    if t in _UNDET:
        return "UNDET"
    return (wmap.get(t) or wmap.get(t.replace("_", "-")) or wmap.get(t.replace("_", " "))
            or wmap.get(t.replace("-", " ")))


def _parse_generic(content: str, base, wmap):
    """Shared disjunctive-read parser for RCC-8 / CDC."""
    obj = _safe_json((content or "").strip())
    syms, underdet, most_likely, conf = set(), False, None, 0.5
    if isinstance(obj, dict):
        underdet = bool(obj.get("underdetermined", False))
        rels = obj.get("relations", obj.get("relation", []))
        if isinstance(rels, str):
            rels = [rels]
        if isinstance(rels, list):
            for r in rels:
                sym = _tok_to_sym(r if not isinstance(r, dict) else
                                  (r.get("relation") or r.get("rel") or r.get("label")), wmap)
                if sym == "UNDET":
                    underdet = True
                elif sym:
                    syms.add(sym)
        ml = obj.get("most_likely")
        if isinstance(ml, list) and ml:
            ml = ml[0]
        msym = _tok_to_sym(ml, wmap)
        if msym and msym != "UNDET":
            most_likely = msym
        c = obj.get("confidence")
        if isinstance(c, (int, float)):
            conf = float(max(0.0, min(1.0, c)))
    else:
        low = (content or "").lower()
        for w, sym in wmap.items():
            if len(w) >= 2 and re.search(r"\b" + re.escape(w) + r"\b", low):
                syms.add(sym)
        for w in _UNDET:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                underdet = True
        if not syms and not underdet:
            return {"rel_set": frozenset(), "underdet": False, "pfail": True,
                    "most_likely": None, "conf": 0.5}
    if most_likely is None and syms:
        most_likely = next(iter(syms))
    pfail = (not syms) and (not underdet) and (obj is None)
    return {"rel_set": frozenset(syms) if syms else frozenset(), "underdet": underdet,
            "pfail": pfail, "most_likely": most_likely, "conf": conf}


# --------------------------------------------------------------------------- #
# RCC-8 prompts + parse
# --------------------------------------------------------------------------- #
def build_rcc8_read_prompt(story_text, desc_A, desc_B):
    defs = "; ".join(f"'{tok}' = {gloss}" for tok, gloss in RCC8_DEFS)
    system = (
        "You are a careful spatial-relation reader. The RCC-8 region-connection relations "
        f"between two regions/objects A and B are: {defs}. "
        "Name EVERY RCC-8 relation the text does NOT rule out (a SOUND disjunction); recall "
        "matters far more than precision -- it is much better to include an extra relation "
        "than to omit the correct one. If the text does not constrain the A-B relation at "
        "all, set underdetermined=true. Judge ONLY from this text. "
        'Reply with ONLY a JSON object: {"relations": [<RCC-8 tokens not ruled out>], '
        '"underdetermined": <true|false>, "most_likely": "<single most probable token>", '
        '"confidence": <0..1>}.')
    user = (f"TEXT:\n{story_text}\n\nWhat is the RCC-8 spatial relation of "
            f"A=({desc_A}) to B=({desc_B})?")
    return system, user


def build_rcc8_pot_prompt(rel1_gloss, rel2_gloss):
    defs = "; ".join(f"'{tok}'={gloss.split(':')[0]}" for tok, gloss in RCC8_DEFS)
    system = (
        "You are given two spatial facts about three regions A, B, C using the 8 RCC-8 "
        f"region-connection relations ({defs}). Using ONLY these two facts and transitive "
        "spatial reasoning, infer the single most likely RCC-8 relation of A to C. If the "
        "two facts do not determine it, set underdetermined=true. "
        'Reply with ONLY JSON: {"most_likely": "<token>", "confidence": <0..1>, '
        '"underdetermined": <true|false>}.')
    user = f"Fact 1: A is '{rel1_gloss}' B\nFact 2: B is '{rel2_gloss}' C\n\nWhat is the RCC-8 relation of A to C?"
    return system, user


def build_rcc8_cot_prompt(story_text, desc_A, desc_B):
    """Chain-of-thought NEURAL BASELINE: reason step-by-step then commit a SINGLE RCC-8
    relation (no symbolic engine, no abstention) -- the 'raw LLM generation' contrast."""
    defs = "; ".join(f"'{tok}' = {gloss}" for tok, gloss in RCC8_DEFS)
    system = (
        "You are a spatial reasoner. The RCC-8 region-connection relations between two "
        f"objects A and B are: {defs}. Reason step by step about the spatial layout described "
        "in the text, then give the SINGLE most likely RCC-8 relation of A to B. "
        'Reply with ONLY JSON: {"reasoning": "<brief chain of thought>", '
        '"most_likely": "<one RCC-8 token>", "confidence": <0..1>}.')
    user = (f"TEXT:\n{story_text}\n\nReason step by step: what is the RCC-8 spatial relation "
            f"of A=({desc_A}) to B=({desc_B})?")
    return system, user


def parse_rcc8(content: str):
    pr = _parse_generic(content, RCC8_BASE, _RCC8_WORD2SYM)
    return {"rcc8_set": pr["rel_set"], "underdet": pr["underdet"], "pfail": pr["pfail"],
            "most_likely": pr["most_likely"], "conf": pr["conf"]}


def build_cdc_read_prompt(story_text, desc_A, desc_B):
    system = (
        "You are a careful spatial-relation reader. The cardinal-direction relation of A "
        "relative to B is one (or a disjunction) of: N(north/above), S(south/below), "
        "E(east/right), W(west/left), NE, NW, SE, SW, EQ(same position). "
        "Name EVERY direction the text does NOT rule out (a SOUND disjunction); recall "
        "matters more than precision. If the text does not constrain it, set "
        "underdetermined=true. Judge ONLY from this text. "
        'Reply with ONLY JSON: {"relations": [<direction tokens>], '
        '"underdetermined": <true|false>, "most_likely": "<token>", "confidence": <0..1>}.')
    user = (f"TEXT:\n{story_text}\n\nWhat is the cardinal-direction relation of "
            f"A=({desc_A}) to B=({desc_B})?")
    return system, user


def parse_cdc(content: str):
    pr = _parse_generic(content, CDC_BASE, _CDC_WORD2SYM)
    return {"cdc_set": pr["rel_set"], "underdet": pr["underdet"], "pfail": pr["pfail"],
            "most_likely": pr["most_likely"], "conf": pr["conf"]}


# --------------------------------------------------------------------------- #
# orientation + engine-set
# --------------------------------------------------------------------------- #
def orient_rcc8(engine_set, stored_uv, want_uv):
    """RCC-8 is NON-symmetric: converse if want direction is the reverse of stored."""
    if engine_set is None:
        return None
    if stored_uv == want_uv:
        return engine_set
    if (stored_uv[1], stored_uv[0]) == want_uv:
        return RCC8.converse(engine_set)
    return engine_set


def orient_cdc(engine_set, stored_uv, want_uv):
    if engine_set is None:
        return None
    if stored_uv == want_uv:
        return engine_set
    if (stored_uv[1], stored_uv[0]) == want_uv:
        return CDC.converse(engine_set)
    return engine_set


def read_to_engine_set_rcc8(pr):
    if pr["pfail"] or pr["underdet"] or not pr["rcc8_set"]:
        return RCC8.universe
    return pr["rcc8_set"]


def canon_rcc8_set(syms):
    """Canonicalise a list of dataset gold/edge tokens to an engine RCC-8 frozenset."""
    out = set()
    for s in syms:
        sym = canon_rcc8_sym(s)
        if sym in RCC8_BASE:
            out.add(sym)
    return frozenset(out)


def canon_cdc_set(syms):
    out = set()
    for s in syms:
        sym = _CDC_WORD2SYM.get(str(s).strip().lower())
        if sym in CDC_BASE:
            out.add(sym)
    return frozenset(out)
