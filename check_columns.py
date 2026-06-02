import pandas as pd

files = [
    "02_nav_history.csv",
    "08_investor_transactions.csv",
    "07_scheme_performance.csv"
]

for file in files:
    print("\n" + "="*50)
    print(file)

    df = pd.read_csv(f"data/raw/{file}")

    print(df.columns.tolist())