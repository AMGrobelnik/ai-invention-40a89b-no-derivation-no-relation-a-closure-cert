# STEP-B (iter-7): closure certificate vs the 4-signal confidence battery on the NATURAL Re-DocRED kinship corpus

**The decisive open test.** iter-6 ran a fair-baseline experiment on *templated* CLUTRR: a
closure **certificate** (forward least-fixpoint UNION over LLM-extracted kinship edges →
abstain when there is no derivation path) versus the **best available confidence/uncertainty
battery** on the raw LLM answerer — verbalized confidence, self-consistency vote-margin@k=10,
Kadavath **P(True)**, semantic-entropy negentropy. This artifact re-runs that experiment
**VERBATIM** on **genuinely-natural Wikipedia introductory prose** (the `art_NUWTxBVWENIJ`
Re-DocRED/DocRED corpus — no templating, no concatenation), so the reviewer can see whether
the diagnostic survives the move from synthetic to real text.

It carries the four load-bearing iter-6 objects onto real prose:
* **FACT A** — the raw LLM commits a confident kinship on **absent-relation** pairs (two people
  in *different connected components* of the document's family graph → no kinship path).
* **FACT B** — those absent hallucinations **survive** every confidence rule: a single global
  threshold tuned to the certificate's coverage still commits them; they sit at high signal value.
* **Mixed-pool matched-coverage showdown** — certificate vs each signal at the certificate's
  coverage on the present+absent pool (so abstain-on-everything cannot win).
* **Holm-adjusted confident-wrong reductions** — doc-clustered paired bootstrap `B=10000`.

…plus the natural-prose additions that make the test honest: **PRIMITIVE-level scoring**
(gender is best-effort in DocRED), **natural-prose atomic P/R** (extraction is *measured*, not
improved), a **certificate-abstention decomposition** (correct-absent vs over-abstain-present),
the **gold-read ceiling**, and a **pre-registered FORK verdict**.

## Pre-registered fork (decided by the data, not after the fact)
```
diagnostic_holds        = FACT_A high (raw hallucinates on absent at high confidence)
                          AND FACT_B (>=2 signals still commit >=50% of those hallucinations)
certificate_wins_mixed  = certificate confident-wrong < EVERY signal on the mixed pool
                          (Holm CI excludes 0, reduction>0)

CONFIRM-HEADLINE             if certificate_wins_mixed         (natural certificate beats the battery)
EXTRACTION-LIMITED-BOUNDARY  elif diagnostic_holds             (FACT A+B transfer; certificate over-
                                                                abstains/ties on PRESENT — extraction-
                                                                recall-limited, quantified)
DIAGNOSTIC-WEAKER-THAN-CLAIMED  else                           (honest negative: a signal filters them)
```

## What is reused VERBATIM vs new
Reused from iter-6 (battle-tested, copied unchanged): `readers.py` (neural reads),
`kinship.py` (the forward least-fixpoint UNION closure — the *correct* engine for the finite
kinship table; **not** the POINT/ALLEN relation-algebra engine), `baselines.py`
(matched-coverage / risk-coverage machinery), `stats.py` (clustered paired bootstrap, Holm),
`llm.py` (sha256-cached, hard-$9-capped async OpenRouter client), `prolog.py` (auditable discharge).

New code: **`dataio_redocred.py`** — the natural-corpus loader + entity-name **grounding**
(LLM names → gold entity_ids via the mention-span alias table; measured gold-surface grounding
recall ≈ 0.99); and the new orchestration in **`method.py`** — primitive scoring, natural-prose
atomic P/R (converse-invariant + strict + vs-locally-justifiable ceiling), abstention
decomposition, cross-family driver, and the fork verdict.

## Two readers (reader-diversity generality)
* **PRIMARY** `google/gemini-3.1-flash-lite` — full re-docred (140 docs, 360 present + 368 absent).
* **CROSS-FAMILY** `deepseek/deepseek-v3.2` — full re-docred, reader-specific certificate
  (re-extract + re-ground), recomputing FACT A / FACT B / mixed showdown / Holm.
* **docred** present-stratum corroboration (its absent gold is DOWNGRADED — DocRED false negatives).

## Reproduce
```bash
uv run tests.py                                   # $0 unit tests (engine round-trip, grounding, primitive scoring, canon PR)
uv run method.py --slice both --cross-family      # full run; cached reads $0, new reads cost-guarded ($9 hard cap)
```
Output `method_out.json` (`exp_gen_sol_out` schema): per-query `predict_*` + gold for
`re-docred_present`, `re-docred_absent`, `docred_present`; `metadata.headline_summary`,
`primary_reader_results` (the four views), `abstention_decomposition`, `natural_prose_atomic_pr`,
`cross_family_sensitivity`, worked traces (no-derivation abstention, over-abstain-present,
present composition + Prolog), and the fork verdict. `mini_/preview_` variants alongside.

## Honest caveats
* **Natural prose, corpus-honest length.** DocRED intro prose averages ~1020 chars; no
  family-bearing doc reaches the umbrella's ~3000-char target (we do not pad). The
  natural-text + absent-relation regime is the load-bearing property.
* **Absent = structural** (different connected components ⇒ conservative closed-world
  `no-relation`); the certificate's absent abstention is therefore structural-by-construction
  (conceded). The load-bearing claims are FACT A + FACT B + mixed-pool signal-discrimination +
  the quantified present-extraction ceiling.
* **Primitive-level scoring** (gender best-effort) — surface-level reported as secondary.
* **Extraction is MEASURED, not improved** — atomic recall is the binding natural-prose ceiling;
  the gold-read certificate (closure over GOLD edges, present-coverage 1.0 / absent-abstain 1.0)
  isolates that ceiling exactly.
* **Prolog.** SWI-Prolog is unavailable here ⇒ discharge is python-checked and labelled
  truthfully; the program text (`comp/3, conv/2, rel/3, solve_/4`) is emitted and cross-checked
  by the Python re-implementation.
* **docred absent gold downgraded** (Re-DocRED carries +80% more family edges on shared titles).
* Re-DocRED/DocRED text is CC BY-SA; CLUTRR composition table is research/non-commercial.
