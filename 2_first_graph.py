import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd

iris = pd.read_csv('data/iris.csv')
iris_plants = iris['Flower'].unique()

app = dash.Dash()

data = [
    go.Scatter(
        x=iris.loc[iris['Flower'] == name]['Sepal Length'],
        y=iris.loc[iris['Flower'] == name]['Sepal Width'],
        mode='markers',
        name=name
    ) for name in iris_plants
]

layout = go.Layout(
    title='Sepal Length and Width',
    xaxis=dict(title='Sepal Length'),
    yaxis=dict(title='Sepal Width'),
    hovermode='closest'
)

app.layout = html.Div(
    [
        html.H1(
            'My First Graph',
            style=dict(
                textAlign='center'
            )
        ),
        dcc.Graph(
            id='scatterplot',
            figure=dict(
                data=data,
                layout=layout
            )
        )
    ]
)

if __name__ == '__main__':
    app.run_server()
