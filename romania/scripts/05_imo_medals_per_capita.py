"""
Chart 05 — Romania's elite math track, in per-capita terms.

Romania ranks #6 worldwide in all-time IMO golds and #3 by total medals
once measured per million population — among countries with ≥100 total
medals. The chart shows total medals per million inhabitants for the top
~20 IMO countries, with Romania highlighted.

Inputs:  data/raw/imo_medals_population.csv
Outputs: figures/05_imo_medals_per_capita.png
Source:  IMO official results (via Wikipedia all-time medal table); UN
         population estimates (mid-2024).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "imo_medals_population.csv"
OUT = ROOT / "figures" / "05_imo_medals_per_capita.png"

df = pd.read_csv(RAW)
df["medals_per_million"] = df["total_medals"] / df["population_millions"]
df = df.sort_values("medals_per_million", ascending=True).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(11, 8.5))
y = range(len(df))

def color(c):
    if c == "Romania":
        return "#c0392b"
    return "#34495e"

bar_colors = [color(c) for c in df["country"]]
ax.barh(y, df["medals_per_million"], color=bar_colors, alpha=0.88)

ax.set_yticks(y)
ax.set_yticklabels(df["country"])
for tick_label, country in zip(ax.get_yticklabels(), df["country"]):
    if country == "Romania":
        tick_label.set_color("#c0392b")
        tick_label.set_fontweight("bold")

for i, row in df.iterrows():
    is_ro = row["country"] == "Romania"
    label = (f"{row['medals_per_million']:.1f}"
             f"   ({int(row['total_medals'])} medals / "
             f"{row['population_millions']:.1f}M pop)")
    ax.text(row["medals_per_million"] + 0.3, i, label,
            va="center", fontsize=9,
            fontweight="bold" if is_ro else "normal",
            color=color(row["country"]))

ax.set_xlabel("IMO medals per million inhabitants (all-time)", fontsize=10)
ax.set_xlim(0, df["medals_per_million"].max() * 1.55)

fig.suptitle(
    "Romania's IMO performance, normalised by population",
    x=0.02, y=0.98, ha="left", fontsize=14, fontweight="bold")
ax.set_title(
    "By total medals per million inhabitants among the 23 top IMO countries, "
    "Romania ranks 5th — ahead of every major power",
    loc="left", fontsize=11, color="#333", pad=12)

ax.grid(axis="x", alpha=0.25, linestyle="--")
ax.set_axisbelow(True)

fig.text(0.02, 0.025,
         "Source: IMO official results aggregated via Wikipedia's all-time "
         "medal table; population estimates UN Population Division 2024.",
         fontsize=8, color="#666")
fig.text(0.02, 0.008,
         "Note: countries are the top 23 by gold-medal count. Defunct teams "
         "(USSR, East Germany, Czechoslovakia) excluded — their medals are "
         "not attributed to current successor states.",
         fontsize=8, color="#666", style="italic")

for s in ("top", "right"):
    ax.spines[s].set_visible(False)

plt.subplots_adjust(top=0.91, bottom=0.09, left=0.15, right=0.97)
plt.savefig(OUT, dpi=150)
print(f"Wrote {OUT.relative_to(ROOT)}")
