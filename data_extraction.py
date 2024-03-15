print("data extraction-------------")
import pandas as pd


def load_data():
    df = pd.read_csv("SampleSuperstore.csv")
    print(df)

    return df

load_data()