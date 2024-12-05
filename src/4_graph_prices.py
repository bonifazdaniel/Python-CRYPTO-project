import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde la carpeta relativa 'data'
df = pd.read_excel('data/bitcoin_prices.xlsx')

# Asegúrate de que la columna de fechas está en formato datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Crear y mostrar el gráfico
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['price'], label='Precio de Bitcoin')
plt.title('Precio de Bitcoin a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Precio en USD')
plt.legend()
plt.grid(True)
plt.show()
