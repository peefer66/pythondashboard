import numpy as np
import pandas as pd

import plotly.graph_objs as go
import plotly.offline as pyo


#create random seed
np.random.seed(56)
# x values - create numbers evenly spaced between 0 and 1
# y values -  create 100 random numbers to normal distribution
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

# Scatter plot - just markers
trace0 = go.Scatter(x=x_values,
                    y=y_values+5, #  Add 5  to y values so that all chartys do not overlay each other
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
                    y=y_values - 5, # Subtract 5 from all nubers 
                    mode='lines+markers',
                    name='mylines and markers')

data = [trace0, trace1, trace2]

# layout formats the chart titles etc
layout=go.Layout(title='Line Chart')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='linechart.html')
