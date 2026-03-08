# Importamos las librerías necesarias
import tkinter as tk                      # Librería principal para GUI
from tkinter import ttk, messagebox      # ttk (widgets modernos) y messagebox (ventanas emergentes)
from tkcalendar import DateEntry         # Widget calendario para seleccionar fechas


# Clase principal de la aplicación
class AgendaApp:
    def __init__(self, root):
        # Ventana principal
        self.root = root
        self.root.title("Agenda Personal")   # Título de la ventana
        self.root.geometry("500x400")        # Tamaño de la ventana

        # =======================
        # FRAME: LISTA DE EVENTOS
        # =======================
        # Creamos un contenedor para la tabla
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)  # Se coloca con un margen vertical

        # Definimos las columnas de la tabla
        columnas = ("Fecha", "Hora", "Descripción")

        # Creamos el TreeView (tabla)
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")

        # Configuramos encabezados y ancho de columnas
        for col in columnas:
            self.tree.heading(col, text=col)   # Nombre de la columna
            self.tree.column(col, width=150)   # Ancho de cada columna

        self.tree.pack()  # Mostramos la tabla

        # =======================
        # FRAME: ENTRADA DE DATOS
        # =======================
        # Contenedor para los campos de entrada
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        # ----- Campo Fecha -----
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5)

        # DateEntry crea un calendario desplegable
        self.fecha_entry = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5)

        # ----- Campo Hora -----
        tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5)

        # Entrada de texto para la hora
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5)

        # ----- Campo Descripción -----
        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5)

        # Entrada de texto más larga
        self.descripcion_entry = tk.Entry(frame_entrada, width=40)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5)

        # =======================
        # FRAME: BOTONES
        # =======================
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        # Botón para agregar evento
        tk.Button(frame_botones, text="Agregar Evento",
                  command=self.agregar_evento).grid(row=0, column=0, padx=10)

        # Botón para eliminar evento seleccionado
        tk.Button(frame_botones, text="Eliminar Evento Seleccionado",
                  command=self.eliminar_evento).grid(row=0, column=1, padx=10)

        # Botón para cerrar la aplicación
        tk.Button(frame_botones, text="Salir",
                  command=root.quit).grid(row=0, column=2, padx=10)

    # =======================
    # FUNCIÓN: AGREGAR EVENTO
    # =======================
    def agregar_evento(self):
        # Obtenemos los valores ingresados por el usuario
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validamos que no haya campos vacíos
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return  # Salimos de la función

        # Insertamos el nuevo evento en la tabla
        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))

        # Limpiamos los campos después de agregar
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    # =======================
    # FUNCIÓN: ELIMINAR EVENTO
    # =======================
    def eliminar_evento(self):
        # Obtenemos el elemento seleccionado
        seleccionado = self.tree.selection()

        # Si no hay selección, mostramos advertencia
        if not seleccionado:
            messagebox.showwarning("Selección vacía", "Selecciona un evento para eliminar.")
            return

        # Confirmación antes de eliminar
        confirmacion = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Estas seguro que deseas eliminar el evento?"
        )

        # Si el usuario confirma, eliminamos
        if confirmacion:
            for item in seleccionado:
                self.tree.delete(item)


# =======================
# EJECUCIÓN DEL PROGRAMA
# =======================
if __name__ == "__main__":
    root = tk.Tk()           # Creamos la ventana principal
    app = AgendaApp(root)    # Instanciamos la aplicación
    root.mainloop()          # Ejecutamos el bucle principal