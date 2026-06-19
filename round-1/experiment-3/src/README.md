# Recall-Bite Frontier & LLM Elicitation Go/No-Go (T0 pilot)

Pre-main-run viability gate for **closure-certified temporal composition**: can an LLM emit
SOUND-but-sub-universal disjunctive temporal-relation sets at usable per-edge recall, with
non-trivial closure singleton-resolution on deduction-required edges? Maps the recall↔breadth
frontier, fixes the operating point + within-document error correlation ρ for iteration-2,
and applies a pre-registered GO/NO-GO. **It does not run the main method-vs-baseline study.**

## Result (this run)

| | |
|---|---|
| **Verdict** | `NO-GO/NICHE` — no real arm clears the recall gate at any breadth knob |
| Best real recall | TBDense 0.80, MATRES 0.86, TDDMan 0.58 (gates: Allen 0.85 / point 0.90) |
| Synthetic (clean text) | recall **0.958**, closure deduction-resolution **~0.37–0.42 ≥ 0.10** |
| Method (closure) vs baseline (direct read) on deduction edges | Δ ≈ 0 (full-context reads already global; path reads unsound) |
| Gate validation (MATRES) | **PASSED** (deduction-fraction = 0.0, as expected by construction) |
| ρ (within-doc soundness ICC) | 0.10 ; J(2)=0.55 > r²=0.48, J(3)=0.34 > r³=0.33 (positive corr.) |
| bite lost (convex point vs Allen) | 0.0 on point-expressible triangles |
| local-only-reader probe | pins gold singleton only 27% on deduction edges → reads truly non-local |
| Spend | **$0.58** OpenRouter (`google/gemini-3.1-flash-lite`), 4191 billed calls, 0 parse-fail, 0 errors |

**Take-away for iter-2:** the binding constraint is real-text *read soundness* (recall below gate),
not the closure step — closure works when reads are sound (synthetic). Iteration-2 should headline
the synthetic arm, scope real text as a niche/safety-net, and measure closure's value against a
LOCAL-only reader (not a full-context reader).

## Files

- `engine.py` — self-contained QCN closure engine: point + Allen-13 algebras (built by the
  endpoint method, cross-checked against the dossier's GQR cells), PC-2 closure, triangle closure,
  naive-single-pass baseline, convex `≠→⊤` widening rule.
- `corpora.py` — builds elicitation tasks (text + marked event pair + gold) and closure triangles
  for the three real corpora.
- `synth.py` — scenario-then-abstract consistent synthetic QCNs (clean-text reference).
- `llm.py` — async OpenRouter client (disk cache, hard cost-guard, robust JSON/relation parsing).
- `method.py` — orchestrator (config, blocking closure tests, elicitation, all metrics, frontier
  plot, go/no-go, schema-valid `results/method_out.json`).
- `tests.py` — BLOCKING closure unit tests (gate all LLM spend).
- `data/` — corpus slices used (see provenance below).
- `results/` — `method_out.json` (+ mini/preview), `figures/*.jpg`.

## Reproduce

```bash
uv run python tests.py          # closure correctness (must pass)
uv run python method.py --mini  # tiny end-to-end smoke (~$0.01)
uv run python method.py --max-docs 24 --max-edges 240 --max-tri 200 --n-synth 22 --concurrency 20
```
Requires `OPENROUTER_API_KEY` in the environment. All responses are sha256-cached under `cache/`,
so re-runs recompute metrics at **$0**.

## Data provenance

- **TimeBank-Dense** (dense arm; NarrativeTime stand-in for the pilot) — TimeML `.tml` with inline
  `<EVENT>` offsets + `<MAKEINSTANCE>` + event-event `<TLINK>` gold (coarse Allen). Source: muk343/TimeBank-dense.
- **TDDMan / TDDiscourse** (non-circular, all-deduction-required >1-sentence pairs) — 4-col TSV gold
  joined to TimeBank-Dense `.tml` text. Source: github.com/aakanksha19/TDDiscourse.
- **MATRES** (gate control, convex point algebra, ~local → N*≈0) — qiangning EMNLP-19 XML
  (self-contained tokenized text + E1/E2 markers + gold + sentence distance).
- **Synthetic** — generated in `synth.py` (no external data).

NarrativeTime (text-machine-lab/nt) was the intended dense corpus but its `nt_format` event token
spans did not align with the document text and its converted `.tml` eids did not match the
`event_order` keys, so the plan-sanctioned **TimeBank-Dense stand-in** was used for the pilot.
