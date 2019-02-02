import random

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_google_charts import Gauge

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Interval(id="interval", interval=1000),
        Gauge(
            id="gauge",
            options={
                "redFrom": 90,
                "redTo": 100,
                "yellowFrom": 75,
                "yellowTo": 90,
                "minorTicks": 5,
            },
        ),
    ]
)


@app.callback(Output("gauge", "data"), [Input("interval", "n_intervals")])
def generate_data(n):
    return [
        ["Label", "Value"],
        ["Memory", random.random() * 100],
        ["CPU", random.random() * 100],
        ["Network", random.random() * 100],
    ]


if __name__ == "__main__":
    app.run_server()
