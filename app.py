import dash
import dash_html_components as html
import dash_core_components as dcc
      
app= dash.Dash()

app.layout = html.Div(children=[html.H1(children= 'Ejemplo'),
              html.Div(children= '''Dash: a web based app to show'''),
              dcc.Graph(id='dash_graph',
              figure = {'data': [{ 'x' :[1,2,3,4,5], 'y' : [4,5,6,7,8,9], 'type':'bar', 'name':'bread'},], 
              'layout':{'title': 'dash example' }     
                    
}
)     
                      
                      
                ])

if __name__ == '__main__':
    app.runserver(debug=True)