# Importamos la librería Tkinter
import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada.get()  # Obtener texto del campo
    if dato != "":
        lista.insert(tk.END, dato)  # Agregar a la lista
        entrada.delete(0, tk.END)   # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato")

# Función para limpiar elemento seleccionado
def limpiar_dato():
    seleccion = lista.curselection()
    if seleccion:
        lista.delete(seleccion)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un elemento para eliminar")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicando GUI")
ventana.geometry("500x400")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón agregar
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Botón limpiar
btn_limpiar = tk.Button(ventana, text="Eliminar seleccionado", command=limpiar_dato)
btn_limpiar.pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()