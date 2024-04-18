print("feature engineer-------------------")
from datavisualization import data_vis
import pandas as pd

def fea_eng():
    data = data_vis()


    data.to_csv("Retail_SuperMarket.csv", index=False)

    return data

fea_eng()
