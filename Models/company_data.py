from dataclasses import dataclass
import pandas as pd
from pandas import DataFrame


@dataclass
class CompanyData:
    name: str
    symbol: str
    historical_prices: pd.Series
    period: str

    def retrieve_historical_prices(self) -> DataFrame:
        if self.historical_prices is None:
            raise ValueError("No hay datos históricos disponibles.")

        return self.clean_data(self.historical_prices)

    def clean_data(self, raw_data):
        if raw_data.empty:
            raise ValueError("La Series de pandas está vacía")

        data = []
        for date, price in raw_data.items():
            data.append({
                'date': date.strftime('%Y-%m-%d'),
                'price': round(float(price), 3)
            })

        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        return df.sort_values('date')