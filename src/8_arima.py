# proporcionará una comprensión amplia del comportamiento del modelo ARIMA con tus datos y su capacidad para predecir futuros valores de la serie temporal
# realizar un análisis ARIMA sobre precios de Bitcoin
# incluyendo la visualización de datos, la verificación de estacionariedad, el ajuste del modelo, las predicciones y la exportación de resultados
# incluye manejo de errores que capturará y mostrará problemas sin cerrar la ventana del script inmediatamente
# incluye un DataFrame que recopila las predicciones junto con sus intervalos de confianza y las guarda en un archivo Excel llamado arima_statsmodels.xlsx

import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import logging

# Configurar la ruta de logs y gráficos
log_path = 'C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\script_log.log'
logging.basicConfig(filename=log_path, level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

try:
    # Configurar el directorio de trabajo
    os.chdir('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project')

    # Mostrar el directorio de trabajo actual para verificar la ruta
    print("Directorio de trabajo actual:", os.getcwd())

    # Cargar el DataFrame desde la carpeta de datos
    file_path = 'data\\bitcoin_prices.xlsx'
    combined_df = pd.read_excel(file_path)
    print(combined_df.head())
    print(combined_df.dtypes)
    logging.info('DataFrame cargado correctamente.')

    # Usar la columna correcta 'price'
    btc_prices = combined_df['price']
    btc_prices.plot(title='Bitcoin Prices Over Time')
    plt.savefig('results\\btc_prices_plot.png')
    logging.info('Gráfico de precios guardado.')

    def check_stationarity(data):
        result = adfuller(data.dropna())
        print('ADF Statistic: %f' % result[0])
        print('p-value: %f' % result[1])
        if result[1] > 0.05:
            print("Series is not stationary")
        else:
            print("Series is stationary")

    check_stationarity(btc_prices)
    logging.info('Chequeo de estacionariedad completado.')

    model = ARIMA(btc_prices, order=(1,1,1))
    fitted_model = model.fit()
    fitted_model.plot_diagnostics(figsize=(15, 12))
    plt.savefig('results\\arima_diagnostics.png')
    logging.info('Diagnósticos del modelo ARIMA guardados.')

    preds = fitted_model.get_forecast(steps=30)
    preds_ci = preds.conf_int()

    ax = btc_prices.plot(label='Observado', figsize=(14, 7))
    preds.predicted_mean.plot(ax=ax, label='Predicciones Futuras')
    ax.fill_between(preds_ci.index, preds_ci.iloc[:, 0], preds_ci.iloc[:, 1], color='k', alpha=.25)
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Precio')
    plt.legend()
    plt.savefig('results\\btc_predictions.png')
    logging.info('Gráfico de predicciones guardado.')

    results_df = pd.DataFrame({
        'Fecha': preds_ci.index,
        'Predicción Media': preds.predicted_mean,
        'Intervalo de Confianza Bajo': preds_ci.iloc[:, 0],
        'Intervalo de Confianza Alto': preds_ci.iloc[:, 1]
    })
    results_df.to_excel('data\\arima_statsmodels.xlsx', index=False)
    print("Archivo 'arima_statsmodels.xlsx' creado con éxito en la carpeta 'data'.")
    logging.info("Archivo Excel creado con éxito en la carpeta 'data'.")

except Exception as e:
    print("Ocurrió un error durante la ejecución del script:", e)
    logging.error("Error: {}".format(e))
