#entrada: ingresa los valores numero1 y numero2
#proceso:se crea una nueva varialble "resultado", si numero1 y numero2 son iguales se multiplica (numero1*numero2),
# si numero1 es mayor que numero2 se resta (numero1-numero2),
# sino  se suman (numero+numero2)
#salida: se muestra el resultado de la operacion.
 
numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))
 
resultado = 0
 
if numero1 == numero2 :
    resultado = numero1 * numero2
elif numero1 > numero2 :
    resultado = numero1 - numero2
else:
    resultado = numero1 + numero2
 
 
print(f'primer numero: {numero1} \n segundo numero: {numero2} \n resultado: {resultado}')