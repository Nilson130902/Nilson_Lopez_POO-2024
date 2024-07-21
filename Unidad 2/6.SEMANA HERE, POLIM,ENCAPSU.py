class Figura:

  def __init__(self, color):
    self.color = color

  def calcular_area(self):
    # Este método es abstracto y debe ser implementado por las clases derivadas.
    pass

  def mostrar_informacion(self):
    print(f"Figura: {self.__class__.__name__}")
    print(f"Color: {self.color}")
    print(f"Área: {self.calcular_area()}")

class Circulo(Figura):

  def __init__(self, color, radio):
    super().__init__(color)
    self.radio = radio

  def calcular_area(self):
    return 3.1415 * self.radio ** 2

class Rectangulo(Figura):


  def __init__(self, color, base, altura):
    super().__init__(color)
    self.base = base
    self.altura = altura

  def calcular_area(self):
    return self.base * self.altura
# Crear instancias de las clases
circulo1 = Circulo("rojo", 5.0)
rectangulo1 = Rectangulo("azul", 10.0, 5.0)

# Mostrar información de las figuras
circulo1.mostrar_informacion()
rectangulo1.mostrar_informacion()

# Calcular y mostrar el área del círculo
print(f"Área del círculo: {circulo1.calcular_area()}")

# Calcular y mostrar el área del rectángulo
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")
