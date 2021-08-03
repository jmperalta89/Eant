# -*- coding: utf-8 -*-
"""Copia_de_EANT_Clase_Dash_Intro_Clase (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MQRqd-4msCe6FfNYdjW_mi_SOyhN8B-d

<img src="https://eant.tech/imagenes/logo.png" width=25% height=80%  >

### <img src="http://icons.iconarchive.com/icons/cornmanthe3rd/plex/256/Other-python-icon.png" width="40"> Dashboards en python 📊

En la clase de hoy vamos a utilizar dash para crear dashboards en python. Para utilizar [dash](https://plotly.com/dash/), existe una versión adaptada para utilizar en jupyter (JupyterDash) que es la que estaremos utilizando  en la clase. 

<center>

![](https://tylertech.plotly.com/assets/plotly-dash-logo.png)

</center>

## Librerías
"""

# Instalación
!pip install jupyter-dash
!pip install dash
!pip install dash_core_components
!pip install dash_html_components
!pip install dash_table

import pandas as pd
import numpy as np

# import dash
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State
import dash_table

import plotly.express as px

#Ports disponibles localmente: 8124,8125,8126, 8050
 #app._terminate_server_for_port("localhost", 8124)

"""# 2. Dash - Estructura básica
Arrancamos creando el dash más simple:

✏️ **Ejercicio  1**: Construir un dash que incluya un componente html.P que diga 'Hola mundo!'
"""

app = JupyterDash()

app.layout = html.P("Hola mundo!")


if __name__ == "__main__":
  app.run_server(mode ="external")

app = JupyterDash()

app.layout = html.Div(children=[html.H1(children= 'Ejemplo'),
              html.Div(children= '''Dash: a web based app to show'''),
              dcc.Graph(id='dash_graph',
              figure = {'data': [{ 'x' :[1,2,3,4,5], 'y' : [4,5,6,7,8,9], 'type':'bar', 'name':'bread'},], 
              'layout':{'title': 'dash example' }     
                    
}
)     
                      
                      
                ])

if __name__ == '__main__':
    app.run_server(debug=True)



"""✏️ **Ejercicio 2** Añadir distintos componentes html para ver cómo se ven en el dash: H1, H2, H3, H4, H5, H6, P"""

app = JupyterDash()

app.layout = html.Div(children= [ 
                                 html.H1("Hola mundo!"),
                                 html.H2("Hola mundo!"),
                                 html.H3("Hola mundo!"),
                                 html.H4("Hola mundo!"),
                                 html.H5("Hola mundo!"),
                                 html.H6("Hola mundo!"),
                                 html.P("Hola mundo!")])


if __name__ == "__main__":
  app.run_server(mode = "external")

"""✏️ **Ejercicio 3**: Añadir divs adentro de divs para generar una estructura más organizadas. 
* Primer div: título del dashboard
* Segundo div: Descripción del dashboard
* Tercer div: html.Iframe, que nos permite incluir un video de youtube dentro de nuestro dashboard (utilizando el parámetro src=url del video)
   * **URL:** https://www.youtube.com/embed/BxV14h0kFs0
"""

app = JupyterDash()

app.layout = html.Div(children= [ 
                                 html.Div(html.H1("Mi primer Dash en Python")),
                                 html.Div(html.P("Este Dash lo realizamos con plotly")),
                                 html.Div(html.Iframe( src = "https://www.youtube.com/embed/BxV14h0kFs0"))
])

if __name__ == "__main__":
  app.run_server(mode = "external")

"""# 3. Dash - dash core componets - Gráficos

✏️ **Ejercicio 4**: Generar una app que incluya un componente dcc.Graph, definiendo el id de este componente como 'grafico_1' y la figure=figura_1.

✏️ **4.1** Para lo cual es necesario generar un dataframe denominado **df_filt** que tenga los datos del año 2007 y las columnas 'country','continent','lifeExp', 'gdpPercap', 'pop'.

✏️ **4.2** Posteriormente generar un scatterplot donde:
* x="lifeExp", 
* y="gdpPercap", 
* color='pop',
* size='pop',
* labels: 
  * 'lifeExp':'Exp de vida', 
  * 'gdpPercap':'Pbi per cápita', 
  * 'pop':'Población'
"""

df = px.data.gapminder()
df_filt = df.loc[df.year == 2007, ['country','continent','lifeExp', 'gdpPercap', 'pop']]
df_filt.head(2)

figura_1 = px.scatter(data_frame= df_filt,  x="lifeExp",
y="gdpPercap",
color='pop',
size='pop',
labels = {'lifeExp':'Exp de vida',
'gdpPercap':'Pbi per cápita',
'pop':'Población'})

figura_1.show()

app = JupyterDash()

app.layout = html.Div(children= [ 
                                 html.Div(html.H1("Mi primer Dash en Python")),
                                 html.Div(html.P("Este Dash lo realizamos con plotly")),
                                 dcc.Graph(id = "Grafico_1", figure = figura_1 )
])

if __name__ == "__main__":
  app.run_server(mode = "external")

"""# 4. Dash - dash core componets - Botones

## Dropdown

✏️ **Ejercicio 5**: Generar un Dropdown que permita seleccionar entre dos alternativas: Americas o Europe. Americas y Europe son los valores mientras que los labels deben ser América y Europa.
"""

app = JupyterDash()

app.layout = html.Div(children= [ 
                                 html.Div(html.H1("Mi primer Dash en Python")),
                                 html.Div(html.P("Este Dash lo realizamos con plotly")),
                                 dcc.Dropdown(id = "dropdown", options= [{"label": "Europa", "value": "Europe"},
                                                                         {"label": "América", "value": "Americas"}],
                                              value = "Americas", multi = False ),
                                 dcc.Graph(id = "Grafico_1", figure = figura_1 )
])

if __name__ == "__main__":
  app.run_server(mode = "external")

"""## Radio items

✏️ **Ejercicio 6**: Generar un RadioItems que permita seleccionar entre dos alternativas: Americas o Europe. Americas y Europe son los valores mientras que los labels deben ser América y Europa.
"""

app = JupyterDash()

app.layout = html.Div(children= [ 
                                 html.Div(html.H1("Mi primer Dash en Python")),
                                 html.Div(html.P("Este Dash lo realizamos con plotly")),
                                 dcc.RadioItems(id = "dropdown", options= [{"label": "Europa", "value": "Europe"},
                                                                         {"label": "América", "value": "Americas"}],
                                              value = "Americas" ),
                                 dcc.Graph(id = "Grafico_1", figure = figura_1 )
])

if __name__ == "__main__":
  app.run_server(mode = "external")

"""# 5. Dash - Callbacks 

Qué ocurre al tocar los botones que generamos en el punto anterior:

✏️ **Ejercicio 7**: En el dash del punto 12, generar una función callback que ante el Input (selección del valor del dropdown), genere un Output (cambie el texto de children en el html.Div).
"""

app = JupyterDash()

app.layout = html.Div(children= [ 
                                 html.Div(html.H1("Mi primer Dash en Python")),
                                 html.Div(html.P("Este Dash lo realizamos con plotly")),
                                 dcc.Dropdown(id = "dropdown", options= [{"label": "Europa", "value": "Europe"},
                                                                         {"label": "América", "value": "Americas"}],
                                              value = "Americas", multi = False ),
                                 html.Br(),
                                 html.Div(id = "Continent", children= "Continente seleccionado:"),
                                 dcc.Graph(id = "Grafico_1", figure = figura_1 )])

@app.callback(
    Output(component_id= "Continent", component_property= "children"),
    Input(component_id = "dropdown", component_property = "value" ))

def update_dropdown(select_value):
  return "El continente seleccionado es:" + select_value

if __name__ == "__main__":
  app.run_server(mode = "external")

"""✏️ **Ejercicio 8:** En el dash del punto anterior modificar para tener un dropdown multiple, que su valor inicial sea Americas.
Asimismo cuando seleciona un pais que retorne los valores seleccionados y cambie el texto de children en el html.Div
"""

app = JupyterDash()

app.layout = html.Div(children= [ 
                                 html.Div(html.H1("Mi primer Dash en Python")),
                                 html.Div(html.P("Este Dash lo realizamos con plotly")),
                                 dcc.Dropdown(id = "dropdown", options= [{"label": "Europa", "value": "Europe"},
                                                                         {"label": "América", "value": "Americas"}],
                                              value = ["Americas"], multi = True ),
                                 html.Br(),
                                 html.Div(id = "Continent", children= "Continente seleccionado:"),
                                 dcc.Graph(id = "Grafico_1", figure = figura_1 )])

@app.callback(
    Output(component_id= "Continent", component_property= "children"),
    Input(component_id = "dropdown", component_property = "value" ))

def update_output_dropdown(select_value):
  if len(select_value) == 1:
    return "El continente seleccionado es:" + select_value[0]
  elif len(select_value) == 2:
    return "Los continentes seleccionados son:" + select_value[0]+ "y" +select_value[1]
  else:
    return "No hay valores seleccionados"

if __name__ == "__main__":
  app.run_server(mode = "external")

"""✏️ **Ejercicio 9:** En el dash del punto anterior modificar que el dropdown tabmien modifique el grafico en base al valor seleccionado."""

app = JupyterDash()

app.layout = html.Div(children= [ 
                                 html.Div(html.H1("Mi primer Dash en Python")),
                                 html.Div(html.P("Este Dash lo realizamos con plotly")),
                                 dcc.Dropdown(id = "dropdown", options= [{"label": "Europa", "value": "Europe"},
                                                                         {"label": "América", "value": "Americas"}],
                                              value = ["Americas"], multi = True ),
                                 html.Br(),
                                 html.Div(id = "Continent", children= "Continente seleccionado:"),
                                 dcc.Graph(id = "Grafico_1", figure = figura_1 )])

@app.callback(
    Output(component_id= "Continent", component_property= "children"),
    Input(component_id = "dropdown", component_property = "value" ))

def update_output_dropdown(select_value):
  if len(select_value) == 1:
    return "El continente seleccionado es:" + select_value[0]
  elif len(select_value) == 2:
    return "Los continentes seleccionados son:" + select_value[0]+ "y" +select_value[1]
  else:
    return "No hay valores seleccionados"


@app.callback(
    Output(component_id= "Grafico_1", component_property= "figure"),
    Input(component_id = "dropdown", component_property = "value" ))

def update_grafico(select_value):
  figura_1 = px.scatter(data_frame= df_filt.loc[df_filt["continent"].isin(select_value),:],  x="lifeExp",
  y="gdpPercap",
  color='pop',
  size='pop',
  labels = {'lifeExp':'Exp de vida',
  'gdpPercap':'Pbi per cápita',
  'pop':'Población'})
  return figura_1


if __name__ == "__main__":
  app.run_server(mode = "external")

"""# 5. Dash - Datatables

✏️ **Ejercicio 10**: convertir df_filt a una lista de diccionarios para cada fila utilizando to_dict('records')
"""

data_table=df_filt.to_dict('records')

data_table[:2]

"""✏️ **Ejercicio 11**: Generar una lista de diccionarios con el siguiente formato: 

    [{'name': Nombre de la variable como queremos que aparezca , 'id': Nombre de la variable en el dataframe}]
        
"""

[{'name':i,'id':i} for i in df_filt.columns]

"""✏️ **Ejercicio 12**: Generar un dash que incluya una dash_table.DataTable. Este datatable debe tener:
* style_header={'backgroundColor': 'steelblue', 'color':'white'},
* style_cell={'backgroundColor': 'ghostwhite','color': 'steelblue'},
* filter_action='native', 
* page_current= 0,
* page_size= 10,
"""

app=JupyterDash()

app.layout=html.Div(children=[
    html.Div(html.H1('Mi primer dash')),
    html.Div(html.P('Este dash lo realizamos con plotly')),
    dcc.Dropdown(id='dropdown',
                 options=[
                          {'label':'Europa','value':'Europe'},
                          {'label':'America','value':'Americas'}
                          ],
                 value=['Americas'],
                 multi=True
                 ),
    html.Br(),
    html.Div(id='Continente',children='Seleccionar un continente'),
    dcc.Graph(id='Grafico_1',figure=figura_1),
    dash_table.DataTable(id='tabla',
                         data=data_table,
                         columns=[{'name':i.upper(),'id':i} for i in df_filt.columns],
                         style_header={'backgroundColor': 'steelblue', 'color':'white'},
                         style_cell={'backgroundColor': 'ghostwhite','color': 'steelblue'},
                         filter_action='native',
                         page_current= 0,
                         page_size= 10)
])


@app.callback(
    Output(component_id='Continente',component_property='children'),
    Input(component_id='dropdown'   ,component_property='value')
)
def update_output_dropdown(select_value):
  if len(select_value)==1:
    return 'El continente seleccionado es: '+ select_value[0]
  elif len(select_value)==2:
    return  'Los continentes seleccionados son: '+ select_value[0]+' y '+select_value[1]
  else:
    return 'No hay valores seleccionados'


@app.callback(
    Output(component_id='Grafico_1',component_property='figure'),
    Input(component_id='dropdown',component_property='value')
)
def update_grafico(select_value):
  figure_1=px.scatter(data_frame=df_filt.loc[df_filt['continent'].isin(select_value),:],
            x="lifeExp",
            y="gdpPercap",
            color='pop',
            size='pop',
            hover_name='country',
            labels={'lifeExp':'Exp de vida','gdpPercap':'Pbi per cápita','pop':'Población'}
           )
  return figura_1



if __name__=='__main__':
  app.run_server(mode='external')

"""✏️ **Ejercicio 13:**  Añadir una función callback que tome como Input el valor del dropdown y como Output la data de la tabla, de tal forma que al seleccionar el (o los) continentes la tabla también se modifique."""

app=JupyterDash()

app.layout=html.Div(children=[
    html.Div(html.H1('Mi primer dash')),
    html.Div(html.P('Este dash lo realizamos con plotly')),
    dcc.Dropdown(id='dropdown',
                 options=[
                          {'label':'Europa','value':'Europe'},
                          {'label':'America','value':'Americas'}
                          ],
                 value=['Americas'],
                 multi=True
                 ),
    html.Br(),
    html.Div(id='Continente',children='Seleccionar un continente'),
    dcc.Graph(id='Grafico_1',figure=figura_1),
    dash_table.DataTable(id='tabla',
                         data=data_table,
                         columns=[{'name':i.upper(),'id':i} for i in df_filt.columns],
                         style_header={'backgroundColor': 'steelblue', 'color':'white'},
                         style_cell={'backgroundColor': 'ghostwhite','color': 'steelblue'},
                         filter_action='native',
                         page_current= 0,
                         page_size= 10)
])


@app.callback(
    Output(component_id='Continente',component_property='children'),
    Input(component_id='dropdown'   ,component_property='value')
)
def update_output_dropdown(select_value):
  if len(select_value)==1:
    return 'El continente seleccionado es: '+ select_value[0]
  elif len(select_value)==2:
    return  'Los continentes seleccionados son: '+ select_value[0]+' y '+select_value[1]
  else:
    return 'No hay valores seleccionados'


@app.callback(
    Output(component_id='Grafico_1',component_property='figure'),
    Input(component_id='dropdown',component_property='value')
)
def update_grafico(select_value):
  figure_1=px.scatter(data_frame=df_filt.loc[df_filt['continent'].isin(select_value),:],
            x="lifeExp",
            y="gdpPercap",
            color='pop',
            size='pop',
            hover_name='country',
            labels={'lifeExp':'Exp de vida','gdpPercap':'Pbi per cápita','pop':'Población'}
           )
  return figura_1

@app.callback(
    Output(component_id='tabla' ,component_property='data'),
    Input(component_id='dropdown',component_property='value')
)
def update_datatable(select_value):
  df_filt_new=df_filt.loc[df_filt.continent.isin(select_value),:].to_dict('records')
  return df_filt_new



if __name__=='__main__':
  app.run_server(mode='external')