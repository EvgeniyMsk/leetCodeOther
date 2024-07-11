import pandas as pd


class Solution:
    def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
        result = employee.drop_duplicates(['salary'], keep='first').sort_values(by='salary', ascending=False).head(2).loc[employee['salary'] != employee['salary'].max()][['salary']].rename(columns={'salary': 'SecondHighestSalary'})
        if result.empty:
            return pd.DataFrame({'SecondHighestSalary': [None]})
        return result
