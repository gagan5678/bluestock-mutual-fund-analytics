import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Check if every AMFI code in fund_master exists in nav_history
result = fund_master["amfi_code"].isin(
    nav_history["amfi_code"]
)

print("Validation Summary:")
print(result.value_counts())

# Find missing codes
missing_codes = fund_master[~result]

print("\nMissing Codes:")
print(missing_codes)