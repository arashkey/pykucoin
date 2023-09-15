import requests
import pandas as pd

def get_daily_btcusd_candles():
    url = "https://api.kucoin.com/api/v1/market/candles?type=1day&symbol=BTC-USDT"
     

    response = requests.get(url )
    data = response.json()


    # Extract timestamps and prices

    prices = data['data']
    print(prices[0])

    # Create a DataFrame
    df = pd.DataFrame(prices )
    df.columns = ["date","o","c","h","l","v","vw"]

    # Convert timestamps to datetime
    df["date"] = pd.to_datetime(df["date"], unit='s', origin='unix')

    return df
if __name__ == "__main__":
    # Get daily BTC/USD candles
    btcusd_candles = get_daily_btcusd_candles()
    # Print the DataFrame
    print(btcusd_candles)

