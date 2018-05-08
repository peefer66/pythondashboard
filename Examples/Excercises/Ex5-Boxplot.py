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
print(df)

# take two random samples of different sizes:



# create a data variable with two Box plots:











# add a layout




# create a fig from data & layout, and plot the fig
