#!/usr/bin/env python3
"""Allen-13 gold/read layer for the iter-4 cross-path-intersection experiment.

The iter-3 headline ran in the COARSE convex POINT start-point algebra (5 labels), which
is exactly why full==naive on dense transitively-closed gold: the start-point projection
collapses {before,meets} -> {<}, so a single best path already resolves and there is no
intersection bite. iter-4 uses the FULL Allen interval algebra (13 base relations).

This module supplies:
  * the dataset(lowercase GQR) -> engine(uppercase) token map and gold extractors
    (canonical = tightest/atomic; sound = coarse_superset when present else canonical),
  * directed gold lookup with converse,
  * the NEW disjunctive Allen READ prompt + a robust parser,
  * orientation helpers.
"""
from __future__ import annotations

import json
import re

import engine

AL = engine.build_allen_algebra()

# dataset lowercase GQR token -> engine uppercase symbol
ALLEN_TOK = {'b': 'B', 'bi': 'BI', 'd': 'D', 'di': 'DI', 'o': 'O', 'oi': 'OI',
             'm': 'M', 'mi': 'MI', 's': 'S', 'si': 'SI', 'f': 'F', 'fi': 'FI',
             'eq': 'E', 'e': 'E'}

# human-readable glosses (token order is deliberate: 6 relations + 6 converses + equal)
ALLEN_DEFS = [
    ("b", "before: E1 ends before E2 starts (a gap between them)"),
    ("m", "meets: E1 ends exactly when E2 starts (no gap, no overlap)"),
    ("o", "overlaps: E1 starts first, they overlap, E1 ends first"),
    ("s", "starts: E1 and E2 start together, E1 ends first (E1 inside E2 at the start)"),
    ("d", "during: E1 is strictly inside E2 (E2 starts before and ends after E1)"),
    ("f", "finishes: E1 and E2 end together, E1 starts later (E1 inside E2 at the end)"),
    ("eq", "equal: E1 and E2 occupy exactly the same interval"),
    ("bi", "after: E1 starts after E2 ends (a gap; converse of before)"),
    ("mi", "met-by: E1 starts exactly when E2 ends (converse of meets)"),
    ("oi", "overlapped-by: E2 starts first, they overlap, E2 ends first (converse of overlaps)"),
    ("si", "started-by: E1 and E2 start together, E1 ends later (E1 contains E2 at the start)"),
    ("di", "contains: E2 is strictly inside E1 (converse of during)"),
    ("fi", "finished-by: E1 and E2 end together, E1 starts earlier (E1 contains E2 at the end)"),
]

# parser synonyms -> engine symbol (multi-char keys matched as whole tokens)
_WORD_TO_SYM = {
    "before": "B", "precedes": "B", "prior": "B", "earlier": "B", "b": "B",
    "after": "BI", "follows": "BI", "later": "BI", "succeeds": "BI", "a": "BI", "bi": "BI",
    "meets": "M", "meet": "M", "m": "M",
    "met-by": "MI", "met by": "MI", "metby": "MI", "mi": "MI",
    "overlaps": "O", "overlap": "O", "o": "O",
    "overlapped-by": "OI", "overlapped by": "OI", "overlappedby": "OI", "oi": "OI",
    "during": "D", "within": "D", "inside": "D", "d": "D",
    "contains": "DI", "includes": "DI", "include": "DI", "containing": "DI", "di": "DI",
    "starts": "S", "start": "S", "s": "S",
    "started-by": "SI", "started by": "SI", "startedby": "SI", "si": "SI",
    "finishes": "F", "finish": "F", "f": "F",
    "finished-by": "FI", "finished by": "FI", "finishedby": "FI", "fi": "FI",
    "equal": "E", "equals": "E", "eq": "E", "e": "E", "simultaneous": "E", "same": "E",
    "identical": "E", "coincides": "E", "concurrent": "E",
}
_UNDET = {"underdetermined", "undetermined", "vague", "unknown", "universal", "none",
          "any", "all", "indeterminate", "unclear", "ambiguous", "everything"}


# --------------------------------------------------------------------------- #
# gold extractors
# --------------------------------------------------------------------------- #
def _map_tokens(toks):
    if not toks:
        return None
    out = [ALLEN_TOK[t.lower()] for t in toks if t.lower() in ALLEN_TOK]
    if len(out) != len(toks):
        return "BADTOK"
    return frozenset(out)


def canon_allen(edge):
    """Tightest / atomic gold set (TDDMan -> singleton truth; NT -> start-point set)."""
    return _map_tokens(edge.get("canonical_relation_set"))


def sound_allen(edge):
    """SOUND gold set used for path composition (coarse_superset when present else canon).

    Mirrors the BROAD high-recall disjunctive sets the LLM reads emit, so gold-only
    feasibility does not over-predict bite (TDDMan tight singletons would be unsoundly
    tight; coarse_superset {b,m},{bi,mi},{di,si,fi},{d,s,f} is the sound version)."""
    css = edge.get("coarse_superset_set")
    if css:
        m = _map_tokens(css)
        if m not in (None, "BADTOK"):
            return m
    return canon_allen(edge)


def gold_dir(by_pair, a, b, fn=canon_allen):
    """Oriented gold set for direction a->b (converse if the stored edge is b->a)."""
    e = by_pair.get(tuple(sorted((a, b))))
    if e is None:
        return None
    g = fn(e)
    if g in (None, "BADTOK"):
        return g
    return g if (e["u"], e["v"]) == (a, b) else AL.converse(g)


def orient_allen(aset, stored_uv, want_uv):
    """Converse aset from stored orientation to the wanted (a,b) direction."""
    if aset is None:
        return None
    if stored_uv == want_uv:
        return aset
    if (stored_uv[1], stored_uv[0]) == want_uv:
        return AL.converse(aset)
    return aset


# --------------------------------------------------------------------------- #
# disjunctive Allen READ prompt + parser
# --------------------------------------------------------------------------- #
def build_allen_read_prompt(marked_text: str, variant: str = ""):
    defs = "; ".join(f"'{tok}' = {gloss}" for tok, gloss in ALLEN_DEFS)
    system = (
        "You read the temporal relation between two events E1 (marked [[E1]]...[[/E1]]) and "
        "E2 (marked [[E2]]...[[/E2]]) in a news-text excerpt. Use the 13 Allen interval "
        f"relations (relation of E1's time interval to E2's): {defs}. "
        "Name EVERY base relation the excerpt does NOT rule out -- recall matters far more "
        "than precision: it is much better to include an extra relation than to omit the "
        "correct one. If the excerpt does not constrain the order at all, set "
        "underdetermined=true. Judge ONLY from this excerpt; do NOT assume consistency with "
        "any other event pair. "
        'Reply with ONLY a JSON object: {"relations": [<lowercase tokens not ruled out>], '
        '"underdetermined": <true|false>, "most_likely": "<the single most probable token>", '
        '"confidence": <0..1 probability your most_likely token is correct>}.'
        + (f" {variant}" if variant else "")
    )
    user = f"{marked_text}\n\nWhat is the Allen temporal relation of E1 to E2?"
    return system, user


def build_allen_pot_prompt(fact1: str, fact2: str):
    defs = "; ".join(f"'{tok}'={gloss.split(':')[0]}" for tok, gloss in ALLEN_DEFS)
    system = (
        "You are given two temporal facts about three events A, B, C using the 13 Allen "
        f"interval relations ({defs}). Using ONLY these two facts and transitive temporal "
        "reasoning, infer the single most likely Allen relation of A to C. If the two facts "
        "do not determine it, set underdetermined=true. "
        'Reply with ONLY JSON: {"most_likely": "<token>", "confidence": <0..1>, '
        '"underdetermined": <true|false>}.'
    )
    user = f"Fact 1: A is '{fact1}' B\nFact 2: B is '{fact2}' C\n\nWhat is the Allen relation of A to C?"
    return system, user


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


def _tok_to_sym(tok):
    if tok is None:
        return None
    t = str(tok).strip().lower()
    if t in _UNDET:
        return "UNDET"
    return _WORD_TO_SYM.get(t) or _WORD_TO_SYM.get(t.replace("_", "-")) \
        or _WORD_TO_SYM.get(t.replace("-", " "))


def parse_allen(content: str):
    """Return {allen_set:frozenset(engine syms), underdet:bool, pfail:bool,
    most_likely:sym|None, conf:float}. Parse failure (empty/no tokens) -> pfail=True
    (MISSING DATA: excluded from recall, NOT silently mapped to universe)."""
    obj = _safe_json((content or "").strip())
    syms = set()
    underdet = False
    most_likely = None
    conf = 0.5
    if isinstance(obj, dict):
        underdet = bool(obj.get("underdetermined", False))
        rels = obj.get("relations", obj.get("relation", []))
        if isinstance(rels, str):
            rels = [rels]
        if isinstance(rels, list):
            for r in rels:
                sym = _tok_to_sym(r if not isinstance(r, dict) else
                                  (r.get("relation") or r.get("rel") or r.get("label")))
                if sym == "UNDET":
                    underdet = True
                elif sym:
                    syms.add(sym)
        ml = obj.get("most_likely")
        if isinstance(ml, list) and ml:
            ml = ml[0]
        msym = _tok_to_sym(ml)
        if msym and msym != "UNDET":
            most_likely = msym
        c = obj.get("confidence")
        if isinstance(c, (int, float)):
            conf = float(max(0.0, min(1.0, c)))
    else:
        # regex fallback over free text
        low = (content or "").lower()
        for w, sym in _WORD_TO_SYM.items():
            if len(w) >= 2 and re.search(r"\b" + re.escape(w) + r"\b", low):
                syms.add(sym)
        for w in _UNDET:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                underdet = True
        if not syms and not underdet:
            return {"allen_set": frozenset(), "underdet": False, "pfail": True,
                    "most_likely": None, "conf": 0.5}
    if most_likely is None and syms:
        most_likely = next(iter(syms))
    pfail = (not syms) and (not underdet) and (obj is None)
    aset = frozenset(syms) if syms else frozenset()
    return {"allen_set": aset, "underdet": underdet, "pfail": pfail,
            "most_likely": most_likely, "conf": conf}


def read_to_engine_set(pr):
    """emitted parse -> engine relation set for closure (underdet/empty/pfail -> universe)."""
    if pr["pfail"] or pr["underdet"] or not pr["allen_set"]:
        return AL.universe
    return pr["allen_set"]
