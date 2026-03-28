import tkinter as tk
from tkinter import messagebox
from typing import Any, List

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tareas Pendientes")

        # Lista de tareas con anotación de tipo para evitar advertencias
        self.tasks: List[dict[str, Any]] = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.add_btn = tk.Button(btn_frame, text="Añadir", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Realizada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Atajos de teclado: usar combinaciones con Ctrl para evitar interferir al escribir
        self.root.bind("<Return>", self.add_task)
        self.root.bind("<Control-c>", self.complete_task)
        self.root.bind("<Delete>", self.delete_task)
        self.root.bind("<Control-d>", self.delete_task)

    def add_task(self, event=None):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Escriba una tarea.")

    def complete_task(self, event=None):
        try:
            index: int = int(self.listbox.curselection()[0])
            self.tasks[index]["completed"] = True
            self.update_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")
        except (TypeError, ValueError):
            # Curselection puede devolver strings no convertibles o no haber selección
            messagebox.showwarning("Advertencia", "Selecciona una tarea válida.")

    def delete_task(self, event=None):
        try:
            index: int = int(self.listbox.curselection()[0])
            del self.tasks[index]
            self.update_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")
        except (TypeError, ValueError):
            messagebox.showwarning("Advertencia", "Selecciona una tarea válida.")

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["completed"]:
                self.listbox.insert(tk.END, "✔ " + task["text"])
                self.listbox.itemconfig(tk.END, fg="gray")
            else:
                self.listbox.insert(tk.END, "☐ " + task["text"])
                self.listbox.itemconfig(tk.END, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()