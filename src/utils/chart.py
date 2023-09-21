import pandas as pd
from lightweight_charts import Chart


class Charts:
        
    def _setSmaData(self, df, period: int = 20):
        return pd.DataFrame({
            'time': df['date'],
            f'{period}-SMA': df['close'].rolling(window=period).mean()
        }).dropna()
    

    def render(
            self,
            csvFile: str, 
            slowPeriod: int = 20 , 
            fastPeriod: int = 5
        ):

        try:
            chart = Chart()
            ticker = csvFile.split('/')[-1].split('.')[0]
            chart.watermark(ticker, color='rgba(180, 180, 240, 0.7)')

            try:
                df = pd.read_csv(csvFile)
            except FileNotFoundError:
                print(f"The file '{csvFile}' does not exist.")
                print("Make sure `--fetch-data` have been executed first before viewing the chart. ")
                return
            
            chart.set(df)

            slowLine = chart.create_line(f'{slowPeriod}-SMA')
            sSmaData = self._setSmaData(df, period=slowPeriod)
            slowLine.set(sSmaData)

            fastLine = chart.create_line(f'{fastPeriod}-SMA')
            fSmaData = self._setSmaData(df, period=fastPeriod)
            fastLine.set(fSmaData)

            chart.show(block=True)

        except Exception as e:
            return Exception("Failed to render chart: " + str(e))

        
  






    