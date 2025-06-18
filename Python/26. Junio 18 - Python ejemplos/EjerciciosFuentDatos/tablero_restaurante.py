# Paso 1: Conexión con la fuente de datos (Archivo en Excel)
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import os
#Leer archivo excel e impirmir las primeras 5 filas
ruta = os.path.join(os.path.dirname(__file__))
df_fuente = pd.read_excel(f'{ruta}/CasoEstudioRestauranteDatos.xlsx', sheet_name='Datos')

# Paso 2: Limpieza de datos (Valores Nulos)
df=df_fuente.dropna()

# Paso 2: Limpieza de datos (Valores Duplicados)
df=df.drop_duplicates()



# Paso 3: Transformaciones - Visualizaciones

# Ventas en el tiempo
# Crear columnas con solo el año y el mes
df["Mes"]=df["Fecha"].dt.strftime("%Y-%m") 
# Tranformación: agrupación por fecha
df1 = df.groupby('Mes').Precio.sum().reset_index()
# Gráfico de líneas para las ventas en el tiempo
fig_lineas=px.line(df1, x="Mes", y="Precio", title='Tendencia de ventas')

# Ventas en el tiempo por tipo de bebida
# Tranformación: agrupación por fecha y tipo producto
df2 = df.groupby(['Mes','Tipo']).Precio.sum().reset_index()
# Gráfico de líneas para las ventas en el tiempo por tipo bebida
fig_lineas_1=px.line(df2, x="Mes", y="Precio",color="Tipo", title='Ventas por tipo producto')

# Ventas en el tiempo por categorá
# Filtrar: Solo seleccionar el tipo de Bebidas 
df3=df[df["Tipo"]=="Bebida"]
# Tranformación: agrupación por fecha y tipo producto
df4 = df3.groupby(['Mes','Categoria']).Precio.sum().reset_index()
# Gráfico de líneas para las ventas en el tiempo por tipo bebida
fig_lineas_2=px.line(df4, x="Mes", y="Precio",color="Categoria", title='Ventas por Categorias (Bebidas)')

# Ventas en el tiempo por mesero en el tiempo
# Tranformación: agrupación por fecha y tipo producto
df5 = df.groupby(['Mes','Atendió']).Precio.sum().reset_index()
# Gráfico de líneas para las ventas por mesero en el tiempo
fig_lineas_3=px.line(df5, x="Mes", y="Precio",color="Atendió", title='Ventas por mesero en el tiempo')

# Ventasde vino por mesero
# Filtrar: Solo seleccionar la categoría Vinos 
df6=df[df["Categoria"]=="Vinos"]
# Tranformación: agrupación por mesero
df7 = df6.groupby('Atendió').Precio.sum().reset_index()
# Gráfico de Barras para las ventas de Vinos por mesero
fig_barra=px.bar(df7, x="Precio", y="Atendió",orientation="h", title='Ventas de Vino por Mesero')

# Propinas por mesero
# Filtrar: Crear columna ValorPropina=Precio*Propina
df8=df
df8["ValorPropina"]=df8["Precio"]*df8["Propina"]
# Tranformación: agrupación del ValorPropina  por mesero
df9 = df8.groupby('Atendió').ValorPropina.sum().reset_index()
# Gráfico de Columnas  para las propinas por mesero
fig_columna=px.bar(df9, x="Atendió", y="ValorPropina",barmode="group", title='Propinas por Mesero')

# Propinas por mesero
# Gráfico de Torta  para las propinas por mesero
fig_torta=px.pie(df9,values='ValorPropina', names='Atendió', title='Distribución Propinas por Mesero')

# Ventas en el tiempo por tipo cliente
# Tranformación: agrupación por fecha y tipo cliente
df10 = df.groupby(['Mes','Tipo de Cliente']).Precio.sum().reset_index()
# Gráfico de líneas para las ventas en el tiempo por tipo cliente
fig_lineas_4=px.line(df10, x="Mes", y="Precio",color="Tipo de Cliente", title='Ventas por tipo cliente')

# Ventas de Vinos en el tiempo por tipo de cliente
# Filtrar: Solo seleccionar Vinos 
df11=df[df["Categoria"]=="Vinos"]
# Tranformación: agrupación por fecha y tipo producto
df12 = df11.groupby(['Mes','Tipo de Cliente']).Precio.sum().reset_index()
# Gráfico de líneas para las ventas de Vinos en el tiempo por tipo de Cliente
fig_lineas_5=px.line(df12, x="Mes", y="Precio",color="Tipo de Cliente", title='Ventas Vinos por Tipo de Cientes')

# Ventas por mesero por tipo de Cliente
# Tranformación: agrupación por mesero y Tipo de Cliente
df13 = df.groupby(['Atendió','Tipo de Cliente']).Precio.sum().reset_index()
# Gráfico de Columnas  para ventas por mesero por tipo de cliente
fig_columna_1=px.bar(df13, x="Atendió", y="Precio",barmode="group",color="Tipo de Cliente", title='Ventas por Mesero y Tipo Cliente')

# Generación del tablero
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Tableros Restaurante'),
    html.Div(),
    
    dcc.Graph(
        id='grafico1',
        figure=fig_lineas
    ),

    dcc.Graph(
        id='grafico2',
        figure=fig_lineas_1
    ),
    
     dcc.Graph(
        id='grafico3',
        figure=fig_lineas_2
    ),

    dcc.Graph(
        id='grafico4',
        figure=fig_lineas_3
    ),

    dcc.Graph(
        id='grafico5',
        figure=fig_barra
    ),

    dcc.Graph(
        id='grafico6',
        figure=fig_columna
    ),

    dcc.Graph(
        id='grafico7',
        figure=fig_torta
    ),

    dcc.Graph(
        id='grafico8',
        figure=fig_lineas_4
    ),

    dcc.Graph(
        id='grafico9',
        figure=fig_lineas_5
    ),

    dcc.Graph(
        id='grafico10',
        figure=fig_columna_1
    )  
])

if __name__ == '__main__':
    app.run(debug=False)





