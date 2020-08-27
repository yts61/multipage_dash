from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate



from app import app


style = {'maxWidth': '960px',
         'margin': 'auto',
         'padding': '10px',
         'background-color': "",}

#https://community.plotly.com/t/make-the-text-fit-to-the-button-width/43734

layout = html.Div([

    html.Div(dcc.Link('Go to App 1', href='/', className="mt-5 pt-5")),
    html.Div(html.H1(id="results")),
    html.Div(dbc.Progress("恭喜你你已經完成所有題目了!", value=100, striped=True, animated=True), className="mt-5 pt-5"),
    html.Div(html.H1(id="results")),
],
    style=style)


@app.callback(Output('results', 'children'),
              [Input('session', 'data')])
def result(data):
    math2 = data['answer1value']
    return 'your answer is "{}"'.format(math2)

