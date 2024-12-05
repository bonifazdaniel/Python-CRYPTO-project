import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde la carpeta relativa 'data'
df = pd.read_excel('data/bitcoin_prices.xlsx')

# Asegúrate de que la columna de fechas está en formato datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Visualización simple (opcional)
plt.plot(df['timestamp'], df['price'])
plt.title('Bitcoin Prices Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Price (USD)')
plt.show()
