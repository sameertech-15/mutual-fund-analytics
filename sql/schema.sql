-- Dimension Table

CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
    risk_grade TEXT
);

-- Date Dimension

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE UNIQUE
);

-- NAV Fact Table

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date_id INTEGER,
    nav REAL,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id)
);

-- Transactions Fact

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    investor_id TEXT,
    amfi_code INTEGER,
    date_id INTEGER,

    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id)
);

-- Performance Fact

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,

    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    expense_ratio_pct REAL,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

-- AUM Fact

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,
    aum_crore REAL,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);