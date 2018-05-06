import numpy as np
import pandas as pd

import plotly.graph_objs as go
import plotly.offline as pyo

np.random.seed(56)

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

# Scatter plot - just markers
trace0 = go.Scatter(x=x_values,
                    y=y_values+5,
                    mode='markers',
                    name='markers'
                    )
# Line plot
trace1 = go.Scatter(x=x_values,
                    y=y_values,
                    mode='lines',
                    name='mylines')
# lines and markers
trace2 = go.Scatter(x=x_values,
                    y=y_values - 5,
                    mode='lines+markers',
                    name='mylines and markers')

data = [trace0, trace1, trace2]

layout=go.Layout(title='Line Chart')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='linechart.html')
