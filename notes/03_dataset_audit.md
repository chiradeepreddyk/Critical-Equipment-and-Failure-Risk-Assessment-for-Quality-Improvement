# Dataset audit: Zenodo 6732794 (laser welding of battery tabs)

Scripts: `analysis/audit.py`, `analysis/feasibility.py`. Run on 3 Nov 2026.

## 1. Completeness
| Check | Result |
|---|---|
| Rows in workbook | A 46, B 14, C 86 (146 in total) |
| Signal CSVs | 146; every one matches a workbook row, with none missing or extra |
| Missing values | Only DP and TS, which are measured for set C alone (60 blanks, expected) |
| Sampling | 50 kHz; windows of 0.3 s (21 files) or 0.4 s (125 files) |
| Recording period | 28 Aug 2020 to 4 Dec 2020 |

## 2. Issues found
1. **Duplicate welds.** Signal IDs 340, 341, 343 and 344 appear in both A and B with identical values. **Unique welds: 142.** We count each once.
2. **The CSV `Result` field is always `NOK`**, even for sound welds. It is the monitor's setting, not a quality verdict, so we ignore it.
3. **The paper's label rule differs slightly from the data.**
   - The paper says lack of connection (LoC) needs DP < 105 µm **and** TS < 150 µm.
   - In the data, a weld is LoC if **either** condition fails. All 55 LoC welds in set C satisfy the either-or rule.
   - Overpenetration (OP) is judged from a burn mark on a check surface, which is not recorded in the data. So OP and SW cannot be told apart from DP and TS alone: 9 OP welds have dimensions that would pass as sound.
   - Report treatment: use the labels as given and note this.
4. **Different materials.** Set C uses a thinner, Ni-plated copper foil. Pool it with A and B only with a material indicator, or analyse it separately.
5. **The paper's percentages for set C** are slightly off from its own counts (64.4% printed vs 55/86 = 64.0%). Use our computed values.

## 3. Label counts (unique welds)
| Set | LoC | OP | SW | Total |
|---|---|---|---|---|
| A | 12 | 18 | 16 | 46 |
| B (excluding the 4 duplicates) | 6 | 0 | 4 | 10 |
| C | 55 | 22 | 9 | 86 |
| **All** | **73** | **40** | **29** | **142** |

These come from a designed experiment that pushed settings outside the good range on purpose. **They are not production defect rates** and must not be used as FMEA occurrence.

## 4. Experimental design
| Set | Laser power (W) | Gap (µm) |
|---|---|---|
| A | 600–1500 in 9 levels | 0 only |
| B | 1050 only | 0, 100, 200, 300 |
| C | 390, 540, 690, 840, 990 | 0–200, measured on a continuous scale |

- There are 57 distinct settings. 33 were run once; the rest have 2–11 repeats.
- Only 3 settings produced mixed labels, so outcomes are highly repeatable at a given setting.

## 5. Feasibility results
### Process window (`outputs/process_window_preview.png`)
- Sets A and B: sound welds only at **900–1050 W with gap ≤ 100 µm**. Below that power gives LoC, above gives OP, and a gap of 200 µm or more always gives LoC.
- Set C: sound welds only at **540–690 W with gap below about 150 µm**. Higher power gives OP; lower power or a large gap gives LoC.
- Takeaway: the good window is narrow, and **fixture gap and laser power are the two critical equipment functions**.

### Sensor features, sound vs defective (Mann–Whitney test)
- Plasma and temperature means and spreads separate sound welds from LoC (p < 1e-6) and from OP (p < 0.005).
- The back-reflection mean does not separate the classes (p > 0.2).

### Classifier (random forest, 6 features plus a material flag)
| Validation | Accuracy | Sound weld recall | Defect catch rate | False alarms on sound welds |
|---|---|---|---|---|
| Random 5-fold | 0.87 | 0.66 | 0.95 | 0.34 |
| **Grouped by setting, 5-fold** | **0.75** | **0.31** | **0.88** | **0.69** |

**Important.** Repeats of the same setting are nearly identical. If repeats land in both training and test, accuracy looks inflated; this may partly explain the paper's 97%.
- We report the grouped result as the honest estimate.
- Detection reading: an in-line photodiode monitor would catch about 88% of defective welds, but it also rejects many good ones. That supports a **moderate** detection rating, not a strong one.
