"""
Chart 02 — The functional numeric illiteracy pyramid (BRIO 2025).
The Romanian school system *worsens* numeric literacy as students progress —
and the rural-urban gap widens at every cycle. By liceu, nearly 3 in 4 rural
students are functionally numerically illiterate, vs 30% in major-urban areas.

Inputs:  data/raw/brio_2025_illiteracy_by_cycle_environment.csv
Outputs: figures/02_brio_illiteracy_pyramid.png
Source:  Iliescu & Iancu (2025), BRIO / AVE România.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "brio_2025_illiteracy_by_cycle_environment.csv"
OUT = ROOT / "figures" / "02_brio_illiteracy_pyramid.png"

df = pd.read_csv(RAW)
cycles = ["Primar (1-4)", "Gimnaziu (5-8)", "Liceu (9-12)"]
env_order = ["Rural", "Urban mic", "Metropolitan", "Urban mare"]
env_colors = {
    "Rural":        "#c0392b",
    "Urban mic":    "#e67e22",
    "Metropolitan": "#3498db",
    "Urban mare":   "#27ae60",
}

fig, ax = plt.subplots(figsize=(10, 6.5))

for env in env_order:
    sub = df[df["environment"] == env].set_index("cycle").loc[cycles]
    ax.plot(cycles, sub["illiteracy_pct"], marker="o", linewidth=2.4,
            markersize=9, color=env_colors[env], label=env)
    for x, y in zip(cycles, sub["illiteracy_pct"]):
        offset = 2.4 if env == "Rural" else (-3.6 if env == "Urban mare" else 2.0)
        ax.annotate(f"{y:.0f}%", (x, y), xytext=(0, offset),
                    textcoords="offset points",
                    ha="center", fontsize=9, color=env_colors[env],
                    fontweight="bold")

national = df[df["environment"] == "Total"].set_index("cycle").loc[cycles]
ax.plot(cycles, national["illiteracy_pct"], linestyle="--", linewidth=1.5,
        color="#7f8c8d", marker="s", markersize=6, label="National average",
        alpha=0.8)
for x, y in zip(cycles, national["illiteracy_pct"]):
    ax.annotate(f"{y:.0f}%", (x, y), xytext=(15, -3),
                textcoords="offset points",
                ha="left", fontsize=9, color="#7f8c8d", style="italic")

fig.suptitle(
    "The Romanian school system worsens numeric literacy as students progress",
    x=0.02, y=0.98, ha="left", fontsize=14, fontweight="bold")
ax.set_title(
    "By high school, 73% of rural students are functionally numerically "
    "illiterate — vs 30% in major urban areas",
    loc="left", fontsize=11, color="#333", pad=22)

ax.set_ylabel("% of students functionally numerically illiterate\n"
              "(BRIO categories D + E)", fontsize=10)
ax.set_ylim(0, 85)
ax.set_yticks(range(0, 81, 10))
ax.set_yticklabels([f"{t}%" for t in range(0, 81, 10)])

ax.grid(axis="y", alpha=0.25, linestyle="--")
ax.set_axisbelow(True)

leg = ax.legend(loc="upper left", frameon=False, fontsize=10,
                title="Environment of origin", title_fontsize=10)
leg._legend_box.align = "left"

fig.text(0.02, 0.02,
         "Source: Iliescu & Iancu (2025), Alfabetizarea numerică în România "
         "(BRIO / AVE România), Tables 12 and 25. Normative sample n=9,719.",
         fontsize=8, color="#666")

for s in ("top", "right"):
    ax.spines[s].set_visible(False)

plt.subplots_adjust(top=0.86, bottom=0.13, left=0.10, right=0.96)
plt.savefig(OUT, dpi=150)
print(f"Wrote {OUT.relative_to(ROOT)}")
