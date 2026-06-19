#!/usr/bin/env python3
"""iter-9 EXTRACTION-RECALL BOOSTER.

The iter-8 verdict was EXTRACTION-LIMITED-BOUNDARY: the closure engine is sound (gold-read
ceiling 1.0/1.0/1.0) but natural-prose atomic extraction recall (~0.15 located-in / ~0.38
kinship) caps the LLM-read certificate's present coverage at ~0.05, so the mixed-pool
matched-coverage confident-wrong REDUCTION is degenerate. This module sweeps >=4 prompt
strategies that try to RAISE atomic recall above that floor, with a PRECISION GUARD, so the
certificate can be RE-computed per strategy while the 6 confident-wrong competitors stay FIXED.

Each strategy returns grounded entity-id edges {doc_id:[{a,b,type,surface}]}, exactly the shape
core.replay_reads produces for its default arm, so downstream certificate recompute is a drop-in.
The two iter-8 arms (default / best-effort) are NOT re-issued here -- the caller passes their
already-grounded dicts as S0/S1; this module implements the NEW strategies S2-S5 only, so every
call it issues is genuinely new spend (cached re-runs replay $0).

Strategies (all REUSE the domain reader's parse_extraction + the domain loader's ground_name):
  S2 'fewshot_enum'     : few-shot + place/person inventory + explicit NO-OMISSION, larger
                          max_tokens (defeats 700-token truncation on dense docs). 1 call/doc.
  S3 'sentencewise'     : walk the document sentence-by-sentence, resolve coref/aliases to the
                          inventory, emit one flat relations list. 1 call/doc, max_tokens 1500.
  S4 'sc_union'         : self-consistency UNION over k samples of the S2 prompt at temp 0.7 ->
                          harvests edges any single sample omits; PRECISION GUARD applied.
  S5 'multimodel_union' : S2 prompt on a SECOND-family model UNIONed with S2(primary); GUARD.

PRECISION GUARD (union strategies): canonicalise each edge converse-invariantly, dedupe, count
per-edge source AGREEMENT, drop directed 2-cycles (keep the higher-agreement direction), and KEEP
an edge iff agreement>=min_agreement OR it is CUE-SUPPORTED (a containment / kinship cue phrase
co-occurs with BOTH endpoint mentions inside a sentence window). Ungroundable names become
isolated NAME:: nodes (honest recall penalty, never a fabricated link).
"""
from __future__ import annotations

import asyncio
import re
from collections import defaultdict

from loguru import logger

# --------------------------------------------------------------------------- #
# Prompt fragments (domain-agnostic; the domain VOCAB lives in R._EXTRACT_SYSTEM)
# --------------------------------------------------------------------------- #
_NO_OMISSION = (
    "\n\nIMPORTANT: list EVERY directly-stated relation between two NAMED entities, including ones "
    "mentioned only in passing, in subordinate clauses, appositives, or parentheticals. Do NOT infer "
    "transitive or composed relations. Do NOT skip any directly-stated relation. Be exhaustive: a "
    "missed relation is worse than an extra one."
)
_SENTENCEWISE = (
    "\n\nWork through the document SENTENCE BY SENTENCE. For EACH sentence that states a relation "
    "between two named entities, FIRST resolve any pronouns, surnames, partial names, or aliases to "
    "the canonical names in the provided inventory, THEN record the relation. Aggregate every "
    'sentence\'s relations into ONE final JSON object {"relations": [{"a":...,"relation":...,"b":...}, '
    "...]} (a single flat list covering the whole document). Do NOT infer transitive relations; only "
    "report relations a sentence states directly."
)


def _inventory(ctx: dict) -> list[str]:
    return sorted({s for s in ctx["id2surface"].values() if s})


def _user_enum(story: str, inv: list[str]) -> str:
    inv_s = ", ".join(inv)
    return (f"Document:\n{story}\n\nThe named entities in this document are: {inv_s}.\n"
            "Return the JSON object listing EVERY directly-stated relation between these entities "
            "(use the names exactly as listed). Be exhaustive.")


def _user_sentencewise(story: str, inv: list[str]) -> str:
    inv_s = ", ".join(inv)
    return (f"Document:\n{story}\n\nThe named entities in this document are: {inv_s}.\n"
            "Walk through the document sentence by sentence, resolving pronouns/aliases to these "
            "canonical names, and return ONE flat JSON object of every directly-stated relation.")


# --------------------------------------------------------------------------- #
# Cue-support check (deterministic; reuses the domain's surface-cue vocabulary)
# --------------------------------------------------------------------------- #
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def cue_words_for(R) -> list[str]:
    """Lower-cased cue phrases for the domain, longest-first, from the reader's synonym map +
    canonical surfaces (located-in: 'located in'/'contains' synonyms; kinship: kinship words)."""
    words = set()
    syn = getattr(R, "_SURF_SYN", {})
    for k in syn:
        words.add(str(k).lower())
    for s in getattr(R, "CANON_SURFACES", []):
        words.add(str(s).lower())
    # keep only multi-useful tokens (>=2 chars) to avoid spurious matches on 'in','a'
    return sorted((w for w in words if len(w) >= 3), key=len, reverse=True)


def cue_supported(text: str, name_a: str, name_b: str, cue_words, window: int = 2) -> bool:
    """True iff a sentence window contains BOTH endpoint mentions AND a domain cue phrase."""
    la, lb = str(name_a).lower().strip(), str(name_b).lower().strip()
    if not la or not lb:
        return False
    sents = [s.lower() for s in _SENT_SPLIT.split(text or "")]
    for i in range(len(sents)):
        win = " ".join(sents[i:i + window])
        if la in win and lb in win and any(c in win for c in cue_words):
            return True
    return False


# --------------------------------------------------------------------------- #
# Converse-invariant id canonicalisation
# --------------------------------------------------------------------------- #
def canon_id(kin, a, b, t):
    a_, b_ = str(a), str(b)
    if a_ == b_:
        return None
    if a_ <= b_:
        return (a_, t, b_)
    return (b_, kin.conv_type(t), a_)


# --------------------------------------------------------------------------- #
# Item builders
# --------------------------------------------------------------------------- #
def _items_for(records, contexts, system: str, user_fn, max_tokens: int, temperature: float,
               tag: str):
    docs = {}
    for r in records:
        docs.setdefault(r["doc_id"], r)
    items, ids = [], {}
    for did, r in docs.items():
        ctx = contexts[did]
        inv = _inventory(ctx)
        it = {"id": f"{tag}::{did}", "system": system, "user": user_fn(r["story"], inv),
              "max_tokens": max_tokens, "temperature": temperature, "tag": tag}
        ids[did] = it["id"]
        items.append(it)
    return docs, items, ids


def _ground_edge(e, ctx, D):
    return {"a": D.ground_name(e["a"], ctx), "b": D.ground_name(e["b"], ctx),
            "type": e["type"], "surface": e.get("surface"),
            "name_a": e["a"], "name_b": e["b"]}


# --------------------------------------------------------------------------- #
# S2 / S3 -- single-call strategies (light guard: drop true 2-cycles only)
# --------------------------------------------------------------------------- #
def _light_guard(parsed_edges, ctx, kin, D):
    """Ground edges; drop directed 2-cycles on the same unordered pair (keep first seen,
    deterministic by canon key); dedupe converse-invariantly. Solo edges are KEPT (single
    source has no agreement signal -- single-call strategies are precision-safe by prompt)."""
    by_pair = defaultdict(dict)  # frozenset(ids) -> {canonkey: grounded_edge}
    for e in parsed_edges:
        g = _ground_edge(e, ctx, D)
        ck = canon_id(kin, g["a"], g["b"], g["type"])
        if ck is None:
            continue
        pr = frozenset((str(g["a"]), str(g["b"])))
        by_pair[pr].setdefault(ck, g)
    out = []
    for pr, cks in by_pair.items():
        if len(cks) >= 2:
            # contradictory directions on one pair -> keep the deterministic first canon key
            ck0 = sorted(cks)[0]
            out.append(cks[ck0])
        else:
            out.extend(cks.values())
    return out


def strategy_single(records, kin, client, contexts, D, R, *, tag, system, user_fn,
                    max_tokens, temperature=0.0, reader_tag="primary"):
    docs, items, ids = _items_for(records, contexts, system, user_fn, max_tokens, temperature, tag)
    logger.info(f"[{reader_tag}] booster {tag}: {len(items)} doc-calls (max_tokens={max_tokens})")
    results = asyncio.run(client.run_batch(items))
    grounded = {}
    for did in docs:
        ctx = contexts[did]
        content = (results.get(ids[did]) or {}).get("content", "")
        parsed = R.parse_extraction(content, kin)
        grounded[did] = _light_guard(parsed["edges"], ctx, kin, D)
    return grounded


def _best_system(R):
    """Few-shot extraction system prompt; falls back to the plain extraction system for readers
    (kinship) that do not define a best-effort few-shot variant."""
    return getattr(R, "_EXTRACT_BEST_SYSTEM", R._EXTRACT_SYSTEM)


def strategy_s2(records, kin, client, contexts, D, R, **kw):
    return strategy_single(records, kin, client, contexts, D, R, tag="s2_fewshot_enum",
                           system=_best_system(R) + _NO_OMISSION, user_fn=_user_enum,
                           max_tokens=1200, **kw)


def strategy_s3(records, kin, client, contexts, D, R, **kw):
    return strategy_single(records, kin, client, contexts, D, R, tag="s3_sentencewise",
                           system=R._EXTRACT_SYSTEM + _SENTENCEWISE, user_fn=_user_sentencewise,
                           max_tokens=1500, **kw)


# --------------------------------------------------------------------------- #
# S4 / S5 -- multi-source UNION strategies (full precision guard)
# --------------------------------------------------------------------------- #
def _collect_source(records, contexts, client, kin, R, *, system, user_fn, max_tokens,
                    temperature, tag):
    docs, items, ids = _items_for(records, contexts, system, user_fn, max_tokens, temperature, tag)
    results = asyncio.run(client.run_batch(items))
    per_doc = {}
    for did in docs:
        content = (results.get(ids[did]) or {}).get("content", "")
        per_doc[did] = R.parse_extraction(content, kin)["edges"]
    return docs, per_doc


def _union_guard(sources_per_doc, contexts, kin, D, R, *, min_agreement, require_cue,
                 doc_ids):
    """sources_per_doc: list over sources of {doc_id:[parsed NAME-edges]}.
    Returns grounded {doc_id:[edges]} after agreement counting + 2-cycle drop + keep rule."""
    cue_words = cue_words_for(R)
    grounded = {}
    n_solo_cue_kept = n_dropped_lowagree = n_2cycle = 0
    for did in doc_ids:
        ctx = contexts[did]
        text = ctx["text"]
        agree = {}  # canonkey -> info
        for sd in sources_per_doc:
            seen_src = set()
            for e in sd.get(did, []):
                ida = D.ground_name(e["a"], ctx)
                idb = D.ground_name(e["b"], ctx)
                ck = canon_id(kin, ida, idb, e["type"])
                if ck is None or ck in seen_src:
                    continue
                seen_src.add(ck)
                info = agree.get(ck)
                if info is None:
                    agree[ck] = {"a": ida, "b": idb, "type": e["type"], "surface": e.get("surface"),
                                 "name_a": e["a"], "name_b": e["b"], "count": 1}
                else:
                    info["count"] += 1
        # group by unordered pair to detect directed 2-cycles
        pairs = defaultdict(list)
        for ck, info in agree.items():
            pairs[frozenset((str(info["a"]), str(info["b"])))].append(ck)
        keep = []
        for pr, cks in pairs.items():
            if len(cks) >= 2:
                n_2cycle += 1
                cks = [max(cks, key=lambda c: agree[c]["count"])]  # higher-agreement direction
            for ck in cks:
                info = agree[ck]
                disp_a = _disp_name(ctx, info["a"], info["name_a"])
                disp_b = _disp_name(ctx, info["b"], info["name_b"])
                cue = cue_supported(text, disp_a, disp_b, cue_words)
                if require_cue:
                    ok = info["count"] >= min_agreement and cue
                else:
                    ok = info["count"] >= min_agreement or cue
                if ok:
                    if info["count"] < min_agreement and cue:
                        n_solo_cue_kept += 1
                    keep.append({"a": info["a"], "b": info["b"], "type": info["type"],
                                 "surface": info["surface"]})
                else:
                    n_dropped_lowagree += 1
        grounded[did] = keep
    stats = {"n_solo_cue_kept": n_solo_cue_kept, "n_dropped_low_agreement": n_dropped_lowagree,
             "n_2cycles_resolved": n_2cycle}
    return grounded, stats


def _disp_name(ctx, eid, raw_name):
    """Display surface for cue-support: the grounded entity's canonical surface (so we check the
    text mention) when grounded, else the raw extracted name."""
    s = ctx["id2surface"].get(eid)
    return s if s else raw_name


def strategy_s4(records, kin, client, contexts, D, R, *, k=4, temperature=0.7,
                min_agreement=2, require_cue=False, reader_tag="primary"):
    """Self-consistency UNION: k temp-0.7 samples of the S2 prompt, agreement-guarded."""
    system = _best_system(R) + _NO_OMISSION
    docs = {r["doc_id"]: r for r in records}
    doc_ids = list(docs)
    logger.info(f"[{reader_tag}] booster s4_sc_union: {len(doc_ids)} docs x k={k} samples")
    sources = []
    for s in range(k):
        _d, per_doc = _collect_source(records, contexts, client, kin, R, system=system,
                                      user_fn=_user_enum, max_tokens=1200, temperature=temperature,
                                      tag=f"s4_sc_union{s}")
        sources.append(per_doc)
    grounded, stats = _union_guard(sources, contexts, kin, D, R, min_agreement=min_agreement,
                                   require_cue=require_cue, doc_ids=doc_ids)
    logger.info(f"[{reader_tag}] s4 guard: {stats}")
    return grounded, stats


def strategy_s5(records, kin, client_primary, client_second, contexts, D, R, *,
                second_model="(2nd)", min_agreement=2, require_cue=False, reader_tag="primary"):
    """Multi-model UNION: S2(primary) UNION S2(second-family model), agreement-guarded."""
    system = _best_system(R) + _NO_OMISSION
    docs = {r["doc_id"]: r for r in records}
    doc_ids = list(docs)
    logger.info(f"[{reader_tag}] booster s5_multimodel_union: {len(doc_ids)} docs x 2 models "
                f"(2nd={second_model})")
    _d1, per_doc_p = _collect_source(records, contexts, client_primary, kin, R, system=system,
                                     user_fn=_user_enum, max_tokens=1200, temperature=0.0,
                                     tag="s5_primary")
    _d2, per_doc_m = _collect_source(records, contexts, client_second, kin, R, system=system,
                                     user_fn=_user_enum, max_tokens=1200, temperature=0.0,
                                     tag="s5_second")
    grounded, stats = _union_guard([per_doc_p, per_doc_m], contexts, kin, D, R,
                                   min_agreement=min_agreement, require_cue=require_cue,
                                   doc_ids=doc_ids)
    logger.info(f"[{reader_tag}] s5 guard: {stats}")
    return grounded, stats
