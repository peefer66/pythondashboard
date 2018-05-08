#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import plotly.graph_objs as go 
import plotly.offline as pyo 
import numpy as np
import pandas as pd 

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/abalone.csv')


# take two random samples of different sizes:
sample1 = [np.random.choice(df['rings'],10,replace=False)]
sample2 = [np.random.choice(df['rings'], 25, replace=False)]

print(sample1)
print(sample2)

# create a data variable with two Box plots:
data = [go.Box(y=sample1, boxpoints='all', jitter=0.3, pointpos=0, name='Sample1'),
        go.Box(y=sample2, boxpoints='all', jitter=0.3, pointpos=0, name='Sample2')]
# add a layout
layout = go.Layout(title='Graph Title')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
