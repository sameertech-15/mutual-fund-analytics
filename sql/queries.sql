-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance_cleaned
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV

SELECT
    AVG(nav) AS avg_nav
FROM nav_history_cleaned;

-- 3. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions_cleaned
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Expense Ratio Less Than 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance_cleaned
WHERE expense_ratio_pct < 1;

-- 5. Average 1 Year Return

SELECT
    AVG(return_1yr_pct)
FROM scheme_performance_cleaned;

-- 6. Category Wise Fund Count

SELECT
    category,
    COUNT(*) AS total_funds
FROM scheme_performance_cleaned
GROUP BY category;

-- 7. Risk Grade Distribution

SELECT
    risk_grade,
    COUNT(*) AS total
FROM scheme_performance_cleaned
GROUP BY risk_grade;

-- 8. Gender Wise Investors

SELECT
    gender,
    COUNT(*) AS total
FROM investor_transactions_cleaned
GROUP BY gender;

-- 9. Payment Mode Usage

SELECT
    payment_mode,
    COUNT(*) AS total
FROM investor_transactions_cleaned
GROUP BY payment_mode;

-- 10. Top States by Investment Amount

SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM investor_transactions_cleaned
GROUP BY state
ORDER BY total_investment DESC;