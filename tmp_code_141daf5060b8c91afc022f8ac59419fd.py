import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Define start and end dates
start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

# Fetch historical price data for NVDA
data = yf.download('NVDA', start=start_date, end=end_date)

# Ensure the data is sorted by date
data.sort_index(inplace=True)

print(data)