import pandas as pd
import numpy as np
import limpiar as lp
import sys

lp.limpiar_pantalla()
# Configurar la codificación de la salida
sys.stdout.reconfigure(encoding="utf-8")

dfExcel = pd.read_excel(
    "Python/22. Junio 3 - Python/Mercado_casa.xlsx", sheet_name="Datos1"
)

print(dfExcel)

# eliminar una columna lácteos
print("eliminar columna lácteos")
dfExcel = dfExcel.drop(columns=["Lácteos"])
print(dfExcel)

# elimniar una fila 4
print("eliminar fila 4")
dfExcel = dfExcel.drop(4)
print(dfExcel)

# sumar una columna por ejemplo carnes
print("suma de una columna")
suma_carnes = dfExcel["Carnes"].sum()
print(suma_carnes)

# promedio una columna por ejemplo Verduras
print("promedio de una columna")
Promedio_Verduras = dfExcel["Verduras"].mean()
print(Promedio_Verduras)

# sumar dos columnas en otra
print("sumar dos columnas")
dfExcel["Suma F y V"] = dfExcel["Frutas"] + dfExcel["Verduras"]
print(dfExcel)

# crear columna con condicional
print("verduras con valor menor a 80000")
dfExcel["V<80000"] = np.where(dfExcel["Verduras"] < 80000, "Menor", "Mayor")
print(dfExcel)

# aumentar el valor de las carnes en un 10%
print("aumentar el valor de las carnes en un 10%")
dfExcel["Carnes"] = dfExcel["Carnes"] * 1.1
print(dfExcel)
