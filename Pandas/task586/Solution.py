import pandas as pd

orders = {
    'order_number': [1, 2, 3, 4],
    'customer_number': [1, 2, 3, 3]
}

df = pd.DataFrame(orders)

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()

print(largest_orders(df))