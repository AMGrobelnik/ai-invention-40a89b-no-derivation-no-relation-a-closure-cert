#!/usr/bin/env python3
"""KINSHIP twin of queryside.py: the query-side false-premise VERIFIER + SELF-VERIFICATION
baselines over the family-relationship vocabulary (for the iter-9 kinship-domain replication).

Identical structure / parse / gate logic to queryside.py; only the domain wording changes
('is there ANY family relationship between X and Y?'). Produces r['queryside_verifier'] /
r['queryside_selfverify'] method dicts in the same shape so the shared core views score them
like every other competitor.
"""
from __future__ import annotations

import asyncio

from loguru import logger

import readers_kinship as R
from queryside import _to_bool, parse_selfverify, parse_verifier  # parsers are vocab-agnostic


_VERIFIER_SYSTEM = (
    "You decide whether a presupposed FAMILY relationship EXISTS between two named people, based "
    'ONLY on the story. Output ONLY a JSON object {"related": true|false, "confidence": <0..1>}. '
    "related=true if, according to the story, the two people are connected by ANY family relationship "
    "(direct or through other relatives). related=false if they have no family relationship. "
    "confidence is your probability that your related judgement is correct."
)


def verifier_item(story: str, xname: str, yname: str, story_id: str, tag: str = "verifier") -> dict:
    user = (f"Story:\n{story}\n\nBased ONLY on the story, are {xname} and {yname} related by ANY "
            f"family relationship (direct or through other relatives)? Answer with the JSON object.")
    return {"id": f"{tag}::{story_id}::{xname}->{yname}", "system": _VERIFIER_SYSTEM, "user": user,
            "max_tokens": 30, "temperature": 0.0, "tag": tag}


_SELFVERIFY_SYSTEM = (
    "You judge whether a PROPOSED answer to a kinship question is correct, based ONLY on the story. "
    'Output ONLY a JSON object {"correct": true|false, "confidence": <0..1>}. Be calibrated: answer '
    "correct=false when the two people have no family relationship in the story or when the proposed "
    "relation is wrong."
)


def selfverify_item(story: str, xname: str, yname: str, proposed: str, story_id: str,
                    tag: str = "selfverify") -> dict:
    user = (f"Story:\n{story}\n\nQuestion: What is {yname} to {xname}?\nProposed answer: "
            f"\"{proposed}\".\nIs this proposed answer correct given the story? Answer with the JSON object.")
    return {"id": f"{tag}::{story_id}::{xname}->{yname}", "system": _SELFVERIFY_SYSTEM, "user": user,
            "max_tokens": 30, "temperature": 0.0, "tag": tag}


def run_queryside(records, client, tag_prefix: str = "", reader_tag: str = "primary"):
    """Issue the verifier + self-verify call per query (both temp 0); attach r['_verifier'] and
    r['_selfverify']. Runs AFTER r['raw'] exists. Cached calls replay $0."""
    v_items, s_items = [], []
    for r in records:
        sid, story = r["doc_id"], r["story"]
        xn, yn = r["qsrc_name"], r["qtgt_name"]
        v_items.append(verifier_item(story, xn, yn, sid, tag=f"{tag_prefix}kverifier"))
        proposed = (r["raw"].get("surface_word") if r["raw"].get("surface_word")
                    else (r["raw"]["surface"] if (r["raw"]["named"] and r["raw"]["surface"]) else "no-relation"))
        r["_sv_proposed"] = proposed
        s_items.append(selfverify_item(story, xn, yn, proposed, sid, tag=f"{tag_prefix}kselfverify"))
    logger.info(f"[{reader_tag}] kinship query-side items: verifier={len(v_items)} selfverify={len(s_items)}")
    v_results = asyncio.run(client.run_batch(v_items))
    s_results = asyncio.run(client.run_batch(s_items))
    for r in records:
        sid, xn, yn = r["doc_id"], r["qsrc_name"], r["qtgt_name"]
        base = f"::{sid}::{xn}->{yn}"
        vr = v_results.get(f"{tag_prefix}kverifier{base}")
        r["_verifier"] = parse_verifier(vr["content"]) if vr and vr.get("content") else {"related": True, "conf": 0.5}
        sr = s_results.get(f"{tag_prefix}kselfverify{base}")
        r["_selfverify"] = parse_selfverify(sr["content"]) if sr and sr.get("content") else {"correct": True, "conf": 0.5}


def build_queryside_method_dicts(records):
    """Build r['queryside_verifier'] / r['queryside_selfverify'] from the raw committed answer
    gated by the verifier / self-verify (identical to queryside.build_queryside_method_dicts)."""
    for r in records:
        raw_word = r["raw"].get("surface_word") or r["raw"].get("surface")
        raw_named = bool(r["raw"]["named"]) and raw_word is not None
        ver = r.get("_verifier", {"related": True, "conf": 0.5})
        sv = r.get("_selfverify", {"correct": True, "conf": 0.5})
        v_named = bool(ver["related"]) and raw_named
        r["queryside_verifier"] = {"surface": raw_word if v_named else None,
                                   "conf": float(ver["conf"]) if v_named else float(1.0 - ver["conf"]),
                                   "named": v_named}
        s_named = raw_named and bool(sv["correct"])
        r["queryside_selfverify"] = {"surface": raw_word if s_named else None,
                                     "conf": float(sv["conf"]), "named": s_named}
