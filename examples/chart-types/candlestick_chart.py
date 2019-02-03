import dash
from dash_google_charts import CandlestickChart

app = dash.Dash()

app.layout = CandlestickChart(
    width="100%",
    height="500px",
    data=[
        ["day", "a", "b", "c", "d"],
        ["Mon", 20, 28, 38, 45],
        ["Tue", 31, 38, 55, 66],
        ["Wed", 50, 55, 77, 80],
        ["Thu", 77, 77, 66, 50],
        ["Fri", 68, 66, 22, 15],
    ],
    options={"legend": "none"},
)

if __name__ == "__main__":
    app.run_server()
