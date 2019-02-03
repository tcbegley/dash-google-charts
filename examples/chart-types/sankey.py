import dash
from dash_google_charts import Sankey

app = dash.Dash()

app.layout = Sankey(
    height="400px",
    data=[
        ["From", "To", "Weight"],
        ["A", "X", 5],
        ["A", "Y", 7],
        ["A", "Z", 6],
        ["B", "X", 2],
        ["B", "Y", 9],
        ["B", "Z", 4],
    ],
)

if __name__ == "__main__":
    app.run_server()
