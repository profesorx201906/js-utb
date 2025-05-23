# Definir una lista
import random
personas = ["Catalina", "Silvia", "Sergio", "Iván", "Paula"]
print(type(personas))
print(personas)
print(personas[2])
print(personas[1:3])

numeros = list(range(2, 11, 2))
print(numeros)

numerosAleoatorios = []
for i in range(5):
  numeroAleatorio = random.randint(1,5)
  numerosAleoatorios.append(numeroAleatorio)

print(numerosAleoatorios)

valoresVarios = ["Cadena", 25, True, [1, 2, 3]]
print(valoresVarios)

# recorrer las lista

for i in range(len(numerosAleoatorios)):
  print(numerosAleoatorios[i])
  
print("-"*20)
for numero in numerosAleoatorios:
  print(numero)
  

