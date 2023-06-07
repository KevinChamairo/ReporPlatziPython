# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711

### Tuples ###

# Definición

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print("Linea 13 -> ",my_tuple.count("Brais")) #Habla de cuantas veces se repite en la tupla "Brais", en este caso son 2
print("Linea 14 -> ",my_tuple) #(35, 1.77, 'Brais', 'Moure', 'Brais')
print("Linea 15 -> ",type(my_tuple)) #Imprime <class 'tuple'>

# Acceso a elementos y búsqueda

print("Linea 19 -> ",my_tuple[0]) #35
print("Linea 20 -> ",my_tuple[-2]) #Moure 
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Brais")) #2 #Hay 2 "Brais" en la tupla
print(my_tuple.index("Moure")) #3 #"Moure" se encuentra en el íncide 3
print(my_tuple.index("Brais")) #2 #"Brais" se encuentra en el íncide 2

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print("Linea 33 -> ",my_sum_tuple) #Concatenamos las 2 tuplas, quedaría: (35, 1.77, 'Brais', 'Moure', 'Brais', 35, 60, 30)

# Subtuplas

print("Linea 37 -> ",my_sum_tuple[3:6]) #Solo queda del valor 3 al 6: ('Moure', 'Brais', 35)

# Tupla mutable con conversión a lista
 
my_tuple = list(my_tuple) #Lo transformamos a lista la tupla
print("Linea 42 -> ",type(my_tuple)) #Printemaos el tipo: <class 'list'>
print("Linea 43 -> ", my_tuple) #Printemaos el tipo: [35, 1.77, 'Brais', 'Moure', 'Brais']

my_tuple[4] = "MoureDev" #chancamos el valor 4 de la tupla
my_tuple.insert(1, "Azul") 
my_tuple = tuple(my_tuple)
print("Linea 48 -> ",my_tuple) #Quedaría: (35, 'Azul', 1.77, 'Brais', 'Moure', 'MoureDev')
print("Linea 49 -> ",type(my_tuple)) #<class 'tuple'>

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple(0)
# print("Linea 56 -> ",my_tuple)
# print(my_tuple) NameError: name 'my_tuple' is not defined