"""Final analysis for the report: every number and figure in Chapter 5 comes from here.

Usage: python analysis/report_analysis.py outputs/features_all.csv outputs
"""
import json
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GroupKFold, cross_val_predict

src, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(src)
u = df.sort_values("set").drop_duplicates("Signal ID", keep="first").copy()  # 142 unique welds
u["foil"] = np.where(u["set"] == "C", "200 um Ni-plated Cu", "300 um Cu")
FEATS = ["Mean SP [V]", "St Dev SP [V]", "Mean ST [V]", "St Dev ST [V]", "Mean SR [V]", "St Dev SR [V]"]
LABELS = ["LoC", "OP", "SW"]
summary = {}

# 1. Outcome counts (Pareto)
counts = u["Label"].value_counts().reindex(LABELS).to_dict()
summary["counts"] = counts
summary["counts_by_set"] = pd.crosstab(u["set"], u["Label"]).to_dict()

# 2. Process window: sound-weld power and gap range per foil
win = {}
for foil, g in u.groupby("foil"):
    sw = g[g.Label == "SW"]
    win[foil] = {"power_min": float(sw["Laser Power [W]"].min()), "power_max": float(sw["Laser Power [W]"].max()),
                 "gap_max": float(sw["gap_um"].max()), "n_settings": int(g.groupby(["Laser Power [W]", "gap_um"]).ngroups)}
summary["window"] = win
summary["min_gap_all_fail_300um"] = float(u[(u.foil == "300 um Cu") & (u.gap_um >= 200)]["Label"].eq("LoC").all())

# 3. Signal comparison
sig = []
for f in FEATS:
    row = {"feature": f}
    for lab in LABELS:
        row[lab] = round(float(u.loc[u.Label == lab, f].median()), 2)
    row["p_SW_vs_LoC"] = float(stats.mannwhitneyu(u.loc[u.Label == "SW", f], u.loc[u.Label == "LoC", f]).pvalue)
    row["p_SW_vs_OP"] = float(stats.mannwhitneyu(u.loc[u.Label == "SW", f], u.loc[u.Label == "OP", f]).pvalue)
    sig.append(row)
summary["signals"] = sig

# 4. Detection: grouped cross-validation by process setting
u["grp"] = u["set"] + "_" + u["Laser Power [W]"].round().astype(int).astype(str) + "_" + u["gap_um"].astype(str)
X = np.column_stack([u[FEATS].values, (u["set"] == "C").astype(int)])
y = u["Label"].values
rf = RandomForestClassifier(n_estimators=400, random_state=0, class_weight="balanced")
pred = cross_val_predict(rf, X, y, cv=GroupKFold(5), groups=u["grp"])
cm = confusion_matrix(y, pred, labels=LABELS)
defect, flagged = y != "SW", pred != "SW"
summary["detection"] = {
    "accuracy": round(float((pred == y).mean()), 3),
    "confusion": {LABELS[i]: dict(zip(LABELS, map(int, cm[i]))) for i in range(3)},
    "defect_catch_rate": round(float((defect & flagged).sum() / defect.sum()), 3),
    "sound_rejected_rate": round(float((~defect & flagged).sum() / (~defect).sum()), 3),
}

# 5. Figures (PNG, for the Word version and the repository)
colors = {"LoC": "#c0392b", "OP": "#e67e22", "SW": "#27ae60"}
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
for ax, foil in zip(axes, ["300 um Cu", "200 um Ni-plated Cu"]):
    s = u[u.foil == foil]
    for lab in LABELS:
        g = s[s.Label == lab]
        ax.scatter(g["Laser Power [W]"], g["gap_um"], c=colors[lab], label=lab, alpha=.8, edgecolor="k", lw=.3, s=40)
    ax.set(xlabel="Laser power [W]", ylabel="Part-to-part gap [µm]", title=f"{foil.replace('um', 'µm')} foil")
    ax.legend()
plt.tight_layout(); plt.savefig(f"{out}/fig_process_window.png", dpi=150); plt.close()

fig, ax = plt.subplots(figsize=(6, 3.5))
order = sorted(counts, key=counts.get, reverse=True)
vals = [counts[k] for k in order]
ax.bar(order, vals, color=[colors[k] for k in order])
ax2 = ax.twinx(); ax2.plot(order, np.cumsum(vals) / sum(vals) * 100, "k-o"); ax2.set_ylim(0, 105); ax2.set_ylabel("Cumulative %")
ax.set_ylabel("Welds"); ax.set_title("Weld outcomes (142 welds, designed experiment)")
plt.tight_layout(); plt.savefig(f"{out}/fig_outcome_pareto.png", dpi=150); plt.close()

rpn = pd.DataFrame([
    ("Sealing", "Void at tab seal", 9, 6, 6), ("Sealing", "Contaminated seal area", 9, 5, 7),
    ("Welding", "LoC - excess gap", 8, 6, 5), ("Welding", "Spatter / porosity", 7, 5, 6),
    ("Welding", "Burn-through", 9, 4, 5), ("Sealing", "Weak seal", 9, 5, 4),
    ("Sealing", "Over-seal / thinning", 7, 4, 6), ("Welding", "LoC - low power", 8, 5, 4),
    ("Sealing", "Wrinkle / misalignment", 6, 4, 4)], columns=["process", "mode", "S", "O", "D"])
rpn["RPN"] = rpn.S * rpn.O * rpn.D
rpn.to_csv(f"{out}/pfmea_rpn.csv", index=False)
fig, ax = plt.subplots(figsize=(8, 4))
r = rpn.sort_values("RPN")
ax.barh(r["process"] + ": " + r["mode"], r["RPN"], color=["#c0392b" if v >= 200 else "#95a5a6" for v in r["RPN"]])
ax.axvline(200, ls="--", c="k"); ax.set_xlabel("RPN"); ax.set_title("PFMEA risk ranking (critical: RPN ≥ 200)")
plt.tight_layout(); plt.savefig(f"{out}/fig_rpn_pareto.png", dpi=150); plt.close()

# Rows for the in-document scatter chart
u[["Laser Power [W]", "gap_um", "Label", "foil"]].rename(columns={"Laser Power [W]": "power"}).to_json(
    f"{out}/scatter_rows.json", orient="records")
json.dump(summary, open(f"{out}/report_summary.json", "w"), indent=2)
print(json.dumps(summary, indent=1))
