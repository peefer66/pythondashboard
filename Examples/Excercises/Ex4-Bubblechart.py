#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd 
import plotly.graph_objs as go 
import plotly.offline as pyo 

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(x=df['weight'], 
                    y=df['acceleration'],
                    mode='markers',
                    text=df['name'],
                    marker=dict(size=df['displacement']/10,
                                color=df['cylinders'],
                                showscale=True)
                    )]
        
                    

# create a layout with a title and axis labels
layout = go.Layout(title='Weight vs Acceration',
                      xaxis=dict(title='Weight (Kg)'),
                      yaxis=dict(title='Acceleration'),
                      hovermode='closest')
                      
# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='bubble2.html')