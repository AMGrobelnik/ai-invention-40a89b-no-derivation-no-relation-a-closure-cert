# Genuine LLM Fuzzy-Unification with a Certificate-Bounded Hallucination Guarantee

This experiment converts reviewer **MAJOR #2** — *"Mode-P 'fuzzy unification' was circular
memorized-table recall (confidence exactly 1.0 on every kinship cell)"* — into a real,
measured contribution. It constructs **genuinely-fuzzy LLM reads** from existing gold and
shows that a training-free **abstain-on-collapse certificate** bounds the hallucination cost
of feeding those reads into a sound symbolic closure engine.

## What is built

Two labeled settings, one consistent pipeline:

1. **Vague / out-of-table spatial RCC-8** (`SpaRP-PS1`, dep `art_f-ofxduZjwSM`). A *known*
   RCC-8 relation between two regions is rendered with a **vague preposition** (`near`,
   `touching`, `around`, `inside`, `overlapping`) that has **no single RCC-8 answer**. A real
   LLM (`google/gemini-3.1-flash-lite`, temp 0) must emit a **calibrated sub-1.0 disjunction**
   over the 8 base relations.

2. **Ambiguous / paraphrased kinship** (`CLUTRR`, dep `art_HS7-lxhZnU9m`). An atomic kinship
   fact is replaced by an informal term (`guardian`, `descendant`, `family elder`,
   `sibling-figure`, `relative by marriage`, `younger relative`) mapping to a **type
   disjunction**.

For each setting we measure:

- **(i) Calibration** — ECE (per-candidate + top-1 views) + reliability diagram; the reads are
  genuinely `<1.0` (`frac_conf_1p0 = 0.00` in both settings) and reasonably calibrated. The
  explicit contrast: the memorized **Mode-P** emitted confidence **exactly 1.0** on 100% of
  cells.
- **(ii) Certificate-bounded closure** — the fuzzy disjunction + the exact-table constituent
  reads are fed into the RCC-8 (`qcn.algebras`) / kinship (disjunctive-seed forward-union)
  engines. Output contract: `|D|==1 → COMMIT`, `|D|==0 → Mode-B COLLAPSE`, `|D|>1 → ABSTAIN`.
  Reported as a **risk-coverage** tradeoff vs a **commit-the-argmax** baseline (ignores the
  disjunction, always answers) and an **abstain-always** baseline. The
  **read-soundness-conditional zero-FP invariant** (sound read ⇒ no confident-wrong) is proved
  by construction and **asserted** on the all-sound subset.
- **(iii) Auditable trace-graphs** — every composition step is tagged `exact_table` vs
  `llm_fuzzy` (with its emitted set + per-relation `p` + whether gold was retained) and the
  final certificate decision; includes the honest unsound-read-caught traces.

Plus a **cross-family sensitivity** arm (`deepseek/deepseek-v3.2`) and doc-clustered bootstrap
CIs on every headline number.

## Headline results (`--max-per-setting 1500`)

| | spatial RCC-8 | ambiguous kinship | Mode-P (memorized) |
|---|---|---|---|
| `frac_conf_1p0` | 0.00 | 0.00 | **1.00** |
| read soundness | 0.93 | 1.00 | 1.00 (recall) |
| ECE (per-candidate / top-1) | 0.142 / 0.286 | 0.111 / 0.051 | — |
| certificate coverage | 0.54 | 0.31 | — |
| certificate confident-wrong | **0.000** | **0.000** | — |
| commit-argmax confident-wrong | 0.364 | 0.216 | — |
| Δ confident-wrong 95% CI | [0.30, 0.43] | [0.17, 0.26] | — |
| zero-FP on sound reads | holds | holds | — |

Spatial: 5 unsound reads, **all caught** (`certificate_caught_fraction = 1.0`, 0 silent-wrong
missed). Verdict **YES** for both settings.

## Files

- `method.py` — the experiment (reads → calibration → certificate closure → risk-coverage →
  contrast → sensitivity → traces → stats → output).
- `figures.py` — `fig_calibration_contrast`, `fig_reliability`, `fig_risk_coverage`,
  `fig_breadth_conf` (→ `results/`).
- `method_out.json` — aii `exp_gen_sol_out` (validated); `mini_/preview_method_out.json`.
- `llm.py`, `kinship.py`, `stats.py`, `dataio.py`, `qcn/` — reused engines from the iter-4
  workspace.
- `cache/` — SHA-256 disk cache (warm reruns cost **$0**; total API spend to build it was
  **$0.0029** for 22 cached calls). Not published (see `upload_ignore`).

## Reproduce

```bash
uv venv .venv --python=3.12 && source .venv/bin/activate
uv pip install numpy scipy matplotlib httpx loguru jsonschema
python method.py --no-llm                 # $0 symbolic plumbing validation (T1/T2)
python method.py --mini                   # tiny LLM smoke
python method.py --max-per-setting 1500   # full run (cache-served → $0 marginal)
python figures.py
```

The fuzzy reads are **term-conditioned** (one read per vague/ambiguous term, temp 0, cached),
so only ~6 distinct reads per setting drive the hundreds of per-edge calibration records and
the per-instance certificate closure. The vague TERM is the unit of fuzziness by construction;
the empirical per-term gold mix is the calibration target. See `metadata.honesty_caveats`.
