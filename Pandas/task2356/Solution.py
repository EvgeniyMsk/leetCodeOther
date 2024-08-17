import pandas as pd

data = {
    'teacher_id': [1, 1, 1, 2, 2, 2, 2],
    'subject_id': [2, 2, 3, 1, 2, 3, 4],
    'dept_id': [3, 4, 3, 1, 1, 1, 1],
}

df = pd.DataFrame(data)

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby('teacher_id', as_index=False).agg(cnt=('subject_id', 'nunique'))

print(count_unique_subjects(df))