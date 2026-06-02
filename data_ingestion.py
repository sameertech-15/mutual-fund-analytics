import pandas as pd
import os

DATA_FOLDER = "data/raw"

summary = []

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

for file in csv_files:

    filepath = os.path.join(DATA_FOLDER, file)

    print("\n" + "=" * 70)
    print(f"DATASET : {file}")

    df = pd.read_csv(filepath)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    print("\nMissing Values:", missing)
    print("Duplicate Rows:", duplicates)

    summary.append(
        f"{file} | Shape={df.shape} | Missing={missing} | Duplicates={duplicates}"
    )

os.makedirs("reports", exist_ok=True)

with open("reports/data_quality_summary.txt", "w") as report:
    report.write("DATA QUALITY SUMMARY\n\n")
    report.write("\n".join(summary))

print("\nData Quality Report Created Successfully")