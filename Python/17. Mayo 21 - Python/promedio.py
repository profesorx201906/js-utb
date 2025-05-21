resultado = 0.0
for i in range(7):
    calificacion = float(input(f'ingrese su calificacion #{i+1}: '))
    resultado+= calificacion #se acumula o se suma las notas 
    #resultado = resultado+calificacion
 
print(f'Su calificacion final es: {resultado/7:.2f}')


