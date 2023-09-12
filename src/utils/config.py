from dotmap import DotMap
import json

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
