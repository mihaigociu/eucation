"""
Chart 03 — Romania's IT workforce paradox.
Despite hosting a large IT sector by GDP weight (6.67% direct contribution per
ANIS), Romania has the second-lowest share of ICT specialists in total
employment of any EU member state — 2.8%, less than half the Sweden top
(8.6%) and well below the EU-27 average of 5.0%. The success story is
narrow, not broad-based.

Inputs:  data/raw/eurostat_2024_ict_specialists_share.csv
Outputs: figures/03_ict_specialists_eu_2024.png
Source:  Eurostat (isoc_sks_itspt), 2024 reference year.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "eurostat_2024_ict_specialists_share.csv"
OUT = ROOT / "figures" / "03_ict_specialists_eu_2024.png"

df = pd.read_csv(RAW)
eu_avg = df.loc[df["is_eu"] == "EU_AVG", "ict_share_pct"].iloc[0]
countries = df[df["is_eu"] == "Y"].sort_values("ict_share_pct",
                                               ascending=True).reset_index(drop=True)

def color(c):
    if c == "Romania":
        return "#c0392b"
    if c == "Greece":
        return "#7f8c8d"
    return "#34495e"

colors = [color(c) for c in countries["country"]]

fig, ax = plt.subplots(figsize=(10, 9))
y = range(len(countries))
ax.barh(y, countries["ict_share_pct"], color=colors, alpha=0.85)

ax.set_yticks(y)
ax.set_yticklabels(countries["country"])

for i, row in countries.iterrows():
    ax.text(row["ict_share_pct"] + 0.1, i, f"{row['ict_share_pct']}%",
            va="center", fontsize=9,
            fontweight="bold" if row["country"] == "Romania" else "normal",
            color=color(row["country"]))

ax.axvline(eu_avg, color="#e67e22", linewidth=1.5, linestyle="--", alpha=0.9)
ax.text(eu_avg + 0.08, len(countries) - 0.2,
        f"EU-27 average: {eu_avg}%",
        color="#e67e22", fontsize=9, fontweight="bold", va="top")

ax.set_xlabel("% of total employment", fontsize=10)
ax.set_xlim(0, 10)
ax.set_xticks(range(0, 11))
ax.set_xticklabels([f"{t}%" for t in range(0, 11)])

fig.suptitle("Romania's IT workforce paradox",
             x=0.02, y=0.98, ha="left", fontsize=14, fontweight="bold")
ax.set_title(
    "Among the EU's largest IT sectors by GDP share, but second-lowest by "
    "ICT-specialist employment share",
    loc="left", fontsize=11, color="#333", pad=18)

ax.grid(axis="x", alpha=0.25, linestyle="--")
ax.set_axisbelow(True)

fig.text(0.02, 0.02,
         "Source: Eurostat (isoc_sks_itspt), 2024. ICT specialists = ISCO "
         "workers in ICT development, operation or maintenance.",
         fontsize=8, color="#666")
fig.text(0.02, 0.005,
         "Note: ANIS 2024 reports Romanian IT sector direct GDP contribution "
         "at 6.67% (5.01% for IT only) — among the EU's highest.",
         fontsize=8, color="#666", style="italic")

for s in ("top", "right"):
    ax.spines[s].set_visible(False)

plt.subplots_adjust(top=0.89, bottom=0.09, left=0.16, right=0.96)
plt.savefig(OUT, dpi=150)
print(f"Wrote {OUT.relative_to(ROOT)}")
