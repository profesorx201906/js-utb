invitados = []
invitados.append("Maria")
invitados.append("Jose")
invitados.extend(["Pedro", "Judas", "Juan", "Tomas"])
print(invitados)
invitados.insert(0, "Jesus")
print(invitados)
invitados.remove("Judas")
print(invitados)
invitados.pop(len(invitados) - 1)
print(invitados)

numeros = [1, 2, 3, 4, 5, 4, 4]
# eliminen todos los numero 4 de la lista


while 4 in numeros:
  numeros.remove(4)

print(numeros)
