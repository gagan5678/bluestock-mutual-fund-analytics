import pandas as pd

# Load data
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Return columns to validate
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Convert return columns to numeric
for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check for invalid numeric values
print("Nulls after numeric conversion:")
print(df[return_cols].isnull().sum())

# Expense Ratio Validation
expense_low = (df["expense_ratio_pct"] < 0.1).sum()
expense_high = (df["expense_ratio_pct"] > 2.5).sum()

print("\nExpense Ratio < 0.1% :", expense_low)
print("Expense Ratio > 2.5% :", expense_high)

# Flag anomalous returns
high_returns = (df["return_1yr_pct"] > 100).sum()
low_returns = (df["return_1yr_pct"] < -100).sum()

print("\nReturn Anomalies:")
print("Return > 100% :", high_returns)
print("Return < -100% :", low_returns)

# Remove duplicates
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nFinal Shape:", df.shape)
print("File Saved Successfully")