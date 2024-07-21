class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Persona creada: {self.nombre}, {self.edad} años")

    def __del__(self):
        print(f"Persona eliminada: {self.nombre}")


class Archivo:
    def __init__(self, nombre_archivo, modo):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = open(nombre_archivo, modo)
        print(f"Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'")

    def escribir(self, texto):
        self.archivo.write(texto)

    def __del__(self):
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado")


# Ejemplo de uso de la clase Persona
p = Persona("Juan", 30)
del p  # Esto llamará al destructor explícitamente

# Ejemplo de uso de la clase Archivo
a = Archivo("mi_archivo.txt", "w")
a.escribir("Hola, mundo!")
del a  # Esto llamará al destructor y cerrará el archivo
