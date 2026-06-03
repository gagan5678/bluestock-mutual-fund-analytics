import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite
engine = create_engine("sqlite:///bluestock_mf.db")

# ------------------
# dim_fund
# ------------------
fund_df = pd.read_csv("data/raw/01_fund_master.csv")

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

# ------------------
# fact_aum
# ------------------
aum_df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

# ------------------
# dim_date
# ------------------
nav_df = pd.read_csv("data/processed/02_nav_history_clean.csv")

date_df = pd.DataFrame()
date_df["full_date"] = pd.to_datetime(nav_df["date"]).drop_duplicates()

date_df["year"] = date_df["full_date"].dt.year
date_df["quarter"] = date_df["full_date"].dt.quarter
date_df["month"] = date_df["full_date"].dt.month
date_df["day"] = date_df["full_date"].dt.day

date_df.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded")
print("fact_aum loaded")
print("dim_date loaded")
print("All tables loaded successfully!")