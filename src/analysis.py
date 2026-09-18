import numpy as np
def calculate_volatility(close_prices,window=20, trading_days=252):
    daily_returns=close_prices.pct_change()
    rolling_vol_20d=daily_returns.rolling(window=window).std()
    annualized_vol_20d=rolling_vol_20d*(trading_days**0.5)
    return annualized_vol_20d

def calculate_sector_ranking(close_prices, sector_map,window=20):
    returns_n = close_prices.pct_change(periods=window)
    latest= returns_n.tail(1).T
    latest.columns= ["returns_n"]
    latest["sector"]=latest.index.map(sector_map)
    ranking=latest.dropna(subset="sector")
    ranking=ranking.sort_values("returns_n",ascending=False)
    return ranking

def calculate_correlation(close_prices):
    daily_returns=close_prices.pct_change()
    correlation=daily_returns.corr()
    return correlation

def classify_regime(vix_level):
    if vix_level < 15:
        return "Calm"
    elif vix_level < 25:
        return "Normal"
    else:
        return "Volatile"