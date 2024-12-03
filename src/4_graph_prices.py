import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos desde la carpeta de datos especificada
df = pd.read_excel('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\bitcoin_prices.xlsx')
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['price'], label='Precio de Bitcoin')
plt.title('Precio de Bitcoin a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Precio en USD')
plt.legend()
plt.grid(True)
plt.show()
