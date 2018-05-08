#######
# This plot compares sample distributions
# of three-letter-words in the works of
# Quintus Curtius Snodgrass and Mark Twain
######

import plotly.offline as pyo 
import plotly.graph_objs as go 

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [go.Box(y=snodgrass, boxpoints='all', jitter=0.3, pointpos=0, name='Snodgrass'),
        go.Box(y=twain, boxpoints='all', jitter=0.3, pointpos=0, name='Twain')]


layout = go.Layout(title='Comparison of three-letter-word frequencies<br>\
    between Quintus Curtius Snodgrass and Mark Twain')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='twain.html')

