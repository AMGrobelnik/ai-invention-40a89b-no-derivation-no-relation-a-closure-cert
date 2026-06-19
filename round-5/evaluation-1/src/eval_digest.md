# iter-5 zero-spend re-analysis — paper-facing digest

**$0 LLM spend** (`llm_spend_usd`=0.0), numpy+scipy only, deterministic seed=20260617, **B=10000** paired bootstrap. Reproduction mismatches vs the validated iter-4 re-analysis: **0**.

This artifact EXTENDS the iter-4 re-analysis. It delivers two reviewer fixes for GEN_PAPER_TEXT: **MINOR #5** — the *small-bite* caveat (the cross-path mechanism's realized value is PRECISION of committed answers, not expanded coverage); and **MAJOR #3** — a single ONE-THESIS contribution table whose evidence-class tags are COLUMNS, not inline hedging.

## (a) Small-bite block — synthetic Allen positive control (recall 0.95, n=500 networks)

Tag: `SYNTHETIC-ALLEN-CONTROL`. Reproduction of the published `recall_95` cell: **PASS** (coverage-gain diff 0.0e+00 vs published; seed 20260712=20260617+95).

| Method | Coverage | Coverage 95% CI | Selective acc. | Selective-acc. 95% CI | n answered | n correct |
|---|---|---|---|---|---|---|
| intersection | 0.2500 | [0.2120, 0.2880] | 0.9760 | [0.9453, 1.0000] | 125 | 122 |
| best_single | 0.2260 | [0.1900, 0.2620] | 0.7168 | [0.6293, 0.7967] | 113 | 81 |
| naive | 0.3160 | [0.2760, 0.3580] | 0.8418 | [0.7823, 0.8978] | 158 | 133 |

**The contrast that retires the over-claim:**

- **Coverage gain** (intersection − best-single): **0.0240** (+2.4% abs), 95% CI [-0.0220, 0.0700], bootstrap p(gain≤0)=0.1703 → **CI INCLUDES 0** (the realized cross-path coverage bite is small AND not significantly above zero).
- **Selective-accuracy gain** (intersection − best-single): **0.2592** (+25.9 pts), 95% CI [0.1765, 0.3494], bootstrap p(gain≤0)=0.0000 → **CI EXCLUDES 0** (the precision win is real and large).
- Intersection precision (0.9760) exceeds BOTH best-single (0.7168) AND naive (0.8418) even though naive answers MORE (0.3160 coverage).

**Where the precision advantage comes from (auditable decomposition, not re-scoring):**

- Queries BOTH resolve (n=50): intersection narrows to the SAME singleton best-single found — **perfect agreement** (aligned acc-gain = 0.0000, CI [0.000, 0.000]).
- Queries only intersection resolves (cross-path bite, n=75): **0.96 correct**.
- Queries only best-single resolves (n=63): intersection COLLAPSES (abstains), **avoiding 32 wrong commitments** best-single makes.

> **Interpretation (deliverable framing).** Intersection sets are a SUBSET of best-single sets (tighter), so intersection mechanically resolves a SUPERSET of queries WHEN it does not collapse -- but the REALIZED coverage gain is only +2.4% absolute (0.250 vs 0.226), while the selective-accuracy gain is large (+25.9 pts; 0.976 vs 0.717) and intersection's precision (0.976) exceeds BOTH best_single (0.717) AND naive (0.842) even though naive answers MORE (0.316). Structurally the only resolution-axis win is a coverage superset, but its realized MAGNITUDE is tiny; the practically meaningful effect is PRECISION OF COMMITTED ANSWERS, not coverage expansion.

## (b) Inverted-U realized-coverage block (realism-matched channel, ρ=0, gate=off, n=600/bin)

Tag: `SYNTHETIC-CHANNEL`. Realized Mode-A coverage per redundancy bin recovered from the stored H4 curves as `realized_coverage = benefit + cost_silent_wrong = 1 − abstain − collapse` (identity verified to <1e-9).

| Recall | Peak K* | Realized cov. @peak | Cov. 95% CI @peak | Cov.-gain vs K=1 @peak | Gain 95% CI | Benefit (correct) @peak | Cost (silent-wrong) @peak |
|---|---|---|---|---|---|---|---|
| 0.500 | 2 | 0.575 | [0.535, 0.614] | 0.135 | [0.079, 0.190] | 0.295 | 0.280 |
| 0.625 | 4 | 0.555 | [0.515, 0.594] | 0.170 | [0.114, 0.225] | 0.407 | 0.148 |
| 0.780 | 7 | 0.702 | [0.664, 0.737] | 0.365 | [0.311, 0.416] | 0.680 | 0.022 |
| 0.900 | 10 | 0.907 | [0.881, 0.927] | 0.597 | [0.551, 0.638] | 0.905 | 0.002 |
| 0.950 | 16 | 0.968 | [0.951, 0.980] | 0.612 | [0.569, 0.651] | 0.968 | 0.000 |

- Peak K* by recall: **[2, 4, 7, 10, 16]** (interior inverted-U, peak shifts outward with recall).
- Silent-wrong (pooled) across recall: **0.0064 → 0.1456** (monotone-decreasing in recall); Page trend ~5e-4 (NOT the paper's earlier mis-stated 1e-13).

> **Recall-dependence (do NOT over-claim 'modest everywhere').** Realized-coverage gain over K=1 is RECALL-DEPENDENT, not uniformly modest: at the peak it rises from +0.135 (recall 0.50, where cost_silent_wrong 0.280 ~= benefit) to +0.612 (recall 0.95, cost ~0.000). The LARGE coverage gains live only in the high-recall regime where reads are near-sound -- exactly the regime LLMs do NOT reach on natural Allen text (the cross-path-bite experiment found per-edge reads near-universe / underdetermined). In the achievable regime (recall <=~0.85, and on Allen near-universe) the realized coverage bite is small.

> **K=1-vs-best-single caveat.** K=1 in the H4 channel is a SINGLE (arbitrary) contributing path, so coverage_gain_vs_K1 conflates redundancy with best-path SELECTION and OVERSTATES the cross-path bite. The conservative apples-to-apples measure is intersection vs the STRONGEST single path (best_single = min-cardinality composition): the synthetic Allen control gives only +0.024 there at recall 0.95 (bootstrap CI INCLUDES 0), while its selective-accuracy gain +0.259 is strongly significant. Both analyses agree: the practical value is PRECISION of committed answers, not coverage expansion.

> **Tempered interpretation.** The inverted-U on RESOLUTION (benefit) conflates two effects -- higher recall AND added redundancy. Decomposing onto the COVERAGE axis (realized coverage = benefit + cost_silent_wrong = 1 - abstain - collapse) shows that redundancy's realized coverage gain over K=1 is offset by a rising silent-wrong cost at low recall (cost grows with K as J(E) decays, then collapse dominates and coverage FALLS); the large coverage gains appear only at high recall (near-sound reads). Measured against the STRONGEST single path rather than an arbitrary K=1 path, the realized cross-path coverage bite is small (synthetic Allen control +2.4%, CI includes 0). The net practical value of the coding mechanism is therefore improved PRECISION of committed answers (fewer wrong singletons among those it commits to), not expanded coverage. Temper any 'expanded coverage' phrasing accordingly.

## (c) ONE-THESIS contribution table (evidence tags as COLUMNS)

Lead the paper with the two SPINE rows; demote the scaling-law / inverted-U to SUPPORTING; leave the spatial-RCC-8 row as a PENDING slot; keep temporal-marginal and scope as FOOTNOTES.

### SPINE (lead with these two rows)

| claim | evidence tag | where it holds | status | key numbers |
|---|---|---|---|---|
| Training-free, gold-free, per-edge ABSTAIN-ON-COLLAPSE certificate over LLM-extracted relational facts: keep the LLM a high-recall disjunctive reader, compose ONLY through exact relation-algebra tables, EMIT a singleton / ABSTAIN on residual disjunction / FLAG unsound read on empty closure. Confirmed at power end-to-end on templated CLUTRR. | REAL-LLM-READ + THEOREM(zero-FP conditional on read soundness) | templated-CLUTRR (<=871 chars) end-to-end; weakly protective on natural temporal text | CONFIRMED-AT-POWER | `modeA_selacc`=0.8857; `vs_pot_gap`=0.4286; `vs_pot_ci95`=[0.2986, 0.5630]; `vs_sc_gap`=0.3286; `vs_raw_gap`=0.3429; `holm_p_adj`=0.0015; `h2_absent_reduction`=0.4444; `h2_ci95`=[0.3167, 0.5833]; `h2_p_one_sided`=0.0005; `goldread_oracle_selacc`=1.0000; `oracle_coverage`=0.9510; `oracle_raw_selacc`=0.4330; `swipl_engine_match`=40/40; `swipl_gold_match`=39/40; `atomic_PRF1`=[0.5360, 0.5320, 0.5340] |
| A quantitative law for WHEN cross-path qualitative-algebra coding can be read off text: richer algebra gives an exact table more headroom but lets an LLM read constituent relations LESS informatively -- high-recall disjunctive reads are sound but near-universe (no intersection bite); forcing tight reads is ~3% correct (unsound). On temporal Allen, intersection/best-single/naive all resolve 0/125 gold-singleton multi-path queries; the synthetic Allen positive control PASSES at recall 0.95, localizing the cause to read-informativeness, NOT closure. | REAL-LLM-READ + GOLD-ONLY-GATE + SYNTHETIC-ALLEN-CONTROL | natural temporal text (TDDMan gold-singleton multi-path N=125) | CONFIRMED-AS-CHARACTERIZATION | `gold_singleton_multipath_N`=125; `intersection_resolved`=0/125; `best_single_resolved`=0/125; `naive_resolved`=0/125; `holm`=n.s.; `per_edge_allen_recall`=0.9000; `recall_gate`=0.8500; `event_local_underdet_rate`=0.8700; `window_underdet_rate`=0.7900; `breadth`=11.5/13; `deepseek_underdet_rate`=0.9900; `deepseek_breadth`=12.9/13; `tight_raw_allen_correct`=0.0320; `intersection_commit_confident_wrong`=1.0000; `synth_control_recall95_intersection_cov`=0.2500; `synth_control_best_single_cov`=0.2260; `synth_control_co … |

### SPINE-PENDING (the deciding row — reserve as a slot for the iter-5 experiment)

| claim | evidence tag | where it holds | status | key numbers |
|---|---|---|---|---|
| DECISIVE iter-5 open experiment: cross-path INTERSECTION on the gated spatial RCC-8 venue (SpaRTUN) -- does it narrow beyond best-single-path at power where constituent relations (containment/connection) may read locally? FORK: narrows -> first real-venue POSITIVE for the coding mechanism; also underdetermines -> SECOND decisive negative, drop cross-path coding from the headline. | SYNTHETIC-CHANNEL -> REAL(ISTIC)-LLM-READ (PENDING) | spatial RCC-8 SpaRTUN (gated 27.4% tight-bite, GENERAL band; tables engine-validated) | PENDING - NOT YET RUN (slot to be filled by iter-5 experiment) | `spartun_tight_bite_fraction`=0.2740; `rcc8_table_validated`=True; `projection_cardinal_is_product_of_two_point_algebras`=True |

### SUPPORTING (mechanism analysis — demote here)

| claim | evidence tag | where it holds | status | key numbers |
|---|---|---|---|---|
| The scaling-law engine behind SPINE-2 first half: with real LLM reads on synthetic NL the advantage over PoT grows monotonically with base-relation count -- point(3) +0.043 -> RCC-8(8) +0.448 -> Allen(13) +0.676. This is the INHERITED exact-table-vs-LLM-composition effect at recall ~1.0 on templated NL (the standard NeSy premise), NOT this work's novel coding mechanism. On Allen the +0.676 DECOMPOSES into inherited +0.673 + novel-on-selective-accuracy +0.0025 (~0). | REAL-LLM-READ-ON-SYNTHETIC | synthetic/templated NL | SUPPORTING (inherited premise; RCC-8/Allen are SOUND LOWER BOUNDS, PC incomplete) | `point3`=0.0430; `rcc8_8`=0.4480; `allen13`=0.6760; `allen_inherited`=0.6730; `allen_novel_selacc`=0.0025; `provenance`=point(+0.043) and RCC-8(+0.448) carried as CITED literals from hypothesis CLAIM 5a (art_QToTkRe6Umb8, algebra-richness scaling -- NOT a dependency of this eval); NOT recomputed here. Allen +0.676 = inherited 0.673 + novel 0.0025 reproduced in iter-4 eval metadata.decomposition.allen_carried_forward. |
| On a realism-matched channel iterated closure error-corrects per recall slice (H3 Page p~5e-4, length-2 tie growing with hop/cyclomatic) and net Mode-A resolution is a recall-dependent inverted-U (peak K*=2,4,7,10,16 for recall 0.5->0.95); silent-wrong rises 0.006->0.146 bounded by (1-r) and (1-J(E)). CRITICAL CAVEAT: realized cross-path COVERAGE bite is SMALL -- intersection adds only ~+2.4% coverage over best-single (synthetic Allen control); the mechanism's practical value is PRECISION of committed answers, not expanded coverage. | SYNTHETIC-CHANNEL + THEOREM(zero-FP on all-sound networks) | synthetic-channel only | SUPPORTING (recall & rho are CONTROLLED INPUTS; does NOT predict a real-text operating point) | `peak_K_by_recall`=[2, 4, 7, 10, 16]; `silent_wrong_range`=[0.0064, 0.1456]; `page_p_corrected`=0.0005; `realized_coverage_bite_vs_best_single`=0.0240; `max_realized_coverage_gain_vs_K1`=0.6117; `zero_FP_theorem_networks`=100296 |

### FOOTNOTES / CEILING (state beside claims, in abstract/intro)

| claim | evidence tag | where it holds | status | key numbers |
|---|---|---|---|---|
| On NATURAL temporal text the matched-coverage Mode-A advantage is MARGINAL and NOT robustly significant: corrected fixed-operating-point CIs bracket the point gaps but INCLUDE ZERO; neither H1 gateway clears Holm; the earlier published CONFIRM was a bootstrap artifact. Raw OUT-accuracies Mode-A by 0.124 at matched coverage; among the ~19% Mode-A commits to it is confident-wrong 42.5% (48/113), ALL silent-wrong-narrowing. | REAL-LLM-READ | natural temporal (NarrativeTime+TDDMan) | MARGINAL / CERTIFICATE-ONLY VALUE | `vs_pot_gap`=0.0265; `vs_pot_corrected_ci95`=[-0.0883, 0.1397]; `vs_pot_boot_p`=0.3322; `vs_sc_gap`=0.0354; `vs_sc_corrected_ci95`=[-0.0614, 0.1347]; `holm_p_adj`=0.5186; `confident_wrong_among_answered`=48/113=0.425; `modeA_coverage`=0.1883; `raw_out_accuracy_gap`=-0.1240 |
| Contribution is the DEDUCTION SUB-MODULE only: atomic extraction MEASURED not improved (~0.53 recall => ~19% Mode-A coverage on natural text); OpenCyc grounding, atomic re-extraction, general LLM fuzzy-unification OUT OF SCOPE; composition table HAND-SUPPLIED in every venue; NO document reaches ~3000 chars (CLUTRR <=871; spatial 130-1338). | SCOPE | all venues | CEILING (state in abstract/intro) | `atomic_recall`=0.5324; `modeA_real_text_coverage`=0.1883; `clutrr_max_chars`=871; `spatial_char_range`=[130, 1338] |

> **Tagging policy.** Every row carries an evidence_tag COLUMN drawn from {THEOREM, SYNTHETIC-CHANNEL, SYNTHETIC-ALLEN-CONTROL, GOLD-ONLY-GATE, REAL-LLM-READ, REAL-LLM-READ-ON-SYNTHETIC, SCOPE, EXPLORATORY}; provenance is legible at a glance, NOT buried in inline hedging.

## (d) Headline-structure guidance for GEN_PAPER_TEXT

- **I.** LEAD abstract/intro/title with the two-row SPINE (the certificate + the read-informativeness impossibility); DEMOTE the 5-claim 'honest split' to ONE mechanism-analysis section.
- **II.** Put evidence tags in TABLE COLUMNS (claim | evidence_tag | where_it_holds | status | key_numbers), NOT inline prose hedging.
- **III.** The spatial RCC-8 SpaRTUN fork is the SINGLE decisive open experiment -- reserve the SPINE-PENDING row as a slot.
- **IV.** Re-title around 'closure-certified DEDUCTION SUB-MODULE' (NOT an end-to-end text-to-FOL system).
- **V.** Report every hallucination number WITH its coverage/abstention (e.g. H2 reduction 0.444 @ Mode-A coverage 26.6%; temporal confident-wrong 42.5% @ coverage 18.8%).
- **VI.** Do NOT call CLUTRR natural text -- it is a TEMPLATED kinship benchmark (<=871 chars, gold surface forms, hand-supplied table).

### Carried (re-affirmed, not recomputed)
- **Corrected temporal (REAL-LLM-READ).** Neither H1 gateway clears Holm; vs-PoT gap 0.0265 corrected CI [-0.0883, 0.1397] (includes 0, boot_p 0.3322); the published CONFIRM was a bootstrap artifact. Among the 0.188 Mode-A commits, confident-wrong 0.4248 (48/113), all silent-wrong-narrowing; raw out-accuracies Mode-A by 0.124 at matched cov.
- **Deduction-sub-module ceiling (SCOPE).** Atomic recall 0.5324 → ~0.188 Mode-A coverage on natural temporal text; OpenCyc / atomic re-extraction / LLM fuzzy-unification OUT OF SCOPE; composition table hand-supplied; no venue reaches the ~3000-char target (CLUTRR ≤871; spatial 130–1338).

### Datasets carried for per-record evidence
- `synthetic_allen_control_worked` — 8 examples.
- `clutrr_templated_kinship` — 282 examples.
- `temporal_point_algebra_natural_text` — 600 examples.
