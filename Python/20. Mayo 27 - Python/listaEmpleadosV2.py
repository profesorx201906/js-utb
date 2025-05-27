# Elaborar un algoritmo que permita almacenar información un grupo de empleados para los cuales se debe solicitar la siguiente información  Identificación , Nombre, Apellido, Edad, Salario
# debemos imprimir el salario promedio de los empleados, debemo imprimir el empleado con mayor salario y debemos imprimir todos los empleados que tengan el apellido Berrocal
import os

empleados = []


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu():
    print("-" * 40)
    print(f"{'     1. Capturar Datos empleado'}")
    print(f"{'     2. Imprimir promedio salario'}")
    print(f"{'     3. Imprimir empleados'}")
    print(f"{'     4. Imprimir Empleados por apellido'}")
    print(f"{'     5. salir'}")
    print("-" * 40)


def imprimirEmpleados(empleados):
    print("-" * 80)
    print(
        f"{'Identificacion':<10} {'Nombre':<10} {'Apellido':<10}{'Edad':>5}{'Salario':>10}"
    )
    print("-" * 80)
    for emp in empleados:
        print(
            f"{emp['indentificacion']:<15}{emp['nombre']:<10}{emp['apellido']:<10}{emp['edad']:>5}{emp['salario']:>15,.2f}"
        )
    print("-" * 80)


def llenarDatos(empleados):
    empleado = {}
    empleado["indentificacion"] = input(f"Digite la identificacion del empleado : ")
    empleado["nombre"] = input(f"Digite la nombre del empleado : ")
    empleado["apellido"] = input(f"Digite la apellido del empleado : ")
    empleado["edad"] = int(input(f"Digite la edad del empleado : "))
    empleado["salario"] = float(input(f"Digite la salario del empleado : "))
    empleados.append(empleado)


def promedio():
    if len(empleados) == 0:
        print("No hay empleados registrados.")
    else:
        total_salario = sum(e["salario"] for e in empleados)
        promedio_salario = total_salario / len(empleados)
        print(f"\nEl promedio de salario es: ${promedio_salario:,.2f}")
    input("\nPresione una tecla para continuar...")


def imprimirPorApellido():
    apellido = input("Digite el apellido a buscar :")


while True:
    limpiar_pantalla()
    menu()
    opcion = int(input("Digite la opcion "))
    if opcion == 5:
        break
    if opcion == 1:
        limpiar_pantalla()
        llenarDatos(empleados)
    elif opcion == 2:
        promedio()
    elif opcion == 3:
        imprimirEmpleados(empleados)
        input("Presione tecla para continuar")
    elif opcion == 4:
        imprimirPorApellido()


"""import json

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


# llenar los Datos
# calcular el promedio
# hallar el salario mayor
# definir un menu
# limpiar pantalla
"""
