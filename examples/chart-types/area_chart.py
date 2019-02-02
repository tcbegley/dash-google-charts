import dash
from dash_google_charts import AreaChart

app = dash.Dash()

app.layout = AreaChart(
    width="100%",
    height="500px",
    data=[
        ["Year", "Sales", "Expenses"],
        ["2013", 1000, 400],
        ["2014", 1170, 460],
        ["2015", 660, 1120],
        ["2016", 1030, 540],
    ],
    options={
        "title": "Company Performance",
        "hAxis": {"title": "Year", "titleTextStyle": {"color": "#333"}},
        "vAxis": {"minValue": 0},
        "chartArea": {"width": "50%", "height": "70%"},
    },
)

if __name__ == "__main__":
    app.run_server()
