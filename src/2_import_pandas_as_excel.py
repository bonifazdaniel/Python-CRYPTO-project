import pandas as pd
from pycoingecko import CoinGeckoAPI

# Crear una instancia de CoinGeckoAPI
cg = CoinGeckoAPI()

# Obtener datos históricos de precios para Bitcoin frente al USD de los últimos 30 días
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days='30')

# Crear un DataFrame con la información de precios
df = pd.DataFrame(bitcoin_data['prices'], columns=['timestamp', 'price'])

# Convertir el timestamp a formato datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Guardar el DataFrame en un archivo Excel en la carpeta de datos
df.to_excel('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\bitcoin_prices.xlsx', engine='openpyxl', index=False)

print("Archivo guardado correctamente en la carpeta data.")

