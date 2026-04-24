# Car Sales Analytics Dashboard
**Python · Power BI · DAX · 537,000 transactions**

---

## Overview

End-to-end analytics project on a real-world used car auction dataset. Raw messy data was profiled and cleaned entirely in Python, then loaded into Power BI where DAX measures and a 2-page dashboard were built from scratch.

---

## Dashboard Preview

### Page 1 — Sales Performance
[![Sales Performance](https://raw.githubusercontent.com/Dimitris1121/car_sales_dashboard/main/Cars_Dashboard_Sales_Performance.png)](https://raw.githubusercontent.com/Dimitris1121/car_sales_dashboard/main/Cars_Dashboard_Sales_Performance.png)

### Page 2 — Market & Inventory
[![Market & Inventory](https://raw.githubusercontent.com/Dimitris1121/car_sales_dashboard/main/Cars_Dashboard_Market_%26_Inventory.png)](https://raw.githubusercontent.com/Dimitris1121/car_sales_dashboard/main/Cars_Dashboard_Market_%26_Inventory.png)

---

## Data Cleaning Highlights

| Issue | Resolution |
|-------|------------|
| 160 duplicate VINs | Dropped |
| Condition scale 0–50 instead of 0–5 | Divided by 10 |
| 999,999 odometer placeholders | Replaced with make/model median |
| JavaScript date format | Parsed with custom format string |
| Mixed case body types, lowercase states | Standardised |
| Prices under $100 or over $200,000 | Dropped as data errors |
| Transmission column (11.7% null) | Dropped entirely |

**Final dataset: 537,028 rows · 13 columns · Jan 2014 → Dec 2015**

---
## Tools

Python · pandas · numpy · Power BI Desktop · DAX · GitHub

---

## How to Run

1. Download dataset from [Kaggle](https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data)
2. Run `cars_dataset_cleaning.py`
3. Open `car_sales_dashboard.pbix` and refresh data source path
