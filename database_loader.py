import sqlite3
import pandas as pd

# Connect Database
conn = sqlite3.connect("data/db/bluestock_mf.db")

print("Connected to SQLite Database")

# Load cleaned files
nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

txn = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

perf = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

# Load into SQLite

nav.to_sql(
    "nav_history_cleaned",
    conn,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "investor_transactions_cleaned",
    conn,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "scheme_performance_cleaned",
    conn,
    if_exists="replace",
    index=False
)

print("Tables loaded successfully!")

# Verify counts

print("\nRow Counts")

print(
    "NAV History:",
    len(nav)
)

print(
    "Transactions:",
    len(txn)
)

print(
    "Performance:",
    len(perf)
)

conn.close()

print("\nDatabase loading completed!")