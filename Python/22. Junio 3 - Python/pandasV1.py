import pandas as pd
import sys

# Configurar la codificación de la salida
sys.stdout.reconfigure(encoding="utf-8")

df = pd.read_csv("Python/22. Junio 3 - Python/colesterol.csv", encoding="utf-8")
print("Datos population total cargando csv")
print(df)

dfExcel = pd.read_excel(
    "Python/22. Junio 3 - Python/Mercado_casa.xlsx", sheet_name="Datos1"
)
print("Datos mercado casa desde excel")
print(dfExcel)
print("*" * 20)
# acceso a elemento por filas y columnas método iloc
print(dfExcel.iloc[0, 2])
print(dfExcel.iloc[4, 3])
print("*" * 20)

# Acceder a una lista de filas y columnas colocando un arreglo en cada posición (filas y columnas)
print(dfExcel.iloc[[0, 1, 2], [0, 1, 6]])
print("*" * 20)

# primeras filas y primeras columnas hasta el valor ingresado
print("primeras filas y columnas")
print(dfExcel.iloc[2:6, 2:5])
print("*" * 20)


# acceder a los elementos de una fila en particular
print(dfExcel.iloc[5])


# imprimir un numero de registros espeficicos
print(df.head())


# acceder por medio de nombres
print("por fila y columna")
print(dfExcel.loc[4, "Verduras"])
print("por fila y columna con lista (tupla)")
print(dfExcel.loc[:2, ("Verduras", "Lácteos")])

print("por columna")
print(dfExcel["Verduras"])
print(dfExcel.Lácteos)

