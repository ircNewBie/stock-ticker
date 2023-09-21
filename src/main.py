from utils.data import Data
from utils.chart import Charts
from utils.tickerutils import Tickers
from utils.config import TickersConf
import pickle


from datetime import date, timedelta
import argparse


data = Data("tiingo")
rawData = dict() 
processedData = dict()

csvFolderPath = "../data/raw"
processedCsvFolderPath = "../data/processed"

tickersAtConfig = TickersConf()
tickerUtils =  Tickers(processedCsvFolderPath)
tickers = tickersAtConfig.get()

def renderChart(ticker):
    charts = Charts()  
    csvFile = f"{csvFolderPath}/{ticker}.csv"
    charts.render(csvFile)
     
def fetchData(nDays = 60):
    # nDays = 60
    startDate = date.today() - timedelta(days=nDays)
    endDate = date.today()

    for ticker in tickers:
        print("fetching " + ticker)
        tickerUrl = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate={startDate}&endDate={endDate}"
        tickerRawData = data.convert2DataFrame(data.fetch(tickerUrl))
        rawData[ticker] = tickerRawData

        # Generate derived dframe (SMAs) 
        processedData[ticker] = data.calcSMA( rawData[ticker], "close", 5 )
        processedData[ticker] = data.calcSMA( rawData[ticker], "close", 20 )

        # Saving raw data frame to csv
        print("Saving raw data ...")
        if data.saveDf2Csv(rawData[ticker], csvFolderPath, ticker + ".csv"):
            print("Success")
        else:
            print("Failed")

        # Saving derived  dframe  to csv
        print("Saving derived data ...")
        if data.saveDf2Csv(rawData[ticker], processedCsvFolderPath, ticker + ".csv"):
            print("Success")
        else:
            print("Failed")

def main():
    parser = argparse.ArgumentParser(description="Command-Line")
    parser.add_argument("--fetch-data", action="store_true", help="Pull market data from api. This should run first and foremost.")
    parser.add_argument("--chart", action="store_true", help="Show / render ticker chart")
    parser.add_argument("--show-bullish", action="store_true", help="Show tickers that are potentially bullish")
    parser.add_argument("--show-bearish", action="store_true", help="Show tickers that are potentially bearish")
    parser.add_argument("--show-tickers", action="store_true", help="Show tickers that are configured")
    parser.add_argument("--add-ticker", action="store_true", help="Add ticker to be configured")
    parser.add_argument("--top-buy", action="store_true", help="Show tickers that are possible to go higher on the next following days")

    args = parser.parse_args()

    if args.top_buy:
        try:
            filePath = './potential-buy.ticker'
            file = open(filePath, 'rb')
            print("Potential Stocks that are possible to go higher on the next following days.")
            potentialBuy = pickle.load(file)
            file.close()

            print(potentialBuy)

        except FileNotFoundError:
            print('Not found! Scanning...')
            tickerUtils._tickerScan()
            file = open(filePath, 'rb')
            potentialBuy = pickle.load(file)
            file.close()
            print(potentialBuy)
        

    if args.show_tickers:
        print("Configured Stock tickers.")
        print(tickerUtils.getTickers())
    
    if args.add_ticker:
        ticker = input("     Ticker Symbol to Add :  ")

        if(ticker.upper()  in tickers):
            print("Ticker already configured")
        else:
            print("Configured Stock tickers.")
            print(tickersAtConfig.addTicker(ticker.upper()))

    if args.show_bullish:
        print("Stocks that are potentially bullish.")
        tickerUtils.showBullish()
    
    if args.show_bearish:
        print("Stocks that are potentially bearish.")
        tickerUtils.showBearish()

    if args.chart:
        ticker = input("     Ticker Symbol :  ")

        if(ticker.upper() not in tickers):
            #    maybe add some immediate fetching 
            print("Ticker not found")
        else:
            renderChart(ticker.upper())

    if args.fetch_data:
        print(" How many days of market price data to fetch?")
        daysOfData = input(" Default is 60 days, maximum of 365 days : _ ")
      
        if daysOfData.isalnum():
            daysOfData = int(daysOfData)
            if(daysOfData > 60 and daysOfData <= 365 ):
                print (f"Overiding the default 60 days. Fetching {daysOfData} days.")
                fetchData(daysOfData)
                return

        print (f"Unable to fetch {daysOfData} days. Fetching  60 days.")
        fetchData()

    print ("Type `python main.py --help` for available options.")

if __name__ == "__main__":
    main()
