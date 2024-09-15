
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}"

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = set()

    class Libro:
        def __init__(self, titulo, autor, categoria, isbn):
            self.titulo_autor = (titulo, autor)
            self.categoria = categoria
            self.isbn = isbn

    class Usuario:
        def __init__(self, nombre, id_usuario):
            self.nombre = nombre
            self.id_usuario = id_usuario
            self.libros_prestados = []

    class Biblioteca:
        def __init__(self):
            self.libros = {}
            self.usuarios = set()

        def agregar_libro(self, libro):
            self.libros[libro.isbn] = libro

        def quitar_libro(self, isbn):
            if isbn in self.libros:
                del self.libros[isbn]

        def registrar_usuario(self, usuario):
            self.usuarios.add(usuario.id_usuario)

        def dar_de_baja_usuario(self, id_usuario):
            self.usuarios.remove(id_usuario)

        def prestar_libro(self, isbn, id_usuario):
            if isbn in self.libros:
                libro = self.libros[isbn]
                for usuario in self.usuarios:
                    if usuario.id_usuario == id_usuario:
                        usuario.libros_prestados.append(libro)
                        break

        def devolver_libro(self, isbn, id_usuario):
            for usuario in self.usuarios:
                if usuario.id_usuario == id_usuario:
                    for i, libro in enumerate(usuario.libros_prestados):
                        if libro.isbn == isbn:
                            usuario.libros_prestados.pop(i)
                            break

        def buscar_libros(self, query):
            resultados = []
            for libro in self.libros.values():
                if query in libro.titulo_autor[0] or query in libro.titulo_autor[1] or query in libro.categoria:
                    resultados.append(libro)
            return resultados

        def listar_libros_prestados(self, id_usuario):
            for usuario in self.usuarios:
                if usuario.id_usuario == id_usuario:
                    return usuario.libros_prestados

# Ejemplo de uso:
biblioteca = Biblioteca()

libro1 = Libro("Don Quijote", ("Cervantes", "Miguel de"), "Literatura", "978-84-206-6223-2")
biblioteca.añadir_libro(libro1)

usuario1 = Usuario("Juan Pérez", 1)
biblioteca.registrar_usuario(usuario1)

biblioteca.prestar_libro(libro1.isbn, usuario1.id_usuario)