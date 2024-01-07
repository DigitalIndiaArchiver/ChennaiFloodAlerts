# Flood Alert Checker

This repository contains a Python script to fetch Chennai flood alerts and store them in a JSON file.

## Workflow

The GitHub Actions workflow in this repository runs the `script.py` once every 4 hours to check for new flood alerts, stores them in `stored_alerts.json`, and commits any changes to the repository.