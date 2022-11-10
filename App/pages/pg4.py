import dash
from dash import dcc, html
import plotly.express as px


from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd


from pathlib import Path

data = Path('../data/health_outcomes_df.csv')

county_df = pd.read_csv(data)
df = county_df[["CountyFIPS", "CANCER"]]

df["CountyFIPS"] = df["CountyFIPS"].apply(str)


import plotly.express as px


fig = px.choropleth_mapbox(df, geojson=counties, locations='CountyFIPS', color='CANCER',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()





dash.register_page(__name__)

df = px.data.gapminder()

layout = html.Div(
    [
        dcc.Graph(id='line-fig', figure = fig)
    ]
)

