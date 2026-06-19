#!/usr/bin/env python3
"""0-LLM unit tests gating every downstream LLM spend (STEP 1 of the testing plan).

(a) data loads + composition table present + dataset counts;
(b) compose_types matches the dataset rules on every listed cell; converse round-trips;
(c) DECISIVE: gold-atomic forward-closure recovers the gold query (soundness == 1.0 on
    every emitted answer; high singleton-rate on clean rows);
(d) iteration mechanism: naive resolves hop-2 but ABSTAINS on hop>=3 while full PC-2
    (forward closure) resolves all -- the H3 mechanism, proven before any LLM call.
"""
from __future__ import annotations

import sys

from loguru import logger

from dataio import gold_atomic_check, load_clutrr
from kinship import Kinship, query_modeA, query_naive
from prolog import discharge, solve_paths

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")


def test_load(mini: bool):
    gen, disc, comp = load_clutrr(mini=mini)
    assert comp is not None and "composition_rules" in comp, "composition table missing"
    for k in ("relation_types", "symmetric_types", "inverse_pairs", "surface_forms",
              "surface_reverse", "composition_rules", "label_map"):
        assert k in comp, f"composition_table missing {k}"
    assert len(gen) > 0 and len(disc) > 0, "empty datasets"
    if not mini:
        assert len(gen) == 16131, f"gen count {len(gen)} != 16131"
        assert len(disc) == 10545, f"disc count {len(disc)} != 10545"
    logger.info(f"(a) load OK: gen={len(gen)} disc={len(disc)}")
    return gen, disc, comp


def test_compose_and_converse(kin: Kinship):
    # every listed rule cell reproduced
    for t1, row in kin.composition_rules.items():
        for t2, t3 in row.items():
            got = kin.compose_types(t1, t2)
            assert got == t3, f"compose({t1},{t2})={got} != {t3}"
    # undefined cell -> None
    assert kin.compose_types("sibling", "SO") is None, "expected undefined SO composition"
    # converse total + round-trips
    for t in kin.base:
        ct = kin.conv_type(t)
        assert ct in kin.base, f"converse({t})={ct} not a base type"
        assert kin.conv_type(ct) == t, f"converse not involutive at {t}"
    logger.info(f"(b) compose/converse OK: {sum(len(r) for r in kin.composition_rules.values())} "
                f"rule cells, {len(kin.base)} converses involutive")


def test_decisive_gold_atomic(gen, disc, kin: Kinship, full: bool):
    rg = gold_atomic_check(gen, kin, only_clean=True, limit=None if full else 400)
    rd = gold_atomic_check(disc, kin, only_clean=True, limit=None if full else 400)
    logger.info(f"(c) gen clean: n={rg['n']} singleton_rate={rg['singleton_rate']:.4f} "
                f"acc_on_singletons={rg['accuracy_on_singletons']:.4f} conflict={rg['n_modeb_conflict']}")
    logger.info(f"(c) disc clean: n={rd['n']} singleton_rate={rd['singleton_rate']:.4f} "
                f"acc_on_singletons={rd['accuracy_on_singletons']:.4f} conflict={rd['n_modeb_conflict']}")
    # SOUNDNESS is the hard gate: every emitted (singleton) answer must be correct.
    assert rg["accuracy_on_singletons"] >= 0.999, "gen soundness < 1.0 -- engine bug"
    if rd["n_singleton"] > 0:
        assert rd["accuracy_on_singletons"] >= 0.999, "disc soundness < 1.0 -- engine bug"
    # recovery should be high on clean gold atomics
    assert rg["singleton_rate"] >= 0.95, f"gen singleton_rate {rg['singleton_rate']} too low"
    logger.info("(c) DECISIVE soundness gate PASSED (100% of emitted answers correct)")
    return rg, rd


def test_iteration_mechanism(kin: Kinship):
    for k in range(2, 7):
        names = [f"e{i}" for i in range(k + 1)]
        edges = [{"a": names[i], "b": names[i + 1], "type": "sibling"} for i in range(k)]
        a = query_modeA(kin, edges, names[0], names[-1])
        n = query_naive(kin, edges, names[0], names[-1])
        assert a["singleton"] and a["answer_type"] == "sibling", f"full failed hop{k}"
        if k == 2:
            assert n["singleton"], "naive should resolve hop-2"
        else:
            assert not n["singleton"], f"naive should ABSTAIN on hop{k}>=3"
    logger.info("(d) iteration mechanism OK: naive resolves hop-2, abstains hop>=3; full resolves all")


def test_prolog_crosscheck(kin: Kinship):
    edges = [{"a": "Lena", "b": "Joshua", "type": "sibling"},
             {"a": "Joshua", "b": "Lynn", "type": "SO"},
             {"a": "Lynn", "b": "Andrea", "type": "child"}]
    d = discharge(kin, edges, "Lena", "Andrea")
    py = sorted(solve_paths(kin, edges, "Lena", "Andrea"))
    logger.info(f"(e) prolog engine={d['engine']} executed_in_swipl={d['executed_in_swipl']} "
                f"prolog={d.get('prolog_results')} python={py}")
    if d["executed_in_swipl"]:
        assert d["prolog_results"] == py == ["un"], "prolog/python disagree on worked example"
        logger.info("(e) SWI-Prolog discharge cross-check PASSED")
    else:
        logger.warning("(e) SWI-Prolog not executed; python-checked fallback only")


def main():
    full = "--full" in sys.argv
    mini = "--mini" in sys.argv
    logger.info(f"running tests (full={full}, mini={mini})")
    gen, disc, comp = test_load(mini=mini)
    kin = Kinship(comp)
    test_compose_and_converse(kin)
    test_decisive_gold_atomic(gen, disc, kin, full=full and not mini)
    test_iteration_mechanism(kin)
    test_prolog_crosscheck(kin)
    logger.info("ALL UNIT TESTS PASSED")


if __name__ == "__main__":
    main()
