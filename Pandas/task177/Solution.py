import pandas as pd

emp = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300],
}

df = pd.DataFrame(emp)


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    s = set()
    for i in employee["salary"]:
        s.add(i)
    l = list(set(s))
    l.sort()
    if len(l) < N or N <= 0 or len(l) == 0:
        a = None
    else:
        a = l[-N]
    r = "getNthHighestSalary" + "(" + str(N) + ")"
    t = {r: [a]}
    return pd.DataFrame(t)


print(nth_highest_salary(df, 3))
