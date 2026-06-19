"""Model-based realization of qualitative scenarios.

Each network is built by embedding every node in a concrete geometric model and
reading the gold ATOMIC relation off the model.  A realizable model is, by
construction, GLOBALLY CONSISTENT -- no constraint solver is needed to certify
consistency, and the gold relation on every pair is exact.

  point : node -> integer coordinate x          ; rel = sign(x_i - x_j)
  allen : node -> integer interval (s, e), s<e   ; rel = 13-case endpoint compare
  rcc8  : node -> integer disc (cx, cy, r), r>=1 ; rel via exact d^2 integer compare
          (centers are placed COLLINEAR so that internal/external tangency EC, TPP
           and equality EQ are realized exactly with integer arithmetic; every
           pairwise relation is a genuine RCC-8 relation, so the scenario is a
           valid -- and globally consistent -- RCC-8 model.)

Endpoints / coordinates / radii are drawn from SMALL integer pools so that
coincidences occur and the degenerate relations (point '='; Allen m/mi/s/si/f/fi/eq;
RCC-8 EC/TPP/TPPi/EQ) are realized with non-trivial frequency.
"""
from __future__ import annotations

from typing import List, Sequence, Tuple

import numpy as np

# ----------------------------------------------------------------------------- readers
def point_rel(xi: int, xj: int) -> str:
    if xi < xj:
        return "<"
    if xi > xj:
        return ">"
    return "="


def allen_rel(x: Tuple[int, int], y: Tuple[int, int]) -> str:
    """Allen interval relation of x w.r.t. y. Requires xs<xe and ys<ye."""
    xs, xe = x
    ys, ye = y
    if xe < ys:
        return "b"
    if xe == ys:
        return "m"
    if xs > ye:
        return "bi"
    if xs == ye:
        return "mi"
    # proper overlap guaranteed: xe>ys and xs<ye
    if xs == ys:
        if xe == ye:
            return "eq"
        return "s" if xe < ye else "si"
    if xe == ye:
        return "fi" if xs < ys else "f"
    if xs < ys:
        return "o" if xe < ye else "di"
    # xs > ys
    return "d" if xe < ye else "oi"


def rcc8_rel(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> str:
    """RCC-8 relation of disc a w.r.t. disc b using exact integer arithmetic."""
    ax, ay, ar = a
    bx, by, br = b
    d2 = (ax - bx) ** 2 + (ay - by) ** 2
    s2 = (ar + br) ** 2
    df = ar - br
    df2 = df * df
    if d2 > s2:
        return "DC"
    if d2 == s2:
        return "EC"
    # d2 < s2 : overlap or containment
    if d2 == 0 and ar == br:
        return "EQ"
    if d2 < df2:
        return "NTPP" if ar < br else "NTPPi"
    if d2 == df2:  # internal tangency (ar != br here, else EQ already returned)
        return "TPP" if ar < br else "TPPi"
    return "PO"


_READERS = {"point": point_rel, "allen": allen_rel, "rcc8": rcc8_rel}


def relation(algebra: str, oi, oj) -> str:
    """Gold atomic relation between two embedded objects (directed: oi rel oj)."""
    return _READERS[algebra](oi, oj)


# ------------------------------------------------------------------------- realization
def realize(algebra: str, n_nodes: int, rng: np.random.RandomState) -> List:
    """Return a list of embedded objects (one per node) drawn from small integer pools.

    Pools are sized so endpoint/coordinate coincidences -- hence degenerate relations
    -- occur with non-trivial probability.
    """
    if algebra == "point":
        pool = max(3, int(round(1.6 * n_nodes)))  # collisions -> '=' appears
        return [int(v) for v in rng.randint(0, pool + 1, size=n_nodes)]

    if algebra == "allen":
        # draw two distinct integer time points from a small pool; coincident endpoints
        # across nodes realize m/mi/s/si/f/fi/eq.
        pts = max(4, int(round(1.4 * n_nodes)))
        out: List[Tuple[int, int]] = []
        for _ in range(n_nodes):
            a = int(rng.randint(0, pts))
            b = int(rng.randint(0, pts))
            while a == b:
                b = int(rng.randint(0, pts))
            out.append((min(a, b), max(a, b)))
        return out

    if algebra == "rcc8":
        # collinear discs: center on x-axis (cy=0), radius>=1, both from small pools.
        cpool = max(4, int(round(1.5 * n_nodes)))
        rpool = max(2, n_nodes // 2 + 1)
        out2: List[Tuple[int, int, int]] = []
        for _ in range(n_nodes):
            cx = int(rng.randint(0, cpool + 1))
            r = int(rng.randint(1, rpool + 1))
            out2.append((cx, 0, r))
        return out2

    raise ValueError(f"unknown algebra {algebra!r}")


# -------------------------------------------------------------- explicit relation planting
# Concrete model fragments that realize EACH base relation, used to guarantee global
# coverage of all base relations even if random sampling under-represents a degenerate one.
def planted_pair(algebra: str, rel: str):
    """Return a concrete (obj_i, obj_j) pair whose gold relation == rel (verified)."""
    if algebra == "point":
        table = {"<": (0, 1), "=": (1, 1), ">": (1, 0)}
        return table[rel]
    if algebra == "allen":
        table = {
            "b": ((0, 1), (2, 3)), "bi": ((2, 3), (0, 1)),
            "m": ((0, 1), (1, 2)), "mi": ((1, 2), (0, 1)),
            "o": ((0, 2), (1, 3)), "oi": ((1, 3), (0, 2)),
            "d": ((1, 2), (0, 3)), "di": ((0, 3), (1, 2)),
            "s": ((0, 1), (0, 2)), "si": ((0, 2), (0, 1)),
            "f": ((1, 2), (0, 2)), "fi": ((0, 2), (1, 2)),
            "eq": ((0, 1), (0, 1)),
        }
        return table[rel]
    if algebra == "rcc8":
        # collinear discs (cx, 0, r)
        table = {
            "DC": ((0, 0, 1), (5, 0, 1)),
            "EC": ((0, 0, 2), (5, 0, 3)),       # d=5 == 2+3
            "PO": ((0, 0, 3), (4, 0, 3)),       # |0|<4<6
            "EQ": ((0, 0, 2), (0, 0, 2)),
            "TPP": ((1, 0, 1), (0, 0, 2)),      # d=1 == 2-1, a inside b tangent
            "NTPP": ((0, 0, 1), (0, 0, 3)),     # d=0 < 3-1
            "TPPi": ((0, 0, 2), (1, 0, 1)),
            "NTPPi": ((0, 0, 3), (0, 0, 1)),
        }
        return table[rel]
    raise ValueError(algebra)
