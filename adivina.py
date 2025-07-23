import random
import time


def adivina_numero():
    print("Bienvenido al juego de adivina el número.")
    print("Eligue la dificulatad:")
    print("1. Fácil (1-10)")
    print("2. Medio (1-50)")
    print("3. Difícil (1-100)")


while True:
    adivina_numero()
    dificultad = input("Elige una opción (1-3): ")

    if dificultad == "1":
        cantidad_numero = 10
        numero_secreto = random.randint(1, 10)
        intentos_maximos = 5
    elif dificultad == "2":
        cantidad_numero = 50
        numero_secreto = random.randint(1, 50)
        intentos_maximos = 5
    elif dificultad == "3":
        cantidad_numero = 100
        numero_secreto = random.randint(1, 100)
        intentos_maximos = 4
    else:
        time.sleep(1)
        print("Opción no válida")
        continue

    time.sleep(1)
    print(f"Tienes {intentos_maximos} intentos para adivinar el numero entre 1 y {cantidad_numero}")

    while intentos_maximos > 0:
        try:
            intento = int(input("Introduce tu número: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        if intento == numero_secreto:
            print("¡Felicidades! Adivinaste el número.")
            time.sleep(1)
            desicion = input("¿deseas jugar de nuevo? ")
            if desicion == "si":
                break
            elif desicion == "no":
                print("Gracias por jugar.")
                exit()
        elif intento < numero_secreto:
            intentos_maximos -= 1
            print("El número es mayor.")
            print(f"Te quedan {intentos_maximos} intentos.")
        elif intento > numero_secreto:
            intentos_maximos -= 1
            print("El número es menor.")
            print(f"Te quedan {intentos_maximos} intentos.")
        if intentos_maximos == 0:
            print(f"Lo siento, has perdido. El número era {numero_secreto}.")
            time.sleep(1)
            while True:
                desicion = input("¿deseas jugar de nuevo? ")
                if desicion == "si":
                    break
                elif desicion == "no":
                    print("Gracias por jugar.")
                    exit()