import pandas as  pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go 

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x,
                     y=random_y,
                     mode='markers',
                     # set the size colour etc of the plot markers
                     marker=dict(
                         size=12,
                         color='rgb(51,204,153)',
                         symbol='pentagon',
                         line= {'width':2}
                    ))

layout = go.Layout(title='First Plot',
                    xaxis=dict(title='X Axis'), # can also use conventional {} dictionary
                    yaxis=dict(title='Y Axis'), # using dict() method helps multi line reading
                    hovermode=('closest')
                    )
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='scatter.html')
