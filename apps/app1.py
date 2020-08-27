

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc

from app import app


style = {'maxWidth': '960px',
         'margin': 'auto',
         'padding': '20px',
         'background-color': "#525ca3",}


center={'width':'100%','display':'flex','align-items':'center','justify-content':'center'}



layout = dbc.Jumbotron([
    dbc.Row(
    [
        dbc.Col([
            html.Div(
                html.Img(src="/assets/home.jpg",
                         style={'height': '',
                                'width': '80%', }, id="the_id")),
            dbc.Tooltip(
                        "Noun: rare, "
                        "the action or habit of estimating something as worthless.",
                        target="the_id",
        ),
        ], lg=6, md=6, xs=12, style=center),

        dbc.Col([
            html.H1("您的濕疹病情是否受控？", className="display-5", style={"color":"#efe2be",} ),
            html.P(
                "請想想您患有濕疹（有時稱為異位性皮膚炎）的經驗，回答下列6條簡單的選擇題，就可了解自己的濕疹病情的受控情況。",
                className="lead", style={"color":"#efe2be",}
            ),
            html.P(dbc.Button("開始評估", color="primary", href="/page2"), className="lead"),
            html.Hr(className="my-2"),
            html.Small(
                "此異位性皮膚炎控制工具 (ADCT) 之設計用途是為協助患者和醫生全面有效地掌握其疾病情況。要自我評估 AD "
                "的控制情況如何，請回答以下問題。您對 ADCT 的回答將有助您的醫生或護士更妥善地了解您的治療需求。"
                "在諮詢醫生或專業醫護人員前，請勿停止或更改您的用藥。"
            ),
        ], lg=6, md=6, xs=12),

    ],

), html.Div(dbc.Col(dbc.Progress("開始評估", value=20, striped=True, color="success", animated=True,),
            className="my-5", width={"size":10, "offset":1}))
], style={"background-color": "#525ca3"}

)
