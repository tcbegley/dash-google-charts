"""
Animated example app based on https://react-google-charts.com/animations
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
from dash_google_charts import ScatterChart

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Interval(id="interval", interval=1000),
        ScatterChart(
            id="scatter",
            options={
                "title": "A Scatter Plot",
                "animation": {
                    "duration": 1000,
                    "easing": "out",
                    "startup": True,
                },
                "vAxis": {"viewWindow": {"max": -10, "min": 10}},
                "hAxis": {"viewWindow": {"max": 10, "min": -10}},
            },
        ),
    ]
)


@app.callback(Output("scatter", "data"), [Input("interval", "n_intervals")])
def generate_data(n):
    data = pd.DataFrame(
        {
            "x": np.random.uniform(-10, 10, 20),
            "y": np.random.uniform(-10, 10, 20),
        }
    )
    return data.T.reset_index().T.values.tolist()


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
