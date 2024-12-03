import json
from pycoingecko import CoinGeckoAPI

# Crear una instancia de CoinGeckoAPI
cg = CoinGeckoAPI()

# Obtener datos históricos de precios para Bitcoin
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days='30')

# Guardar los datos en un archivo JSON en la carpeta relativa 'data'
with open('data/bitcoin_data.json', 'w') as f:
    json.dump(bitcoin_data, f)

print("Archivo 'bitcoin_data.json' guardado correctamente en la carpeta 'data'.")

input("Presione Enter para continuar...")
