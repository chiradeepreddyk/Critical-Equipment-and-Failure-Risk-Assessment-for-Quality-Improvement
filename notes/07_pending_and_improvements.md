# Report status, pending work and improvements

**Report draft:** Claude Doc "Critical Equipment and Failure Risk Assessment for Quality Improvement" (https://claude.ai/artifact/TAQsyAXBzLaBaZ1ncbRJby). It exports to Word or PDF.

## Pending (team)
- [ ] Confirm the cover page: names, roll numbers, guide and group number are copied from the sample report.
- [ ] Review the criticality scores in Section 5.1. These are team-judgement ratings.
- [ ] Review the S/O/D scores and the revised scores after actions in Section 5.10.
- [ ] Export to Word and apply college formatting: page numbers, header "Group __ | Total Quality Management", table of contents, figure and table numbers.
- [ ] Merge the "Process" cells in the PFMEA table in Word. The doc shows the process once per group, but cannot merge cells.
- [ ] Final read-through for wording and consistency.

## Improvements (optional, in order of value)
1. **Action Priority column:** add AIAG-VDA Action Priority (H/M/L) next to RPN in the PFMEA.
2. **Sensitivity check:** change each S, O and D by ±1 and show the top-4 ranking stays the same. Answers "aren't your scores arbitrary?"
3. **Cost of poor quality box:** the Bolt recall (about $1.8 B, about 142,000 vehicles) as a short example in Chapter 1.
4. **Viva preparation:** one page of likely questions (Why 142 welds? Why PFMEA, not DFMEA? Why is your accuracy lower than the paper's?).

## Done on 3 Nov 2026 (second pass)
- I-chart of plasma signal mean for set C (86 welds, limits from sound welds): flags 19/22 overpenetrations with no false alarms; misses 34/55 lack-of-connection welds, mostly 200 µm gaps. Section 5.11; `outputs/fig_control_chart.png`.
- Photodiode trace chart: one weld of each outcome (Section 5.5); `outputs/fig_photodiode_traces.png`.
- Cross-validation comparison: random vs grouped folds (Section 5.6).
- Script: `analysis/extra_charts.py`.

## Done on 3 Nov 2026 (third pass)
- Control plan is now its own Section 5.12. It is a full control plan with 12 rows grouped by process (Sealing, Welding), product vs process type, spec, method, frequency, control method, reaction plan, and the PFMEA risk with its RPN.
- Sensor-signals graph (median and interquartile range of all 6 photodiode features by outcome) replaces the median table in Section 5.5; `outputs/fig_sensor_signals.png`.
- Removed repeats: the signal median table, the control-chart outcome table (counts are in the chart subtitle), and the duplicate "paper reported 97%" bullet (now marked on the cross-validation chart).
- Limitations renumbered to 5.13.

## More graph ideas (not yet added)
- Feature importance bar chart (plasma and temperature means rank highest).
- Penetration depth vs laser power for set C (measured DP values).
- Before vs after RPN chart for the four critical risks.
- Criticality heat map of the 7 stations × 4 factors.
