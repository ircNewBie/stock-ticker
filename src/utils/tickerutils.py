import pandas as pd
import pickle
from .config import TickersConf


class Tickers:
    def __init__(self, dataSourcePath: str ):
        self.dataSourcePath = dataSourcePath
        self.bullishStocks = {}
        self.bearishStocks = {}
        self.potentialBuy = []
        self.tickers = TickersConf().get()

    def _potentialBuy(self, slowSMA: int ,  priceData )->bool: 
        '''
        Rule: when on uptrend i.e. fast SMA  > slow SMA:
             + When price closes at around slow-SMA
                **  there is a probability bias that price may bounce / pull-back  on
                    this dynamic support levels
        '''
        closePrice = priceData["close"].values[0]
        return closePrice <= slowSMA


    def getTickers(self):
        return self.tickers

    def showBullish(self):
        print("Potentially Bullish Stocks: ")
        self._tickerScan()
        for ticker in self.bullishStocks:
            print (ticker) 

    def showBearish(self):
        print("Potentially Bearish Stocks: ")
        self._tickerScan()
        for ticker in self.bearishStocks:
            print (ticker) 


    def _setSmaData(self, df, period: int = 20):
        return pd.DataFrame({
            'time': df['date'],
            f'{period}-SMA': df['close'].rolling(window=period).mean()
        }).dropna()

    
    def _tickerScan(self):

        # Scanning Tickers 
        for ticker in self.tickers:
            csvFile = self.dataSourcePath +"/" + ticker + ".csv"
            try:
                df = pd.read_csv(csvFile)
            except FileNotFoundError:
                print(f"The file '{csvFile}' does not exist.")
                print("Make sure `--fetch-data` have been executed first. ")
                return
            
            dayAgoPrice = df.tail(1)

            fastSMA = dayAgoPrice["5DaySMA"].values[0]
            slowSMA = dayAgoPrice["20DaySMA"].values[0]

            if(fastSMA > slowSMA): 
                self.bullishStocks[ticker] = dayAgoPrice

                if (self._potentialBuy(slowSMA, dayAgoPrice)):
                    self.potentialBuy.append(ticker)
                    
            if(fastSMA < slowSMA): 
                self.bearishStocks[ticker] = dayAgoPrice
            
        # Dumping self.potentialBuy variable to file
        file = open('potential-buy.ticker', 'wb')
        pickle.dump(self.potentialBuy, file)
        file.close()


            

   
       

        
  






    