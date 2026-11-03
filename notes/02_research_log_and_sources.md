# Research log and sources

## Searches done (3 Nov 2026)
1. Public datasets for battery tab ultrasonic welding, laser welding and pouch sealing.
2. The companion paper for the Zenodo dataset.
3. Scrap rates in cell production, for FMEA occurrence.
4. Field failure cases and recalls, for severity.
5. Leak-test and inspection methods, for detection.
6. Heat-seal process windows and causes of seal failure.
7. Ultrasonic welding tool wear.
8. AIAG-VDA FMEA changes (Action Priority).

## Data availability: findings
| Process | Public data? | Notes |
|---|---|---|
| Laser tab welding | **Yes.** Zenodo 6732794 (used) | 142 unique welds, photodiode signals, labelled, CC-BY |
| Laser welding images | Described, not confirmed downloadable | Din et al. 2023: 3,736 images in 8 classes from a production line |
| Laser welding thermal imaging | Possibly | Hoang et al. 2026 says the data is in a public repository |
| Ultrasonic tab welding | No open dataset found | Many studies; data not published |
| Pouch heat sealing | No open dataset found | Literature only (RSC Advances 2016 experiment; industry articles) |

## Sources
### Dataset and paper
- Zenodo 6732794: https://zenodo.org/records/6732794
- Chianese et al. 2022 (WRAP): https://wrap.warwick.ac.uk/171884/1/WRAP-using-photodiodes-supervised-machine-learning-automatic-classification-weld-defects-laser-welding-thin-foils-copper-to-steel-battery-tabs-2022.pdf
- Photodiodes for gap and penetration detection, MSEC 2021 (WRAP 167205): https://wrap.warwick.ac.uk/167205/

### Welding
- TUM inline failure detection in laser beam welding of battery cells. Defects tested: contaminated surface, gap, connector misalignment. https://portal.fis.tum.de/en/publications/inline-failure-detection-in-laser-beam-welding-of-battery-cells-a/
- Ultrasonic welding failures from material and surface condition, tool and fixture wear (Müller et al. 2023): https://ersearch2.cvtisr.sk/vufind/SummonRecord/FETCH-LOGICAL-c410t-47b8f8eb274862498a1bd37cd1cc1eae4a31b881585a7879db78a2cde6df21a13
- Tool wear monitoring for ultrasonic welding of Li-ion batteries (Illinois): https://experts.illinois.edu/en/publications/tool-wear-monitoring-for-ultrasonic-metal-welding-of-lithium-ion-/
- EWI ultrasonic welding monitoring (60-weld DOE, over 90% classification): https://doi.org/10.1117/12.2583121
- Laser welding defect images, 8 classes (Din et al. 2023): https://doaj.org/article/f370a3818dfc435c8edb8c9d05ffe7f2
- More than 10,000 welds per 85 kWh pack (WRAP MSEC 2021): https://wrap.warwick.ac.uk/167205/1/WRAP-characterization-photodiodes-detection-variations-part-to-part-gap-weld-penetration-depth-during-remote-laser-welding-copper-to-steel-battery-tab-connectors-2021.pdf

### Sealing
- Heat seal properties of polymer–aluminium–polymer films (RSC Advances 2016): https://pubs.rsc.org/en/content/articlehtml/2016/ra/c5ra27097a
- Causes of pouch sealing leakage (TOB New Energy): https://www.tobmachine.com/blog/main-causes-of-pouch-cell-sealing-leakage_b154
- Seal strength spec ≥22.5 N/15 mm; top seals most failure-prone: https://heatsealtester-com.pages.dev/blog/lithium-pouch-cell-heat-sealing-test-methods
- Pouch edge seal integrity (batterydesign.net): https://www.batterydesign.net/battery-cell/formats/pouch-cells/pouch-cell-edge-seal-integrity/

### Occurrence, severity, detection
- Scrap rates by production step (battery-technology.net heatmap): https://battery-technology.net/heatmap-of-quality/
- Chevy Bolt recall (torn anode tab and folded separator; about 142,000 vehicles; about $1.8 B): https://www.nbcnews.com/news/us-news/gm-recalls-all-chevrolet-bolt-electric-cars-over-fire-risk-n1277356
- Marposs leak testing in battery production: https://www.marposs.com/media/32567/d-1/t-file/LEAK-TEST-IN-BATTERY-PRODUCTION.pdf

### FMEA method
- AIAG-VDA FMEA, 2019: seven steps; Action Priority replaces RPN. https://blog.softexpert.com/en/new-edition-of-aiag-vda-fmea-for-the-automotive-sector-check-out-what-has-changed/
  - Caution: this blog describes AP as A/B/C. The handbook itself uses High/Medium/Low. Cite the AIAG & VDA FMEA Handbook (2019) directly in the report.

### TQM classics (as in the sample)
- Deming (1986), *Out of the Crisis*.
- Juran & Godfrey (1999), *Juran's Quality Handbook*.
- Ishikawa (1985), *What Is Total Quality Control?*
