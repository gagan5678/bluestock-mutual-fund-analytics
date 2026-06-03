import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Shape: ", df.shape)
print("\n Columns: ")
print(df.columns.tolist())
print("\n First 5 rows: ")
print(df.head())
print("\n Missing Values: ")
print(df.isnull().sum())


# 1. Convert date column

df['date'] = pd.to_datetime(df['date'])

# 2. Sort by fund and date

df = df.sort_values(['amfi_code','date'])

# 3. Check duplicates

duplicates = df.duplicated().sum()
print("Duplicate rows: " , duplicates)

df = df.drop_duplicates()

# 4. Validate NAV > 0

invalid_nav = (df['nav']<=0).sum()
print("Invalid Nav rows:", invalid_nav)

# 5. Save cleaned file

df.to_csv("data/processed/02_nav_history_clean.csv", index=False)

print("\nCleaned Shape:", df.shape)
print("File Saved Successfully")