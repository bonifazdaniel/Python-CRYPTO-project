import pandas as pd

# Cargar los datos desde la ruta específica en la carpeta de datos
df = pd.read_excel('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\bitcoin_prices.xlsx')
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Calcular estadísticas descriptivas
mean_price = df['price'].mean()
median_price = df['price'].median()
std_deviation = df['price'].std()
quantiles = df['price'].quantile([0.25, 0.5, 0.75])

# Crear un DataFrame con las estadísticas
stats_df = pd.DataFrame({
    'Estadística': ['Media', 'Mediana', 'Desviación Estándar', 'Primer Cuartil', 'Mediana (Q2)', 'Tercer Cuartil'],
    'Valor': [mean_price, median_price, std_deviation, quantiles[0.25], quantiles[0.50], quantiles[0.75]]
})

# Guardar el DataFrame en un archivo Excel en la carpeta de datos
stats_df.to_excel('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\media_mediana.xlsx', index=False)

print("Archivo 'media_mediana.xlsx' creado con éxito en la carpeta 'data'. Contiene las siguientes estadísticas:")
print(stats_df)

input("Presione Enter para continuar...")
