import warnings
import requests
import pandas as pd

import datetime
import time

def get_candles(numOfDayStart=100,coin='BTC-USDT',duration='1day',numOfDayEnd=1):
    today= datetime.datetime.now()
    end=today

    if(numOfDayEnd>1):
        end=  today + datetime.timedelta(days=-1*numOfDayEnd)

    start = today + datetime.timedelta(days=-1*numOfDayStart)

    startAt= int(time.mktime(start.timetuple()))
    endAt=int(time.mktime(end.timetuple()))

    url = f"https://api.kucoin.com/api/v1/market/candles?type={duration}&symbol={coin}&startAt={startAt}&endAt={endAt}"
     

    try:
        response = requests.get(url )
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    data = response.json()

    
    # Extract timestamps and prices

    prices = data['data']
    prices.reverse()


    # Create a DataFrame
    df = pd.DataFrame(prices )
    df.columns = ["date","o","c","h","l","v","vw"]

    # Convert timestamps to datetime
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        df["date"] = pd.to_datetime(df["date"], unit='s', origin='unix')
    df["o"] = pd.to_numeric(df["o"])
    df["h"] = pd.to_numeric(df["h"])
    df["l"] = pd.to_numeric(df["l"])
    df["c"] = pd.to_numeric(df["c"])
    
    #df.drop(index=df.index[-1],axis=0,inplace=True)

    return df

if __name__ == "__main__":
    # Get daily BTC/USD candles
    btcusd_candles = get_candles(numOfDayStart=10,coin='BTC-USDT',duration='1day',numOfDayEnd=5)
    # Print the DataFrame
    print(btcusd_candles)

