import finnhub
import pandas as pd

# Initialize client
finnhub_client = finnhub.Client(api_key="cse3n61r01qs1ihofdr0cse3n61r01qs1ihofdrg")

# Get US stock symbols and save to CSV
symbols = finnhub_client.stock_symbols('US')
pd.DataFrame(symbols).to_csv('us_stock_symbols.csv', index=False)



import yfinance as yf
import pandas as pd
import numpy as np
import time
import logging

logging.basicConfig(level=logging.INFO)

# Load symbols and set up batching
us_stock_df = pd.read_csv('us_stock_symbols.csv')
symbols = [str(symbol) for symbol in us_stock_df['symbol'].dropna().tolist() if symbol]
start_date = "2024-01-01"
end_date = "2024-01-31"
batch_size = 50

all_stock_data = pd.DataFrame()

for i in range(0, len(symbols), batch_size):
    batch_symbols = symbols[i:i + batch_size]
    logging.info(f"Starting batch {i//batch_size + 1} for {len(batch_symbols)} symbols.")
    try:
        # Download batch
        batch_data = yf.download(batch_symbols, start=start_date, end=end_date, group_by='ticker', threads=True)
        
        # Process each symbol in the batch
        for symbol in batch_symbols:
            if symbol in batch_data:
                stock_data = batch_data[symbol].copy()
                stock_data.reset_index(inplace=True)
                stock_data['Symbol'] = symbol
                stock_data['LogReturn'] = np.log(stock_data['Close'] / stock_data['Close'].shift(1))
                all_stock_data = pd.concat([all_stock_data, stock_data[['Symbol', 'Date', 'Close', 'LogReturn']]])
                
                # Calculate and log progress
                progress = (len(all_stock_data['Symbol'].unique()) / len(symbols)) * 100
                logging.info(f"Progress: {progress:.2f}% complete.")

    except Exception as e:
        logging.error(f"Failed to download batch {batch_symbols}: {e}")
        continue  # Skip to the next batch on failure
    
    # Optional: Delay to reduce rate limit risk
    time.sleep(5)

# Save the final results to CSV
all_stock_data.to_csv('daily_log_returns_yfinance.csv', index=False)

import pandas as pd

# Assuming `all_stock_data` contains columns ['Symbol', 'Date', 'LogReturn']
# Calculate summary statistics for each stock

# Step 1: Group by stock symbol and calculate summary statistics
aggregated_stats = all_stock_data.groupby('Symbol')['LogReturn'].agg(
    MeanLogReturn='mean', 
    StdLogReturn='std', 
    MinLogReturn='min', 
    MaxLogReturn='max'
).reset_index()

# Now `aggregated_stats` contains one row per stock with summary statistics
print("Aggregated Data:")
print(aggregated_stats.head())

# Save this aggregated dataset for easy access later
aggregated_stats.to_csv('aggregated_log_returns_summary.csv', index=False)

#commit note


