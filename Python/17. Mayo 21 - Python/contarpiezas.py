# entrada
n = int(input("Digite la cantidad de piezas a evaluar : "))
longitud = 0.0
cantidadAptas = 0

# proceso
for i in range(n):
    longitud = float(input(f"Digite la longitud de la pieza {i+1}: "))
    if longitud >= 1.2 and longitud <= 1.3:
        cantidadAptas = cantidadAptas + 1

# salidad
print(f"El numero de piezas aptas para {n} piezas es {cantidadAptas}")
