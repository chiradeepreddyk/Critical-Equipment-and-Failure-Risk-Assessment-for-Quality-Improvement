# Draft PFMEA scoring (for team review)

## Scales used
**Process FMEA (PFMEA)** scales from the AIAG FMEA Manual, 4th edition. Welding and sealing are process steps, so PFMEA applies rather than design FMEA (DFMEA).

| Scale | Key anchors |
|---|---|
| **Severity (S)** | 10 = safety hazard without warning; 9 = safety hazard with warning; 8 = loss of primary function; 7 = degraded primary function; 6 = loss of secondary function; 5 = degraded secondary function |
| **Occurrence (O)** | 7 ≈ 10 per 1,000; 6 ≈ 2 per 1,000; 5 ≈ 0.5 per 1,000; 4 ≈ 0.1 per 1,000 |
| **Detection (D)** | 4 = automated detection at a later station; 5 = variable gauging or in-station monitor; 6 = gauging after processing; 7 = operator visual check |

## Criticality rule (our choice; state it in the report)
| Class | Rule |
|---|---|
| **Critical** | RPN ≥ 200 |
| **Significant** | RPN 100–199. Action recommended |
| **Low** | RPN < 100. Monitor |
| **Safety flag** | Any S ≥ 9, regardless of RPN. Treated as a special characteristic |

## Draft scores
| ID | Process | Failure mode | Cause (equipment link) | S | O | D | RPN | Class |
|---|---|---|---|---|---|---|---|---|
| S2 | Sealing | Void or channel at the tab seal | Metal tab pulls heat away; tab sealant film misplaced | 9 | 6 | 6 | **324** | Critical, safety |
| S3 | Sealing | Contaminated seal area | Electrolyte or debris on the seal zone | 9 | 5 | 7 | **315** | Critical, safety |
| W1 | Welding | Lack of connection | Excess gap from a worn or misaligned clamp | 8 | 6 | 5 | **240** | Critical |
| W4 | Welding | Spatter or porosity | Surface contamination or oxide on the tab | 7 | 5 | 6 | **210** | Critical |
| W3 | Welding | Overpenetration (burn-through) | Excess power or wrong recipe for the foil | 9 | 4 | 5 | 180 | Significant, safety |
| S1 | Sealing | Weak seal (interfacial failure) | Low temperature or dwell from heater drift | 9 | 5 | 4 | 180 | Significant, safety |
| S4 | Sealing | Over-seal or thinning | Excess temperature or pressure | 7 | 4 | 6 | 168 | Significant |
| W2 | Welding | Lack of connection | Low effective power from a dirty window or ageing laser source | 8 | 5 | 4 | 160 | Significant |
| S5 | Sealing | Wrinkle or misalignment | Sealing jaws misaligned | 6 | 4 | 4 | 96 | Low |

## Reasoning
### Severity
- A leaking pouch lets electrolyte out and moisture in, which forms HF and causes swelling: a safety risk the BMS may warn of, so **S = 9**.
- Burn-through into the cell can cause a leak or internal short, so **S = 9**.
- Lack of connection loses the electrical path; it raises resistance and causes local heating, so **S = 8**.
- Spatter or porosity degrades the joint, so **S = 7**.

### Occurrence
- Scrap at the assembly step ranges from 0.5% to 10% (heatmap), and many modes share that. So each mode is placed at about 0.01–0.2%, which is O = 4–6.
- Tab seals and gap-driven lack of connection get **O = 6**:
  - top seals are reported as the most failure-prone
  - the Zenodo process window shows a gap of about 150–200 µm already causes failure

### Detection
- Welding: the in-line photodiode monitor catches about 88% of defects, with many false alarms (our grouped classifier result), so **D = 5**. Peel tests are destructive and done on samples only.
- Tab voids and contamination can look fine visually and may leak only slowly, so **D = 6–7**.
- A weak seal is caught by the electrolyte-vapour leak test at a later station, so **D = 4**.

## Re-scoring after improvement (to fill in later)
Each critical row gets an action, then new O and D scores, to show the risk reduction.
- **W1:** an automatic gap check before firing, with interlock and fixture maintenance, could take O from 6 to 3 and D from 5 to 3. RPN 240 → 72.
