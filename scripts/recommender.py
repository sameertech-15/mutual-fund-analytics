import pandas as pd

df = pd.read_csv("../data/processed/07_scheme_performance_cleaned.csv")

def recommend_funds(risk_grade="Low", top_n=3):

    filtered = df[
        df["risk_grade"].str.lower() ==
        risk_grade.lower()
    ]

    recommendations = (
        filtered
        .sort_values(
            by="sharpe_ratio"
            ascending=False
        )
        .head(top_n)
    )

    return recommendations[
    [
        "amfi_code",
        "scheme_name",
        "sharpe_ratio",
        "risk_grade"
    ]
]

if __name__ == "__main__":

    print(recommend_funds("Low"))