#!/usr/bin/env python3
"""Relation -> canonical-algebra mapping for the spatial multi-path corpus.

Splits native spatial relations into two calculi (per the iter-4 plan / dossier
art_aQ2Rf8rwqteI):
  * rcc8                : mereotopological  {DC,EC,PO,EQ,TPP,NTPP,TPPI,NTPPI}
                          -- engine-validated, usable for closure in iter-5.
  * cardinal_direction  : directional / distance  -- the engine does NOT yet
                          implement CDC; the vocabulary is recorded here so the
                          next-iter engine extension knows what to build.

Distance (near/far) and 3D depth (front/behind) are tagged as out-of-standard-2D-CDC
so the card can report them honestly.
"""
from __future__ import annotations

# RCC-8 base symbols (canonical upper-case), keyed by every native spelling we see.
RCC8_SYMBOLS = {"DC", "EC", "PO", "EQ", "TPP", "NTPP", "TPPI", "NTPPI"}

# SpaRP symbolic_context uses lower-case RCC-8 tokens verbatim.
_RCC8_TOKEN = {
    "dc": "DC", "ec": "EC", "po": "PO", "eq": "EQ",
    "tpp": "TPP", "ntpp": "NTPP", "tppi": "TPPI", "ntppi": "NTPPI",
}

# Verbalised topological phrases (SpaRP `targets`, SpartQA `spatial_indicator`,
# SpartQA `rel_with_block`) -> RCC-8.  Verified against SpaRP `target_choices`.
_RCC8_VERBAL = {
    "outside": "DC", "disconnected": "DC", "disconnected from": "DC",
    "outside and touching": "EC", "touching": "EC", "touching the bottom edge of": "TPP",
    "partially overlapping": "PO", "overlapping": "EQ", "equal": "EQ",
    "inside and touching": "TPP", "inside": "NTPP", "in": "NTPP",
    "contains and touches": "TPPI", "contains": "NTPPI", "has": "NTPPI",
    "cover": "TPPI", "covers": "TPPI", "covered by": "TPP",
    # SpartQA "touching the <edge> edge of <block>" => object inside & touching = TPP
    "touching the bottom edge of": "TPP", "touching the top edge of": "TPP",
    "touching the left edge of": "TPP", "touching the right edge of": "TPP",
    "touching the bottom of": "TPP", "touching the top of": "TPP",
}

# Directional / distance words -> cardinal-direction-calculus tile names (or
# distance / depth tags).  Covers SpaRP (left/right/above/below/front/behind/near/far),
# StepGame (8 cardinals + diagonals + clock paraphrases handled upstream) and SpartQA.
_DIR = {
    "left": "W", "right": "E", "above": "N", "below": "S",
    "north": "N", "south": "S", "east": "E", "west": "W",
    "northeast": "NE", "northwest": "NW", "southeast": "SE", "southwest": "SW",
    "upper-left": "NW", "upper-right": "NE", "lower-left": "SW", "lower-right": "SE",
    "top-left": "NW", "top-right": "NE", "bottom-left": "SW", "bottom-right": "SE",
    "upper": "N", "lower": "S", "top": "N", "bottom": "S", "up": "N", "down": "S",
}
# Distance (not a direction) -- tagged distance algebra, recorded under cardinal_direction family.
_DIST = {"near": "NEAR", "near to": "NEAR", "close": "NEAR", "far": "FAR", "far from": "FAR"}
# 3-D depth -- NOT part of standard 2-D CDC; flagged out_of_cdc.
_DEPTH = {"front": "FRONT", "in front": "FRONT", "in front of": "FRONT",
          "behind": "BEHIND", "back": "BEHIND"}


def map_relation(native: str) -> dict:
    """Map ONE native relation token/phrase to {algebra, canonical, flags}.

    algebra in {rcc8, cardinal_direction, unmapped}.
    Returns canonical=None and algebra='unmapped' for tokens we cannot place
    (so the card can report relation-vocab coverage honestly -- never fabricate).
    """
    t = native.strip().lower()
    if t in _RCC8_TOKEN:
        return {"algebra": "rcc8", "canonical": _RCC8_TOKEN[t], "subtype": "topological"}
    if t in _RCC8_VERBAL:
        return {"algebra": "rcc8", "canonical": _RCC8_VERBAL[t], "subtype": "topological"}
    if t in _DIR:
        return {"algebra": "cardinal_direction", "canonical": _DIR[t], "subtype": "direction"}
    if t in _DIST:
        return {"algebra": "cardinal_direction", "canonical": _DIST[t], "subtype": "distance"}
    if t in _DEPTH:
        return {"algebra": "cardinal_direction", "canonical": _DEPTH[t],
                "subtype": "depth_out_of_cdc"}
    # heuristic fallback: any "...touching...edge..." phrasing => inside & touching (TPP)
    if "touch" in t and "edge" in t:
        return {"algebra": "rcc8", "canonical": "TPP", "subtype": "topological"}
    return {"algebra": "unmapped", "canonical": None, "subtype": "unmapped"}


def map_relation_list(natives) -> dict:
    """Map a list of native relation tokens (one stated edge can carry several,
    e.g. SpaRP 'below, dc, front').  Returns aggregated algebra/canonical/flags."""
    algebras, canon, subtypes, unmapped = set(), [], set(), []
    for n in natives:
        m = map_relation(n)
        if m["algebra"] == "unmapped":
            unmapped.append(n)
        else:
            algebras.add(m["algebra"])
            canon.append(m["canonical"])
            subtypes.add(m["subtype"])
    if not algebras:
        primary = "unmapped"
    elif algebras == {"rcc8"}:
        primary = "rcc8"
    elif algebras == {"cardinal_direction"}:
        primary = "cardinal_direction"
    else:
        primary = "mixed"
    return {
        "algebra": primary,
        "canonical": canon,
        "subtypes": sorted(subtypes),
        "unmapped": unmapped,
    }
