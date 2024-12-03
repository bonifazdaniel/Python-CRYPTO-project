import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde la ruta correcta
df = pd.read_excel('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\bitcoin_prices.xlsx')

# Asegúrate de que la columna de fechas está en formato datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Puedes añadir aquí cualquier análisis adicional o visualización que necesites
