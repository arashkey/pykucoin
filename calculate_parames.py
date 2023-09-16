import pandas_ta as pta


def calculate(data, rsiSmaPeriod=14,preiodMaShort=9,preiodMaLong=21):
    """
    Returns a pd.Series with the relative strength index.
    """
    rsi = pta.rsi(data, length = rsiSmaPeriod)
    rsi_sma = rsi.rolling(window=rsiSmaPeriod).mean()
    maShort =  pta.ma("sma",data, length = preiodMaShort)
    maLong =  pta.ma("sma",data, length = preiodMaLong)

    return (rsi,rsi_sma,maShort,maLong)
 

if __name__ == "__main__":
    from get_data import get_candles

    # Get daily BTC/USD candles
    btcusd_candles = get_candles()
    # Print the DataFrame
    #print(btcusd_candles)
    
    # # Generate some example price data
    # np.random.seed(0)
    # price_data = np.random.rand(50) * 10 + 90  # Generate random prices between 90 and 100

    # # Create a pandas DataFrame
    # df = pd.DataFrame(price_data, columns=['Close'])

    # Calculate RSI with a 14-day period
    (rsi,rsi_sma,maShort,maLong) = calculate(btcusd_candles['c'] )
    

    #print(rsi,rsi_sma)
    print(maShort,maLong)
