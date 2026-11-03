# FMEA evidence pack (for team scoring)

The team assigns S, O and D scores. This file gives the evidence for each one. Use 1–10 scales:
- **S:** 10 = most severe.
- **O:** 10 = most frequent.
- **D:** 10 = least likely to be detected.

## A. Laser tab welding
| Failure mode | Effect | Causes (equipment link) | Occurrence evidence | Current detection |
|---|---|---|---|---|
| Lack of connection (LoC) | High contact resistance, local heating, power loss, joint can open under vibration | Low laser power from source degradation or a dirty protective window; gap ≥ 150–200 µm from fixture or clamp wear; surface contamination | Industry scrap at cell assembly 0.5–10% (heatmap). In the experiment, LoC appears whenever the gap is large or power is low | Photodiode monitor catches about 88% of defects (our grouped result). Cross-sections and peel tests are destructive and done on samples only |
| Overpenetration (OP) | Burns through the steel can or tab, damages what lies beneath, risks spatter or a leak path | Too much power for the foil thickness; wrong recipe after a material change (set C needs much lower power) | Same scrap range. In the experiment, OP appears at the top power levels | Monitor catches OP well (82% recall when grouped). Visual check of the underside is possible on samples |
| Spatter or porosity | Short-circuit particles, weak joint | Contamination, oxide, unstable focus | Not in the dataset; literature only | Vision inspection |
| Tool wear (ultrasonic variant) | Gradual drop in weld strength | Horn and anvil knurl wear | Tool replacement is a major cost; wear strongly affects joint quality (Illinois) | Tool condition monitoring, periodic peel tests |

**Severity anchor:** the Chevy Bolt recall, blamed on cell defects (a torn anode tab and folded separator), covered about 142,000 vehicles at a cost of about $1.8 billion. This shows that internal joining and tab defects can reach the field as fire risks.

## B. Pouch heat sealing
| Failure mode | Effect | Causes (equipment link) | Occurrence evidence | Current detection |
|---|---|---|---|---|
| Weak seal / interfacial failure | Electrolyte leakage; moisture getting in, which forms HF; swelling; safety risk | Sealing temperature or dwell below the minimum (about 170 °C, 3 s in RSC 2016); low pressure; heater drift | Electrolyte filling scrap 0.1–6% (heatmap) | Electrolyte-vapour leak test on sealed cells; peel test on samples (≥22.5 N/15 mm) |
| Over-seal / degradation | Thinned sealant, damaged aluminium layer, delamination over time | Temperature, pressure or dwell too high; uneven pressure | Same | Visual checks; peel test; seal-thickness measurement |
| Seal void or channel at the tab | Slow leak, fails during cycling | Metal tab pulls heat away; tab sealant film misplaced | Top (tab) seals are more failure-prone than side seals | Leak test; may look fine visually |
| Contaminated seal area | Micro-channels; late failure in storage | Electrolyte, dust or electrode debris on the seal area | Literature (TOB) | Hard to detect; the seal looks visually OK |
| Wrinkle or misalignment | Incomplete seal width | Jaw misalignment, film handling | Literature | Vision inspection of seal width |

**Detection reference (Marposs):**
- Helium tracer in vacuum detects about 10⁻⁵ to 10⁻⁷ mbar·l/s, but only before filling.
- After filling, electrolyte-vapour tracing checks the full pouch seal edge.

## C. Occurrence banding: needs a team decision
The dataset cannot give production frequencies. Proposed approach:
- Map each mode to the scrap-rate range of its step.
- Score occurrence by the upper end of that range, using the AIAG-VDA occurrence table.
- State in the report that occurrence is literature-based.
