import math

def formula(a, b):
    resta = (a - b)
    return resta ** 2

def formula_2(a, b):
    resta = (a - b)
    return resta ** 2

while True:
    print("1. Calculo de la distancia entre dos puntos en un plano cartesiano")
    print("2.)
    input("elige una opcion:")


    try:
        x1 = float(input("ingresa x1:"))
        x2 = float(input("ingresa x2:"))
        y1 = float(input("ingresa y1:"))
        y2 = float(input("ingresa y2:"))
    except ValueError:
        print("Por favor ingresa un numero valido.")
        continue

    while True:
        result_1 = formula(float(x2), float(x1))
        result_2 = formula_2(float(y2), float(y1))
        result_3 = result_1 ** 2
        result_4 = result_2 ** 2
        resultl_5 = math.sqrt(result_3 + result_4)
        print(f"El resultado es: {resultl_5}")
        print("procedimiento:")
        print(f"1. Calcular la resta de x2 y x1: {x2} - {x1} = {result_1}")
        print(f"2. Calcular la resta de y2 y y1: {y2} - {y1} = {result_2}")
        print(f"3. Elevar al cuadrado el resultado 1: {result_1}^2 = {result_3}")
        print(f"4. Elevar al cuadrado el resultado 2: {result_2}^2 = {result_4}")
        print(f"5. Calcular la raíz cuadrada de la suma de los cuadrados: √({result_3} + {result_4}) = {resultl_5}")
        break

    cont = input("Quieres continuar? (si/no): ")
    if cont.lower() == "si":
        continue
    else:
        break
