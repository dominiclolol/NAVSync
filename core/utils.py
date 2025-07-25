import numpy as np
import yfinance as yf



def last_price_NAV(etf: object) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """
    Returns component symbols, shares, latest traded prices, and Net Asset Value (approximated as total_market_value / outstanding_shares) for the given ETF.
    """
    symbols = np.array(etf.symbols)
    shares = np.array(etf.shares)
    def last_price(s): return yf.Ticker(s).fast_info['lastPrice']
    prices = np.fromiter((last_price(s) for s in etf.symbols), dtype=np.float64)
    nav = etf.total_market_value / etf.outstanding_shares
    return symbols, shares, prices, nav



def last_price_ticker(ticker: str) -> float:
    """
    Fetches the latest (traded) price of a single ticker from yfinance.
    """
    return yf.Ticker(ticker).fast_info['lastPrice']
