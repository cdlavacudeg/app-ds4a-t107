from dash import Dash, html, dcc, html, callback, Input, Output

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

app.layout = html.Div(children=[
    # represents the browser address bar and doesn't render anything
    dcc.Location(id='url', refresh=False),
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
     dcc.Link('Navigate to "/fig1"', href='/fig1'),
    html.Br(),
    dcc.Link('Navigate to "/fig2"', href='/fig2'),

    # content will be rendered in this element
    html.Div(id='page-content'),

    
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


if __name__ == '__main__':
    app.run_server(debug=True)