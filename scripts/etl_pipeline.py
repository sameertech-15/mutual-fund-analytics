import os

print("=" * 50)
print("BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE")
print("=" * 50)

print("\nRunning Data Ingestion...")
os.system("jupyter nbconvert --to notebook --execute notebooks/01_data_ingestion.ipynb")

print("\nRunning Data Cleaning...")
os.system("jupyter nbconvert --to notebook --execute notebooks/02_data_cleaning.ipynb")

print("\nRunning EDA Analysis...")
os.system("jupyter nbconvert --to notebook --execute notebooks/03_eda_analysis.ipynb")

print("\nRunning Performance Metrics...")
os.system("jupyter nbconvert --to notebook --execute notebooks/04_performance_metrics.ipynb")

print("\nRunning Advanced Analytics...")
os.system("jupyter nbconvert --to notebook --execute notebooks/05_advanced_analytics.ipynb")

print("\nPipeline Execution Completed Successfully!")