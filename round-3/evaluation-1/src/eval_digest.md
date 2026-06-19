# Evaluation digest - decomposition / risk-coverage / multiplicity

Pure re-analysis of three iter-2 experiments. **LLM spend: $0.00.**

## TASK 1 - Decomposition of the system gap

Do NOT present the +0.676 Allen Mode-A-vs-PoT gap as a single iteration win. It DECOMPOSES additively into an INHERITED exact-table-vs-LLM-composition component (~+0.673, the standard neuro-symbolic premise that an LLM composes 13-relation Allen poorly: PoT 0.308 vs exact-table naive 0.981) and a NOVEL iteration component that is ~0 on the selective-accuracy axis but lives on the COVERAGE axis (full PC resolves L>=3 / cyclic queries naive single-pass cannot reach).

| algebra | pool | system_gap | inherited (exact-table-vs-LLM) | novel_selacc | additivity_resid |
|---|---|---|---|---|---|
| point | bite_bearing | 0.0426 | 0.0426 | 0.0000 | 0.0000 |
| point | all_comparison | 0.0554 | 0.0554 | 0.0000 | 0.0000 |
| allen | bite_bearing | 0.6760 | 0.6735 | 0.0025 | 0.0000 |
| allen | all_comparison | 0.6757 | 0.6721 | 0.0036 | 0.0000 |

**Coverage axis (the iteration novelty's true home):** full-minus-naive resolve-to-correct gap by hop bin.

| algebra | L2 | L3 | L4 | L5 |
|---|---|---|---|---|
| point | 0.000 | 0.344 | 0.033 | 0.022 |
| allen | 0.000 | 0.144 | 0.044 | 0.000 |

On the matched-coverage selective-accuracy axis the +0.676 (Allen) / +0.043 (point) is almost entirely INHERITED; iteration adds ~0 selective accuracy in the length-2-dominated bite pool (novel_selacc ~ +0.0025 Allen / 0.0 point).

The genuine iteration novelty is a COVERAGE gain at maintained selective accuracy on long-hop/cyclic queries: full-minus-naive resolve-to-correct gap +0.344 (point) / +0.144 (Allen) at L=3, growing with hop and cyclomatic number, a verified exact TIE at length-2.

Corrected Page-p note: ~5e-4 order (Jonckheere trend on the lower-recall slice; per-slice Page p ~1e-3..1e-1, Jonckheere p down to ~1e-118 at high recall). The paper's earlier '1e-13' was a mis-statement.

## TASK 2 - Risk-coverage (real text)

Mode-A drives confident-wrong from 0.65 (raw) to 0.0, but at ~90% abstention (answered 2/20). Reported as a risk-coverage operating point: a near-zero confident-wrong rate in isolation is trivial; at MATCHED coverage 0.10 the advantage over raw/PoT/SC is not significant at n=20. Every hallucination number is paired with its coverage/abstention rate.

- Mode-A operating point: coverage **0.10** (answered 2/20), selective accuracy 1.00, confident-wrong 0.00, abstention **0.90**.
- Raw LLM: coverage 1.00, accuracy 0.35, confident-wrong 0.65.
- AUC risk-coverage (n=20, underpowered): modeA 1.000, naive 1.000, pot 0.647, raw 0.549, sc 0.520.
- (i) The 0.65->0.0 confident-wrong reduction is achieved at ~90% abstention (Mode-A answered only 2/20 queries), so a near-zero confident-wrong rate IN ISOLATION is trivial.
- (ii) The FAIR metric is selective accuracy at MATCHED coverage.
- (iii) At matched coverage 0.10 the Mode-A advantage over raw/PoT/SC is NOT statistically significant at n=20 (boot p: vs raw 0.394, vs PoT 0.254, vs SC 0.175); the gap CIs are [0,1] (underpowered).

**Read-soundness caveat:** Real-text read-soundness remains UNRESOLVED at this n: NT primary recall 0.743 (n=74) is below the 0.90 gate; the stronger reader reaches 0.897 (n=39) with CI [0.667,1.0] that merely CONTAINS 0.90; TDDMan 0.902 (n=41) with CI crossing the gate. The risk-coverage win therefore cannot yet be claimed on real text.

## TASK 3 - Multiplicity policy

Confirmatory family {H1,H2,H3,H4} under Holm-Bonferroni with H1/H2 gateways: H2 (hallucination) CLEARS coverage-conditionally, H3/H4 CONFIRMED on synthetic, H1 (real-text transfer) FAILS; all stratum/audit/reliability analyses are EXPLORATORY.

| H | evidence class | raw p | reject | gateway | gate status |
|---|---|---|---|---|---|
| H1 | REAL-LLM-READ (gateway) | 0.2545 | False | True | FAILS (p=0.254); real-text comparative advantage UNESTABLISHED at n=20 |
| H2 | REAL-LLM-READ (gateway) | 0.0000 | True | True | CLEARS at Holm threshold 0.0167; MUST be reported WITH the ~90% abstention caveat (coverage-conditional; NOT significant at matched coverage) |
| H3 | SYNTHETIC-CHANNEL (primary); real-text stratum EXPLORATORY | 0.0036 | True | False | PASS on synthetic channel (gated behind gateway H2 which clears) |
| H4 | SYNTHETIC-CHANNEL | structural | True | False | gated-behind-gateway PASS (not forced into Holm; structural) |

**Gatekeeping:** Hierarchical gatekeeping: H1 and H2 are gateways; H3/H4 are confirmatory-valid only if >=1 gateway clears. Gateway H2 CLEARS (Holm-adjusted), so H3/H4 are confirmatory-valid. Gateway H1 (the real-text transfer gateway) FAILS. Therefore: hallucination-reduction is CONFIRMED-but-coverage-conditional (H2); iteration & redundancy are CONFIRMED on synthetic (H3/H4); real-text comparative advantage is OPEN NEGATIVE (H1).

**Conclusion by hypothesis:**
- **H1**: OPEN NEGATIVE - real-text comparative advantage unestablished (n=20, p=0.254).
- **H2**: CONFIRMED but COVERAGE-CONDITIONAL - confident-wrong reduction significant (Holm), but achieved at ~90% abstention; not significant at matched coverage.
- **H3**: CONFIRMED on SYNTHETIC channel - iteration coverage gap grows with hop & cyclomatic; real-text stratum exploratory/under-powered.
- **H4**: CONFIRMED on SYNTHETIC channel - redundancy inverted-U, peak shifts outward (structural criterion).

## Retired critiques

- MAJOR: 'central claim conflates two effects' -> retired by Task 1 additive decomposition (selacc axis = inherited; coverage axis = novel).
- MINOR: 'hallucination driven by abstention' -> retired by Task 2 risk-coverage framing (every number paired with ~90% abstention; matched-coverage gap not significant at n=20).

## Sanity checks

Discrepancies vs source values: **0**.
