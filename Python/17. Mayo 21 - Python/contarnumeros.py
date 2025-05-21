negativo = 0
positivo = 0
cero = 0
for i in range(20):
    num = float(input(f"ingrese un numero #{i+1}: "))
    if num == 0:
        cero += 1
    elif num > 0:
        positivo += 1
    else:
        negativo += 1

print(f"numeros negativo: {negativo} \n numeros positivo: {positivo} \n numeros cero: {cero}")
