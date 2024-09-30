import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, master):
        self.master = master
        master.title("Lista de Tareas")

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Botones
        self.add_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()
        self.complete_button = tk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack()
        self.delete_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        # Lista de tareas
        self.task_list = tk.Listbox(master)
        self.task_list.pack()

        # Lista para almacenar las tareas
        self.tasks = []

        # Asociar el evento Enter del Entry con la función de agregar tarea
        self.entry.bind("<Return>", self.add_task)

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def complete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.tasks.pop(selected_index[0])
            self.task_list.delete(selected_index)
            # Aquí podrías agregar lógica para marcar la tarea como completada en una base de datos, etc.
            messagebox.showinfo("Tarea Completada", f"La tarea '{task}' ha sido marcada como completada.")

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.task_list.delete(selected_index)

root = tk.Tk()
app = TaskApp(root)
root.mainloop()