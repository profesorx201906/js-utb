import numpy as np
import pandas as pd
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

ruta = os.path.join(os.path.dirname(__file__))



df_poblacion = pd.read_csv(f"{ruta}/population_total.csv")

#limpieza y transformacion
#eliminar valores nulos
df_poblacion=df_poblacion.dropna()

#filtra paises
paises = ["United States","India","China","Indonesia","Brazil"]
df = df_poblacion[df_poblacion["country"].isin(paises)]

#filtrar por años
anno=[2000,2010,2020]
df =df[df["year"].isin(anno)]

#crear grafica de barras
graf_barras= px.bar(df,x="year",y="population",barmode="group",color="country",title="Gráfico de barras")

app = dash.Dash(__name__)

app.layout =html.Div([
    html.H1(children="Tableros población"),
    html.Div(children="Tableros"),
    dcc.Graph(id="Ejemplo Columnas",figure=graf_barras)
])

if __name__ == "__main__":
    app.run(debug=False)