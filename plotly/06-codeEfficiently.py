import dash
import dash_core_components as dcc
import dash_html_components as html
colors = {
    'text' : '#ff0000',
    'plot_color' : '#D3D3D3',
    'paper_color' : '#00ffff'
}
app = dash.Dash()
app.layout = html.Div([
    html.H1(children='Genome!!!',
            style={
                'textAlign' :'center',
                'color': colors['text'],
            }),
    html.Div(children='Plotly Tutorial',
             style={
                 'textAlign' : 'center',
                 'color' : colors['text'],
             }),

    dcc.Graph(
        id = 'RevIn Chart',
        figure={
            'data':[
                {'x':[10,20,30],'y':[12,15,50],'type':'bar','name':'FC'},
                {'x':[10,20,30],'y':[120,150,500],'type':'bar','name':'FC2'}
            ],
            'layout':{
                'plot_bgcolor' : colors['plot_color'],
                'paper_bgcolor' : colors['paper_color'],
                'title' : 'BAR Chart',
                'font':{
                    'color':colors['text']
                }
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(port=4050)