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
            slowPeriod: int = 5 , 
            fastPeriod: int = 20
            ):

        chart = Chart()
        
        chart.watermark(csvFile, color='rgba(180, 180, 240, 0.7)')
        
        try:
            df = pd.read_csv(csvFile)
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

        
  






    