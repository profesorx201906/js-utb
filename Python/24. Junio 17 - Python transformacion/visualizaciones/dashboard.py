import limpiar as lp
import numpy as np
import pandas as pd
import os

ruta = os.path.join(os.path.dirname(__file__))


lp.limpiar_pantalla()
df_poblacion = pd.read_csv(f"{ruta}/population_total.csv")
print(df_poblacion)