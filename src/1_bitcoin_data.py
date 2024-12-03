from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# Obtén datos históricos de precios para Bitcoin
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days='30')
print(bitcoin_data)

input("Presione Enter para continuar...")