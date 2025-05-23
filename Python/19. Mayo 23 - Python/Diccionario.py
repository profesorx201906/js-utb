# crear un diccionario
empleado = {"nombre": "Kennyn", "apellido": "Marquez", "edad": 25, "salario": 1500000}
print(empleado)
print(type(empleado))
print(empleado["nombre"])
print(empleado.get("edad"))
print(empleado.get("email", "Elemento no encontrado"))
empleado["email"] = "kennyn@gmail.com"
print(empleado)

datos = {2: "Telefono", 1: "camara", 3: "televisor"}
print(datos[3])
datos[5]="plancha"
print(datos)
datos[5]="Carro"
print(datos)
del datos[5]
print(datos)
