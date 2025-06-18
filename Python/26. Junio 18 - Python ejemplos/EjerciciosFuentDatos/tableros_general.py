import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Fuente de Datos
df_poblacion = pd.read_csv('C:\\tableros\\population_total.csv')

# Eliminar Valores nulos
df_poblacion = df_poblacion.dropna()
#print(df)

# Filtrar datos para el año 2020
df =df_poblacion[df_poblacion["year"].isin([2020])]
df=df.reset_index()
#print(df)


# Agrupar Datos( Por  producto)
df = df.groupby('country')['population'].sum().reset_index()
#print(df)

# Filtrar solo algunos países
paises = ['United States', 'India', 'China','Indonesia', 'Brazil']
df =df[df["country"].isin(paises)]
#print(df)


# Filtrar un solo  países sin filtrar el año
paises = ['United States', 'India', 'China','Indonesia', 'Brazil']
df1 =df_poblacion[df_poblacion["country"].isin(paises)]
#print(df1)


#Generar las visualizaciones

#Gráfico de columnas para el año 2020 de determinados páises
fig_barra=px.bar(df,x="country",y="population",barmode="group",title='Gráfico de Columnas')
#Gráfico de barras para el año 2020 de determinados páises
fig_barrah=px.bar(df,y="country",x="population",title='Gráfico de Barras',orientation="h")
#Gráfico de torta para el año 2020 de determinados páises
fig_torta=px.pie(df,values='population', names='country', title='Gráfico de tortas')
# Grpafico de líneas para determinados paises de todos los años
fig_lineas=px.line(df1, x="year", y="population",color='country', title='Gráfico de Lineas')

# Generación del tablero
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Tableros Población'),
    html.Div(children='''Tableros'''),
    
    dcc.Graph(
        id='ejemplo-columna',
        figure=fig_barra
    ),

    dcc.Graph(
        id='ejemplo-barra',
        figure=fig_barrah
    ),
    
     dcc.Graph(
        id='ejemplo-torta',
        figure=fig_torta
    ),

    dcc.Graph(
        id='ejemplo-lineas',
        figure=fig_lineas
    )  
])

if __name__ == '__main__':
    app.run_server(debug=True)

