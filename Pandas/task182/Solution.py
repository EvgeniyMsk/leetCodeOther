import pandas as pd


class solution:
    def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
        return person.loc[person.duplicated('email') == True][['email']].drop_duplicates(keep='first')
