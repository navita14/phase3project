import alpaca_trade_api as tradeapi
import pandas as pd
from config import ALPACA_CONFIG 

# Alpaca API credentials
API_KEY = ALPACA_CONFIG["API_KEY"]
API_SECRET = ALPACA_CONFIG["SECRET_KEY"]
APCA_API_BASE_URL = ALPACA_CONFIG["ENDPOINT"]

# Initialize Alpaca API client
api = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, api_version='v3')

# Define trading parameters
symbol = 'BTC/USDT'  # The stock symbol to trade
qty = 3  # The number of shares to buy/sell
fast_period = 50  # Fast moving average period
slow_period = 200  # Slow moving average period

# Function to get historical price data
def get_historical_data(symbol, start, end, timeframe, limit=None):
    data = api.get_barset(symbol, timeframe, start=start, end=end, limit=limit).df
    return data[symbol]

# Function to check if a golden cross (fast MA crosses above slow MA) has occurred
def has_golden_cross(data, fast_period, slow_period):
    fast_ma = data['close'].rolling(fast_period).mean()
    slow_ma = data['close'].rolling(slow_period).mean()
    return fast_ma.iloc[-1] > slow_ma.iloc[-1] and fast_ma.iloc[-2] <= slow_ma.iloc[-2]

# Function to place a buy order
def place_buy_order(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='limit',
        time_in_force='gtc',
        limit_price=data['close'].iloc[-1]  # Buy at the current price
    )

# Main trading loop
while True:
    # Get historical price data
    data = get_historical_data(symbol, '2021-01-01', '2023-09-30', '1D', limit=slow_period)

    # Check for a golden cross
    if has_golden_cross(data, fast_period, slow_period):
        print("Golden Cross detected. Plaing buy order.")
        place_buy_order(symbol, qty) 