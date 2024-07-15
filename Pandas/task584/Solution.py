import pandas as pd



customer = {
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Will', 'Jane', 'Alex', 'Bill', 'Zack', 'Mark'],
    'referee_id': [None, None, 2, None, 1, 2]
}

df = pd.DataFrame(customer)

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[(customer['referee_id'] != 2) | (customer.referee_id.isna())][['name']]


print(find_customer_referee(df))

