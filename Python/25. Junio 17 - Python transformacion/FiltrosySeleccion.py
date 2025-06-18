import limpiar as lp
import numpy as np
import pandas as pd

lp.limpiar_pantalla()
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [1, 25, 90]})
print("Información Original")
print(df)
dfFiltrado = df[(df["C"] > 0) & (df["A"] < 3)]
print("Dataframe filtrado")
print(dfFiltrado)
print("Digite tecla para continuar")
input()
lp.limpiar_pantalla()
print("Información Original")
print(df)
print("Método isin (lista de valores)")
lista = [1,2,3]
dfFiltrado=df[df["C"].isin(lista)]
print(dfFiltrado)
print("Digite tecla para continuar")
input()

lp.limpiar_pantalla()
print("Información Original")
print(df)
print("Método between rango de datos")
dfFiltrado=df[df["C"].between(8,100)]
print(dfFiltrado)