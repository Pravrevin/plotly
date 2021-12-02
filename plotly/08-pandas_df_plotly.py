import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('insurance.csv')
# print(df.head())
app = dash.Dash()

# x_rand = np.random.randint(1,61,60)
# y_rand = np.random.randint(1,61,60)

app.layout = html.Div([
    dcc.Graph(
        id = 'ScatterChart',
        figure={
            'data' : [
                go.Scatter(
                    x=df['age'],
                    y=df['charges'],
                    mode='markers'
                )
            ],
            'layout' : go.Layout(
                title = 'Scatter Plots',
                xaxis = {'title':'Age'},
                yaxis = {'title':'Charges'},
                hovermode='closest'
            )
        }
    )

])

if __name__ == '__main__':
    app.run_server(port=4050)