Car Sales Analytics Dashboard
Python · Power BI · DAX · 537,000 transactions

Overview
End-to-end analytics project on a real-world used car auction dataset. Raw messy data was profiled and cleaned entirely in Python, then loaded into Power BI where DAX measures and a 2-page dashboard were built from scratch.

Dashboard Preview
Page 1 — Sales Performance
Show Image
Page 2 — Market & Inventory
Show Image

Data Cleaning Highlights
IssueResolution160 duplicate VINsDroppedCondition scale 0–50 instead of 0–5Divided by 10999,999 odometer placeholdersReplaced with make/model medianJavaScript date formatParsed with custom format stringMixed case body types, lowercase statesStandardisedPrices under $100 or over $200,000Dropped as data errorsTransmission column (11.7% null)Dropped entirely
Final dataset: 537,028 rows · 13 columns · Jan 2014 → Dec 2015

Key Insights

February is the strongest month by both volume (155K units) and revenue
Q1 dominates — Q3 and Q4 are significantly weaker
When volume drops, avg price rises — sparse months sell premium inventory only
Florida and California account for over €2bn in revenue
Budget segment drives 44.8% of total revenue through volume


Tools
Python · pandas · numpy · Power BI Desktop · DAX · GitHub

How to Run

Download dataset from Kaggle
Run cars_dataset_cleaning.py
Open car_sales_dashboard.pbix and refresh data source path
