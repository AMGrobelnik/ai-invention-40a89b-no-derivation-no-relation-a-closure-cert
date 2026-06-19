# Zero-LLM-spend re-analysis digest (paper-facing)

**$0 LLM spend.** numpy+scipy only. seed=20260617, B=10000, doc/story-clustered paired bootstrap.
Temporal per-query records rebuilt by a **$0 cached re-run** (total_cache_misses=0, primary_cost=0.0, 600 records; reproduced aggregates match published exactly). Reproduction mismatches vs source: **0**.

Evidence tags: REAL-LLM-READ · REAL-LLM-READ-ON-SYNTHETIC · SYNTHETIC-CHANNEL · GOLD-ONLY-GATE · THEOREM · EXPLORATORY

## R1 — Bracketing CI on the temporal Mode-A-vs-PoT gap (REAL-LLM-READ)

**Root cause.** method.py:531-563 matched_coverage_gap re-derived the TARGET coverage mc from each resample (line ~548 'mp,mc,ma=_curve(mrec)') and interpolated the baseline at that VARYING mc (line ~550 'ba=_acc_at_coverage(bp,mc)'). The resampled gap is therefore a DIFFERENT estimator than the headline gap; on the volatile low-coverage PoT curve the distribution recenters (~0.18) so the published vs-PoT CI [0.0454,0.3148] does NOT contain the observed point gap +0.0265. Holding the operating point FIXED across resamples (Mode-A's fixed answered set vs PoT's fixed top-k-by-conf matched set) yields a CI that BRACKETS +0.0265.

**Fix.** Hold the matched-coverage operating point FIXED across resamples: Mode-A's fixed answered set vs the baseline's fixed top-k-by-conf matched set; recompute both accuracies over those FIXED sets in each doc-clustered resample (do NOT re-derive the coverage/threshold inside the bootstrap).

| baseline | point gap | published OLD CI (B=2000) | OLD brackets? | NEW bracketing CI (B=10000) | NEW brackets? | corrected boot_p | corrected sig? |
|---|---|---|---|---|---|---|---|
| vs POT | +0.0265 | [0.0454, 0.3148] | False | [-0.0883, 0.1397] | **True** | 0.3322 | False |
| vs SC | +0.0354 | [0.0161, 0.2963] | True | [-0.0614, 0.1347] | **True** | 0.2593 | False |
| vs NAIVE | +0.0265 | [-0.0068, 0.0834] | True | [-0.0096, 0.0635] | **True** | 0.0878 | False |
| vs RAW | -0.1239 | [-0.2130, 0.0325] | True | [-0.2282, -0.0317] | **True** | 0.9962 | False |

The published **vs-PoT** CI [0.0454, 0.3148] does NOT contain its own point gap +0.0265 (estimator/resample mismatch); the corrected CI **[-0.088276, 0.139723] brackets +0.0265**. The plan's 'equivalent' fixed-m_cov interpolation variant also BRACKETS the point (vs-PoT [0.022453, 0.336686]) but disagrees on significance (see honest finding below).

> **Honest finding (R1).** IMPORTANT (honest re-analysis result): once the operating point is held FIXED, the corrected doc-clustered CIs are centered on the true point gaps and BRACKET them, but they are WIDE and INCLUDE 0 for both H1 gateways -- vs PoT new_ci=[-0.088276, 0.139723] (boot_p=0.3322), vs SC new_ci=[-0.061388, 0.134703] (boot_p=0.2593). The published Holm-significance (boot_p 0.007 / 0.0185, CI ENTIRELY above 0 yet EXCLUDING the point estimate) was an ARTIFACT of the same estimator/resample mismatch: the buggy bootstrap recentered on the volatile low-coverage baseline curve (~0.18), simultaneously inflating the gap magnitude AND its apparent significance. The plan's 'equivalent' fixed-m_cov INTERPOLATION variant (which RE-SELECTS the baseline matched set within each resample) gives vs-PoT [0.022453, 0.336686] (boot_p 0.0114) -- borderline, lower bound just above 0, but it retains RESIDUAL interpolation volatility (its upper bound ~0.34 echoes the buggy ~0.31), so the literal fixed-SET estimator (which pins the specific top-k matched queries per the plan's 'do NOT re-derive the threshold' instruction) is the PRIMARY. CONCLUSION: significance is ESTIMATOR-DEPENDENT and FRAGILE -- on natural temporal text the Mode-A selective-accuracy advantage over PoT/SC is MARGINAL and NOT robustly significant under a correctly-centered bootstrap (~36 doc clusters, SE~0.06); it is NOT the robust CONFIRM the published boot_p implied. The transferable temporal contribution is the gold-free abstain-on-collapse CERTIFICATE, NOT selective-accuracy dominance. vs-naive (boot_p 0.088) and vs-raw (gap -0.124) are consistent before and after the fix.

Holm over the CORRECTED {vs PoT, vs SC} family: {'H1_vs_SC': 0.5186, 'H1_vs_PoT': 0.5186} → neither gateway clears after correction.

## R2 — CLUTRR naive natural-vs-forced coverage; iteration routed through COVERAGE (REAL-LLM-READ)

| naive operating point | coverage | selective accuracy | note |
|---|---|---|---|
| natural | 0.216 (22/102) | 0.727 (16/22) | predominantly hop-2; single-pass intersection resolves |
| matched / force-extended | 0.686 | 0.229 | **FORCE-EXTENDED with representative-surface answers** |

> naive matched-coverage selective accuracy (0.229 @ cov 0.686) is FORCE-EXTENDED beyond naive's natural coverage 0.216 (22/102 answered, predominantly hop-2) with representative-surface answers; the natural-coverage figure (selacc ~0.73 @ cov 0.216) is reported alongside. The '0.229 -> 0.886' contrast must NOT be read as the iteration result.

**Iteration (H3) via the COVERAGE axis** (full_minus_naive coverage gap by hop): hop2:0.0, hop3:0.5862, hop4:0.25, hop5:0.75, hop6:0.75, hop7:0.625, hop8:0.25, hop9:0.875, hop10:0.375.
full iterated closure resolves a strictly larger COVERAGE fraction than naive single-pass for hop>=3 (0.0@hop-2 -> 0.586@hop-3 -> up to 0.875@hop-9); naive single-pass resolves only hop-2. Route the CLUTRR H3 (iteration) claim through the coverage axis, NOT the forced selective-accuracy gap.

**Legitimate matched-coverage leaderboard** (cov 0.686): Mode-A 0.886 vs PoT 0.457 / SC 0.557 / raw 0.543; naive row = 0.229 (FORCE-EXTENDED). Corrected fixed-set gaps (B=10000): vs PoT +0.4286 [0.298589, 0.563015], vs SC +0.3286 [0.202937, 0.453127], vs raw +0.3429 [0.222279, 0.464956]; Holm p_adj 0.001499.

## The 42.5% (48/113) confident-wrong-among-answered block (REAL-LLM-READ)

> On natural temporal text, among the ~19% of queries Mode-A commits to, it is CONFIDENT-WRONG 42.5% (48/113). REPORT THIS BESIDE EVERY TEMPORAL CLAIM. Mechanism: silent-wrong-narrowing -- when gold is OMITTED from a contributing local read, closure narrows to a confident WRONG singleton with NO empty collapse, so Mode-B cannot flag it; ALL 48 Mode-A confident-wrongs are of this type. Bounded per-edge by (1-recall) and per-network by (1-J(E)). Hence 'faithfulness-by-abstention' is WEAKLY protective on dense temporal prose (~0.85 recall): raw actually out-accuracies Mode-A at matched coverage by 0.124. The temporal value of Mode-A is the gold-free certificate + abstention-as-an-OPTION, NOT selective-accuracy dominance, and even that is bounded by read recall.

- confident-wrong among Mode-A answered: **0.4248 (48/113)**; Mode-A coverage 0.1883 (abstention 0.8117); raw confident-wrong 0.61.
- reduction vs raw 0.1852 (published CI [0.08645, 0.281589]; recomputed B=10000 0.1827 [0.086829, 0.280125]).
- silent-wrong-narrowing: **all 48** Mode-A confident-wrongs are silent-wrong-narrowing (undetectable by Mode-B: no empty collapse).
- raw out-accuracies Mode-A at matched coverage by 0.124 (gap -0.124).

**Read-soundness frontier (REAL-LLM-READ):**
| corpus×reader | recall | CI95 | gate verdict |
|---|---|---|---|
| narrativetime_primary | 0.8564 | [0.832, 0.880] | CI_excludes_below_gate |
| narrativetime_strong | 0.9317 | [0.888, 0.967] | CI_contains_gate |
| tddman_primary | 0.8279 | [0.778, 0.869] | CI_excludes_below_gate |
| tddman_strong | 0.8187 | [0.727, 0.897] | CI_excludes_below_gate |

ρ within-doc soundness ∈ [0.002828, 0.167214]. **$0 synthetic backstop (SYNTHETIC-CHANNEL, recall 0.96): mean Mode-A vs raw +0.225** → read soundness (not closure) is the real-text gate.

## Inherited-vs-novel decomposition

**CLUTRR (REAL-LLM-READ, templated):** system_gap(ModeA−PoT)=+0.429 = INHERITED(naive−PoT)=-0.229 + NOVEL(ModeA−naive)=+0.657. ⚠ naive@matched (0.229) is FORCE-EXTENDED, so this additive split mis-attributes: the negative 'inherited' (-0.229) and inflated 'novel' (+0.657) are ARTIFACTS of force-extending naive's coverage with representative-surface (wrong) answers. naive single-pass CANNOT iterate, so it is a poor proxy for the inherited exact-table composition advantage on CLUTRR.
> On CLUTRR the Mode-A advantage is realized through ITERATED exact-table composition over multi-hop chains (naive single-pass resolves only hop-2). The actionable inherited part is the STANDARD neuro-symbolic premise 'use exact composition tables instead of LLM composition' -- NOT this work's discovery; the novel cross-path-INTERSECTION mechanism is NOT what drives CLUTRR (kinship is a single-chain forward UNION fixpoint, no involutive converse).

**TEMPORAL (REAL-LLM-READ, point algebra):** on the covered-by-BOTH subset (n=107) NOVEL_selacc = ModeA 0.570 − naive 0.561 = **+0.009** [0.0, 0.032609] (pred disagreements: 1). On the SELECTIVE-ACCURACY axis the temporal iteration/novel term is ~0 (covered-by-both novel_selacc ~0); INHERITED (naive-PoT) is also ~0 at matched coverage. The matched-coverage system gap +0.0265 is MARGINAL and reflects Mode-A's higher accuracy on its low-coverage answered set, not iteration. Iteration's value (where any) is on the COVERAGE axis (ge3_cyclic +0.042, p=0.061, NS).
Iteration on coverage: len2 gap 0.0 (0 by theorem); ge3_cyclic gap +0.0417 [0.0, 0.10531] (p=0.06105, EXPLORATORY, NS).

**ALLEN (REAL-LLM-READ-ON-SYNTHETIC, carried from iter-2 Allen experiment art_N0e4pH_C_Cxw (carried via art_D0cHQUJ8kY75); NOT a dependency of this eval):** system_gap 0.676 = INHERITED 0.673 + NOVEL_selacc 0.0025. Independent recompute (covered-by-both novel_selacc) = +0.0000 ✓.

> The INHERITED part (exact composition table vs LLM per-path composition) is the STANDARD neuro-symbolic premise, not this work's discovery. The NOVEL-on-selective-accuracy term (cross-path iterated intersection) is ~0 on both available algebras.

## Contribution split — TRANSFERABLE-AT-POWER vs SYNTHETIC-CHANNEL-ONLY (headline deliverable)

| # | Claim | Tag | Venue | Where it holds | Key number |
|---|---|---|---|---|---|
| T1 | CLUTRR Mode-A selective accuracy vs PoT / SC / raw at matched coverage 0.686 -- inherited exact-table multi-hop composit | REAL-LLM-READ | templated-CLUTRR | TRANSFERABLE-AT-POWER | modeA_selacc=0.8857; vs_pot_gap=0.428571; vs_pot_ci95=[0.298589, 0.563015] |
| T2 | CLUTRR H2 absent-relation confident-wrong (hallucination) reduction vs raw, risk-coverage on mixed n=282 pool (Mode-A an | REAL-LLM-READ | templated-CLUTRR | TRANSFERABLE-AT-POWER | reduction=0.4444; ci95=[0.3167, 0.5833]; p_one_sided=0.0005 |
| T3 | CLUTRR gold-read ORACLE: Mode-A 1.00 selective accuracy @ coverage 0.951 vs 0.433 raw/PoT -- closure is NOT the bottlene | REAL-LLM-READ | templated-CLUTRR | TRANSFERABLE-AT-POWER | oracle_modeA_selacc=1.0; oracle_coverage=0.95098; oracle_raw_selacc=0.433 |
| T4 | CLUTRR multi-hop accuracy ~0.80-1.00 through hop-10 while raw->0.0 / PoT->0.2; SWI-Prolog discharge executed | REAL-LLM-READ | templated-CLUTRR | TRANSFERABLE-AT-POWER | hop10_modeA_selacc=1.0; hop10_raw_selacc=0.0; hop10_pot_selacc=0.2 |
| T5 | Gold-free, training-free, per-edge ABSTAIN-ON-COLLAPSE certificate (Mode-B conflict detection) -- the genuinely portable | THEOREM | natural-temporal + templated-CLUTRR | TRANSFERABLE-AT-POWER | clutrr_prolog_collapse_certified=True; temporal_worked_collapse_certified=True; zero_FP=conditional on read soundness (THEOREM-grade engine; empirical recall ~0.53-0.86) |
| M1 | TEMPORAL Mode-A vs PoT / SC selective-accuracy at matched coverage on NATURAL text -- the point gaps reproduce (+0.0265  | REAL-LLM-READ | natural-temporal | MARGINAL-NATURAL-TEXT (not significant after correction) | vs_pot_gap=0.026549; vs_pot_corrected_ci95=[-0.088276, 0.139723]; vs_pot_corrected_boot_p=0.3322 |
| S1 | Cross-path INTERSECTION error-correcting-code mechanism + inverted-U redundancy optimum (recall & rho are CONTROLLED INP | SYNTHETIC-CHANNEL | synthetic-channel | SYNTHETIC-CHANNEL-ONLY | carried_from=art_FtN4LBzazO_l; clutrr_is_single_chain_UNION_fixpoint=True; clutrr_pc2_converse_intersection_UNSOUND_collapse_rate=~13% of gold-clean chains |
| S2 | Synthetic backstop: Mode-A beats raw by ~+0.225 at matched coverage at recall 0.96 (mechanism works when local reads are | SYNTHETIC-CHANNEL | synthetic-channel | SYNTHETIC-CHANNEL-ONLY | mean_vs_raw_gap=0.225228; recall=0.96; cells={'R_redundancy_K4': 0.218589, 'R_redundancy_K8': 0.259516, 'H_hop_L4_C2': 0.211268, 'H_hop_L6_C3': 0.211538} |

> The prior reviewer's 'central comparative contribution is synthetic-only' concern is RECAST, NOT retired. The signature cross-path-intersection coding mechanism remains synthetic-channel-only (CLUTRR is a single-chain UNION fixpoint; temporal iteration is NS at power). The iter-4 DECISIVE experiment -- cross-path INTERSECTION vs best-single-path composition on a REAL multi-path-redundant stratum with adjusted-CI separation -- is what would move the SYNTHETIC-CHANNEL-ONLY rows.

## Scope-framing guidance for GEN_PAPER_TEXT

1. **CLUTRR re-tag:** RE-TAG CLUTRR as a 'templated kinship benchmark (semi-synthetic)': max 871 chars (NONE reach the ~3000-char target), gold surface forms for entity grounding, hand-supplied composition table. The abstract must NOT say 'two non-synthetic venues' -- only the temporal corpora are natural text, and there the comparative contribution is MARGINAL (+0.0265; the CORRECTED bracketing CI INCLUDES 0 / boot_p~0.33, NOT robustly significant -- the published Holm-significance was a bootstrap artifact, see R1). Lead the natural-text story with the CERTIFICATE, not selective-accuracy dominance.
2. **Deduction sub-module scope:** Foreground the DEDUCTION-SUB-MODULE scope: OpenCyc grounding, atomic re-extraction, and LLM fuzzy-unification are OUT OF SCOPE. Real-text utility is EXTRACTION-LIMITED: ~0.53 atomic recall -> ~19% Mode-A coverage on natural temporal text.
3. **Multiplicity policy:** Re-affirm H1-H4 Holm / hierarchical gatekeeping: H1 (matched-coverage advantage) and H2 (hallucination reduction) are GATEWAYS; H3 (iteration) / H4 tested only if a gateway clears; everything else EXPLORATORY with nominal CIs (len2/ge3_cyclic strata, coverage-axis iteration).
4. **Re-title:** Recommend re-titling the paper to center 'closure-certified deduction sub-module' (not an end-to-end text-to-FOL system): the substantive, transferable contribution is the gold-free abstain-on-collapse certificate over a deduction sub-module, evaluated at power on a templated benchmark and marginally on natural temporal text.
