import pandas as pd

data = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
}

df = pd.DataFrame(data)

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'].apply(lambda x: x * 2)
    return employees[['name', 'salary', 'bonus']]

print(createBonusColumn(df))