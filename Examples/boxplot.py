import plotly.offline as pyo 
import plotly.graph_objs as go 

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]
# boxpoints all - shows the all the points of data, ouliers just the outlining points etc
# jitter - spreads the points out, they will retain their y values, reduces the congestion.
# pointpos -the position of the points minus to the left, positive to the right and 0 on top
# 
data = [go.Box(y=y, boxpoints='outliers', jitter=0.3, pointpos=0)]

pyo.plot(data)