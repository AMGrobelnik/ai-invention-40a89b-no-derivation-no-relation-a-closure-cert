#!/usr/bin/env python3
"""$0 unit tests + the reproduction-gate go/no-go (no LLM calls)."""
from __future__ import annotations

import json
import numpy as np

import method as M
from stats import matched_coverage_mask, selective_accuracy
from llm import OpenRouterClient


def test_parsers():
    assert M.parse_verifier('{"related":"RELATED","confidence":0.9}') == (True, 0.9)
    assert M.parse_verifier('{"related":"UNRELATED","confidence":0.8}') == (False, 0.8)
    r, c = M.parse_verifier("garbage no json but UNRELATED here")
    assert r is False
    r, c = M.parse_verifier("")
    assert r is None and c == 0.5
    assert M.parse_selfverify('{"verdict":"TRUE","confidence":0.7}') == (True, 0.7)
    assert M.parse_selfverify('```json\n{"verdict":"FALSE","confidence":0.6}\n```') == (False, 0.6)
    # clip
    assert M.clip01(1.7) == 1.0 and M.clip01(-2) == 0.0 and M.clip01("x") == 0.5
    print("test_parsers OK")


def test_matched_coverage():
    conf = np.array([0.9, 0.8, 0.7, 0.6, 0.5])
    m = matched_coverage_mask(conf, 0.6)  # ceil/round(0.6*5)=3
    assert m.sum() == 3 and m[0] and m[1] and m[2]
    correct = np.array([1.0, 1.0, 1.0, 0.0, 0.0])
    assert selective_accuracy(correct, m) == 1.0
    print("test_matched_coverage OK")


def test_primitive_key():
    rec_p = {"scoring": "primitive"}
    assert M.primitive_key(rec_p, "grandfather") == "inv-grand"
    assert M.primitive_key(rec_p, "grandson") == "grand"
    assert M.primitive_key(rec_p, "ABSTAIN") is None
    rec_s = {"scoring": "surface"}
    assert M.primitive_key(rec_s, "grandson") == "grandson"
    assert M.primitive_key(rec_s, "no-relation") is None
    print("test_primitive_key OK")


def test_named_of():
    assert M.named_of("grandson") and not M.named_of("ABSTAIN")
    assert not M.named_of("no-relation") and not M.named_of(None)
    print("test_named_of OK")


def test_cache_keying_distinct():
    """Verifier prompts must not collide with the battery cache (different system/tag)."""
    c = OpenRouterClient("k", "m", [], M.HERE / "cache")
    k1 = c._key(M.VERIFIER_SYS, "u", 0.0, "verifier")
    k2 = c._key(M.SELFVERIFY_SYS, "u", 0.0, "selfverify")
    assert k1 != k2
    print("test_cache_keying_distinct OK")


def test_reproduction_gate():
    """The decisive $0 go/no-go: must reproduce FACT-A / certificate leaderboard / crux exactly."""
    clutrr_recs, clutrr_md = M.load_pool(M.CLUTRR_POOL, "clutrr")
    redoc_recs, redoc_md = M.load_pool(M.REDOCRED_POOL, "redocred")
    all_recs = clutrr_recs + redoc_recs
    M.build_order_and_text(all_recs)
    for r in all_recs:
        M.build_base_methods(r)
    gate, all_ok = M.reproduction_gate(clutrr_recs, clutrr_md, redoc_recs, redoc_md)
    fails = [c for c in gate["checks"] if not c["ok"]]
    for c in fails:
        print(f"  FAIL {c['name']}: recomputed={c['recomputed']} carried={c['carried']} published={c['published']}")
    print(f"reproduction gate: {gate['n_passed']}/{gate['n_checks']} passed; all_ok={all_ok}")
    assert all_ok, f"{len(fails)} gate checks failed"
    print("test_reproduction_gate OK")


if __name__ == "__main__":
    test_parsers()
    test_matched_coverage()
    test_primitive_key()
    test_named_of()
    test_cache_keying_distinct()
    test_reproduction_gate()
    print("\nALL TESTS PASSED")
