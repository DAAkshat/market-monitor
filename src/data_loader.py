import yfinance as yf

def fetch_price_data(tickers,period="6mo",interval="1d"):
    data=yf.download(tickers,period=period,interval=interval)
    return data

def clean_price_data(raw_data):
    raw_data_close= raw_data['Close']
    clean_data= raw_data_close.ffill()
    return clean_data
