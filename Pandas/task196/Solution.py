import pandas as pd

data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}

df = pd.DataFrame(data)

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by=['id'], ascending=False, inplace=True)
    person.drop_duplicates(['email'], keep='first', inplace=True)

delete_duplicate_emails(df)

print(df)