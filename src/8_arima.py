# proporcionará una comprensión amplia del comportamiento del modelo ARIMA con tus datos y su capacidad para predecir futuros valores de la serie temporal
# realizar un análisis ARIMA sobre precios de Bitcoin
# incluyendo la visualización de datos, la verificación de estacionariedad, el ajuste del modelo, las predicciones y la exportación de resultados
# incluye manejo de errores que capturará y mostrará problemas sin cerrar la ventana del script inmediatamente
# incluye un DataFrame que recopila las predicciones junto con sus intervalos de confianza y las guarda en un archivo Excel llamado arima_statsmodels.xlsx

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import logging

# Configurar logs para registrar errores
logging.basicConfig(filename='data/script_log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

try:
    # Cargar el archivo desde la carpeta relativa 'data'
    combined_df = pd.read_excel('data/bitcoin_prices.xlsx')
    logging.info('Archivo cargado correctamente.')
    
    # Verificar los primeros datos
    print(combined_df.head())
    btc_prices = combined_df['price']

    # Verificar estacionariedad
    def check_stationarity(data):
        result = adfuller(data.dropna())
        print('ADF Statistic:', result[0])
        print('p-value:', result[1])
        if result[1] > 0.05:
            print("La serie no es estacionaria")
        else:
            print("La serie es estacionaria")

    check_stationarity(btc_prices)
    logging.info('Chequeo de estacionariedad completado.')

    # Ajustar modelo ARIMA
    model = ARIMA(btc_prices, order=(1, 1, 1))
    fitted_model = model.fit()
    logging.info('Modelo ARIMA ajustado con éxito.')

    # Diagnóstico del modelo
    fitted_model.plot_diagnostics(figsize=(10, 8))
    plt.savefig('results/arima_diagnostics.png')
    logging.info('Diagnósticos del modelo ARIMA guardados.')

    # Predicciones
    forecast = fitted_model.get_forecast(steps=30)
    forecast_ci = forecast.conf_int()

    # Gráfico de predicciones
    ax = btc_prices.plot(label='Observado', figsize=(10, 6))
    forecast.predicted_mean.plot(ax=ax, label='Predicción')
    ax.fill_between(forecast_ci.index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='gray', alpha=0.3)
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Precio')
    plt.legend()
    plt.savefig('results/btc_predictions.png')
    logging.info('Gráfico de predicciones guardado.')

    # Guardar predicciones en Excel
    results_df = pd.DataFrame({
        'Fecha': forecast_ci.index,
        'Predicción Media': forecast.predicted_mean,
        'Intervalo Bajo': forecast_ci.iloc[:, 0],
        'Intervalo Alto': forecast_ci.iloc[:, 1]
    })
    results_df.to_excel('data/arima_statsmodels.xlsx', index=False)
    logging.info('Archivo Excel de predicciones creado con éxito.')

except Exception as e:
    logging.error("Error durante la ejecución del script: {}".format(e))
    print("Ocurrió un error: ", e)
