import pandas as pd
df = pd.read_csv("Python/22. Junio 3 - Python/colesterol.csv")
print("Datos population total cargando csv")
print(df)

dfExcel = pd.read_excel("Python/22. Junio 3 - Python/Mercado_casa.xlsx",sheet_name="Datos1")
print("Datos mercado casa desde excel")
print(dfExcel)