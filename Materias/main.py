from materias import signature

def pedir_nombre_materia():
    while True:
        input_name = input("Ingrese el nombre de la materia: ").strip()
        if input_name != "":
            break
        print("Por favor, introduce un nombre válido.")
    return input_name

def pedir_calificacion():
    while True:
        try:
            input_grade = int(input("Ingrese la calificacion: "))
            if input_grade < 0 or input_grade > 100:
                print("Por favor, introduce una calificacion valida.")
                continue
            else:
                break
        except ValueError:
            print("Por favor, introduce un numero valido.")
            continue
    return input_grade

ticket = []

while True:
    #variables para agregar parametros al objeto signature
    name = pedir_nombre_materia()
    grade = pedir_calificacion()
    #agrega los parametros al objeto signature
    #y se meten en la variable status
    status = signature(name, grade)
    #agrega el objeto signature a la lista ticket
    #se mete a la lista ticket el objeto signature para poder acceder a los parametros
    ticket.append(status)
    #NO CREAR VARIABLES QUE SE LLAMEN IGUALES QUE LAS CLASES COMO EN ESTE CASO
    #es una mala practica
    #lo mejor seria reparar el codigo pero mejor lo dejo asi para saber que no se tiene que hacer
    continuar = input("¿Desea agregar otra materia? (s/n): ")
    if continuar.lower() == "n":
        break
    else:
        continue

suma = 0
for materia in ticket:
    print(f"Materia: {materia.name} | Nota: {materia.grade} | Estatus: {materia.status()}#")
    suma += materia.grade

promedio = suma / len(ticket)
print(f"PROMEDIO FINAL: {promedio:.2f}")