import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 


df = pd.read_csv('Data/nst-est2017-alldata.csv')
# Filter out DIVISION  ie string == 1
df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace=True) # Uses the column NAME (State) as the index

# List comprehenstion - create a list of colums that start with POP
list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
# Filter out based on list
df2 = df2[list_of_pop_col] # Dataframe now consists of list of states with there population estimate

# List comprehension - build a line plot for ever state in df2 index 
# x = the estimated population year
# y = the value loc for cells in each column for the name ie State 
data = [go.Scatter(x=df2.columns,
                    y=df2.loc[name],
                    mode='lines',
                    name=name) for name in df2.index ]

pyo.plot(data, filename='states.html')

