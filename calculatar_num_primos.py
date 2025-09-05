import time

print("Bienvenido a la calculadora de números primos")
time.sleep(3)
while True:
    try:
        num =  int((input("Ingrese un número para verificar si es primo: ")).strip())
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
            else:
                primo = True
                break

        if primo == True:
            print(f"{num} es un número primo.")
        else:
            print(f"{num} no es un número primo.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue