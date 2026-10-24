# Weight Tracker

A personal weight and body-composition tracker. It's a single-page web app (PWA) hosted on GitHub Pages and made to be used from a phone.

**Live site:** https://janbacer.github.io/WeightTracker/

## Features

- **Log** weight, body fat, muscle, moisture and bone, with BMI calculated from your height.
- **Read the scale from a photo:** take or pick a photo of the scale's display, crop or rotate it, and Gemini fills in the values.
- **History** of all entries, with the change since the previous entry, plus JSON import and export.
- **Charts** on a time axis where equal spans of time take equal width (one year is always the same width):
  - the selected metric, with 1M / 3M / 1Y / 3Y / All ranges
  - fat mass and lean mass in kg
  - min–max range and average weight per year
  - latest body composition
- **Cloud sync** to a private GitHub repo, so data survives a phone reset and can be shared between devices.

## Setup

Open the site on your phone and use "Add to Home Screen" to install it like an app. Both settings below are on the **Log** tab.

### Gemini API key (for photo reading)
1. Get a free key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey).
2. Paste it into **Gemini API key**.

### Cloud sync (GitHub)
1. Create a **private** repo (for example `weight-data`) containing a `weight-data.json` file. Use `[]` if you're starting with no data.
2. Create a fine-grained token at [github.com/settings/personal-access-tokens/new](https://github.com/settings/personal-access-tokens/new):
   - **Repository access:** Only select repositories → your data repo
   - **Permissions:** Contents → Read and write
3. In the app, open **Cloud sync (GitHub)**, paste the token, and set the repo as `owner/repo`.

The status label shows `✓ synced HH:MM`, `offline`, or an error such as `token invalid or expired`.

## How sync works

- Your phone keeps its own copy of the data, so the app works offline. The GitHub repo holds the shared copy.
- A sync runs when the app opens, when you return to it, when the phone comes back online, and about a second after each save or delete.
- Entries are matched by **date** (one entry per day). If an entry was changed or deleted on this device since the last sync, this device's version wins. Otherwise the repo's version is used. Additions and deletions therefore carry over in both directions.
- Each sync that changes data makes a commit, so the repo's history works as a full backup.

## Where things are stored

Everything lives in the browser's `localStorage` on each device. Nothing secret is in this repo.

| Key | Contents |
|---|---|
| `wt_v1` | entries (JSON array) |
| `wt_ht` | height in cm |
| `wt_gemini` | Gemini API key |
| `wt_gh_token` | GitHub token |
| `wt_gh_repo` | data repo (`owner/repo`) |
| `wt_gh_base` | copy from the last sync, used for merging |

The keys are stored in plain text on the device and are shared by every site under `janbacer.github.io`. Clearing the site's data removes them; entries can be restored from the repo by syncing again.

**Lost the GitHub token?** GitHub never shows a token again after you create it. Regenerate it in GitHub settings and paste the new one. **Lost the Gemini key?** AI Studio still shows it at the link above.

## Entry format

```json
{
  "date": "2025-12-30",
  "datetime": "2025-12-30T12:45",
  "weight": 88.8,
  "bmi": 22.2,
  "fat": 14.0,
  "muscle": 43.5,
  "moisture": 62.8,
  "bone": 10.0
}
```

Fields other than `date`, `datetime` and `weight` may be `null`.

## Development

There is no build step. The app is `index.html` plus the PWA files (`manifest.json`, `sw.js`, icons). To run it locally:

```sh
python -m http.server 8000
# open http://localhost:8000
```

Charts use [Chart.js](https://www.chartjs.org/) with the date-fns adapter, loaded from a CDN.

### Branches
- `website`: deployed to GitHub Pages
- `main`: older snapshot

### Private data
`.gitignore` keeps personal data out of this public repo: `weight-data.json`, `*.xlsx`, `*.csv`, the `MiFitness_data_*` exports, and the `7seg/` experiments. Before committing after adding new personal files, check `git status`.
