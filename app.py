from dash import Dash, html, dcc, html, callback, Input, Output
from pages import dashboard
from lib import navBar
import plotly.express as px
import pandas as pd

app = Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

df2 = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [20, 10, 30, 40, 15, 55],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig2 = px.bar(df2, x="Fruit", y="Amount", color="City", barmode="group")

CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

app.layout = html.Div(children=[
    # represents the browser address bar and doesn't render anything
    dcc.Location(id='url', refresh=False),
    navBar.layout,
    html.H1(children='Hello Dash',style=CONTENT_STYLE),

    # content will be rendered in this element
    html.Div(id='page-content', style=CONTENT_STYLE),

    
])

@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/fig1':
        return dcc.Graph(
            id='example-graph',
            figure=fig
        )
    if pathname == '/fig2':
        return dcc.Graph(
            id='example-graph',
            figure=fig2
        )
    
    if pathname == '/dashboard':
        return dashboard.layout


if __name__ == '__main__':
    app.run_server(debug=True)