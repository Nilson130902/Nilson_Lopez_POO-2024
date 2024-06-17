#Programacion tradicional
def ingresar_temperaturas():
  #Función para ingresar las temperaturas diarias de la semana.

  temperaturas = []
  for i in range(7):
    temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
    temperaturas.append(temperatura)
  return temperaturas
#Función para calcular el promedio de temperaturas semanales.
def calcular_promedio(temperaturas):

  promedio = sum(temperaturas) / len(temperaturas)
  return promedio

# Programa principal
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)

#impresion del resultado del promedio semanal
print(f"El promedio semanal de temperaturas es: {promedio:.2f}")
