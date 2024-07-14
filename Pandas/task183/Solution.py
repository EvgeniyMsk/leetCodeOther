import pandas as pd

customers = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
}

orders = {
    'id': [1, 2],
    'customerId': [3, 1]
}

dfCustomers = pd.DataFrame(customers)
dfOrders = pd.DataFrame(orders)


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers.id.isin(orders.customerId)].rename(columns={'name': 'Customers'})
    df = df[['Customers']]
    return df


print(find_customers(dfCustomers, dfOrders))
