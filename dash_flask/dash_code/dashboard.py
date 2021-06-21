"""Instantiate a Dash app."""
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import numpy as np
import pandas as pd

from .data import create_dataframe
from .layout import html_layout


def init_dashboard():
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=False,
        url_base_pathname="/dashapp/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    df = create_dataframe()

    # Custom HTML layout
    #dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            html.Div(
                id="banner",
                className="banner",
                children=[html.Img(src=dash_app.get_asset_url("plotly_logo.png"))],
            ),
            dcc.Graph(
                id="histogram-graph",
                figure={
                    "data": [
                        {
                            "x": df["complaint_type"],
                            "text": df["complaint_type"],
                            "customdata": df["key"],
                            "name": "311 Calls by region.",
                            "type": "histogram",
                        }
                    ],
                    "layout": {
                        "title": "NYC 311 Calls category.",
                        "height": 500,
                        "padding": 150,
                    },
                },
            ),
            create_data_table(df),
        ],
        id="dash-container",
    )
    return dash_app


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={
            'height': '500px'
        },
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=50,
    )
    return table
