import pandas as pd
def remove_duplicates(df):
    return df.drop_duplicates()


def handle_missing_values(df):
    return df.dropna()


def convert_datetime(df, columns):
    for col in columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except Exception as e:
            print(f"Datetime error in {col}: {e}")
    return df