# Data

## Source
Zenodo record 6732794, DOI 10.5281/zenodo.6732794. Licence: Creative Commons Attribution 4.0 (CC-BY 4.0). Redistribution is allowed with credit to the authors (citation in the main README).

Companion paper (open access): Warwick WRAP 171884, *Using photodiodes and supervised machine learning for automatic classification of weld defects in laser welding of thin foils copper-to-steel battery tabs* (2022).

## Files in `raw/` (unchanged from Zenodo)
| File | Contents |
|---|---|
| `Statistic featuress.xlsx` | One sheet per dataset (A, B, C). One row per weld: 6 photodiode features, laser power, gap, label, signal ID. Sheet C also has measured penetration depth (DP) and throat thickness (TS) |
| `Signals - Dataset A/B/C.rar` | One CSV per weld. A 10-line header, then 50 kHz samples of plasma (P), temperature (T), back-reflection (BR) and laser power, raw and filtered ("Eps") |

## Process
Laser lap welding of copper foil (upper) onto 300 µm Ni-plated steel (lower), the cell-to-tab joint in battery packs.
- Sets A and B: uncoated 300 µm copper.
- Set C: Ni-plated 200 µm copper.

## Labels
| Label | Meaning |
|---|---|
| SW | Sound weld |
| LoC | Lack of connection (too little fusion) |
| OP | Overpenetration (burned through the lower foil) |

## Known issues (details in `notes/03_dataset_audit.md`)
- Welds 340, 341, 343 and 344 appear in both A and B. There are **142 unique welds**, not 146.
- Every CSV header says `Result: NOK`, including sound welds. That field is a monitor setting, not a quality label, and is ignored.
