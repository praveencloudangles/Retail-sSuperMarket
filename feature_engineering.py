print("feature engineer-------------------")
from data_cleaning import datavisualization
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def fea_eng():
    data = datavisualization()

    label_encoder = LabelEncoder()

    # Specify columns to encode
    columns_to_encode = ['City', 'State', 'Sub-Category']

    # Apply label encoding to specified columns
    for column in columns_to_encode:
        data[column] = label_encoder.fit_transform(data[column])


    data.to_csv("Retail_SuperMarket.csv", index=False)

    return data

fea_eng()
