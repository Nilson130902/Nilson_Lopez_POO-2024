def convertir_a_celsius(fahrenheit):
  """
  Convierte una temperatura de Fahrenheit a Celsius.
  """
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius

def convertir_a_fahrenheit(celsius):
  """
  Convierte una temperatura de Celsius a Fahrenheit.

  Args:
    celsius: Valor de temperatura en Celsius (float).

  Returns:
    Valor de temperatura equivalente en Fahrenheit (float).
  """
  fahrenheit = celsius * 9 / 5 + 32
  return fahrenheit

def main():
  """
  Función principal del programa.
  """
  # Obtener la temperatura inicial y la escala de destino del usuario
  temperatura_inicial = float(input("Ingrese la temperatura inicial: "))
  escala_inicial = input("Ingrese la escala inicial (C/F): ").lower()

  # Validar la entrada del usuario
  if escala_inicial not in ["c", "f"]:
    print("Escala no válida. Ingrese 'C' para Celsius o 'F' para Fahrenheit.")
    return

  # Convertir la temperatura a la escala deseada
  if escala_inicial == "c":
    temperatura_convertida = convertir_a_fahrenheit(temperatura_inicial)
    escala_convertida = "F"
  else:
    temperatura_convertida = convertir_a_celsius(temperatura_inicial)
    escala_convertida = "C"

  # Mostrar el resultado de la conversión
  print(f"{temperatura_inicial:.2f} {escala_inicial.upper()} equivale a {temperatura_convertida:.2f} {escala_convertida.upper()}")

if __name__ == "__main__":
  main()
