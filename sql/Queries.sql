-- Query 1: Top 5 Funds by 5-Year Return
SELECT scheme_name,
       category,
       return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Query 2:Funds with Expense Ratio Below 1%
SELECT scheme_name,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Query 3: Top States by Investment Amount
SELECT state,
       SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;

-- Query 4: Transaction Count by Type
SELECT transaction_type,
       COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type;

-- Query 5: Average Investment by City Tier
SELECT city_tier,
       ROUND(AVG(amount_inr),2) AS avg_investment
FROM fact_transactions
GROUP BY city_tier
ORDER BY avg_investment DESC;

-- Query 6: Average NAV by Fund
SELECT amfi_code,
       ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- Query 7: Highest Rated Funds
SELECT scheme_name,
       morningstar_rating,
       return_3yr_pct
FROM fact_performance
WHERE morningstar_rating = 5
ORDER BY return_3yr_pct DESC;

-- Query 8: Risk Category Distribution
SELECT risk_grade,
       COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade
ORDER BY fund_count DESC;

-- Query 9: Fund House AUM Ranking
SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;

-- Query 10: Benchmark vs Fund Performance
SELECT scheme_name,
       return_3yr_pct,
       benchmark_3yr_pct,
       ROUND(return_3yr_pct - benchmark_3yr_pct,2) AS excess_return
FROM fact_performance
ORDER BY excess_return DESC;





