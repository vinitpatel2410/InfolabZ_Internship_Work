import requests
import json
import matplotlib.pyplot as plt

def task_1():
    url = 'https://data.covid19india.org/data.json'
    response = requests.get(url)
    data = response.json()

    statewise_data = data['statewise']
    states = [entry['state'] for entry in statewise_data]
    confirmed = [int(entry['confirmed']) for entry in statewise_data]

    plt.figure(figsize=(12, 8))
    plt.barh(states, confirmed)
    plt.xlabel('Total Confirmed Cases')
    plt.ylabel('States')
    plt.title('COVID-19 Total Confirmed Cases by State')
    plt.tight_layout()
    plt.show()

task_1()
