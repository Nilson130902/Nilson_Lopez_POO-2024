class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado_a = None

    def esta_prestado(self):
        return self.prestado_a is not None

    def prestar(self, usuario):
        if not self.esta_prestado():
            self.prestado_a = usuario
            return True
        else:
            return False

    def devolver(self):
        if self.esta_prestado():
            self.prestado_a = None
            return True
        else:
            return False

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def agregar_libro(self, libro):
        self.catalogo[libro.isbn] = libro

    def buscar_libro(self, isbn):
        if isbn in self.catalogo:
            return self.catalogo[isbn]
        else:
            return None

    def prestar_libro(self, isbn, usuario):
        libro = self.buscar_libro(isbn)
        if libro:
            return libro.prestar(usuario)
        else:
            return False

    def devolver_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            return libro.devolver()
        else:
            return False


# Ejemplo de uso del sistema de gestión de biblioteca
if __name__ == "__main__":
    # Crear algunos libros
    libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", "9788445075717")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "9788437604947")
    libro3 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "9788478884455")

    # Crear usuarios
    usuario1 = Usuario("Juan")
    usuario2 = Usuario("María")

    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Agregar libros al catálogo de la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Mostrar catálogo inicial
    print("Catálogo inicial de la biblioteca:")
    for isbn, libro in biblioteca.catalogo.items():
        print(libro)

    # Juan toma prestado "El señor de los anillos"
    biblioteca.prestar_libro("9788445075717", usuario1)

    # María intenta tomar prestado "Cien años de soledad" (ya prestado)
    resultado_prestamo = biblioteca.prestar_libro("9788437604947", usuario2)
    if resultado_prestamo:
        print("María ha tomado prestado 'Cien años de soledad'.")
    else:
        print("No se pudo prestar 'Cien años de soledad'. Está prestado actualmente.")

    # Juan devuelve "El señor de los anillos"
    biblioteca.devolver_libro("9788445075717")

    # Mostrar catálogo actualizado
    print("\nCatálogo actualizado de la biblioteca:")
    for isbn, libro in biblioteca.catalogo.items():
        estado = "Disponible" if not libro.esta_prestado() else f"Prestado a {libro.prestado_a}"
        print(f"{libro} - Estado: {estado}")

