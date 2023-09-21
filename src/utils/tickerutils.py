import pandas as pd
from .config import TickersConf


class Tickers:
    def __init__(self, dataSourcePath: str ):
        self.dataSourcePath = dataSourcePath
        self.bullishStocks = {}
        self.bearishStocks = {}
        self.tickers = TickersConf().get()

    def potentialBuy(self):
        '''
        Rule: when on uptrend i.e. fast SMA  > slow SMA:
             + When price closes at around slow-SMA
                **  there is a probability bias towards price pull-back  on
                    this dynamic support levels
                **  We can add some confirmation indicator here
                    but for this project, there is none yet.
        '''

    def getTickers(self):
        print("Tickers configured")
        for ticker in self.tickers:
            print(ticker)
        
        return self.tickers

    def showBullish(self):
        print("Potentially Bullish Stocks: ")
        self._tickerScan()
        for bullish in self.bullishStocks:
            print (bullish) 
        # print(self.bullishStocks)

    def showBearish(self):
        print("Potentially Bearish Stocks: ")
        self._tickerScan()
        for bearish in self.bearishStocks:
            print (bearish) 
        # print(self.bearishStocks)


    def _setSmaData(self, df, period: int = 20):
        return pd.DataFrame({
            'time': df['date'],
            f'{period}-SMA': df['close'].rolling(window=period).mean()
        }).dropna()

    
    def _tickerScan(self):
        print("Scanning tickers")

        for ticker in self.tickers:
            csvFile = self.dataSourcePath +"/" + ticker + ".csv"
            df = pd.read_csv(csvFile)
            
            dayAgoPrice = df.tail(1)

            fastSMA = dayAgoPrice["5DaySMA"].values[0]
            slowSMA = dayAgoPrice["20DaySMA"].values[0]

            if(fastSMA > slowSMA): 
                self.bullishStocks[ticker] = dayAgoPrice

            if(fastSMA < slowSMA): 
                self.bearishStocks[ticker] = dayAgoPrice
            

   
       

        
  






    