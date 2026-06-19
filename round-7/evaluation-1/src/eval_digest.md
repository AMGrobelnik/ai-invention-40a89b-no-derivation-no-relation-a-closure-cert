# eval_iter7_dir3 — Empirical-Isolation Reframe & Framing Scaffold (paper-facing)

**$0 re-analysis.** numpy/scipy/json only; no LLM, no network. Seed 20260617, B=10000. Reproduction gate: **38/38 checks pass**, reproduction_ok=**True**.

## Headline-structure guidance for GEN_PAPER_TEXT

- LEAD with the empirical-isolation / confidence-blindness result (FACT A + FACT B + the mixed-pool showdown), NOT with the closure mechanism.
- CONCEDE the mechanism up front as INHERITED: the multi-hop deduction win is a standard neuro-symbolic premise (+0.673 of the gap is inherited closure; the novel empirical-isolation increment is +0.0025). Make this concession a framing sentence, not a buried footnote.
- Do NOT present the 2.8% certificate confident-wrong on CLUTRR absent pairs as the load-bearing number; it is structural-by-construction (disconnected components => sound closure abstains by definition). Use the non-circular-facts ledger to police this.
- Carry a clearly-LABELED PENDING slot for the iter-7 natural-corpus run: on Re-DocRED, report FACT-A (raw absent-hallucination rate), FACT-B (signal survival), and the mixed-pool showdown; this is what makes the natural-corpus result DECISIVE (the extracted graph is no longer trivially correct).
- Present evidence-class tags (THEOREM / SYNTHETIC-CHANNEL / GOLD-ONLY-GATE / REAL-LLM-READ / REAL-LLM-READ-ON-SYNTHETIC) as table COLUMNS, not inline hedges.
- Keep the spatial single-path boundary (P_O honesty): on ordinary single-path RCC-8 the certificate ties/loses (selective-accuracy gap -0.088, CI brackets 0). State it plainly as the scope boundary so the paper cannot overclaim generality.

## 1A. Structural-by-construction paragraph (verbatim-ready)

> A note on what the certificate's 2.8% confident-wrong rate on CLUTRR absent pairs does and does not establish. In the CLUTRR construction an absent pair is DEFINED as two entities that fall in DIFFERENT connected components of the extracted kinship graph; a SOUND forward-closure least-fixpoint over that graph therefore derives the EMPTY relation set for such a pair and ABSTAINS almost by definition. Imperfect extraction (atomic recall ~0.53) can only REMOVE edges, which can only INCREASE apparent disconnection, so it makes the certificate abstain MORE, never less, on absent pairs. The certificate's 2.8% confident-wrong on this stratum is thus NEAR-TAUTOLOGICAL given the setup: one side of the comparison is handed the answer by the way the regime is built, and this number must NOT be allowed to carry the section. The genuinely non-circular content -- the content that becomes the headline -- is a property of the RAW LLM and of the confidence signals, measured INDEPENDENTLY of the certificate. FACT A: the raw LLM confidently fabricates a kinship relation on 47.2% of these absent pairs (cross-family deepseek-v3.2: 48.3%). FACT B: not one member of a strong four-signal confidence battery -- verbalized confidence, self-consistency vote-margin, Kadavath P(True), and semantic-entropy negentropy -- removes those hallucinations at a coverage matched to the certificate; the fractions surviving a certificate-matched rule are 0.4353 / 0.7176 / 0.2471 / 0.7176, and even the single best signal, P(True), still lets 24.7% through. These two facts hold no matter how the certificate behaves. Finally, this is exactly why extraction recall and the natural-corpus run are load-bearing: on a NATURAL corpus the extracted graph -- and hence absent-detection -- is no longer trivially correct, because extraction errors can also DELETE a true edge and make the certificate OVER-abstain on a PRESENT pair (a cost the disconnected-by-construction CLUTRR regime hides). That asymmetry is what converts the iter-7 natural-corpus experiment from a confirmatory check into a DECISIVE test of whether the certificate's abstention discipline survives when the graph is no longer handed to it.

## 1B. Non-circular vs structural-by-construction ledger

| key | value | evidence_tag | side | role | source | recomputed | matches |
|---|---|---|---|---|---|---|---|
| FACT_A_raw_absent_hallucination | 0.4722 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| FACT_A_cross_family_deepseek | 0.4833 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | False | True |
| FACT_B_crux_survival_verbalized | 0.4353 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| FACT_B_crux_survival_sc_margin | 0.7176 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| FACT_B_crux_survival_ptrue | 0.2471 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| FACT_B_crux_survival_negent | 0.7176 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| FACT_B_deepseek_survival_verbalized | 0.6724 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | False | True |
| FACT_B_deepseek_survival_sc_margin | 0.2241 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | False | True |
| FACT_B_deepseek_survival_ptrue | 0.1034 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | False | True |
| FACT_B_deepseek_survival_negent | 0.2241 | REAL-LLM-READ | NON_CIRCULAR | HEADLINE | art_LeRQRGHJZcdQ | False | True |
| certificate_absent_confident_wrong | 0.0278 | REAL-LLM-READ | STRUCTURAL_BY_CONSTRUCTION | SUPPORTING | art_LeRQRGHJZcdQ | True | True |
| absent_confident_wrong_reduction_vs_raw | 0.4444 | REAL-LLM-READ | STRUCTURAL_BY_CONSTRUCTION | SUPPORTING | art_LeRQRGHJZcdQ | True | True |
| absent_reduction_ci95_lo | 0.3167 | REAL-LLM-READ | STRUCTURAL_BY_CONSTRUCTION | SUPPORTING | art_LeRQRGHJZcdQ | False | True |
| absent_reduction_ci95_hi | 0.5833 | REAL-LLM-READ | STRUCTURAL_BY_CONSTRUCTION | SUPPORTING | art_LeRQRGHJZcdQ | False | True |
| multihop_present_selacc_certificate | 0.8857 | INHERITED | INHERITED | SUPPORTING | art_LeRQRGHJZcdQ | True | True |
| multihop_present_selacc_ct_verbalized | 0.5429 | INHERITED | INHERITED | SUPPORTING | art_LeRQRGHJZcdQ | True | True |
| multihop_present_coverage | 0.6863 | INHERITED | INHERITED | SUPPORTING | art_LeRQRGHJZcdQ | True | True |
| inherited_gap_increment | 0.673 | INHERITED | INHERITED | FRAMING | art_D0cHQUJ8kY75 | False | True |
| novel_empirical_isolation_increment | 0.0025 | INHERITED | INHERITED | FRAMING | art_D0cHQUJ8kY75 | False | True |
| mixed_selacc_certificate | 0.8267 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_selacc_ct_verbalized | 0.4133 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_selacc_ct_sc_margin | 0.3733 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_selacc_ct_ptrue | 0.44 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_selacc_ct_negent | 0.3733 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_matched_coverage | 0.266 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_cw_reduction_verbalized | 0.1099 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_cw_reduction_sc_margin | 0.1206 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_cw_reduction_ptrue | 0.1028 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_cw_reduction_negent | 0.1206 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_holm_p_adj_verbalized | 0.0004 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_holm_p_adj_sc_margin | 0.0027 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_holm_p_adj_ptrue | 0.0027 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| mixed_holm_p_adj_negent | 0.0027 | REAL-LLM-READ | NON_CIRCULAR_CONDITIONAL | HEADLINE | art_LeRQRGHJZcdQ | True | True |
| spatial_certificate_confident_wrong | 0.0219 | REAL-LLM-READ | STRUCTURAL_BY_CONSTRUCTION | SUPPORTING | art_LeRQRGHJZcdQ | True | True |
| spatial_raw_abstain_confident_wrong | 0.0351 | REAL-LLM-READ | STRUCTURAL_BY_CONSTRUCTION | SUPPORTING | art_LeRQRGHJZcdQ | True | True |
| spatial_selacc_gap_certificate_vs_raw_abstain | -0.0882 | REAL-LLM-READ | STRUCTURAL_BY_CONSTRUCTION | BOUNDARY | art_LeRQRGHJZcdQ | False | True |
| spatial_selacc_gap_ci95_lo | -0.2222 | REAL-LLM-READ | STRUCTURAL_BY_CONSTRUCTION | BOUNDARY | art_LeRQRGHJZcdQ | False | True |
| spatial_selacc_gap_ci95_hi | 0.04 | REAL-LLM-READ | STRUCTURAL_BY_CONSTRUCTION | BOUNDARY | art_LeRQRGHJZcdQ | False | True |
| atomic_precision | 0.5361 | REAL-LLM-READ | MEASURED | SUPPORTING | art_0a7i481ZRwS1 | True | True |
| atomic_recall | 0.5324 | REAL-LLM-READ | MEASURED | SUPPORTING | art_0a7i481ZRwS1 | True | True |
| atomic_f1 | 0.5343 | REAL-LLM-READ | MEASURED | SUPPORTING | art_0a7i481ZRwS1 | True | True |
| fuzzy_spatial_cw_reduction | 0.364 | REAL-LLM-READ | MEASURED | SUPPORTING | art_I22c-J7-OcXl | False | True |
| fuzzy_kinship_cw_reduction | 0.2162 | REAL-LLM-READ | MEASURED | SUPPORTING | art_I22c-J7-OcXl | False | True |
| fuzzy_spatial_unsound_reads_caught | 1.0 | REAL-LLM-READ | MEASURED | SUPPORTING | art_I22c-J7-OcXl | False | True |
| redocred_present_multihop | 360 | NATURAL-CORPUS-PENDING | PENDING | PENDING | art_NUWTxBVWENIJ | False | True |
| redocred_absent_pairs | 368 | NATURAL-CORPUS-PENDING | PENDING | PENDING | art_NUWTxBVWENIJ | False | True |
| combined_present_round_trip | 476 | GOLD-ONLY-GATE | STRUCTURAL_BY_CONSTRUCTION | SUPPORTING | art_NUWTxBVWENIJ | True | True |
| combined_absent_round_trip | 577 | GOLD-ONLY-GATE | STRUCTURAL_BY_CONSTRUCTION | SUPPORTING | art_NUWTxBVWENIJ | True | True |

## 2. Re-DocRED count breakdown + fix clause

- **Re-DocRED (PRIMARY)**: 360 present multi-hop (222 composed-only/non-circular; hops {'2': 318, '3': 38, '4': 4}) / 368 absent.
- **DocRED (SECONDARY)**: 116 present / 209 absent (DOWNGRADED (vanilla DocRED false-negatives)).
- **Combined engine round-trip**: 476 present / 577 absent — **360+116=476, 368+209=577** (hard-asserted).
- **Completeness correction**: on 400 shared titles Re-DocRED carries 3087 family edges vs DocRED's 1716 (+80%).

> The Re-DocRED natural-text corpus reports two figure pairs that are sometimes confused: the PRIMARY trustworthy-absent slice (re-docred) supplies 360 present multi-hop queries and 368 absent pairs, while the engine round-trip verification (476 present / 577 absent) is the COMBINED re-docred (360 / 368) plus secondary docred (116 / 209) total -- 360+116 = 476 and 368+209 = 577 -- so the two pairs are not in conflict; the larger pair is the union over both sources, the smaller is the load-bearing Re-DocRED slice on which absent gold is trustworthy.

## 3. Abstract front-matter (scope) + operational compression

> Scope. This paper studies a closure-certified DEDUCTION SUB-MODULE -- a sound symbolic forward-closure over LLM-extracted relations that abstains rather than guess -- and NOT a full operational text-to-FOL umbrella pipeline. We therefore state up front what is explicitly OUT OF SCOPE and named here as FUTURE WORK THIS PAPER DOES NOT CLAIM TO DELIVER: (a) upper-ontology / OpenCyc grounding and taxonomic background knowledge; (b) general fuzzy unification over arbitrary predicates -- our fuzzy contribution is scoped to disjunctions over a KNOWN base vocabulary (RCC-8 base relations; CLUTRR kinship primitives), not open-vocabulary predicate invention; (c) atomic re-extraction -- extraction quality is MEASURED, not improved (CLUTRR atomic precision/recall/F1 ~0.536 / 0.532 / 0.534); and (d) reasoning over genuine ~3000-character professional documents -- no benchmark document we use reaches that length (CLUTRR <=871 chars; Re-DocRED Wikipedia intros average ~1020 chars, none family-bearing reach 3000), and the operational case study is bracket-selected and concatenation-constructed rather than naturally long. Because extraction is the ceiling (~0.53 atomic recall implies only ~19% Mode-A deductive coverage on dense prose), we report real-text utility as structurally EXTRACTION-LIMITED. Accordingly we target a neuro-symbolic / temporal-and-qualitative-reasoning venue (NeSy; EMNLP Findings) rather than a full knowledge-extraction-pipeline track, and frame the contribution as an EMPIRICAL ISOLATION of confidence-blindness, not as a new end-to-end system.

> Compression recommendation for the operational ~3000-char case study (art_WQoePKrpsTPo): collapse its two arms -- the bracket-selected temporal arm and the concatenation-constructed kinship arm (in which all 56/56 cross-story absent pairs are abstained trivially BY CONSTRUCTION, because concatenated stories share no entities) -- into ONE short paragraph whose only claims are that the pipeline RUNS at ~3000-character length and that EXTRACTION recall is the binding ceiling. This frees roughly a column of space for the natural-corpus (Re-DocRED) result, which is the decisive evidence; the operational study should support feasibility, not headline accuracy.

## 4. Fuzzy downweight — LEAD with the 5/5 Mode-B catch

**Lead:** The distinctive fuzzy-unification contribution is the abstain-on-collapse CATCH of SOUND-VIOLATING reads, not a calibration number. Worked case: the vague preposition 'around' is read as the RCC-8 disjunction {NTPPi, TPPi}, which DROPS the gold relation EC; the closure then collapses to the empty set, so the certificate ABSTAINS instead of committing the wrong relation DC. On the spatial setting every sound-violating read was caught: 5 of 5 unsound reads triggered collapse-or-abstain, with 0 silent-wrong answers missed (read-soundness-conditional zero-FP, asserted with 0 violations). The kinship setting had 0 unsound reads, so its catch holds only TRIVIALLY there and is reported as UNTESTED rather than as evidence.

**Calibration contrast (supporting):** Supporting honesty contrast: on genuinely-vague reads the LLM emits calibrated sub-1.0 disjunctions -- the fraction of reads at confidence exactly 1.0 is 0.00 in BOTH settings, versus the memorized iter-4 Mode-P's 1.00 (which was table recall, not fuzzy unification). Per-candidate ECE is 0.142 (spatial) and 0.111 (kinship).

**Supporting number:** The clean within-artifact risk-coverage comparison: the certificate has confident-wrong 0.000 at coverage 0.535 on spatial (n=228, 38 multipath) and 0.000 at coverage 0.314 on kinship (n=1013), versus commit-argmax confident-wrong 0.364 and 0.216 respectively (doc-clustered paired-bootstrap reduction CIs [0.303, 0.430] and [0.192, 0.242], both exclude 0). LEAD with the 5/5 catch; cite this as the supporting magnitude.

**Demoted unit caveat:** DEMOTED caveat (keep, but no headline table): an earlier 0.000-vs-0.415 framing is APPLES-TO-ORANGES, because the certificate's confident-wrong is measured at the closure-QUERY level while the confidence baseline's 0.415 / 0.346 thresholded-abstainer figures (from a different artifact, art_0MDLD-w-RXOu) are at the edge-READ level, matched only on coverage fraction. The unit mismatch means that contrast must not anchor a table; the query-level certificate-vs-commit-argmax comparison above is the matched one.

## 5. One-thesis contribution table (tags as columns)

| claim_id | claim | headline numbers | evidence_tag | role | status |
|---|---|---|---|---|---|
| SPINE/CLAIM-1 | Empirical isolation of confidence-blindness: a raw LLM confidently fabricates absent relations (FACT A, 47.2%; deepseek 48.3%) and NO member of a strong 4-signal confidence battery removes them at matched coverage (FACT B, survival 0.4353/0.7176/0.2471/0.7176); a sound closure certificate does, winning the mixed-pool showdown (selective accuracy 0.827 vs 0.37-0.44). The closure MECHANISM is conceded INHERITED (+0.673 inherited / +0.0025 novel). | FACT A 0.4722; FACT B 0.4353/0.7176/0.2471/0.7176; mixed 0.8267 vs 0.37-0.44; Holm p_adj 0.0004/0.0027/0.0027/0.0027 | REAL-LLM-READ | HEADLINE | ESTABLISHED (CLUTRR + cross-family) |
| CLAIM-2 | Natural-corpus run on Re-DocRED: does the certificate still beat the confidence battery when the extracted graph is NO LONGER trivially correct (extraction can over-abstain on PRESENT pairs)? Fill FACT-A / FACT-B / mixed-pool on real Wikipedia prose; iter-8 adds a second 'located-in' domain/reader. | PENDING (Re-DocRED 360 present / 368 absent slot) | NATURAL-CORPUS-PENDING | PENDING | SLOT (to be filled iter-7/iter-8) |
| CLAIM-3 | Fuzzy unification with a certificate-bounded hallucination guarantee: sound-violating reads are CAUGHT by abstain-on-collapse (spatial 5/5, 0 silent-wrong missed); calibrated sub-1.0 disjunctions (frac_conf_1p0=0.00 vs memorized 1.00). | 5/5 caught; cert CW 0.000 vs commit-argmax 0.364 (spatial) / 0.216 (kinship) | REAL-LLM-READ-ON-SYNTHETIC | SUPPORTING | ESTABLISHED (spatial); kinship catch UNTESTED |
| CLAIM-4 | Cross-path intersection mechanism is a SYNTHETIC-CHANNEL-ONLY negative: iterated PC beats naive single-path only on synthetic long-hop redundancy; on real text it ties at length 2. | synthetic-only positive; real-text null | SYNTHETIC-CHANNEL; GOLD-ONLY-GATE; SYNTHETIC-CONTROL | SUPPORTING | HONEST NEGATIVE |
| CLAIM-5 | Natural-temporal redundancy is at best WEAKLY protective: corrected CIs include 0. | CI includes 0 | REAL-LLM-READ | SUPPORTING | WEAK / NULL |
| CLAIM-6 | Operational ~3000-char case study: the pipeline RUNS at length and EXTRACTION is the ceiling (bracket-selected + concatenation-constructed; 56/56 cross-story absent trivially abstained). | feasibility only (compress to one paragraph) | REAL-LLM-READ | SUPPORTING-COMPRESSED | FEASIBILITY |
| CLAIM-7 | Mechanism analysis: algebra-richness scaling, redundancy inverted-U optimum, and a read-soundness-conditional zero-FP theorem. | P=1 zero-FP theorem; synthetic-channel scaling curves | THEOREM; SYNTHETIC-CHANNEL; REAL-LLM-READ-ON-SYNTHETIC | APPENDIX | ESTABLISHED (scoped) |

## Reproduction gate detail

| check | carried | recomputed | matches |
|---|---|---|---|
| factA_raw_absent_hallucination | 0.4722 | 0.4722 | True |
| factB_crux_survival_verbalized | 0.4353 | 0.4353 | True |
| factB_crux_survival_sc_margin | 0.7176 | 0.7176 | True |
| factB_crux_survival_ptrue | 0.2471 | 0.2471 | True |
| factB_crux_survival_negent | 0.7176 | 0.7176 | True |
| certificate_absent_confident_wrong | 0.0278 | 0.0278 | True |
| absent_confident_wrong_reduction_vs_raw | 0.4444 | 0.4444 | True |
| mixed_selacc_certificate | 0.8267 | 0.8267 | True |
| mixed_selacc_ct_verbalized | 0.4133 | 0.4133 | True |
| mixed_selacc_ct_sc_margin | 0.3733 | 0.3733 | True |
| mixed_selacc_ct_ptrue | 0.44 | 0.44 | True |
| mixed_selacc_ct_negent | 0.3733 | 0.3733 | True |
| mixed_matched_coverage | 0.266 | 0.266 | True |
| mixed_cw_reduction_verbalized | 0.1099 | 0.1099 | True |
| mixed_cw_reduction_ci_verbalized | [0.0543, 0.1703] | [0.0543, 0.1703] | True |
| mixed_cw_reduction_sc_margin | 0.1206 | 0.1206 | True |
| mixed_cw_reduction_ci_sc_margin | [0.0486, 0.1957] | [0.0486, 0.1957] | True |
| mixed_cw_reduction_ptrue | 0.1028 | 0.1028 | True |
| mixed_cw_reduction_ci_ptrue | [0.0395, 0.1706] | [0.0395, 0.1706] | True |
| mixed_cw_reduction_negent | 0.1206 | 0.1206 | True |
| mixed_cw_reduction_ci_negent | [0.0486, 0.1957] | [0.0486, 0.1957] | True |
| holm_p_adj_verbalized | 0.0004 | 0.0004 | True |
| holm_p_adj_sc_margin | 0.0027 | 0.0027 | True |
| holm_p_adj_ptrue | 0.0027 | 0.0027 | True |
| holm_p_adj_negent | 0.0027 | 0.0027 | True |
| spatial_certificate_confident_wrong | 0.0219 | 0.0219 | True |
| spatial_raw_abstain_confident_wrong | 0.0351 | 0.0351 | True |
| multihop_present_selacc_certificate | 0.8857 | 0.8857 | True |
| multihop_present_selacc_ct_verbalized | 0.5429 | 0.5429 | True |
| multihop_present_coverage | 0.6863 | 0.6863 | True |
| deepseek_absent_hallucination | 0.4833 | 0.4833 | True |
| deepseek_survival_verbalized | 0.6724 | 0.6724 | True |
| deepseek_survival_sc_margin | 0.2241 | 0.2241 | True |
| deepseek_survival_ptrue | 0.1034 | 0.1034 | True |
| deepseek_survival_negent | 0.2241 | 0.2241 | True |
| atomic_precision | 0.5361 | 0.5361 | True |
| atomic_recall | 0.5324 | 0.5324 | True |
| atomic_f1 | 0.5343 | 0.5343 | True |
