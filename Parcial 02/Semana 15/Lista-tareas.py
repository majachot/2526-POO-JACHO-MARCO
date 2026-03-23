import tkinter as tk
from tkinter import messagebox

class TareaApp:
    def __init__(self, root):
        """
        Constructor de la aplicación.
        Inicializa la ventana principal y todos los componentes GUI.
        """
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista interna que almacena las tareas
        # Cada tarea es una tupla: (texto, estado_completado)
        self.tasks = []

        # ----------------------------
        # Campo de entrada (Entry)
        # ----------------------------
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento: presionar Enter para añadir tarea
        self.entry.bind("<Return>", self.add_task_event)

        # ----------------------------
        # Botones
        # ----------------------------
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.add_btn = tk.Button(
            btn_frame, text="Añadir Tarea", command=self.add_task
        )
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(
            btn_frame,
            text="Marcar como Completada",
            command=self.complete_task
        )
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(
            btn_frame, text="Eliminar Tarea", command=self.delete_task
        )
        self.delete_btn.grid(row=0, column=2, padx=5)

        # ----------------------------
        # Lista de tareas (Listbox)
        # ----------------------------
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=20)

        # Evento opcional: doble clic para completar tarea
        self.listbox.bind("<Double-Button-1>", self.complete_task_event)

    # ============================
    # MÉTODOS DE LÓGICA
    # ============================

    def add_task(self):
        """
        Añade una nueva tarea a la lista.
        Valida que el campo no esté vacío.
        """
        task_text = self.entry.get().strip()

        if task_text == "":
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")
            return

        # Se añade como no completada (False)
        self.tasks.append((task_text, False))

        self.update_listbox()
        self.entry.delete(0, tk.END)

    def add_task_event(self, event):
        """
        Manejador de evento para la tecla Enter.
        Llama al método add_task().
        """
        self.add_task()

    def complete_task(self):
        """
        Marca la tarea seleccionada como completada.
        """
        selected = self.listbox.curselection()

        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")
            return

        index = selected[0]
        text, completed = self.tasks[index]

        # Cambia el estado a completado
        self.tasks[index] = (text, True)

        self.update_listbox()

    def complete_task_event(self, event):
        """
        Evento de doble clic en la lista.
        Marca la tarea como completada.
        """
        self.complete_task()

    def delete_task(self):
        """
        Elimina la tarea seleccionada de la lista.
        """
        selected = self.listbox.curselection()

        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")
            return

        index = selected[0]
        del self.tasks[index]

        self.update_listbox()

    def update_listbox(self):
        """
        Actualiza la visualización de la lista de tareas.
        Muestra un símbolo diferente según el estado.
        """
        self.listbox.delete(0, tk.END)

        for task, completed in self.tasks:
            if completed:
                self.listbox.insert(tk.END, f"✔ {task}")
            else:
                self.listbox.insert(tk.END, f"✗ {task}")


# ============================
# EJECUCIÓN DE LA APP
# ============================

if __name__ == "__main__":
    root = tk.Tk()
    app = TareaApp(root)
    root.mainloop()