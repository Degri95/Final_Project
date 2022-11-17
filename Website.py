import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.express as px
import json
import pandas as pd
from pathlib import Path

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
    
data = pd.read_csv('/Users/dante/Final_Project/data/health_outcomes_df.csv')

county_df = data
df = county_df[["CountyFIPS", "CANCER"]]

df["CountyFIPS"] = df["CountyFIPS"].apply(str)



app = dash.Dash(external_stylesheets=[dbc.themes.SANDSTONE])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
        html.Hr(),
        html.P(
            "Visualizations", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [
            html.H1 ("Map", style={'textAlign':'center'}),
            dcc.Graph(figure = px.choropleth_mapbox(df, geojson=counties, locations='CountyFIPS', color='CANCER',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'},
                           width=1000, height=600
                          ))]
                     
    elif pathname == "/page-1":
        return [
            html.H1 ("Graph", style = {'textAlign':'center'}),
            dcc.Dropdown([x for x in df["CountyFIPS"].unique()], id='cont-choice', style={'width':'50%'}),
             ]
    elif pathname == "/page-2":
        return html.P("Machine learning", style={'textAlign':'center'})
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__=='__main__':
    app.run_server(port=8887)