# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print("Linea 8 -> ",len(my_string)) #9
print("Linea 9 -> ",len(my_other_string)) #14
print("Linea 10 -> ",my_string + " " + my_other_string) #Mi String Mi otro String

my_new_line_string = "Este es un String\ncon salto de línea"
#Este es un String
#con salto de línea
print("Linea 15 -> ",my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" #        Este es un String con tabulación
print("Linea 18 -> ",my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Linea 26 -> ","Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #Mi nombre es Brais Moure y mi edad es 35
print("Linea 27 -> ","Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) #Mi nombre es Brais Moure y mi edad es 35
print("Linea 28 -> ","Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #Mi nombre es Brais Moure y mi edad es 35
print("Linea 29 -> ",f"Mi nombre es {name} {surname} y mi edad es {age}") #Mi nombre es Brais Moure y mi edad es 35

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print("Linea 35 -> ",a) #p
print("Linea 36 -> ",e) #o

# División

language_slice = language[1:3]
print("Linea 41 -> ",language_slice) #yt

language_slice = language[1:]
print("Linea 44 -> ",language_slice) #ython

language_slice = language[-2]
print("Linea 47 -> ",language_slice) #o

language_slice = language[0:6:2]
print("Linea 50 -> ",language_slice) #pto

# Reverse

reversed_language = language[::-1]
print("Linea 55 -> ",reversed_language) #nohtyp

# Funciones del lenguaje

print("Linea 59 -> ",language.capitalize()) #Pone la primera letra en mayúscula
print("Linea 60 -> ",language.upper()) #Pone todo en mayúscula
print("Linea 61 -> ",language.count("t")) #1
print("Linea 62 -> ",language.isnumeric()) #False
print("Linea 63 -> ","1".isnumeric()) #True
print("Linea 64 -> ",language.lower()) #python
print("Linea 65 -> ",language.lower().isupper()) #False
print("Linea 66 -> ",language.capitalize().startswith("Py")) #True
print("Linea 67 -> ","Py" == "py") #False # No es lo mismo