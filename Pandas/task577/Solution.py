import pandas as pd

employee = {
    'empId': [3, 1, 2, 4],
    'name': ['Brad', 'John', 'Dan', 'Thomas'],
    'supervisor': [None, 3, 3, 3],
    'salary': [4000, 1000, 2000, 4000]
}

bonus = {
    'empId': [2, 4],
    'bonus': [500, 2000]
}

df_employee = pd.DataFrame(employee)
df_bonus = pd.DataFrame(bonus)


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    return employee.merge(bonus, on='empId', how='left').query('bonus <= 1000 | bonus.isnull()')[['name', 'bonus']]


print(employee_bonus(df_employee, df_bonus))
