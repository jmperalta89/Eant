# -*- coding: utf-8 -*-
"""PRUEBA PARA JUPYTER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14B5yemIxh1FcP4W-xSORDQ6EY0iFWoxa
"""

import pandas as pd

indices = [['uno','dos','tres']]
values =  [['1','2','3']]
nueva_tabla = pd.DataFrame( { 'NUMEROS':indices, 'VALORES': values})
nueva_tabla

!pip freeze > requirements.txt
import types

def imports():
  for name, val in globals().items():
    if isinstance(val, types.ModuleType):
      if val.__name__ !='builtins':
        if val.__name__!='types':
          yield val.__name__
list(imports())