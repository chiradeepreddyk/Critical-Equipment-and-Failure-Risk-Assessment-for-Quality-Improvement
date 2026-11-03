# Project risk register: what can go wrong, and how we handle it

| # | Risk | Impact if ignored | Mitigation |
|---|---|---|---|
| 1 | Dataset is small (142 welds) and from a lab | Examiner says the results aren't representative | Frame it as a process-characterisation study. Make no production claims. Use the data for cause-and-effect, process window and detection, not for frequency |
| 2 | Experiment defect counts mistaken for production rates | Wrong FMEA occurrence; overclaiming | Take occurrence from industry scrap-rate ranges; state the source of every number |
| 3 | Duplicate welds in A and B | Counts and ML results slightly wrong | De-duplicate to 142 (already done) |
| 4 | Label-rule inconsistency in the paper | Questions about the labels | Use labels as given; document the either-or rule in an appendix |
| 5 | Mixing two foil materials | Spurious process window and features | Separate plots per material; material flag in the ML model |
| 6 | ML leakage from replicate welds | Inflated accuracy (87% instead of 75%) | Grouped cross-validation by setting; report the honest number and explain why it is lower than the paper's |
| 7 | Cp/Cpk on experiment data is invalid | Statistically wrong conclusions | No Cpk across the experiment. Use an individuals chart at the most replicated setting and a signal monitoring band from sound welds, both labelled illustrative |
| 8 | No sealing dataset | The sealing section looks thin | Use published experiment trends and specs. Label it a literature-based assessment. Add a process-window schematic. Never invent numbers |
| 9 | Topic says "equipment", but the data is about weld quality | Examiner says it's off-topic | Start with an equipment criticality ranking. Map every defect to an equipment function: laser source and optics → power; fixture and clamp → gap; sealing head → temperature and pressure |
| 10 | FMEA scores look arbitrary | Low marks for rigour | Publish the rubric (AIAG-VDA tables); tie each score to the evidence pack; add Action Priority; run a ±1 sensitivity check on rankings |
| 11 | Overclaiming in the conclusions | Credibility loss | Keep separate sections for confirmed findings, interpretation and recommendations, as the sample does |
| 12 | Copied wording from sources | Plagiarism flag | Paraphrase; cite every source; redraw figures ourselves; credit the CC-BY dataset |
| 13 | Results can't be reproduced | Hard to answer viva questions | Scripts and raw data in Git; README with run steps |
| 14 | Recency of references | Report looks dated | Mix the TQM classics with 2020–2026 battery manufacturing papers |
| 15 | Sharing someone else's report | Privacy or courtesy issue | The sample report is not stored in this repo |

## Fallback if the welding data proves too weak
Not needed on current evidence: the process window and sensor separation are both clear.

If the team still wants to switch, the alternatives are:
- the Intel arc-welding multimodal dataset (more than 4,000 samples; not battery-specific)
- the AI4I 2020 dataset, which the sample report already uses, so it's less original
