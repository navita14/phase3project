from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import alpaca_trade_api as tradeapi



# No keys required for crypto data
client = CryptoHistoricalDataClient()

# Creating request object
request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD"],
                        timeframe=TimeFrame.Day,
                        start="2022-09-01",
                        end="2022-09-07"
                        )
# Retrieve daily bars for Bitcoin in a DataFrame and printing it
btc_bars = client.get_crypto_bars(request_params)

# Convert to dataframe
btc_bars.df





class StockMarket:
    def __init__(self, initial_balance, stock_data, stock_prices, portfolio):
        self.balance = initial_balance
        self.stock_data = stock_data
        self.stock_prices = stock_prices
        self.portfolio = portfolio


    def buy(self,quantity):
        pass

    def sell(self,quantity):
        pass


