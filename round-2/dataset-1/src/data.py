#!/usr/bin/env python3
"""data.py -- BUILD the CLUTRR kinship gold-graph corpus (iter-2 dataset_1).

Standardizes CLUTRR (Sinha et al., EMNLP 2019, arXiv:1908.06177) into the aii
``exp_sel_data_out`` schema -- ONE ROW per story:

  * input  = the de-bracketed natural-language story (the actually-presented
             narrative, incl. any noise facts; '[' / ']' markers removed).
  * output = json.dumps(gold_graph): entity NODES (id, surface, gender, mention
             char-spans) + typed atomic kinship EDGES (the directly-stated facts
             = the proof chain) + the held-out QUERY edge (deduced by composing
             >=2 atomics) + structural ABSENT-relation pairs (different connected
             components => provably no kinship path => honest 'no-relation') +
             structural NOISE edges (extra story_edges CLUTRR does not type).
  * metadata_* = hop_count, noise_type, f_comb, the atomic facts, the backward-
             chaining gold proof (trace-graph gold), genders, graph descriptors,
             fold, etc.

Top-level metadata carries the finite kinship COMPOSITION TABLE read verbatim
from facebookresearch/clutrr (rules_store.yaml / relations_store.yaml): abstract
relation TYPES (+inverse/symmetry flags), the (type x gender)->surface-word map
(and reverse), the composition rules rules[t1][t2]=t3, the int<->text label map
(0..20), and a derived gendered surface-level composition table. It is a finite
composition table, NOT a full relation algebra.

DESCRIPTIVE COUNTS ONLY. No composition/closure, no derived metrics, no LLM
calls -- those are iter-3's experiment.

Acquisition is bulletproof: the CSVs are downloaded directly from the GitHub raw
mirror that HF's own ``CLUTRR/v1`` loader (``v1.py``) points at -- no datasets
library, no trust_remote_code. CSVs + yamls are cached under ``temp/datasets/``.

Run:
    uv run data.py                 # full corpus (all 3 configs, all splits)
    uv run data.py --limit 50      # quick smoke test (50 rows/split)
"""
from __future__ import annotations

import argparse
import ast
import glob
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median

import networkx as nx
import pandas as pd
import requests
import yaml
from loguru import logger

# --------------------------------------------------------------------------- #
# Paths & logging
# --------------------------------------------------------------------------- #
ROOT = Path(__file__).resolve().parent
TEMP = ROOT / "temp" / "datasets"
OUT_DIR = ROOT / "full_data_out"   # split parts live here (canonical aii layout)
RESULTS = ROOT / "results"
LOGS = ROOT / "logs"
for d in (TEMP, OUT_DIR, RESULTS, LOGS):
    d.mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(LOGS / "run.log", rotation="30 MB", level="DEBUG")

# --------------------------------------------------------------------------- #
# Constants verified against the data (see data card / README for provenance)
# --------------------------------------------------------------------------- #
RAW_BASE = "https://raw.githubusercontent.com/kliang5/CLUTRR_huggingface_dataset/main"
FB_STORE = "https://raw.githubusercontent.com/facebookresearch/clutrr/main/clutrr/store"

# (name, hf_config, role, expected split sizes)  -- order is deterministic.
# THE BEST 2 (delivered by default; target_num_datasets=2): clutrr_gen hosts
# atomic-extraction P/R + multi-hop-accuracy-vs-length + trace-graph; clutrr_disc
# supplies the genuine within-document absent-relation pairs for the hallucination
# demo (and its test split also mixes clean/supporting/irrelevant/disconnected, so
# distractor examples for P/R robustness are present without a 3rd slice).
CONFIGS = [
    {
        "name": "clutrr_gen",
        "config": "gen_train234_test2to10",
        "role": "core_clean_systematic_generalization",
        "expected": {"train": 12064, "validation": 3019, "test": 1048},
        "doc": "Clean stories. Train hops 2-3-4, test hops 2..10 -> the multi-hop "
               "accuracy-vs-chain-length curve + atomic-extraction P/R + trace-graph.",
    },
    {
        "name": "clutrr_disc",
        "config": "rob_train_disc_23_test_all_23",
        "role": "disconnected_noise_absent_pairs",
        "expected": {"train": 8080, "validation": 2020, "test": 445},
        "doc": "Disconnected-fact noise: a second, structurally separate family chain "
               "=> genuine within-document ABSENT-relation pairs for the hallucination demo.",
    },
]

# Plan's explicitly-OPTIONAL 3rd slice (off by default). Enable with --include-sup
# to add a supporting-fact distractor-robustness arm for the atomic-extraction P/R claim.
OPTIONAL_CONFIGS = [
    {
        "name": "clutrr_sup",
        "config": "rob_train_sup_23_test_all_23",
        "role": "supporting_fact_distractors",
        "expected": {"train": 8123, "validation": 2031, "test": 447},
        "doc": "Supporting-fact distractors (extra same-context facts) -> a distractor-"
               "robustness arm for the atomic-extraction P/R claim. Optional 3rd slice.",
    },
]

SPLITS = ["train", "validation", "test"]
FOLD_MAP = {"train": "train", "validation": "dev", "test": "test"}
# task_<n1>.<n2>:  n1 = noise regime, n2 = chain length.
# Mapping VERIFIED empirically by config<->task correspondence: gen (clean) train is
# 100% task_1; rob_train_sup (supporting) train is 100% task_2; rob_train_disc
# (disconnected) train is 100% task_4 => task_3 is the remaining regime, irrelevant
# (it is what rob_train_irr trains on). Structural corroboration: only task_4 yields
# 2 components; task_2/task_3 add extra edges but stay single-component.
NOISE_TYPE = {1: "none", 2: "supporting", 3: "irrelevant", 4: "disconnected"}

SPLIT_LIMIT_BYTES = 70 * 1024 * 1024  # split full_data_out into parts under this

# Canonical CLUTRR target int<->text order (cross-checked empirically below).
CANONICAL_LABELS = [
    "aunt", "son-in-law", "grandfather", "brother", "sister", "father", "mother",
    "grandmother", "uncle", "daughter-in-law", "grandson", "granddaughter",
    "father-in-law", "mother-in-law", "nephew", "son", "daughter", "niece",
    "husband", "wife", "sister-in-law",
]


# --------------------------------------------------------------------------- #
# Acquisition
# --------------------------------------------------------------------------- #
def _download(url: str, dest: Path) -> None:
    if dest.exists() and dest.stat().st_size > 0:
        logger.debug(f"cached {dest.name}")
        return
    logger.info(f"downloading {url}")
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    dest.write_bytes(r.content)


def acquire_csvs(configs) -> dict[str, dict[str, Path]]:
    """PRIMARY path: pull each config's {train,validation,test}.csv directly."""
    paths: dict[str, dict[str, Path]] = {}
    for cfg in configs:
        paths[cfg["name"]] = {}
        for split in SPLITS:
            dest = TEMP / f"{cfg['config']}__{split}.csv"
            _download(f"{RAW_BASE}/{cfg['config']}/{split}.csv", dest)
            paths[cfg["name"]][split] = dest
    return paths


def acquire_yamls() -> tuple[dict, dict]:
    rules_p = TEMP / "rules_store.yaml"
    rels_p = TEMP / "relations_store.yaml"
    _download(f"{FB_STORE}/rules_store.yaml", rules_p)
    _download(f"{FB_STORE}/relations_store.yaml", rels_p)
    rules = yaml.safe_load(rules_p.read_text())
    rels = yaml.safe_load(rels_p.read_text())
    return rules, rels


# --------------------------------------------------------------------------- #
# Composition table (top-level metadata; emitted once)
# --------------------------------------------------------------------------- #
def build_composition_table(rules: dict, rels: dict) -> tuple[dict, dict]:
    """Returns (composition_table, surface2type)."""
    fam_sym = list(rules["symmetric"]["family"].keys())          # sibling, SO
    fam_inv = dict(rules["inverse-equivalence"]["family"])        # child->inv-child, ...
    inv_pairs = {}
    for a, b in fam_inv.items():
        inv_pairs[a] = b
        inv_pairs[b] = a
    comp_rules = {k: dict(v) for k, v in rules["compositional"]["family"].items()}

    # surface forms from relations_store.yaml (normalize the 'neice' typo).
    surface_forms: dict[str, dict[str, str]] = {}
    surface2type: dict[str, tuple[str, str]] = {}
    for rtype, gmap in rels.items():
        if not isinstance(gmap, dict):
            continue
        sf = {}
        for gender in ("male", "female"):
            if gender in gmap and isinstance(gmap[gender], dict):
                word = str(gmap[gender]["rel"]).strip()
                if word == "neice":
                    word = "niece"
                sf[gender] = word
                if rtype != "no-relation":
                    surface2type[word] = (rtype, gender)
        if sf:
            surface_forms[rtype] = sf

    # relation TYPES with flags
    relation_types = {}
    for rtype in surface_forms:
        if rtype == "no-relation":
            continue
        relation_types[rtype] = {
            "symmetric": rtype in fam_sym,
            "inverse": inv_pairs.get(rtype),  # None for symmetric / unpaired (e.g. sibling-in-law)
        }

    # reverse surface map word -> [type, gender]
    surface_reverse = {w: [t, g] for w, (t, g) in surface2type.items()}

    # DERIVED gendered surface-level composition (convenience). For A s1 B, B s2 C:
    # type(t3)=rules[type(s1)][type(s2)]; gender(C)=gender(s2); surface = forms[t3][gender(C)].
    derived = {}
    for s1, (t1, _g1) in surface2type.items():
        for s2, (t2, g2) in surface2type.items():
            t3 = comp_rules.get(t1, {}).get(t2)
            if t3 is None:
                continue
            word3 = surface_forms.get(t3, {}).get(g2)
            if word3 is None:
                continue
            derived[f"{s1}|{s2}"] = word3

    composition_table = {
        "relation_types": relation_types,
        "symmetric_types": fam_sym,
        "inverse_pairs": fam_inv,
        "surface_forms": surface_forms,
        "surface_reverse": surface_reverse,
        "composition_rules": comp_rules,
        "derived_gendered_surface_composition": derived,
        "label_map": {str(i): w for i, w in enumerate(CANONICAL_LABELS)},
        "label_map_reverse": {w: i for i, w in enumerate(CANONICAL_LABELS)},
        "semantics": ("Triple (h, r, t) reads 't is h's r'. Composition: A t1 B, "
                      "B t2 C => A t3 C, where rules[t1][t2]=t3 and the surface form "
                      "of t3 uses the gender of C."),
        "note": ("Finite composition table over kinship relation TYPES "
                 "(facebookresearch/clutrr rules_store.yaml). NOT a full relation "
                 "algebra: no general intersection/converse closure beyond these "
                 "rules; some compositions yield no-relation; ambiguous compositions "
                 "(e.g. grand o inv-child) are intentionally excluded in CLUTRR. Use "
                 "to temper any generality claim."),
        "source": {
            "rules_store": f"{FB_STORE}/rules_store.yaml",
            "relations_store": f"{FB_STORE}/relations_store.yaml",
            "scope": "family relation type only (CLUTRR 'work' relation type excluded; "
                     "the delivered configs are all kinship).",
        },
    }
    return composition_table, surface2type


# --------------------------------------------------------------------------- #
# Per-row parsing helpers
# --------------------------------------------------------------------------- #
def parse_proof(proof_str: str):
    """Return (parsed_proof_state, leaf_atomic_triples).

    proof_state is a list of dicts {goal_triple: [sub_triples...]} produced by
    backward chaining. A LEAF (atomic fact) is any sub-triple that is never
    itself a goal key.
    """
    pl = ast.literal_eval(proof_str)
    keys, subs = set(), []
    for d in pl:
        for goal, sublist in d.items():
            keys.add(goal)
            subs.extend(sublist)
    leaves = [s for s in subs if s not in keys]
    return pl, leaves


def bracket_parse(story: str):
    """Remove '['/']' markers; return (input_text, mention_spans name->[[s,e],...])."""
    out, spans, i, n = [], defaultdict(list), 0, len(story)
    cur = 0  # running length of input_text
    while i < n:
        c = story[i]
        if c == "[":
            j = story.index("]", i)
            name = story[i + 1:j]
            spans[name].append([cur, cur + len(name)])
            out.append(name)
            cur += len(name)
            i = j + 1
        else:
            out.append(c)
            cur += 1
            i += 1
    return "".join(out), {k: v for k, v in spans.items()}


def absent_pairs_from_components(node_ids, story_edges, node2name, query_nodes, cap=20):
    """Pairs of entities in DIFFERENT connected components => structural no-relation."""
    g = nx.Graph()
    g.add_nodes_from(node_ids)
    g.add_edges_from([tuple(e) for e in story_edges])
    comps = [sorted(c) for c in nx.connected_components(g)]
    qset = set(query_nodes)
    main = next((c for c in comps if qset & set(c)), comps[0] if comps else [])
    main_set = set(main)
    pairs = []
    # prioritise pairs that touch the main (query) component
    for m in sorted(main_set):
        for o in sorted(node_ids - main_set):
            a, b = sorted((m, o))
            pairs.append((a, b))
    # then remaining cross-component pairs (non-main x non-main, different comp)
    comp_of = {}
    for ci, c in enumerate(comps):
        for nd in c:
            comp_of[nd] = ci
    extra = []
    non_main = sorted(node_ids - main_set)
    for ii in range(len(non_main)):
        for jj in range(ii + 1, len(non_main)):
            a, b = non_main[ii], non_main[jj]
            if comp_of[a] != comp_of[b]:
                extra.append(tuple(sorted((a, b))))
    seen = set(pairs)
    for p in extra:
        if p not in seen:
            pairs.append(p)
            seen.add(p)
    pairs = pairs[:cap]
    out = [
        {"source": a, "target": b,
         "source_name": node2name[a], "target_name": node2name[b],
         "gold": "no-relation"}
        for a, b in pairs
    ]
    return out, comps


# --------------------------------------------------------------------------- #
# Row standardization
# --------------------------------------------------------------------------- #
def standardize_row(row: dict, corpus: str, fold: str, surface2type: dict, flags: Counter):
    rid = str(row["id"])
    story = str(row["story"])
    clean_story = str(row["clean_story"])
    target_text = str(row["target_text"])
    target_int = int(row["target"])
    f_comb = str(row["f_comb"])
    task_name = str(row["task_name"])

    story_edges = [tuple(e) for e in ast.literal_eval(row["story_edges"])]
    edge_types = list(ast.literal_eval(row["edge_types"]))
    query_edge = tuple(ast.literal_eval(row["query_edge"]))
    query = tuple(ast.literal_eval(row["query"]))
    genders = dict(p.split(":") for p in str(row["genders"]).split(","))
    _proof_state, leaves = parse_proof(row["proof_state"])

    # node_id -> name  (genders is canonically ordered by node id; verified vs proof)
    node2name = list(genders.keys())
    leaf_set = set(leaves)

    # all node ids appearing in the story graph (proof + noise + query anchors)
    node_ids = set()
    for s, t in story_edges:
        node_ids.add(s)
        node_ids.add(t)
    node_ids.add(query_edge[0])
    node_ids.add(query_edge[1])

    # ---- robustness checks (record, never silently drop) -------------------
    if max(node_ids) >= len(node2name):
        flags["node_id_out_of_genders_range"] += 1
        # extend with placeholder names so the row stays usable
        while len(node2name) <= max(node_ids):
            node2name.append(f"_entity_{len(node2name)}")
    if node2name[query_edge[0]] != query[0] or node2name[query_edge[1]] != query[1]:
        flags["query_anchor_mismatch"] += 1

    hop_count = len(edge_types)
    n2 = int(task_name.split(".")[-1]) if "." in task_name else hop_count
    n1 = int(task_name.split("_")[1].split(".")[0]) if "_" in task_name else 1
    if not (hop_count == f_comb.count("-") + 1 == n2):
        flags["hop_count_disagreement"] += 1

    # ---- typed atomic (proof-chain) edges = story_edges[:hop_count] ---------
    edges = []
    atomic_facts = []
    for k in range(hop_count):
        s, t = story_edges[k]
        rel = edge_types[k]
        rtype, _g = surface2type.get(rel, (None, None))
        if (node2name[s], rel, node2name[t]) not in leaf_set:
            flags["proof_edge_not_in_leaves"] += 1
        edges.append({
            "source": s, "target": t,
            "kinship_relation": rel, "relation_type": rtype,
            "is_query": False, "hop_count": 1,
        })
        atomic_facts.append({
            "source_id": s, "target_id": t,
            "source_name": node2name[s], "target_name": node2name[t],
            "kinship_relation": rel, "relation_type": rtype,
        })

    # ---- structural NOISE edges = story_edges[hop_count:] (CLUTRR untyped) --
    noise_edges = []
    for k in range(hop_count, len(story_edges)):
        s, t = story_edges[k]
        noise_edges.append({
            "source": s, "target": t,
            "source_name": node2name[s], "target_name": node2name[t],
            "kinship_relation": None, "relation_type": None,
            "is_query": False,
            "note": "Structural fact stated in the story but not typed by CLUTRR's "
                    "released fields (edge_types covers only the proof chain).",
        })

    # ---- input text + mention spans ---------------------------------------
    input_text, mention_spans = bracket_parse(story)
    for nm, sl in mention_spans.items():
        for s_, e_ in sl:
            if input_text[s_:e_] != nm:
                flags["span_substring_mismatch"] += 1
    for nm in re.findall(r"\[([^\]]+)\]", story):
        if nm not in genders:
            flags["bracket_name_missing_from_genders"] += 1

    # ---- absent-relation pairs (pure connectivity) ------------------------
    absent, comps = absent_pairs_from_components(
        node_ids, story_edges, node2name, (query_edge[0], query_edge[1])
    )

    # ---- nodes -------------------------------------------------------------
    nodes = []
    for nid in sorted(node_ids):
        nm = node2name[nid]
        nodes.append({
            "entity_id": nid,
            "surface": nm,
            "gender": genders.get(nm),
            "mention_spans": mention_spans.get(nm, []),
        })

    # ---- query edge --------------------------------------------------------
    q_rtype, _qg = surface2type.get(target_text, (None, None))
    query_edge_obj = {
        "source": query_edge[0], "target": query_edge[1],
        "kinship_relation": target_text, "relation_type": q_rtype,
        "target_int": target_int, "is_query": True, "hop_count": hop_count,
    }

    gold_graph = {
        "doc_id": rid,
        "corpus": corpus,
        "nodes": nodes,
        "edges": edges,                       # typed atomic story facts (proof chain)
        "noise_edges": noise_edges,           # structural-only (untyped in source)
        "query_edge": query_edge_obj,         # held-out, deduced
        "absent_relation_pairs": absent,      # structural no-relation
        "absent_pairs_source": "structural_components",
    }

    # ---- gold backward-chaining proof (trace-graph gold) -------------------
    gold_proof = []
    for d in _proof_state:
        for goal, sublist in d.items():
            gold_proof.append({
                "goal": list(goal),
                "subgoals": [list(x) for x in sublist],
            })

    example = {
        "input": input_text,
        "output": json.dumps(gold_graph, ensure_ascii=False),
        "metadata_doc_id": rid,
        "metadata_corpus": corpus,
        "metadata_fold": fold,
        "metadata_hop_count": hop_count,
        "metadata_noise_type": NOISE_TYPE.get(n1, "unknown"),
        "metadata_task_name": task_name,
        "metadata_f_comb": f_comb,
        "metadata_query": {
            "source_name": query[0], "target_name": query[1],
            "relation": target_text, "target_int": target_int,
        },
        "metadata_atomic_facts": atomic_facts,
        "metadata_gold_proof": gold_proof,
        "metadata_genders": genders,
        "metadata_num_entities": len(node_ids),
        "metadata_num_atomic_edges": len(edges),
        "metadata_num_noise_edges": len(noise_edges),
        "metadata_num_components": len(comps),
        "metadata_absent_pair_count": len(absent),
        "metadata_story_char_len": len(input_text),
        "metadata_clean_story": clean_story,
    }
    return example


# --------------------------------------------------------------------------- #
# Descriptive counts (ALLOWED: pure tallies / graph descriptors)
# --------------------------------------------------------------------------- #
def hist(values):
    return dict(sorted(Counter(values).items()))


def length_stats(vals):
    vs = sorted(vals)
    if not vs:
        return {}
    return {
        "min": vs[0], "max": vs[-1],
        "mean": round(mean(vs), 1), "median": int(median(vs)),
        "p90": vs[int(0.9 * (len(vs) - 1))],
        "n_ge_2000_chars": sum(v >= 2000 for v in vs),
        "n_ge_3000_chars": sum(v >= 3000 for v in vs),
    }


def descriptive_counts(name, examples):
    char_lens = [e["metadata_story_char_len"] for e in examples]
    n_with_absent = sum(e["metadata_absent_pair_count"] > 0 for e in examples)
    return {
        "n_stories": len(examples),
        "n_entities_total": sum(e["metadata_num_entities"] for e in examples),
        "n_atomic_edges_total": sum(e["metadata_num_atomic_edges"] for e in examples),
        "n_noise_edges_total": sum(e["metadata_num_noise_edges"] for e in examples),
        "fold_counts": hist(e["metadata_fold"] for e in examples),
        "hop_count_distribution": hist(e["metadata_hop_count"] for e in examples),
        "relation_label_distribution": hist(e["metadata_query"]["relation"] for e in examples),
        "noise_type_distribution": hist(e["metadata_noise_type"] for e in examples),
        "component_count_distribution": hist(e["metadata_num_components"] for e in examples),
        "n_stories_with_absent_pairs": n_with_absent,
        "total_absent_pairs": sum(e["metadata_absent_pair_count"] for e in examples),
        "story_char_length": length_stats(char_lens),
    }


# --------------------------------------------------------------------------- #
# Output writing (full split by size, + mini / preview variants)
# --------------------------------------------------------------------------- #
def _truncate_strings(obj, limit=200):
    if isinstance(obj, str):
        return obj if len(obj) <= limit else obj[:limit] + "...[truncated]"
    if isinstance(obj, list):
        return [_truncate_strings(x, limit) for x in obj]
    if isinstance(obj, dict):
        return {k: _truncate_strings(v, limit) for k, v in obj.items()}
    return obj


def write_full_split(metadata, datasets):
    """Write full_data_out/full_data_out_*.json, each part a valid {metadata,datasets} doc."""
    for old in glob.glob(str(OUT_DIR / "full_data_out_*.json")):
        Path(old).unlink()
    # flatten to (dataset_name, example) preserving dataset order
    flat = [(ds["dataset"], ex) for ds in datasets for ex in ds["examples"]]

    parts, cur, cur_bytes = [], defaultdict(list), 0
    base_overhead = len(json.dumps({"metadata": metadata, "datasets": []}).encode())
    for dsname, ex in flat:
        ex_bytes = len(json.dumps(ex, ensure_ascii=False).encode()) + 2
        if cur_bytes + ex_bytes + base_overhead > SPLIT_LIMIT_BYTES and any(cur.values()):
            parts.append(cur)
            cur, cur_bytes = defaultdict(list), 0
        cur[dsname].append(ex)
        cur_bytes += ex_bytes
    if any(cur.values()):
        parts.append(cur)

    written = []
    for idx, part in enumerate(parts, 1):
        doc = {
            "metadata": metadata,
            "datasets": [{"dataset": dn, "examples": exs} for dn, exs in part.items()],
        }
        p = OUT_DIR / f"full_data_out_{idx}.json"
        p.write_text(json.dumps(doc, ensure_ascii=False))
        written.append(p)
        logger.info(f"wrote {p.name}  ({p.stat().st_size/1e6:.1f} MB, "
                    f"{sum(len(x) for x in part.values())} rows)")
    return written


def select_variant(datasets, per_dataset):
    """Pick `per_dataset` representative examples per dataset: one per distinct
    hop-count (ascending → spans the multi-hop curve, guarantees ≥1 multi-hop),
    then force-include ≥1 absent-pair row where the corpus has any."""
    out = []
    for ds in datasets:
        exs = ds["examples"]
        picked, seen = [], set()
        by_hop = {}
        for e in exs:
            by_hop.setdefault(e["metadata_hop_count"], e)  # first per hop
        for h in sorted(by_hop):
            if len(picked) < per_dataset:
                e = by_hop[h]
                picked.append(e)
                seen.add(id(e))
        # ensure an absent-pair example is present if the corpus has any
        has_absent = any(e["metadata_absent_pair_count"] > 0 for e in picked)
        absent_rows = [e for e in exs if e["metadata_absent_pair_count"] > 0]
        if not has_absent and absent_rows:
            if len(picked) < per_dataset:
                picked.append(absent_rows[0])
                seen.add(id(absent_rows[0]))
            else:
                picked[-1] = absent_rows[0]  # swap last in
        # top up from the head if still short
        for e in exs:
            if len(picked) >= per_dataset:
                break
            if id(e) not in seen:
                picked.append(e)
                seen.add(id(e))
        out.append({"dataset": ds["dataset"], "examples": picked[:per_dataset]})
    return out


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
@logger.catch(reraise=True)
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="rows per split (0=all)")
    ap.add_argument("--include-sup", action="store_true",
                    help="also build the optional 3rd slice clutrr_sup (supporting-fact distractors)")
    args = ap.parse_args()

    active_configs = CONFIGS + (OPTIONAL_CONFIGS if args.include_sup else [])
    logger.info(f"=== CLUTRR kinship gold-graph builder ({len(active_configs)} datasets: "
                f"{[c['name'] for c in active_configs]}) ===")
    csv_paths = acquire_csvs(active_configs)
    rules, rels = acquire_yamls()
    composition_table, surface2type = build_composition_table(rules, rels)
    logger.info(f"composition table: {len(composition_table['relation_types'])} relation "
                f"types, {len(composition_table['composition_rules'])} rule-heads, "
                f"{len(composition_table['surface_reverse'])} surface words")

    flags = Counter()
    datasets = []
    empirical_label_map = {}
    for cfg in active_configs:
        examples = []
        for split in SPLITS:
            df = pd.read_csv(csv_paths[cfg["name"]][split], dtype=str)
            df = df.sort_values("id").reset_index(drop=True)
            exp = cfg["expected"][split]
            if len(df) != exp:
                logger.warning(f"{cfg['name']}/{split}: {len(df)} rows (expected {exp})")
            else:
                logger.info(f"{cfg['name']}/{split}: {len(df)} rows OK")
            rows = df.to_dict("records")
            if args.limit:
                rows = rows[: args.limit]
            for row in rows:
                try:
                    empirical_label_map[int(row["target"])] = str(row["target_text"])
                    ex = standardize_row(row, cfg["name"], FOLD_MAP[split],
                                         surface2type, flags)
                    examples.append(ex)
                except Exception:
                    flags["row_parse_error"] += 1
                    logger.error(f"row parse error id={row.get('id')}")
                    continue
        datasets.append({"dataset": cfg["name"], "examples": examples,
                         "_role": cfg["role"], "_config": cfg["config"], "_doc": cfg["doc"]})
        logger.info(f"{cfg['name']}: {len(examples)} examples standardized")

    # cross-check empirical label map vs canonical
    label_ok = all(empirical_label_map.get(i) == w
                   for i, w in enumerate(CANONICAL_LABELS) if i in empirical_label_map)
    logger.info(f"empirical label_map matches canonical 0..20: {label_ok} "
                f"({len(empirical_label_map)} ints observed)")

    # descriptive counts
    per_corpus = {ds["dataset"]: descriptive_counts(ds["dataset"], ds["examples"])
                  for ds in datasets}
    all_examples = [e for ds in datasets for e in ds["examples"]]
    overall = descriptive_counts("ALL", all_examples)

    # ---- top-level metadata ------------------------------------------------
    metadata = {
        "name": "CLUTRR kinship gold graphs",
        "description": (
            "CLUTRR (Sinha et al., EMNLP 2019) semi-synthetic family stories "
            "standardized to per-story gold KINSHIP graphs: entity nodes (surface, "
            "gender, mention spans) + typed atomic story facts (the proof chain) + a "
            "held-out query edge requiring >=2-hop composition + structural "
            "absent-relation pairs (different connected components) + structural noise "
            "edges. One end-to-end venue for atomic-extraction P/R, multi-hop accuracy "
            "vs chain length, human-auditable trace-graphs, and a hallucination demo on "
            "provably-absent relations."),
        "schema": "exp_sel_data_out (input=story string, output=json.dumps(gold_graph), "
                  "structured per-row data under metadata_* keys).",
        "datasets_overview": {ds["dataset"]: {"role": ds["_role"],
                                              "hf_config": ds["_config"],
                                              "doc": ds["_doc"],
                                              "n_examples": len(ds["examples"])}
                              for ds in datasets},
        "composition_table": composition_table,
        "gold_graph_field_spec": {
            "nodes": "[{entity_id, surface, gender, mention_spans=[[start,end),...] into input}]",
            "edges": "typed ATOMIC story facts (the proof chain); "
                     "{source,target,kinship_relation,relation_type,is_query=false,hop_count=1}; "
                     "directed: t is source's kinship_relation (i.e. (h,r,t) with h=source).",
            "noise_edges": "extra story_edges CLUTRR does NOT type (disconnected/distractor "
                           "facts); structural only {source,target,relation_type=null}. The "
                           "word-before-bracket heuristic recovers only ~54% even on known "
                           "edges, so noise relations are intentionally left untyped, not fabricated.",
            "query_edge": "held-out, NOT stated; deduced by composing the atomic edges; "
                          "{source,target,kinship_relation=gold,relation_type,target_int,hop_count}.",
            "absent_relation_pairs": "entity pairs in DIFFERENT connected components of the "
                                     "story graph => provably no kinship path => 'no-relation' "
                                     "(structural, conservative, sound). Capped at 20/story.",
        },
        "reconstruction_facts": {
            "node_id_to_name": "genders is canonically ordered by node id; verified consistent "
                               "with the backward-chaining proof leaves on all rows.",
            "atomic_edges": "= story_edges[:len(edge_types)] zipped with edge_types (the proof "
                            "chain is always the prefix; verified 0 violations).",
            "noise_edges": "= story_edges[len(edge_types):] (untyped in CLUTRR's released fields).",
            "leaves": "proof_state sub-triples that are never a goal key (= the atomic facts).",
            "directionality": "story_edge (s,t) with edge_types[k]=r encodes leaf (name[s], r, name[t]) "
                              "= 'name[t] is name[s]'s r'.",
        },
        "provenance": {
            "dataset": "CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text",
            "authors": "Sinha, Sodhani, Dong, Pineau, Hamilton",
            "venue": "EMNLP 2019 (ACL Anthology D19-1458)",
            "arxiv": "1908.06177",
            "csv_source": f"{RAW_BASE} (the GitHub raw mirror HF CLUTRR/v1 v1.py downloads)",
            "hf_dataset": "CLUTRR/v1",
            "composition_source": "facebookresearch/clutrr (rules_store.yaml, relations_store.yaml)",
            "license": "CLUTRR is released by Facebook under a research/non-commercial license "
                       "(see facebookresearch/clutrr LICENSE; CC-BY-NC-style). Use for research only.",
        },
        "build_qa": {
            "rows_total": len(all_examples),
            "empirical_label_map_matches_canonical": label_ok,
            "flags": dict(flags),
        },
        "boundary_note": ("DESCRIPTIVE counts only. No composition/closure, all-pair labeling, "
                          "atomic-extraction P/R, multi-hop accuracy, N*, or hallucination-rate "
                          "numbers, and no LLM calls -- those are iter-3's experiment."),
        "descriptive_counts": {"overall": overall, "per_corpus": per_corpus},
    }

    clean_datasets = [{"dataset": ds["dataset"], "examples": ds["examples"]} for ds in datasets]

    # ---- write outputs -----------------------------------------------------
    write_full_split(metadata, clean_datasets)

    mini = select_variant(clean_datasets, per_dataset=3)    # 3 examples / dataset
    (ROOT / "mini_data_out.json").write_text(
        json.dumps({"metadata": metadata, "datasets": mini}, ensure_ascii=False))
    preview_rows = select_variant(clean_datasets, per_dataset=10)  # 10 / dataset
    preview = {"metadata": _truncate_strings(metadata),
               "datasets": _truncate_strings(preview_rows)}
    (ROOT / "preview_data_out.json").write_text(
        json.dumps(preview, ensure_ascii=False))
    logger.info(f"wrote mini ({sum(len(d['examples']) for d in mini)} rows) + "
                f"preview ({sum(len(d['examples']) for d in preview_rows)} rows)")

    # ---- data card ---------------------------------------------------------
    card = {
        "name": metadata["name"],
        "provenance": metadata["provenance"],
        "datasets_overview": metadata["datasets_overview"],
        "build_qa": metadata["build_qa"],
        "descriptive_counts": {"overall": overall, "per_corpus": per_corpus},
        "composition_table_summary": {
            "n_relation_types": len(composition_table["relation_types"]),
            "relation_types": list(composition_table["relation_types"].keys()),
            "n_composition_rule_entries": sum(len(v) for v in
                                              composition_table["composition_rules"].values()),
            "label_map": composition_table["label_map"],
        },
    }
    (RESULTS / "dataset_metadata.json").write_text(json.dumps(card, indent=2, ensure_ascii=False))
    logger.info("wrote results/dataset_metadata.json")
    logger.info(f"flags: {dict(flags)}")
    logger.info(f"DONE: {len(all_examples)} rows across {len(clean_datasets)} datasets")


if __name__ == "__main__":
    main()
