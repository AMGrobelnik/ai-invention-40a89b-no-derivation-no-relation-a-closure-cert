#!/usr/bin/env python3
"""Paper figures for the genuine-LLM-fuzzy-unification certificate experiment.

Reads method_out.json and writes PNGs to results/:
  fig_calibration_contrast.png -- frac(conf==1.0): memorized Mode-P (1.0) vs the two
                                  genuinely-fuzzy settings (<<1.0) [the honesty headline]
  fig_reliability.png          -- per-candidate reliability diagrams (spatial + kinship)
  fig_risk_coverage.png        -- coverage vs confident-wrong frontier: certificate vs
                                  commit-argmax vs abstain-always (both settings)
  fig_breadth_conf.png         -- per-edge breadth vs top-1 confidence, coloured by soundness
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
    full = json.loads(p.read_text())
    # expose metadata keys at top level, keep datasets accessible
    meta = dict(full["metadata"])
    meta["datasets"] = full["datasets"]
    return meta


def fig_calibration_contrast(m):
    cc = m["calibration_contrast_vs_modeP"]
    labels, vals, colors = [], [], []
    mp = cc.get("modeP_memorized", {})
    if mp.get("frac_conf_1p0") is not None:
        labels.append("Mode-P\n(memorized\nkinship cells)")
        vals.append(mp["frac_conf_1p0"])
        colors.append("#b22222")
    for key, lab, c in (("setting1_spatial_fuzzy", "vague spatial\nRCC-8", "C0"),
                        ("setting2_kinship_fuzzy", "ambiguous\nkinship", "C2")):
        if cc.get(key):
            labels.append(lab)
            vals.append(cc[key]["frac_conf_1p0"])
            colors.append(c)
    fig, ax = plt.subplots(figsize=(6.0, 4.3))
    bars = ax.bar(labels, vals, color=colors)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.02, f"{v:.2f}", ha="center", fontsize=11)
    ax.set_ylim(0, 1.12)
    ax.set_ylabel("fraction of reads with max confidence = 1.0")
    ax.set_title("Memorized recall vs genuine fuzzy reads\n"
                 "Mode-P is always certain (1.0); fuzzy reads are calibrated sub-1.0")
    ax.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(RES / "fig_calibration_contrast.png", dpi=140)
    plt.close(fig)


def _reliability_panel(ax, cal, title):
    rel = cal.get("reliability_per_candidate", [])
    xs = [r["mean_conf"] for r in rel if r["count"] > 0]
    ys = [r["mean_acc"] for r in rel if r["count"] > 0]
    cs = [r["count"] for r in rel if r["count"] > 0]
    ax.plot([0, 1], [0, 1], "k--", alpha=0.5, label="perfect calibration")
    if xs:
        sizes = [20 + 380 * (c / max(cs)) for c in cs]
        ax.scatter(xs, ys, s=sizes, color="C0", alpha=0.7, edgecolor="k", zorder=3)
    ece = cal.get("ECE_per_candidate")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("predicted probability (LLM)")
    ax.set_ylabel("empirical P(relation = gold)")
    ax.set_title(f"{title}\nECE={ece:.3f}, n={cal.get('n_candidate_pairs')} (size = #candidates)"
                 if ece is not None else title)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="upper left")


def fig_reliability(m):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    _reliability_panel(axes[0], m["setting1_spatial_calibration"], "Vague spatial RCC-8")
    _reliability_panel(axes[1], m["setting2_kinship_calibration"], "Ambiguous kinship")
    fig.suptitle("Per-candidate reliability of the LLM fuzzy disjunctions", y=1.02)
    fig.tight_layout()
    fig.savefig(RES / "fig_reliability.png", dpi=140, bbox_inches="tight")
    plt.close(fig)


def fig_risk_coverage(m):
    fig, ax = plt.subplots(figsize=(6.6, 4.6))
    settings = [("setting1_spatial_risk_coverage", "spatial", "C0", "o"),
                ("setting2_kinship_risk_coverage", "kinship", "C2", "s")]
    for key, name, color, mk in settings:
        rc = m.get(key, {})
        if not rc or rc.get("n_pool", 0) == 0:
            continue
        pts = [("certificate", rc["certificate"]), ("commit-argmax", rc["commit_argmax"]),
               ("abstain-always", rc["abstain_always"])]
        for lab, d in pts:
            x, y = d["coverage"], d["confident_wrong_rate"]
            ax.scatter([x], [y], color=color, marker=mk, s=110, edgecolor="k", zorder=3)
            ax.annotate(f"{name}:{lab}", (x, y), textcoords="offset points",
                        xytext=(6, 6), fontsize=7.5)
        # connect the frontier
        xs = [d["coverage"] for _, d in pts]
        ys = [d["confident_wrong_rate"] for _, d in pts]
        ax.plot(xs, ys, color=color, alpha=0.35, lw=1.3, label=name)
    ax.set_xlabel("coverage (fraction of queries committed)")
    ax.set_ylabel("confident-wrong (hallucination) rate")
    ax.set_title("Certificate bounds hallucination: zero confident-wrong at non-trivial\n"
                 "coverage, vs commit-argmax which answers everything but hallucinates")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(RES / "fig_risk_coverage.png", dpi=140)
    plt.close(fig)


def fig_breadth_conf(m):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
    for ax, ds_name, title in ((axes[0], "spatial_fuzzy_rcc8", "Vague spatial RCC-8"),
                               (axes[1], "kinship_fuzzy_paraphrase", "Ambiguous kinship")):
        ds = next((d for d in m["datasets"] if d["dataset"] == ds_name), None)
        if not ds:
            continue
        reads = [e for e in ds["examples"] if e.get("metadata_record_kind") == "edge_read"]
        b = [e["metadata_breadth"] for e in reads]
        c = [e["metadata_top1_conf"] for e in reads]
        sound = [e["metadata_sound"] for e in reads]
        # jitter breadth for visibility
        import numpy as np
        rng = np.random.default_rng(0)
        bj = [bi + rng.uniform(-0.18, 0.18) for bi in b]
        for s, col, lab in ((True, "C2", "sound (gold retained)"), (False, "C3", "unsound")):
            xs = [bj[i] for i in range(len(reads)) if sound[i] == s]
            ys = [c[i] for i in range(len(reads)) if sound[i] == s]
            if xs:
                ax.scatter(xs, ys, s=14, color=col, alpha=0.45, label=lab)
        ax.set_xlabel("emitted disjunction breadth |S|")
        ax.set_ylabel("top-1 confidence")
        ax.set_title(title)
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)
    fig.suptitle("Per-edge fuzzy reads: breadth vs confidence (genuinely sub-1.0)", y=1.02)
    fig.tight_layout()
    fig.savefig(RES / "fig_breadth_conf.png", dpi=140, bbox_inches="tight")
    plt.close(fig)


def main():
    m = _load()
    fig_calibration_contrast(m)
    fig_reliability(m)
    fig_risk_coverage(m)
    fig_breadth_conf(m)
    print("wrote figures to", RES)


if __name__ == "__main__":
    main()
