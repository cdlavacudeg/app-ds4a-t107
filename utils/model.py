import plotly.graph_objects as go

def renderFigure(value):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",  # "gauge+number+delta",
            value=value,
            number={"font":{"color":"#3d3c37","size":160}},
            domain={"x": [0, 1], "y": [0, 1]},
            #title={"text": "Risk Factor", "font": {"size": 50}},
            # delta = {'reference': 250, 'increasing': {'color': "RebeccaPurple"}},
            gauge={
                "axis": {
                    "range": [None, 100],
                    "tickwidth": 1,
                    "tickcolor": "#525150",
                    "tickfont": {"color":"#3d3c37"},
                },
                "bar": {"color": "#3d3c37"},
                "bgcolor": "white",
                "borderwidth": 1,
                "bordercolor": "#3d3c37",
                "steps": [
                    {"range": [0, 33], "color": "#1efc35"},
                    {"range": [33, 66], "color": "#fcdb1e"},
                    {"range": [66, 100], "color": "#fc351e"},
                ],
            },
        )
    )

    fig.update_layout(
        paper_bgcolor="#f1f5f8", font={"color": "#135ea4", "family": "sans-serif"}
    )
    return fig
