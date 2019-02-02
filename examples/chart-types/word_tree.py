import dash
from dash_google_charts import WordTree

app = dash.Dash()

app.layout = WordTree(
    data=[
        ["Phrases"],
        ["cats are better than dogs"],
        ["cats eat kibble"],
        ["cats are better than hamsters"],
        ["cats are awesome"],
        ["cats are people too"],
        ["cats eat mice"],
        ["cats meowing"],
        ["cats in the cradle"],
        ["cats eat mice"],
        ["cats in the cradle lyrics"],
        ["cats eat kibble"],
        ["cats for adoption"],
        ["cats are family"],
        ["cats eat mice"],
        ["cats are better than kittens"],
        ["cats are evil"],
        ["cats are weird"],
        ["cats eat mice"],
    ],
    options={"wordtree": {"format": "implicit", "word": "cats"}},
)

if __name__ == "__main__":
    app.run_server()
