"""
Example app based on https://react-google-charts.com/pie-chart
"""
import dash
from dash_google_charts import Chart

app = dash.Dash()

app.layout = Chart(
    chartType="PieChart",
    data=[
        ["Task", "Hours per Day"],
        ["Work", 11],
        ["Eat", 2],
        ["Commute", 2],
        ["Watch TV", 2],
        ["Sleep", 7],
    ],
    options={"title": "My Daily Activities"},
)


if __name__ == "__main__":
    app.run_server(port=8888)
