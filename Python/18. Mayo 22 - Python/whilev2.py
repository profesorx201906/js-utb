# saber la cantidad de compras (solo tener en cuenta las compras con valores positivos) y el promedio de las compras
# Entrada
totalCompras = 0
cantidad = 0
promedio = 0
# Proceso
while True:
    monto = float(input("Digite el valor de la compra : "))
    #---
    if monto == 0:
        break
    #---
    if monto < 0:
        print("no se puede sumar el valor de la compra por ser menor que 0")
    else:
        totalCompras += monto
        cantidad += 1
# Salida
if cantidad>0:
  promedio = totalCompras / cantidad
print(
    f"se realizaron {cantidad} de compras. \nPromedio fue de {promedio} y el total de las compras es {totalCompras:,.2f} "
)
