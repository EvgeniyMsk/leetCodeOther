import pandas as pd

data = {
    'product_id': [0, 1, 2, 3, 4],
    'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
    'recyclable': ['N', 'Y', 'Y', 'Y', 'N'],
}

df = pd.DataFrame(data)

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]

print(find_products(df))