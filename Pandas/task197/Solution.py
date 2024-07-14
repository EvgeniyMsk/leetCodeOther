import datetime
import pandas as pd

data = {
    'id': [1, 2, 3, 4],
    'recordDate': [
        datetime.date(2015, 1, 1),
        datetime.date(2015, 1, 2),
        datetime.date(2015, 1, 3),
        datetime.date(2015, 1, 4)],
    'temperature': [10, 10, 20, 30],
}

df = pd.DataFrame(data)


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    return weather[
        (weather.temperature.diff() > 0)
        & (weather.recordDate.diff().dt.days == 1)
        ][['id']]


df['delta'] = df.recordDate.diff().dt.days

print(df)
