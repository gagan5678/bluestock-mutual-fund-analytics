import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav_df = pd.read_csv("data/processed/02_nav_history_clean.csv")
trans_df = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
perf_df = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

# Load into SQLite tables
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)

trans_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)

perf_df.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Data loaded successfully!")