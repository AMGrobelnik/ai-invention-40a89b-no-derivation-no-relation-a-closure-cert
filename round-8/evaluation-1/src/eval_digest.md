# eval_iter8_dir4 — Signal-Agnostic Capability-Gap Pivot & 16-Cell Caught Scaffold

**$0 re-analysis.** numpy/json only; no LLM, no network. Seed 20260617, B=10000, TOL=0.001. Reproduction gate: **80/80 checks pass** (62 genuinely recomputed from per-query rows), reproduction_ok=**True**.

## 2. The 16-cell per-signal × reader × corpus SURVIVAL / CAUGHT table (centerpiece)

`caught = 1 − survival` (always recomputed). `survival` recomputed for gemini cells; carried (separate-reader spot-check) for deepseek cells.

| corpus | reader | FACT A | verbalized | sc_margin | ptrue | negent |
|---|---|---|---|---|---|---|
| clutrr | gemini | 0.4722 | 0.4353 / **0.5647** | 0.7176 / **0.2824** | 0.2471 / **0.7529** | 0.7176 / **0.2824** |
| clutrr | deepseek | 0.4833 | 0.6724 / **0.3276** | 0.2241 / **0.7759** | 0.1034 / **0.8966** | 0.2241 / **0.7759** |
| re-docred | gemini | 0.3261 | 0.5083 / **0.4917** | 0.85 / **0.15** | 0.4833 / **0.5167** | 0.85 / **0.15** |
| re-docred | deepseek | 0.3178 | 0.4118 / **0.5882** | 0.2941 / **0.7059** | 0.3235 / **0.6765** | 0.2941 / **0.7059** |

_(cell = survival / **caught**.)_

**FACT-A band row:** the four FACT-A rates (0.4722/0.4833/0.3261/0.3178) lie in a tight 0.32–0.48 band across BOTH corpora AND BOTH readers — the robust, transferable, non-circular content. FACT B (caught) is reader/signal-dependent: verbalized never reaches a strong majority caught; dispersion signals swing from ~15% (Re-DocRED/gemini) to ~90% (CLUTRR/deepseek).

## 3. The capability-gap SPINE (verbatim-ready)

> The load-bearing finding is a SIGNAL-AGNOSTIC MIXED-POOL CAPABILITY GAP, not a claim about any one confidence signal. On a mixed pool of answerable (present) and unanswerable (absent) relational queries, NO single confidence threshold can SIMULTANEOUSLY cover the present pairs and abstain on the absent pairs at matched coverage, because one scalar knob cannot separate 'confident-and-right (present)' from 'confident-and-wrong (absent)': the LLM emits both with the same high confidence (FACT A). A sound closure certificate separates them structurally -- it abstains exactly when no derivation path exists -- so it dominates every confidence threshold at matched coverage. This is a property of the DECISION GEOMETRY, so it survives the collapse of any per-signal blindness claim: it does not matter WHICH signal you pick. POWERED on clean templated CLUTRR: at matched coverage 0.266 the certificate's selective accuracy is 0.827 versus 0.413 / 0.373 / 0.440 / 0.373 for verbalized / sc-margin / P(True) / negentropy thresholds (~2x); the doc-clustered paired-bootstrap confident-wrong reductions are 0.110 / 0.121 / 0.103 / 0.121, every 95% CI excludes 0, and all four survive Holm correction (p_adj 0.0004 / 0.0027 / 0.0027 / 0.0027). We state plainly that the capability gap is currently POWERED ONLY on clean CLUTRR. On the natural Re-DocRED corpus it does NOT yet win: the confident-wrong reductions are slightly negative (-0.055 / -0.034 / -0.047 / -0.034), every CI includes 0, and Holm rejects none -- because natural-prose extraction recall is 0.376 and that is the binding constraint, not the certificate's logic. The gold-read ceiling (present coverage 1.0, correct-absent-abstention 1.0, present selective accuracy 1.0) isolates extraction, not closure, as the cause. PENDING: the parallel located-in same-component-sibling experiment lands the capability gap on a natural, NON-by-construction regime (iter-9), where abstention is a genuine deductive result rather than a disconnected-component artifact.

**Powered on CLUTRR:** certificate selacc 0.8267 vs signals 0.3733–0.44 at matched coverage 0.266; cw reductions [0.1099, 0.1206, 0.1028, 0.1206], all CIs exclude 0 = True, all Holm-rejected = True.

**Re-DocRED (PENDING / not yet won):** certificate selacc 0.475 vs best signal 0.675; cw reductions [-0.0549, -0.0343, -0.0467, -0.0343], all CIs include 0 = True, any Holm-rejected = False; binding constraint = extraction recall 0.3762 (gold-read ceiling 1.0/1.0/1.0 isolates extraction).

## 4. Definitional vs empirical (lead with empirical)

**Empirical (LEAD):** Empirical half (LEAD with this -- it is the measured, non-obvious part): how OFTEN does the LLM actually emit absent-relation fabrications at high confidence and low dispersion, and how strongly does that fraction vary by reader? Answer: FACT A puts the high-confidence fabrication rate in a tight 0.32-0.48 band across two corpora and two readers, while the fraction a dispersion threshold can catch swings from ~15% (Re-DocRED/gemini) to ~90% (CLUTRR/deepseek). Neither the rate nor its reader-variance is derivable a priori; both are the 16-cell table's contribution.

**Definitional (state once):** Definitional half (state ONCE, briefly, as the explanatory mechanism -- NOT a contribution): a high-confidence, self-consistent fabrication survives ANY dispersion threshold BY CONSTRUCTION. If the model commits an absent relation with maximal confidence and zero answer-dispersion, then no threshold tuned on that same dispersion can single it out -- this is true by definition of a dispersion signal and needs no experiment.

## 5. Softened-overclaim language

- The statement 'no confidence signal removes a single hallucination' holds ONLY at the LLM's NATURAL (no-abstention) operating point: at that coverage every named-on-absent answer is by definition wrong, so all four thresholded baselines coincide with the raw answerer and remove none. It is NOT a claim that confidence is useless at every coverage.
- At the CERTIFICATE's (lower) coverage the picture changes and we say so: a dispersion threshold tuned to the certificate's coverage already CATCHES a substantial share of the hallucinations. P(True) catches 75.3% on CLUTRR (1 - 0.247) and 51.7% on natural Re-DocRED prose (1 - 0.483) for the gemini reader. The certificate's advantage is that it catches them ALL via structural abstention, but the confidence signals are far from worthless once a non-natural coverage is permitted.
- DELETE the marginal '>=3 of 4 signals keep >=50%' / '>=2 of 4 commit >=50%' framing. It obscures the strong reader-dependence. Replace it with the per-cell caught fractions from the 16-cell table so the reader sees directly that the same signal swings from 15% to 90% caught depending on the reader.

**First-class numbers:** P(True) caught 0.7529 on CLUTRR / 0.5167 on natural Re-DocRED (gemini), evidence=REAL-LLM-READ.

## 6. Abstract front-matter (scope) + operational concatenated-kinship CUT

> This paper studies a closure-certified DEDUCTION SUB-MODULE -- a sound symbolic forward-closure over LLM-extracted relations that abstains rather than guess -- and explicitly NOT a full operational text-to-FOL umbrella pipeline; we name the umbrella components OUT OF SCOPE / FUTURE WORK THIS PAPER DOES NOT CLAIM in the first sentence so no reader mistakes the contribution. Out of scope and not claimed: (a) atomic / multi-hop fact EXTRACTION and re-extraction, which we MEASURE but do not improve (CLUTRR atomic precision/recall/F1 ~0.536 / 0.532 / 0.534; natural Re-DocRED recall 0.376, vs 0.465 against the locally-justifiable subset); (b) upper-ontology / OpenCyc grounding and taxonomic background knowledge; (c) reasoning over genuine ~3000-character professional documents -- no benchmark document we use reaches that length (CLUTRR <=871 chars; Re-DocRED Wikipedia intros average ~1020 chars, none family-bearing reach 3000), and the operational case study is bracket-selected, not naturally long; and (d) general open-vocabulary fuzzy unification -- our fuzzy contribution is scoped to disjunctions over a KNOWN base vocabulary (RCC-8 base relations; CLUTRR kinship primitives), not open-vocabulary predicate invention. We state plainly that, until the located-in second-domain fork lands, the certificate's NET utility is demonstrated only on clean / templated graphs (CLUTRR): on natural prose the result is an EXTRACTION-GATED BOUNDARY -- atomic recall 0.376 natural vs ~0.53 templated, and the gold-read ceiling (1.0 / 1.0 / 1.0) shows the boundary is extraction recall, not the closure logic. We therefore target a neuro-symbolic / NeSy (EMNLP Findings) venue and frame the contribution as a COMPOSITIONAL FALSE-PREMISE diagnostic plus a gold-free structural detector, not a new end-to-end system.

**Operational arm cut:** CUT `concatenated-kinship` (56/56 trivial-by-construction); KEEP `bracket-selected temporal as feasibility only`.

> CUT the concatenated-kinship arm of the operational ~3000-char case study ENTIRELY. Its 56/56 cross-story absent abstentions are trivial BY CONSTRUCTION -- concatenated stories share no entities, so the entities are in different connected components and a sound closure abstains by definition; the arm carries no evidential weight and reads as inflated coverage. KEEP ONLY the bracket-selected temporal arm, and demote it to a single one-paragraph feasibility note whose only claim is that the pipeline RUNS end-to-end at ~3000-character length. The reclaimed space (roughly a column) goes to the diagnostic (the 16-cell table + capability gap) and the second-domain located-in replication, which is the decisive evidence.

## 7. One-thesis contribution table (tags as columns; SPINE first, PENDING labelled)

| claim_id | claim | headline numbers | evidence_tag | role | status |
|---|---|---|---|---|---|
| SPINE | FACT A (the raw LLM confidently FABRICATES absent relations: CLUTRR 47.2%/48.3%, Re-DocRED 32.6%/31.8%) + the SIGNAL-AGNOSTIC MIXED-POOL CAPABILITY GAP (no single confidence threshold can simultaneously cover present and abstain on absent; powered on CLUTRR: certificate selacc 0.827 vs 0.37-0.44, Holm-rejected), positioned as a COMPOSITIONAL FALSE-PREMISE / unanswerable-question instance, with a gold-free TRAINING-FREE STRUCTURAL detector. | FACT A 0.472/0.483/0.326/0.318; capability gap (CLUTRR) selacc 0.827 vs 0.37-0.44; Holm p_adj 0.0004/0.0027/0.0027/0.0027 | REAL-LLM-READ | HEADLINE | ESTABLISHED on CLUTRR + cross-family; natural-prose capability gap PENDING (extraction-gated) |
| P1-located-in-net-win | PENDING: located-in SAME-COMPONENT-SIBLING net-win on art_RfjDpsGkBXDG (~20,814 same-component-sibling pairs -- entities in the SAME connected component with NO valid derivation path, so abstention is a genuine DEDUCTIVE result, NOT disconnected-trivially-empty). Run vs the four-signal battery AND the query-side verifier at matched coverage with Holm-adjusted doc-clustered CIs. FORK: if the certificate's Holm-adjusted cw reductions EXCLUDE 0 there -> DEMONSTRATED FIX (becomes headline); else extraction-limited boundary. | PENDING (filled iter-9) | NATURAL-CORPUS-PENDING | PENDING | SLOT -- filled iter-9 |
| P2-query-side-verifier | PENDING: the QUERY-SIDE FALSE-PREMISE VERIFIER baseline ('are these two entities related at all?' / self-verification pass) -- the established method for this failure mode. The certificate's claim is credible only if it MATCHES or BEATS this verifier at matched coverage. | PENDING (filled iter-9) | NATURAL-CORPUS-PENDING | PENDING | SLOT -- filled iter-9 |
| S1-fuzzy-unification | Fuzzy unification with a certificate-bounded hallucination guarantee: sound-violating reads are CAUGHT by abstain-on-collapse (spatial 5/5, 0 silent-wrong missed); calibrated sub-1.0 disjunctions (frac_conf_1.0 = 0.00 vs memorized 1.00; ECE 0.142/0.111). | 5/5 caught; frac_conf_1.0 0.00 vs 1.00 | REAL-LLM-READ-ON-SYNTHETIC | SUPPORTING | ESTABLISHED (spatial); kinship catch UNTESTED |
| S2-cross-path | Cross-path intersection mechanism is a SYNTHETIC-CHANNEL-ONLY negative: iterated PC beats naive single-path only on synthetic long-hop redundancy; on real text it ties at length 2. | synthetic-only positive; real-text null | SYNTHETIC-CHANNEL | SUPPORTING | HONEST NEGATIVE |
| S3-natural-temporal | Natural-temporal redundancy is at best WEAKLY protective: corrected CIs include 0. | CI includes 0 | REAL-LLM-READ | SUPPORTING | WEAK / NULL |
| S4-operational | Operational ~3000-char feasibility: the pipeline RUNS at length; the concatenated-kinship arm is CUT (56/56 cross-story abstentions trivial BY CONSTRUCTION); only the bracket-selected temporal arm is kept as a one-paragraph feasibility note. | feasibility only (concat arm CUT) | REAL-LLM-READ | SUPPORTING | FEASIBILITY (compressed) |
| A1-mechanism-analysis | Mechanism analysis: algebra-richness scaling, redundancy inverted-U optimum, and a read-soundness-conditional zero-FP theorem. | P=1 zero-FP theorem; synthetic-channel scaling curves | THEOREM | APPENDIX | ESTABLISHED (scoped) |

**Mechanism concession (SPINE row):** closure MECHANISM INHERITED: +0.673 inherited / +0.0025 novel.

**False-premise positioning:** Position the contribution against the false-premise / unanswerable-question literature, NOT merely the neuro-symbolic literature. The raw LLM confidently answering an absent relational query is a COMPOSITIONAL FALSE-PREMISE / unanswerable-question instance: the question presupposes a relation that does not hold. Engage: FalseQA (Hu et al., ACL 2023) on questions with false presuppositions; AbstentionBench (NeurIPS 2025) on when models should abstain; and the query-side self-verification line (Wen et al., 'Know Your Limits', TACL 2025). The carved delta vs that literature is two-fold: (1) we operate in a MULTI-HOP RELATIONAL COMPOSITIONAL setting (the false premise is that a derivable kinship/located-in path exists), not single-fact factuality; and (2) our detector is GOLD-FREE and TRAINING-FREE -- a structural property of the extracted graph's closure -- rather than a learned or prompt-elicited confidence judgment. The credibility test for the certificate is whether it MATCHES OR BEATS a query-side false-premise verifier ('are these two entities related at all?') at matched coverage; that verifier is the established baseline for this failure mode and is a NAMED PENDING comparison (iter-9).

## 8. Reproduction-gate detail (carried | recomputed | matches | recomputed?)

| check | carried | recomputed | matches | recomputed? |
|---|---|---|---|---|
| clutrr_factA_raw_absent_hallucination | 0.4722 | 0.4722 | True | True |
| clutrr_gemini_crux_survival_verbalized | 0.4353 | 0.4353 | True | True |
| clutrr_gemini_crux_survival_sc_margin | 0.7176 | 0.7176 | True | True |
| clutrr_gemini_crux_survival_ptrue | 0.2471 | 0.2471 | True | True |
| clutrr_gemini_crux_survival_negent | 0.7176 | 0.7176 | True | True |
| clutrr_certificate_absent_confident_wrong | 0.0278 | 0.0278 | True | True |
| clutrr_absent_confident_wrong_reduction_vs_raw | 0.4444 | 0.4444 | True | True |
| clutrr_mixed_selacc_certificate | 0.8267 | 0.8267 | True | True |
| clutrr_mixed_selacc_ct_verbalized | 0.4133 | 0.4133 | True | True |
| clutrr_mixed_selacc_ct_sc_margin | 0.3733 | 0.3733 | True | True |
| clutrr_mixed_selacc_ct_ptrue | 0.44 | 0.44 | True | True |
| clutrr_mixed_selacc_ct_negent | 0.3733 | 0.3733 | True | True |
| clutrr_mixed_matched_coverage | 0.266 | 0.266 | True | True |
| clutrr_mixed_cw_reduction_verbalized | 0.1099 | 0.1099 | True | True |
| clutrr_mixed_cw_reduction_ci_verbalized | [0.0543, 0.1703] | [0.0543, 0.1703] | True | True |
| clutrr_mixed_cw_reduction_sc_margin | 0.1206 | 0.1206 | True | True |
| clutrr_mixed_cw_reduction_ci_sc_margin | [0.0486, 0.1957] | [0.0486, 0.1957] | True | True |
| clutrr_mixed_cw_reduction_ptrue | 0.1028 | 0.1028 | True | True |
| clutrr_mixed_cw_reduction_ci_ptrue | [0.0395, 0.1706] | [0.0395, 0.1706] | True | True |
| clutrr_mixed_cw_reduction_negent | 0.1206 | 0.1206 | True | True |
| clutrr_mixed_cw_reduction_ci_negent | [0.0486, 0.1957] | [0.0486, 0.1957] | True | True |
| clutrr_holm_p_adj_verbalized | 0.0004 | 0.0004 | True | True |
| clutrr_holm_p_adj_sc_margin | 0.0027 | 0.0027 | True | True |
| clutrr_holm_p_adj_ptrue | 0.0027 | 0.0027 | True | True |
| clutrr_holm_p_adj_negent | 0.0027 | 0.0027 | True | True |
| spatial_certificate_confident_wrong | 0.0219 | 0.0219 | True | True |
| spatial_raw_abstain_confident_wrong | 0.0351 | 0.0351 | True | True |
| clutrr_multihop_present_selacc_certificate | 0.8857 | 0.8857 | True | True |
| clutrr_multihop_present_selacc_ct_verbalized | 0.5429 | 0.5429 | True | True |
| clutrr_multihop_present_coverage | 0.6863 | 0.6863 | True | True |
| clutrr_atomic_precision | 0.5361 | 0.5361 | True | True |
| clutrr_atomic_recall | 0.5324 | 0.5324 | True | True |
| clutrr_atomic_f1 | 0.5343 | 0.5343 | True | True |
| clutrr_deepseek_factA | 0.4833 | 0.4833 | True | False |
| clutrr_deepseek_crux_survival_verbalized | 0.6724 | 0.6724 | True | False |
| clutrr_deepseek_crux_survival_sc_margin | 0.2241 | 0.2241 | True | False |
| clutrr_deepseek_crux_survival_ptrue | 0.1034 | 0.1034 | True | False |
| clutrr_deepseek_crux_survival_negent | 0.2241 | 0.2241 | True | False |
| redocred_factA_raw_absent_hallucination | 0.3261 | 0.3261 | True | True |
| redocred_gemini_crux_survival_verbalized | 0.5083 | 0.5083 | True | True |
| redocred_gemini_crux_survival_sc_margin | 0.85 | 0.85 | True | True |
| redocred_gemini_crux_survival_ptrue | 0.4833 | 0.4833 | True | True |
| redocred_gemini_crux_survival_negent | 0.85 | 0.85 | True | True |
| redocred_mixed_selacc_certificate | 0.475 | 0.475 | True | True |
| redocred_mixed_selacc_ct_verbalized | 0.675 | 0.675 | True | True |
| redocred_mixed_selacc_ct_sc_margin | 0.6 | 0.6 | True | True |
| redocred_mixed_selacc_ct_ptrue | 0.645 | 0.645 | True | True |
| redocred_mixed_selacc_ct_negent | 0.6 | 0.6 | True | True |
| redocred_mixed_matched_coverage | 0.2747 | 0.2747 | True | True |
| redocred_mixed_cw_reduction_verbalized | -0.0549 | -0.0549 | True | True |
| redocred_mixed_cw_ci_excludes_0_verbalized | false | false | True | True |
| redocred_mixed_cw_ci_verbalized | [-0.1302, 0.0133] | [-0.1302, 0.0133] | True | False |
| redocred_mixed_cw_reduction_sc_margin | -0.0343 | -0.0343 | True | True |
| redocred_mixed_cw_ci_excludes_0_sc_margin | false | false | True | True |
| redocred_mixed_cw_ci_sc_margin | [-0.1145, 0.0396] | [-0.1145, 0.0396] | True | False |
| redocred_mixed_cw_reduction_ptrue | -0.0467 | -0.0467 | True | True |
| redocred_mixed_cw_ci_excludes_0_ptrue | false | false | True | True |
| redocred_mixed_cw_ci_ptrue | [-0.1223, 0.023] | [-0.1223, 0.023] | True | False |
| redocred_mixed_cw_reduction_negent | -0.0343 | -0.0343 | True | True |
| redocred_mixed_cw_ci_excludes_0_negent | false | false | True | True |
| redocred_mixed_cw_ci_negent | [-0.1145, 0.0396] | [-0.1145, 0.0396] | True | False |
| redocred_holm_p_adj_verbalized | 1.0 | 1.0 | True | True |
| redocred_holm_p_adj_sc_margin | 1.0 | 1.0 | True | True |
| redocred_holm_p_adj_ptrue | 1.0 | 1.0 | True | True |
| redocred_holm_p_adj_negent | 1.0 | 1.0 | True | True |
| redocred_llm_read_present_coverage | 0.4833 | 0.4833 | True | True |
| redocred_over_abstain_present_rate | 0.5167 | 0.5167 | True | True |
| redocred_present_selacc_primitive | 0.546 | 0.546 | True | True |
| redocred_goldread_present_coverage | 1.0 | 1.0 | True | False |
| redocred_goldread_correct_absent_abstention | 1.0 | 1.0 | True | False |
| redocred_goldread_present_selacc | 1.0 | 1.0 | True | False |
| redocred_atomic_precision | 0.6203 | 0.6203 | True | True |
| redocred_atomic_recall_converse_invariant | 0.3762 | 0.3762 | True | True |
| redocred_atomic_f1 | 0.4684 | 0.4684 | True | True |
| redocred_atomic_recall_vs_locally_justifiable | 0.4646 | 0.4646 | True | False |
| redocred_deepseek_factA | 0.3178 | 0.3178 | True | False |
| redocred_deepseek_crux_survival_verbalized | 0.4118 | 0.4118 | True | False |
| redocred_deepseek_crux_survival_sc_margin | 0.2941 | 0.2941 | True | False |
| redocred_deepseek_crux_survival_ptrue | 0.3235 | 0.3235 | True | False |
| redocred_deepseek_crux_survival_negent | 0.2941 | 0.2941 | True | False |


**Count breakdown:** 360+116=476 present; 368+209=577 absent (hard-asserted).
