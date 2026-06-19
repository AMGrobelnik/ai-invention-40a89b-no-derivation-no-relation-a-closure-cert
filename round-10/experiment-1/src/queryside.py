#!/usr/bin/env python3
"""The NEW iter-8 baselines the closure certificate must MATCH or BEAT: a QUERY-SIDE
false-premise verifier and a SELF-VERIFICATION pass.

These are the ESTABLISHED method for the absent-relation failure mode (research dossier
art_dA_3iFe_7fn_: FalseQA / AbstentionBench / Wen2024): rather than reasoning structurally,
ask the model directly whether the presupposed relation exists at all, and gate the committed
answer on that. If a trained/prompted false-premise detector already catches confident
absent-relation hallucinations, the structural certificate is not NEEDED for the absent
stratum (the VERIFIER-SUFFICES fork). If it does NOT, the certificate's structural abstention
is the load-bearing fix.

Both produce {surface, conf, named} method dicts identical in shape to ct_<signal>, so they
plug straight into matched_coverage_showdown / cw_matched_to_ref / the Holm family and are
primitivized like every other method.
"""
from __future__ import annotations

import asyncio
import re

from loguru import logger

import readers_locatedin as R


# --------------------------------------------------------------------------- #
# (1) QUERY-SIDE FALSE-PREMISE VERIFIER ('are these places related at all?')
# --------------------------------------------------------------------------- #
_VERIFIER_SYSTEM = (
    "You decide whether a presupposed geographic containment relation EXISTS between two named "
    'places, based ONLY on the document. Output ONLY a JSON object {"related": true|false, '
    '"confidence": <0..1>}. related=true if, according to the document, one place is located in / '
    "part of the other OR one place contains the other (containment in EITHER direction). "
    "related=false if neither place is inside the other. confidence is your probability that your "
    "related judgement is correct."
)


def verifier_item(story: str, xname: str, yname: str, story_id: str, tag: str = "verifier") -> dict:
    user = (f"Document:\n{story}\n\nBased ONLY on the document, is {xname} located in {yname}, OR "
            f"does {xname} contain {yname} (i.e. is there ANY containment between them in either "
            f"direction)? Answer with the JSON object.")
    return {"id": f"{tag}::{story_id}::{xname}->{yname}", "system": _VERIFIER_SYSTEM, "user": user,
            "max_tokens": 30, "temperature": 0.0, "tag": tag}


def parse_verifier(content: str) -> dict:
    """Return {related:bool, conf:float}."""
    obj = R._load_json(content)
    related, conf = None, None
    if isinstance(obj, dict):
        for k in ("related", "is_related", "exists", "containment"):
            if k in obj:
                related = _to_bool(obj[k]); break
        c = obj.get("confidence", obj.get("conf"))
        try:
            conf = float(c)
        except (TypeError, ValueError):
            conf = None
    if related is None:
        low = (content or "").lower()
        if re.search(r"\bfalse\b|\bno\b|not related|unrelated", low):
            related = False
        elif re.search(r"\btrue\b|\byes\b|related", low):
            related = True
        else:
            related = False
    if conf is None:
        m = re.search(r"(\d*\.\d+|\d+)", content or "")
        conf = float(m.group(1)) if m else 0.5
        if conf > 1.0:
            conf = min(1.0, conf / 100.0)
    conf = max(0.0, min(1.0, conf))
    return {"related": bool(related), "conf": conf}


# --------------------------------------------------------------------------- #
# (2) SELF-VERIFICATION pass on the raw committed answer
# --------------------------------------------------------------------------- #
_SELFVERIFY_SYSTEM = (
    "You judge whether a PROPOSED answer to a geographic-containment question is correct, based "
    'ONLY on the document. Output ONLY a JSON object {"correct": true|false, "confidence": <0..1>}. '
    "Be calibrated: answer correct=false when the two places have no containment relation in the "
    "document or when the proposed relation/direction is wrong."
)


def selfverify_item(story: str, xname: str, yname: str, proposed: str, story_id: str,
                    tag: str = "selfverify") -> dict:
    user = (f"Document:\n{story}\n\nQuestion: What is the geographic relationship of {xname} to "
            f"{yname}?\nProposed answer: \"{proposed}\".\nIs this proposed answer correct given the "
            f"document? Answer with the JSON object.")
    return {"id": f"{tag}::{story_id}::{xname}->{yname}", "system": _SELFVERIFY_SYSTEM, "user": user,
            "max_tokens": 30, "temperature": 0.0, "tag": tag}


def parse_selfverify(content: str) -> dict:
    """Return {correct:bool, conf:float}."""
    obj = R._load_json(content)
    correct, conf = None, None
    if isinstance(obj, dict):
        for k in ("correct", "is_correct", "valid"):
            if k in obj:
                correct = _to_bool(obj[k]); break
        c = obj.get("confidence", obj.get("conf"))
        try:
            conf = float(c)
        except (TypeError, ValueError):
            conf = None
    if correct is None:
        low = (content or "").lower()
        if re.search(r"\bfalse\b|incorrect|\bno\b|wrong", low):
            correct = False
        elif re.search(r"\btrue\b|correct|\byes\b", low):
            correct = True
        else:
            correct = False
    if conf is None:
        m = re.search(r"(\d*\.\d+|\d+)", content or "")
        conf = float(m.group(1)) if m else 0.5
        if conf > 1.0:
            conf = min(1.0, conf / 100.0)
    conf = max(0.0, min(1.0, conf))
    return {"correct": bool(correct), "conf": conf}


def _to_bool(v):
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return v != 0
    s = str(v).strip().lower()
    return s in ("true", "yes", "1", "y", "t", "related", "correct", "valid")


# --------------------------------------------------------------------------- #
# Batch driver + method-dict builder
# --------------------------------------------------------------------------- #
def run_queryside(records, client, tag_prefix: str = "", reader_tag: str = "primary"):
    """Issue the verifier + self-verify call per query (both temp 0); attach r['_verifier'] and
    r['_selfverify']. Must run AFTER r['raw'] exists (self-verify needs the raw proposal).
    Cached calls replay at $0."""
    v_items, s_items = [], []
    for r in records:
        sid, story = r["doc_id"], r["story"]
        xn, yn = r["qsrc_name"], r["qtgt_name"]
        v_items.append(verifier_item(story, xn, yn, sid, tag=f"{tag_prefix}verifier"))
        proposed = (r["raw"]["surface_word"] if r["raw"].get("surface_word")
                    else (r["raw"]["surface"] if (r["raw"]["named"] and r["raw"]["surface"]) else "no-relation"))
        r["_sv_proposed"] = proposed
        s_items.append(selfverify_item(story, xn, yn, proposed, sid, tag=f"{tag_prefix}selfverify"))
    logger.info(f"[{reader_tag}] query-side items: verifier={len(v_items)} selfverify={len(s_items)}")
    v_results = asyncio.run(client.run_batch(v_items))
    logger.info(f"[{reader_tag}] verifier done | cost=${client.cost:.4f} calls={client.n_calls} cache={client.n_cache_hits}")
    s_results = asyncio.run(client.run_batch(s_items))
    logger.info(f"[{reader_tag}] selfverify done | cost=${client.cost:.4f} calls={client.n_calls} cache={client.n_cache_hits}")
    for r in records:
        sid, xn, yn = r["doc_id"], r["qsrc_name"], r["qtgt_name"]
        base = f"::{sid}::{xn}->{yn}"
        vr = v_results.get(f"{tag_prefix}verifier{base}")
        r["_verifier"] = parse_verifier(vr["content"]) if vr and vr.get("content") else {"related": True, "conf": 0.5}
        sr = s_results.get(f"{tag_prefix}selfverify{base}")
        r["_selfverify"] = parse_selfverify(sr["content"]) if sr and sr.get("content") else {"correct": True, "conf": 0.5}


def build_queryside_method_dicts(records):
    """Build r['queryside_verifier'] and r['queryside_selfverify'] from the raw committed answer
    gated by the verifier / self-verify. Surfaces are the raw committed WORD (primitivized later).

    queryside_verifier: the verifier GATES the committed answer -- related=True commits raw's
      answer at the verifier's confidence; related=False ABSTAINS.
    queryside_selfverify: keep raw's answer only if self-verify says correct=True; conf = the
      self-verify confidence (used for matched-coverage thresholding)."""
    for r in records:
        raw_word = r["raw"].get("surface_word") or r["raw"].get("surface")
        raw_named = bool(r["raw"]["named"]) and raw_word is not None
        ver = r.get("_verifier", {"related": True, "conf": 0.5})
        sv = r.get("_selfverify", {"correct": True, "conf": 0.5})
        # verifier gate
        v_named = bool(ver["related"]) and raw_named
        r["queryside_verifier"] = {
            "surface": raw_word if v_named else None,
            "conf": float(ver["conf"]) if v_named else float(1.0 - ver["conf"]),
            "named": v_named}
        # self-verify gate
        s_named = raw_named and bool(sv["correct"])
        r["queryside_selfverify"] = {
            "surface": raw_word if s_named else None,
            "conf": float(sv["conf"]),
            "named": s_named}


def cached_queryside_fallback(records):
    """--no-queryside / --no-battery smoke: degenerate query-side dicts from cached raw only
    (no new calls). The verifier defaults to 'related == raw committed' (a trivial gate)."""
    for r in records:
        r.setdefault("_verifier", {"related": bool(r["raw"]["named"]), "conf": float(r["raw"]["conf"])})
        r.setdefault("_selfverify", {"correct": bool(r["raw"]["named"]), "conf": float(r["raw"]["conf"])})
    build_queryside_method_dicts(records)
