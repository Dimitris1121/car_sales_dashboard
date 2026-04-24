import kagglehub
import pandas as pd
import numpy as np
import os


# ── 1. Download & Load ────────────────────────────────────────────────────────
path = kagglehub.dataset_download("syedanwarafridi/vehicle-sales-data")

# Load CSV into DataFrame and preview
csv_path = os.path.join(path, os.listdir(path)[0])
df = pd.read_csv(csv_path)
print(df.head())


# ── 2. Basic Exploration ──────────────────────────────────────────────────────
df.info()
print(df.shape)
print(df.dtypes)


# ── 3. Duplicates ─────────────────────────────────────────────────────────────
# Full duplicate rows
full_dups = df.duplicated().sum()
print(f"Full duplicates: {full_dups}")

# Duplicate VINs (each sale should be unique)
vin_dups = df.duplicated(subset='vin').sum()
print(f"Duplicate VINs : {vin_dups}")

print(f"Before: {len(df):,} rows")
df = df.drop_duplicates(subset='vin', keep='first')
print(f"After:  {len(df):,} rows")


# ── 4. Null Values ────────────────────────────────────────────────────────────
# Count nulls and % per column
null_summary = pd.DataFrame({
    'null_count': df.isnull().sum(),
    'null_pct'  : (df.isnull().sum() / len(df) * 100).round(1)
})
null_summary = null_summary[null_summary['null_count'] > 0]
print(null_summary.sort_values('null_pct', ascending=False))

# Drop transmission column
df = df.drop(columns=['transmission'])
print(f"Columns now: {df.shape[1]}")

# Drop rows where any of these fields are null
critical_cols = ['vin', 'sellingprice', 'mmr', 'saledate', 'odometer', 'body', 'model', 'trim']
before = len(df)
df = df.dropna(subset=critical_cols)
print(f"Rows dropped: {before - len(df):,}")
print(f"Rows remaining: {len(df):,}")

# condition: fix scale first — divide values above 5 by 10, then impute nulls with median
df['condition'] = df['condition'].apply(lambda x: x/10 if x > 5 else x)
median_condition = df['condition'].median()
df['condition'] = df['condition'].fillna(median_condition)
print(f"condition  → filled with median: {median_condition}")

# color & interior: fill with mode
mode_color    = df['color'].mode()[0]
mode_interior = df['interior'].mode()[0]
df['color']    = df['color'].fillna(mode_color)
df['interior'] = df['interior'].fillna(mode_interior)
print(f"color      → filled with mode: {mode_color}")
print(f"interior   → filled with mode: {mode_interior}")

# Final null check — should be all zeros
print("\nFinal null check:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print("All clean ✓" if df.isnull().sum().sum() == 0 else "Still has nulls — check above")


# ── 5. Date Handling ──────────────────────────────────────────────────────────
print(df['saledate'].dtype)
print(df['saledate'].dropna().head(5).tolist())

df['saledate'] = pd.to_datetime(
    df['saledate'].str[:15],
    format='%a %b %d %Y',
    errors='coerce'
)

print(f"Date range : {df['saledate'].min().date()} → {df['saledate'].max().date()}")
print(f"Null dates : {df['saledate'].isna().sum()}")


# ── 6. Numeric Columns ────────────────────────────────────────────────────────
print(df[['year', 'condition', 'odometer', 'mmr', 'sellingprice']].describe().round(1))

# Odometer: flag extremes
print(f"\nUnder 1,000 miles  : {(df['odometer'] < 1000).sum()}")
print(f"Over 300,000 miles : {(df['odometer'] > 300000).sum()}")

print("\nLowest odometer rows:")
print(df[df['odometer'] < 1000][['make', 'model', 'year', 'odometer', 'sellingprice']].head(5))

print("\nHighest odometer rows:")
print(df[df['odometer'] > 300000][['make', 'model', 'year', 'odometer', 'sellingprice']].head(5))

# Replace 999999 placeholders with null
df['odometer'] = df['odometer'].replace(999999, np.nan)
print(f"Placeholders replaced: {df['odometer'].isna().sum()} nulls now")

# Impute with median per make + model (more accurate than global median)
df['odometer'] = df.groupby(['make', 'model'])['odometer'].transform(
    lambda x: x.fillna(x.median())
)

# Catch any remaining (make/model group too small)
global_median = df['odometer'].median()
df['odometer'] = df['odometer'].fillna(global_median)

print(f"Max odometer now: {df['odometer'].max():,.0f}")
print(f"Nulls remaining : {df['odometer'].isna().sum()}")

# Extremely low prices handling
print(df[df['sellingprice'] < 100][['make', 'model', 'year', 'odometer', 'mmr', 'sellingprice']])
print(f"\nRows under $100  : {(df['sellingprice'] < 100).sum()}")
print(f"Rows under $500  : {(df['sellingprice'] < 500).sum()}")

# Drop rows where sellingprice is under $100
before = len(df)
df = df[df['sellingprice'] >= 100]
print(f"Dropped: {before - len(df)} rows")
print(f"Remaining: {len(df):,}")

# Drop rows where mmr is under $100
before = len(df)
df = df[df['mmr'] >= 100]
print(f"Dropped : {before - len(df)} rows")
print(f"Remaining: {len(df):,}")

# Price columns final check
print(df[['mmr', 'sellingprice']].describe().round(1))

# Drop MMR column
df = df.drop(columns=['mmr'])
print(f"Columns remaining: {df.shape[1]}")
print(df.columns.tolist())


# ── 7. Categorical Columns ────────────────────────────────────────────────────
cat_cols = ['make', 'model', 'trim', 'body', 'color', 'interior', 'state', 'seller']

for col in cat_cols:
    print(f"\n{col} ({df[col].nunique()} unique):")
    print(df[col].value_counts().head(10))

df['body'] = df['body'].str.strip().str.title()

# Verify
print(df['body'].value_counts().head(10))


# ── 8. Final Checks ───────────────────────────────────────────────────────────
print("=" * 55)
print(f"  Shape      : {df.shape[0]:,} rows  x  {df.shape[1]} columns")
print(f"  Columns    : {df.columns.tolist()}")

print("\n--- Null check ---")
nulls = df.isnull().sum()
print(nulls[nulls > 0] if nulls.sum() > 0 else "No nulls ✓")

print("\n--- Dtypes ---")
print(df.dtypes)

print("\n--- Numeric ranges ---")
print(df[['condition', 'odometer', 'sellingprice']].describe().round(1))

print("\n--- Categoricals ---")
for col in ['make', 'body', 'transmission', 'color', 'interior']:
    if col in df.columns:
        print(f"  {col:<12}: {df[col].nunique()} unique  — {sorted(df[col].dropna().unique())[:5]}")

print("\n--- Date range ---")
df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce')
print(f"  {df['saledate'].min().date()} → {df['saledate'].max().date()}")

print("\n--- Duplicates ---")
print(f"  Full duplicate rows : {df.duplicated().sum()}")
print(f"  Duplicate VINs      : {df.duplicated(subset='vin').sum()}")

print("\n--- Sample rows ---")
print(df.sample(5, random_state=42))
print("=" * 55)


# ── 9. Export ─────────────────────────────────────────────────────────────────
df.to_csv(r"C:\Users\mypc\Desktop\cars_dataset_cleaned.csv", index=False)
print("Saved ✓")
print(f"Shape: {df.shape[0]:,} rows x {df.shape[1]} columns")
