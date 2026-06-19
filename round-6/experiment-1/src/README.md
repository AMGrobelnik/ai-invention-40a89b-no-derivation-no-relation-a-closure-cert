# STEP A — Closure certificate vs a STRONG, fair confidence-thresholded neural abstainer

**Question.** Is the closure certificate's hallucination-safety on the *no-derivation /
absent-relation* stratum just a re-skin of an uncertainty signal the raw LLM already has?
We answer it by pitting the certificate against the **best available confidence/uncertainty
battery** (not a weak verbalized-confidence strawman) at **matched coverage**, and showing
the certificate eliminates exactly the high-confidence absent-relation hallucinations that
**no** confidence rule removes — while honestly **tying/losing** on ordinary *single-path*
spatial deduction (the scope boundary).

This is a **fair-baseline re-analysis** of already-collected pools plus a small confidence
battery. It re-uses the EXACT cached iter-3 CLUTRR pool (`art_0a7i481ZRwS1`: 180 absent +
102 present) and iter-5 spatial RCC-8 pool (`art_f-…`: 228 single-path deduction queries).
It is **not** STEP B (no new natural corpus) and does **not** re-run the cross-path RCC-8
intersection test (settled, clean negative, in iter-5).

## The confidence/uncertainty battery (4 signals on the raw LLM answerer)

| signal | definition | new LLM calls / query |
|---|---|---|
| **verbalized** | the raw answerer's self-reported confidence in [0,1] | 0 (already collected iter-3) |
| **sc_margin** | self-consistency vote-margin: top-relation fraction over **k=10** temp-0.7 samples | +5 (present) / +7 (absent) |
| **ptrue** | **Kadavath P(True)**: model's probability that raw's committed answer is correct | +1 (temp-0) |
| **negent** | semantic-entropy negentropy `1 − H/log(k_eff)` over the k=10 SC samples clustered by relation | 0 |

Each signal `s` defines a **confidence-thresholded RAW-ABSTAIN baseline** `ct_s`: commit
raw's top-1 answer iff `s ≥ τ`, else abstain. All baselines and the certificate are
thresholded to the **same coverage object** ("commits an actual relation") and scored by
**confident-wrong** (a named answer disagreeing with gold; on the absent pool *any* named
answer is wrong). Story-clustered paired bootstrap `B=10000`, Holm-adjusted over the 4 signals.

## Headline results (all REAL-LLM-READ; `google/gemini-3.1-flash-lite`)

* **The LLM is confidently wrong on absent relations.** On the 180 absent pairs the raw LLM
  commits a kinship on **47.2 %** of them; the certificate's confident-wrong rate is **2.8 %**
  → a **0.444** reduction (95 % CI **[0.317, 0.583]**). At the LLM's *natural* coverage **no**
  confidence signal removes a single hallucination (they coincide with raw — matched coverage
  forces committing all named answers).
* **Crux — confidence cannot see absent hallucinations.** Fraction of the 85 absent
  hallucinations that *survive* a confidence rule calibrated to the certificate's coverage:
  verbalized **0.435**, sc_margin **0.718**, **ptrue 0.247**, negent **0.718**. Verbalized
  confidence is ≥ 0.5 on **100 %** of them; only P(True) partially separates them (median
  P(True) = **0.0** on hallucinations) yet **still 24.7 % survive**.
* **Decisive mixed-pool showdown.** At matched coverage (0.266) the structural certificate's
  selective accuracy is **0.827** vs verbalized **0.413** / sc_margin **0.373** / ptrue **0.440**
  / negent **0.373** — it ~**doubles** every signal. The certificate's confident-wrong is
  strictly below every signal (reductions 0.10–0.12; Holm-adjusted CIs all exclude 0). A single
  neural threshold cannot simultaneously abstain-on-absent and cover-present; the certificate does both.
* **Honest scope boundary (P_O).** On the genuine ordinary **single-path** stratum (spatial
  RCC-8, 228 queries) the certificate **ties/loses**: confident-wrong 0.022 vs raw-abstain 0.035
  (reduction CI includes 0) and the matched-coverage selective-accuracy gap is **−0.088**
  (CI **[−0.222, 0.040]**, favors the baseline). When one short chain suffices, neural confidence
  is already well-calibrated and the sound-but-incomplete closure only sacrifices coverage.
  *(CLUTRR-present is multi-hop, not single-path; there the certificate WINS too, consistent with iter-3.)*
* **Cross-family (`deepseek-v3.2`).** The edge persists: deepseek hallucinates a kinship on
  **48.3 %** of absent pairs; survival fractions verbalized **0.672** / sc_margin **0.224** /
  **ptrue 0.103** / negent **0.224**; the certificate still abstains structurally.

**Verdict: CONFIRM** — P_A (certificate beats every signal on no-derivation) ∧ P_O
(ties/loses on single-path spatial) ∧ P_CRUX (high survival for ≥2 signals).

## Pipeline

```
[iter-3 cached pool] --rebuild+verify $0-->  282 records (cert/raw/sc/pot == published)
        |                                          |
        |                                  +-- confidence BATTERY (SC@k=10, P(True), semantic-entropy)
        v                                          v
forward-closure certificate (Mode-A)     ct_verbalized / ct_sc_margin / ct_ptrue / ct_negent
        \__________ matched-coverage / risk-coverage / crux survival __________/
[iter-5 cached pool] --read-only-->  spatial RCC-8 ordinary-deduction tie/lose
```

* **`method.py`** — orchestrator: Stage 1 reproduction gate (rebuild the exact 282 records from
  CLUTRR + cache, cross-check IDENTICAL to the published iter-3 predictions at $0), Stage 2
  battery, Stage 3 `ct_*` baselines, Stage 4 leaderboards (VIEW-1 absent reduction / VIEW-2
  risk-coverage dominance / VIEW-3 matched-coverage showdown), Stage 5 crux survival table,
  Stage 6 spatial reuse, Stage 7 worked traces + Prolog, Stage 8 cross-family, Stage 9 output+verdict.
* **`readers.py` / `baselines.py` / `kinship.py` / `stats.py` / `prolog.py` / `dataio.py` / `llm.py`**
  — reused VERBATIM from iter-3 (the closure engine, matched-coverage stats, sha256-cached
  hard-$9-capped OpenRouter client). `tests.py` — 0-LLM unit tests for the new components.

## Reproduce

```bash
uv run tests.py                       # 0-LLM unit tests (semantic-entropy, ct plumbing, cw semantics)
uv run method.py --cross-family       # full run; cached reads $0; new battery ~$0.30 once, then $0
```

Output: `method_out.json` (`exp_gen_sol_out` schema) — per-query `predict_*` + gold for
`clutrr_no_derivation` (180), `clutrr_ordinary_deduction` (102), `spatial_rcc8_ordinary` (228);
`metadata.headline_summary`, the three leaderboard views, the crux survival table, worked
traces, cross-family arm, Holm families, and the CONFIRM verdict. `mini_/preview_` variants alongside.

## Honest caveats

* **Spend.** Cached iter-3/iter-5 reads replay at $0. The new battery was billed **once**:
  gemini primary $0.166 (2024 calls) + deepseek cross-family $0.132 (2110 calls) ≈ **$0.30**,
  far under the $9 cap. Re-runs are $0; the `budget` block shows the final cached run.
* **Pure-absent degeneracy.** On the pure-absent pool confident-wrong == coverage, so the
  per-signal distinction lives in the *mixed-pool* VIEW-3 and the crux survival table, not in
  matched-coverage-on-absent (stated explicitly in `metadata.leaderboard_no_derivation.subtlety`).
* **Story length.** CLUTRR stories are short (max 871 chars); spatial scenes are templated
  (130–1338 chars, symbolic ids). Neither reaches the umbrella's ~3000-char target.
* **Absent pairs** are STRUCTURAL (different connected components) ⇒ conservative gold `no-relation`.
* **RCC-8** path-consistency is sound-but-incomplete ⇒ spatial closure coverage is a lower bound.
* **Prolog.** SWI-Prolog is unavailable here, so discharge is **python-checked** and labelled
  truthfully (iter-5 precedent); the Prolog program text (`comp/3,conv/2,rel/3,solve_/4`) is emitted
  and cross-checked by the Python re-implementation of the same rules.
* CLUTRR is research/non-commercial (CC-BY-NC-style).
