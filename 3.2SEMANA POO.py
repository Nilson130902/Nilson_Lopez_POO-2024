#PROGRAMACION ORIENTADA A OBJETO
class DiaClima:
  #Clase para la información del clima.
  def __init__(self, temperatura):
      #temperatura: La temperatura del día.
    self.temperatura = temperatura
  def ingresar_temperatura(self):
    #Método para ingresar la temperatura del día.
    self.temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))

  def obtener_temperatura(self):
    #Método para obtener la temperatura del día.

    return self.temperatura

class RegistroSemanal:

  #Clase que representa un registro semanal de información climática.

  def __init__(self):
    self.dias = []

  def agregar_dia(self, dia_clima):

    #Método para agregar un objeto `DiaClima` al registro semanal.

    self.dias.append(dia_clima)

  def calcular_promedio(self):
    #Método para calcular el promedio semanal de temperaturas.

    if not self.dias:
      raise Exception("No hay datos para calcular el promedio")

    temperaturas = [dia_clima.obtener_temperatura() for dia_clima in self.dias]
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Programa principal
registro_semanal = RegistroSemanal()

for dia in range(1,8):
  dia_clima = DiaClima(0)
  dia_clima.ingresar_temperatura()
  registro_semanal.agregar_dia(dia_clima)

promedio = registro_semanal.calcular_promedio()
print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

