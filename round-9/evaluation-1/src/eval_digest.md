# Eval digest — zero-spend re-analysis (caught-fraction headline)

**Reproduction gate:** 68/68 hard checks PASSED (all_ok=True); 5/5 soft MC cross-checks within tol.

## Caught-fraction leaderboard (located-in sibling fabrications, n=135) — THE headline

| method | fraction caught |
|---|---|
| certificate | 0.7852 |
| ct_verbalized | 0.4 |
| ct_sc_margin | 0.0667 |
| ct_ptrue | 0.3037 |
| ct_negent | 0.0667 |
| queryside_verifier | 0.2741 |
| queryside_selfverify | 0.4593 |

NEW doc-clustered paired-bootstrap gaps excluding 0: ['ct_verbalized', 'ct_sc_margin', 'ct_ptrue', 'ct_negent', 'queryside_verifier', 'queryside_selfverify']

## Pure-absent identity (rigor MAJOR)

On a PURE-ABSENT pool there are no present pairs to cover, so each method's 'coverage' degenerates to its named-rate, which equals its confident-wrong rate (any named answer on an absent pair is wrong). Therefore the view1_absent '0.2267 reduction at matched coverage / meets the 0.20 bar' is NOT a risk-coverage selective-accuracy gain; it is exactly (signal named-rate 0.30 - certificate named-rate 0.0733) = a coverage/abstention-rate difference, i.e. a re-expression of the caught-fraction gap.

## Load-bearing natural confident-wrong

certificate 0.0733 vs raw/all-dispersion 0.30 vs verifier 0.2178 vs self-verify 0.1622

## 16-cell capability-gap table (survival / caught per signal)

| corpus | reader | tag | verbalized | sc_margin | ptrue | negent |
|---|---|---|---|---|---|---|
| Re-DocRED | gemini | REPRODUCED-FROM-ROWS | 0.5083/0.4917 | 0.85/0.15 | 0.4833/0.5167 | 0.85/0.15 |
| Re-DocRED | deepseek | CARRIED-NOT-REPRODUCED | 0.4118/0.5882 | 0.2941/0.7059 | 0.3235/0.6765 | 0.2941/0.7059 |
| CLUTRR | gemini | CARRIED-LITERAL | 0.4353/0.5647 | 0.7176/0.2824 | 0.2471/0.7529 | 0.7176/0.2824 |
| CLUTRR | deepseek | CARRIED-LITERAL | 0.672/0.328 | 0.224/0.776 | 0.103/0.897 | 0.224/0.776 |

*(cells are survival/caught)*

## Count reconciliation

```
{
 "kinship_redocred_primary_slice": {
  "present_multihop": 360,
  "present_composed_only_non_circular": 222,
  "absent": 368,
  "engine_round_trip_present_combined": 476,
  "engine_round_trip_absent_combined": 577,
  "docred_present": 116,
  "docred_absent": 209,
  "docred_absent_false_negative_frac": 0.646,
  "explanation": "the 476/476 present and 577/577 absent engine round-trip is the COMBINED re-docred (360/368) + docred (116/209, whose absent gold is downgraded ~64.6% false-negatives); removes the apparent 360!=476 / 368!=577 inconsistency"
 },
 "locatedin": {
  "present": 515,
  "same_component_sibling_absent": 450,
  "different_component_absent": 250,
  "never_annotated": 115,
  "held_out": 400,
  "n_docs": 283,
  "note": "present 515 = held_out 400 + never_annotated 115"
 },
 "evidence_tag": "REPRODUCED-FROM-ROWS"
}
```

## Seven paper-facing blocks

### located-in results (CORRECTED: caught-fraction as the matched-coverage headline)

On 450 natural Wikipedia same-component-sibling absent located-in pairs, the raw reader confidently fabricates a containment on **30%** [FACT-A; REAL-LLM-READ]. Of those 135 high-confidence fabrications, the fraction each method turns into an abstention (matched-coverage-fair: identical denominator) is:

| method | fraction caught |
|---|---|
| **certificate (no-derivation)** | **0.785** |
| verbalized confidence | 0.400 |
| self-consistency margin | 0.067 |
| Kadavath P(True) | 0.304 |
| semantic-entropy | 0.067 |
| query-side false-premise verifier | 0.274 |
| self-verification | 0.459 |

Natural confident-wrong on the sibling pool: certificate **0.073** vs raw/all-dispersion-signals **0.30** vs verifier 0.218 vs self-verify 0.162 [REAL-LLM-READ/NATURAL-PROSE]. DELETE the sentence '0.227 confident-wrong reduction at matched coverage / meets the 0.20 bar'. RELABEL alternative (if kept): 'the certificate at its abstaining operating point (0.073) vs each signal at its natural operating point (0.30) on the pure-absent pool, where coverage==confident-wrong by construction'. CAVEAT: on a pure-absent pool confident-wrong == coverage for every method, so the 0.227 number is mechanically (0.30 - 0.073), not a risk-coverage gain [RE-ANALYSIS-DERIVED].

### sec:boundary (regenerated CLEAN from intended numbers only)

The certificate's NET utility is extraction-limited on natural prose. On Re-DocRED kinship the mixed-pool confident-wrong reductions of the certificate vs the four dispersion signals are -0.055 / -0.034 / -0.047 / -0.034, with doc-clustered bootstrap CIs ALL including 0 and Holm rejecting none [REAL-LLM-READ]. On located-in, the certificate's present coverage is 0.05 at atomic extraction recall 0.148 (best-effort 0.186) [REAL-LLM-READ]. The gold-read ceiling is 1.0 present coverage / 1.0 absent abstention / 1.0 present selective accuracy [GOLD-READ-CEILING], isolating EXTRACTION (not closure) as the binding constraint. On the absent stratum the certificate stays hallucination-safe: sibling confident-wrong 0.073 [REAL-LLM-READ/NATURAL-PROSE]. (See the end-to-end proofread checklist in the eval metadata before assembling the draft.)

### sibling-regime decisiveness (restated via fabrication prevalence)

The same-component-sibling regime is the decisive one because the raw reader fabricates a containment on 30% of sibling-absent pairs vs only 6% of different-component pairs [REAL-LLM-READ]; the prevalence makes the sibling pool the hard test. The relatedness verifier is FOOLED by shared-parent structure — it inherits the reader's confidence and catches only 0.274 — because both endpoints share a containing parent and the reader confidently asserts a relation. The certificate's abstention is still a structural no-derivation determination, but a NON-TRIVIAL one: it requires the composition table (located_in o contains is UNDEFINED), NOT mere disconnection (that is the different-component contrast). [REAL-LLM-READ/NATURAL-PROSE]

### fuzzy-unification feasibility note (supporting, not a contribution)

Fuzzy unification is demoted to a feasibility note: an LLM probabilistic-unification arm emits calibrated sub-1.0 disjunctions (fraction-at-1.0 0.00 vs Mode-P 1.00; per-candidate ECE 0.142 spatial / 0.111 kinship; Mode-B catches 5/5 sound-violating spatial reads) — supporting evidence for feasibility on commodity hardware, not a substantive contribution. [SYNTHETIC/SUPPORTING]

### verifier-scope block (methodology)

We scope the necessity claim precisely to **a same-model prompt-based query-side verifier**: a recognized prompt-based instantiation of the false-premise / unanswerable-question abstention approach (FalseQA / AbstentionBench / Wen2024). It catches only 0.274 of sibling fabrications (located-in) and 0.10 / 0.588 (Re-DocRED / CLUTRR) because it runs on the SAME LLM that hallucinated and inherits the generation error. PENDING SLOT (filled by the parallel iter-9 extraction experiment's methodology-MINOR arm): a STRONGER cross-model verifier — a larger / different-family judge with relatedness + self-verify at k=5 — to test whether cross-model verification narrows the gap. [REAL-LLM-READ; PENDING-PARALLEL-EXPERIMENT]

### contribution table (one thesis)

| contribution | status |
|---|---|
| ROBUST DIAGNOSTIC: FACT A (confident absent-fabrication rate, corpus+reader transferable) + the signal-agnostic mixed-pool capability gap | candidate NOVELTY [REAL-LLM-READ] |
| certificate MECHANISM (forward least-fixpoint closure -> abstain) | inherited NeSy premise (+0.673 inherited / +0.0025 novel) [INHERITED-NESY-PREMISE] |
| caught-fraction dominance over the confidence battery AND the query-side verifier | the SAFETY result (certificate 0.785 vs verifier 0.274) [RE-ANALYSIS-DERIVED] |
| DEMONSTRATED-FIX-PENDING: net mixed-pool confident-wrong reduction excluding 0 off the structural-by-construction stratum | reserved for the parallel extraction-recall experiment [PENDING-PARALLEL-EXPERIMENT] |

### abstract_first_results_sentence_FORK

**FORK-A:** On natural prose the closure certificate reduces confident-relation hallucinations at matched coverage by a margin whose doc-clustered CI excludes 0 on a non-structural-by-construction regime, while a same-model query-side verifier does not (caught-fraction 0.785 vs 0.274).

**FORK-B:** The certificate's NET utility is demonstrated only on clean/templated graphs; the natural-prose contribution is the catching-objective win (caught-fraction cert 0.785 vs verifier 0.274) plus a quantified extraction boundary.

**Selection rule:** Use FORK-A IFF the parallel iter-9 extraction experiment flips the mixed-pool confident-wrong reduction CI to EXCLUDE 0 on a natural (non-structural-by-construction) regime; otherwise use FORK-B. GEN_PAPER_TEXT selects deterministically from that experiment's verdict field.

## sec:boundary proofread checklist

- [ ] FLAG duplicated sentences (identical or near-identical consecutive sentences).
- [ ] FLAG truncated '...' fragments or sentences ending mid-clause.
- [ ] FLAG any number reported WITHOUT a coverage/abstention qualifier (every selective-accuracy / confident-wrong number must state its coverage or operating point).
- [ ] DOWNGRADE any 'family-level blindness' / 'entire confidence family is blind' phrasing to reader-dependent FACT B (verbalized robustly blind; dispersion signals catch the majority for deepseek).
- [ ] FLAG any 'natural' label applied to CLUTRR — CLUTRR is TEMPLATED; only Re-DocRED/located-in are natural prose.
- [ ] FLAG any claim that the certificate NET-WINS on natural prose — it does NOT (mixed-pool reduction is negative/degenerate; the natural win is the catching-objective + the quantified extraction boundary).
- [ ] VERIFY every cross-reference to sec:boundary resolves and is not stale.
- [ ] VERIFY the '0.227 reduction at matched coverage' sentence is DELETED or RELABELED per block (i).
- [ ] VERIFY the verifier is scoped to 'a same-model prompt-based query-side verifier' (not 'the' verifier).
- [ ] VERIFY FACT A rates (CLUTRR 47/48%, Re-DocRED 33/32%, located-in sibling 30%) and caught-fractions match the eval_out.json metadata literals exactly.