# Decisive real-text test: cross-path Allen-13 intersection vs best-single-path

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** experiment  
**ID:** `art_0AIWMhwc1pJM`

## Layman Summary

Tests whether combining several reasoning paths (instead of the single best one) lets a logic reasoner pin down event orderings in real news text, and finds it cannot because language is too vague.

## Full Summary

THE decisive iter-4 experiment retiring reviewer MAJOR #1 (the cross-path-intersection mechanism was synthetic-only in iter-3). It tests, at statistical power on frozen real temporal gold graphs (NarrativeTime + TDDMan + MATRES), whether the cross-path full-PC INTERSECTION of disjunctive LLM Allen-interval reads narrows deduction-required queries strictly BEYOND the best-single-path composition, using the FULL Allen-13 algebra (not iter-3's coarse point projection that made full==naive).

VERDICT = SCOPE-BOUNDARY (powered, n=125 TDDMan gold-singleton headline queries; ~$0.94 LLM spend, hard-guarded <$9). Three converging, pre-registered results:
(1) STEP-1 a-priori GATE = GO (zero-LLM): the coding STRUCTURE exists in gold — combined gold-singleton multi-path-with-bite N=125 (TDDMan; NarrativeTime 0 because its dense start-point gold is structurally DISJUNCTIVE — explaining iter-3's full==naive; MATRES 0, confirming the gate is discriminative). Gold bite hist {2:62, 4:63}; power/MDE table included.
(2) Synthetic Allen POSITIVE CONTROL: on consistent-by-construction Allen QCNs with a noisy reader channel, intersection beats best-single at reader-recall 0.95 — the comparison code detects a true effect when reads are sound.
(3) REAL TEXT fails for a sharply localized reason: LLM Allen reads of constituent edges are near-universe/underdetermined across BOTH read regimes (event-local AND wider inter-event window) and BOTH readers (gemini-3.1-flash-lite underdet-rate 0.79; the STRONGER cross-family deepseek-v3.2 underdet-rate 0.99, breadth 12.9/13 — MORE conservative, so NOT a weak-model artifact). Composition of near-universe sets stays at the universe -> zero realized bite -> intersection/best-single/naive all resolve 0/125. Per-edge Allen recall 0.90 clears the 0.85 gate, but only because near-universe reads trivially contain gold (breadth, not soundness, is the issue).

KEY INSIGHT (precision/recall impossibility): high-recall disjunctive reads are SOUND but bite-free; forcing a single tight Allen relation (the raw baseline) is tight but only ~3% correct (UNSOUND). Text underdetermines interval endpoints, so no reader operating point yields tight-AND-sound Allen reads — the richer algebra that ENABLES intersection bite (gate GO) is exactly the one LLMs cannot read informatively. This extends iter-3's read-soundness finding to the Allen setting. The few times intersection committed to a singleton it was wrong (confident-wrong=1.0): an auditable silent-wrong-narrowing failure mode, shown in runnable Prolog trace-graphs (python-checker fallback; swipl absent here, reported truthfully; traces reproduce the engine intersection exactly).

DELIVERABLES for GEN_PAPER_TEXT: method.py (driver: gate->reads->matched-coverage comparison with the R1 BRACKETING-CI fix that flags any CI excluding its own point, Holm-adjusted over {intersection_vs_best_single, intersection_vs_naive, intersection_vs_PoT}); gate.py (a-priori multi-path gate, cached); allen_layer.py (Allen-13 token map, prompts, parser); synth_allen.py (positive control). method_out.json (schema exp_gen_sol_out, validated) carries: a_priori_gate (per-corpus N, prevalence, bite_hist, gold-singleton, singleton-resolvable, ge3-stratum, power_MDE, MATRES validation, gate_decision), read_conditions + read_informativeness_localization (3 conditions), per_edge_recall (recall/CI/rho/breadth/gate_verdict), leaderboard (5 contrasts with gap_point/gap_ci95/gap_bootstrap_median/brackets/boot_p), holm, singleton_resolution_rates, set_tightening_secondary, precision_recall_impossibility, cross_family_sensitivity, narrativetime_descriptive, synthetic_allen_control, worked_examples_prolog, stratified_exploratory, cost, verdict + rationale + honesty_caveats; datasets carry 125 TDDMan + 40 NarrativeTime per-query examples with predict_* and metadata_* fields. 3 figures (intersection-vs-best-single risk-coverage, gold-gate bite histogram, realized-bite-vs-paths). Transferable contribution surviving the negative: inherited exact-table composition + the gold-free abstain-on-collapse certificate; the cross-path coding mechanism is honestly synthetic-channel-only on these temporal corpora, with the multi-path-richer RCC-8 spatial venue recommended for iter-5.

## Dependencies

- `art_PNrS9T8JeATf` — dataset
- `art_aQ2Rf8rwqteI` — engine-specs

## Output Files

- `method.py`
- `full_method_out.json`
- `mini_method_out.json`
- `preview_method_out.json`

## Demo Files

- **method.py** — Research methodology implementation

---
*Generated by AI Inventor Pipeline*
