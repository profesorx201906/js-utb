# funcion max: Encuentra el elemento con mayor valor de la lista

numeros = [1, 2, 3, 4, 5, 4, 4, 7, 2, -5]
mayor = max(numeros)
print(f"la lista \n{numeros}")
print(f"el elemento mayor es {mayor}")

# funcion min: Encuentra el elemento con menor valor de la lista
menor = min(numeros)
print(f"el elemento menor es {menor}")

# funcion len: Encuentra la longitud o el tamaño de  la lista

longitud = len(numeros)
print(f"el tamaño de la lista es {longitud}")

# funcion sum: suma los elementos de una lista
suma = sum(numeros)
print(f"La suma de la lista es {suma}")
# como calculo el promedio de la lista
promedio = sum(numeros) / len(numeros)
print(f"El promedio de la lista es {promedio}")

# funcion sorted: ordena la lista en orden ascendente, si se desea ordenar descendente se debe agregar un parametro adicional que es reverse=true
numerosOrdenadosAsc = sorted(numeros)
print(f"lista ordenada ascendentemente {numerosOrdenadosAsc}")

numerosOrdenadosDes = sorted(numeros, reverse=True)
print(f"lista ordenada descendemente {numerosOrdenadosDes}")

# utilizar funciones matemáticas debo import la libreria math

import math

raiz = math.sqrt(225)
print(raiz)
