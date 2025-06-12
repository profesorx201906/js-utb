# Taller

# Ejercicio 1 Fundamentos numpy
# Crear vectores y matrices (visualizar)

# 1. Crear vectores y matrices
import numpy as np
import limpiar as lp
import os

lp.limpiar_pantalla()


def linea():
    print("*" * 45)


print("1. Crear vectores y matrices")
numeros = np.array([1, 2, 3, 4, 5, 6])
numeroRomanos = np.array(["I", "II", "III"])
nombre_apellido = np.array(
    [["Hever", "Juan", "Hector", "Pedro"], ["Torres", "Perez", "Delgado", "sanchez"]]
)
print(numeros)
print(nombre_apellido)

vectorUno = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
print("El primer vector es:")
print(vectorUno)

vectorDos = np.array([-8, -7, -6, -5, -4, -3, -2, -1, 0])
print("\nEl segundo vector es:")
print(vectorDos)

sumaVector = np.add(vectorUno, vectorDos)
print("\nEl vector suma, usando la función np.add es:")
print(sumaVector)

# Crear una matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatriz:")
print(matriz)

input("Presione tecla para continuar")
lp.limpiar_pantalla()
print("2 Obtener estadísticas básicas")
# 2 Obtener estadísticas básicas
# suma de numeros
suma = np.sum(numeros)
print(f"La suma de los numeros es : {suma}")

# promedio de los numeros
linea()
prom = np.mean(numeros)
print(f"El promedio de los numeros es : {prom}")

# desviacion estandar
linea()
desviacion = np.std(numeros)
print(f"La desviacion estandar es : {desviacion} ")
linea()

input("Presione tecla para continuar")
lp.limpiar_pantalla()

# 3. Usar operaciones sobre ejes
print("3. Usar operaciones sobre ejes")

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriz:\n", matriz)

# Sumar filas
suma_filas = np.sum(matriz, axis=1)
print("Suma por filas:", suma_filas)

# Sumar columnas
suma_columnas = np.sum(matriz, axis=0)
print("Suma por columnas:", suma_columnas)

# promedio filas y columnas
# proemdio filas
promedio_filas = np.mean(matriz, axis=1)
print("Promedio por filas:", promedio_filas)

# proemdio filas
promedio_columnas = np.mean(matriz, axis=0)
print("Promedio por columnas:", promedio_columnas)

input("Presione tecla para continuar")
lp.limpiar_pantalla()

# 4. Crear matrices especiales
print("4. Crear matrices especiales")

# Matriz de ceros
ceros = np.zeros((3, 2))
print("Matriz de ceros:\n", ceros)

# matriz de unos
unos = np.ones((3, 5))
print("Matri de unos:\n", unos)

# Matriz identidad
identidad = np.eye(5, k=2)
print("Matriz identidad:\n", identidad)

# crear matriz identidad con ciclos sin numpy

iden = []
n = 5
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)

    iden.append(fila)

iden = np.array(iden)
print(iden)
input("Presione tecla para continuar")
lp.limpiar_pantalla()
print("Pandas")
print("1. Cargar el archivo CSV y visualizar la información")
# PANDAS
import pandas as pd

ruta = os.path.join(os.path.dirname(__file__))
print(ruta)
# leer el archivo
archivo = pd.read_csv(f'{ruta}\datos_estudiantes.csv', sep="*")

print(archivo)

input("Presione tecla para continuar")
lp.limpiar_pantalla()

#2. Ver información básica
print("2. Ver información básica")

print("primeras filas",archivo.head(2))#si no se envia parametro muestra 5
linea()
print("informacio del df",archivo.info())
linea()
print("Descripcion estadística",archivo.describe())

input("Presione tecla para continuar")
lp.limpiar_pantalla()
#3. Acceder a columnas y filas
print("3. Acceder a columnas y filas")
linea()
print("nombres estudinates\n",archivo["Nombre"])