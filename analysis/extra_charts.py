"""Control chart, photodiode traces and cross-validation comparison for the report.

Usage: python analysis/extra_charts.py outputs/features_unique.csv data/extracted outputs
"""
import glob
import json
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score
from sklearn.model_selection import GroupKFold, StratifiedKFold, cross_val_predict

feat_csv, sig_dir, out = sys.argv[1], sys.argv[2], sys.argv[3]
u = pd.read_csv(feat_csv)
COLORS = {"LoC": "#c0392b", "OP": "#e67e22", "SW": "#27ae60"}


def header_date(path):
    with open(path, encoding="latin-1") as fh:
        for line in fh:
            if line.startswith("Date:"):
                return pd.to_datetime(line.split(":", 1)[1].strip())
            if line.startswith("Index;"):
                return None


def load_signal(sig_id, s):
    path = os.path.join(sig_dir, f"Dataset_{s}", f"{int(sig_id)}.csv")
    with open(path, encoding="latin-1") as fh:
        skip = next(n for n, line in enumerate(fh) if line.startswith("Index;"))
    d = pd.read_csv(path, sep=";", skiprows=skip, encoding="latin-1")
    d.columns = ["idx", "t", "P_raw", "P", "T_raw", "T", "R_raw", "R", "power"]  # set C names its filtered columns differently
    return d


# 1. Individuals (I) control chart: set C plasma mean in run order, limits from the sound welds
c = u[u.set == "C"].copy()
c["date"] = [header_date(os.path.join(sig_dir, "Dataset_C", f"{int(i)}.csv")) for i in c["Signal ID"]]
c = c.sort_values(["date", "Signal ID"]).reset_index(drop=True)
c["run"] = np.arange(1, len(c) + 1)
sw = c[c.Label == "SW"]["Mean SP [V]"].values
mr_bar = np.abs(np.diff(sw)).mean()
cl, ucl, lcl = sw.mean(), sw.mean() + 3 * mr_bar / 1.128, sw.mean() - 3 * mr_bar / 1.128
c["zone"] = np.where(c["Mean SP [V]"] > ucl, "above", np.where(c["Mean SP [V]"] < lcl, "below", "inside"))
chart = {"CL": round(cl, 3), "UCL": round(ucl, 3), "LCL": round(lcl, 3), "MRbar_sound": round(mr_bar, 3),
         "table": pd.crosstab(c.Label, c.zone).to_dict(),
         "missed_LoC_median_gap": float(c[(c.Label == "LoC") & (c.zone == "inside")]["gap_um"].median())}
fig, ax = plt.subplots(figsize=(10, 4))
for lab, g in c.groupby("Label"):
    ax.scatter(g.run, g["Mean SP [V]"], c=COLORS[lab], label=lab, s=22, zorder=3)
ax.plot(c.run, c["Mean SP [V]"], c="#bbb", lw=.8, zorder=1)
for v, name in [(ucl, "UCL"), (cl, "CL"), (lcl, "LCL")]:
    ax.axhline(v, ls="--" if name != "CL" else "-", c="k", lw=1); ax.text(len(c) + 1, v, f"{name} {v:.2f}", va="center")
ax.set(xlabel="Weld number (run order, set C)", ylabel="Plasma signal mean (V)", title="I-chart of plasma signal; limits from sound welds")
ax.legend(); plt.tight_layout(); plt.savefig(f"{out}/fig_control_chart.png", dpi=150); plt.close()

# 2. Photodiode traces: one weld of each outcome, set C, zero gap
picks = [(666, "LoC", 390), (672, "SW", 690), (677, "OP", 840)]
trace_rows = []
fig, ax = plt.subplots(figsize=(8, 3.6))
for sig_id, lab, power in picks:
    d = load_signal(sig_id, "C")
    d = d[d.t < 0.30]
    d["bin"] = (d.t // 0.0025).astype(int)
    b = d.groupby("bin").agg(t=("t", "min"), p=("P_raw", "mean")).reset_index()
    for _, r in b.iterrows():
        trace_rows.append({"lab": lab, "power": power, "ms": round(r.t * 1000, 1), "v": round(r.p, 3)})
    ax.plot(b.t * 1000, b.p, c=COLORS[lab], label=f"{lab} ({power} W)")
ax.set(xlabel="Time (ms)", ylabel="Plasma signal (V)", title="Plasma photodiode during one weld of each outcome")
ax.legend(); plt.tight_layout(); plt.savefig(f"{out}/fig_photodiode_traces.png", dpi=150); plt.close()

# 2b. Sensor signals by outcome: all six photodiode features (box plots)
fig, axes = plt.subplots(2, 3, figsize=(11, 6))
names = [("Mean SP [V]", "Plasma mean"), ("Mean ST [V]", "Temperature mean"), ("Mean SR [V]", "Back-reflection mean"),
         ("St Dev SP [V]", "Plasma spread"), ("St Dev ST [V]", "Temperature spread"), ("St Dev SR [V]", "Back-reflection spread")]
for ax, (feat, title) in zip(axes.flat, names):
    data = [u.loc[u.Label == lab, feat] for lab in ["LoC", "SW", "OP"]]
    bp = ax.boxplot(data, patch_artist=True, showfliers=False)
    ax.set_xticks([1, 2, 3], ["LoC", "Sound", "OP"])
    for patch, lab in zip(bp["boxes"], ["LoC", "SW", "OP"]):
        patch.set_facecolor(COLORS[lab]); patch.set_alpha(.5)
    ax.set_title(title); ax.set_ylabel("V")
fig.suptitle("Photodiode features by weld outcome (142 welds)")
plt.tight_layout(); plt.savefig(f"{out}/fig_sensor_signals.png", dpi=150); plt.close()

# 3. Cross-validation: random vs grouped by setting
FEATS = ["Mean SP [V]", "St Dev SP [V]", "Mean ST [V]", "St Dev ST [V]", "Mean SR [V]", "St Dev SR [V]"]
u["grp"] = u["set"] + "_" + u["Laser Power [W]"].round().astype(int).astype(str) + "_" + u["gap_um"].astype(str)
X = np.column_stack([u[FEATS].values, (u["set"] == "C").astype(int)]); y = u["Label"].values
rf = RandomForestClassifier(n_estimators=400, random_state=0, class_weight="balanced")
cv_rows = []
for name, cv, groups in [("Random folds", StratifiedKFold(5, shuffle=True, random_state=0), None),
                         ("Grouped by setting", GroupKFold(5), u["grp"])]:
    p = cross_val_predict(rf, X, y, cv=cv, groups=groups)
    rec = dict(zip(["LoC", "OP", "SW"], recall_score(y, p, average=None, labels=["LoC", "OP", "SW"])))
    for metric, val in [("Overall accuracy", (p == y).mean()), ("Lack of connection caught", rec["LoC"]),
                        ("Overpenetration caught", rec["OP"]), ("Sound welds passed", rec["SW"])]:
        cv_rows.append({"method": name, "metric": metric, "v": round(float(val) * 100, 1)})
rf.fit(X, y)
importance = dict(zip(FEATS + ["foil flag"], np.round(rf.feature_importances_, 3)))

json.dump({"control_chart": chart, "importance": importance, "cv": cv_rows}, open(f"{out}/extra_summary.json", "w"), indent=1)
json.dump(c[["run", "Signal ID", "Label", "Mean SP [V]", "gap_um"]].to_dict("records"), open(f"{out}/control_chart_rows.json", "w"))
json.dump(trace_rows, open(f"{out}/trace_rows.json", "w"))
print(json.dumps({"control_chart": chart, "importance": importance, "cv": cv_rows}, indent=1))
print("trace rows", len(trace_rows))
