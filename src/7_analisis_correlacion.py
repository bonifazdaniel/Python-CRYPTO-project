import pandas as pd
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

# Obtener precios para bitcoin y ethereum
btc_price = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days='30')['prices']
eth_price = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days='30')['prices']

# Crear DataFrames
btc_df = pd.DataFrame(btc_price, columns=['timestamp', 'btc_price'])
eth_df = pd.DataFrame(eth_price, columns=['timestamp', 'eth_price'])

# Convertir timestamps a datetime y redondear al día más cercano para mejorar la coincidencia
btc_df['timestamp'] = pd.to_datetime(btc_df['timestamp'], unit='ms').dt.floor('D')
eth_df['timestamp'] = pd.to_datetime(eth_df['timestamp'], unit='ms').dt.floor('D')

# Fusionar los DataFrames en un solo DataFrame usando una unión interna
combined_df = pd.merge(btc_df, eth_df, on='timestamp', how='inner')

# Establecer timestamp como índice
combined_df.set_index('timestamp', inplace=True)

# Calcular los retornos diarios
combined_df['btc_returns'] = combined_df['btc_price'].pct_change()
combined_df['eth_returns'] = combined_df['eth_price'].pct_change()

# Eliminar filas con valores NaN
combined_df = combined_df.dropna()

# Calcular la correlación entre los retornos
correlation = combined_df[['btc_returns', 'eth_returns']].corr()

# Guardar la correlación en un archivo Excel en la carpeta de datos
correlation.to_excel('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\correlaciones_crypto.xlsx')

print("Archivo 'correlaciones_crypto.xlsx' creado con éxito en la carpeta 'data'. Contiene las correlaciones entre retornos:")
print(correlation)

# Verificar cuántos datos quedan después de la fusión
print(combined_df.info())

# Verificar los primeros datos para ver si hay valores faltantes o constantes
print(combined_df.head())

input("Presiona Enter para cerrar")
