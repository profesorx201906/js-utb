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
# elimniar datos nulos (todos los datos de la fila o registro deben ser nulos)

print("Eliminando valores nulos de la tabla (registros completos)")
df_sin_nulos = df.dropna(how="all")
print(df_sin_nulos)
print("Digite tecla para continuar")
input()
