import pandas as pd 
import numpy as np 
import plotly.offline as pyo 
import plotly.graph_objs as go 

df = pd.read_csv('Data/mpg.csv')

# xbins start value, end value, size of each bin
data = [go.Histogram(x=df['mpg'],
                     xbins=dict(start=0, end=50, size=10))]


layout = go.Layout(title='Histogram of MPG',
                     xaxis=dict(title='MPG'),
                     yaxis=dict(title='COUNT')
                     )

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='histogram.html')