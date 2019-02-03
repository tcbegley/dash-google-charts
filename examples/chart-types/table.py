import dash
from dash_google_charts import Table

app = dash.Dash()

app.layout = Table(
    data=[
        [
            {"type": "string", "label": "Name"},
            {"type": "number", "label": "Salary"},
            {"type": "boolean", "label": "Full Time Employee"},
        ],
        ["Mike", {"v": 10000, "f": "$10,000"}, True],
        ["Jim", {"v": 8000, "f": "$8,000"}, False],
        ["Alice", {"v": 12500, "f": "$12,500"}, True],
        ["Bob", {"v": 7000, "f": "$7,000"}, True],
    ],
    options={"showRowNumber": True},
)

if __name__ == "__main__":
    app.run_server()
