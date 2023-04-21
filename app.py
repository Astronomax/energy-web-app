import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import geopandas as gpd

app = dash.Dash(__name__)

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

mapbox_access_token = "pk.eyJ1IjoiY2FydG9kYmluYyIsImEiOiJja202bHN2OXMwcGYzMnFrbmNkMzVwMG5rIn0.Zb3J4JTdJS-oYNXlR3nvnQ"
px.set_mapbox_access_token(mapbox_access_token)

fig = px.scatter_mapbox(
    geo_df,
    lat=geo_df.geometry.y,
    lon=geo_df.geometry.x,
    hover_name="name",
    zoom=1)

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(
                id='map',
                figure=fig
            )
        ],
        className="five-twelfth column map__container"),
        html.Div([
            html.Div(children=["hello"])
        ],
        className="seven-twelfth column")
    ],
    className="app__content",)
],
className="app__container")

if __name__ == '__main__':
    app.run_server(debug=True)