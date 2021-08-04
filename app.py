
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

