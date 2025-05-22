# control de excepciones
# IMC

while True:
    try:
        peso = float(input("Digite el valor del peso "))
        if peso < 10 or peso > 120:
            print("el peso  debe ser mayor que 10 y menor que 120")
        else:
            break
    except ValueError:
        print("Digite un dato correcto (número)")

while True:
    try:
        altura = float(input("Digite el valor del altura "))
        if altura <= 0:
            print("la altura debe ser mayor que 0")
        else:
            break
    except ValueError:
        print("Digite un dato correcto (número)")


IMC = peso / (altura**2)
print(f"El IMC es de {IMC:,.2f}")
