import limpiar as lp
import numpy as np
import pandas as pd

lp.limpiar_pantalla()
df1 = pd.DataFrame(
    {"id": [10, 20, 30], "nombre": ["Juan", "Pedro", "Luis"], "estrato": [1, 3, 4]}
)
df2 = pd.DataFrame(
    {
        "estrato": [1, 2, 3, 4, 5],
        "descripcion": ["bajo-bajo", "bajo", "medio", "medio-alto", "alto"],
    }
)

print("Data Frame 1")
print(df1)
print("Data Frame 2")
print(df2)

# merge
print("merge por el campo estrato")
df_merge = pd.merge(df1, df2, on="estrato", how="inner")
print("Data frame merge")
print(df_merge)
print("Presione tecla para continuar")
input()
lp.limpiar_pantalla()

print("Operación de pivot en dataframe")
productos_df = pd.DataFrame(
    {
        "Fecha": ["2023-01", "2023-01", "2023-02", "2023-02"],
        "Producto": ["Samsung", "Apple", "Samsung", "Apple"],
        "Descuento": [10, 15, 20, 10],
        "Venta": [100, 150, 200, 120],
    }
)
print("Información original")
print(productos_df)
print("información pivoteada")

productos_pivot = productos_df.pivot(index="Producto", columns="Fecha", values="Descuento")
print(productos_pivot)
print("Presione tecla para continuar")
input()
lp.limpiar_pantalla()
