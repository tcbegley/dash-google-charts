import dash
from dash_google_charts import SteppedAreaChart

app = dash.Dash()

app.layout = SteppedAreaChart(
    height="500px",
    data=[
        ["Director (Year)", "Rotten Tomatoes", "IMDB"],
        ["Alfred Hitchcock (1935)", 8.4, 7.9],
        ["Ralph Thomas (1959)", 6.9, 6.5],
        ["Don Sharp (1978)", 6.5, 6.4],
        ["James Hawes (2008)", 4.4, 6.2],
    ],
    options={
        "title": "The decline of 'The 39 Steps'",
        "vAxis": {"title": "Accumulated Rating"},
        "isStacked": True,
    },
)

if __name__ == "__main__":
    app.run_server()
