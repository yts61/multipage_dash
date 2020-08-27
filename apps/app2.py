from dash.dependencies import Output, Input, State
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import json
from app import app


center={'width':'100%','display':'flex','align-items':'center','justify-content':'center'}

style = {'maxWidth': '',
         'margin': 'auto',
         'padding': '20px',
         'background-color': "#525ca3",}

#https://community.plotly.com/t/make-the-text-fit-to-the-button-width/43734

layout = html.Div([
    html.Br(),
    dbc.Row(
    [
        dbc.Col([
            html.Div(
                html.Img(src="/assets/18.jpg",
                         style={'height': '',
                                'width': '40%', },
                         ), style={'width':'100%','display':'flex','align-items':'center','justify-content':'center'}
            ),
        ], lg=6, md=6, xs=12, style=center),


        dbc.Col([
            html.H2("(1)您年滿 18 歲嗎？", className="display-5", style={"color": "#efe2be", }),
            html.Div([
                dcc.RadioItems(
                    id='q1',
                    options=[{'label': '是', 'value': '18'},
                             {'label': '否', 'value': '0'}],
                    value='0',
                    labelStyle={"font-size":40, "padding":"10px", "color": "#efe2be", },
            )]),
            html.P(dbc.Button("下一題", color="primary", href="/page3"), className="lead"),

        ], lg=6, md=6, xs=12),

    ]),
    html.Div(dbc.Col(dbc.Progress("第一題", value=90, striped=True, color="success", animated=True,),
            className="my-5", width={"size":10, "offset":1})),

    # Hidden div inside the app that stores the intermediate value
    html.Div(html.H1(id="result")),

], style=style

)

@app.callback(Output('session', 'data'), 
              [Input('q1', 'value')])
def q1_value(q1):
     # some expensive clean data step
        return {'answer1value': q1}





#________________________________________________________________________




@app.callback(Output('result', 'children'),
              [Input('session', 'data')])
def result(data):
    math = data['answer1value']
    return 'your answer is "{}"'.format(math)