"""
Suponga que se tiene un conjunto de calificaciones de un grupo de N alumnos, se realizar hasta que se digite una calificación de 0. Realizar un algoritmo para calcular la calificación media y la calificación mas baja de todo el grupo.
"""

calificacion = -1
totalCalificacion = 0
count = 0
calificacionMasBaja = 5.0
promedio = 0

# Proceso
while calificacion != 0:
    try:
        while True:
            calificacion = float(input("Digite la calificación : "))
            if calificacion > 5 or calificacion < 0:
                print("las calificaciones deben ser entre 0.0 y 5.0")
            else:
                break

        if calificacion < 0:
            print("la calificación no puede ser menor que 0")
        elif calificacion == 0:
            print("Finalizo la captura de datos")
        else:
            totalCalificacion += calificacion
            count += 1
            if calificacion != 0 and calificacion < calificacionMasBaja:
                calificacionMasBaja = calificacion

    except ValueError:
        print("Digite un dato correcto (número)")
if count > 0:
    promedio = totalCalificacion / count
else:
    calificacionMasBaja = 0
# Salida
print(
    f"la media de la calificacion del grupo es  {promedio:.2f} \n calificacion mas baja: {calificacionMasBaja} "
)
