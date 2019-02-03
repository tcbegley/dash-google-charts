import json

import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_google_charts import ScatterChart

app = dash.Dash()

app.layout = html.Div(
    [
        ScatterChart(
            id="chart",
            data=[
                ["x", "dogs"],
                [0, 0],
                [1, 10],
                [2, 23],
                [3, 17],
                [4, 18],
                [5, 9],
            ],
        ),
        html.Div(id="output"),
        html.Div(id="datatable"),
    ]
)


@app.callback(Output("output", "children"), [Input("chart", "selection")])
def print_selection(selection):
    print(selection)
    return json.dumps(selection)


@app.callback(Output("datatable", "children"), [Input("chart", "dataTable")])
def print_datatable(datatable):
    print(datatable)
    return json.dumps(datatable)


if __name__ == "__main__":
    app.run_server(debug=True)
