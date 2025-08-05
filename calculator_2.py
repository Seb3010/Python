import time
import math

def suma(*numeros):
    if len(numeros) < 2:
        return "Se requieren al menos dos números"
    return round(sum(numeros), 2)


def resta(*numeros):
    if len(numeros) < 2:
        return "Se requieren al menos dos números"
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado -= n
    return round(resultado, 2)


def multiplicacion(*numeros):
    if len(numeros) < 2:
        return "Se requieren al menos dos números"
    resultado = 1
    for n in numeros:
        resultado *= n
    return round(resultado, 2)


def division(*numeros):
    if len(numeros) < 2:
        return "Se requieren al menos dos números"
    resultado = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            return "Error: división por cero"
        resultado /= n
    return round(resultado, 2)

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
    try:
        opcion = int(input("elige opcion "))
    except ValueError:
        print("Por favor, ingresa una opción válida.")
        continue

    if opcion in [1, 2, 3, 4]:
        while True:
            try:
                cantidad = int(input("¿Cuántos números quieres ingresar? "))
                if cantidad < 2:
                    print("Debes ingresar al menos dos números.")
                    continue
                break
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

        numeros = []
        for i in range(cantidad):
            while True:
                try:
                    n = float(input(f"Ingrese el número {i+1}: "))
                    numeros.append(n)
                    break
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                    continue

        if opcion == 1:
            print(f"resultado {suma(*numeros)}")
        elif opcion == 2:
            print(f"resultado {resta(*numeros)}")
        elif opcion == 3:
            print(f"resultado {multiplicacion(*numeros)}")
        elif opcion == 4:
            print(f"resultado {division(*numeros)}")
    elif opcion in [5, 6]:
        while True:
            try:
                num1 = float(input("ingresa el numero "))
                break
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue
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
