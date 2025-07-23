import time

def bienvenida():
    print("bienvenido al calculador de promedio")

time.sleep(1)
bienvenida()

while True:
    try:
        num_materias = int(input("¿Cuántas materias tienes? "))
        if num_materias <= 0:
            print("Debes tener al menos una materia.")
            continue
        break
    except ValueError:
       print("Por favor, ingresa un número valido.")
       continue
    
materias = []
calificaciones = []
    
for materia in range(num_materias):
    nombre_materia = input(f"¿Cuál es el nombre de la materia {materia+1}? ")
    materias.append(nombre_materia)
    
    while True:
        try:
            calificacion = float(input(f"¿Cuál es la calificación de {nombre_materia}? "))
            calificaciones.append(calificacion)
            break
        except ValueError:
            print("Por favor, ingresa una calificación válida. ")
            continue
        


promedio = sum(calificaciones) / num_materias
print(f"Tu promedio es: {promedio:.2f}")

if promedio >= 6: 
    print("¡Felicidades! Has aprobado.")
else:
    print("Lo siento, has reprobado.")

continuar = input("¿deseas continuar?")
if continuar == "si":
    print("continuando...")
    bienvenida()
else:
    print("gracias por usar promediando")
    print("hasta luego")
    exit()