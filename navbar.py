import os
import pathlib
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
# https://dash-bootstrap-components.opensource.faculty.ai/l/components

# Dash DAQ comprises a robust set of fancy controls
import dash_daq as daq

from app import app, server

LOGO = "http://www.d100.net/wp-content/uploads/2013/12/D100.png"


# dropdown Items
# make a reuseable navitem for the different examples for the dbc container below
nav_item = dbc.NavItem(dbc.NavLink("D100 網站", href="http://www.d100.net/"))




# make a reuseable dropdown for the different examples for the dbc container below
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("收聽D100 PBS台", href='http://www.d100.net/radio.php?cid=1'),
        dbc.DropdownMenuItem("D100 App iOS 用戶", href='https://itunes.apple.com/hk/app/d100/id588656311?mt=8'),
        dbc.DropdownMenuItem("D100 App Android 用戶", href='https://play.google.com/store/apps/details?id=hk.d100&hl=zh_TW'),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Youtube", href='https://www.youtube.com/d100hk'),
        dbc.DropdownMenuItem("D100 Radio Facebook Fan Page", href='https://www.facebook.com/D100Radio'),
    ],
    nav=True,
    in_navbar=True,
    label="D100網上電台最新消息",
)

nav = dbc.Nav(
            [
                dbc.NavLink("題目首頁", href="/",style={"color": "#f8f9fa"}),
                dbc.NavLink("第一條", href="/page2", style={"color": "#f8f9fa"}),
                dbc.NavLink("結果", href="/page3", style={"color": "#f8f9fa"}),

            ],  horizontal="center", pills=True
        )







"""------------------------------------  Header  ------------------------------------"""
navbar = html.Div([
    dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=LOGO, height="50px")),
                                    dbc.Col(dbc.NavbarBrand("網上電台", className="ml-2")),
                                ],
                                align="center",
                                no_gutters=True,
                            ),
                            href="https://positivehk.com/category/健康相關/疾病預防/肺炎防疫2020/",
                        ),

                        dbc.NavbarToggler(id="navbar-toggler"),
                        dbc.Collapse(
                            dbc.Nav(
                                [nav_item,
                                 dropdown,
                                 ], className="ml-auto", navbar=True
                            ),
                            id="navbar-collapse",
                            navbar=True,
                        )
                    ],
                ),
                color="primary",
                dark="",
                className="mt-0 pt-5",
                light=True,
                sticky="top",
                style={"width": "100%"}
            ),
    html.Div(nav, className="mt-0 bg-primary")

])


"""------------------------------------  Paste to the index.py  ------------------------------------"""

# add callback for toggling the collapse on small screens

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
