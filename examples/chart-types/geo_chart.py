"""
Note: you will need to get a mapsApiKey for your project. See:

https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
"""
import dash
from dash_google_charts import GeoChart

# specify your maps api key here
YOUR_API_KEY = ""

if not YOUR_API_KEY:
    raise ValueError(
        "Please edit this example and add your api key before running."
    )

app = dash.Dash()

app.layout = GeoChart(
    width="100%",
    height="700px",
    data=[
        ["Country", "Popularity"],
        ["Germany", 200],
        ["United States", 300],
        ["Brazil", 400],
        ["Canada", 500],
        ["France", 600],
        ["RU", 700],
    ],
    mapsApiKey=YOUR_API_KEY,
)

if __name__ == "__main__":
    app.run_server()
