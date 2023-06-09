# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=32030

### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except

try:
    print(numberOne + numberTwo)
    print("Linea 13 ->","No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Linea 16 ->","Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(numberOne + numberTwo)
    print("Linea 22 ->","No se ha producido un error")
except:
    print("Linea 24 ->","Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("Linea 27 ->","La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("Linea 30 ->","La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("Linea 36 ->","No se ha producido un error")
except ValueError:
    print("Linea 38 ->","Se ha producido un ValueError")
except TypeError:
    print("Linea 40 ->","Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("Linea 46 ->","No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print("Linea 50 ->",my_random_error_name)