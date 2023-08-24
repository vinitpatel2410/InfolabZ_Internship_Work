import requests
url_mutual_fund = "https://api.mfapi.in/mf"
response = requests.get(url_mutual_fund)
data_mutual_fund = response.json()
print(data_mutual_fund[0])
print(data_mutual_fund[0]["schemeCode"])