import datetime
from calculate_parames import calculate
from get_data import get_candles
import math 

#pip install -r requirements.txt

def calculate_result(candles 
                     ,isWithLoss=True
                     ,stopLossPercent=0.05,rmaPercent=0.01
                     ,isPrint=False):
    
    (rsi,rsi_sma,maShort,maLong) = calculate(candles['c'], rsiSmaPeriod=14)
    isBuy=False
    sum=0
    closeBuyPrice=0
    buyPrice=0
    stopLoss=0


    for i, x in enumerate(rsi):
      if(i>14 and math.isnan( rsi_sma[i-1]) ==False):
        rx = round(x)
        rrsi_sma = round(rsi_sma[i])
        rmaShort = round(maShort[i])
        rmaLong = round(maLong[i])
        c = candles['c'][i]
        #print('shortSubLong',shortSubLong)
  
        if( isBuy == False  and rx>rrsi_sma and rmaShort>rmaLong+(rmaLong*rmaPercent)  ):
            #print(i,rx,rrsi_sma,btcusd_candles['date'][i])
            buyPrice=candles['c'][i]
            isBuy=True
            stopLoss=buyPrice-(buyPrice*stopLossPercent)
            if(isPrint):
                print('buy in ' +str(buyPrice)+f' ({stopLoss})')
            
            #rmaShort<rmaLong 
        elif ( isBuy == True and (rx<rrsi_sma  or (isWithLoss and c<stopLoss))):
            #print(i,rx,rrsi_sma,btcusd_candles['date'][i])
            if(isWithLoss and c<stopLoss):
               if(isPrint):
                print('loss = '+str(stopLoss))
            closeBuyPrice=candles['c'][i]
            diffPrice=closeBuyPrice-buyPrice
            if(isPrint):
                print('close buy in ' +str(closeBuyPrice)+' prifit: '+str(int(diffPrice))+'\n')
            sum+= diffPrice         
            isBuy=False
    return sum

if __name__ == "__main__":
    # Get daily BTC/USD candles
    # Print the DataFrame

    
    # # Generate some example price data
    # np.random.seed(0)
    # price_data = np.random.rand(50) * 10 + 90  # Generate random prices between 90 and 100

    # # Create a pandas DataFrame
    # df = pd.DataFrame(price_data, columns=['Close'])

    # Calculate RSI with a 14-day period
    
    numberOfDay=300
    coin='DIG-USDT'
    duration='4hour'
    candles = get_candles(numberOfDay,coin,duration)
    max=0
    bigx=0
    bigy=0
    for x in range(1, 10):     
        for y in range(1, 10):     
            sum = calculate_result(candles
                                ,isWithLoss=True
                                ,stopLossPercent=x/100,rmaPercent=y/100
                                ,isPrint=False)
                    

            print(f'{x} {y} sum= {int(sum)}')
            if(sum>max):
               max=sum
               bigx=x
               bigy=y

    print(bigx,bigy,max)



     


