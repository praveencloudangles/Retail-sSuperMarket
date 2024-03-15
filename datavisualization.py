print("data visualization--------------")
import matplotlib.pyplot as plt
from feature_engineering import fea_eng
from data_cleaning import data_cleaning
from data_analysis import data_analysis
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
import io
from PIL import Image

def data_vis():
    data = fea_eng()

    column=list(data.columns)
    column_to_remove = ["Profit", "Category", "Ship Mode", "Segment", "Region", "Discount"]
    for col_to_remove in column_to_remove:
        column.remove(col_to_remove)

    print(column)

    columns_to_remove_outliers = ["Quantity", "Sales", "State", "Sub-Category"]

    for col in columns_to_remove_outliers:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1
        upper_limit = q3 + (1.5 * iqr)
        lower_limit = q1 - (1.5 * iqr)

        # Apply the filtering conditions to the original DataFrame
        data = data.loc[(data[col] < upper_limit) & (data[col] > lower_limit)]

    for i in column:
        fig = px.histogram(data, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        # fig.show()
        fig.write_image(f"{i}_hist.jpg")
        # a.append(fig)
    for i in column:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"{i}_box.jpg")
        # a.append(fig)

    columns_to_remove=["Profit"]
    df=data.drop(columns=columns_to_remove,axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    fig.write_image("img.jpg")

    
    return data

data_vis()
