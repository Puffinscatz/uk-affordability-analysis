# UK Housing Affordability Analysis

## Project Overview

This project explores whether housing affordability has worsened across UK regions by comparing private rents with median monthly pay.

The main affordability measure used is:

```text
Rent-to-pay ratio = average monthly rent / median monthly pay * 100

uk-affordability-analysis/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_exploratory_analysis.ipynb
│
├── outputs/
│   └── charts/
│
└── sql/
    └── analysis_queries.sql