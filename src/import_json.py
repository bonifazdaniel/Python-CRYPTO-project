import json
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# Obtén datos históricos de precios para Bitcoin
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days='30')

# Guarda los datos en un archivo JSON
with open('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\bitcoin_data.json', 'w') as f:
    json.dump(bitcoin_data, f)

print("Datos guardados en bitcoin_data.json")

input("Presione Enter para continuar...")
