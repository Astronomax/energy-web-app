from datetime import *
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_extensions.enrich import  DashProxy, MultiplexerTransform, html,  dcc
import plotly.graph_objects as go
import plotly.express as px
import geopandas as gpd
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
px.set_mapbox_access_token(open(".mapbox_token").read())
fig = px.scatter_mapbox(
    geo_df,
    lat=geo_df.geometry.y,
    lon=geo_df.geometry.x,
    hover_name="name",
    zoom=1)

tips = px.data.tips()
df = pd.read_csv('./assets/data/Meteo_0_test_1.csv')  
df = df.head(500)
df['ts'] = df['ts'].apply(lambda ts: datetime.utcfromtimestamp(int(str(ts)[:-3])))
temp_fig = px.line(df, x='ts', y='Temperature')
#temp_fig = go.Figure(data=[go.Scatter()])

tabs = {
    'intro': dbc.Row([
        dbc.Col(
            dcc.Graph(
                id='map',
                figure=fig
            ), 
            width = 5
        ),
        dbc.Col(
            dcc.Graph(figure=temp_fig), 
            width = 7
        )
    ]),
    'analysis': dbc.Row([
        dbc.Col(
            html.Div(children=["left"]), 
            width = 5
        ),
        dbc.Col(
            html.Div(children=["right"]), 
            width = 7
        )
    ]),
    'about': html.Div([
        html.H3('Tab content 3')
    ])
}

@app.callback(
    Output('tabs-content-1', 'children'),
    Input('tabs-example-1', 'value')
)
def render_content(tab):
    return tabs[tab]

app.layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.A(
                [html.Img(src=app.get_asset_url("icsenergy-logo.png"))], 
                href="https://energy.ipu.ru/"), 
            width = 2
        ),
        dbc.Col(
            dcc.Tabs([
                dcc.Tab(label='Intro', value='intro'),
                dcc.Tab(label='Analysis', value='analysis'),
                dcc.Tab(label='About the platform', value='about'),
            ],
            id='tabs-example-1', 
            value='intro'
            ),
            width = 5
        )
    ]), #navigation
    html.Div(
        className="tabs__content",
        id='tabs-content-1'
    ), #tab-content
])

if __name__ == '__main__':
    app.run_server(debug=True)