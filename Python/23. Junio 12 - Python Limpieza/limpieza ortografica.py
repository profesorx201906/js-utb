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
df["Nombre"]=df["Nombre"].str.title()
df["Ciudad"]=df["Ciudad"].str.title()
print(df)


lp.limpiar_pantalla()

# Cargar la data
df = pd.read_excel(f"{ruta}\LimpiezaOrtografia.xlsx", sheet_name="Datos")
print("Limpieza Ortográfica - Data original")
print(df)

print("convertir a tipo título (inicial en mayúscula) las columnas nombre y ciudad")
df["Nombre"]=df["Nombre"].str.title()
df["Ciudad"]=df["Ciudad"].str.title()
print(df)


