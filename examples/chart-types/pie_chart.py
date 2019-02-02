"""
Example app based on https://react-google-charts.com/pie-chart
"""
import json

import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_google_charts import PieChart

app = dash.Dash()

app.layout = html.Div(
    [
        PieChart(
            id="chart",
            data=[
                ["Task", "Hours per Day"],
                ["Work", 11],
                ["Eat", 2],
                ["Commute", 2],
                ["Watch TV", 2],
                ["Sleep", 7],
            ],
            options={"title": "My Daily Activities"},
        ),
        html.Div(id="output"),
    ]
)


@app.callback(Output("output", "children"), [Input("chart", "selection")])
def print_selection(selection):
    print(selection)
    return json.dumps(selection)


if __name__ == "__main__":
    app.run_server(port=8888)
