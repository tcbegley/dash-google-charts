from datetime import date

import dash
import gviz_api
from dash_google_charts import Timeline

data = gviz_api.DataTable(
    [("President", "string"), ("Start", "date"), ("End", "date")],
    [
        ["Washington", date(1789, 3, 30), date(1797, 2, 4)],
        ["Adams", date(1797, 2, 4), date(1801, 2, 4)],
        ["Jefferson", date(1801, 2, 4), date(1809, 2, 4)],
    ],
)

app = dash.Dash()

app.layout = Timeline(data=data.ToJSon())

if __name__ == "__main__":
    app.run_server(debug=True)
