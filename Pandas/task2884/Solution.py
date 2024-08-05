import pandas as pd

data = {
    'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
    'salary': [19666, 74754, 62509, 54866]
}

df = pd.DataFrame(data)

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].apply(lambda x: int(x * 2))
    return employees

print(modifySalaryColumn(df))