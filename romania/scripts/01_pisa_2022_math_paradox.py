"""
Chart 01 — Romania's PISA 2022 math paradox: many more low achievers AND fewer top
performers than EU/CEE peers. This single chart undermines the comforting narrative
that the elite track survives while only the bottom suffers — both ends are weak.

Inputs:  data/raw/pisa_2022_math_low_top.csv
Outputs: figures/01_pisa_2022_math_paradox.png
Source:  OECD (2025), Education and Skills in Romania, Figure 1.1 (PISA 2022).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "pisa_2022_math_low_top.csv"
OUT = ROOT / "figures" / "01_pisa_2022_math_paradox.png"

df = pd.read_csv(RAW)
df = df.sort_values("low_achievers_below_L2_pct").reset_index(drop=True)

fig, ax = plt.subplots(figsize=(10, 6.5))

y = range(len(df))
colors = ["#c0392b" if c == "Romania"
          else "#7f8c8d" if c == "OECD average"
          else "#34495e" for c in df["country"]]

ax.barh(y, df["low_achievers_below_L2_pct"], color=colors, alpha=0.85,
        label="Low achievers (below Level 2)")
ax.barh(y, -df["top_performers_L5_or_6_pct"], color=colors, alpha=0.5,
        label="Top performers (Level 5 or 6)")

ax.set_yticks(y)
ax.set_yticklabels(df["country"])
ax.axvline(0, color="black", linewidth=0.6)

ax.set_xlabel("% of 15-year-olds")
xticks = [-15, -10, -5, 0, 10, 20, 30, 40, 50, 60]
ax.set_xticks(xticks)
ax.set_xticklabels([f"{abs(t)}%" for t in xticks])

for i, row in df.iterrows():
    ax.text(row["low_achievers_below_L2_pct"] + 1, i,
            f"{row['low_achievers_below_L2_pct']}%", va="center", fontsize=9)
    ax.text(-row["top_performers_L5_or_6_pct"] - 1, i,
            f"{row['top_performers_L5_or_6_pct']}%",
            va="center", ha="right", fontsize=9)

fig.suptitle("Romania's PISA 2022 math paradox", x=0.02, y=0.98,
             ha="left", fontsize=14, fontweight="bold")
ax.set_title(
    "Far more low achievers, and fewer top performers, than any other "
    "EU peer except Bulgaria",
    loc="left", fontsize=11, color="#333", pad=22)

ax.annotate("← Top performers (Level 5/6)", xy=(-7.5, -0.9),
            fontsize=9, color="#555", ha="center")
ax.annotate("Low achievers (below Level 2) →", xy=(30, -0.9),
            fontsize=9, color="#555", ha="center")

fig.text(0.02, 0.02,
         "Source: OECD (2025), Education and Skills in Romania, Fig. 1.1A "
         "(OECD PISA 2022 Database).",
         fontsize=8, color="#666")

for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.invert_yaxis()

plt.subplots_adjust(top=0.86, bottom=0.12, left=0.16, right=0.96)
plt.savefig(OUT, dpi=150)
print(f"Wrote {OUT.relative_to(ROOT)}")
