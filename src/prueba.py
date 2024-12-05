# script para identificar exactamente dónde se produce el fallo. Comienza solo con la carga de datos y una visualización simple

import pandas as pd
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
import logging

# Configurar logs para registrar resultados y errores
logging.basicConfig(filename='data/script_log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

try:
    # Crear una instancia de CoinGeckoAPI
    cg = CoinGeckoAPI()

    # Obtener datos históricos de precios para Bitcoin frente al USD de los últimos 30 días
    bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days='30')

    # Crear un DataFrame con la información de precios
    df = pd.DataFrame(bitcoin_data['prices'], columns=['timestamp', 'price'])

    # Convertir el timestamp a formato datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Guardar el DataFrame en un archivo Excel en la carpeta relativa 'data'
    df.to_excel('data/bitcoin_prices_prueba.xlsx', engine='openpyxl', index=False)
    logging.info('Archivo guardado como bitcoin_prices_prueba.xlsx en la carpeta data.')

    # Gráfico de prueba
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['price'], label='Precio de Bitcoin')
    plt.title('Prueba de Gráfico de Precios de Bitcoin')
    plt.xlabel('Fecha')
    plt.ylabel('Precio en USD')
    plt.legend()
    plt.grid(True)
    plt.savefig('results/bitcoin_prices_plot_prueba.png')
    logging.info('Gráfico guardado como bitcoin_prices_plot_prueba.png en la carpeta results.')

    print("Script ejecutado con éxito. Verifica los archivos generados en las carpetas 'data' y 'results'.")

except Exception as e:
    logging.error("Error durante la ejecución del script: {}".format(e))
    print("Ocurrió un error: ", e)
