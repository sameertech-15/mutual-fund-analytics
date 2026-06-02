# Data Dictionary

## 02_nav_history_cleaned.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Mutual Fund Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## 08_investor_transactions_cleaned.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | String | Unique Investor ID |
| transaction_date | Date | Transaction Date |
| transaction_type | String | SIP/Lumpsum/Redemption |
| amount_inr | Float | Investment Amount |
| state | String | Investor State |
| city | String | Investor City |
| kyc_status | String | KYC Verification Status |

---

## 07_scheme_performance_cleaned.csv

| Column | Type | Description |
|----------|----------|----------|
| scheme_name | String | Mutual Fund Name |
| category | String | Fund Category |
| return_1yr_pct | Float | 1 Year Return |
| return_3yr_pct | Float | 3 Year Return |
| return_5yr_pct | Float | 5 Year Return |
| expense_ratio_pct | Float | Expense Ratio |
| aum_crore | Float | Assets Under Management |
| risk_grade | String | Risk Classification |