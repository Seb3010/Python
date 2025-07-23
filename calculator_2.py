import time
import math

def suma(a, b):
    return round(a + b, 2)


def resta(a, b):
    return round(a - b, 2)


def multiplicacion(a, b):
    return round(a * b, 2)


def division(a, b):
    if b != 0:
        return round(a / b, 2)
    else:
        return 0

def potencia(a):
    return round(pow(a, 2), 2)


def raiz_cuadrada(a):
    if a >= 0:
        return round(math.sqrt(a), 2)
    else:
        return 0


def calculadora():
    print("elige una opcion")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. potencia")
    print("6. raiz cuadrada")


while True:
    calculadora()
    opcion = int(input("elige opcion "))

    if opcion in [1, 2, 3, 4]:
        num1 = float(input("ingresa el primer numero "))
        num2 = float(input("ingresa el segundo numero "))
    if opcion == 1:
        print(f"resultado {suma(num1, num2)}")
    elif opcion == 2:
        print(f"resultado {resta(num1, num2)}")
    elif opcion == 3:
        print(f"resultado {multiplicacion(num1, num2)}")
    elif opcion == 4:
        print(f"resultado {division(num1, num2)}")
    elif opcion in [5, 6]:
        num1 = float(input("ingresa el numero "))
    if opcion == 5:
        print(f"resultado {potencia(num1)}")
    elif opcion == 6:
        print(f"resultado {raiz_cuadrada(num1)}")

    time.sleep(3)
    desicion = input("¿Deseas continuar? ")
    if desicion == "no":
        print("Gracias por usar la calculadora")
        print("Hasta luego")
        break
    else:
        print("continuando...")
        time.sleep(3)
