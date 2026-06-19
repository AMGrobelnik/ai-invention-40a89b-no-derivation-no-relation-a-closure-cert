# iter-8 experiment_2 — Query-side false-premise verifier vs the no-derivation certificate

**The reviewer-mandated DISCONFIRM test.** The closure-certificate paper claims its
hallucination-safety on the *absent-relation* stratum is a STRUCTURAL property (no derivation
path ⇒ abstain), not a re-skin of an uncertainty signal. A reviewer asked the sharpest
disconfirming question: *could a cheap query-side false-premise VERIFIER — just asking the LLM
"are X and Y related at all?" — recover the same abstention without the closure engine?* If yes,
the certificate is not strictly needed (honest negative). This artifact answers it.

## What it does (reuse-heavy, <$1 new spend)

It loads the two EXISTING, fully-cached prediction pools by direct filesystem read —
* **CLUTRR battery** (`iter_6/gen_art/gen_art_experiment_1`, templated kinship, gemini reader)
* **Re-DocRED battery** (`iter_7/gen_art/gen_art_experiment_1`, natural Wikipedia kinship, gemini reader)

— and the certificate / raw / 4-signal-battery predictions ALREADY in them, then adds **two new
baselines** built from the reviewer's ask:

1. **Query-side false-premise verifier** (corrective gate): for every (story, pair) ask
   *"Are X and Y related by family/kinship at all?"* → if UNRELATED, answer `no-relation`; else keep
   the raw answer. (also a pure-abstention-signal sensitivity framing.)
2. **Self-verification**: *"Is it true that Y is X's ⟨raw answer⟩?"* → keep iff TRUE.

Reader-matched gemini-3.1-flash-lite, sha256-cached, hard-$9-capped (`llm.py`). Total new spend
**$0.14** (one billed run; re-runs replay at $0 from `./cache`).

## The $0 reproduction gate (go/no-go before any spend)

Phase 2 re-derives the published literals from the carried row fields and asserts they match each
pool's own aggregates AND the published constants — **32/32 checks pass, $0**:
FACT-A absent-hallucination rate (CLUTRR 0.472 gemini / 0.483 deepseek; Re-DocRED 0.326 / 0.318),
certificate confident-wrong-on-absent, the mixed-pool matched-coverage **certificate** selective
accuracy (0.8267 / 0.475), **every** confidence-signal mixed selective accuracy
(0.4133/0.3733/0.44/0.3733 and 0.675/0.6/0.645/0.6), and the crux survival fractions — all exact.
The tie-break-sensitive signal selaccs reproduce byte-exactly only after the source record ORDER is
reconstructed (CLUTRR ← iter-3 row order; Re-DocRED ← dataset doc order); the certificate/FACT-A/crux
numbers are order-independent. A structural mismatch is a hard stop (no spend); the gate passed.

## Headline result — `CERTIFICATE_NECESSARY_BOTH_VENUES`

On the absent-relation **fabrication set** (raw LLM confidently committed a kinship on a
different-component pair), fraction CAUGHT (method abstains / says `no-relation`):

| venue | certificate | query-side verifier | self-verify | best dispersion signal |
|---|---|---|---|---|
| CLUTRR (n=85)  | **0.941** | 0.588 | 0.824 | P(True) 0.753 |
| Re-DocRED (n=120) | **0.850** | **0.100** | 0.542 | P(True) 0.517 |

The structural certificate catches **strictly more** confident absent-relation hallucinations than
the query-side verifier on BOTH venues (doc-clustered paired bootstrap B=10000, gap CI excludes 0,
p≈0). **Why the verifier fails:** it is built on the *same* LLM that produced the hallucination, so
when the reader confidently invents "Y is X's sister", asking "are X and Y related?" returns RELATED
(p=1.0) — the verifier inherits the generation error. The certificate's abstention is independent of
the LLM's confidence. Self-verify is intermediate but still significantly below the certificate.

**Honest boundary (reported, not hidden):** on Re-DocRED *mixed-pool selective accuracy* the
certificate ties/loses (0.475 vs verifier 0.595 / signals 0.60–0.675) because natural-prose
extraction recall makes it OVER-ABSTAIN on PRESENT pairs (the iter-7 extraction-limited finding).
The necessity verdict is therefore scoped to the **hallucination-catching** objective (the paper's
safety claim), where the certificate dominates; the mixed selective-accuracy view is emitted
alongside so the contribution is not over-claimed.

## Reader scope (honest)

Both cached pools carry per-row predictions from the **gemini** reader only (deepseek is
aggregate-only). The verifier is therefore reader-matched to gemini; deepseek FACT-A is reproduced
from each pool's carried cross-family aggregate (gate checks). A deepseek-verifier robustness arm is
available behind `--no-deepseek-sensitivity` (default disabled in the final artifact to keep it
focused on the load-bearing reader-matched comparison).

## Files / reproduce

```bash
uv run tests.py            # $0 unit tests + the 32/32 reproduction gate (no LLM calls)
uv run method.py           # full run; cached reads replay $0, verifier billed once (~$0.14)
```

`method.py` (orchestrator), `tests.py`; reused VERBATIM: `llm.py`, `stats.py`, `baselines.py`,
`kinship.py`, `clutrr_composition_table.json`. Output `method_out.json` (`exp_gen_sol_out`, validated)
+ `full_/mini_/preview_` variants: per-query `predict_certificate / predict_conf_thresh_* /
predict_commit_argmax / predict_queryside_verifier / predict_queryside_selfverify /
predict_verifier_as_signal` (all strings) + gold + rich metadata; `metadata` carries the reproduction
gate, per-venue matched-coverage leaderboards, fraction-caught crux tables, and the certificate-necessity
verdict. `cache/` is sha256 content-addressed and excluded from the repo.
