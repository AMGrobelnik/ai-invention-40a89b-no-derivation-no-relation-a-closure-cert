#!/usr/bin/env python3
"""Publication figures for the CLUTRR closure-certificate experiment.

Generates (into results/):
  fig_accuracy_vs_hop.png       -- selective accuracy vs chain length per method
  fig_coverage_vs_hop.png       -- coverage vs chain length + full-minus-naive gap (H3)
  fig_risk_coverage_absent.png  -- confident-wrong rate vs coverage on absent pairs (H2)
  fig_matched_coverage_bar.png  -- matched-coverage selective accuracy leaderboard (H1)
All are best-effort; any failure is logged and skipped (never aborts the run).
"""
from __future__ import annotations

from pathlib import Path

from loguru import logger

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

_COLORS = {"modeA": "#1b7837", "naive": "#a6611a", "raw": "#b2182b",
           "sc": "#762a83", "pot": "#2166ac", "off": "#999999"}
_LABEL = {"modeA": "Mode-A (closure, ours)", "naive": "naive single-pass",
          "raw": "raw LLM", "sc": "self-consistency", "pot": "Path-of-Thoughts", "off": "off"}


def _hops_sorted(hop_table):
    return sorted(hop_table.keys(), key=lambda h: int(h))


def fig_accuracy_vs_hop(hop_table, outdir: Path):
    hops = _hops_sorted(hop_table)
    xs = [int(h) for h in hops]
    plt.figure(figsize=(7, 4.5))
    for m in ("modeA", "naive", "raw", "sc", "pot"):
        ys = [hop_table[h][m]["selective_accuracy"] for h in hops]
        ys = [(None if (y != y) else y) for y in ys]
        plt.plot(xs, ys, marker="o", color=_COLORS[m], label=_LABEL[m])
    plt.xlabel("chain length (hops)"); plt.ylabel("selective accuracy")
    plt.title("Selective accuracy vs chain length (CLUTRR, end-to-end)")
    plt.ylim(0, 1.02); plt.grid(alpha=0.3); plt.legend(fontsize=8)
    p = outdir / "fig_accuracy_vs_hop.png"; plt.tight_layout(); plt.savefig(p, dpi=130); plt.close()
    return p


def fig_coverage_vs_hop(hop_table, outdir: Path):
    hops = _hops_sorted(hop_table)
    xs = [int(h) for h in hops]
    plt.figure(figsize=(7, 4.5))
    for m in ("modeA", "naive", "raw", "sc", "pot"):
        ys = [hop_table[h][m]["coverage"] for h in hops]
        plt.plot(xs, ys, marker="o", color=_COLORS[m], label=_LABEL[m])
    gap = [hop_table[h].get("full_minus_naive_coverage_gap", 0) for h in hops]
    plt.plot(xs, gap, marker="s", color="black", linestyle="--", label="full - naive coverage gap (H3)")
    plt.xlabel("chain length (hops)"); plt.ylabel("coverage")
    plt.title("Coverage vs chain length: iteration advantage (full PC vs naive)")
    plt.ylim(-0.02, 1.02); plt.grid(alpha=0.3); plt.legend(fontsize=8)
    p = outdir / "fig_coverage_vs_hop.png"; plt.tight_layout(); plt.savefig(p, dpi=130); plt.close()
    return p


def fig_risk_coverage_absent(rc_curves, outdir: Path):
    plt.figure(figsize=(7, 4.5))
    for m in ("modeA", "raw", "sc", "pot"):
        cur = rc_curves.get(m, {}).get("points", [])
        if not cur:
            continue
        xs = [p["coverage"] for p in cur]
        ys = [p["confident_wrong_rate"] for p in cur]
        plt.plot(xs, ys, marker="o", color=_COLORS[m], label=_LABEL[m])
    plt.xlabel("coverage (fraction of absent pairs answered)")
    plt.ylabel("confident-wrong (hallucination) rate")
    plt.title("Risk-coverage on absent-relation pairs (lower is better)")
    plt.grid(alpha=0.3); plt.legend(fontsize=8)
    p = outdir / "fig_risk_coverage_absent.png"; plt.tight_layout(); plt.savefig(p, dpi=130); plt.close()
    return p


def fig_matched_coverage_bar(showdown, outdir: Path):
    lb = showdown.get("leaderboard", {})
    if not lb:
        return None
    methods = [m for m in ("modeA", "naive", "raw", "sc", "pot", "off") if m in lb]
    accs = []
    for m in methods:
        d = lb[m]
        a = d.get("selective_accuracy")
        accs.append(0.0 if (a is None or a != a) else a)
    plt.figure(figsize=(7, 4.5))
    plt.bar(range(len(methods)), accs, color=[_COLORS[m] for m in methods])
    plt.xticks(range(len(methods)), [_LABEL[m] for m in methods], rotation=20, ha="right", fontsize=8)
    plt.ylabel("selective accuracy @ matched coverage")
    cstar = showdown.get("c_star")
    plt.title(f"Matched-coverage selective accuracy (c*={cstar:.2f})" if cstar else
              "Matched-coverage selective accuracy")
    plt.ylim(0, 1.02); plt.grid(axis="y", alpha=0.3)
    p = outdir / "fig_matched_coverage_bar.png"; plt.tight_layout(); plt.savefig(p, dpi=130); plt.close()
    return p


def make_all(hop_table, rc_curves, showdown, outdir: Path) -> list:
    outdir.mkdir(parents=True, exist_ok=True)
    made = []
    for fn, args in ((fig_accuracy_vs_hop, (hop_table, outdir)),
                     (fig_coverage_vs_hop, (hop_table, outdir)),
                     (fig_risk_coverage_absent, (rc_curves, outdir)),
                     (fig_matched_coverage_bar, (showdown, outdir))):
        try:
            p = fn(*args)
            if p:
                made.append(str(p))
        except Exception as e:  # noqa: BLE001
            logger.warning(f"figure {fn.__name__} failed: {e}")
    return made
