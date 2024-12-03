# script para identificar exactamente dónde se produce el fallo. Comienza solo con la carga de datos y una visualización simple

import pandas as pd
import matplotlib.pyplot as plt

# Crea un DataFrame simple para prueba
data = {'btc_price': [1, 2, 3, 4, 5]}
btc_prices = pd.DataFrame(data)

# Intenta visualizar
btc_prices.plot(title='Test Plot')
plt.show()

input("Presione Enter para ver si esto funciona...")
