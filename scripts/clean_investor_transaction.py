import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# print("Shape:", df.shape)

# print("\n Columns: ")
# print(df.columns.tolist())

# print("\n First 5 Rows: ")
# print(df.head())

# print("\n Missing Values: ")
# print(df.isnull().sum())

# 1. Convert date column

df['transaction_date'] = pd.to_datetime(df['transaction_date'])


# 2. Standardize transaction types

df['transaction_type'] = (df['transaction_type'].astype(str).str.strip().str.title())

# Keep only valid trascaction types

valid_types = ['Sip', 'Lumpsum','Redemption']

invalid_types = ~df["transaction_type"].isin(valid_types)
print("Invalid Transaction Types:", invalid_types.sum())

df = df[df["transaction_type"].isin(valid_types)]

# 3. Validate amount > 0
invalid_amount = (df["amount_inr"] <= 0).sum()
print("Invalid Amount Rows:", invalid_amount)

df = df[df["amount_inr"] > 0]

# 4. Standardize KYC Status
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.title()
)

print("\nUnique KYC Status Values:")
print(df["kyc_status"].unique())

# 5. Remove duplicates
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("\nFinal Shape:", df.shape)
print("File Saved Successfully")