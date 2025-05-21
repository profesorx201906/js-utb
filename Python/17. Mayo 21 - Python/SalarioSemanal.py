# Entrada

numeroHoras = float(input("Digite el numero de horas trabajadas en la semana : "))
salarioSemanal = 0

# Proceso

if numeroHoras < 0:
    print("no se puede calcular el salario por que el numero de horas no es correcto")
else:
    if numeroHoras <= 40:
        salarioSemanal = numeroHoras * 16
    else:
        salarioSemanal = (40 * 16) + (numeroHoras - 40) * 20

# salida

    print(f"El salario semanal para {numeroHoras} semanales es : {salarioSemanal}")
