# Query-side verifier vs no-derivation certificate on CLUTRR + Re-DocRED kinship pools

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** experiment  
**ID:** `art_963U_7mCLAMJ`

## Layman Summary

We test whether simply asking an LLM 'are these two people related at all?' catches the confident made-up family relationships that a logic no-proof-no-answer certificate catches; it does not.

## Full Summary

iter-8 experiment_2 EXECUTED: the reviewer-mandated DISCONFIRM test for the closure-certificate paper. It asks whether a cheap QUERY-SIDE false-premise VERIFIER ('are X and Y related by kinship at all?') or a SELF-VERIFICATION pass ('is Y really X's <raw answer>?') recovers the structural certificate's absent-relation hallucination-safety without the closure engine. REUSE-HEAVY: loads the two fully-cached prediction pools by filesystem read (CLUTRR battery iter_6/gen_art_experiment_1, 102 present + 180 absent; Re-DocRED battery iter_7/gen_art_experiment_1, 360 present + 368 absent + 116 docred-present), reuses llm.py/stats.py/baselines.py/kinship.py VERBATIM, and adds ONLY the verifier + self-verify calls (reader-matched gemini-3.1-flash-lite, sha256-cached, total billed $0.14, hard cap $9).

A $0 REPRODUCTION GATE (32/32 checks PASS) re-derives every published literal from the carried row fields and asserts it matches each pool's own aggregates AND the published constants: FACT-A absent-hallucination rate (CLUTRR 0.472 gemini / 0.483 deepseek; Re-DocRED 0.326 / 0.318), certificate confident-wrong-on-absent (0.0278 / 0.0707), the mixed-pool matched-coverage CERTIFICATE selective accuracy (0.8267 / 0.475), EVERY confidence-signal mixed selacc (CLUTRR 0.4133/0.3733/0.44/0.3733; Re-DocRED 0.675/0.6/0.645/0.6), and the crux survival fractions (CLUTRR 0.4353/0.7176/0.2471/0.7176; Re-DocRED 0.5083/0.85/0.4833/0.85) -- ALL EXACT. The tie-break-sensitive signal selaccs reproduce byte-exactly only after the source record ORDER is reconstructed (CLUTRR <- iter-3 row order; Re-DocRED <- dataset doc order, present-then-absent per doc); certificate/FACT-A/crux numbers are order-independent. A structural mismatch is a hard stop (no spend).

HEADLINE VERDICT = CERTIFICATE_NECESSARY_BOTH_VENUES. On the absent-relation FABRICATION set (raw LLM confidently committed a kinship on a different-component pair), fraction CAUGHT (method abstains / answers no-relation): certificate 0.941 (CLUTRR) / 0.850 (Re-DocRED) vs query-side verifier 0.588 / 0.100 vs self-verify 0.824 / 0.542 vs best dispersion signal P(True) 0.753 / 0.517. The certificate catches STRICTLY MORE than the query-side verifier on BOTH venues (doc-clustered paired bootstrap B=10000; cert-minus-verifier caught-gap 0.353 CI[0.187,0.510] and 0.750 CI[0.620,0.848]; CIs exclude 0, p<=0.002). WHY THE VERIFIER FAILS: it runs on the SAME LLM that hallucinated, so when the reader confidently invents 'Y is X's sister' on an unrelated pair, 'are X and Y related?' returns RELATED (p=1.0) -- the verifier inherits the generation error; the certificate's abstention is independent of LLM confidence. Self-verify is intermediate but still significantly below the certificate.

HONEST BOUNDARY (emitted alongside, not hidden): on Re-DocRED MIXED-pool selective accuracy the certificate ties/loses (0.475 vs verifier 0.595 / signals 0.60-0.675) because natural-prose extraction recall makes it OVER-ABSTAIN on PRESENT pairs (the iter-7 extraction-limited finding); the necessity verdict is therefore scoped to the hallucination-CATCHING objective (the paper's safety claim), where the certificate dominates. READER SCOPE: both pools carry per-row predictions from the GEMINI reader only (deepseek aggregate-only), so the verifier is reader-matched to gemini and deepseek FACT-A is reproduced from the carried aggregate; a deepseek-verifier robustness arm exists behind a flag (disabled in the final artifact for focus).

OUTPUT method_out.json (exp_gen_sol_out, validated 0 errors; full/mini/preview, all <3MB) groups 1126 per-query rows into clutrr_present/clutrr_absent/redocred_present/redocred_absent/docred_present, each carrying predict_certificate, predict_conf_thresh_{4}, predict_commit_argmax, predict_queryside_verifier, predict_queryside_selfverify, predict_verifier_as_signal (ALL STRINGS) + gold + rich metadata; metadata holds the reproduction_gate, per-venue matched-coverage leaderboards (Holm-adjusted doc-clustered B=10000 CIs), fraction_caught_crux_tables, and the certificate_necessity_verdict. This is the load-bearing evidence that the certificate's structural abstention is NOT reproducible by a query-side LLM verifier -- the reviewer's DISCONFIRM does not disconfirm.

## Dependencies

- `art_HS7-lxhZnU9m` — dataset
- `art_NUWTxBVWENIJ` — dataset
- `art_dA_3iFe_7fn_` — methodology

## Output Files

- `method.py`
- `full_method_out.json`
- `mini_method_out.json`
- `preview_method_out.json`

## Demo Files

- **method.py** — Research methodology implementation

---
*Generated by AI Inventor Pipeline*
