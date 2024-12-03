# Este script calcula la volatilidad basada en los retornos diarios y la anualiza (multiplicando por la raíz cuadrada de 252,
# que es el número aproximado de días de trading en un año)
# crea un archivo de excel

import pandas as pd

# Cargar los datos desde la carpeta especificada
df = pd.read_excel('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\bitcoin_prices.xlsx')
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Calcular los retornos diarios
df['daily_returns'] = df['price'].pct_change()

# Calcular la volatilidad (desviación estándar de los retornos diarios)
volatility = df['daily_returns'].std() * (252**0.5)  # Anualizar la volatilidad si es necesario

# Crear un DataFrame con la volatilidad
volatility_df = pd.DataFrame({
    'Estadística': ['Volatilidad Anualizada'],
    'Valor': [volatility]
})

# Guardar el DataFrame en un archivo Excel en la carpeta de datos
volatility_df.to_excel('C:\\Users\\bonif\\OneDrive\\Documentos\\Python CRYPTO project\\data\\volatilidad.xlsx', index=False)

print("Archivo 'volatilidad.xlsx' creado con éxito en la carpeta 'data'. Contiene la siguiente estadística:")
print(volatility_df)

input("Presione Enter para cerrar")
