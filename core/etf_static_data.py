#Since this data is static, it needs to be manually updated
#ETFs included: QQQ, the script will support custom ETFs if you add the required info
import yfinance as yf



class ETF:
    def __init__(self, ticker, weighted_holdings, outstanding_shares, total_market_value, expense_ratio):
        self.ticker = ticker
        self.weighted_holdings = weighted_holdings
        self.symbols = list(weighted_holdings.keys())
        self.shares = []
        self.outstanding_shares = outstanding_shares
        self.total_market_value = total_market_value
        self.expense_ratio = expense_ratio

    def compute_shares(self):
        """
        Computes the number of shares held for each holding in the ETF, and updates self.shares accordingly.

        Uses latest traded prices from yfinance to calculate the number of shares for each component based on its weight in the ETF and the total market value.
        """
        self.shares = []
        for i in range(len(self.symbols)):
            last_price = yf.Ticker(self.symbols[i]).fast_info['lastPrice']
            shares_held = ((self.weighted_holdings[self.symbols[i]] / 100 ) * self.total_market_value) / last_price
            self.shares.append(shares_held)



#QQQ (Up to date information on holdings available at: https://www.invesco.com/qqq-etf/en/about.html)
#Last updated June 2025
QQQ_weighted_holdings = {
    'NVDA': 9.26,
    'MSFT': 8.75,
    'AAPL': 7.44,
    'AMZN': 5.52,
    'AVGO': 5.01,
    'META': 3.71,
    'NFLX': 3.17,
    'TSLA': 2.57,
    'COST': 2.55,
    'GOOGL': 2.41,
    'GOOG': 2.27,
    'PLTR': 1.84,
    'CSCO': 1.58,
    'TMUS': 1.56,
    'AMD': 1.3,
    'LIN': 1.29,
    'INTU': 1.27,
    'TXN': 1.15,
    'ISRG': 1.1,
    'BKNG': 1.08,
    'PEP': 1.08,
    'QCOM': 1.02,
    'ADBE': 0.95,
    'AMGN': 0.93,
    'AMAT': 0.91,
    'HON': 0.9,
    'GILD': 0.81,
    'MU': 0.81,
    'SHOP': 0.8,
    'PANW': 0.79,
    'CMCSA': 0.78,
    'LRCX': 0.75,
    'CRWD': 0.74,
    'MELI': 0.73,
    'ADP': 0.73,
    'KLAC': 0.71,
    'ADI': 0.71,
    'VRTX': 0.7,
    'SBUX': 0.63,
    'APP': 0.62,
    'INTC': 0.6,
    'MSTR': 0.59,
    'CEG': 0.57,
    'DASH': 0.56,
    'MDLZ': 0.52,
    'CDNS': 0.52,
    'CTAS': 0.51,
    'SNPS': 0.5,
    'FTNT': 0.48,
    'ORLY': 0.46,
    'MAR': 0.45,
    'PYPL': 0.43,
    'PDD': 0.41,
    'ASML': 0.41,
    'CSX': 0.37,
    'MRVL': 0.36,
    'ADSK': 0.36,
    'AXON': 0.36,
    'MNST': 0.35,
    'ROP': 0.35,
    'ABNB': 0.35,
    'CHTR': 0.34,
    'REGN': 0.34,
    'NXPI': 0.34,
    'AEP': 0.32,
    'PAYX': 0.3,
    'PCAR': 0.3,
    'WDAY': 0.3,
    'FAST': 0.29,
    'ZS': 0.28,
    'CPRT': 0.27,
    'KDP': 0.27,
    'DDOG': 0.27,
    'TTWO': 0.26,
    'CCEP': 0.26,
    'IDXX': 0.25,
    'EXC': 0.25,
    'VRSK': 0.25,
    'ROST': 0.25,
    'FANG': 0.25,
    'AZN': 0.24,
    'MCHP': 0.23,
    'CTSH': 0.23,
    'BKR': 0.23,
    'XEL': 0.23,
    'EA': 0.22,
    'ODFL': 0.21,
    'TEAM': 0.21,
    'CSGP': 0.2,
    'GEHC': 0.2,
    'DXCM': 0.19,
    'TTD': 0.19,
    'ANSS': 0.19,
    'KHC': 0.18,
    'LULU': 0.16,
    'WBD': 0.16,
    'CDW': 0.14,
    'ON': 0.14,
    'GFS': 0.13,
    'ARM': 0.12,
    'BIIB': 0.11,
    }
QQQ_total_market_value = 356.34 * 1e9 #Approximate Total Net Assets as Total Market Value (Invesco does not provide a Total Net Assets figure)
QQQ_outstanding_shares = 640.45 * 1e6
QQQ_expense_ratio = 0.002

QQQ = ETF('QQQ', QQQ_weighted_holdings, QQQ_outstanding_shares, QQQ_total_market_value, QQQ_expense_ratio)



#Custom ETFs should be included here as well!
etf_dict = {'QQQ': QQQ}