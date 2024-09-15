class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado")
        else:
            print("Libro no disponible")

    def devolver(self):
        self.disponible = True
        print("Libro devuelto")

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.prestamos = []

    def prestar_libro(self, libro):
        if libro.disponible:
            self.prestamos.append(libro)
            libro.prestar()
            print(f"{self.nombre} ha prestado el libro {libro.titulo}")
        else:
            print("El libro no está disponible")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.categorias = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def prestar_libro(self, usuario, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            usuario.prestar_libro(libro)
        else:
            print("Libro no encontrado")

# Ejemplo de uso:
biblioteca = Biblioteca()

libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", "Fantasía", "9780261102358")
libro2 = Libro("1984", "George Orwell", "Ciencia ficción", "9780451524935")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario("Juan Pérez", "123456789")
biblioteca.agregar_usuario(usuario1)

biblioteca.prestar_libro(usuario1, "El señor de los anillos")