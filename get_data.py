import requests
import pandas as pd

import datetime
import time

def get_daily_btcusd_candles(numOfDay=100):
    ms = datetime.datetime.now()
    startms = ms+ datetime.timedelta(days=-1*numOfDay)
     
    startAt= int(time.mktime(startms.timetuple()))
    endAt=int(time.mktime(ms.timetuple()))

    url = f"https://api.kucoin.com/api/v1/market/candles?type=1day&symbol=BTC-USDT&startAt={startAt}&endAt={endAt}"
     

    response = requests.get(url )
    data = response.json()

    
    # Extract timestamps and prices

    prices = data['data']
    prices.reverse()


    # Create a DataFrame
    df = pd.DataFrame(prices )
    df.columns = ["date","o","c","h","l","v","vw"]

    # Convert timestamps to datetime
    df["date"] = pd.to_datetime(df["date"], unit='s', origin='unix')
    df["o"] = pd.to_numeric(df["o"])
    df["h"] = pd.to_numeric(df["h"])
    df["l"] = pd.to_numeric(df["l"])
    df["c"] = pd.to_numeric(df["c"])
    
    df.drop(index=df.index[-1],axis=0,inplace=True)

    return df
if __name__ == "__main__":
    # Get daily BTC/USD candles
    btcusd_candles = get_daily_btcusd_candles()
    # Print the DataFrame
    print(btcusd_candles)

