import dash
from dash_google_charts import ScatterChart

app = dash.Dash()

app.layout = ScatterChart(
    height="400px",
    data=[
        ["Age", "Weight"],
        [8, 12],
        [4, 5.5],
        [11, 14],
        [4, 5],
        [3, 3.5],
        [6.5, 7],
    ],
    options={
        "title": "Age vs. Weight comparison",
        "hAxis": {"title": "Age", "minValue": 0, "maxValue": 15},
        "vAxis": {"title": "Weight", "minValue": 0, "maxValue": 15},
        "legend": "none",
    },
)

if __name__ == "__main__":
    app.run_server()
