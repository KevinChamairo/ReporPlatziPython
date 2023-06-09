# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=21442

### Conditionals ###

# if

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Linea 10 ->","Se ejecuta la condición del if")
else:
    print("Linea 12 ->","Entra aquí porque my_condition es False")

my_condition = 5 * 5

if my_condition == 10:
    print("Linea 17 ->","Se ejecuta la condición del segundo if")

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Linea 22 ->","Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Linea 24 ->","Es igual a 25")
else:
    print("Linea 26 ->","Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("Linea 28 ->","La ejecución continúa")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Linea 35 ->","Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Linea 38 ->","Estas cadenas de texto coinciden")