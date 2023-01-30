# file app.py
from dash import Dash, html, dcc
import plotly.graph_objects as go

app = Dash(__name__)

xs = list(range(30))
ys = [10000 * 1.07**i for i in xs]

fig = go.Figure(data=go.Scatter(x=xs, y=ys))
fig.update_layout(xaxis_title='Years', yaxis_title='$')


app.layout = html.Div(children=[
    html.H1(children='Assets'),
    dcc.Graph(figure=fig)])


if __name__ == '__main__':
    app.run_server(debug=True)
