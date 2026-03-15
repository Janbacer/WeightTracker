# Weight Tracker

A lightweight personal weight-tracking web app with chart visualizations, local JSON persistence, and optional photo/scale workflows.

## What this repo contains

- Web app files (HTML/CSS/JS and PWA assets):
  - index.html
  - manifest.json
  - sw.js
  - icon-192.png
  - icon-512.png

## Website: https://janbacer.github.io/WeightTracker/

## Data storage behavior

- The app stores entries locally (browser/local file flow depending on feature path).
- Large raw datasets are intended to stay local.

## Branch workflow used here

- main: clean snapshot / primary branch
- website: branch used for website-related work and deployment flow