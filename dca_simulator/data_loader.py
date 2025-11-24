import pandas as pd
import yfinance as yf

def load_price_data(ticker: str, start_date: str, end_date: str):
    """Download daily adj. close prices for a stock"""

    df = yf.download(ticker, start=start_date, end=end_date)
    return df[["Adj Close"]]