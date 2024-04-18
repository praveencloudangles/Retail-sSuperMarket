print("data cleaning-------------")
from data_analysis import data_analysis
from sklearn.preprocessing import LabelEncoder

def data_cleaning():
    data = data_analysis()

    data.drop_duplicates(inplace=True)

    data.drop('Country', inplace=True, axis=1)

    data.drop('Postal Code', inplace=True, axis=1)

    list(data.columns)

    data['Ship Mode'] = data['Ship Mode'].replace(['Standard Class', 'Second Class', 'First Class', 'Same Day'], [0, 1, 2, 3])

    data['Segment'] = data['Segment'].replace(['Consumer', 'Corporate', 'Home Office'], [0, 1, 2])

    data['Region'] = data['Region'].replace(['West', 'East', 'Central', 'South'], [0, 1, 2, 3])

    data['Category'] = data['Category'].replace(['Office Supplies', 'Furniture', 'Technology'], [0, 1, 2])

    label_encoder = LabelEncoder()

    # Specify columns to encode
    columns_to_encode = ['City', 'State', 'Sub-Category']

    # Apply label encoding to specified columns
    for column in columns_to_encode:
        data[column] = label_encoder.fit_transform(data[column])

    return data
data_cleaning()
