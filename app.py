# -*- coding: utf-8 -*-
"""Copy of Copia_de_EANT_Clase_Dash_Intro_Clase (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dE944z165LGzP0RARc9FPpX41oH2oX3b
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

app = JupyterDash()

app.layout = html.P("Hola mundo!")


if __name__ == "__main__":
  app.run_server(mode ="external")