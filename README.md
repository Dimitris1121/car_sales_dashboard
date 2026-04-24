# Car Sales Analytics Dashboard
### End-to-end data analytics project — Python cleaning · Power BI reporting

---

## Overview

A full analytics pipeline built on a real-world used car auction dataset of **537,000+ transactions** spanning 2014–2015. The project covers every stage of the analytics workflow: raw data profiling, systematic cleaning in Python, and a professional 2-page Power BI dashboard designed for a sales manager audience.

---

## Dashboard Preview

| Page | Title | Focus |
|------|-------|-------|
| 1 | Sales Performance | Time trends · seasonality · avg price behaviour |
| 2 | Market & Inventory | Makes · body types · states · price tiers |

---

## Dataset

**Source:** [Vehicle Sales Data — Kaggle](https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data)

| Field | Description |
|-------|-------------|
| `year` | Vehicle manufacture year |
| `make` | Brand (Ford, BMW, Toyota…) |
| `model` | Specific model |
| `trim` | Variant level |
| `body` | Body type (Sedan, SUV, Pickup…) |
| `vin` | Unique transaction identifier |
| `state` | US state where sold |
| `condition` | Auction condition score (1–5) |
| `odometer` | Mileage at time of sale |
| `color` / `interior` | Exterior and interior colour |
| `seller` | Dealer / seller name |
| `sellingprice` | Final transaction price |
| `saledate` | Date of sale |

---

## Data Cleaning — Python

All cleaning was performed in Python using `pandas` and `numpy` before loading into Power BI.

### Issues found and resolved

| Issue | Count | Resolution |
|-------|-------|------------|
| Full duplicate rows | 160 | Dropped |
| Duplicate VINs | 160 | Dropped — keep first |
| Null selling price | 335 | Dropped — revenue analysis requires it |
| Null MMR | 238 | Column dropped entirely |
| Null condition | 354 | Fixed scale (0–50 → 0–5), filled with median |
| Null odometer | 247 | Replaced 999,999 placeholders, filled with make/model median |
| Null dates | 162 | Parsed from raw JS format `"Tue Jul 14 2015 00:00:00 GMT+0000"` |
| Null body/model/trim | ~10k | Rows dropped |
| Null color/interior | 744 | Filled with mode |
| Mixed case body types | — | Standardised with `str.title()` + manual SUV fix |
| Lowercase state codes | — | Uppercased with `str.upper()` |
| Selling price outliers | — | Dropped rows under $100 and over $200,000 |
| Condition scale error | 470k+ | Values above 5 divided by 10 to rescale |
| Transmission column | 11.7% null | Dropped entirely |
| Date format | All rows | Sliced to `str[:15]` and parsed with `format='%a %b %d %Y'` |


### Final dataset

| Metric | Value |
|--------|-------|
| Rows | 537,028 |
| Columns | 13 |
| Date range | Jan 2014 → Dec 2015 |
| Selling price range | $100 — $199,999 |
| Condition range | 1.0 — 5.0 |

---

## Power BI Report
## Key Insights

- **February dominates** both volume (155K units) and revenue (€2.1bn) — the strongest single month in the dataset
- **Q1 accounts for the majority of annual revenue** — Q3 and Q4 are significantly weaker
- **April and July are near-dead months** — fewer than 1K transactions each, driven by data availability rather than seasonal demand
- **When volume drops, avg price rises** — July has near-zero volume but the highest avg selling price (€17K), suggesting only premium inventory transacts in slow periods
- **Florida and California lead revenue** — together accounting for over €2bn, well ahead of all other states
- **Sedan and SUV dominate by volume and revenue** — together representing over 60% of total transactions
- **Budget segment drives 44.8% of revenue** despite lower per-unit prices — volume is the key driver

---

## Project Structure

```
car-sales-dashboard/
│
├── data/
│   ├── car_sales_raw.csv          # Original dataset (from Kaggle)
│   └── cars_dataset_cleaned.csv   # Cleaned dataset ready for Power BI
│
├── notebooks/
│   └── cleaning.py                # Full Python cleaning script
│
├── powerbi/
│   └── CarSalesDashboard.pbix     # Power BI report file
│
└── README.md
```

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3 | Data profiling and cleaning |
| pandas | DataFrame manipulation |
| numpy | Numerical operations |
| Power BI Desktop | Data modelling and visualisation |
| DAX | Measures and calculated columns |
| GitHub | Version control and portfolio |

---

## How to Run

1. Download the raw dataset from [Kaggle](https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data)
2. Run `cleaning.py` to produce the cleaned CSV
3. Open `CarSalesDashboard.pbix` in Power BI Desktop
4. Update the data source path to point to your local `cars_dataset_cleaned.csv`
5. Refresh the data — all visuals will populate automatically

---

## Author

Built as a hands-on Power BI training project covering the full analytics pipeline — from raw data audit and systematic cleaning through to DAX measure development and professional dashboard design.
