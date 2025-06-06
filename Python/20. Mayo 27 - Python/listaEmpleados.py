# Elaborar un algoritmo que permita almacenar información un grupo de empleados para los cuales se debe solicitar la siguiente información  Identificación , Nombre, Apellido, Edad, Salario
# debemos imprimir el salario promedio de los empleados, debemo imprimir el empleado con mayor salario y debemos imprimir todos los empleados que tengan el apellido Berrocal
import json

empleados = []

salarioMayor = 0
posicionEmpleado = 0
sumaSalarios = 0
promedio = 0.0

N = int(input("Digite el número de empleados : "))

for i in range(N):
    empleado = {}
    empleado["indentificacion"] = input(
        f"Digite la identificacion del empleado {i+1} : "
    )
    empleado["nombre"] = input(f"Digite la nombre del empleado {i+1} : ")
    empleado["apellido"] = input(f"Digite la apellido del empleado {i+1} : ")
    empleado["edad"] = int(input(f"Digite la edad del empleado {i+1} : "))
    empleado["salario"] = float(input(f"Digite la salario del empleado {i+1} : "))

    empleados.append(empleado)

i = 0

for emp in empleados:
    sumaSalarios += emp["salario"]
    if emp["salario"] > salarioMayor:
        salarioMayor = emp["salario"]
        posicionEmpleado = i
    i += 1

promedio = sumaSalarios / N
print(f"El empleado con mayor  salario es : {empleados[posicionEmpleado]['nombre']}")
print(f"El promedio de salarios es : {promedio:,.2f}")

print(f"Empleados con apellido Berrocal")
for emp in empleados:
    if emp["apellido"].lower() == "berrocal":
        print(emp)
