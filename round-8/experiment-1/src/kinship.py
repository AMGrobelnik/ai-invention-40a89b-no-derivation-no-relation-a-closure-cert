#!/usr/bin/env python3
"""Kinship finite-composition closure engine (the symbolic half of the pipeline).

CLUTRR's kinship calculus is a FINITE COMPOSITION TABLE over 11 abstract relation
TYPES -- and, as the dataset card states verbatim, it is NOT a full relation algebra:
"no general intersection/converse closure beyond these rules". A naive port of the
temporal PC-2 engine (Mackworth converse-intersection path-consistency) is therefore
UNSOUND here -- closing the converse constraints makes ~13% of GOLD-clean chains
spuriously collapse to EMPTY, because two derivation orders can yield two different
(individually valid) relations that the table does not reconcile. (We verified this
directly: PC-2-style closure gives 100% accuracy WHEN it answers but only 0.87
singleton-rate, with 2153/16131 clean rows collapsing.)

The SOUND closure for a finite composition table is a FORWARD LEAST-FIXPOINT
*UNION* DERIVATION over DEFINED compositions only -- exactly the backward/forward
chaining that produces CLUTRR's own `gold_proof`, and exactly what the emitted Prolog
`derive/3` predicate computes:

  D[(a,b)] = { t : t derivable for directed pair a->b by composing atomic links }

  * seed: every atomic edge a->b:t adds t to D[(a,b)] and conv(t) to D[(b,a)];
  * close: while changing, for every a-b-c, for t1 in D[(a,b)], t2 in D[(b,c)],
    if rules[t1][t2]=t3 is DEFINED, add t3 to D[(a,c)] (and conv(t3) to D[(c,a)]);
    UNDEFINED compositions add nothing (SOUND: "unknown", never a wrong fact).

OUTPUT CONTRACT (disjunction-preserving Mode-A / abstain-on-collapse Mode-B):
  * |D[query]| == 1  -> EMIT the relation (covered).            [unique derivation]
  * |D[query]| >  1  -> ABSTAIN (Mode-B CONFLICT certificate).  [incompatible derivations]
  * |D[query]| == 0  -> ABSTAIN (no connecting path = universe). [absent-relation / underdetermined]

This contract is hallucination-safe by construction: with no connecting path (the
absent-relation case, entities in different components) D is empty, so the engine
NEVER invents a kinship -- it abstains. The naive single-pass baseline uses ONLY the
seed (atomic) edges and one composition step, so it resolves hop-2 chains but abstains
on hop>=3 (the iteration contrast), while the full fixpoint derives the intermediate
composite edges first and resolves the whole chain.
"""
from __future__ import annotations

from collections import defaultdict, deque
from typing import Iterable


class Kinship:
    """Finite kinship composition calculus parsed from the dataset composition table."""

    def __init__(self, comp_table: dict):
        rt = comp_table["relation_types"]
        self.base: list[str] = list(rt.keys())  # 11 abstract relation types
        self.universe = frozenset(self.base)
        self.empty = frozenset()
        self.symmetric_types = set(comp_table["symmetric_types"])  # {'sibling','SO'}
        self.inv: dict[str, str] = {}
        for a, b in comp_table["inverse_pairs"].items():
            self.inv[a] = b
            self.inv[b] = a
        self.composition_rules = comp_table["composition_rules"]
        self.surface_forms = comp_table["surface_forms"]
        self.surface_reverse = comp_table["surface_reverse"]
        self.label_map = comp_table.get("label_map", {})
        self.label_map_reverse = comp_table.get("label_map_reverse", {})
        # ---- total converse over every base type (sound; no empties) ----
        self._conv: dict[str, str] = {}
        for t in self.base:
            if t in self.symmetric_types:
                self._conv[t] = t
            elif t in self.inv:
                self._conv[t] = self.inv[t]
            elif t == "sibling-in-law":
                # brother/sister-in-law are mutual: converse(sibling-in-law)=sibling-in-law.
                self._conv[t] = t
            else:
                self._conv[t] = t  # sound self-converse fallback (never reached for the 11 types)

    # ------------------------------------------------------------------ ops
    def conv_type(self, t: str) -> str:
        return self._conv[t]

    def compose_types(self, t1: str, t2: str):
        """Defined composition rules[t1][t2]=t3, else None (UNDEFINED == 'unknown')."""
        return self.composition_rules.get(t1, {}).get(t2)

    def label(self, s) -> str:
        s = frozenset(s)
        if not s:
            return "EMPTY"
        if s == self.universe:
            return "UNIVERSE"
        return "|".join(t for t in self.base if t in s)

    # ------------------------------------------------------------- surface words
    def surface(self, rel_type: str, gender: str) -> str:
        g = "male" if str(gender).lower().startswith("m") else "female"
        sf = self.surface_forms.get(rel_type)
        if not sf:
            return rel_type
        return sf.get(g, sf.get("male", rel_type))

    def surface_to_type(self, surface_word: str):
        """Return (relation_type, implied_gender) or None for an unknown word."""
        w = str(surface_word).strip().lower()
        rev = self.surface_reverse.get(w)
        if rev is None:
            return None
        return rev[0], rev[1]


# --------------------------------------------------------------------------- #
# Forward least-fixpoint UNION derivation (the sound closure for the finite table)
# --------------------------------------------------------------------------- #
def _seed(kin: Kinship, atomic_edges: list[dict]):
    """Seed D with atomic edges + their converses. Returns (D, nbrs).
    D[(a,b)] = set of types; nbrs[a] = set of directed successors."""
    D: dict = defaultdict(set)
    nbrs: dict = defaultdict(set)

    def add(a, b, t):
        if t not in D[(a, b)]:
            D[(a, b)].add(t)
            nbrs[a].add(b)

    for e in atomic_edges:
        t = e["type"]
        if t not in kin.base:
            continue
        a, b = e["a"], e["b"]
        if a == b:
            continue
        add(a, b, t)
        add(b, a, kin.conv_type(t))
    return D, nbrs


def forward_closure(kin: Kinship, atomic_edges: list[dict], with_prov: bool = False):
    """Forward least-fixpoint union derivation. Returns (D, nbrs, n_fired) or, with
    with_prov, (D, nbrs, n_fired, prov) where prov[(a,c,t3)] = (a,b,c,t1,t2,t3) records
    the FIRST composition that produced type t3 on pair (a,c) (a directed-edge of the
    proof DAG; seed edges map to None).

    D[(a,b)] holds EVERY relation type derivable for the directed pair a->b; closed
    under defined composition + converse. n_fired = number of new type-additions."""
    D, nbrs = _seed(kin, atomic_edges)
    prov: dict = {}
    if with_prov:
        for (a, b), ts in D.items():
            for t in ts:
                prov.setdefault((a, b, t), None)
    Q = deque(D.keys())
    inq = set(D.keys())
    n_fired = 0

    def push(p):
        if p not in inq:
            inq.add(p)
            Q.append(p)

    def emit(a, c, t3, provtuple):
        nonlocal n_fired
        grew = False
        if t3 not in D[(a, c)]:
            D[(a, c)].add(t3)
            nbrs[a].add(c)
            if with_prov:
                prov.setdefault((a, c, t3), provtuple)
            n_fired += 1
            grew = True
        ct3 = kin.conv_type(t3)
        if ct3 not in D[(c, a)]:
            D[(c, a)].add(ct3)
            nbrs[c].add(a)
            if with_prov:
                prov.setdefault((c, a, ct3), (c, a, a, ct3, None, ct3))  # converse marker
        if grew:
            push((a, c)); push((c, a))

    while Q:
        (a, b) = Q.popleft()
        inq.discard((a, b))
        tab = list(D[(a, b)])
        # extend a->b with b->c  =>  a->c
        for c in list(nbrs[b]):
            if c == a:
                continue
            for t1 in tab:
                for t2 in list(D[(b, c)]):
                    t3 = kin.compose_types(t1, t2)
                    if t3 is not None:
                        emit(a, c, t3, (a, b, c, t1, t2, t3))
        # extend z->a with a->b  =>  z->b   (a is the middle)
        for z in list(nbrs[a]):
            if z == b:
                continue
            for t1 in list(D[(z, a)]):
                for t2 in tab:
                    t3 = kin.compose_types(t1, t2)
                    if t3 is not None:
                        emit(z, b, t3, (z, a, b, t1, t2, t3))
    if with_prov:
        return D, nbrs, n_fired, prov
    return D, nbrs, n_fired


def naive_single_pass(kin: Kinship, atomic_edges: list[dict], qsrc, qtgt) -> set:
    """BASELINE: ONE composition pass at the query edge using ONLY seed (atomic) edges.

    R = union over intermediates w of {rules[t1][t2] : t1 in seed(u,w), t2 in seed(w,v)}.
    NO fixpoint, NO derived edges. On a hop-k chain only the hop-2 case has an
    intermediate w with BOTH atomic links to the endpoints, so naive resolves hop-2 but
    derives nothing (-> abstain) on hop>=3."""
    D, nbrs = _seed(kin, atomic_edges)
    R: set = set()
    for w in nbrs.get(qsrc, ()):
        if w in (qsrc, qtgt):
            continue
        if (w, qtgt) in D:
            for t1 in D[(qsrc, w)]:
                for t2 in D[(w, qtgt)]:
                    t3 = kin.compose_types(t1, t2)
                    if t3 is not None:
                        R.add(t3)
    return R


# --------------------------------------------------------------------------- #
# Query wrappers with the Mode-A / Mode-B output contract
# --------------------------------------------------------------------------- #
def _answer_from_set(kin: Kinship, R: set) -> dict:
    R = set(R)
    n = len(R)
    if n == 1:
        t = next(iter(R))
        return {"types": sorted(R), "singleton": True, "answer_type": t,
                "n_derivations": n, "mode_b_conflict": False, "no_path": False}
    if n == 0:
        return {"types": [], "singleton": False, "answer_type": None,
                "n_derivations": 0, "mode_b_conflict": False, "no_path": True}
    # n > 1 : incompatible derivations => Mode-B conflict
    rep = sorted(R, key=lambda t: kin.base.index(t))[0]  # deterministic representative
    return {"types": sorted(R), "singleton": False, "answer_type": rep,
            "n_derivations": n, "mode_b_conflict": True, "no_path": False}


def query_modeA(kin: Kinship, atomic_edges: list[dict], qsrc, qtgt) -> dict:
    """Mode-A forward-closure query. Returns the output-contract decision + n_fired."""
    D, nbrs, n_fired = forward_closure(kin, atomic_edges)
    R = D.get((qsrc, qtgt), set())
    out = _answer_from_set(kin, R)
    out["n_fired"] = n_fired
    return out


def query_naive(kin: Kinship, atomic_edges: list[dict], qsrc, qtgt) -> dict:
    """Naive single-pass query (fresh seed only)."""
    R = naive_single_pass(kin, atomic_edges, qsrc, qtgt)
    return _answer_from_set(kin, R)


def simple_paths_names(atomic_edges: list[dict], qsrc, qtgt, max_paths: int = 3,
                       max_len: int = 12):
    """Up to `max_paths` simple undirected entity paths qsrc..qtgt over the atomic-edge
    graph (feeds Path-of-Thoughts). Returns lists of node names, shortest first."""
    adj: dict = {}
    for e in atomic_edges:
        adj.setdefault(e["a"], set()).add(e["b"])
        adj.setdefault(e["b"], set()).add(e["a"])
    if qsrc not in adj or qtgt not in adj:
        return []
    paths: list[list] = []
    stack = [(qsrc, [qsrc])]
    while stack and len(paths) < max_paths * 4:
        node, path = stack.pop()
        if len(path) > max_len:
            continue
        for nb in sorted(adj.get(node, ())):
            if nb == qtgt:
                paths.append(path + [nb])
            elif nb not in path:
                stack.append((nb, path + [nb]))
    paths.sort(key=len)
    # de-dup
    seen = set(); uniq = []
    for p in paths:
        k = tuple(p)
        if k not in seen:
            seen.add(k); uniq.append(p)
    return uniq[:max_paths]


def derivation_trace(kin: Kinship, atomic_edges: list[dict], qsrc, qtgt,
                     max_steps: int = 60):
    """Reconstruct ONE concrete derivation for (qsrc->qtgt) for the trace-graph:
    which (t1 o t2 -> t3) compositions fire, mirroring the gold backward proof.
    Returns a list of {a,b,c,t1,t2,t3} steps producing the answer type, or [] if the
    query is not a unique-derivation singleton."""
    D, nbrs, _, prov = forward_closure(kin, atomic_edges, with_prov=True)
    target = D.get((qsrc, qtgt), set())
    if len(target) != 1:
        return []
    goal_type = next(iter(target))
    steps = []
    stack = [(qsrc, qtgt, goal_type)]
    seen = set()
    while stack and len(steps) < max_steps:
        key = stack.pop()
        if key in seen:
            continue
        seen.add(key)
        p = prov.get(key)
        if p is None:
            continue  # seed edge (atomic fact) -- a leaf of the proof DAG
        a, b, c, t1, t2, t3 = p
        if t2 is None:
            # converse marker: unfold to the forward edge (b->a : conv(t3))
            stack.append((c, a, kin.conv_type(t3)))
            continue
        steps.append({"a": a, "b": b, "c": c, "t1": t1, "t2": t2, "t3": t3})
        stack.append((a, b, t1))
        stack.append((b, c, t2))
    steps.reverse()
    return steps


if __name__ == "__main__":
    import json, glob
    base = ("/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/"
            "gen_art/gen_art_dataset_1/full_data_out")
    part = json.load(open(sorted(glob.glob(base + "/full_data_out_*.json"))[0]))
    kin = Kinship(part["metadata"]["composition_table"])
    print("types:", kin.base)
    print("conv:", kin._conv)
    # Lena -> Andrea (brother-wife-daughter) should derive 'un' (niece)
    edges = [{"a": "Lena", "b": "Joshua", "type": "sibling"},
             {"a": "Joshua", "b": "Lynn", "type": "SO"},
             {"a": "Lynn", "b": "Andrea", "type": "child"}]
    print("Mode-A Lena->Andrea:", query_modeA(kin, edges, "Lena", "Andrea"))
    print("naive Lena->Andrea:", query_naive(kin, edges, "Lena", "Andrea"))
    print("trace:", derivation_trace(kin, edges, "Lena", "Andrea"))
