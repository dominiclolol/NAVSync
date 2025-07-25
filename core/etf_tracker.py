import numpy as np
from core.utils import last_price_NAV, last_price_ticker



class ETF_tracker:
    def __init__(self, etf):
        self.etf = etf
        self.etf_ticker = etf.ticker
        self.etf_outstanding_shares = etf.outstanding_shares

        print(f"Setting up ETF_tracker for {self.etf_ticker}...     Remember to update static data!")
        self.etf.compute_shares()
        last_price = last_price_ticker(self.etf_ticker)
        self.etf_price = last_price

        print(f"Computing {self.etf_ticker}s Net Asset Value...")
        self.symbols, self.shares, self.prices, self.nav = last_price_NAV(etf)
        self.all_tickers = self.etf.symbols + [self.etf_ticker]


    def process_update(self, ticker : str, new_price : float):
        """
        Calls update_prices or updates etf_price based on an incoming price update for a ticker.
        """
        if ticker == self.etf_ticker:
            self.etf_price = new_price
        else:
            self.update_prices(ticker, new_price)


    def update_prices(self, ticker : str, new_price : float):
        """
        Update a component's price and recompute NAV (with compute_NAV).
        """
        index = np.where(self.symbols == ticker)[0][0]
        self.prices[index] = new_price
        self.compute_NAV()


    def compute_NAV(self):
        self.nav = (sum(self.shares * self.prices)) / self.etf_outstanding_shares