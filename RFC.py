print("ingrese sus datos para obtener su RFC")
nombre = input("Nombre: ")
apellido_p = input("apellido paterno: ")
primera_vocal = next(letra for letra in apellido_p if letra in "aeiou")
apellido_m = input("apellido materno: ")
dia = input("dia de nacimiento: ")
mes = input("mes de nacimiento en numero: ")
año = input("año de nacimiento: ")

rfc = apellido_p[0] + primera_vocal + \
    apellido_m[:1] + nombre[:1] + año[2:4] + mes + dia

print("Este es tu rfc")
print(rfc)
