#importing libraries 
import pandas as pd
import datetime as dt
import geopandas
import matplotlib.pyplot as plt
import numpy as np
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from dash import Dash, dash_table
import plotly.graph_objects as go
from pandas.io.html import read_html
spotify=pd.read_csv('Spotify-2000.csv')

import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')

spotify_group = spotify.groupby('Top Genre')['Title'].nunique().reset_index()
fig2 = px.bar(spotify_group, x='Top Genre', y='Title')

### pandas dataframe to html table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server
app.layout = html.Div([

dcc.Graph(figure=fig)
,dcc.Graph(figure=fig2) 
])
if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)
    
    
