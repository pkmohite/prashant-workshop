import pandas as pd
import yfinance as yf

# Define the stock symbol and time period
stock_symbol = "SPY"
start_date = "2019-03-18"
end_date = "2024-03-18"

# Fetch the historical stock data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate the daily returns
stock_data["Daily Returns"] = stock_data["Close"].pct_change()

# Calculate the annualized mean return and standard deviation
mean_return = stock_data["Daily Returns"].mean() * 252
std_deviation = stock_data["Daily Returns"].std() * (252 ** 0.5)

# Set the risk-free rate (e.g., 0.05 for 5%)
risk_free_rate = 0.05

# Calculate the Sharpe ratio
sharpe_ratio = (mean_return - risk_free_rate) / std_deviation

# Print the Sharpe ratio
print("Sharpe Ratio:", sharpe_ratio)