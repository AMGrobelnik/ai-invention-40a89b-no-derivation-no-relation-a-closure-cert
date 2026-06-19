#!/usr/bin/env python3
"""0-LLM unit tests for the iter-6 confidence-battery components (testing_plan A).

Run: uv run tests.py   (no LLM, no network, deterministic).
Gates: semantic-entropy bounds + monotonicity; ct_* baseline plumbing at tau extremes
(matched-coverage mask + coverage_confidence rank abstentions below named answers);
confident-wrong / query-correct semantics on absent vs present; reproduction of the
published absent-pool 0.444 reduction is checked by method.py against the stored pool."""
from __future__ import annotations

import sys

import numpy as np
from loguru import logger

import baselines as B
from stats import matched_coverage_mask, selective_accuracy
from method import semantic_entropy, SIGNALS

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")


def _mk(surf):
    return {"surface": surf, "confidence": 1.0, "abstain": surf in (None, "no-relation")}


def test_semantic_entropy():
    # unanimous -> negent 1.0, H 0
    u = semantic_entropy([_mk("father")] * 10)
    assert abs(u["negent"] - 1.0) < 1e-9 and abs(u["H"]) < 1e-9, u
    # uniform over k distinct clusters -> negent ~0, H = log k
    distinct = [_mk(s) for s in ["father", "mother", "brother", "sister", "son",
                                 "daughter", "uncle", "aunt", "nephew", "niece"]]
    d = semantic_entropy(distinct)
    assert d["negent"] < 1e-6, d
    assert abs(d["H"] - np.log(10)) < 1e-9, d
    # monotone: more agreement => higher negent
    a = semantic_entropy([_mk("father")] * 8 + [_mk("mother")] * 2)["negent"]
    b = semantic_entropy([_mk("father")] * 5 + [_mk("mother")] * 5)["negent"]
    assert a > b, (a, b)
    # 'no-relation'/None form their own cluster
    nr = semantic_entropy([_mk("no-relation")] * 6 + [_mk(None)] * 4)
    assert nr["negent"] > 0.99, nr  # both map to the same 'no-relation' cluster -> unanimous
    logger.info("test_semantic_entropy PASS")


def test_ct_baseline_plumbing():
    # 4 present records; raw named all; signal varies. tau=0 (cover all) => confident-wrong
    # equals commit_argmax's; ranking puts low-signal abstentions below named answers.
    recs = []
    for i, (surf, gold, sig) in enumerate([("father", "father", 0.9), ("mother", "father", 0.8),
                                           ("uncle", "uncle", 0.3), ("aunt", "uncle", 0.2)]):
        recs.append({"doc_id": f"d{i}", "is_absent": False, "gold_surface": gold,
                     "ct_x": {"surface": surf, "conf": sig, "named": True},
                     "commit_argmax": {"surface": surf, "conf": 1.0, "named": True}})
    conf = np.array([B.coverage_confidence(r["ct_x"]["named"], r["ct_x"]["conf"]) for r in recs])
    cw = np.array([B.confident_wrong(r["ct_x"]["named"], r["ct_x"]["surface"], r["gold_surface"],
                                     r["is_absent"]) for r in recs], float)
    # tau covering all (coverage 1.0) -> mask all -> cw = 2/4 (mother, aunt wrong)
    mask_full = matched_coverage_mask(conf, 1.0)
    assert mask_full.all() and abs((cw * mask_full).sum() / 4 - 0.5) < 1e-9
    # coverage 0.5 -> top-2 by signal (father .9, mother .8) -> 1 wrong (mother)
    mask_half = matched_coverage_mask(conf, 0.5)
    assert mask_half.sum() == 2 and abs((cw * mask_half).sum() / 4 - 0.25) < 1e-9
    # an abstaining record ranks below any named one
    recs[2]["ct_x"] = {"surface": None, "conf": 0.99, "named": False}
    conf2 = np.array([B.coverage_confidence(r["ct_x"]["named"], r["ct_x"]["conf"]) for r in recs])
    order = sorted(range(4), key=lambda i: (-conf2[i], i))
    assert order[-1] == 2, order  # the (named=False, conf .99) record is ranked LAST
    logger.info("test_ct_baseline_plumbing PASS")


def test_confident_wrong_semantics():
    # absent: ANY named answer is wrong; abstain is correct
    assert B.confident_wrong(True, "father", "no-relation", True) is True
    assert B.confident_wrong(False, None, "no-relation", True) is False
    assert B.query_correct(False, None, "no-relation", True) is True
    assert B.query_correct(True, "father", "no-relation", True) is False
    # present: named & match correct
    assert B.query_correct(True, "father", "father", False) is True
    assert B.confident_wrong(True, "mother", "father", False) is True
    assert B.confident_wrong(False, None, "father", False) is False
    logger.info("test_confident_wrong_semantics PASS")


def test_signals_constant():
    assert SIGNALS == ("verbalized", "sc_margin", "ptrue", "negent")
    logger.info("test_signals_constant PASS")


if __name__ == "__main__":
    test_semantic_entropy()
    test_ct_baseline_plumbing()
    test_confident_wrong_semantics()
    test_signals_constant()
    logger.info("ALL TESTS PASS")
