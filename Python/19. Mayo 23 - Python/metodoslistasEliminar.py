# Metodo Pop Elimina un elemento de la lista dado su indice

frutas = ["Manzana", "Pera"]
frutas.append("Fresa")
frutas.append("Naranja")
frutas.extend(["Melon", "Kiwi"])
frutas.extend("hola")
frutas.insert(0, "Piña")
frutas.insert(3, "Uva")
print(frutas)
# elimina el elemento con posición 10
frutas.pop(10)
print(frutas)

# metodo remove elimina un elemento basado en el valor del elemento
try:
    frutas.remove("pera")
except ValueError:
    print("no encontro el elemento")

print(frutas)
