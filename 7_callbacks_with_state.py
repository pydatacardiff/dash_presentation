import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd


app = dash.Dash()

iris = pd.read_csv('data/iris.csv')
iris_plants = iris['Flower'].unique()

app.layout = html.Div(
    [
        html.H1(
            'Intro to Callbacks',
            style=dict(
                textAlign='center'
            )
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id='xaxis',
                    value='Sepal Length'
                )
            ],
            style=dict(
                width='48%',
                display='inline-block'
            )
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id='yaxis',
                    value='Sepal Width'
                )
            ],
            style=dict(
                width='48%',
                display='inline-block'
            )
        ),
        html.P(
            html.Button(id='input_button',
                        n_clicks=0,
                        children='Submit',
                        style=dict(fontSize=18))

        ),
        dcc.Graph(
            id='scatter_graph'
        )
    ]
)


@app.callback(Output(component_id='xaxis', component_property='options'),
              [Input(component_id='yaxis', component_property='value')])
def update_xaxis(yaxis_value):
    option_dict = [{'label': i, 'value': i} for i in iris.columns[:-1]
                   if i != yaxis_value]
    return option_dict


@app.callback(Output(component_id='yaxis', component_property='options'),
              [Input(component_id='xaxis', component_property='value')])
def update_xaxis(xaxis_value):
    option_dict = [{'label': i, 'value': i} for i in iris.columns[:-1]
                   if i != xaxis_value]
    return option_dict


@app.callback(Output(component_id='scatter_graph', component_property='figure'),
              [Input(component_id='input_button',
                     component_property='n_clicks')],
              [State(component_id='xaxis', component_property='value'),
               State(component_id='yaxis', component_property='value')])
def update_graph(n_clicks, xaxis_name, yaxis_name):
    data = [
        go.Scatter(
            x=iris.loc[iris['Flower'] == name][xaxis_name],
            y=iris.loc[iris['Flower'] == name][yaxis_name],
            name=name,
            mode='markers'
        ) for name in iris_plants
    ]

    layout = go.Layout(
        title='{} and {}. The button has been clicked {} times'.format(
            xaxis_name, yaxis_name, n_clicks),
        xaxis=dict(title=xaxis_name),
        yaxis=dict(title=yaxis_name),
        hovermode='closest'
    )
    return dict(data=data, layout=layout)


if __name__ == '__main__':
    app.run_server()
