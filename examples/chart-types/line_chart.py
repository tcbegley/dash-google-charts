import dash
from dash_google_charts import LineChart

app = dash.Dash()

app.layout = LineChart(
    height="500px",
    data=[
        ["x", "dogs"],
        [0, 0],
        [1, 10],
        [2, 23],
        [3, 17],
        [4, 18],
        [5, 9],
        [6, 11],
        [7, 27],
        [8, 33],
        [9, 40],
        [10, 32],
        [11, 35],
    ],
    options={"hAxis": {"title": "Time"}, "vAxis": {"title": "Popularity"}},
)

if __name__ == "__main__":
    app.run_server()
