# Metodo append permite agregar un elemento al final de la 
frutas = ["Manzana","Pera"]
print(frutas)
frutas.append("Fresa")
frutas.append("Naranja")
print(frutas)

# Metodo extend permite agregar una lista de elementos elementos de una lista iterable

#agrega 2 elementos Melon y Kiwi  a la lista frutas
frutas.extend(["Melon","Kiwi"])
print(frutas)

#agrega cada letra como un elemento nuevo a  lista frutas
frutas.extend("hola")
print(frutas)


# Metodo Insert: inserta un elemento en la posición requerida. Se envia la posición y el valor como argumentos
frutas.insert(0,"Piña")
print(frutas)
frutas.insert(3,"Uva")
print(frutas)