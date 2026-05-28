"""
Chart 04 — The rural-urban early-leaving gap across the EU.
A dumbbell chart showing the share of 18-24 year olds who left education
without completing upper secondary, by degree of urbanisation, 2023.

Romania's gap is 24.2 percentage points (27.5% rural vs 3.3% cities) — by
far the largest in the EU. Bulgaria, the runner-up, sits at 14.6 pp. The
dumbbells make the geography of educational exclusion visible at a glance.

Inputs:  data/raw/eurostat_2023_early_leavers_urbanisation.csv
Outputs: figures/04_early_leaving_rural_urban_eu.png
Source:  Eurostat (edat_lfse_30), 2023 reference year.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "eurostat_2023_early_leavers_urbanisation.csv"
OUT = ROOT / "figures" / "04_early_leaving_rural_urban_eu.png"

df = pd.read_csv(RAW)
df = df.sort_values("gap_pp", ascending=True).reset_index(drop=True)

def is_eu_avg(c):    return c == "EU-27 average"
def is_romania(c):   return c == "Romania"

fig, ax = plt.subplots(figsize=(11, 9.5))
y = range(len(df))

for i, row in df.iterrows():
    is_ro = is_romania(row["country"])
    is_avg = is_eu_avg(row["country"])

    line_color = "#c0392b" if is_ro else ("#e67e22" if is_avg else "#bdc3c7")
    city_color = "#c0392b" if is_ro else ("#e67e22" if is_avg else "#3498db")
    rural_color = "#c0392b" if is_ro else ("#e67e22" if is_avg else "#2c3e50")
    lw = 3.2 if is_ro else (2.4 if is_avg else 1.6)
    ms = 11 if is_ro else (9 if is_avg else 7)

    ax.plot([row["cities_pct"], row["rural_pct"]], [i, i],
            color=line_color, linewidth=lw,
            alpha=0.95 if (is_ro or is_avg) else 0.55, zorder=2)
    ax.scatter(row["cities_pct"], i, color=city_color, s=ms*ms, zorder=4,
               edgecolor="white", linewidth=1.0)
    ax.scatter(row["rural_pct"], i, color=rural_color, s=ms*ms, zorder=4,
               edgecolor="white", linewidth=1.0,
               marker="s" if is_ro or is_avg else "o")

    if is_ro or is_avg:
        ax.text(row["cities_pct"] - 0.6, i, f"{row['cities_pct']}%",
                va="center", ha="right", fontsize=9, color=line_color,
                fontweight="bold")
        ax.text(row["rural_pct"] + 0.6, i, f"{row['rural_pct']}%",
                va="center", ha="left", fontsize=9, color=line_color,
                fontweight="bold")
        if is_ro:
            ax.text(row["rural_pct"] + 4.5, i,
                    f"gap: {row['gap_pp']:.1f} pp",
                    va="center", ha="left", fontsize=9, color="#c0392b",
                    fontweight="bold", style="italic")

ax.set_yticks(list(y))
labels = [f"{r['country']}" + (" ←" if is_romania(r["country"]) else "")
          for _, r in df.iterrows()]
ax.set_yticklabels(labels)
for tick_label, country in zip(ax.get_yticklabels(), df["country"]):
    if is_romania(country):
        tick_label.set_color("#c0392b")
        tick_label.set_fontweight("bold")
    elif is_eu_avg(country):
        tick_label.set_color("#e67e22")
        tick_label.set_fontweight("bold")

ax.set_xlim(-2, 35)
ax.set_xticks(range(0, 31, 5))
ax.set_xticklabels([f"{t}%" for t in range(0, 31, 5)])
ax.set_xlabel("% of 18-24 year olds who left school before upper-sec completion",
              fontsize=10)

ax.grid(axis="x", alpha=0.25, linestyle="--")
ax.set_axisbelow(True)

fig.suptitle(
    "Romania's rural-urban early-leaving gap is by far the EU's widest",
    x=0.02, y=0.985, ha="left", fontsize=14, fontweight="bold")
ax.set_title(
    "27.5% of rural 18-24 year olds left school early in 2023, vs 3.3% in "
    "cities. The 24.2-point gap is ~10 points wider than Bulgaria's, the EU runner-up.",
    loc="left", fontsize=10.5, color="#333", pad=14)

from matplotlib.lines import Line2D
legend_items = [
    Line2D([0],[0], marker="o", linestyle="", color="#3498db",
           markersize=9, label="Cities (other EU)"),
    Line2D([0],[0], marker="o", linestyle="", color="#2c3e50",
           markersize=9, label="Rural (other EU)"),
    Line2D([0],[0], marker="s", linestyle="", color="#c0392b",
           markersize=10, label="Romania"),
    Line2D([0],[0], marker="s", linestyle="", color="#e67e22",
           markersize=10, label="EU-27 average"),
]
ax.legend(handles=legend_items, loc="lower right", frameon=False,
          fontsize=9, ncol=1)

fig.text(0.02, 0.02,
         "Source: Eurostat dataset edat_lfse_30 (early leavers from education "
         "and training by degree of urbanisation), 2023.",
         fontsize=8, color="#666")
fig.text(0.02, 0.005,
         "Note: countries with no rural data (BA, EU-27 candidate countries) "
         "omitted. Countries with negative gaps (urban > rural) include AT, "
         "DE, IT — typically reflecting urban concentration of disadvantage.",
         fontsize=8, color="#666", style="italic")

for s in ("top", "right"):
    ax.spines[s].set_visible(False)

plt.subplots_adjust(top=0.91, bottom=0.09, left=0.13, right=0.97)
plt.savefig(OUT, dpi=150)
print(f"Wrote {OUT.relative_to(ROOT)}")
