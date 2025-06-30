import pandas as pd


def load_data(path):
    df = pd.read_csv(path, index_col=0)
    return df


def handle_missing_values(df):
    df = df.copy()
    df["MonthlyIncome"] = df["MonthlyIncome"].fillna(df["MonthlyIncome"].median())
    return df