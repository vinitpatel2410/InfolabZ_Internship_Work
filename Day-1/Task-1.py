import requests
url_isro = "https://isro.vercel.app/api/spacecrafts"
response = requests.get(url_isro)
data_isro = response.json()
for key in data_isro.keys():
    print(key)
print(data_isro["spacecrafts"][0]["name"])