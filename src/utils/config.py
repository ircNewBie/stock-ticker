from dotmap import DotMap
import pickle
import json

tickers = [
    "TSLA",  # TESLA
    "NVDA",  # NVIDIA CORP
    "AVGO",  # Broadcom
    "MSFT",  # Microsoft
    "AMZN",  # Amazo
    # "ORCL",  # Oraclen
    # "GOOG",  # Google
    # "META",  # Facebook
    # "AMD",   # ADVANCED MICRO DEVICES INC
    # "BABA"   # ALIBABA GROUP HOLDING LTD
]

class Config:
    def __init__(self, config_file_path):
        self.config = self._load_config(config_file_path)

    def _load_config(self, config_file_path):
        with open(config_file_path, "r") as file:
            config_data = json.load(file)
        return DotMap(config_data)

    def getApiKey(self, key):
        keys = self.config.apiKey.keys()
        current = self.config.apiKey
        for k in keys:
            if k == key:
                return current[k]
        return None

class TickersConf:
    def __init__(self) -> None:
        self.tickerConf = './tickers.cfg'
        try:
            configFile = open(self.tickerConf, 'rb')
            self.tickers = pickle.load(configFile)
            configFile.close()

        except:
            self.tickers = tickers
            configFile = open(self.tickerConf, 'wb')
            self.tickers = pickle.dump(self.tickers, configFile)
            configFile.close()

    def get(self):
        return self.tickers
    
    def addTicker(self, tickerSymbol):
        configFile = open(self.tickerConf, 'rb')
        self.tickers = pickle.load(configFile)
        configFile.close()

        self.tickers.append(tickerSymbol)
        configFile = open(self.tickerConf, 'wb')
        pickle.dump(self.tickers, configFile)
        configFile.close()

        return self.tickers
