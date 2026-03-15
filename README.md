# Weight Tracker

Personal weight-tracking web app with manual entry, scale-photo reading, and trend charts.

## Live site

https://janbacer.github.io/WeightTracker/

## Main features

- Log measurements: weight, BMI (auto from saved height), fat, muscle, moisture, bone mass.
- Scan scale photo with Gemini to auto-fill values.
- Choose input source for scan:
  - Take a new photo (camera)
  - Select an existing photo (gallery/files)
- Preview selected image before processing.
- Edit image before processing:
  - Crop
  - Rotate left/right
  - Reset edits
- Charts tab:
  - Line chart with visible individual points
  - Composition comparison bar chart
- History tools:
  - Import JSON
  - Export JSON
  - Delete single entry or all entries

## Storage and privacy

- App data is stored in browser localStorage for this site origin.
- Keys used by the app:
  - wt_v1: entries array
  - wt_ht: saved height
  - wt_gemini: Gemini API key
- Data is not automatically written to project files on disk.
- Use Export to download a weight-data.json backup.

## Project structure

- Web app files at repository root:
  - index.html
  - manifest.json
  - sw.js
  - icon-192.png
  - icon-512.png
- Optional assets and experiments:
  - 7seg/
- Local datasets (kept local by ignore policy):
  - MiFitness_data_original/
  - MiFitness_data_tests/

## Branches

- main: primary branch
- website: website-focused updates and deployment work