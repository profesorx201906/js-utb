import limpiar as lp
import numpy as np
import pandas as pd

lp.limpiar_pantalla()
ventas = pd.DataFrame(
    {
        "Producto": ["A", "B", "C", "A", "B", "A", "C"],
        "Ventas": [10, 15, 20, 20, 25, 20, 30],
    }
)
print("Información original")
print(ventas)
print("Agrupar por columa producto y mostrar la media")
dfagrupadoproductos = ventas.groupby(by="Producto").mean()
print(dfagrupadoproductos)
print("Agrupar por columa producto y mostrar la suma")
dfagrupadoproductos = ventas.groupby(by="Producto").sum()
print(dfagrupadoproductos)

print("digite tecla para continuar")
input()
lp.limpiar_pantalla()
print("Información original")
print(ventas)
print("Generacion de columna con funcion lambda")
ventas["ValorConDescuento"] = ventas["Ventas"].apply(lambda x: x * 0.95)
print(ventas)
