with open("algoritmo/words.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

palabras = []

while True:
    try:
        texto = input("Introduce el texto ").strip()
    except ValueError:
        print("introduzca un texto")


    for palabra in texto.split():
        if palabra in contenido:
            palabras.append("descartar")
        else:
            palabras.append("aceptar")

    for texto in palabras:
        if texto == "des"

    continuar = input("¿Quieres continuar?")

    if continuar == "si":
        continue
    else:
        break
