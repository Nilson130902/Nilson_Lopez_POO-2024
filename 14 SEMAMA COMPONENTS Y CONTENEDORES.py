import tkinter as tk
from tkinter import messagebox, ttk

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear el TreeView
        self.tree = ttk.Treeview(root, columns=("fecha", "hora", "descripcion"), show='headings')
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Campos de entrada
        self.fecha_label = tk.Label(root, text="Fecha (DD/MM/AAAA):")
        self.fecha_label.pack()
        self.fecha_entry = tk.Entry(root)
        self.fecha_entry.pack()

        self.hora_label = tk.Label(root, text="Hora (HH:MM):")
        self.hora_label.pack()
        self.hora_entry = tk.Entry(root)
        self.hora_entry.pack()

        self.descripcion_label = tk.Label(root, text="Descripción:")
        self.descripcion_label.pack()
        self.descripcion_entry = tk.Entry(root)
        self.descripcion_entry.pack()

        # Botones
        self.agregar_btn = tk.Button(root, text="Agregar Evento", command=self.agregar_evento)
        self.agregar_btn.pack()

        self.eliminar_btn = tk.Button(root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.eliminar_btn.pack()

        self.salir_btn = tk.Button(root, text="Salir", command=root.quit)
        self.salir_btn.pack()

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un evento para eliminar.")

    def limpiar_campos(self):
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
