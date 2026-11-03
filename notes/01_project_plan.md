# Project plan

## Topic
**Critical Equipment and Failure Risk Assessment for Quality Improvement.** Case study: battery cell joining, covering laser tab welding and pouch heat sealing.

## Decisions (agreed with the team)
| Item | Decision |
|---|---|
| Format | Same as the sample report (Group 15, Amrita TQM): cover page, abstract, 6 chapters, references, appendix |
| Length | No limit; keep it crisp |
| Scope | Welding and sealing, both |
| Data | Public research data only. The team does the FMEA scoring; Claude supplies the evidence |
| Deliverable | Report only, for now |
| ML | Allowed where it helps. Used as evidence for detection capability |

## What the sample report did and where we go further
| Sample report | Our report |
|---|---|
| Used counts from the dataset's web page and never opened the CSV | Computes every number from the raw files |
| Ranked failure modes only | First ranks the equipment, then the failure modes |
| RPN only | RPN plus AIAG-VDA Action Priority |
| No SPC | Signal-based monitoring band; I-MR chart at the replicated setting (with caveats) |
| No process window | Power × gap process-window map for welding; temperature × time window for sealing |
| No detection evidence | Detection-methods table plus classifier performance, measured without leakage |

## Report outline
1. **Introduction:** why battery joining is quality-critical; problem statement; objectives; scope.
2. **Literature review:** TQM and PDCA; Pareto; FMEA (classic and AIAG-VDA); SPC; equipment criticality; welding and sealing defect studies.
3. **Problem definition:** process map of the cell assembly line, list of stations, data sources, assumptions.
4. **Methods:**
   - criticality matrix rubric
   - data audit
   - Pareto
   - statistical tests
   - process window
   - classifier with grouped cross-validation
   - FMEA rubric
   - fishbone
   - PDCA
5. **Results:**
   1. Equipment criticality ranking
   2. Dataset audit
   3. Pareto of weld outcomes
   4. Good vs defective signal comparison
   5. Welding process window
   6. Detection capability (classifier)
   7. Sealing assessment from literature
   8. FMEA (welding and sealing) with RPN and Action Priority
   9. Fishbone
   10. Control plan and PDCA
6. **Conclusion:** findings, limitations, future work.
7. **Appendix:** reproducibility notes, code location, rubric tables.

## Workflow
1. Data audit (done) → 2. Feasibility (done) → 3. Team scores S/O/D using `04_fmea_evidence.md` → 4. Full analysis and figures → 5. Draft → 6. Review → 7. Final Word file.
