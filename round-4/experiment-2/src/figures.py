#!/usr/bin/env python3
"""Paper figures for the LLM fuzzy-unification gap-filling experiment.

Reads method_out.json and writes PNGs to results/:
  fig_richness_curve.png       -- LLM composition-cell accuracy & soundness vs algebra richness
  fig_risk_coverage.png        -- CLUTRR mixed-pool selective-accuracy vs coverage (4 methods)
  fig_hallucination.png        -- confident-wrong (hallucination) rate by method
  fig_recovered_precision.png  -- gap-pool recovered precision: cell-fill vs story-fill vs raw
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WORK = Path(__file__).resolve().parent
RES = WORK / "results"
RES.mkdir(exist_ok=True)


def _load():
    p = WORK / "method_out.json"
    if not p.exists():
        parts = sorted((WORK / "method_out").glob("method_out_*.json"))
        m = json.loads(parts[0].read_text())
        return m["metadata"]
    return json.loads(p.read_text())["metadata"]


def fig_richness(m):
    cra = m.get("composition_accuracy_by_algebra", {})
    order = [("point", 3), ("rcc8", 8), ("allen", 13)]
    xs = [f"{a}\n({n} rels)" for a, n in order]
    exact = [cra.get(a, {}).get("exact_match_acc") for a, _ in order]
    sound = [cra.get(a, {}).get("soundness_rate") for a, _ in order]
    jac = [cra.get(a, {}).get("mean_jaccard") for a, _ in order]
    kin = m.get("kinship_composition_cell_accuracy", {}).get("exact_match_acc")
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.plot(xs, exact, "o-", label="exact-match acc", lw=2)
    ax.plot(xs, sound, "s--", label="soundness rate", lw=2)
    ax.plot(xs, jac, "^:", label="mean Jaccard", lw=2)
    if kin is not None:
        ax.axhline(kin, color="green", ls="-.", alpha=0.7,
                   label=f"kinship exact={kin:.2f} (common-sense calculus)")
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("score")
    ax.set_title("LLM composition-cell quality degrades with algebra richness\n"
                 "(a non-sound fill = silent-wrong-narrowing hazard)")
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(RES / "fig_richness_curve.png", dpi=140)
    plt.close(fig)


def fig_risk_coverage(m):
    curve = m.get("clutrr_gapfill_mixed_pool_curve", {})
    if not curve:
        return
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    styles = {"symbolic_abstain": ("k", "symbolic-only (abstain on gaps)"),
              "gapfill_P": ("C2", "neuro-symbolic Mode-P (cell-fill)"),
              "gapfill_S": ("C1", "neuro-symbolic Mode-S (story-fill)"),
              "raw_llm": ("C3", "raw LLM CoT (pure neural)")}
    for key, (c, lab) in styles.items():
        pts = curve.get(key, [])
        xs = [p["coverage"] for p in pts if p["selective_accuracy"] is not None]
        ys = [p["selective_accuracy"] for p in pts if p["selective_accuracy"] is not None]
        if xs:
            ax.plot(xs, ys, "o-", color=c, label=lab, ms=3, lw=1.8)
    ax.set_xlabel("coverage (fraction of mixed pool answered)")
    ax.set_ylabel("selective accuracy (among answered)")
    ax.set_title("CLUTRR mixed pool: risk-coverage\n(cell-fill keeps symbolic safety at full coverage)")
    ax.set_ylim(0, 1.03)
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(RES / "fig_risk_coverage.png", dpi=140)
    plt.close(fig)


def fig_hallucination(m):
    hr = m.get("clutrr_hallucination_reduction", {})
    if not hr:
        return
    labels = ["symbolic", "Mode-P\n(cell-fill)", "Mode-S\n(story-fill)", "raw LLM\n(CoT)"]
    vals = [hr.get("confident_wrong_rate_symbolic"), hr.get("confident_wrong_rate_gapfill_P"),
            hr.get("confident_wrong_rate_gapfill_S"), hr.get("confident_wrong_rate_raw_llm")]
    vals = [v if v is not None else 0 for v in vals]
    colors = ["#444", "C2", "C1", "C3"]
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    bars = ax.bar(labels, vals, color=colors)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.008, f"{v:.3f}", ha="center", fontsize=9)
    ax.set_ylabel("confident-wrong (hallucination) rate on the mixed pool")
    relP = hr.get("rel_reduction_P_vs_raw")
    ttl = "Hallucination rate by method (full coverage)"
    if relP is not None:
        ttl += f"\nMode-P cuts hallucination {100*relP:.0f}% vs raw LLM"
    ax.set_title(ttl)
    ax.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(RES / "fig_hallucination.png", dpi=140)
    plt.close(fig)


def fig_recovered(m):
    rc = m.get("clutrr_gapfill_risk_coverage", {})
    if not rc:
        return
    modes = [("gapfill_P", "Mode-P\n(cell-fill)", "C2"),
             ("gapfill_S", "Mode-S\n(story-fill)", "C1"),
             ("raw_llm", "raw LLM\n(CoT)", "C3")]
    labels = [m_[1] for m_ in modes]
    prec = [(rc.get(k, {}).get("recovered_precision") or 0) for k, _, _ in modes]
    colors = [c for _, _, c in modes]
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    bars = ax.bar(labels, prec, color=colors)
    for b, v in zip(bars, prec):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.01, f"{v:.2f}", ha="center", fontsize=9)
    ax.axhline(m.get("net_faithful_bar", 0.5), color="k", ls="--", alpha=0.6,
               label=f"net-faithful bar ({m.get('net_faithful_bar', 0.5)})")
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("precision among recovered gap answers")
    ax.set_title("Gap-pool recovered precision (CLUTRR manufactured gaps)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(RES / "fig_recovered_precision.png", dpi=140)
    plt.close(fig)


def main():
    m = _load()
    fig_richness(m)
    fig_risk_coverage(m)
    fig_hallucination(m)
    fig_recovered(m)
    print("wrote figures to", RES)


if __name__ == "__main__":
    main()
