import limpiar as lp
import numpy as np
import pandas as pd
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

ruta = os.path.join(os.path.dirname(__file__))


lp.limpiar_pantalla()
df_poblacion = pd.read_csv(f"{ruta}/population_total.csv")
print(df_poblacion)

# limpieza
# Eliminar valores nulos
df_poblacion = df_poblacion.dropna()
# filtrar información por año 2020
df = df_poblacion[df_poblacion["year"] > 2000]
df = df.reset_index()
# Agrupar datos por pais
df = df.groupby("country")["population"].sum().reset_index()
# filtro por paises
paises = ["United States", "India", "China", "Indonesia", "Brazil"]
df = df[df["country"].isin(paises)]
# visualizar dt transformado
print(
    "data frame transformado año 2020, paises United States, India, China, Indonesia, Brazil"
)
print(df)
print("presione tecla para continuar")
input()
lp.limpiar_pantalla()
# Datos a visualizar
print(df)
grafica_barras = px.bar(
    df, x="country", y="population", barmode="group", title="Gráfico de Columnas"
)
# grafica_barras.show()


grafica_barrasH = px.bar(
    df,
    y="country",
    x="population",
    barmode="group",
    title="Gráfico de Columnas Horizontales",
    orientation="h" "",
)
# grafica_barrasH.show()

grafica_torta = px.pie(
    df, values="population", names="country", title="Gráfico de tortas"
)
# grafica_torta.show()


df = df_poblacion[df_poblacion["year"] > 2000]
df = df.reset_index()
# Agrupar datos por pais
df = df.groupby(["country", "year"])["population"].sum().reset_index()
# filtro por paises
paises = ["United States", "India", "China", "Indonesia", "Brazil"]
df = df[df["country"].isin(paises)]
grafica_lineas = px.line(
    df, x="year", y="population", color="country", title="Gráfico de lineas"
)
# grafica_lineas.show()

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Tableros Población"),
        html.Div(children="Tableros"),
        html.Table(),
        dcc.Graph(id="Ejemplo Columna", figure=grafica_barras),
        dcc.Graph(id="Ejemplo barra", figure=grafica_barrasH),
        dcc.Graph(id="Ejemplo Torta", figure=grafica_torta),
        dcc.Graph(id="Ejemplo Lineas", figure=grafica_lineas),
    ]
)

if __name__ == "__main__":
    app.run(debug=False)
