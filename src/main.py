from utils.data import Data
from datetime import date, timedelta
import argparse


data = Data("tiingo")
rawData = dict() 
processedData = dict()

tickers = [
    "TSLA",  # TESLA
    "NVDA",  # NVIDIA CORP
    "AVGO",  # Broadcom
    "AMD",   # ADVANCED MICRO DEVICES INC
    "BABA"   # ALIBABA GROUP HOLDING LTD
]


csvFolderPath = "../data/raw"
processedCsvFolderPath = "../data/processed"

def fetchData():
    nDays = 60
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

        print(processedData[ticker])
        # Saving raw data frame to csv
        print("Saving raw data ...")
        if data.saveDf2Csv(rawData[ticker], csvFolderPath, ticker + ".csv"):
            print("Success")
        else:
            print("Failed")

         # Saving derived / processed  dframe  to csv
        print("Saving derived data ...")
        if data.saveDf2Csv(rawData[ticker], processedCsvFolderPath, ticker + ".csv"):
            print("Success")
        else:
            print("Failed")

def main():
    parser = argparse.ArgumentParser(description="Command-Line options")
    parser.add_argument("--fetch-data", action="store_true", help="Pull market data from api.")
    parser.add_argument("--csv-path", action="store_true", help="Show full file path location of CSV files.")

    args = parser.parse_args()

    if args.fetch_data:
        fetchData()
    
    if args.csv_path:
        print ("Raw CSV files are saved in " +csvFolderPath)
        print ("Processed CSV files are saved in " +processedCsvFolderPath)


    

if __name__ == "__main__":
    main()
