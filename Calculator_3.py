import tkinter as tk
from tkinter import messagebox
import math

def calcular():
    operacion = var_opcion.get()
    entradas = entry_numeros.get()

    # Convertir la entrada en lista de números (separados por comas)
    try:
        numeros = [float(x.strip()) for x in entradas.split(",") if x.strip() != '']
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números separados por comas")
        return

    if operacion in ["suma", "resta", "multiplicacion", "division"]:
        if len(numeros) < 2:
            messagebox.showerror("Error", "Se requieren al menos dos números")
            return

    if operacion == "suma":
        resultado = round(sum(numeros), 2)

    elif operacion == "resta":
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado -= n
        resultado = round(resultado, 2)

    elif operacion == "multiplicacion":
        resultado = 1
        for n in numeros:
            resultado *= n
        resultado = round(resultado, 2)

    elif operacion == "division":
        resultado = numeros[0]
        for n in numeros[1:]:
            if n == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero")
                return
            resultado /= n
        resultado = round(resultado, 2)

    elif operacion == "potencia":
        if len(numeros) != 1:
            messagebox.showerror("Error", "Solo ingresa un número para potencia")
            return
        resultado = round(pow(numeros[0], 2), 2)

    elif operacion == "raiz":
        if len(numeros) != 1:
            messagebox.showerror("Error", "Solo ingresa un número para raíz cuadrada")
            return
        if numeros[0] < 0:
            messagebox.showerror("Error", "No se puede calcular la raíz cuadrada de un número negativo")
            return
        resultado = round(math.sqrt(numeros[0]), 2)

    label_resultado.config(text=f"Resultado: {resultado}")

# Ventana principal
root = tk.Tk()
root.title("Calculadora con Tkinter")

# Variable para la opción seleccionada
var_opcion = tk.StringVar(value="suma")

# Opciones para la operación
operaciones = [("Suma", "suma"), 
              ("Resta", "resta"), 
              ("Multiplicación", "multiplicacion"),
              ("División", "division"),
              ("Potencia (al cuadrado)", "potencia"),
              ("Raíz cuadrada", "raiz")]

tk.Label(root, text="Selecciona la operación:").pack()

for texto, valor in operaciones:
    tk.Radiobutton(root, text=texto, variable=var_opcion, value=valor).pack(anchor="w")

tk.Label(root, text="Ingresa números separados por coma (,):").pack()
entry_numeros = tk.Entry(root, width=40)
entry_numeros.pack()

boton = tk.Button(root, text="Calcular", command=calcular)
boton.pack(pady=10)

label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.pack()

root.mainloop()