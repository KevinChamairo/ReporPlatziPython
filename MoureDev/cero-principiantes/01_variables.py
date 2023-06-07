# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###

my_string_variable = "My String variable"
print("Linea 6 -> ",my_string_variable) 
#My String variable

my_int_variable = 5
print(my_int_variable)
#5

my_int_to_str_variable = str(my_int_variable)
print("Linea 14 -> ",my_int_to_str_variable)
#5
print(type(my_int_to_str_variable))
#<class 'str'>

my_bool_variable = False
print(my_bool_variable)
#False

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
#Se queda con el ultimo tpo chancado "<class 'float'>"
print(type(address))