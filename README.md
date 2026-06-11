# Bluestock Mutual Fund Analytics Capstone

## Project Overview

The Bluestock Mutual Fund Analytics Capstone is an end-to-end data analytics project designed to analyze mutual fund industry trends, fund performance, investor behavior, SIP growth, and portfolio concentration.

The project includes:

* Data ingestion and cleaning
* Exploratory Data Analysis (EDA)
* Performance metric calculations
* Advanced analytics (VaR, CVaR, Rolling Sharpe)
* Investor cohort analysis
* SIP continuity analysis
* Fund recommendation engine
* Interactive Power BI dashboard

---

## Project Architecture

Raw CSV Files
→ Data Cleaning
→ Processed Datasets
→ SQLite Database
→ Python Analytics
→ Power BI Dashboard
→ Final Reports & Insights

---

## Dataset Description

### 01_fund_master

Contains fund metadata including fund house, category, plan, and scheme details.

### 02_nav_history

Historical NAV values for all mutual fund schemes.

### 03_aum_by_fund_house

Assets Under Management (AUM) by fund house.

### 04_monthly_sip_inflows

Monthly SIP inflow trends across the industry.

### 05_category_inflows

Category-wise net inflows and investment trends.

### 06_industry_folio_count

Industry folio statistics across categories.

### 07_scheme_performance

Fund returns, Sharpe ratio, Sortino ratio, risk metrics, and performance indicators.

### 08_investor_transactions

Investor transaction history including SIP, redemption, and lumpsum investments.

### 09_portfolio_holdings

Fund portfolio holdings and sector allocations.

### 10_benchmark_indices

Benchmark index historical performance data.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd mutual_fund_analytics
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the ETL Pipeline

```bash
python scripts/run_pipeline.py
```

---

## Running Advanced Analytics

```bash
python scripts/recommender.py
```

---

## Power BI Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

Dashboard Pages:

1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends
5. Fund Details

---

## Key Analytics Implemented

### Risk Analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)

### Performance Analytics

* Rolling 90-Day Sharpe Ratio
* Fund Return Analysis

### Investor Analytics

* Cohort Analysis
* SIP Continuity Analysis

### Portfolio Analytics

* Herfindahl-Hirschman Index (HHI)
* Portfolio Concentration Analysis

### Recommendation Engine

Top mutual fund recommendations based on risk grade and Sharpe ratio.

---

## Author

Dudekula Sameer
