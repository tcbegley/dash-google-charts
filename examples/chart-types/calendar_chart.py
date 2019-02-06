from datetime import date

import dash
import gviz_api
from dash_google_charts import Calendar

data = gviz_api.DataTable(
    [("Date", "date"), ("Attendance", "number")],
    [
        [date(2018, 8, 10), 74439.0],
        [date(2018, 8, 19), 30592.0],
        [date(2018, 8, 27), 74400.0],
        [date(2018, 9, 2), 21525.0],
        [date(2018, 9, 15), 20537.0],
        [date(2018, 9, 19), 31120.0],
        [date(2018, 9, 22), 74489.0],
        [date(2018, 9, 25), 55227.0],
        [date(2018, 9, 29), 56938.0],
        [date(2018, 10, 2), 73569.0],
        [date(2018, 10, 6), 74519.0],
        [date(2018, 10, 20), 40721.0],
        [date(2018, 10, 23), 73946.0],
        [date(2018, 10, 28), 74525.0],
        [date(2018, 11, 3), 10792.0],
        [date(2018, 11, 7), 41470.0],
        [date(2018, 11, 11), 54316.0],
        [date(2018, 11, 24), 74516.0],
        [date(2018, 12, 1), 30187.0],
        [date(2018, 12, 5), 74507.0],
        [date(2018, 12, 8), 74523.0],
        [date(2018, 12, 12), 36544.0],
        [date(2018, 12, 16), 52908.0],
        [date(2018, 12, 22), 33028.0],
        [date(2018, 12, 26), 74523.0],
        [date(2018, 12, 30), 74556.0],
        [date(2019, 1, 2), 52217.0],
        [date(2019, 1, 5), 73918.0],
        [date(2019, 1, 13), 80062.0],
        [date(2019, 1, 19), 74532.0],
        [date(2019, 1, 25), 59571.0],
        [date(2019, 1, 29), 74529.0],
        [date(2019, 2, 3), 32148.0],
    ],
)

app = dash.Dash()

app.layout = Calendar(
    data=data.ToJSon(),
    options={"title": "Manchester United Attendance: 2018/19 season"},
    height="500px",
)

if __name__ == "__main__":
    app.run_server(debug=True)
