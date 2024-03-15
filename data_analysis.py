print("data analysis--------------")
from data_extraction import load_data

def data_analysis():
    data = load_data()
    print(data)

    data.isnull().sum()
    data.duplicated().sum()
    data.describe()
    data.shape
    data.nunique()

    return data

data_analysis()
