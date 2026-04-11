# Namma Nildana — Bus Stop Map

A lightweight web map for visualizing bus stop accessibility and status along the Sarjapur Road corridor.

## Overview

This project shows a list of surveyed bus stop locations and displays them on an interactive Leaflet map. Each stop includes status details, accessibility notes, facility conditions, and cleanliness observations.

## Files

- `index.html` — Main landing/about page for the project. Contains editable project description, purpose, and usage notes.
- `map.html` — Map application file. Contains the bus stop map UI, marker rendering, search, and popup details.
- `places.json` — Survey dataset containing bus stop names, GPS coordinates, and description metadata.

## Features

- Interactive map powered by Leaflet
- Sidebar search/filter for bus stop entries
- Status legend for existing stops, missing stops, and entries without coordinates
- Detail panel for facilities, accessibility, and cleanliness information
- Counts for total stops, mapped stops, and existing bus stops

## How to run

1. Open `index.html` in a modern browser to view the project overview.
2. Click the `View Map` button on the landing page to open `map.html`.
3. The map loads the bus stop data and displays markers automatically.
4. Click any list item or map marker to view the stop details.

## Notes

- The current implementation embeds the `places` dataset directly inside `index.html`.
- `places.json` is available as a standalone data file, but the app does not automatically load it.

## Extending the project

To use external JSON data instead of the embedded dataset:

1. Move the dataset into `places.json`.
2. Load it via `fetch('places.json')` in the app script.
3. Keep the same object format so the existing rendering logic continues to work.

## Editing pages

- Edit `index.html` to update the landing/about content, project overview, purpose, and instructions.
- Edit `map.html` to change map UI behavior, marker rendering, styles, or data handling.

## Dependencies

- [Leaflet](https://leafletjs.com/) via CDN

## License

This repository does not include an explicit license. Add one if you plan to share or reuse the code publicly.
