import requests
import time
def get_bitcoin_price():
    url_bitcoin = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url_bitcoin)
    data_bitcoin = response.json()
    for key in data_bitcoin.keys():
        print(key)
    print(data_bitcoin["bpi"]["USD"]["rate"])
while True:
    get_bitcoin_price()
    time.sleep(10)