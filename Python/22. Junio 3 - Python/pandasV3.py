import pandas as pd
import numpy as np
import limpiar as lp
import sys

lp.limpiar_pantalla()
sys.stdout.reconfigure(encoding="utf-8")

# crear df

datos = pd.DataFrame(
    {
        "Nombre": ["Ana", "Juan", "María", "Carlos"],
        "Edad": [22, 30, 25, 28],
        "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    }
)
print("Información del dataframe")
print(datos)
# datos filtrados personas mayor que el promedio
promedio = datos["Edad"].mean()
datos_filtrados = datos[datos["Edad"] < promedio]
print(f"Personas con edad menor a al promedio {promedio}")
print(datos_filtrados)

# crea categoria para adulto >25 y joven menor o igual
print(f"Crear categoria de adulto o joven")
datos["Categoria"] = np.where(datos["Edad"] <= 25, "Joven", "Adulto")
print(datos)
