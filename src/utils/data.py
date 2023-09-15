import os
import requests
from utils.config import Config
import pandas as pd


config_file_path = "../config/config.json"


class Data:
    def __init__(self, dataProvider):
        self.config = Config(config_file_path)
        self.dataProvider = dataProvider


    def fetch(self, apiUri):
        apiKey = self.config.getApiKey(self.dataProvider)
        headers = {
            'Content-Type': 'application/json',
            'Authorization' : f'Token {apiKey}'
        }

        requestResponse = requests.get(apiUri, headers=headers)
        return requestResponse.json()


    def calcSMA (self, df, price, days):
        '''
        Adds moving averages to the existing dataframe \n
        
        Arguments:
             df:        the source data frame
             price:     price column where averages are based on
                        eg: close, high, low, etc...
             days:      the number of days to calculate 
                        eg: 20-day SMA, days = 20
        '''
        df[f'{days}-Day-SMA'] = df[price].rolling(window=days).mean().fillna(0)
        return df



    def convert2DataFrame(self, data):
        '''
        Converts rawaDta into a dataFrame from a array of price object \n
        Example \n
        data = [
            {'date': '2023-09-11T00:00:00.000Z', 'close': 273.58, 'high': 274.85, 'low': 260.61, 'open': 264.27, 'volume': 174667852, 'adjClose': 273.58, 'adjHigh': 274.85, 'adjLow': 260.61, 'adjOpen': 264.27, 'adjVolume': 174667852, 'divCash': 0.0, 'splitFactor': 1.0},
            {'date': '2023-09-12T00:00:00.000Z', 'close': 267.48, 'high': 278.39, 'low': 266.6, 'open': 270.76, 'volume': 135999866, 'adjClose': 267.48, 'adjHigh': 278.39, 'adjLow': 266.6, 'adjOpen': 270.76, 'adjVolume': 135999866, 'divCash': 0.0, 'splitFactor': 1.0},
            {'date': '2023-09-13T00:00:00.000Z', 'close': 271.3, 'high': 274.98, 'low': 268.1, 'open': 270.07, 'volume': 111164741, 'adjClose': 271.3, 'adjHigh': 274.98, 'adjLow': 268.1, 'adjOpen': 270.07, 'adjVolume': 111164741, 'divCash': 0.0, 'splitFactor': 1.0}
        ]
        '''
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date']).dt.date

        return df
    

    def saveDf2Csv(self, df, folderPath, fileName):
        '''
        Save a DataFrame to a CSV file.

        Parameters:
            df (pd.DataFrame): The DataFrame to be saved.
            file_path (str): The path to the CSV file where the DataFrame will be saved.
        Returns:
            bool: True if the DataFrame was successfully saved, False otherwise.
        '''
        fullCsvFilePath = os.path.join(folderPath, fileName)

        try:
            # Set index=False to exclude the index column
            df.to_csv(fullCsvFilePath, index=False)  

            print(f"DataFrame saved to {fullCsvFilePath}")

            return True
        
        except Exception as e:
            print(f"Error saving DataFrame to {fullCsvFilePath}: {str(e)}")
            return False
