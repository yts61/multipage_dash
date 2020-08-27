import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2, app3, app4
from navbar import *

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    # load the specific page
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return app1.layout
    elif pathname == '/page2':
        return app2.layout
        dcc.Store(id='session', storage_type='session'), 

    elif pathname == '/page3':
        return app3.layout
    elif pathname == '/page4':
        return app4.layout
    else:
        return '404'


if __name__ == "__main__":
    app.run_server(debug = True, port=8064)