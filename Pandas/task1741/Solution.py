import datetime
import pandas as pd

data = {
    'emp_id': [1, 1, 1, 2, 2],
    'event_day': [datetime.date(2020, 11, 28),
                  datetime.date(2020, 11, 28),
                  datetime.date(2020, 12, 3),
                  datetime.date(2020, 11, 28),
                  datetime.date(2020, 12, 9)],
    'in_time': [4, 55, 1, 3, 47],
    'out_time': [32, 200, 42, 33, 74]
}

df = pd.DataFrame(data)

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    temp = employees
    temp['total_time'] = employees['out_time'] - employees['in_time']
    result = temp.groupby(['event_day', 'emp_id'])[['total_time']].sum().reset_index()
    return result.rename(columns={'event_day': 'day'})

print(total_time(df))

