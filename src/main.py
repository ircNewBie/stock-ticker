from utils.data import Data
from dotmap import DotMap

tickers = [
    "TSLA",  # TESLA
    "NVDA",  # NVIDIA CORP
    "AVGO",  # Broadcom
    "AMD",  # ADVANCED MICRO DEVICES INC
    "BABA"  # ALIBABA GROUP HOLDING LTD
]

if __name__ == "__main__":
    url = "https://api.tiingo.com/tiingo/daily/TSLA/prices"
    data = Data("tiingo")

    for ticker in tickers:
        tickerUrl = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
        # print(tickerUrl)
        rawData = data.fetch(tickerUrl)
        tickerData = DotMap(rawData)
        print(ticker, ":", tickerData.date, " ", tickerData.close)

    # print(rawData.close)
