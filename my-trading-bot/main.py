import requests
import pandas as pd
# from alpaca_trade_api import REST

# Configuration
ALPHA_VANTAGE_API_KEY = '3Q292841PDKS6XSN'
ALPACA_API_KEY = 'YOUR_ALPACA_API_KEY'
ALPACA_SECRET_KEY = 'YOUR_ALPACA_SECRET_KEY'
ALPACA_ENDPOINT = 'https://paper-api.alpaca.markets'
SYMBOL = 'BTC'
SMA_PERIOD = 20
SMA_INTERVAL = '60min'
TRADE_QUANTITY = 10

# Initialize Alpaca API
# api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_ENDPOINT, api_version='v2')

def get_sma_prediction(symbol, interval, period, api_key):
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'SMA',
        'symbol': symbol,
        'interval': interval,
        'time_period': period,
        'series_type': 'close',
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    sma_values = data['Technical Analysis: SMA']
    latest_sma = float(list(sma_values.values())[0]['SMA'])
    return latest_sma

# def get_current_price(symbol):
#     barset = api.get_barset(symbol, 'minute', 1)
#     current_price = barset[symbol][0].c
#     return current_price
#
# def place_order(symbol, qty, side):
#     api.submit_order(
#         symbol=symbol,
#         qty=qty,
#         side=side,
#         type='market',
#         time_in_force='gtc'
#     )

def main():
    sma_prediction = get_sma_prediction(SYMBOL, SMA_INTERVAL, SMA_PERIOD, ALPHA_VANTAGE_API_KEY)
#     current_price = get_current_price(SYMBOL)

    print(f"SMA Prediction: {sma_prediction}")
#     print(f"Current Price: {current_price}")

#     if sma_prediction > current_price:
#         print("Placing buy order")
# #         place_order(SYMBOL, TRADE_QUANTITY, 'buy')
#     elif sma_prediction < current_price:
#         print("Placing sell order")
# #         place_order(SYMBOL, TRADE_QUANTITY, 'sell')
#     else:
#         print("No trade signal")

if __name__ == "__main__":
    main()
