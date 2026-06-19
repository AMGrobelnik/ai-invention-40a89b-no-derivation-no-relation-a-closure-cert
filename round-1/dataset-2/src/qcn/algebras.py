"""Qualitative relation algebras: convex Point, Allen Interval, RCC-8.

Composition (TransTable) and converse maps are loaded from the AUTHORITATIVE
qualreas algebra definitions (alreich/qualreas), bundled in ``algebra_tables/``.
These are the standard tables (Allen-1983 interval composition; Renz & Nebel
RCC-8 composition; linear point algebra).  We map qualreas relation codes to the
canonical codes used throughout this dataset:

  point : '<' '=' '>'
  allen : b bi m mi o oi d di s si f fi eq           (qualreas E -> eq)
  rcc8  : DC EC PO EQ TPP NTPP TPPi NTPPi             (qualreas *I -> *i)

The tables are cross-checked by three INDEPENDENT derivations in
``tests/test_qcn.py``:
  * point composition vs. direct sign reasoning,
  * Allen composition vs. exhaustive endpoint-CSP enumeration,
  * RCC-8 composition soundness vs. exhaustive integer disc-triple enumeration,
plus relation-algebra axioms (identity, involution / Peirce law).
"""
from __future__ import annotations

import json
from itertools import product
from pathlib import Path
from typing import Dict, FrozenSet, List, Tuple

_TABLE_DIR = Path(__file__).resolve().parent / "algebra_tables"

# qualreas-code -> canonical-code maps -------------------------------------------------
_POINT_MAP = {"<": "<", "=": "=", ">": ">"}
_ALLEN_MAP = {
    "B": "b", "BI": "bi", "M": "m", "MI": "mi", "O": "o", "OI": "oi",
    "D": "d", "DI": "di", "S": "s", "SI": "si", "F": "f", "FI": "fi", "E": "eq",
}
_RCC8_MAP = {
    "DC": "DC", "EC": "EC", "PO": "PO", "EQ": "EQ",
    "TPP": "TPP", "NTPP": "NTPP", "TPPI": "TPPi", "NTPPI": "NTPPi",
}

# canonical base-relation orderings (stable, used for serialization / histograms)
POINT_BASE = ["<", "=", ">"]
ALLEN_BASE = ["b", "bi", "m", "mi", "o", "oi", "d", "di", "s", "si", "f", "fi", "eq"]
RCC8_BASE = ["DC", "EC", "PO", "EQ", "TPP", "NTPP", "TPPi", "NTPPi"]


class Algebra:
    """A qualitative relation algebra with composition, converse and helpers."""

    def __init__(self, name: str, base: List[str], converse: Dict[str, str],
                 comp: Dict[Tuple[str, str], FrozenSet[str]]):
        self.name = name
        self.base = list(base)
        self.base_set = frozenset(base)
        self.universe = frozenset(base)
        self.converse = dict(converse)
        self.comp = dict(comp)  # (r1, r2) -> frozenset of base relations
        # identity element of the algebra (the relation r with comp(r, x) == {x})
        self.identity = {"point": "=", "allen": "eq", "rcc8": "EQ"}[name]
        # stable index for ordering disjunctive labels
        self._idx = {r: i for i, r in enumerate(base)}

    # -- single-relation operations --------------------------------------------------
    def compose(self, r1: str, r2: str) -> FrozenSet[str]:
        return self.comp[(r1, r2)]

    def conv(self, r: str) -> str:
        return self.converse[r]

    # -- set (disjunctive label) operations ------------------------------------------
    def compose_sets(self, s1, s2) -> FrozenSet[str]:
        """Composition of two disjunctive labels: union of pairwise base comps."""
        out: set = set()
        for r1 in s1:
            for r2 in s2:
                out |= self.comp[(r1, r2)]
        return frozenset(out)

    def converse_set(self, s) -> FrozenSet[str]:
        return frozenset(self.converse[r] for r in s)

    @staticmethod
    def intersect(s1, s2) -> FrozenSet[str]:
        return frozenset(s1) & frozenset(s2)

    def sorted_label(self, s) -> List[str]:
        """Disjunctive label as a list in canonical base order."""
        return [r for r in self.base if r in s]

    # -- path composition (the certificate engine in miniature) ----------------------
    def compose_path(self, rels: List[str]) -> FrozenSet[str]:
        """Iterated composition of a sequence of *atomic* directed relations.

        rels = [rel(n0,n1), rel(n1,n2), ..., rel(n_{k-1},n_k)].
        Returns the composed disjunctive relation between n0 and n_k.
        """
        if not rels:
            return frozenset([self.identity])
        acc: FrozenSet[str] = frozenset([rels[0]])
        for r in rels[1:]:
            acc = self.compose_sets(acc, frozenset([r]))
        return acc


def _parse_transtable(tt: dict, code_map: Dict[str, str]) -> Dict[Tuple[str, str], FrozenSet[str]]:
    comp: Dict[Tuple[str, str], FrozenSet[str]] = {}
    for q1, row in tt.items():
        for q2, val in row.items():
            rels = frozenset(code_map[p] for p in val.split("|"))
            comp[(code_map[q1], code_map[q2])] = rels
    return comp


def _load(name: str, fname: str, code_map: Dict[str, str], base: List[str]) -> Algebra:
    d = json.loads((_TABLE_DIR / fname).read_text())
    rels = d["Relations"]
    converse = {code_map[q]: code_map[rels[q]["Converse"]] for q in rels}
    comp = _parse_transtable(d["TransTable"], code_map)
    # sanity: full base coverage and square composition table
    assert set(converse) == set(base), (name, "converse keys")
    assert len(comp) == len(base) ** 2, (name, "comp size", len(comp))
    return Algebra(name, base, converse, comp)


def load_algebras() -> Dict[str, Algebra]:
    return {
        "point": _load("point", "Linear_Point_Algebra.json", _POINT_MAP, POINT_BASE),
        "allen": _load("allen", "Linear_Interval_Algebra.json", _ALLEN_MAP, ALLEN_BASE),
        "rcc8": _load("rcc8", "RCC8_Algebra.json", _RCC8_MAP, RCC8_BASE),
    }


# ---------------------------------------------------------------------------------------
# Convex-point-algebra guard: which disjunctive point labels are CONVEX (pointisable).
# Path-consistency is complete only on the convex fragment; the non-convex '!=' ({<,>})
# must never appear in a point-arm disjunctive label.
_CONVEX_POINT_LABELS = [
    frozenset({"<"}), frozenset({"="}), frozenset({">"}),
    frozenset({"<", "="}), frozenset({"=", ">"}), frozenset({"<", "=", ">"}),
]


def is_convex_point_label(s) -> bool:
    return frozenset(s) in _CONVEX_POINT_LABELS


def convex_supersets_of(gold: str) -> List[FrozenSet[str]]:
    """All convex point labels that contain `gold` (sound supersets, no '!=')."""
    return [lab for lab in _CONVEX_POINT_LABELS if gold in lab]
