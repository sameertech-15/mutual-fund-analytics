import requests
import pandas as pd

funds = {
    "HDFC Top 100": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

nav_data = []

for fund_name, amfi_code in funds.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        latest_nav = data["data"][0]

        nav_data.append({
            "fund_name": fund_name,
            "amfi_code": amfi_code,
            "date": latest_nav["date"],
            "nav": latest_nav["nav"]
        })

        print(f"{fund_name} fetched successfully")

df = pd.DataFrame(nav_data)

df.to_csv("data/raw/live_nav.csv", index=False)

print("\nLive NAV data saved successfully")