import requests
import json

# COVID-19 API
covid_url = "https://data.covid19india.org/data.json"

# 1) Store all data in a variable
response = requests.get(covid_url)
data = response.json()

# Saving data to a file (optional)
with open("covid_data.json", "w") as file:
    json.dump(data, file)

# 2) Highest cases
max_cases = max(data["cases_time_series"], key=lambda x: int(x["dailyconfirmed"]))
highest_cases = int(max_cases["dailyconfirmed"])
date_highest_cases = max_cases["date"]

# 3) Print date of that day
print("Date with the highest cases:", date_highest_cases)

# 4) Print total number of days (count) which have greater than 1 lakh cases
count_greater_than_1_lakh = sum(
    int(entry["dailyconfirmed"]) > 100000
    for entry in data["cases_time_series"]
)
print("Total number of days with more than 1 lakh cases:", count_greater_than_1_lakh)

# 5) Allow the user to insert a date, print cases (1 lakh or not) and the number of cases for that date
user_date = input("Enter a date (in DD-MMM-YY format): ")

# Search for the user-provided date in the data
for entry in data["cases_time_series"]:
    if entry["date"] == user_date:
        cases_on_user_date = int(entry["dailyconfirmed"])
        print("Cases on {}: {}".format(user_date, cases_on_user_date))
        print("1 lakh cases? ", "Yes" if cases_on_user_date >= 100000 else "No")
        break
else:
    print("Date not found in the data.")
