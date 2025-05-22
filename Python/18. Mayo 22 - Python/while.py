# saber la cantidad de compras y el promedio de las compras
# Entrada
monto = -1
totalCompras = 0

# Proceso
while monto != 0:
    monto = float(input("Digite el valor de la compra : "))
    if monto < 0:
        print("no se puede sumar el valor de la compra por ser menor que 0")
    else:
        totalCompras += monto

# Salida
print(f"El total de las compras es {totalCompras:,.2f}")
