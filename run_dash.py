import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask

import case_map

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#server = Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                )#sharing=True, server=server, csrf_protect=False)

server = app.server

app.layout = html.Div(children=[
    html.H1(children='San Diego County COVID-19 Cases'),

    html.Div(children='''
        Updated 4/2/2020 at 11:08 PM Pacific | Contact Twitter: @alextwenzel
    '''),

    dcc.Graph(
        id='example-graph',
        figure=case_map.build_map_df("data/zipcode_case_counts/through040102020_updated04022020_updated0800.txt")
    )
])

if __name__ == '__main__':
    #app.run_server(debug=True, host='0.0.0.0')
    app.run_server(debug=True)
