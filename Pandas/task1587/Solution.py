import pandas as pd
import datetime

users = {
    'account': [900001, 900002, 900003],
    'name': ['Alice', 'Bob', 'Charlie']
}

transactions = {
    'trans_id': [1, 2, 3, 4, 5, 6, 7],
    'account': [900001, 900001, 900001, 900002, 900003, 900003, 900003],
    'amount': [7000, 7000, -3000, 1000, 6000, 6000, -4000],
    'transacted_on': [datetime.date(2020, 8, 1),
                      datetime.date(2020, 9, 1),
                      datetime.date(2020, 9, 2),
                      datetime.date(2020, 9, 12),
                      datetime.date(2020, 8, 7),
                      datetime.date(2020, 9, 7),
                      datetime.date(2020, 9, 11)]
}

dfUsers = pd.DataFrame(users)
dfTransactions = pd.DataFrame(transactions)

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    return transactions.groupby('account')[['amount']].sum().join(users.set_index('account')).query('amount > 10000').rename(columns={'amount': 'balance'})


print(account_summary(dfUsers, dfTransactions))
