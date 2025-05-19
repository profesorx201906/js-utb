# operador parentesis mayor nivel de jeraquia
# siempre se ejecuta primero lo que este dentro de el

a = 5
b = 6
c = -5

resultado = a + b * (c + b + 1)
print(resultado)

resultado = 3 + 4 * 2  # 11
print(resultado)

resultado = (3 + 4) * 2  # 14
print(resultado)

resultado = 10 + 6 / 2  # 13 si se hace con doble / es division entera ejemplo a =40//3
print(resultado)

resultado = 2 * 3**2  # 18
print(resultado)

resultado = 5 + 3 * 2**2 - (4 / 2)  # 15
print(resultado)

resultado = ((2 + 3) * 2) ** 2  # 100
print(resultado)

print(10 % 3)

# Relacionales
print("Operadores Relacionales")
print(5 == 7)
print(5 != 7)
print(5 < 10)
print(5 > 10)
print(5 <= 3)
print(5 >= 3)

# operadores lógicos
print("Operadores Lógicos")
print(True and False)
print(True or False)

print((5 <= 1) and (6 >= 3))
