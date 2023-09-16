from calculate_parames import calculate
from get_data import get_daily_btcusd_candles
import math 

#pip install -r requirements.txt

if __name__ == "__main__":
    # Get daily BTC/USD candles
    btcusd_candles = get_daily_btcusd_candles(365)
    # Print the DataFrame

    
    # # Generate some example price data
    # np.random.seed(0)
    # price_data = np.random.rand(50) * 10 + 90  # Generate random prices between 90 and 100

    # # Create a pandas DataFrame
    # df = pd.DataFrame(price_data, columns=['Close'])

    # Calculate RSI with a 14-day period
    (rsi,rsi_sma,maShort,maLong) = calculate(btcusd_candles['c'], rsiSmaPeriod=14)
    isBuy=False
    sum=0
    closeBuyPrice=0
    buyPrice=0
    lossPercent=0.05
    isWithLoss=True
    stopLoss=0
    shortSubLong=0
    isCheck=False
    for i, x in enumerate(rsi):
      if(i>14 and math.isnan( rsi_sma[i-1]) ==False):
        rx = round(x)
        rrsi_sma = round(rsi_sma[i])
        rmaShort = round(maShort[i])
        rmaLong = round(maLong[i])
        c = btcusd_candles['c'][i]
        shortSubLong = rmaShort-rmaLong
        #print('shortSubLong',shortSubLong)
  
        if( isBuy == False  and rx>rrsi_sma and rmaShort>rmaLong+(rmaLong*0.01)  ):
            print(i,rx,rrsi_sma,btcusd_candles['date'][i])
            buyPrice=btcusd_candles['c'][i]
            isBuy=True
            stopLoss=buyPrice-(buyPrice*lossPercent)
            print('buy in ' +str(buyPrice)+f' ({stopLoss})')
            
            #rmaShort<rmaLong 
        elif ( isBuy == True and (rx<rrsi_sma  or (isWithLoss and c<stopLoss))):
            print(i,rx,rrsi_sma,btcusd_candles['date'][i])
            if(isWithLoss and c<stopLoss):
               print('loss = '+str(stopLoss))
            closeBuyPrice=btcusd_candles['c'][i]
            diffPrice=closeBuyPrice-buyPrice
            print('close buy in ' +str(closeBuyPrice)+' prifit: '+str(int(diffPrice))+'\n')
            sum+= diffPrice         
            isBuy=False
            

    print('sum= ',str(int(sum)))



     


