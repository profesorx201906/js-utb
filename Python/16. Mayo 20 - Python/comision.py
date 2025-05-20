# Entrada
salarioBase = float(input("Digite el salario base"))
venta1 = float(input("Digite el valor de la venta 1: "))
venta2 = float(input("Digite el valor de la venta 2: "))
venta3 = float(input("Digite el valor de la venta 3: "))


# Proceso

valorComisiones = (venta1 + venta2 + venta3) * 0.1
salorioTotal = valorComisiones + salarioBase


# salida

print(
    f"El valor de salario total es:  \nSalario Base {salarioBase:15,.2f} \ncomisiones : {valorComisiones:15,.2f} \nsalario total:{salorioTotal:15,.2f} "
)

totalCompra = float(input("ingrese cantidad de la compra: "))

