import pandas as pd
import plotly_express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

# Fuente de Datos
df_poblacion=pd.read_csv("population_total.csv")

#Limpieza de Datos (Valores nulos)
df_poblacion=df_poblacion.dropna()

#Transformación de Datos
#Filtro para el año 2020
df=df_poblacion[df_poblacion["year"].isin([2020])]
#Filtro para los paises 'United States', 'India', 'China','Indonesia', 'Brazil’
paises=['United States', 'India', 'China','Indonesia', 'Brazil']
df=df[df["country"].isin(paises)]
#agrupación por país sumando la población
df=df.groupby("country")["population"].sum().reset_index()

#Filtro para los paises 'United States', 'India', 'China','Indonesia', 'Brazil’ sin filtrar año
paises=['United States', 'India', 'China','Indonesia', 'Brazil']
df1=df_poblacion[df_poblacion["country"].isin(paises)]

#Visualizaciones
#Gráfico de columnas
fig_barra=px.bar(df,x="country",y="population",barmode="group",title="Gráfico de Columnas")
#Gráfico de barras
fig_barrah=px.bar(df,y="country",x="population",title="Gráfico de Barras",orientation="h")
#Gráfico de torta
fig_torta=px.pie(df,values="population",names="country",title="Gráfico de Torta")
#Gráfico de líneas
fig_linea=px.line(df1,x="year",y="population",color="country",title="Gráfico de Linea")

#Generación de tableros

app=dash.Dash(__name__)

app.layout= html.Div(children=[
            html.H1("Tableros Población"),
            html.Div(),

            dcc.Graph(
                    id="ejemplo-columna",
                    figure=fig_barra
                ),
            
            dcc.Graph(
                    id="ejemplo-barra",
                    figure=fig_barrah
                ),

            dcc.Graph(
                    id="ejemplo-torta",
                    figure=fig_torta
                ),

            dcc.Graph(
                    id="ejemplo-lineas",
                    figure=fig_linea
                )
            
    ])

if __name__=="__main__":
    app.run(debug=False)


    




                 




        


    


