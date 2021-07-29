import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("data.csv")
fig = px.scatter(df, x='Population', y='Per Capita', size = 'Percentage', color= "Country", size_max= 60)
fig.show()