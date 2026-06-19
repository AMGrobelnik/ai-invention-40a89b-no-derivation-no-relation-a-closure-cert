#!/usr/bin/env python3
"""Natural-corpus loader + entity grounding for the Re-DocRED/DocRED LOCATED-IN
(administrative-containment) corpus -- the iter-8 drop-in adaptation of iter-7's
dataio_redocred.py.

This is the SECOND genuinely-natural absent-relation domain (after kinship). The engine,
grounding, and record schema are reused verbatim; the located-in domain differs in three
load-bearing ways that this module implements:

  CHANGE 1 (held_out direct-edge ABLATION) -- the single most important new rule. The
    corpus engine_edge_mapping states verbatim: 'For a held_out query, FIRST drop the
    single atomic edge whose (source,target)==(query source,target) before querying.'
    A held_out present pair has a DIRECTLY-annotated located_in edge that is ALSO derivable
    via an alternative >=2-hop path; removing the redundant direct edge preserves the full
    transitive closure (SOUND) and forces a genuine deduction, so PRESENT coverage becomes a
    real deductive result rather than a read-back. never_annotated pairs have no direct edge,
    so the drop is a no-op there.

  CHANGE 2 (absent REGIME tag) -- decisive for the headline. Absent pairs split into
    different_component (unrelated places; the clean kinship-analog) and
    same_component_sibling (co-component places, neither inside the other -- the
    containment-specific regime that is NOT structural-by-construction: their closure is
    EMPTY because located_in o contains is UNDEFINED, a genuine deductive abstention).

  CHANGE 3 (located_in gold primitive / surface) -- located_in is gender-free; gold
    primitive='located_in', gold word='located in', no kinship_relation field.

Two id systems coexist (identical to iter-7): CLOSURE KEYS = gold ENTITY_IDS (ints);
PROMPT NAMES = entity SURFACES (strings). A record carries both qsrc/qtgt (entity_ids) and
qsrc_name/qtgt_name (surfaces). Scoring is PRIMITIVE-level.
"""
from __future__ import annotations

import json
import re

_WS = re.compile(r"\s+")


def norm(s) -> str:
    """Normalize a mention/name string for alias matching."""
    return _WS.sub(" ", str(s).strip().lower())


def load_slice(full: dict, slice_name: str, with_strata_only: bool = True) -> list[dict]:
    """Return the rows (examples) of one dataset slice. By default keep only documents
    that actually carry a present-query or absent-pair stratum (the ones that need reads)."""
    rows = []
    for ds in full["datasets"]:
        if ds["dataset"] != slice_name:
            continue
        for ex in ds["examples"]:
            gg = json.loads(ex["output"])
            if with_strata_only and not (gg.get("query_edges") or gg.get("absent_relation_pairs")):
                continue
            rows.append(ex)
    return rows


def build_doc_context(row: dict) -> dict:
    """Parse one document row into a reusable context: text, gold graph, id->surface,
    id->gender (default 'male' for surface rendering only; located_in is gender-free), and
    the mention alias table (normalized mention string -> entity_id or 'AMBIGUOUS')."""
    gg = json.loads(row["output"])
    text = row["input"]
    id2surface = {n["entity_id"]: n["surface"] for n in gg["nodes"]}
    id2gender = {n["entity_id"]: (n.get("gender") or "male") for n in gg["nodes"]}
    alias2id: dict[str, object] = {}
    for n in gg["nodes"]:
        eid = n["entity_id"]
        names = {norm(n["surface"])}
        for span in n.get("mention_spans", []):
            try:
                cs, ce = span[0], span[1]
                names.add(norm(text[cs:ce]))
            except (TypeError, IndexError):
                continue
        for nm in names:
            if not nm:
                continue
            if nm in alias2id and alias2id[nm] != eid:
                alias2id[nm] = "AMBIGUOUS"
            else:
                alias2id[nm] = eid
    return {"text": text, "gg": gg, "id2surface": id2surface,
            "id2gender": id2gender, "alias2id": alias2id,
            "doc_id": gg["doc_id"], "source": row.get("metadata_source"),
            "split": row.get("metadata_split")}


def ground_name(name, ctx: dict):
    """Map an LLM-extracted place name to a gold entity_id, or to a normalized fallback
    node key ('NAME::<norm>') when it cannot be grounded. The fallback keeps the certificate
    SOUND: an ungroundable name simply becomes its own isolated node that never connects to
    gold ids (an honest recall penalty, never a fabricated link)."""
    nm = norm(name)
    if not nm:
        return "NAME::"
    a2i = ctx["alias2id"]
    v = a2i.get(nm)
    if v is not None and v != "AMBIGUOUS":
        return v
    # token-superset / substring match: name is a substring of (or contains) exactly ONE
    # distinct entity alias -> ground to that entity.
    hits = set()
    for al, eid in a2i.items():
        if eid is None or eid == "AMBIGUOUS":
            continue
        if len(nm) >= 3 and (nm in al or al in nm):
            hits.add(eid)
    if len(hits) == 1:
        return next(iter(hits))
    return "NAME::" + nm


def _atomics_to_id_edges(gg: dict, justifiable_only: bool = False) -> list[dict]:
    """Gold atomic located_in edges -> closure-engine edges keyed by ENTITY_ID:
    {a:source, b:target, type:primitive}. (Direction: a is located_in b.)
    justifiable_only -> keep only edges flagged locally_justifiable (span-extractable: the
    fair recall ceiling for a span-local reader; the rest are KB-implied)."""
    out = []
    for e in gg.get("atomic_edges", []):
        if justifiable_only and not e.get("locally_justifiable", False):
            continue
        out.append({"a": e["source"], "b": e["target"], "type": e["primitive"]})
    return out


def closure_edges_drop_direct(edges: list[dict], qsrc, qtgt) -> list[dict]:
    """Drop the single atomic edge whose endpoints are exactly the query pair (either
    direction) -- the held_out ablation. Removes the direct (qsrc,qtgt) edge AND its converse
    seed so the closure must DEDUCE the relation via the alternative >=2-hop path."""
    return [e for e in edges if {e["a"], e["b"]} != {qsrc, qtgt}]


def make_present_record(ctx, q, kin, slice_name) -> dict:
    gg = ctx["gg"]
    qsrc, qtgt = q["source"], q["target"]
    gold_prim = q.get("primitive", "located_in")
    gold_word = kin.surface(gold_prim, "male")  # 'located in' (gender-free)
    composed_only = bool(q.get("composed_only", False))
    # derive query_subtype robustly: prefer explicit query_kind, else composed_only, else
    # existence of a direct (qsrc,qtgt) atomic edge (held_out iff a direct edge exists).
    full_atomics = _atomics_to_id_edges(gg)
    has_direct = any({e["a"], e["b"]} == {qsrc, qtgt} for e in full_atomics)
    qkind = q.get("query_kind")
    if qkind in ("held_out", "never_annotated"):
        subtype = qkind
    elif composed_only:
        subtype = "never_annotated"
    else:
        subtype = "held_out" if has_direct else "never_annotated"
    is_held_out = subtype == "held_out"
    # PRIMARY: ablate the direct edge for held_out (no-op for never_annotated).
    gold_atomics = closure_edges_drop_direct(full_atomics, qsrc, qtgt) if is_held_out else full_atomics
    gold_atomics_just = _atomics_to_id_edges(gg, justifiable_only=True)
    if is_held_out:
        gold_atomics_just = closure_edges_drop_direct(gold_atomics_just, qsrc, qtgt)
    return {
        "doc_id": f"{slice_name}::{ctx['doc_id']}", "title": ctx["doc_id"], "slice": slice_name,
        "story": ctx["text"], "qsrc": qsrc, "qtgt": qtgt,
        "qsrc_name": ctx["id2surface"].get(qsrc, str(qsrc)),
        "qtgt_name": ctx["id2surface"].get(qtgt, str(qtgt)),
        "gold_surface": gold_prim, "gold_surface_word": gold_word, "gold_primitive": gold_prim,
        "is_absent": False, "hop": int(q.get("hop_count", 2)),
        "composed_only": composed_only, "query_subtype": subtype, "is_held_out": is_held_out,
        "fully_readable": bool(q.get("fully_readable", False)),
        "derivation_path": q.get("derivation_path", []), "noise_type": "natural",
        "absent_regime": None,
        "genders": ctx["id2gender"],
        "gold_atomics": gold_atomics,            # ablated for held_out (PRIMARY)
        "gold_atomics_full": full_atomics,        # un-ablated (sensitivity)
        "gold_atomics_just": gold_atomics_just,
        "_ctx": ctx, "_id2surface": ctx["id2surface"],
    }


def make_absent_record(ctx, p, kin, slice_name) -> dict:
    gg = ctx["gg"]
    qsrc, qtgt = p["source"], p["target"]
    reason = p.get("reason")
    if reason not in ("different_component", "same_component_sibling"):
        reason = "same_component_sibling" if p.get("same_component") else "different_component"
    regime = "same_component_sibling" if ("sibling" in reason or p.get("same_component")) else "different_component"
    full_atomics = _atomics_to_id_edges(gg)
    return {
        "doc_id": f"{slice_name}::{ctx['doc_id']}", "title": ctx["doc_id"], "slice": slice_name,
        "story": ctx["text"], "qsrc": qsrc, "qtgt": qtgt,
        "qsrc_name": ctx["id2surface"].get(qsrc, str(qsrc)),
        "qtgt_name": ctx["id2surface"].get(qtgt, str(qtgt)),
        "gold_surface": "no-relation", "gold_surface_word": "no-relation",
        "gold_primitive": "no-relation", "is_absent": True, "hop": 0,
        "composed_only": False, "query_subtype": regime, "is_held_out": False,
        "fully_readable": False, "derivation_path": [], "noise_type": "natural",
        "absent_regime": regime, "reason": reason,
        "genders": ctx["id2gender"],
        "gold_atomics": full_atomics,             # no direct (qsrc,qtgt) edge exists to drop
        "gold_atomics_full": full_atomics,
        "gold_atomics_just": _atomics_to_id_edges(gg, justifiable_only=True),
        "_ctx": ctx, "_id2surface": ctx["id2surface"],
    }


def build_records(rows: list[dict], kin, slice_name: str):
    """Build per-query records (present + absent) from one slice's document rows.
    Returns (records, contexts) where contexts maps doc_id -> doc context."""
    records, contexts = [], {}
    for row in rows:
        ctx = build_doc_context(row)
        did = f"{slice_name}::{ctx['doc_id']}"
        contexts[did] = ctx
        gg = ctx["gg"]
        for q in gg.get("query_edges", []):
            records.append(make_present_record(ctx, q, kin, slice_name))
        for p in gg.get("absent_relation_pairs", []):
            records.append(make_absent_record(ctx, p, kin, slice_name))
    return records, contexts


def id_path_to_names(id_path: list, ctx: dict) -> list:
    """Map an entity-id path to a name path for the Path-of-Thoughts prompt."""
    return [ctx["id2surface"].get(e, str(e)) for e in id_path]
