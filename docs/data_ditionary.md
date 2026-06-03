# Mutual Fund Analytics Data Dictionary

## dim_fund

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | INTEGER | Unique mutual fund identifier |
| fund_house | TEXT | AMC/Fund House name |
| scheme_name | TEXT | Mutual fund scheme name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Regular/Direct plan |
| launch_date | TEXT | Fund launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | FLOAT | Expense ratio percentage |
| exit_load_pct | FLOAT | Exit load percentage |
| min_sip_amount | INTEGER | Minimum SIP investment |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk category |
| sebi_category_code | TEXT | SEBI classification code |

---

## fact_nav

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | INTEGER | Fund identifier |
| date | DATE | NAV date |
| nav | FLOAT | Net Asset Value |

---

## fact_transactions

| Column | Data Type | Description |
|----------|----------|-------------|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Fund identifier |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | INTEGER | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | FLOAT | Annual income in lakhs |
| payment_mode | TEXT | Mode of payment |
| kyc_status | TEXT | KYC verification status |

---

## fact_performance

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | INTEGER | Fund identifier |
| scheme_name | TEXT | Scheme name |
| fund_house | TEXT | Fund house |
| category | TEXT | Fund category |
| plan | TEXT | Direct/Regular |
| return_1yr_pct | FLOAT | 1-year return |
| return_3yr_pct | FLOAT | 3-year return |
| return_5yr_pct | FLOAT | 5-year return |
| benchmark_3yr_pct | FLOAT | Benchmark return |
| alpha | FLOAT | Alpha ratio |
| beta | FLOAT | Beta ratio |
| sharpe_ratio | FLOAT | Sharpe ratio |
| sortino_ratio | FLOAT | Sortino ratio |
| std_dev_ann_pct | FLOAT | Annualized volatility |
| max_drawdown_pct | FLOAT | Maximum drawdown |
| aum_crore | FLOAT | Assets under management |
| expense_ratio_pct | FLOAT | Expense ratio |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk level |

---

## fact_aum

| Column | Data Type | Description |
|----------|----------|-------------|
| date | DATE | Reporting date |
| fund_house | TEXT | Fund house |
| aum_lakh_crore | FLOAT | AUM in lakh crores |
| aum_crore | FLOAT | AUM in crores |
| num_schemes | INTEGER | Number of schemes managed |