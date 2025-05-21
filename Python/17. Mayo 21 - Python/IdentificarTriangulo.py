# Entrada
lado1 = int(input("Digite el valor del lado 1 : "))
lado2 = int(input("Digite el valor del lado 2 : "))
lado3 = int(input("Digite el valor del lado 3 : "))
tipoTriangulo = ""

# proceso

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("alguno de los lados no es correcto, es menor o igual a cero")
else:

    if lado1 == lado2 and lado1 == lado3:
        tipoTriangulo = "Equilatero"
    elif lado1 != lado2 and lado1 != lado3:
        tipoTriangulo = "Escaleno"
    else:
        tipoTriangulo = "isosceles"

    # Salida

    print(
        f"El tipo de triangulo con lados \n lado1={lado1} \n lado2={lado2} \n lado3={lado3} \n es {tipoTriangulo}"
    )
