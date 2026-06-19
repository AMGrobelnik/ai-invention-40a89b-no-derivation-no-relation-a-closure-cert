#!/usr/bin/env python3
"""Natural-corpus loader + entity grounding for the Re-DocRED/DocRED kinship corpus.

This is the ONE substantively-new data module for iter-7 STEP-B. It converts the
one-row-per-document natural-prose dataset (`art_NUWTxBVWENIJ`) into per-QUERY record
dicts that plug UNCHANGED into the iter-6 confidence-battery / matched-coverage /
closure machinery (readers.py, kinship.py, baselines.py, stats.py).

Two id systems coexist and must never be confused:
  * CLOSURE KEYS  = gold ENTITY_IDS (ints). The forward-closure engine, gold atomic
    edges, derivation paths, and absent pairs all live in entity-id space.
  * PROMPT NAMES  = entity SURFACES (strings). Every LLM reader sees the natural prose
    and is asked about people by NAME, then returns NAMES; those names are GROUNDED
    back to gold entity_ids via the mention-span alias table so the certificate's
    forward closure runs over real reads.

A record therefore carries BOTH: `qsrc`/`qtgt` (entity_ids = closure keys) and
`qsrc_name`/`qtgt_name` (surfaces = prompt names). Scoring is PRIMITIVE-level (gender is
best-effort in DocRED): `gold_surface` holds the gold PRIMITIVE; `gold_surface_word`
holds the human gendered word (secondary).
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
    id->gender, and the mention alias table (normalized mention string -> entity_id or
    the 'AMBIGUOUS' sentinel)."""
    gg = json.loads(row["output"])
    text = row["input"]
    id2surface = {n["entity_id"]: n["surface"] for n in gg["nodes"]}
    # default 'male' is ONLY for surface RENDERING; all scoring is primitive-level
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
    """Map an LLM-extracted person name to a gold entity_id, or to a normalized fallback
    node key ('NAME::<norm>') when it cannot be grounded. The fallback keeps the
    certificate SOUND: an ungroundable name simply becomes its own isolated node that
    never connects to gold ids (an honest recall penalty, never a fabricated link)."""
    nm = norm(name)
    if not nm:
        return "NAME::"
    a2i = ctx["alias2id"]
    v = a2i.get(nm)
    if v is not None and v != "AMBIGUOUS":
        return v
    # token-superset / surname / substring match: name is a substring of (or contains)
    # exactly ONE distinct entity alias -> ground to that entity.
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
    """Gold atomic edges -> closure-engine edges keyed by ENTITY_ID:
    {a:source, b:target, type:primitive}. (Direction: target is source's primitive.)
    justifiable_only -> keep only edges flagged locally_justifiable (span-extractable: the
    fair recall ceiling for a span-local reader; the rest are KB-implied)."""
    out = []
    for e in gg.get("atomic_edges", []):
        if justifiable_only and not e.get("locally_justifiable", False):
            continue
        out.append({"a": e["source"], "b": e["target"], "type": e["primitive"]})
    return out


def make_present_record(ctx, q, kin, slice_name) -> dict:
    gg = ctx["gg"]
    qsrc, qtgt = q["source"], q["target"]
    gold_prim = q["primitive"]
    tgt_gender = q.get("target_gender") or ctx["id2gender"].get(qtgt, "male")
    gold_word = q.get("kinship_relation") or kin.surface(gold_prim, tgt_gender)
    return {
        "doc_id": f"{slice_name}::{ctx['doc_id']}", "title": ctx["doc_id"], "slice": slice_name,
        "story": ctx["text"], "qsrc": qsrc, "qtgt": qtgt,
        "qsrc_name": ctx["id2surface"].get(qsrc, str(qsrc)),
        "qtgt_name": ctx["id2surface"].get(qtgt, str(qtgt)),
        "gold_surface": gold_prim, "gold_surface_word": gold_word, "gold_primitive": gold_prim,
        "is_absent": False, "hop": int(q.get("hop_count", 2)),
        "composed_only": bool(q.get("composed_only", False)),
        "fully_readable": bool(q.get("fully_readable", False)),
        "derivation_path": q.get("derivation_path", []), "noise_type": "natural",
        "genders": ctx["id2gender"], "gold_atomics": _atomics_to_id_edges(gg),
        "gold_atomics_just": _atomics_to_id_edges(gg, justifiable_only=True),
        "_ctx": ctx, "_id2surface": ctx["id2surface"],
    }


def make_absent_record(ctx, p, kin, slice_name) -> dict:
    gg = ctx["gg"]
    qsrc, qtgt = p["source"], p["target"]
    return {
        "doc_id": f"{slice_name}::{ctx['doc_id']}", "title": ctx["doc_id"], "slice": slice_name,
        "story": ctx["text"], "qsrc": qsrc, "qtgt": qtgt,
        "qsrc_name": ctx["id2surface"].get(qsrc, str(qsrc)),
        "qtgt_name": ctx["id2surface"].get(qtgt, str(qtgt)),
        "gold_surface": "no-relation", "gold_surface_word": "no-relation",
        "gold_primitive": "no-relation", "is_absent": True, "hop": 0,
        "composed_only": False, "fully_readable": False, "derivation_path": [],
        "noise_type": "natural", "genders": ctx["id2gender"],
        "gold_atomics": _atomics_to_id_edges(gg),
        "gold_atomics_just": _atomics_to_id_edges(gg, justifiable_only=True),
        "reason": p.get("reason", "different_component"),
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
