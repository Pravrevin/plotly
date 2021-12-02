import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    html.H1(children='Genome!!!',
            style={
                'textAlign' :'center',
                'color': '#ff0000',
            }),
    html.Div(children='Plotly Tutorial',
             style={
                 'textAlign' : 'center',
                 'color' : '#456FBV',
             }),

    dcc.Graph(
        id = 'RevIn Chart',
        figure={
            'data':[
                {'x':[10,20,30],'y':[12,15,50],'type':'bar','name':'FC'},
                {'x':[10,20,30],'y':[120,150,500],'type':'bar','name':'FC2'}
            ],
            'layout':{
                'title' : 'BAR Chart'
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(port=4050)