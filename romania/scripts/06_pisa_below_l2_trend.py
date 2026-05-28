"""
Chart 06 — Romania's PISA share-below-Level-2, three cycles.
A small-multiples chart showing the share of Romanian 15-year-olds at the
lowest proficiency band in math, reading, and science across PISA 2012,
2018, and 2022. The OECD's qualitative finding — stable at high levels
since 2006 — is annotated.

The argument the chart carries: across a decade of announced reforms, the
share of Romanian students who cannot meet baseline proficiency has not
moved meaningfully. The math line drifts upward (+7pp 2012-2022).

Inputs:  data/raw/pisa_romania_below_level2_trend.csv
Outputs: figures/06_pisa_below_l2_trend.png
Source:  OECD PISA Country Notes Romania 2018 + 2022; OECD 2025 review.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "pisa_romania_below_level2_trend.csv"
OUT = ROOT / "figures" / "06_pisa_below_l2_trend.png"

df = pd.read_csv(RAW)
subjects = ["Mathematics", "Reading", "Science"]

fig, axes = plt.subplots(1, 3, figsize=(13, 5.5), sharey=True)

for ax, subj in zip(axes, subjects):
    sub = df[df["subject"] == subj].sort_values("year")
    ax.plot(sub["year"], sub["romania_below_l2_pct"], marker="o",
            linewidth=2.6, markersize=10, color="#c0392b", label="Romania")
    ax.plot(sub["year"], sub["oecd_below_l2_pct"], marker="s",
            linewidth=2.0, markersize=8, color="#7f8c8d", label="OECD average")

    for x, y in zip(sub["year"], sub["romania_below_l2_pct"]):
        ax.annotate(f"{y}%", (x, y), xytext=(0, 9),
                    textcoords="offset points", ha="center", fontsize=10,
                    color="#c0392b", fontweight="bold")
    for x, y in zip(sub["year"], sub["oecd_below_l2_pct"]):
        ax.annotate(f"{y}%", (x, y), xytext=(0, -16),
                    textcoords="offset points", ha="center", fontsize=9,
                    color="#7f8c8d")

    ax.set_title(subj, fontsize=12, fontweight="bold", pad=6)
    ax.set_xticks([2012, 2018, 2022])
    ax.set_xticklabels(["2012", "2018", "2022"])
    ax.set_xlim(2010.5, 2023.5)
    ax.set_ylim(0, 60)
    ax.set_yticks(range(0, 61, 10))
    ax.grid(axis="y", alpha=0.25, linestyle="--")
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    # Shaded band from 2006 (start of RO PISA participation) to 2012, marked
    # as "stable since 2006" per OECD 2025.
    ax.axvspan(2006, 2011.5, alpha=0.08, color="#c0392b")
    ax.text(2008.75, 56, "OECD: stable\nsince 2006",
            ha="center", va="top", fontsize=8.5,
            color="#7f1d10", style="italic")
    ax.set_xlim(2005.5, 2023.5)
    ax.set_xticks([2006, 2012, 2018, 2022])
    ax.set_xticklabels(["2006", "2012", "2018", "2022"])

axes[0].set_ylabel("% of 15-year-olds below PISA Level 2", fontsize=10)
axes[0].legend(loc="lower right", frameon=False, fontsize=9)

fig.suptitle(
    "A decade of reform announcements, no movement at the bottom",
    x=0.02, y=0.985, ha="left", fontsize=14, fontweight="bold")
fig.text(0.02, 0.945,
         "Share of Romanian 15-year-olds below baseline PISA proficiency, "
         "by subject and cycle. OECD finds the share has been stable at "
         "high levels since 2006.",
         fontsize=10.5, color="#333")

fig.text(0.02, 0.025,
         "Sources: PISA 2018 + 2022 Romania Country Notes; OECD (2025) "
         "Education and Skills in Romania, Figure 4.11.",
         fontsize=8, color="#666")
fig.text(0.02, 0.008,
         "Note: 2012 values derived from PISA 2022 country note's stated "
         "change between 2012 and 2022 (+7pp math, 0 reading, +6pp science). "
         "2009 and 2015 cycles omitted — full series not retrievable from "
         "public OECD URLs at draft time.",
         fontsize=8, color="#666", style="italic")

plt.subplots_adjust(top=0.83, bottom=0.13, left=0.07, right=0.97, wspace=0.18)
plt.savefig(OUT, dpi=150)
print(f"Wrote {OUT.relative_to(ROOT)}")
