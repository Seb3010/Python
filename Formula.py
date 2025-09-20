import math

def formula(a, b):
    return (a - b)

def formula_2(a, b):
    return (a - b)

def election():
    print("1. Calculo de la distancia entre dos puntos en un plano cartesiano")
    print("2. area de un triangulo")
    return int(input("elige una opcion:"))

while True:
    option = election()

    if option == 1:
        try:
            x1 = float(input("ingresa x1:"))
            x2 = float(input("ingresa x2:"))
            y1 = float(input("ingresa y1:"))
            y2 = float(input("ingresa y2:"))
        except ValueError:
            print("Por favor ingresa un numero valido.")
            continue

        
        result_1 = formula(float(x2), float(x1))
        result_2 = formula_2(float(y2), float(y1))
        result_3 = result_1 ** 2
        result_4 = result_2 ** 2
        resultl_5 = round(math.sqrt(result_3 + result_4), 2)
        print(f"El resultado es: {resultl_5}")
        print("procedimiento:")
        print(f"1. Calcular la resta de x2 y x1: {x2} - {x1} = {result_1}")
        print(f"2. Calcular la resta de y2 y y1: {y2} - {y1} = {result_2}")
        print(f"3. Elevar al cuadrado el resultado 1: {result_1}^2 = {result_3}")
        print(f"4. Elevar al cuadrado el resultado 2: {result_2}^2 = {result_4}")
        print(f"5. Calcular la raíz cuadrada de la suma de los cuadrados: √({result_3} + {result_4}) = {resultl_5}")
            

    elif option == 2:
        try:
            x1 = float(input("ingresa x1:"))
            x2 = float(input("ingresa x2:"))
            x3 = float(input("ingresa x3:"))
            y1 = float(input("ingresa y1:"))
            y2 = float(input("ingresa y2:"))
            y3 = float(input("ingresa y3:"))
        except ValueError:
            print("Por favor ingresa un numero valido.")
            continue
        
        result_1 = (x1*y2 + x2*y3 + x3*y1)
        result_2 = (y1*x2 + y2*x3 + y3*x1)
        result_3 = result_1 - result_2
        result_4 = 0.5*result_3
        print(f"El resultado es: {result_4}")
        print("procedimiento:")
        print(f"1. Calcular x1*y2 + x2*y3 + x3*y1: {x1}*{y2} + {x2}*{y3} + {x3}*{y1} = {result_1}")
        print(f"2. Calcular y1*x2 + y2*x3 + y3*x1: {y1}*{x2} + {y2}*{x3} + {y3}*{x1} = {result_2}")
        print(f"3. Calcular la resta del resultado 1 y resultado 2: {result_1} - {result_2} = {result_3}")
        print(f"4. Calcular 0.5 * resultado 3: 0.5 * {result_3} = {result_4}")

    cont = input("Quieres continuar? (si/no): ")
    if cont.lower() == "si":
        continue
    else:
        break
