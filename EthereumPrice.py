import requests

url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    eth_price = data['USD']
    print("Ethereum Price:", eth_price)
else:
    print("Erro ao fazer solicitação à API do CryptoCompare:", response.text)
