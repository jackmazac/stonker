##CURRENT STOCK SHOULD BE STORED IN PLAYER CLASS##
import yfinance as yf

'''
This method gets the current information of a stock 
Parameters: 
- stock_ticker: The stock ticker you are looking to use 
Returns: 
- stock_price: The price of the stock 
'''
def get_stock_price(stock_ticker):
    stock = yf.Ticker(stock_ticker)
    stock_info = stock.info
    stock_price = stock_info["currentPrice"]
    return stock_price

#print(get_stock_price("AAPL"))
