import limpiar as lp
import numpy as np
lp.limpiar_pantalla()
#array una dimensión
a1 = np.array([[1, 2, 3]])
lista = [1,2,3]
print(a1)
print(lista)

#array dos dimensiones 
tabla = [[1, 2, 3],[4, 5, 6]]
a2 = np.array([[1, 2, 3],[4, 5, 6]])
print(tabla)
print(a2)

#array tres dimensiones
cubo=[[[1,2,3],[4,5,6],[4,4,4]],[[7,8,9],[0,0,0],[9,9,9]]]
a3=np.array([[[1,2,3],[4,5,6],[4,4,4]],[[7,8,9],[0,0,0],[9,9,9]]])
print(cubo)
print(a3)

# Ejemplo operacion suma
print("*"*20)
print("Matriz original ")
matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
#suma las columnas
print("suma de columnas ")
m=np.sum(matriz,axis=0)
print(m)
#suma las las filas
print("suma de filas ")
m=np.sum(matriz,axis=1)
print(m)
print("Valor máximo de la columna ")
m=np.amax(matriz,axis=0)
print(m)
print("Valor máximo de la fila ")
m=np.amax(matriz,axis=1)
print(m)

#crear arreglo vacio
print("arreglo vacio")
arreglo1= np.empty([2,2],dtype=int)
arreglo1[0,0]=5
arreglo1[0,1]=15
arreglo1[1,0]=6
arreglo1[1,1]=7

print(arreglo1)

#arreglo lleno de 0
print("Arrego lleno de ceros")
arreglo=np.zeros([3,3])
print(arreglo)

#arreglo lleno de 1
print("Arrego lleno de unos")
arreglo=np.ones([3,4])
print(arreglo)

#arreglo lleno de un numero definido
print("Arrego lleno de un numero definido")
arreglo=np.full([2,2],8)
print(arreglo)

#creacion de arreglo con rango de valores
arreglo=np.arange(2,20,2)
print("arreglo creado con rango de valores desde el 2 hasta el 18 con incremento de 2")
print(arreglo)