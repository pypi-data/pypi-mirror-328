# My WASDE Package

A client for downloading and querying USDA [WASDE](https://www.usda.gov/oce/commodity-markets/wasde) (World Agricultural Supply and Demand Estimates) CSV data.

## Overview

This package automates the process of:
1. Checking for the latest monthly WASDE report data (published as CSV).
2. Downloading and appending new data to your existing local `Wasde.csv`.
3. Providing a `WasdeCSVClient` class for easy querying and light transformations (like pivoting attributes or computing “Use” and “STU”).

## Features
- Auto-download updated CSV from USDA website.
- Append new months to your local dataset.
- Query by commodity, region, or multiple regions at once.
- Convenient partitioning of estimates (e.g., current year vs. last year vs. two years ago).
- Compute custom fields like “Use” and “STU.”

## Installation

If you’ve published this package to PyPI, install with:

```bash
pip install my-wasde-package
