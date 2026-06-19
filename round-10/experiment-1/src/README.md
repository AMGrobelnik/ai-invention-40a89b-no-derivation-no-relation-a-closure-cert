# iter-10 — `S_supervised`: a precision-preserving supervised `located_in` extractor to test for a NET-utility certificate win

## One-sentence result
A **trained, threshold-tunable, precision-preserving** supervised `located_in` extractor — built two independent ways
(calibrated GBDT over engineered per-pair features, and a fine-tuned `deberta-v3-small` encoder) and trained **doc-disjoint**
on the gold distribution over **gold-mention entity pairs** — **dominates** iter-9's refuted prompt-only extractor in
precision/recall space (GBDT recall 0.155 at **precision 0.80** vs prompt-only's 0.665; the encoder reaches recall **0.46 at
precision 0.86** and a max recall **0.65**, operating *strictly beyond* the prompt-only ceiling of 0.23), yet **no operating
point** lifts the closure certificate's mixed-pool confident-wrong reduction above 0 against all 6 competitors → the fork
resolves to **NET-UTILITY-BOUNDARY-STRUCTURAL**.

**The decisive structural reason** (read off the encoder sweep): the query-side verifier's sibling confident-wrong is
**FIXED at ~0.218** (it ignores the extracted graph). The certificate's sibling confident-wrong is far *lower* at
high-precision operating points (**0.011** at recall 0.28) — it abstains structurally — but present coverage there is only
~0.025, so the matched-coverage mixed reduction stays ~0 (the competitors, throttled to that tiny coverage, commit ~0
confident-wrong, so there is nothing to beat). Raising the extractor's recall to lift present coverage pushes the
certificate's *own* sibling confident-wrong **above** the verifier's (**0.327** at recall 0.65), because `located_in`
transitivity turns each injected sibling false-edge into a spurious containment path. The two requirements for a strict win —
present coverage high enough to beat the throttled competitors AND sibling confident-wrong below the fixed verifier — are
**anti-correlated through the extractor's recall**, so **no operating point** (0 "sweet spots") satisfies both. The gold-read
ceiling stays **1.0/1.0/1.0**, proving the headroom exists but is *not extractor-reachable* — a limit **deeper than** the
refuted prompt-only one, and **not** an extraction-quality artifact.

## What changed vs iter-8/iter-9 (and what is reused VERBATIM)
This experiment changes **only the extraction step**. Everything downstream is reused byte-identically:

- **Reused VERBATIM** (copied from iter-9): `core.py` (= the iter-8 `method.py`: all view / verdict / output functions),
  `kinship.py` (forward least-fixpoint UNION closure engine), `dataio_locatedin.py` / `readers_locatedin.py` /
  `queryside.py` (located-in harness), `baselines.py`, `stats.py`, `llm.py`, `prolog.py`.
- **The 6 confident-wrong competitors** (4 dispersion signals: verbalized / SC-margin / Kadavath P(True) / semantic-entropy;
  + 2 query-side verifiers: false-premise verifier + self-verification) are **REPLAYED byte-identical at $0** from the
  SHA-256 cache merged from iter-8 + iter-9. A snapshot assertion vs `FROZEN8` (iter-8 `method_out.json`) confirms
  **0 mismatches** over all 1215 joined records.
- **NEW** (`extractor.py` + `run_supervised.py`): the supervised extractor and the per-operating-point certificate recompute,
  the precision-preserving recall→net-utility frontier, the iter-9 prompt-only frontier overlay + slope/dominance contrast,
  and the pre-registered fork verdict.

## The supervised extractor (`extractor.py`)
- **Task**: binary `located_in(i,j)` over **ordered gold-entity pairs** `(i,j)` whose mentions co-occur within a
  `W=2`-sentence window. The engine seeds the converse (`contains`) itself, so only `type='located_in'` edges are emitted;
  directed 2-cycles on one unordered pair are resolved by the higher calibrated probability.
- **No grounding loss**: the extractor works directly over gold `entity_id`s, so there is **no LLM name-grounding step** and
  no grounding recall loss (a structural advantage over the prompt-only PATH-2 extraction, which was also scored after
  grounding to gold entities). It does **not** perform mention detection / NER — the entity set is given — which isolates
  exactly the relation-extraction recall the certificate depends on.
- **Two independent families** (both expose `extract_supervised(ctx, tau)`):
  - **GBDT** — calibrated LightGBM (fallback GradientBoosting/LogReg) over ~30 engineered per-pair features (sentence/char
    distance, directional cue counts from the located-in surface vocabulary, appositive/parenthetical patterns, admin-level
    ordinal, substring/token overlap, mention counts, co-occurrence degree). CPU, robust.
  - **Encoder** — fine-tuned `microsoft/deberta-v3-small` over the marked text window `[E1]…[/E1] … [E2]…[/E2]` of the
    closest co-occurring mention pair (GPU, bf16).
- **Calibration**: `IsotonicRegression` on a doc-disjoint within-train fold maps the score to a precision-monotone
  threshold, so sweeping `tau` traces a well-formed precision-preserving frontier.
- **Leakage guard**: training docs are **doc-disjoint** from the eval pool (the real guard); the label definition is
  identical train/eval (no label leakage). Fold = `SHA-256(doc_id) % 5`.

## Pipeline (`run_supervised.py`)
1. Reproduce the iter-8 eval pool exactly (515 present / 450 same-component-sibling-absent / 250 different-component-absent
   over 283 docs; `SEED=20260618`, targets 400/450/250) and **assert** the counts match `FROZEN8`.
2. Build doc-disjoint training contexts (all re-docred docs minus the 283 eval docs ≈ 2321 docs); report fold histograms.
3. Replay the 6 competitors + the S0 LLM-read certificate **once at $0**; assert cost < $0.05; snapshot-assert vs `FROZEN8`.
4. Gold-read ceiling sanity: feeding the gold atomic edges yields present-coverage / absent-abstain / selective-accuracy =
   **1.0 / 1.0 / 1.0** (the constant upper bound carried in every table).
5. Train each supervised family doc-disjoint; sweep ≥7 precision-preserving `tau`; per `tau`, recompute **only** `modeA`
   (held_out ablation kept), re-run `core.compute_core_views` on the decisive sibling mixed pool (Holm, B=10000,
   doc-clustered paired bootstrap), and record the frontier row.
6. Build the precision-preserving frontier; overlay iter-9's negative prompt-only frontier (located-in slope **−0.30**,
   kinship **−0.67**); compute the matched-recall-range slope and the point-by-point **frontier dominance**.
7. Resolve the pre-registered fork: **DEMONSTRATED-FIX-NATURAL-PROSE** (some `tau` flips every Holm CI > 0 AND beats the
   verifier; report `R*`) vs **NET-UTILITY-BOUNDARY-STRUCTURAL** (no flip — localize whether the limit is achievable-recall
   or intrinsic present/absent confusion).

## Files
- `extractor.py` — the supervised extractor (candidate enumeration, features, GBDT + encoder families, calibration).
- `run_supervised.py` — the driver (eval-pool reproduction, leakage guard, $0 replay, snapshot, tau sweep, frontier,
  dominance, fork, worked traces, output).
- `core.py`, `kinship.py`, `dataio_locatedin.py`, `readers_locatedin.py`, `queryside.py`, `baselines.py`, `stats.py`,
  `llm.py`, `prolog.py` — reused VERBATIM from iter-9 (the frozen certificate harness).
- `method_out.json` (+ `mini_`/`preview_`) — the validated `exp_gen_sol_out` artifact.
- `cache/` — SHA-256 LLM read cache (merged iter-8 + iter-9; excluded from the published repo; all reads replay at $0).

## Reproduce
```bash
export LD_LIBRARY_PATH="$(pwd)/extra_libs:$LD_LIBRARY_PATH"   # provides libgomp.so.1 for lightgbm
.venv/bin/python run_supervised.py --families gbdt,encoder \
  --taus "0.95,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1" --encoder-epochs 2 --out method_out.json
```

## Honesty caveats
- Supervised over **gold entity-mention pairs** (no NER); this is the fair comparison to the prompt-only extractor, which was
  also scored after grounding to gold entities.
- Atomic recall is capped by the locally-justifiable fraction (~0.588 on re-docred) plus the window; KB-implied non-local
  edges are not span-recoverable. The vs-locally-justifiable ceiling is reported per operating point.
- The mixed matched-coverage reduction is throttled when present coverage is low; the load-bearing objects are the per-`tau`
  natural sibling confident-wrong and the crux fraction-caught (exactly as in iter-8/9).
- swipl discharge falls back to python-checked and is labelled truthfully when swipl is unavailable.
- Kinship is a time-permitting SECONDARY replication; located-in is the load-bearing deliverable.
