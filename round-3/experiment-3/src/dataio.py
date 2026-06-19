#!/usr/bin/env python3
"""Load + parse the SYNTHETIC QCN backbone (gen_art_dataset_2) and prepare it for
REAL-LLM reading.

One ROW = one network. We reconstruct each of the three datasets
(synthetic_qcn_point / _allen / _rcc8) by concatenating same-named datasets across
the two full_data_out parts, then expose, per network:

  * nodes (count), entity_map {idx -> phrase}, gold_edges {(u,v): base_symbol}
    (oriented source->target, source < target),
  * query (s, t, gold_base_symbol)  -- DEDUCTION-REQUIRED (s,t never co-occur),
  * the LOCAL sentence for each gold edge, ENTITY-NORMALIZED to E1/E2 so identical
    (relation x paraphrase x order) reads share one SHA-256 cache slot,
  * the full document (all edge sentences + the Query line) for the full-document
    neural baselines,
  * structure metadata (cyclomatic, num_simple_paths, contributing_edge_count, ...)
    and the dataset's own naive_intersection / singleton_resolved (NAIVE structural
    bite) for cross-checking.

The gold ATOMIC relation on every edge (incl. the query pair) is read off the
realization model, so gold is well-defined and globally consistent BY CONSTRUCTION.
metadata_reference_disjunctive_labels is a SOUND superset per edge -- used ONLY to
sanity-check, NEVER as the read.
"""
from __future__ import annotations

import gc
import json
import re
from pathlib import Path

# ----------------------------------------------------------------------------------
# Algebra base-symbol vocab (dataset symbols -> engine symbols)
# ----------------------------------------------------------------------------------
# POINT: dataset already uses engine symbols '<','=','>'.
POINT_BASE = ["<", "=", ">"]

# ALLEN: dataset uses lowercase (b,bi,m,mi,o,oi,d,di,s,si,f,fi,eq); engine uses uppercase
# with 'E' for equals.
ALLEN_SYM2ENG = {"b": "B", "bi": "BI", "m": "M", "mi": "MI", "o": "O", "oi": "OI",
                 "d": "D", "di": "DI", "s": "S", "si": "SI", "f": "F", "fi": "FI",
                 "eq": "E", "e": "E"}
ALLEN_ENG2SYM = {"B": "b", "BI": "bi", "M": "m", "MI": "mi", "O": "o", "OI": "oi",
                 "D": "d", "DI": "di", "S": "s", "SI": "si", "F": "f", "FI": "fi", "E": "eq"}
ALLEN_BASE_ENG = list(ALLEN_ENG2SYM.keys())

DATASET_NAMES = {"point": "synthetic_qcn_point", "allen": "synthetic_qcn_allen",
                 "rcc8": "synthetic_qcn_rcc8"}


def gold_to_engine(rel: str, algebra: str) -> str:
    """Map a dataset gold relation symbol to the engine base symbol."""
    if algebra == "point":
        return rel
    if algebra == "allen":
        return ALLEN_SYM2ENG[rel.strip().lower()]
    # rcc8 already uppercase tokens (DC,EC,PO,EQ,TPP,NTPP,TPPi,NTPPi)
    return rel


# ----------------------------------------------------------------------------------
# Entity-normalization of a local edge sentence -> E1 (source) / E2 (target)
# ----------------------------------------------------------------------------------
def normalize_sentence(sentence: str, src_phrase: str, tgt_phrase: str) -> str:
    """Replace the source entity phrase with E1 and the target with E2 (case-insensitive,
    all occurrences). Longest phrase first to avoid partial-overlap clobbering."""
    pairs = sorted([(src_phrase, "E1"), (tgt_phrase, "E2")], key=lambda p: -len(p[0]))
    out = sentence
    for phrase, token in pairs:
        out = re.sub(re.escape(phrase), token, out, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", out).strip()


def split_sentences(doc_body: str) -> list[str]:
    """Split a realization body (without the Query line) into sentences. Sentences end
    with '. ' (templates always end with a period)."""
    # keep the period; split on '. ' boundaries
    parts = re.split(r"(?<=\.)\s+", doc_body.strip())
    return [p.strip() for p in parts if p.strip()]


def map_edge_sentences(input_text: str, gold_edges: dict, entity_map: dict) -> dict:
    """Return {(u,v): {raw, normalized}} mapping each gold edge to its local sentence.

    The body (everything before the final 'Query:' line) holds exactly one sentence per
    gold edge. We match the sentence that contains BOTH entity phrases. The query line is
    excluded (the (s,t) pair is never a verbalized edge)."""
    if "\nQuery:" in input_text:
        body = input_text.split("\nQuery:")[0]
    else:
        body = re.split(r"\bQuery:", input_text)[0]
    sents = split_sentences(body)
    out = {}
    used = set()
    for (u, v) in gold_edges:
        pu, pv = entity_map[u], entity_map[v]
        found = None
        for si, s in enumerate(sents):
            if si in used:
                continue
            sl = s.lower()
            if pu.lower() in sl and pv.lower() in sl:
                found = (si, s)
                break
        if found is None:
            # fall back: allow reuse (shouldn't happen for distinct entities)
            for si, s in enumerate(sents):
                sl = s.lower()
                if pu.lower() in sl and pv.lower() in sl:
                    found = (si, s)
                    break
        if found is None:
            continue
        si, s = found
        used.add(si)
        out[(u, v)] = {"raw": s, "normalized": normalize_sentence(s, pu, pv)}
    return out


# ----------------------------------------------------------------------------------
# Row parsing
# ----------------------------------------------------------------------------------
def parse_row(row: dict, algebra: str, net_id: str) -> dict | None:
    """Parse one dataset row into a Network dict. Returns None if it cannot be mapped."""
    out_obj = json.loads(row["output"])
    entity_map = {int(k): v for k, v in row["metadata_entity_map"].items()}
    gold_edges = {}
    for e in out_obj["edges"]:
        u, v = int(e["source"]), int(e["target"])
        if u > v:
            u, v = v, u  # canonicalize; relation oriented for the stored direction
        gold_edges[(int(e["source"]), int(e["target"]))] = gold_to_engine(e["relation"], algebra)
    q = out_obj["query_edge"]
    s, t = int(q["source"]), int(q["target"])
    q_gold = gold_to_engine(q["relation"], algebra)

    struct = row.get("metadata_structure", {}) or {}
    paths = row.get("metadata_paths", {}) or {}
    cell = (row.get("metadata_cell", {}) or {}).get("cell_id", "NA")

    edge_sents = map_edge_sentences(row["input"], gold_edges, entity_map)
    # Every non-query edge must have a local sentence; if some are missing, drop the network
    if len(edge_sents) < len(gold_edges):
        return None

    return {
        "net_id": net_id,
        "algebra": algebra,
        "cell": cell,
        "fold": row.get("metadata_fold", "NA"),
        "seed": int(row.get("metadata_seed", 0)),
        "num_nodes": int(struct.get("num_nodes", len(entity_map))),
        "entity_map": entity_map,
        "gold_edges": gold_edges,             # {(u,v): engine_symbol}  (u may be > v per stored)
        "query": {"s": s, "t": t, "gold": q_gold},
        "edge_sentences": edge_sents,         # {(u,v): {raw, normalized}}
        "full_doc": row["input"],
        "cyclomatic": int(struct.get("cyclomatic_number", 0)),
        "num_simple_paths": int(struct.get("num_simple_paths_s_t", 0)),
        "contributing_edge_count": int(struct.get("contributing_edge_count", len(gold_edges))),
        "avg_degree": float(struct.get("avg_degree", 0.0)),
        "path_list": paths.get("path_list", []),
        "naive_intersection": paths.get("naive_intersection", None),
        "has_bite": bool(paths.get("has_bite", False)),
        "singleton_resolved_gold": bool(paths.get("singleton_resolved", False)),
        "redundancy_P": (row.get("metadata_cell", {}) or {}).get("redundancy_P"),
        "hop_L": (row.get("metadata_cell", {}) or {}).get("hop_count_L"),
        "cyclomatic_target": (row.get("metadata_cell", {}) or {}).get("cyclomatic_target"),
    }


# ----------------------------------------------------------------------------------
# Loading + subsetting
# ----------------------------------------------------------------------------------
def load_networks(ds_dir: Path, algebra: str, cells: list[str], folds: list[str],
                  n_per_cell: int, seed_sort: bool = True, parts=None) -> list[dict]:
    """Reconstruct one dataset across the two full_data_out parts, filter to (cells, folds),
    take a deterministic stratified subsample of <= n_per_cell networks per cell.

    Memory-safe: load one part at a time, keep only matching rows, free the rest."""
    ds_name = DATASET_NAMES[algebra]
    cells_set = set(cells)
    folds_set = set(folds)
    if parts is None:
        parts = [ds_dir / "full_data_out" / "full_data_out_1.json",
                 ds_dir / "full_data_out" / "full_data_out_2.json"]
    raw_rows = []
    for part in parts:
        if not Path(part).exists():
            continue
        blob = json.loads(Path(part).read_text())
        for ds in blob.get("datasets", []):
            if ds.get("dataset") != ds_name:
                continue
            for row in ds["examples"]:
                cell = (row.get("metadata_cell", {}) or {}).get("cell_id", "NA")
                fold = row.get("metadata_fold", "NA")
                if cell in cells_set and fold in folds_set:
                    raw_rows.append(row)
        del blob
        gc.collect()
    # group by cell, deterministic order by seed, take first n_per_cell
    by_cell = {}
    for row in raw_rows:
        cell = (row.get("metadata_cell", {}) or {}).get("cell_id", "NA")
        by_cell.setdefault(cell, []).append(row)
    nets = []
    for cell in cells:
        rows = by_cell.get(cell, [])
        if seed_sort:
            rows = sorted(rows, key=lambda r: int(r.get("metadata_seed", 0)))
        for i, row in enumerate(rows[:n_per_cell]):
            net = parse_row(row, algebra, net_id=f"{algebra}|{cell}|{i}")
            if net is not None:
                nets.append(net)
    return nets


def load_networks_from_file(path: Path, algebra: str, max_n: int = 9999) -> list[dict]:
    """Load networks of one algebra from a single mini/preview file (smoke tests)."""
    ds_name = DATASET_NAMES[algebra]
    blob = json.loads(Path(path).read_text())
    nets = []
    for ds in blob.get("datasets", []):
        if ds.get("dataset") != ds_name:
            continue
        for i, row in enumerate(ds["examples"][:max_n]):
            net = parse_row(row, algebra, net_id=f"{algebra}|mini|{i}")
            if net is not None:
                nets.append(net)
    return nets


# ----------------------------------------------------------------------------------
# Native-vocab relation parsing (the LLM's local read)
# ----------------------------------------------------------------------------------
_POINT_WORD2SYM = {
    "<": "<", ">": ">", "=": "=", "==": "=",
    "before": "<", "earlier": "<", "precedes": "<", "preceding": "<", "prior": "<",
    "after": ">", "later": ">", "follows": ">", "following": ">", "succeeds": ">",
    "simultaneous": "=", "simultaneously": "=", "same": "=", "equal": "=", "equals": "=",
    "coincide": "=", "coincides": "=", "concurrent": "=", "same_time": "=",
}
_ALLEN_WORD2SYM = {
    # symbol forms
    "b": "B", "bi": "BI", "m": "M", "mi": "MI", "o": "O", "oi": "OI", "d": "D", "di": "DI",
    "s": "S", "si": "SI", "f": "F", "fi": "FI", "eq": "E", "e": "E", "=": "E",
    # word forms
    "before": "B", "after": "BI", "meets": "M", "met-by": "MI", "met_by": "MI",
    "metby": "MI", "overlaps": "O", "overlapped-by": "OI", "overlapped_by": "OI",
    "overlappedby": "OI", "during": "D", "contains": "DI", "starts": "S",
    "started-by": "SI", "started_by": "SI", "startedby": "SI", "finishes": "F",
    "finished-by": "FI", "finished_by": "FI", "finishedby": "FI", "equals": "E",
    "equal": "E", "simultaneous": "E", "same": "E",
}
_RCC8_WORD2SYM = {w.lower(): w for w in ["DC", "EC", "PO", "EQ", "TPP", "NTPP", "TPPi", "NTPPi"]}
_RCC8_WORD2SYM.update({"disconnected": "DC", "externally-connected": "EC",
                       "partial-overlap": "PO", "equal": "EQ", "tangential-proper-part": "TPP",
                       "non-tangential-proper-part": "NTPP"})

_UNDET = {"underdetermined", "undetermined", "vague", "unknown", "universal", "none",
          "any", "indeterminate", "all", "unclear", "ambiguous", "uncertain"}


def _word_map(algebra):
    return {"point": _POINT_WORD2SYM, "allen": _ALLEN_WORD2SYM, "rcc8": _RCC8_WORD2SYM}[algebra]


def _first_json_block(txt: str):
    start = txt.find("{")
    if start < 0:
        return None
    depth = 0
    for i in range(start, len(txt)):
        if txt[i] == "{":
            depth += 1
        elif txt[i] == "}":
            depth -= 1
            if depth == 0:
                return txt[start:i + 1]
    return None


def parse_native(content: str, algebra: str):
    """Parse an LLM read into (frozenset(engine base symbols), underdetermined, parse_fail).

    Accepts {"relations":[...], "underdetermined":bool} OR a single relation string. Maps
    symbol/word synonyms to the engine base. Empty/underdetermined -> universe."""
    wmap = _word_map(algebra)
    base = set(wmap.values())
    if not content or not content.strip():
        return frozenset(base), True, True
    txt = content.strip()
    txt = re.sub(r"^```(?:json)?|```$", "", txt, flags=re.M).strip()
    obj = None
    for cand in (txt, _first_json_block(txt)):
        if cand is None:
            continue
        try:
            obj = json.loads(cand)
            break
        except Exception:
            continue
    tokens, underdet = [], False
    if isinstance(obj, dict):
        underdet = bool(obj.get("underdetermined", False))
        rels = obj.get("relations", obj.get("relation", []))
        tokens = _flatten_tokens(rels)
    elif isinstance(obj, list):
        tokens = _flatten_tokens(obj)
    else:
        # regex fallback: scan for known tokens/words
        low = txt.lower()
        for w in list(wmap) + list(_UNDET):
            if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low):
                tokens.append(w)
        if not tokens:
            return frozenset(base), True, True

    syms = []
    for tk in tokens:
        tl = str(tk).strip().lower()
        if tl in _UNDET:
            underdet = True
            continue
        sym = wmap.get(tl) or wmap.get(tl.replace(" ", "_")) or wmap.get(tl.replace(" ", "-"))
        if sym:
            syms.append(sym)
    syms = list(dict.fromkeys(syms))
    if underdet and not syms:
        return frozenset(base), True, False
    if not syms:
        return frozenset(base), True, True  # parsed but no relation tokens -> universe
    return frozenset(syms), (len(syms) == len(base)), False


def _flatten_tokens(rels):
    out = []
    if isinstance(rels, str):
        return [rels]
    if isinstance(rels, list):
        for r in rels:
            if isinstance(r, str):
                out.append(r)
            elif isinstance(r, dict):
                for k in ("relation", "rel", "label", "type", "value"):
                    if k in r:
                        out.append(r[k]); break
    elif isinstance(rels, dict):
        for k in ("relation", "rel", "label", "type", "value"):
            if k in rels:
                out.append(rels[k])
    return out
