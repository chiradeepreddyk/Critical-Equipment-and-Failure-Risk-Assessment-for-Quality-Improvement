# Critical Equipment and Failure Risk Assessment for Quality Improvement

TQM course project. The case study is lithium-ion battery joining: **laser tab welding** (analysed with real sensor data) and **pouch-cell heat sealing** (assessed from published research).

## Status
- [x] Sample report reviewed (structure and gaps noted in `notes/01_project_plan.md`)
- [x] Public data sources researched (`notes/02_research_log_and_sources.md`)
- [x] Zenodo weld dataset downloaded and audited (`notes/03_dataset_audit.md`)
- [x] Feasibility check: process window and a leakage-safe classifier (`analysis/feasibility.py`)
- [x] FMEA evidence collected for team scoring (`notes/04_fmea_evidence.md`)
- [x] Project risks and mitigations listed (`notes/05_risk_register.md`)
- [ ] Team S/O/D scoring
- [ ] Full analysis and figures
- [ ] Report draft

## Repository layout
| Path | Contents |
|---|---|
| `data/raw/` | Original Zenodo files, unchanged (CC-BY 4.0, see `data/README.md`) |
| `analysis/` | Python scripts |
| `outputs/` | Generated tables and figures |
| `notes/` | Plan, research log, audit, FMEA evidence, risk register |

## Reproduce
```bash
pip install pandas openpyxl scipy scikit-learn matplotlib libarchive-c
python analysis/extract.py data/raw data/extracted            # unpack the RAR signal files
python analysis/audit.py "data/raw/Statistic featuress.xlsx" data/extracted outputs/features_all.csv
python analysis/feasibility.py outputs/features_all.csv outputs
```

## Dataset citation
Chianese G., Sun T., Franciosa P., Ceglarek D., Patalano S. (2022). *Using photodiodes and supervised machine learning for automatic classification of weld defects in laser welding of thin foils copper-to-steel battery tabs* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6732794
