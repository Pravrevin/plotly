import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
app = dash.Dash()
#np.random.seed(50)
x_rand = np.random.randint(1,61,60)
y_rand = np.random.randint(1,61,60)

app.layout = html.Div([
    dcc.Graph(
        id = 'ScatterChart',
        figure={
            'data' : [
                go.Scatter(
                    x=x_rand,
                    y=y_rand,
                    mode='markers'
                )
            ],
            'layout' : go.Layout(
                title = 'Scatter Plots',
                xaxis = {'title':'Randam X Values'},
                yaxis = {'title':'Randam Y Values'}
            )
        }
    )

])

if __name__ == '__main__':
    app.run_server(port=4050)