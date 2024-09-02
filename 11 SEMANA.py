class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}  # Usamos un diccionario para un acceso rápido por ID

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        del self.productos[id]

    def actualizar_producto(self, id, nuevo_nombre=None, nueva_cantidad=None, nuevo_precio=None):
        producto = self.productos.get(id)
        if producto:
            if nuevo_nombre:
                producto.nombre = nuevo_nombre
            if nueva_cantidad:
                producto.cantidad = nueva_cantidad
            if nuevo_precio:
                producto.precio = nuevo_precio

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                yield producto

    def mostrar_todos_los_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        import pickle
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)

    def cargar_inventario(self, archivo):
        import pickle
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
        except FileNotFoundError:
            print("Archivo no encontrado")

# Crear un inventario
inventario = Inventario()

# Crear productos y agregarlos al inventario
producto1 = Producto(1, "Manzana", 100, 2.5)
producto2 = Producto(2, "Banana", 50, 1.5)
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

# Buscar un producto
for producto in inventario.buscar_producto("ana"):
    print(producto)

# Guardar el inventario
inventario.guardar_inventario("inventario.pkl")

# Cargar el inventario
inventario.cargar_inventario("inventario.pkl")