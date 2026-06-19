# iter-10 eval digest — $0 re-analysis scaffold (stronger-verifier rigor fix + 4 MINOR fixes)

**Reproduction / no-spend gate:** 87/87 HARD checks PASSED (all_ok=True); 5/5 soft MC cross-checks within tol. Budget $0, 0 LLM calls.

## BLOCK 1 — RIGOR MAJOR

### Table~\ref{tab:stronger-verifier} (stronger cross-family verifier, OWN n=60 subsample)

```latex
% Table~\ref{tab:stronger-verifier} — stronger cross-family verifier on its OWN n=60 subsample
\begin{tabular}{lcc}
\toprule
method (deepseek-v3.2, $k{=}5$; $n_{\text{sibling}}{=}250$, 60 fabrications) & frac.\ caught & nat.\ conf-wrong \\
\midrule
\textbf{certificate (no-derivation)} & \textbf{0.667} & 0.096 \\
self-verification (strong) & 0.533 & 0.112 \\
query-side verifier (weak, same-model) & 0.200 & 0.192 \\
query-side verifier (strong, x-family) & 0.100 & 0.216 \\
\bottomrule
\end{tabular}
```

> a STRONGER, larger, different-family verifier is NO BETTER (in fact WORSE: a better geographer over-infers co-regional containment); both verifiers sit far below the certificate -> certificate-necessity is intrinsic to running the premise check on a generative LLM, not an artifact of a weak same-model verifier (retires methodology MINOR #5)

### Table~\ref{tab:locatedin} (CORRECTED — n_sibling=450 / 135 fab.; 0.100 row REMOVED)

```latex
% Table~\ref{tab:locatedin} — CORRECTED caught-fraction (n_sibling=450, 135 fabrications; identical denom.)
% NOTE: the stronger x-family verifier 0.100 is DELIBERATELY ABSENT — see footnote / Table~\ref{tab:stronger-verifier}.
\begin{tabular}{lccc}
\toprule
method & frac.\ caught & cert$-$method gap & 95\% CI \\
\midrule
\textbf{certificate (no-derivation)} & \textbf{0.785} & -- & -- \\
verbalized confidence & 0.400 & 0.385 & [0.244, 0.520] \\
Kadavath P(True) & 0.304 & 0.481 & [0.365, 0.596] \\
self-consistency margin & 0.067 & 0.719 & [0.632, 0.800] \\
semantic-entropy & 0.067 & 0.719 & [0.632, 0.800] \\
query-side verifier (same-model) & 0.274 & 0.511 & [0.399, 0.620] \\
self-verification & 0.459 & 0.326 & [0.207, 0.442] \\
\bottomrule
\end{tabular}
```

**Footnote:** The stronger cross-family verifier (deepseek-v3.2, k=5) is reported on its OWN n=60 subsample in Table~\ref{tab:stronger-verifier}; its 0.10 caught fraction is computed on a different denominator (n_sibling=250, 60 fabrications) and is NOT comparable to this column.

All six cert-minus-method caught-gaps exclude 0: True. rigor_major_retired = True.

## BLOCK 2 — EVIDENCE MINOR (0.785 always paired with the caveat)

**abstract.** On a non-by-construction natural same-component-sibling regime the no-derivation certificate catches 0.785 of the raw reader's high-confidence absent-relation fabrications versus 0.274 for the strongest query-side verifier and <=0.40 for every confidence signal (all six certificate-minus-competitor caught-gaps exclude 0); we report this as TARGETING QUALITY, not a deployment win — the catching objective on a pure-absent pool structurally favors high-abstention methods (it measures only how well a method's abstentions target the fabrications), and the certificate's NET utility on mixed present/absent natural prose remains extraction-gated.

**intro.** Our headline safety number is a TARGETING-QUALITY result, not a deployment win: the certificate turns 0.785 of the raw reader's high-confidence sibling fabrications into abstentions (vs 0.274 for the strongest query-side verifier), but because this catching objective is scored on a pure-absent pool it structurally favors methods that abstain more on absent pairs, and the certificate's NET utility on mixed present/absent natural prose stays extraction-gated.

**contribution_3.** Third, we isolate a one-sided catching win as TARGETING QUALITY rather than a deployment win: on the natural sibling-absent pool the certificate catches 0.785 of the raw fabrications against 0.274 for the strongest query-side verifier, while acknowledging that the pure-absent catching objective structurally rewards high-abstention methods and that the net mixed-pool utility remains extraction-gated.

**conclusion.** In sum the certificate catches 0.785 of the confident absent-relation fabrications versus 0.274 for the strongest query-side verifier, a TARGETING-QUALITY win and not a deployment win — the catching objective on a pure-absent pool structurally favors high-abstention methods, so the certificate's NET deployable utility on mixed natural prose remains extraction-gated until a precision-preserving extractor lifts present coverage.

evidence_minor_retired = True (per-sentence both-clauses: {'abstract': True, 'intro': True, 'contribution_3': True, 'conclusion': True}).

## BLOCK 3 — PRESENTATION MINOR

**De-densification checklist:**

- [1] Evidence-class tags (REAL-LLM-READ, GOLD-ONLY-GATE, SYNTHETIC-CHANNEL, THEOREM, REAL-LLM-READ-ON-SYNTHETIC) appear ONLY in the spine table + section headers; DELETE every inline \textsc{...} marker in results prose.
- [2] Rewrite reviewer-response meta-narration as declarative claims-with-caveats — replace 'a skeptical reviewer rightly observed...', 'stated without spin', 'we never let that number carry the contribution' with plain assertions of the caveated claim.
- [3] Collapse the 7 bold-headed intro paragraphs into <=3 so the contributions list + headline numbers (FACT A rate; capability gap; caught 0.785) appear within the first ~half page.
- [4] Flag duplicated / near-duplicate consecutive sentences and any '...'-truncated fragments.
- [5] Every selective-accuracy / confident-wrong number must carry its coverage/abstention qualifier.

**Lean intro skeleton (<=3 blocks):**

- **Block 1 (problem + thesis):**
  - (a) PROBLEM: confident absent-relation hallucination as a compositional false-premise failure in the deduction sub-module of a text->FOL pipeline.
  - (b) THESIS (one sentence): a high-recall disjunctive reader + compose-through-exact-table + abstain-on-no-derivation; the certificate MECHANISM is the INHERITED NeSy premise (+0.673 inherited / +0.0025 novel).
- **Block 2 (three contributions + headline numbers):**
  - (c1) a corpus/domain/reader-robust DIAGNOSTIC = FACT A (confident absent-fabrication rate 0.30 sibling / 0.06 diffcomponent, transfers across readers+corpora) + a signal-agnostic capability gap.
  - (c2) a one-sided TARGETING-QUALITY catching win (caught 0.785) that beats the confidence family (<=0.40) AND the same-model verifier (0.274) AND the stronger cross-family verifier (0.10 on its own n=60 subsample).
  - (c3) a QUANTIFIED recall-precision frontier proving the natural-prose net-utility boundary is FUNDAMENTAL for prompt-only extraction (slope -0.30 located-in / -0.67 kinship; gold-read ceiling 1.0/1.0/1.0).
- **Block 3 (scope + venue):**
  - (d) OUT-OF-SCOPE (stated in the intro, not the appendix): OpenCyc grounding, atomic re-extraction, general fuzzy unification, genuine ~3000-char documents = future work.
  - (e) VENUE: ACL Knowledge Extraction PRIMARY, NeSy fallback.

## BLOCK 4 — SCOPE MINOR (single feasibility appendix)

**Appendix A — Feasibility on commodity hardware (NOT a substantive contribution)** — Both notes below are FEASIBILITY demonstrations on commodity hardware, NOT substantive contributions; the substantive contributions are the diagnostic, the targeting-quality catching win, and the recall-precision frontier (intro).

- **A.1 Operational ~3000-char bracket-selected case study:** 95 Prolog programs discharged & executed in swipl 9.0.4; hallucination reduction 0.27-0.60 (mean 0.45) at Mode-A coverage 0-0.33; atomic recall ~0.49 is the binding ceiling. CUT the concatenated-kinship arm (56/56 cross-story abstentions are trivial by construction). LABEL the documents bracket-selected. STATE: the pipeline RUNS at length, NOT that it is USEFUL at length.

- **A.2 Fuzzy-unification feasibility note:** vague prepositions / informal kinship -> calibrated sub-1.0 disjunctions; fraction-at-1.0 0.00 vs Mode-P 1.00; per-candidate ECE 0.142 spatial / 0.111 kinship; Mode-B catches around->{NTPPi,TPPi} 5/5 sound-violating spatial reads (kinship UNTESTED). Supporting query-level cert confident-wrong 0.000 vs commit-argmax 0.364/0.216 WITH the query-vs-edge unit-of-analysis caveat.

Out-of-scope statement stays in: INTRO (not the appendix).

## BLOCK 5 — NOVELTY MINOR slot

`NOVELTY-DISTINGUISHING-SENTENCE (filled by parallel research artifact)` — one sentence separating the no-derivation certificate (per-query, gold-free, training-free, NO-external-KB abstention from deductive closure over the document-INTERNAL relation graph) from ontology-grounded POST-EXTRACTION structural CORRECTION (e.g. arXiv:2605.29168), which repairs/commits a labeling against EXTERNAL ontology structure — preserving the gold-free / training-free / no-external-KB delta

Placeholder: `<<FILL: no-derivation certificate vs ontology-grounded post-extraction correction — verified content from the parallel research artifact>>` (status: PENDING-PARALLEL-RESEARCH-ARTIFACT).

## BLOCK 6 — SIGNIFICANCE

**FORK_A (demonstrated fix):** ... + a DEMONSTRATED net-utility fix on natural prose via a PRECISION-PRESERVING extractor: on a mixed present / same-component-sibling-absent pool the certificate's Holm-adjusted, doc-clustered mixed-pool confident-wrong reduction CI EXCLUDES 0 at extraction recall R*, matching/beating the query-side verifier ...

**FORK_B (honest boundary):** ... + a targeting-quality catching win (caught-fraction cert 0.785 vs verifier 0.274, extraction-gated, not a deployment win) + a net-utility boundary shown FUNDAMENTAL even for precision-preserving extraction (deeper than prompt-only) ...

**Selection rule:** Use FORK_A IFF the parallel iter-10 precision-preserving-extractor experiment flips the mixed-pool confident-wrong reduction CI to EXCLUDE 0 on a natural (non-structural-by-construction) regime AND the certificate matches/beats the query-side verifier; otherwise use FORK_B. GEN_PAPER_TEXT reads the extractor experiment verdict and selects.


### contribution table (one thesis)

| contribution | status |
|---|---|
| ROBUST DIAGNOSTIC (FACT A + signal-agnostic mixed-pool capability gap) | ESTABLISHED [REAL-LLM-READ] |
| TARGETING-QUALITY CATCHING WIN (0.785, one-sided, extraction-gated; beats confidence family + same-model + stronger x-family verifier) | ESTABLISHED-BUT-ONE-SIDED [RE-ANALYSIS-DERIVED] |
| RECALL-PRECISION FRONTIER (prompt-only natural-prose net-utility boundary FUNDAMENTAL; slope -0.30/-0.67, gold-read ceiling 1.0/1.0/1.0) | ESTABLISHED [REAL-LLM-READ] |
| certificate MECHANISM (forward least-fixpoint closure -> abstain) | INHERITED NeSy premise (+0.673 inherited / +0.0025 novel) [INHERITED-NESY-PREMISE] |
| DEMONSTRATED-FIX-OR-DEEPER-BOUNDARY (net mixed-pool reduction CI excluding 0 on a natural regime via precision-preserving extraction, OR the boundary shown fundamental even there) | PENDING-EXTRACTOR-EXPERIMENT (FORK) [PENDING-PARALLEL-EXPERIMENT] |

## Caught-fraction leaderboard (located-in sibling fabrications, n=135)

| method | fraction caught |
|---|---|
| certificate | 0.7852 |
| ct_verbalized | 0.4 |
| ct_ptrue | 0.3037 |
| ct_sc_margin | 0.0667 |
| ct_negent | 0.0667 |
| queryside_verifier | 0.2741 |
| queryside_selfverify | 0.4593 |

## 16-cell capability-gap table (survival / caught per signal)

| corpus | reader | tag | verbalized | sc_margin | ptrue | negent |
|---|---|---|---|---|---|---|
| Re-DocRED | gemini | REPRODUCED-FROM-ROWS (S2) | 0.5083/0.4917 | 0.85/0.15 | 0.4833/0.5167 | 0.85/0.15 |
| Re-DocRED | deepseek | CARRIED-LITERAL | 0.4118/0.5882 | 0.2941/0.7059 | 0.3235/0.6765 | 0.2941/0.7059 |
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
  "explanation": "the 476/476 present and 577/577 absent engine round-trip is the COMBINED re-docred (360/368) + docred (116/209, whose absent gold is downgraded ~64.6% false-negatives); removes the apparent 360!=476 / 368!=577 inconsistency",
  "evidence_tag": "CARRIED-LITERAL (present/absent 360/368 + docred_present 116 reproduced from S2 rows)"
 },
 "locatedin": {
  "present": 515,
  "same_component_sibling_absent": 450,
  "different_component_absent": 250,
  "never_annotated": 115,
  "held_out": 400,
  "n_docs": 283,
  "note": "present 515 = held_out 400 + never_annotated 115",
  "evidence_tag": "REPRODUCED-FROM-ROWS"
 },
 "evidence_tag": "REPRODUCED-FROM-ROWS / CARRIED-LITERAL"
}
```
