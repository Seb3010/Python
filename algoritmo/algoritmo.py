import time

with open("algoritmo/words.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

palabras = []

while True:
    while True:
        texto = input("Introduce el texto ").strip()
        texto_1 = len(texto)
        if texto_1 == 0:
            time.sleep(1)
            print("introduzca un texto")
            time.sleep(1)
            continue
        else:
            break

    for palabra in texto.split():
        if palabra in contenido:
            palabras.append("descartar")
        else:
            palabras.append("aceptar")

    if "descartar" in palabras:
            print("descartar")
    else:
        print("Aceptar")

    while True:
        continuar = input("¿Quieres continuar?")
        continuar_1 = len(continuar)
        if continuar_1 == 0:
            print("introduzca si o no")
            continue
        else:
            break

    if continuar == "si":
        continue
    else:
        break