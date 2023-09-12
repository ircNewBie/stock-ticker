import requests
from utils.config import Config

config_file_path = "../config/config.json"


class Data:
    def __init__(self, dataProvider):
        self.config = Config(config_file_path)
        self.dataProvider = dataProvider

    def fetch(self, apiUri):
        apiKey = self.config.getApiKey(self.dataProvider)

        headers = {
            'Content-Type': 'application/json'
        }

        requestResponse = requests.get(
            apiUri + "?token=" + apiKey,
            headers=headers
        )

        return requestResponse.json()[0]
