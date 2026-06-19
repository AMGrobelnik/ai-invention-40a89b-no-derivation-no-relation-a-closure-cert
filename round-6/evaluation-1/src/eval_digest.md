# Evaluation digest — fuzzy fair-baseline + framing spine (iter-6)

**$0 LLM spend** · pure numpy+scipy re-analysis · seed=20260617 · doc-clustered paired bootstrap B=10000.

- STEP 0 reproduce-verify: **0 mismatches vs iter-5** (29 checks), **0 vs iter-4** (13 checks). Target = 0.
- Carried-literal verify vs CLUTRR+SPATIAL source files: **0 mismatches**.
- FUZZY ground-truth literals (spatial cert cov 0.5350877 / CW 0.000; commit-argmax CW 0.3640 = 83/228; kinship cert cov 0.3139191; commit-argmax CW 0.2162 = 219/1013): **all asserted, pass**.

## Headline (TASK 1, MAJOR #2): the certificate beats a FAIR confidence abstainer

Replacing the misleading *always-answer* comparator (0.000 vs 0.364) with a **confidence-thresholded top-1 abstainer at matched coverage**:

- **Spatial RCC-8**: baseline confident-wrong **0.4147** (95% CI [0.3760, 0.4566]) @ coverage 0.5353 (implied τ=0.70); certificate confident-wrong 0.000 → **certificate beats = True** (ECE_top1 0.286, POOR calibration).
- **Kinship paraphrase**: baseline confident-wrong **0.3461** (95% CI [0.2931, 0.4128]) @ coverage 0.3140 (implied τ=0.40); certificate 0.000 → **certificate beats = True** (ECE_top1 0.051, GOOD calibration — beats anyway).

> PRE-STATED expectation: spatial top-1 calibration is POOR (ECE 0.286) so the certificate should BEAT the matched-coverage confidence baseline; kinship top-1 calibration is GOOD (ECE 0.051) so the baseline MIGHT tie. ACTUAL RESULT: the certificate beats the confidence-thresholded top-1 baseline in BOTH settings (spatial confident-wrong 0.415, 95% CI [0.376, 0.457]; kinship 0.346, 95% CI [0.293, 0.413]; both bootstrap lower bounds > 0). The kinship non-tie does NOT contradict good calibration: ECE measures confidence-vs-accuracy AGREEMENT, but the kinship reads' MAXIMUM emitted top-1 confidence is only 0.8 and most committed reads sit at conf 0.4, so even the most-confident ~31% of reads are ~35% wrong -- a confidence threshold cannot reach 0 confident-wrong when the underlying read accuracy is modest, however well-calibrated.

> **Unit-of-analysis caveat** — LOAD-BEARING: the certificate's 0.000 confident-wrong is measured on closure QUERIES, while the confidence baseline's confident-wrong is measured on single edge READS (query records carry no per-query confidence), matched only on the committed FRACTION, not the object. This establishes that the LLM's OWN per-read confidence cannot be thresholded to low confident-wrong at matched coverage (a real, $0 finding); a query-level verbalized-confidence / self-consistency abstainer on the SAME query pool is the PENDING STEP-A experiment (iter-6). The certificate's strictly distinctive, same-object edge is the Mode-B catch: 5/5 sound-violating spatial reads at ordinary confidence (0 silent-wrong missed); 0 testable on kinship (no unsound reads).

**Honest framing string for GEN_PAPER_TEXT:** auditable, faithful abstention that ADDITIONALLY catches sound-violating reads a confidence threshold cannot see — quantified at 5/5 unsound spatial reads caught (0 silent-wrong missed), 0 testable on kinship (no unsound reads) — rather than letting 0.000-vs-0.364 (an always-answer contrast) carry the section.

### Rebuilt Table 3 — Spatial RCC-8 (spatial_fuzzy_rcc8)

| Method | Coverage | Acc-among-answered | Confident-wrong | Δ vs certificate (95% CI) | Evidence tag |
|---|---|---|---|---|---|
| commit-argmax (always-answer) | 1.0000 | 0.6360 | 0.3640 | n/a (always-answers) | REAL-LLM-FUZZY-READ |
| abstain-always | 0.0000 | — | 0.0000 | n/a (coverage 0) | REAL-LLM-FUZZY-READ |
| **CERTIFICATE (abstain-on-collapse)** | 0.5351 | 1.0000 | **0.0000** | 0.000 (reference) | REAL-LLM-FUZZY-READ + THEOREM:zero-FP-cond. |
| **CONFIDENCE-THRESHOLDED TOP-1 @ matched cov (NEW)** | 0.5353 | 0.5853 | 0.4147 | +0.4147 [0.3760, 0.4566] (beats=True) | REAL-LLM-FUZZY-READ |
| _Mode-B sound-violation catches_ | — | — | — | 5/5 caught, 0 silent-wrong missed | REAL-LLM-FUZZY-READ + THEOREM |

Mode-B detail: 100 unsound calibration edge-reads, all at top-1 conf ['0.7', '0.8'] (dist {'0.7': 13, '0.8': 87}); 88 of them sit in the matched-coverage committed (conf≥τ) region — i.e. reads a confidence threshold would COMMIT WRONG but the certificate catches via set-soundness.

### Rebuilt Table 3 — Kinship paraphrase (kinship_fuzzy_paraphrase)

| Method | Coverage | Acc-among-answered | Confident-wrong | Δ vs certificate (95% CI) | Evidence tag |
|---|---|---|---|---|---|
| commit-argmax (always-answer) | 1.0000 | 0.7838 | 0.2162 | n/a (always-answers) | REAL-LLM-FUZZY-READ |
| abstain-always | 0.0000 | — | 0.0000 | n/a (coverage 0) | REAL-LLM-FUZZY-READ |
| **CERTIFICATE (abstain-on-collapse)** | 0.3139 | 1.0000 | **0.0000** | 0.000 (reference) | REAL-LLM-FUZZY-READ + THEOREM:zero-FP-cond. |
| **CONFIDENCE-THRESHOLDED TOP-1 @ matched cov (NEW)** | 0.3140 | 0.6539 | 0.3461 | +0.3461 [0.2931, 0.4128] (beats=True) | REAL-LLM-FUZZY-READ |
| _Mode-B sound-violation catches_ | — | — | — | 0/0 (no unsound reads → UNTESTED) | REAL-LLM-FUZZY-READ + THEOREM |

## TASK 2 (MAJOR #3): tempered two-condition paragraph (verbatim for sec:decisive)

> Across the two real venues we could a-priori gate before any LLM spend, the cross-path coding mechanism — multi-path intersection as an error-correcting code over LLM reads — fails to realize, but for OPPOSITE reasons, and we present this as an explanatory account of two negatives rather than a predictive law. The mechanism needs two conditions to hold jointly: (i) the per-edge reads must be INFORMATIVE (sound but sub-universal, so intersection has bite), and (ii) the document redundancy must be SAME-ALGEBRA structural redundancy (>=2 edge-disjoint paths whose compositions land in one calculus). On natural temporal Allen text condition (i) is violated: high-recall reads are near-universe (event-local underdetermined rate 0.87, mean breadth 11.5/13; a stronger reader, deepseek-v3.2, is even more conservative at 0.99), so intersection / best-single / naive all resolve 0/125 gold-singleton multi-path queries — not a weak-model artifact. On semi-natural spatial RCC-8 text condition (ii) is violated: reads ARE informative (breadth 2.1/8, underdetermined 0.036), but the gold is a containment TREE — all 228 deduction queries have exactly one edge-disjoint path and the cardinal subgraph already composes to a singleton on the best single path, so the corpus 27.4% tight-multipath flag is purely STRUCTURAL (undirected, mixed-algebra) and the genuine redundancy is CROSS-algebra (topology vs direction), not intersectable in one calculus. Synthetic positive controls that satisfy BOTH conditions confirm the mechanism is real: on Allen at recall 0.95 intersection reaches selective accuracy 0.976 vs best-single 0.717 (+0.259, 95% CI [0.177, 0.349]); on RCC-8, 0.890 vs 0.797. We therefore claim only that these two conditions were each INDEPENDENTLY VIOLATED in the two venues we could gate, with synthetic controls localizing the cause — NOT a sharp, general, predictive characterization (the conditions are close to definitionally necessary, so their joint absence across two venues is an explanation, not a validated law). Even where the mechanism works its realized cross-path COVERAGE bite is tiny (+0.024 over best-single, CI includes 0); the value is precision of committed answers (+0.259 selective accuracy), not coverage. This subsection is subordinate to the certificate headline and is the paper single cross-path-coding result; it is NOT a co-equal contribution.

*Section target:* sec:decisive (ONE subordinate subsection, NOT a co-headline). *Drops:* 'two NECESSARY conditions', 'sharp, general characterization', 'two-condition LAW'.

## TASK 3 (MINOR #5): one-thesis contribution table (tags as columns)

**One-line thesis:** *A structural, label-free certificate that catches confident relational hallucinations that confidence cannot see.*

| Row | Claim | Evidence tag | Where it holds | Status |
|---|---|---|---|---|
| **SPINE** | Training-free, gold-free, per-edge ABSTAIN-ON-COLLAPSE certificate over LLM-extracted relational facts whose DISTINCTIVE value is reducing CONFIDENT-WRONG hallucination on no-derivation / absent-relation queries where a confidence threshold structurally CANNOT abstain (high-confidence hallucinations), and on sound-violating reads (Mode-B collapse). | REAL-LLM-READ + THEOREM(zero-FP conditional on read soundness) | templated CLUTRR end-to-end (<=871 chars); fuzzy spatial/kinship RCC-8 & paraphrase; weakly protective on natural temporal text | CONFIRMED-AT-POWER (certificate). Fair-confidence-baseline edge: the certificate beats a matched-coverage confidence-thresholded top-1 abstainer at the EDGE-READ level in BOTH fuzzy settings (CI excludes 0); the strictly same-object distinctive edge (Mode-B sound-violation catch) is ESTABLISHED on fuzzy spatial (5/5) and UNTESTED on kinship (0 unsound reads). PENDING: query-level confidence/self-consistency abstainer on CLUTRR absent/mixed + spatial RCC-8 deduction pools (STEP-A), and on a genuinely-natural ~3000-char corpus (STEP-B). |
| SUPPORTING | Cross-path coding is SYNTHETIC-CHANNEL-ONLY — two conditions each independently violated on both a-priori-gated real venues (temporal near-universe reads; spatial containment-tree gold), synthetic controls confirm the mechanism when both hold. | REAL-LLM-READ + GOLD-ONLY-GATE + SYNTHETIC-CONTROL | synthetic Allen + RCC-8 channels only; refuted on real temporal + real spatial | RESOLVED NEGATIVE (no longer PENDING; art_i53dBKgGY3Ig overturns dataset-card GENERAL-band optimism, $0 gold-structural) |
| APPENDIX A1 | Algebra-richness scaling: point(3) +0.043 -> RCC-8(8) +0.448 -> Allen(13) +0.676; INHERITED table-vs-LLM-composition (Allen decomposes +0.673 inherited / +0.0025 novel). | REAL-LLM-READ-ON-SYNTHETIC | — | APPENDIX |
| APPENDIX A2 | Redundancy inverted-U: peak_K [2,4,7,10,16]; silent-wrong [0.0064,0.1456]; Page p~5e-4; realized cross-path coverage bite +0.024. | SYNTHETIC-CHANNEL | — | APPENDIX |
| APPENDIX A3 | Zero-FP soundness THEOREM verified on 100,296 networks; recall & rho are INPUTS (characterizes, not predicts). | THEOREM | — | APPENDIX |
| FOOTNOTE F1-ceiling-temporal | Corrected natural-temporal marginal: vs-PoT 0.0265 CI[-0.0883,0.1397] includes 0; confident-wrong-among-answered 0.4248=48/113; modeA cov 0.1883. | REAL-LLM-READ | — | ceiling/scope |
| FOOTNOTE F2-scope-deduction | Deduction-sub-module ceiling: atomic recall 0.5324 => ~0.19 coverage; OpenCyc / atomic re-extraction / general fuzzy OUT OF SCOPE; hand-supplied tables; no doc reaches ~3000 chars. | SCOPE | — | ceiling/scope |
| PENDING P-A | STEP A — add confidence-thresholded raw-abstain baseline (verbalized-confidence + self-consistency vote-margin) to the CLUTRR absent/mixed pool AND the spatial RCC-8 deduction pool at matched coverage (iter-6 experiment). | — | — | **PENDING (NOT computed here)** |
| PENDING P-B | STEP B — certificate vs confidence abstainer on >=1 genuinely-natural corpus' no-derivation stratum, e.g. the iter-6 Re-DocRED ~3000-char corpus (iter-7). | — | — | **PENDING (NOT computed here)** |

Spine key numbers: {"clutrr_modeA_selacc": 0.8857, "clutrr_h2_absent_reduction": 0.4444, "clutrr_h2_ci95": [0.3167, 0.5833], "clutrr_goldread_oracle": "1.000@cov0.951", "clutrr_swipl": "40/40 executed, 39/40 surface-match gold", "clutrr_atomic_PRF1": [0.536, 0.532, 0.534], "fuzzy_cert_confident_wrong": "0.000 @cov 0.5351 spatial / 0.3139 kinship", "fuzzy_conf_baseline_cw_spatial": 0.4147, "fuzzy_conf_baseline_cw_spatial_ci": [0.376, 0.4566], "fuzzy_certificate_beats_spatial": true, "fuzzy_conf_baseline_cw_kinship": 0.3461, "fuzzy_conf_baseline_cw_kinship_ci": [0.2931, 0.4128], "fuzzy_certificate_beats_kinship": true, "modeB_catches": "5/5 spatial, 0/0 kinship"}

## TASK 4 (MINOR #4): venue reposition + scope boundaries

**Venue:** ACL Knowledge Extraction track → **NeSy / temporal-and-qualitative-reasoning (EMNLP / neuro-symbolic) track**. The substantive contribution is closure-certified DEDUCTION / CONSISTENCY, not extraction. Atomic extraction is MEASURED not improved (F1 ~0.534), so a knowledge-extraction track is a poor fit; EMNLP / NeSy / qualitative-reasoning audiences can deeply evaluate the relation-algebra + abstention contribution.

**Scope boundaries (abstract front-matter, each tagged SCOPE):**
- deduction sub-module only
- atomic extraction measured-not-improved (~0.53 recall, F1 0.534)
- OpenCyc / upper-ontology grounding OUT OF SCOPE
- composition tables HAND-SUPPLIED in every venue (Allen / point / RCC-8 published tables; CLUTRR rules_store.yaml)
- real-text utility extraction-limited (~0.53 recall => ~19% Mode-A coverage on dense prose)
- no benchmark doc reaches the goal ~3000-char target (CLUTRR <=871; spatial 130-1338)

**Operational ~3000-char study labels (art_WQoePKrpsTPo):**
- Temporal arm: 5 NarrativeTime articles BRACKET-selected around 3000 chars (NONE in [2500,3500]; mean 3050, range 2197-4293)
- Kinship arm: 3 docs CONCATENATED from disjoint-entity CLUTRR sub-stories (cross-story pairs absent-by-construction => trivially abstained)
- the iter-6 Re-DocRED corpus will supply genuinely-natural ~3000-char documents (PENDING)

## Headline-structure guidance for GEN_PAPER_TEXT

- Lead with the SINGLE certificate thesis: a structural, label-free certificate that catches confident relational hallucinations that a confidence threshold cannot see.
- Cross-path coding = ONE subordinate subsection (sec:decisive), framed as an explanatory account of two independently-violated conditions — NOT a co-headline, NOT a predictive law.
- Demote mechanism analysis (algebra-richness scaling, redundancy inverted-U, zero-FP theorem) to appendix rows.
- Report EVERY hallucination number WITH its coverage (e.g. 0.000 @cov 0.5351, not bare 0.000).
- Do NOT call CLUTRR natural text (templated, <=871 chars); do NOT call the operational 3000-char docs natural (bracket-selected temporal / concatenation-constructed kinship).
- Carry the fuzzy section on the Mode-B catch count (5/5 unsound spatial reads caught at ordinary confidence, 0 testable on kinship) rather than the 0.000-vs-0.364 always-answer contrast.
- The certificate beats the matched-coverage confidence-thresholded top-1 abstainer in BOTH fuzzy settings (spatial CW 0.415, kinship CW 0.346; both CIs exclude 0) — including well-calibrated kinship (ECE 0.051), because modest max confidence (0.8) + modest read accuracy keeps thresholded CW high. Report this as the edge-read-level finding, NOT as a tie.
- Always carry the unit-of-analysis caveat: certificate CW is on closure QUERIES, the confidence baseline CW is on edge READS (matched on coverage fraction, not object); a query-level confidence abstainer is the PENDING STEP-A experiment. Do not overstate the comparison as same-object beyond Mode-B.
