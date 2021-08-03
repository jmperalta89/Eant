app = JupyterDash()

app.layout = html.P("Hola mundo!")


if __name__ == "__main__":
  app.run_server(mode ="external")
  
!pip freeze > requirements.txt
import types

def imports(): 
   for name, val in globals().items():
     if isinstance(val, types.ModuleType):
       if val.__name__ !='builtins':
         if val.__name__!='types':
           yield val.__name__
list(imports())
