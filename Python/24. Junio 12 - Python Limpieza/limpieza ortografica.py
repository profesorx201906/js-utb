import limpiar as lp
import numpy as np
import pandas as pd
import os

ruta = os.path.join(os.path.dirname(__file__))


lp.limpiar_pantalla()

# Cargar la data
df = pd.read_excel(f"{ruta}\LimpiezaOrtografia.xlsx", sheet_name="Datos")
print("Limpieza Ortográfica - Data original")
print(df)

print("convertir a tipo título (inicial en mayúscula) las columnas nombre y ciudad")
df["Nombre"] = df["Nombre"].str.title()
df["Ciudad"] = df["Ciudad"].str.title()
print(df)

print("Presione tecla para continuar")
input()
lp.limpiar_pantalla()
print("Data original")
print(df)
# Agrupar
print("AGrupar por ciudad")
df_grupo_ciudad = df.groupby("Ciudad").ValorFactura.sum().reset_index()
print(df_grupo_ciudad)

print("Presione tecla para continuar")
input()
lp.limpiar_pantalla()
print("Data original")
print(df)
# Agrupar
print("corregir nombres")
df.replace({"Ciudad": {"Bogota": "Bogotá", "Medellin": "Medellín"}}, inplace=True)
print(df)

print("AGrupar por ciudad")
df_grupo_ciudad = df.groupby("Ciudad").ValorFactura.sum().reset_index()
print(df_grupo_ciudad)
