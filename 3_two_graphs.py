import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd

iris = pd.read_csv('data/iris.csv')
iris_plants = iris['Flower'].unique()

app = dash.Dash()

scatter_data = [
    go.Scatter(
        x=iris.loc[iris['Flower'] == name]['Sepal Length'],
        y=iris.loc[iris['Flower'] == name]['Sepal Width'],
        mode='markers',
        name=name
    ) for name in iris_plants
]

scatter_layout = go.Layout(
    title='Sepal Length and Width',
    xaxis=dict(title='Sepal Length'),
    yaxis=dict(title='Sepal Width'),
    hovermode='closest'
)

sepal_lengths = [iris.loc[iris['Flower'] == name]['Sepal Length'].values
                 for name in iris_plants]

dist_fig = ff.create_distplot(sepal_lengths, iris_plants, bin_size=0.2)
dist_fig['layout']['title'] = 'Sepal Length Distributions'

for hist in dist_fig['data']:
    hist['marker']['line'] = dict(width=1, color='white')

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
                data=scatter_data,
                layout=scatter_layout
            )
        ),
        dcc.Graph(
            id='distplot',
            figure=dist_fig
        )
    ]
)

if __name__ == '__main__':
    app.run_server()
