import yfinance as yf


def get_stock_price(stock_ticker):
    stock = yf.Ticker(stock_ticker)
    stock_info = stock.info
    stock_price = stock_info["currentPrice"]
    return stock_price

#print(get_stock_price("AAPL"))
