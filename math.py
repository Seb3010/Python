import math

def formula(a, b):
    resta = (a - b)
    return resta ** 2

def formula_2(a, b):
    resta = (a - b)
    return resta ** 2

while True:
    try:
        x1 = input("ingresa x1:")
        x2 = input("ingresa x2:")
        y1 = input("ingresa y1:")
        y2 = input("ingresa y2:")
        result_1 = formula(float(x2), float(x1))
        result_2 = formula_2(float(y2), float(y1))
        result_3 = (result_1 + result_2)
        math.pow(result_3)
    except ValueError:
        print("Por favor ingresa solo numeros.")
