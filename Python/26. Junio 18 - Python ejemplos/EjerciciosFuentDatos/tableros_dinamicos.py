import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output

# Fuente de Datos
df = pd.read_csv('Covid19VacunasAgrupadas.csv')


#Generación del tablero
app = dash.Dash(__name__)

app.layout = html.Div([
    
     html.Div([
        html.H1('Vacunados por covid')
    ]),

    html.Div([
        html.Div([
            html.P('Selecciona dosis vacuna', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'dosis', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'Primera Dosis', 'value' : 'primera_dosis'},
                                {'label' : 'Segunda Dosis', 'value' : 'segunda_dosis'}
                            ], value = 'primera_dosis',
                            style = {'text-aling':'center', 'color':'black'}),
        ],  style = {'margin-bottom': '20px'})
    ]),

    html.Div([
        html.Div([
            dcc.Graph(id = 'bar_graph', figure = {})
        ]),

        html.Div([
            dcc.Graph(id = 'pie_graph', figure = {})
        ],)
    ]),

], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})

@app.callback(
    Output('bar_graph', component_property='figure'),
    [Input('dosis', component_property='value')])

def update_graph_bar(value):
    
#Gráfico de barras - con selección de la dosis
    if value == 'primera_dosis':
        fig = px.bar(
            data_frame = df,
            x = 'jurisdiccion_nombre',
            y = 'primera_dosis_cantidad')
    else:
        fig = px.bar(
            data_frame= df,
            x = 'jurisdiccion_nombre',
            y = 'segunda_dosis_cantidad')
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('dosis', component_property='value')])

def update_graph_pie(value):
    
#Gráfico de tortas - con selección de la dosis
    if value == 'primera_dosis':
        fig2 = px.pie(
            data_frame = df,
            names = 'jurisdiccion_nombre',
            values = 'primera_dosis_cantidad')
    else:
        fig2 = px.pie(
            data_frame = df,
            names = 'jurisdiccion_nombre',
            values = 'segunda_dosis_cantidad'
        )
    return fig2



if __name__ == ('__main__'):
    app.run(debug=False)
