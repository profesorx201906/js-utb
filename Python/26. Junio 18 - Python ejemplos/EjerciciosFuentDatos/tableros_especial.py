import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


# Fuente de Datos
df_poblacion = pd.read_csv('population_total.csv')

# Eliminar Valores nulos
df_poblacion = df_poblacion.dropna()
#print(df)

# Filtrar solo algunos países
paises = ['United States', 'India', 'China','Indonesia', 'Brazil']
df =df_poblacion[df_poblacion["country"].isin(paises)]
#print(df)

#Filtrar solo algunos años
annos=[1980, 1990, 2000, 2010, 2020]
df =df[df["year"].isin(annos)]
#print(df)


#Generación visualización
#Gráfico de columnas con varias series (Años y Páises)
fig_barra=px.bar(df,x="year",y="population",barmode="group",color="country",title='Gráfico de Columnas')

#Generación del tablero
#app = dash.Dash(__name__)
app= dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1('Tableros Población'),
    html.Div(),
    
    dcc.Graph(
        id='ejemplo-columnas',
        figure=fig_barra
    )
    
])

if __name__ == '__main__':
#if __name__ == '__main__':
    app.run(debug=False)

