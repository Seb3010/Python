# funcion para hacer un retraso en el tiempo
import time

# bienvwenida a la aplicacion
print("bienvenido al medidodor de tus soft skills")
time.sleep(1)

# listas para hacer el promedio de la evaluacion
preguntas = [25]
respuestas = []

# buvle para ingresar el nombre y evitar errores como que no pongan nada o que sean numeros
while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if len(nombre) > 0 and nombre.isalpha():
        break
    else:
        print("Por favor, ingresa un nombre válido que contenga solo letras.")
        time.sleep(1)

# explicacion de la aplicacion
print("a continuacion se te presentaran una serie de preguntas (responde en una escala de 1 a 5)")
time.sleep(1)

# bucles para responder preguntas y validar errores de que se pasen del numero y un valor no valido
while True:
    try:
        respuesta_1 = int(input("Involucro a otros en conversaciones sobre intereses personales."))
        respuestas.append(respuesta_1)
        if respuesta_1 < 1 or respuesta_1 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_2 = int(input("¿Doy aliento a los demás.? "))
        respuestas.append(respuesta_2)
        if respuesta_2 < 1 or respuesta_2 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_3 = int(input(
            "¿Muestro respeto por las diferencias y contribuciones de los compañeros.? "))
        respuestas.append(respuesta_3)
        if respuesta_3 < 1 or respuesta_3 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_4 = int(
            input("¿Ofrezco ayudar a los colegas cuando una necesidad es aparente.? "))
        respuestas.append(respuesta_4)
        if respuesta_4 < 1 or respuesta_4 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_5 = int(
            input("¿Demuestro confiabilidad al cumplir con los compromisos.? "))
        respuestas.append(respuesta_5)
        if respuesta_5 < 1 or respuesta_5 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_6 = int(input(
            "¿Repito puntos durante una conversación para garantizar la comprensión.? "))
        respuestas.append(respuesta_6)
        if respuesta_6 < 1 or respuesta_6 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_7 = int(
            input("¿Hago preguntas abiertas durante las conversaciones.? "))
        respuestas.append(respuesta_7)
        if respuesta_7 < 1 or respuesta_7 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_8 = int(
            input("¿No interrumpo a las personas que están hablando.? "))
        respuestas.append(respuesta_8)
        if respuesta_8 < 1 or respuesta_8 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_9 = int(
            input("¿Utilizo un lenguaje corporal que demuestra que estoy escuchando.? "))
        respuestas.append(respuesta_9)
        if respuesta_9 < 1 or respuesta_9 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_10 = int(input(
            "¿Me comunico de manera apropiada, tanto en mensajes escritos como verbales.? "))
        respuestas.append(respuesta_10)
        if respuesta_10 < 1 or respuesta_10 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_11 = int(input(
            "¿Busco una perspectiva positiva en una situación negativa - evito difundir una actitud pesimista.? "))
        respuestas.append(respuesta_11)
        if respuesta_11 < 1 or respuesta_11 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_12 = int(input("¿Es agradable conversar conmigo.? "))
        respuestas.append(respuesta_12)
        if respuesta_12 < 1 or respuesta_12 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_13 = int(
            input("¿Dedico  un alto nivel de integridad en mi trabajo.? "))
        respuestas.append(respuesta_13)
        if respuesta_13 < 1 or respuesta_13 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_14 = int(
            input("¿Pido ayuda cuando estoy luchando con un problema.? "))
        respuestas.append(respuesta_14)
        if respuesta_14 < 1 or respuesta_14 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_15 = int(
            input("¿Pido ayuda cuando estoy luchando con un problema.? "))
        respuestas.append(respuesta_15)
        if respuesta_15 < 1 or respuesta_15 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_16 = int(
            input("¿Busco múltiples perspectivas al determinar qué causó un problema.? "))
        respuestas.append(respuesta_16)
        if respuesta_16 < 1 or respuesta_16 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_17 = int(input(
            "¿Pienso en cualquier problema nuevo que podría ser causado por una solución que he propuesto.? "))
        respuestas.append(respuesta_17)
        if respuesta_17 < 1 or respuesta_17 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_18 = int(input(
            "¿Doy seguimiento a las soluciones de los problemas para ver si los efectos fueron positivos.? "))
        respuestas.append(respuesta_18)
        if respuesta_18 < 1 or respuesta_18 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_19 = int(
            input("¿Mantengo un equilibrio productivo entre el trabajo y la vida.? "))
        respuestas.append(respuesta_19)
        if respuesta_19 < 1 or respuesta_19 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_20 = int(input(
            "¿Planeo con anticipación para que sepan en qué se trabajará al día siguiente.? "))
        respuestas.append(respuesta_20)
        if respuesta_20 < 1 or respuesta_20 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_21 = int(input(
            "¿Priorizo bien mi tiempo, para que las tareas más importantes se completen.? "))
        respuestas.append(respuesta_21)
        if respuesta_21 < 1 or respuesta_21 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_22 = int(
            input("¿Busco formas más eficientes de hacer las cosas.? "))
        respuestas.append(respuesta_22)
        if respuesta_22 < 1 or respuesta_22 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_23 = int(
            input("¿Cumplo con los plazos y mantengo mis compromisos.? "))
        respuestas.append(respuesta_23)
        if respuesta_23 < 1 or respuesta_23 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_24 = int(input(
            "¿Busco las perspectivas de los demás para que puedan ver una decisión desde múltiples ángulos.? "))
        respuestas.append(respuesta_24)
        if respuesta_24 < 1 or respuesta_24 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

while True:
    try:
        respuesta_25 = int(input(
            "¿Veo tanto la lógica como las emociones involucradas en la toma de decisiones.? "))
        respuestas.append(respuesta_25)
        if respuesta_25 < 1 or respuesta_25 > 5:
            print("Por favor, ingresa un número entre 1 y 5.")
            time.sleep(1)
            continue
        break
    except ValueError:
        print("ingresa un valor valido valido")
        time.sleep(1)
        continue

# calcula el promedio de las respuestas y da resultado
evaluacion = sum(respuestas) / len(respuestas)
print(f"Hola, {nombre} tu evaluacion es: {evaluacion:.2f}")
if evaluacion >= 3:
    print("¡Felicidades! Tienes buenas soft skills.")
else:
    print("Lo siento, necesitas mejorar tus soft skills.")
