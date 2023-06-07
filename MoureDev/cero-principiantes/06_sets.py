# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###

# Definición

my_set = set()
my_other_set = {}

print("Linea 10 -> ",type(my_set)) #Tipo set: <class 'set'>
print("Linea 11 -> ",type(my_other_set)) #Tipo: <class 'dict'> # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print("Linea 14 -> ",type(my_other_set)) #Tipo: <class 'set'>

print("Linea 16 -> ",len(my_other_set)) #3

# Inserción

my_other_set.add("MoureDev") #Insertamos el valor "MoureDev"

print("Linea 22 -> ",my_other_set)  #{'Moure', 35, 'Brais', 'MoureDev'} #Un set no es una estructura ordenada

my_other_set.add("MoureDev")  # Un set no admite repetidos

print("Linea 26 -> ",my_other_set) #{'Moure', 35, 'Brais', 'MoureDev'}

# Búsqueda

print("Linea 30 -> ","Moure" in my_other_set) #True
print("Linea 31 -> ","Mouri" in my_other_set) #False

# Eliminación

my_other_set.remove("Moure") #Se quita el valor "Moure"
print("Linea 36 -> ",my_other_set)

my_other_set.clear() #Se limpia todo el set
print("Linea 39 -> ",len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Brais", "Moure", 35} #Establecemos un set
my_list = list(my_set) #Casteamos a list
print("Linea 48 -> ",my_list) #Imprimimos el list: ['Brais', 'Moure', 35]
print("Linea 49 -> ",my_list[0]) #El primer valor del list "Brais"

# my_other_set = {"Kotlin", "Swift", "Python"}

# # Otras operaciones

# my_new_set = my_set.union(my_other_set)
# print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
# print(my_new_set.difference(my_set))

lenguajes = {"Kotlin", "Swift", "Python"}
lenguajes2 = {"Java", "Python"}

# Otras operaciones

mylenguaje = lenguajes2.union(lenguajes)
print("Linea 65 -> ",mylenguaje)

print("Linea 67 -> ",mylenguaje.union(mylenguaje).union(lenguajes2).union({"JavaScript", "C#"}))
print("Linea 68 -> ",mylenguaje.difference(lenguajes2))