import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Aplicación GUI")

# Crear un label
etiqueta = tk.Label(ventana, text="Ingrese un texto:")
etiqueta.pack()

# Crear un campo de texto
entrada_texto = tk.Entry(ventana)
entrada_texto.pack()

# Crear una lista para mostrar los datos
lista_datos = tk.Listbox(ventana)
lista_datos.pack()

# Función para agregar un elemento a la lista
def agregar_elemento():
    texto = entrada_texto.get()
    lista_datos.insert(tk.END, texto)
    entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear los botones
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack()
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()