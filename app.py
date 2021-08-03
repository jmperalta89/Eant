app = JupyterDash()

app.layout = html.P("Hola mundo!")


if __name__ == "__main__":
  app.run_server(mode ="external")

