import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime


# Task-4: Line graph with user-entered start and end dates
def task_4(start_date, end_date):
    url = 'https://data.covid19india.org/data.json'
    response = requests.get(url)
    data = response.json()

    cases_time_series = data['cases_time_series']
    dates = [datetime.strptime(entry['date'], '%d %B %Y') for entry in cases_time_series]
    daily_confirmed = [int(entry['dailyconfirmed']) for entry in cases_time_series]

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    filtered_dates = []
    filtered_cases = []
    for date, cases in zip(dates, daily_confirmed):
        if start_date <= date <= end_date:
            filtered_dates.append(date)
            filtered_cases.append(cases)

    plt.figure(figsize=(12, 8))
    plt.plot(filtered_dates, filtered_cases, color='blue')

    plt.xlabel('Date')
    plt.ylabel('Daily Confirmed Cases')
    plt.title('COVID-19 Daily Confirmed Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Run Task-4
start_date = input('Enter the start date (YYYY-MM-DD): ')
end_date = input('Enter the end date (YYYY-MM-DD): ')
task_4(start_date, end_date)
