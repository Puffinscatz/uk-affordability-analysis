# UK Housing Affordability Analysis

## Project Overview

This project explores whether housing affordability has worsened across UK regions by comparing private rents with median monthly pay.

The main affordability measure used is:

```text
Rent-to-pay ratio = average monthly rent / median monthly pay * 100

```
## Project Structure

```text
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

```
## Research Questions

- Which UK regions currently have the highest rent-to-pay ratios?
- Have rents grown faster than wages over time?
- Which regions have experienced the largest change in affordability pressure?

## Tools Used

- Python
- pandas
- matplotlib
- plotly
- Streamlit
- Git/GitHub

## Data Sources

- Office for National Statistics: Price Index of Private Rents
- Office for National Statistics: PAYE Real Time Information median pay data

## How to Run the Dashboard

Install the required packages:

```bash
pip install -r requirements.txt

```markdown
![Dashboard preview](outputs/charts/dashboard_screenshot.png)