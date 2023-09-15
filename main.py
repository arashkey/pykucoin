#pip install -r requirements.txt
from get_data import get_daily_btcusd_candles


if __name__ == "__main__":
    # Get daily BTC/USD candles
    btcusd_candles = get_daily_btcusd_candles()
    # Print the DataFrame
    print(btcusd_candles)
    
    # # Generate some example price data
    # np.random.seed(0)
    # price_data = np.random.rand(50) * 10 + 90  # Generate random prices between 90 and 100

    # # Create a pandas DataFrame
    # df = pd.DataFrame(price_data, columns=['Close'])

    # Calculate RSI with a 14-day period
    (rsi,rsi_sma) = calculate_rsi_sum(btcusd_candles['c'], period=14)
    

    print(rsi,rsi_sma)