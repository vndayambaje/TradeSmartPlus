import yfinance as yf
import pandas as pd
import ta  # Technical Analysis library

def fetch_stock_data(symbols, start_date="2018-01-01"):
    stock_data = {}
    for symbol in symbols:
        data = yf.download(symbol, start=start_date)
        
        # Calculate technical indicators
        data['SMA_20'] = data['Close'].rolling(window=20).mean()
        data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=14).rsi()
        data['Bollinger_Upper'], data['Bollinger_Lower'] = ta.volatility.BollingerBands(data['Close']).bollinger_hband(), ta.volatility.BollingerBands(data['Close']).bollinger_lband()
        
        stock_data[symbol] = data.dropna()
    return stock_data

