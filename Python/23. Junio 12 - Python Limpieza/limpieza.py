import limpiar as lp
import numpy as np
import pandas as pd
import os

ruta = os.path.join(os.path.dirname(__file__))


lp.limpiar_pantalla()

# Cargar la data
df = pd.read_excel(f"{ruta}\mercado_casa.xlsx", sheet_name="Datos")
print("Data de mercado casa")
print(df)

print("Digite tecla para continuar")
input()
lp.limpiar_pantalla()
# elimniar datos nulos (todos los datos de la fila o registro deben ser nulos)

print("Eliminando valores nulos de la tabla (registros completos)")
df_sin_nulos = df.dropna(how="all")
print("Data original")
print(df)
print("Data Modificada")
print(df_sin_nulos)
print("Digite tecla para continuar")
input()
lp.limpiar_pantalla()
# elimniar datos nulos donde haya uno

print("Eliminando valores nulos de la tabla ")
print("Data original")
print(df)
print("Data Modificada")
df_sin_nulos = df.dropna()
print(df_sin_nulos)
print("Digite tecla para continuar")
input()

lp.limpiar_pantalla()
#reemplazar valores nulos por un dato en particular
print("reemplazar valores nulos por un dato en particular")
print("Data original")
print(df)
print("Data Modificada")
df_cambio_valores = df.dropna(how="all")
df_cambio_valores = df_cambio_valores.fillna(-1)
print(df_cambio_valores)
print("Digite tecla para continuar")
input()

lp.limpiar_pantalla()
#Eliminar duplicados
print("Eliminar duplicados")
print("Data original")
print(df)
print("Data Modificada")
df_sin_duplicados = df.drop_duplicates()
print(df_sin_duplicados)
print("Digite tecla para continuar")
input()

lp.limpiar_pantalla()
#Eliminar duplicados por columna
print("Eliminar duplicados por columna")
print("Data original")
print(df)
print("Data Modificada")
df_sin_duplicados = df.drop_duplicates(subset="Frutas")
print(df_sin_duplicados)
print("Digite tecla para continuar")
input()

lp.limpiar_pantalla()
#Eliminar valores outliers(eliminandolos) (tomando el cuartil superios)
print("Eliminar valores outliers(eliminandolos) (tomando el cuartil superios)")
print("Data original")
df = pd.read_excel(f"{ruta}\mercado_casa.xlsx", sheet_name="Datos1")
print(df)
limiteSuperior = df["Carnes"].quantile(0.95)
df_sin_outliers=df[df["Carnes"]<limiteSuperior]
print("Data Modificada")
print(df_sin_outliers)
print("Digite tecla para continuar")
input()

lp.limpiar_pantalla()
#Eliminar valores outliers(eliminandolos) (tomando el cuartil inferior)
print("Eliminar valores outliers(eliminandolos) (tomando el cuartil inferior)")
print("Data original")
df = pd.read_excel(f"{ruta}\mercado_casa.xlsx", sheet_name="Datos1")
print(df_sin_outliers)
limiteInferior = df["Carnes"].quantile(0.05)
df_sin_outliers=df_sin_outliers[df_sin_outliers["Carnes"]>limiteInferior]
print("Data Modificada")
print(df_sin_outliers)
