import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

def task_3():
    url = 'https://data.covid19india.org/data.json'
    response = requests.get(url)
    data = response.json()

    cases_time_series = data['cases_time_series']
    dates = [datetime.strptime(entry['date'], '%d %B %Y') for entry in cases_time_series]
    new_cases = [int(entry['dailyconfirmed']) for entry in cases_time_series]
    recovered = [int(entry['dailyrecovered']) for entry in cases_time_series]
    deaths = [int(entry['dailydeceased']) for entry in cases_time_series]

    plt.figure(figsize=(12, 8))
    plt.plot(dates, new_cases, color='blue', label='New Cases')
    plt.plot(dates, recovered, color='green', label='Recovered')
    plt.plot(dates, deaths, color='red', label='Deaths')

    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.title('COVID-19 Daily Data')
    plt.legend()
    plt.tight_layout()
    plt.show()

task_3()
