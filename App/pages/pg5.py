import dash
from dash import dcc, html

dash.register_page(__name__)


import plotly.express as px

df = px.data.gapminder()

layout = html.Div(
    [
        dcc.Dropdown([x for x in df.continent.unique()], id='cont-choice', style={'width':'50%'}),
        dcc.Graph(id='line-fig',
                  figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
    ]
)

