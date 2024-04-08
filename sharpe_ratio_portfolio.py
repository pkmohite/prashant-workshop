import yfinance as yf
import pandas as pd
import numpy as np

def calculate_portfolio_sharpe_ratio(tickers, shares, start_date, end_date, risk_free_rate=0.01):
    """
    Calculates the Sharpe ratio of a portfolio.

    Args:
        tickers (list): List of ETF ticker symbols.
        shares (list): List of the number of shares owned for each ETF.
        start_date (str): Start date for historical data in 'YYYY-MM-DD' format.
        end_date (str): End date for historical data in 'YYYY-MM-DD' format.
        risk_free_rate (float, optional): Annual risk-free rate. Defaults to 0.01 (1%).

    Returns:
        float: The Sharpe ratio of the portfolio.
    """

    # Download historical prices 
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

    # Calculate daily returns
    returns = data.pct_change().dropna()

    # Calculate portfolio weights
    total_value = returns * shares * data 
    portfolio_value = total_value.sum(axis=1)
    weights = total_value.div(portfolio_value, axis=0)

    # Calculate portfolio returns
    portfolio_returns = (weights * returns).sum(axis=1)

    # Calculate expected portfolio return
    expected_portfolio_return = portfolio_returns.mean()

    # Calculate portfolio standard deviation (volatility)
    portfolio_std_dev = portfolio_returns.std()

    # Calculate Sharpe ratio
    sharpe_ratio = (expected_portfolio_return - risk_free_rate) / portfolio_std_dev

    # Annualize the Sharpe ratio (assuming 252 trading days)
    annualized_sharpe_ratio = sharpe_ratio * np.sqrt(252)

    return annualized_sharpe_ratio



# # Example usage
# tickers = ['SPY', 'QQQ', 'VTI']  # Popular ETFs
# shares = [30, 30, 30]
# start_date = '2023-03-13'
# end_date = '2024-03-18'  

# portfolio_sharpe_ratio = calculate_portfolio_sharpe_ratio(tickers, shares, start_date, end_date)
# print("Portfolio Sharpe Ratio:", portfolio_sharpe_ratio) 

# Calculate 5 year from 3/18 sharpe ratio for VQNPX
ticker = 'VTI'
start_date = '2019-03-18'
end_date = '2024-03-18'
sharpe_ratio = calculate_sharpe_ratio(ticker, start_date, end_date)
print("Sharpe Ratio:", sharpe_ratio)  # 5 year sharpe ratio for VQNPX