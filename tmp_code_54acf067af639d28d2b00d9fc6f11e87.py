import yfinance as yf
from datetime import datetime, timedelta

# Get today's date and calculate one month ago
today = datetime.now()
one_month_ago = today - timedelta(days=30)

# Fetch historical data for NVDA
nvda_hist = yf.Ticker("NVDA").history(start=one_month_ago.strftime("%Y-%m-%d"), end=today.strftime("%Y-%m-%d"))

# Get the current price of NVDA using 'regularMarketPrice' from Ticker() instead of get_info()
nvda_current = yf.Ticker("NVDA").Ticker().__getattr__("regularMarketPrice")

start_date = one_month_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

nvda_prices = nvda_hist['Close']
percentage_change = ((nvda_prices[-1] / nvda_prices[0]) - 1) * 100

print(f"NVIDIA Stock Price Performance: {start_date} to {end_date}")
print(f"Current Stock Price: ${nvda_current:.2f}")
print(f"Percentage Change in Stock Price over the Past Month: {percentage_change:.2f}%")