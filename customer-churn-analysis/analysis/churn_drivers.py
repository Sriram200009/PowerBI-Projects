"""Re-check the churn dashboard's findings straight from the raw data.

Prints churn rate and sample size for every segment the dashboard uses,
writes them to churn_by_segment.csv, and draws images/churn_drivers.png.

Run from the project folder:  python analysis/churn_drivers.py
"""
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(ROOT / "data" / "customer_churn_data.csv")))
overall = sum(r["churn"] == "1" for r in rows) / len(rows)


def age_band(a):
    a = int(a)
    for hi, label in [(30, "18-30"), (40, "31-40"), (50, "41-50"), (60, "51-60"), (70, "61-70")]:
        if a <= hi:
            return label
    return "71+"


def score_band(s):
    s = int(s)
    for hi, label in [(400, "<=400"), (500, "401-500"), (600, "501-600"), (700, "601-700"), (800, "701-800")]:
        if s <= hi:
            return label
    return "801+"


SEGMENTS = {
    "Products held": (lambda r: r["products_number"], ["1", "2", "3", "4"]),
    "Age": (lambda r: age_band(r["age"]), ["18-30", "31-40", "41-50", "51-60", "61-70", "71+"]),
    "Country": (lambda r: r["country"], ["France", "Spain", "Germany"]),
    "Activity": (lambda r: "Active" if r["active_member"] == "1" else "Inactive", ["Active", "Inactive"]),
    "Gender": (lambda r: r["gender"], ["Male", "Female"]),
    "Tenure (years)": (lambda r: "0-2" if int(r["tenure"]) <= 2 else "3-6" if int(r["tenure"]) <= 6 else "7-10",
                       ["0-2", "3-6", "7-10"]),
    "Credit score": (lambda r: score_band(r["credit_score"]),
                     ["<=400", "401-500", "501-600", "601-700", "701-800", "801+"]),
}

table = []
for name, (key, order) in SEGMENTS.items():
    n, churned = defaultdict(int), defaultdict(int)
    for r in rows:
        k = key(r)
        n[k] += 1
        churned[k] += r["churn"] == "1"
    for k in order:
        table.append((name, k, n[k], churned[k], churned[k] / n[k]))

with open(ROOT / "analysis" / "churn_by_segment.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["segment", "group", "customers", "churned", "churn_rate"])
    for seg, k, n_, c, rate in table:
        w.writerow([seg, k, n_, c, f"{rate:.3f}"])

print(f"Overall churn: {overall:.1%} of {len(rows):,} customers\n")
for seg, k, n_, c, rate in table:
    flag = "  <- small sample" if n_ < 100 else ""
    print(f"{seg:15} {k:9} n={n_:5,}  churn={rate:6.1%}{flag}")

# ---- Chart: one panel per segment, one hue, overall rate as a reference line
BLUE, MUTED, INK, INK2, SURFACE = "#2a78d6", "#b7d3f6", "#0b0b0b", "#52514e", "#fcfcfb"
panels = ["Products held", "Age", "Country", "Activity", "Gender", "Tenure (years)"]
fig, axes = plt.subplots(2, 3, figsize=(12, 5.6), facecolor=SURFACE,
                         gridspec_kw={"height_ratios": [6, 3]})
for ax, seg in zip(axes.flat, panels):
    data = [(k, n_, rate) for s, k, n_, c, rate in table if s == seg]
    labels = [k for k, _, _ in data]
    rates = [rate * 100 for _, _, rate in data]
    colors = [MUTED if n_ < 100 else BLUE for _, n_, _ in data]
    ax.barh(labels, rates, color=colors, height=0.62, zorder=2)
    ax.axvline(overall * 100, color=INK2, linewidth=1, linestyle="--", zorder=1)
    for y, (k, n_, rate) in enumerate(data):
        ax.text(rate * 100 + 1.5, y, f"{rate:.0%}  (n={n_:,})", va="center", fontsize=8.5, color=INK, zorder=3,
                bbox=dict(boxstyle="square,pad=0.15", facecolor=SURFACE, edgecolor="none"))
    ax.set_title(seg, loc="left", fontsize=11, color=INK, fontweight="bold")
    ax.set_xlim(0, 125)
    ax.set_ylim((6 if seg in panels[:3] else 3) - 0.5, -0.5)
    ax.set_facecolor(SURFACE)
    ax.tick_params(colors=INK2, labelsize=9, length=0)
    ax.set_xticks([])
    for side in ["top", "right", "bottom"]:
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color("#d9d8d4")
fig.suptitle("Churn rate by segment (dashed line = 20% overall; pale bars = fewer than 100 customers)",
             x=0.01, ha="left", fontsize=12, color=INK)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(ROOT / "images" / "churn_drivers.png", dpi=160, facecolor=SURFACE)
print("\nSaved images/churn_drivers.png and analysis/churn_by_segment.csv")
