# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### Operadores Aritméticos ###

# Operaciones con enteros
print("Linea 6 -> ",3 + 4) #7
print("Linea 7 -> ",3 - 4) #-1
print("Linea 8 -> ",3 * 4) #12
print("Linea 9 -> ",3 / 4) #0.75
print("Linea 10 -> ",10 % 3) #1
print("Linea 11 -> ",10 // 3) #3
print("Linea 12 -> ",2 ** 3) #8
print("Linea 13 -> ",2 ** 3 + 3 - 7 / 1 // 4) #10.0

# Operaciones con cadenas de texto
print("Linea 16 -> ","Hola " + "Python " + "¿Qué tal?") #Hola Python ¿Qué tal?
print("Linea 17 -> ","Hola " + str(5)) #Hola 5

# Operaciones mixtas
print("Linea 20 -> ","Hola " * 5) #Hola Hola Hola Hola Hola
print("Linea 21 -> ","Hola " * (2 ** 3)) #Hola Hola Hola Hola Hola Hola Hola Hola

my_float = 2.5 * 2
print("Linea 22 -> ","Hola " * int(my_float)) #Hola Hola Hola Hola Hola

### Operadores Comparativos ###

# Operaciones con enteros
print("Linea 29 -> ",3 > 4) #False
print("Linea 30 -> ",3 < 4) #True
print("Linea 31 -> ",3 >= 4) #False
print("Linea 32 -> ",4 <= 4) #True
print("Linea 33 -> ",3 == 4) #False
print("Linea 34 -> ",3 != 4) #True

# Operaciones con cadenas de texto
print("Linea 37 -> ","Hola" > "Python") #False
print("Linea 38 -> ","Hola" < "Python") #True
print("Linea 39 -> ","abaa" >= "aaaa") #False  # Ordenación alfabética por ASCII
print("Linea 40 -> ", len("aaaa") >= len("abaa")) #True  # Cuenta caracteres
print("Hola" <= "Python") #True
print("Hola" == "Hola") #True
print("Hola" != "Python") #True

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))