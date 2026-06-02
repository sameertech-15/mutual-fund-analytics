import pandas as pd
import os

# Create processed folder if not exists
os.makedirs("data/processed", exist_ok=True)

print("Loading datasets...")

nav = pd.read_csv("data/raw/02_nav_history.csv")
txn = pd.read_csv("data/raw/08_investor_transactions.csv")
perf = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Datasets loaded successfully!")

# ======================================
# NAV HISTORY CLEANING
# ======================================

print("\nCleaning NAV History...")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    by=["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

print("NAV History cleaned")

# ======================================
# INVESTOR TRANSACTIONS CLEANING
# ======================================

print("\nCleaning Investor Transactions...")

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

txn = txn[
    txn["transaction_type"].isin(valid_types)
]

txn = txn[
    txn["amount_inr"] > 0
]

txn["kyc_status"] = (
    txn["kyc_status"]
    .str.strip()
    .str.title()
)

txn = txn.drop_duplicates()

print("Investor Transactions cleaned")

# ======================================
# SCHEME PERFORMANCE CLEANING
# ======================================

print("\nCleaning Scheme Performance...")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf = perf.drop_duplicates()

perf = perf[
    perf["expense_ratio_pct"].between(
        0.1,
        2.5
    )
]

print("Scheme Performance cleaned")

# ======================================
# SAVE CLEANED FILES
# ======================================

nav.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

txn.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

perf.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaned files saved successfully!")