"""Template NL realization of a qualitative constraint network.

Each NON-query edge is verbalized as ONE professional-prose sentence describing its
gold relation (chosen among 2-3 paraphrases, recorded per edge for error analysis).
The held-out query edge is NEVER verbalized; the document ends with a single
``Query:`` line.  Entities are unique within a network and drawn from pools of >=50
distinct phrases (temporal for point/allen, spatial for rcc8).
"""
from __future__ import annotations

from typing import Dict, List, Tuple

import numpy as np

# ---------------------------------------------------------------- entity phrase pools
TEMPORAL_POOL: List[str] = [
    "the merger announcement", "the board meeting", "the product launch",
    "the regulatory filing", "the press briefing", "the quarterly audit",
    "the shareholder vote", "the funding round", "the site inspection",
    "the contract signing", "the staff onboarding", "the policy rollout",
    "the data migration", "the system outage", "the security patch",
    "the marketing campaign", "the earnings call", "the budget review",
    "the hiring freeze", "the office relocation", "the pilot program",
    "the customer survey", "the compliance training", "the vendor negotiation",
    "the prototype demo", "the field trial", "the litigation hearing",
    "the patent submission", "the supplier handover", "the inventory count",
    "the network upgrade", "the recruitment drive", "the strategy offsite",
    "the certification review", "the maintenance window", "the price adjustment",
    "the partnership signing", "the recall notice", "the warehouse expansion",
    "the software release", "the tax assessment", "the safety drill",
    "the procurement cycle", "the design review", "the investor roadshow",
    "the membership renewal", "the catalog refresh", "the loan disbursement",
    "the depot closure", "the franchise opening", "the trademark dispute",
    "the seasonal promotion", "the freight shipment", "the annual report",
    "the holiday shutdown", "the equipment delivery", "the licensing deal",
    "the curriculum update", "the grant disbursal", "the venue booking",
]

SPATIAL_POOL: List[str] = [
    "the industrial zone", "the flood plain", "the conservation area",
    "the harbor district", "Parcel A", "Parcel B", "the buffer strip",
    "the wetland reserve", "the transit corridor", "the commercial block",
    "the residential tract", "the quarry site", "the green belt",
    "the watershed basin", "the customs enclave", "the parking precinct",
    "the warehouse lot", "the heritage district", "the airport perimeter",
    "the coastal margin", "the forest compartment", "the mining lease",
    "the irrigation district", "the campus grounds", "the utility easement",
    "the protected habitat", "the floodway channel", "the survey block",
    "the municipal park", "the freight terminal", "the orchard plot",
    "the recreation ground", "the levee district", "the railway reserve",
    "the cemetery grounds", "the pasture allotment", "the marina basin",
    "the vineyard estate", "the construction site", "the landfill cell",
    "the nature sanctuary", "the harbor jetty", "the school catchment",
    "the power substation", "the grazing common", "the riverside walk",
    "the market square", "the depot yard", "the sports complex",
    "the embassy compound", "the shopping precinct", "the fishing ground",
    "the tunnel approach", "the meadow enclosure", "the dockland estate",
    "the highway verge", "the plantation block", "the reservoir margin",
    "the village green", "the customs yard",
]

# ---------------------------------------------------------------- templates per relation
POINT_TEMPLATES: Dict[str, List[str]] = {
    "<": ["{A} occurred before {B}.", "{A} took place earlier than {B}.",
          "{A} came before {B}."],
    "=": ["{A} happened at the same time as {B}.",
          "{A} occurred simultaneously with {B}.", "{A} and {B} coincided in time."],
    ">": ["{A} occurred after {B}.", "{A} took place later than {B}.",
          "{A} came after {B}."],
}

ALLEN_TEMPLATES: Dict[str, List[str]] = {
    "b": ["{A} ended before {B} began.", "{A} was entirely over before {B} started."],
    "bi": ["{A} began only after {B} had ended.",
           "{A} started after {B} was completely finished."],
    "m": ["{A} ended exactly as {B} began.",
          "{A} finished at the very moment {B} started."],
    "mi": ["{A} began exactly as {B} ended.",
           "{A} started at the very moment {B} finished."],
    "o": ["{A} began before {B} and the two overlapped, with {A} finishing first.",
          "{A} started first and was still ongoing when {B} began, yet {A} ended before {B} did."],
    "oi": ["{A} began after {B} and the two overlapped, with {A} finishing later.",
           "{B} started first and was still ongoing when {A} began, and {A} ended after {B} did."],
    "d": ["{A} took place entirely during {B}.",
          "{A} happened wholly within the span of {B}."],
    "di": ["{A} began before {B} and ended after it, spanning {B} entirely.",
           "{B} took place entirely during {A}."],
    "s": ["{A} and {B} began together, but {A} ended first.",
          "{A} and {B} started at the same time, with {A} finishing earlier."],
    "si": ["{A} and {B} began together, but {A} ended later.",
           "{A} and {B} started at the same time, with {A} finishing later."],
    "f": ["{A} and {B} ended together, but {A} began later.",
          "{A} and {B} finished at the same time, with {A} starting later."],
    "fi": ["{A} and {B} ended together, but {A} began earlier.",
           "{A} and {B} finished at the same time, with {A} starting earlier."],
    "eq": ["{A} and {B} spanned exactly the same period.",
           "{A} and {B} occurred over precisely the same interval."],
}

RCC8_TEMPLATES: Dict[str, List[str]] = {
    "DC": ["{A} is completely separate from {B}.",
           "{A} and {B} are disconnected, sharing no points."],
    "EC": ["{A} touches {B} along its boundary without overlapping.",
           "{A} and {B} meet at their boundary but share no interior."],
    "PO": ["{A} and {B} partially overlap.",
           "{A} and {B} share a common region while each also extends beyond the other."],
    "EQ": ["{A} occupies exactly the same area as {B}.",
           "{A} and {B} cover precisely the same region."],
    "TPP": ["{A} lies inside {B} and touches its boundary.",
            "{A} is contained within {B}, meeting {B}'s outer edge."],
    "NTPP": ["{A} lies strictly inside {B}.",
             "{A} is contained well within {B}, away from its boundary."],
    "TPPi": ["{A} contains {B}, which touches {A}'s boundary.",
             "{B} lies inside {A} and meets {A}'s boundary."],
    "NTPPi": ["{A} strictly contains {B}.", "{B} lies strictly inside {A}."],
}

_TEMPLATES = {"point": POINT_TEMPLATES, "allen": ALLEN_TEMPLATES, "rcc8": RCC8_TEMPLATES}
_POOL = {"point": TEMPORAL_POOL, "allen": TEMPORAL_POOL, "rcc8": SPATIAL_POOL}
_QUERY_KIND = {"point": "temporal", "allen": "temporal", "rcc8": "spatial"}


def assign_entities(algebra: str, nodes: List[int], rng: np.random.RandomState
                    ) -> Dict[int, str]:
    pool = _POOL[algebra]
    if len(nodes) > len(pool):
        raise ValueError(f"network has {len(nodes)} nodes > pool {len(pool)}")
    chosen = rng.choice(len(pool), size=len(nodes), replace=False)
    return {int(n): pool[int(i)] for n, i in zip(nodes, chosen)}


def realize_text(algebra: str, edges: List[Tuple[int, int, str]],
                 entity_map: Dict[int, str], s: int, t: int,
                 rng: np.random.RandomState) -> Tuple[str, Dict[str, int]]:
    """Return (document, templates_used). Each edge -> one sentence; query is a final line."""
    tmpl = _TEMPLATES[algebra]
    sentences: List[str] = []
    templates_used: Dict[str, int] = {}
    order = list(range(len(edges)))
    rng.shuffle(order)
    for ei in order:
        u, v, rel = edges[ei]
        assert {u, v} != {s, t}, "query pair must not be a verbalized edge"
        paraphrases = tmpl[rel]
        idx = int(rng.randint(0, len(paraphrases)))
        templates_used[f"{u}-{v}"] = idx
        # format with raw phrases, then capitalize ONLY the sentence-initial character
        # (so mid-sentence entity repeats stay lowercase, e.g. "..., but the offsite ...").
        sentence = _cap(paraphrases[idx].format(A=entity_map[u], B=entity_map[v]))
        sentences.append(sentence)
    query_line = (f"Query: what is the {_QUERY_KIND[algebra]} relation between "
                  f"{entity_map[s]} and {entity_map[t]}?")
    document = " ".join(sentences) + "\n" + query_line
    return document, templates_used


def _cap(phrase: str) -> str:
    """Capitalize the first character for sentence-initial position (keeps proper names)."""
    return phrase[0].upper() + phrase[1:] if phrase else phrase
