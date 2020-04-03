import dash
import dash_core_components as dcc
import dash_html_components as html

import case_map

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=case_map.build_map_df("data/zipcode_case_counts/through040102020_updated04022020_updated0800.txt")
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
