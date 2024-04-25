import requests

url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    btc_price = data['USD']
    print("Bitcoin Price:", btc_price)
else:
    print("Erro ao fazer solicitação à API do CryptoCompare:", response.text)
