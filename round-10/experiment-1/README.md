# Supervised located_in extractor vs closure certificate: a net-utility boundary test

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** experiment  
**ID:** `art_fg_Yo5LRCY2d`

## Layman Summary

Trains a precise place-containment extractor and feeds it to a logical reasoner; shows that even a much better extractor cannot make the certificate beat simple confidence baselines on tricky sibling places.

## Full Summary

Artifact S_supervised replaces iter-9's refuted prompt-only LLM extraction with a TRAINED, threshold-tunable, precision-preserving located_in extractor built two independent ways and feeds its edges into the FROZEN closure-certificate engine (kinship.py forward-union, held_out direct-edge ablation) at 10 precision-preserving operating points on the natural Re-DocRED located-in corpus. ONLY the extraction step changes; the certificate engine and ALL 6 confident-wrong competitors (4 dispersion signals verbalized/SC-margin/Kadavath-P(True)/semantic-entropy + 2 query-side verifiers) are reused VERBATIM from core.py (the iter-8 method.py) and REPLAYED byte-identical at $0 from the merged SHA-256 cache (snapshot vs iter-8 FROZEN8 = 1215/1215 joined, 0 mismatch). Cost $0.00 (18722 cache hits, 0 LLM calls).

EXTRACTOR (extractor.py): binary located_in(i,j) over ORDERED gold-entity pairs co-occurring within W=2 sentences (NO grounding step / no grounding loss, the structural advantage over prompt-only); 2-cycles resolved by higher calibrated prob; isotonic-calibrated on a doc-disjoint within-train fold so tau maps to precision. Two families both exposing extract_supervised(ctx,tau): (A) GBDT = calibrated LightGBM over ~30 engineered per-pair features (cue counts, admin-level ordinal, appositive, substring, degree); (B) Encoder = fine-tuned microsoft/deberta-v3-small over marked windows [E1]..[/E1]/[E2]..[/E2], bf16. Trained doc-disjoint (2321 train docs vs 283 eval docs; leakage guard asserts disjointness + reports fold histograms).

EVAL POOL reproduces iter-8 exactly: 515 present / 450 same_component_sibling-absent / 250 different_component-absent over 283 docs (SEED=20260618, targets 400/450/250; counts MATCH FROZEN8). Gold-read ceiling held constant at 1.0/1.0/1.0 (present-coverage / sibling-abstain / selective-accuracy), proving all headroom is in extraction.

RESULT = NET-UTILITY-BOUNDARY-STRUCTURAL (robust across BOTH families). The supervised extractor DOMINATES iter-9's prompt-only frontier in precision/recall space (GBDT recall 0.155@precision 0.80 vs prompt-only 0.665@0.148; encoder recall 0.46@0.86 and max recall 0.65, operating STRICTLY BEYOND the prompt-only ceiling of 0.227), yet NO operating point flips the mixed-pool confident-wrong reduction CI>0 against all 6 competitors (Holm, B=10000, doc-clustered). Decisive structural synthesis: the query-side verifier's sibling confident-wrong is FIXED at 0.218 (it ignores the extracted graph); the certificate's is far LOWER at high precision (0.011 at recall 0.28) but present coverage there is only ~0.025 so the matched-coverage reduction stays ~0 (throttled competitors commit ~0); raising recall to lift coverage pushes the certificate's OWN sibling confident-wrong ABOVE the verifier's (0.327 at recall 0.65) because located_in transitivity turns each sibling false-edge into a spurious containment path. The two win-requirements (coverage high enough to beat throttled competitors AND sibling-cw below the fixed verifier) are ANTI-CORRELATED through recall, so 0 sweet spots exist. The limit is deeper than the refuted prompt-only one and is NOT an extraction-quality artifact.

method_out.json metadata carries, for the paper: fork_verdict (overall + decisive_boundary_synthesis + per-family boundary localization), per_family_results (10-point recall->net-utility frontier, slope contrast, point-by-point frontier dominance, reference/best-F1/net-utility-optimal taus), prompt_only_frontier_overlay_iter9 (iter-9 frontier + slopes -0.3038/-0.6724 + the n=60 stronger cross-family verifier block), snapshot_equality_vs_FROZEN8, gold_read_ceiling, FACT_A per regime (sibling raw-LLM hallucination 0.45), leakage_guard, worked_present_recovery (truthful: Aalborg County, S0 LLM abstained, supervised recovered the connecting edge, certificate composes the hop-2 deduction; prolog python-checked), worked_no_derivation, honesty caveats, and the $0 budget ledger. datasets (1215 examples, 3 corpora) carry predict_certificate_supervised (at the encoder best-F1 tau) + the byte-identical competitor predict_* strings + metadata_supervised_tau. FROZEN8/FRONTIER9 read by absolute path. Kinship secondary was DROPPED (located-in is the load-bearing deliverable; the kinship absent regime is different_component, not the sibling containment test). All 4 JSON variants validate against exp_gen_sol_out.

## Dependencies

- `art_RfjDpsGkBXDG` — dataset
- `art_NUWTxBVWENIJ` — dataset
- `art_oUhZgMSjf7lm` — methodology

## Output Files

- `method.py`
- `full_method_out.json`
- `mini_method_out.json`
- `preview_method_out.json`

## Demo Files

- **method.py** — Research methodology implementation

---
*Generated by AI Inventor Pipeline*
