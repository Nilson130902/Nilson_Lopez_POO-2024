import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("400x400")

        # Frame para la entrada y el botón de añadir tarea
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Entrada de texto para añadir nuevas tareas
        self.task_entry = tk.Entry(self.frame, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind('<Return>', self.add_task)  # Atajo para "Enter"

        # Botón para añadir tarea
        self.add_button = tk.Button(self.frame, text="Añadir tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Lista para mostrar tareas
        self.task_listbox = tk.Listbox(root, height=15, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Frame para botones de acción
        self.action_frame = tk.Frame(root)
        self.action_frame.pack()

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(self.action_frame, text="Tarea completada", command=self.mark_completed)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.action_frame, text="Borrar tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Atajos de teclado
        root.bind('<Delete>', self.delete_task)  # Atajo para eliminar tarea
        root.bind('<d>', self.delete_task)  # Atajo para eliminar tarea (tecla D)
        root.bind('<c>', self.mark_completed)  # Atajo para completar tarea (tecla C)
        root.bind('<Escape>', lambda event: root.quit())  # Cerrar la app con tecla Escape

    # Función para añadir tarea
    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Por favor ingrese tarea.")

    # Función para marcar tarea como completada
    def mark_completed(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"{task} (Completo)")
        except IndexError:
            messagebox.showwarning("Selection Error", "Porfavor seleccione una tarea completada.")

    # Función para eliminar tarea
    def delete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Porfavor seleccione una tarea para borrar.")


# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()