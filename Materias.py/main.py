from materias import signature

ticket = []

while True:
    while True:
        input_name = input("Ingrese el nombre de la materia: ").strip()
        if input_name != "":
            break
        print("Por favor, introduce un nombre válido.")
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

    status = signature(input_name, input_grade)

    ticket.append(status)

    suma = 0
    continuar = input("¿Desea agregar otra materia? (s/n): ")
    if continuar.lower() == "n":
        break
    else:
        continue


for materia in ticket:
    print(f"Materia: {materia.name} | Nota: {materia.grade}")
    suma += materia.grade

promedio = suma / len(ticket)
print(f"PROMEDIO FINAL: {promedio:.2f}")