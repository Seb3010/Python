class Activo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def ganancia(self, precio_actual):
        self.precio_actual = 50000
        return precio_actual - self.precio
        if precio_actual < self. precio:
            return True
        else:
            return False
while True:
    nombre = input("Ingrese el nombre del activo: ")
    try:
        if nombre == "":
            print("Por favor, introduce un nombre.")
            continue
    except:
        break
    precio = float(input("Ingrese el precio del activo: "))
    try:
        if precio == "":
            print("Por favor, introduce un precio.")
            continue
    except:
        break

    print("Ficha del activo:")
    Activo = Activo(nombre, precio)
    print(f"Nombre: {Activo.nombre}")
    print(f"Precio: {Activo.precio}")
    print(f"Precio actual: {Activo.precio_actual}")
    
    if Activo.ganancia(precio_actual) == True:
        print("El activo ha tenido Perdida.")
        print(f"La perdida es de: {Activo.ganancia(precio_actual)}")
    else:
        print("El activo ha tenido Ganancia.")
        print(f"La ganancia es de: {Activo.ganancia(precio_actual)}")
    
    continuar = input("¿quieres continuar? (s/n)")
    if continuar == "n":
        break
    else:
        continue