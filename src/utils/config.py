from dotmap import DotMap
import json

tickers = [
    "TSLA",  # TESLA
    "NVDA",  # NVIDIA CORP
    "AVGO",  # Broadcom
    "MSFT",  # Microsoft
    "AMZN",  # Amazo
    "ORCL",  # Oraclen
    "GOOG",  # Google
    "META",  # Facebook
    "AMD",   # ADVANCED MICRO DEVICES INC
    "BABA"   # ALIBABA GROUP HOLDING LTD
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
        self.tickers = tickers

    def get(self):
        return self.tickers
