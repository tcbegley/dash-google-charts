import dash
from dash_google_charts import OrgChart

app = dash.Dash()

app.layout = OrgChart(
    height="400px",
    data=[
        ["Name", "Manager", "ToolTip"],
        [
            {"v": "Mike", "f": 'Mike<div style="color:red;">President</div>'},
            "",
            "The President",
        ],
        [
            {
                "v": "Jim",
                "f": 'Jim<div style="color:red;">Vice President</div>',
            },
            "Mike",
            "VP",
        ],
        ["Alice", "Mike", ""],
        ["Bob", "Jim", "Bob Sponge"],
        ["Carol", "Bob", ""],
    ],
    options={"allowHtml": True},
)

if __name__ == "__main__":
    app.run_server()
