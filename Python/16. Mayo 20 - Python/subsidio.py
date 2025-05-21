# Entrada
nombre = input("Digite su nombre : ")
salario = float(input("Digite su salario base : "))
subsidio = 0
# Procesos

if salario <= 1500000:
    subsidio = 150000
else:
    subsidio = 0

salarioTotal = salario + subsidio


# Salida
print(f"El salario total de {nombre} \n salario base : {salario:20,.2f}\n subsidio es {subsidio:20,.2f} \n salario total {salarioTotal:20,.2f}")
