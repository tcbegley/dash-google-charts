from datetime import date

import dash
import gviz_api
from dash_google_charts import GanttChart

data = gviz_api.DataTable(
    [
        ("Task ID", "string"),
        ("Task Name", "string"),
        ("Start Date", "date"),
        ("End Date", "date"),
        ("Duration", "number"),
        ("Percent Complete", "number"),
        ("Dependencies", "string"),
    ],
    [
        [
            "Research",
            "Find sources",
            date(2015, 1, 1),
            date(2015, 1, 5),
            None,
            100,
            None,
        ],
        [
            "Write",
            "Write paper",
            None,
            date(2015, 1, 9),
            3 * 24 * 60 * 60 * 1000,
            25,
            "Research,Outline",
        ],
        [
            "Cite",
            "Create bibliography",
            None,
            date(2015, 1, 7),
            1 * 24 * 60 * 60 * 1000,
            20,
            "Research",
        ],
        [
            "Complete",
            "Hand in paper",
            None,
            date(2015, 1, 10),
            1 * 24 * 60 * 60 * 1000,
            0,
            "Cite,Write",
        ],
        [
            "Outline",
            "Outline paper",
            None,
            date(2015, 1, 6),
            1 * 24 * 60 * 60 * 1000,
            100,
            "Research",
        ],
    ],
)

app = dash.Dash()

app.layout = GanttChart(data=data.ToJSon(), width="1000px", height="300px")

if __name__ == "__main__":
    app.run_server(debug=True)
