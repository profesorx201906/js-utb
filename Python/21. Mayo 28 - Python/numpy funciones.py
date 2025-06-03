import limpiar
import numpy as np

limpiar.limpiar_pantalla()

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)
print("dimensiones de la matriz")
print(matriz.shape)

# hallar el valor máximo y la posición

arreglo = np.arange(1, 11, 1)
print(arreglo)
print("valor máximo del arreglo", arreglo.max())
print("posición valor maximo del arreglo", arreglo.argmax())

print("valor mínimo del arreglo", arreglo.min())
print("posición valor mínimo del arreglo", arreglo.argmin())

print(f"promedio del arreglo {arreglo.mean()}")

# ejemplo de condiciones en array
array = np.array([1, -2, -3, 4, 5])
condicion = array < 0
resultado = np.where(condicion, 0, array)
print(" valores menores que 0 reemplados con 0")
print("\n Arreglo original", array)
print("\n Arreglo con condiciones", resultado)

# extra un subarray
array = np.array([[1, 2, 3], [4, 5, 6]])
print("arreglo original \n",array)
print("sub array\n",array[1:2,1:3])
