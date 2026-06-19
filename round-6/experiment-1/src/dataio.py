#!/usr/bin/env python3
"""Load + merge the PREPARED CLUTRR kinship gold graphs (dependency art_HS7-lxhZnU9m).

NO network: the gold graphs are already frozen by the dataset dependency. We merge the
two <100MB parts, expose the composition table, and provide deterministic subsamplers
for (a) the gen accuracy/atomic/iteration scored set and (b) the disc absent-relation
pool. A decisive 0-LLM verifier (`gold_atomic_check`) closes every story from its GOLD
atomic facts and asserts the recovered query matches the gold relation -- the go/no-go
gate for trusting the symbolic engine.
"""
from __future__ import annotations

import glob
import json
from collections import defaultdict
from pathlib import Path

from loguru import logger

from kinship import Kinship, query_modeA

# Dependency dataset workspace (read-only). Parts merge by dataset name.
DEP_DATASET_DIR = Path(
    "/ai-inventor/aii_data/runs/run_IuSkWzF0As-P/3_invention_loop/iter_2/"
    "gen_art/gen_art_dataset_1"
)
FULL_DIR = DEP_DATASET_DIR / "full_data_out"
MINI_FILE = DEP_DATASET_DIR / "mini_data_out.json"


def _atomics_to_edges(metadata_atomic_facts: list[dict]) -> list[dict]:
    """Gold atomic facts -> [{a,b,type}] (a=source, b=target, 'b is a's type')."""
    out = []
    for f in metadata_atomic_facts:
        out.append({"a": f["source_name"], "b": f["target_name"],
                    "type": f["relation_type"], "surface": f.get("kinship_relation")})
    return out


def load_clutrr(mini: bool = False):
    """Return (gen_examples, disc_examples, composition_table)."""
    if mini:
        part = json.loads(MINI_FILE.read_text())
        comp = part["metadata"]["composition_table"]
        byname = defaultdict(list)
        for ds in part["datasets"]:
            byname[ds["dataset"]].extend(ds["examples"])
        logger.info(f"loaded MINI: gen={len(byname['clutrr_gen'])} disc={len(byname['clutrr_disc'])}")
        return byname["clutrr_gen"], byname["clutrr_disc"], comp

    files = sorted(glob.glob(str(FULL_DIR / "full_data_out_*.json")))
    if not files:
        raise FileNotFoundError(f"no full_data_out parts under {FULL_DIR}")
    comp = None
    byname = defaultdict(list)
    for f in files:
        part = json.loads(Path(f).read_text())
        if comp is None:
            comp = part["metadata"]["composition_table"]
        for ds in part["datasets"]:
            byname[ds["dataset"]].extend(ds["examples"])
    logger.info(f"loaded FULL: gen={len(byname['clutrr_gen'])} disc={len(byname['clutrr_disc'])} "
                f"from {len(files)} parts")
    return byname["clutrr_gen"], byname["clutrr_disc"], comp


def parse_gold_graph(ex: dict) -> dict:
    """json.loads the per-row gold_graph (output field)."""
    return json.loads(ex["output"])


# --------------------------------------------------------------------------- #
# Deterministic subsamplers (sorted by doc_id; fixed caps; no randomness)
# --------------------------------------------------------------------------- #
def subsample_gen(gen_examples: list[dict], fold: str = "test",
                  cap_per_hop: int | None = None, scale: int | None = None) -> list[dict]:
    """gen scored set for accuracy-vs-hop + atomic P/R + trace. Default: the whole TEST
    fold (spans hops 2..10; train is hops 2-3-4 only). cap_per_hop caps each hop bin."""
    rows = [e for e in gen_examples if e["metadata_fold"] == fold]
    rows.sort(key=lambda e: e["metadata_doc_id"])
    if cap_per_hop is not None:
        by_hop: dict = defaultdict(list)
        for e in rows:
            by_hop[e["metadata_hop_count"]].append(e)
        kept = []
        for h in sorted(by_hop):
            kept.extend(by_hop[h][:cap_per_hop])
        rows = kept
    if scale is not None:
        rows = rows[:scale]
    return rows


def subsample_disc(disc_examples: list[dict], fold: str = "test",
                   cap: int | None = None, scale: int | None = None) -> list[dict]:
    """disc scored set: prefer two-component stories carrying genuine absent pairs, plus
    their present held-out query. Default: the whole TEST fold (mixes clean/supporting/
    irrelevant/disconnected noise -> P/R robustness + absent-relation demo)."""
    rows = [e for e in disc_examples if e["metadata_fold"] == fold]
    # absent-pair-bearing stories first (deterministic), then the rest
    rows.sort(key=lambda e: (0 if e.get("metadata_absent_pair_count", 0) > 0 else 1,
                             e["metadata_doc_id"]))
    if cap is not None:
        rows = rows[:cap]
    if scale is not None:
        rows = rows[:scale]
    return rows


# --------------------------------------------------------------------------- #
# DECISIVE go/no-go: gold-atomic closure recovers the gold query on every row
# --------------------------------------------------------------------------- #
def gold_atomic_check(examples: list[dict], kin: Kinship, only_clean: bool = True,
                      limit: int | None = None) -> dict:
    """Build each story's QCN from GOLD atomic facts, close it, and compare the recovered
    query relation to gold. Returns aggregate stats + a few failing rows for inspection.
    On noise_type='none' rows we expect ~100% (0 violations is the go signal)."""
    n = 0
    n_singleton = 0
    n_correct = 0
    n_conflict = 0
    n_nopath = 0
    fails = []
    for ex in examples:
        if only_clean and ex["metadata_noise_type"] != "none":
            continue
        q = ex["metadata_query"]
        qsrc, qtgt = q["source_name"], q["target_name"]
        gold_surface = q["relation"]
        genders = ex["metadata_genders"]
        edges = _atomics_to_edges(ex["metadata_atomic_facts"])
        res = query_modeA(kin, edges, qsrc, qtgt)
        n += 1
        if res["mode_b_conflict"]:
            n_conflict += 1
        if res["no_path"]:
            n_nopath += 1
        if res["singleton"]:
            n_singleton += 1
            pred_surface = kin.surface(res["answer_type"], genders.get(qtgt, "male"))
            if pred_surface == gold_surface:
                n_correct += 1
            elif len(fails) < 12:
                fails.append({"doc_id": ex["metadata_doc_id"], "hop": ex["metadata_hop_count"],
                              "qsrc": qsrc, "qtgt": qtgt, "gold": gold_surface,
                              "pred_type": res["answer_type"], "pred_surface": pred_surface,
                              "types": kin.label(res["types"]), "f_comb": ex.get("metadata_f_comb")})
        elif len(fails) < 12:
            tag = "ABSTAIN(conflict)" if res["mode_b_conflict"] else "ABSTAIN(no-path)"
            fails.append({"doc_id": ex["metadata_doc_id"], "hop": ex["metadata_hop_count"],
                          "qsrc": qsrc, "qtgt": qtgt, "gold": gold_surface,
                          "pred_type": None, "pred_surface": tag,
                          "types": kin.label(res["types"]), "f_comb": ex.get("metadata_f_comb")})
        if limit and n >= limit:
            break
    return {"n": n, "n_singleton": n_singleton, "n_correct": n_correct,
            "n_modeb_conflict": n_conflict, "n_no_path": n_nopath,
            "singleton_rate": (n_singleton / n if n else 0.0),
            "accuracy_on_singletons": (n_correct / n_singleton if n_singleton else 0.0),
            "overall_recovery": (n_correct / n if n else 0.0), "fails": fails}


if __name__ == "__main__":
    import sys
    logger.remove()
    logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
    gen, disc, comp = load_clutrr(mini=False)
    kin = Kinship(comp)
    logger.info("=== DECISIVE gold-atomic closure check on ALL clean (noise=none) rows ===")
    for name, exs in [("clutrr_gen", gen), ("clutrr_disc", disc)]:
        r = gold_atomic_check(exs, kin, only_clean=True)
        logger.info(f"{name}: n_clean={r['n']} singleton_rate={r['singleton_rate']:.4f} "
                    f"acc_on_singletons={r['accuracy_on_singletons']:.4f} "
                    f"overall_recovery={r['overall_recovery']:.4f} "
                    f"conflict={r['n_modeb_conflict']} no_path={r['n_no_path']}")
        if r["fails"]:
            logger.warning(f"{name} sample fails ({len(r['fails'])}):")
            for f in r["fails"][:8]:
                logger.warning(f"   {f}")
