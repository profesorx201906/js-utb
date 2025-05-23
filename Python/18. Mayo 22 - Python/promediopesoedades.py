'''
Entradas:
Peso (se caracteriza por ser número positivo, diferente de cero y podemos expresarlo  o no en decimales)
Edad (se caracteriza por ser número positivo, puede ser igual a cero y llevar decimales para los bebés de meses )
 
Proceso:
Se reciben los datos de entrada
El programa debe ir agrupando los datos de peso clasificados por su rango de edad.
Una vez clasificados los datos, el programa debe calcular el promedio por cada rango de edad.
Como dato adicional, el programa puede contar el número de muestras por cada rango de edad y número de muestras total.
Finaliza cuando ingresemos los datos de la muestra número 5.
 
Salidas:
Promedio de peso por cada rango de edad
Número de muestras por rango de edad
Numero de muestras total


niños = 0
jovenes = 0
adultos = 0
ancianos = 0
pesoNiños = 0
pesoJovenes = 0
pesoAdultos = 0
pesoAncianos = 0
 
for i in range(5):
    edad = int(input("ingrese la edad de la persona "))
    peso = float(input("ingrese el peso de la persona "))
    if edad <= 12:
        niños += 1
        pesoNiños += peso
    elif edad <= 29:
        jovenes += 1
        pesoJovenes += peso
    elif edad <= 59:
        adultos += 1
        pesoAdultos += peso
    else:
        ancianos += 1
        pesoAncianos += peso
if niños > 0:
    promedioNiños = pesoNiños / niños  
else:
    promedioNiños = 0
if jovenes > 0:
    promedioJovenes = pesoJovenes / jovenes
else:
    promedioJovenes = 0
if adultos > 0:
    promedioAdultos = pesoAdultos / adultos
else:
    promedioAdultos = 0
 
if ancianos > 0:
    promedioAncianos = pesoAncianos / ancianos
else:
    promedioAncianos = 0
print("el promedio de peso de los niños es ", promedioNiños)
print("el promedio de peso de los jovenes es ", promedioJovenes)
print("el promedio de peso de los adultos es ", promedioAdultos)
print("el promedio de peso de los ancianos es ", promedioAncianos)

'''

# Inicialización de contadores y acumuladores
niños = 0
jovenes = 0
adultos = 0
ancianos = 0
pesoNiños = 0
pesoJovenes = 0
pesoAdultos = 0
pesoAncianos = 0
 
# Recolectar datos de 5 personas
for i in range(5):
    print(f"\nPersona {i+1}")
 
    # Validar la entrada de la edad
    while True:
        try:
            edad = int(input("Ingrese la edad de la persona: "))
            if edad < 0:
                print("La edad no puede ser negativa. Intente de nuevo.")
            else:
                break
        except ValueError:
            print("Dato inválido. Ingrese un número entero válido para la edad.")
 
    # Validar la entrada del peso
    while True:
        try:
            peso = float(input("Ingrese el peso de la persona: "))
            if peso < 10 or peso > 120:
                print("El peso debe ser mayor que 10 y menor que 120. Intente de nuevo.")
            else:
                break
        except ValueError:
            print("Dato inválido. Ingrese un número válido para el peso.")
 
    # Clasificar según la edad y acumular los datos
    if edad <= 12:
        niños += 1
        pesoNiños += peso
    elif edad <= 29:
        jovenes += 1
        pesoJovenes += peso
    elif edad <= 59:
        adultos += 1
        pesoAdultos += peso
    else:
        ancianos += 1
        pesoAncianos += peso
 
# Calcular promedios, evitando división por cero
promedioNiños = pesoNiños / niños if niños > 0 else 0
promedioJovenes = pesoJovenes / jovenes if jovenes > 0 else 0
promedioAdultos = pesoAdultos / adultos if adultos > 0 else 0
promedioAncianos = pesoAncianos / ancianos if ancianos > 0 else 0
 
# resultados
print("\n--- Promedios de peso por categoría ---")
print(f"Niños: {promedioNiños:.2f} kg")
print(f"Jóvenes: {promedioJovenes:.2f} kg")
print(f"Adultos: {promedioAdultos:.2f} kg")
print(f"Ancianos: {promedioAncianos:.2f} kg")