# pedir nombre al usuario, quitar espacios en blanco y poner mayusculas
name = input("¿cual es tu nombre? ").strip().title()
# separar nombre
first, last = name.split(" ")
# decir hola al usuario
print(f"hola, {name} es un gusto en conocerte")
# preguntar al usuario como esta
print(f"¿como estas {first}?")
# respuesta del usuario
input("")
