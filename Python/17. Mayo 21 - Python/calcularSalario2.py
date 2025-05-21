horasTrabajo = float(input("Por favor digite el total de horas extras laboradas "))
valorHora = float(input("Digite el valor de la hora "))
salario = 0

if horasTrabajo <= 0:
    print("Por favor verifique el dato ingresado e intente de nuevo ")
elif horasTrabajo <= 40:
    salario = horasTrabajo * valorHora
elif horasTrabajo > 40 and horasTrabajo <= 48:
    salario = 40 * valorHora + (horasTrabajo - 40) * 2 * valorHora
else:
    salario = 40 * valorHora + (8 * 2) * valorHora + (horasTrabajo - 48) * 3 * valorHora

print(f"El salario devengado este mes es por valor de {salario:,.2f}")
