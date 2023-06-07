# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()
my_other_list = []

print("Linea 10 -> ",len(my_list)) #0

my_list = [35, 24, 62, 52, 30, 30, 17]

print("Linea 14 -> ",my_list) #[35, 24, 62, 52, 30, 30, 17]
print("Linea 15 -> ",len(my_list)) #7

my_other_list = [35, 1.77, "Brais", "Moure"]

print("Linea 19 -> ",type(my_list)) #<class 'list'>
print("Linea 20 -> ",type(my_other_list)) #<class 'list'>

# Acceso a elementos y búsqueda

print("Linea 24 -> ",my_other_list[0]) #35
print("Linea 25 -> ",my_other_list[1]) #1.77
print("Linea 26 -> ",my_other_list[-1]) #Moure
print("Linea 27 -> ",my_other_list[-4]) #35 - de atrás hacia adelante
print('Count of 30:', my_list.count(30)) #2
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print("Posicion numero:",my_other_list.index("Brais"), "del array") #Posicion numero 2 del array


my_other_list2 = [35, 1.77, "Brais", "Moure"]
age, height, name, surname = my_other_list2 
print("Linea 37 -> ",name) #Brais

name, height, age, surname = my_other_list2[2], my_other_list2[1], my_other_list2[0], my_other_list2[3]
print("Linea 40 -> ",age) #35

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

mipropialista = ["1", "2", "3", "4", "5"]
print("Linea 50 -> ",mipropialista) #["1", "2", "3", "4", "5"]

mipropialista.append("MoureDev")
print("Linea 53 -> ",mipropialista) #Agrega al final "MoureDev", quedaría #['1', '2', '3', '4', '5', 'MoureDev']

mipropialista.insert(1, "Rojo")
print("Linea 56 -> ",mipropialista) #Agrega en la posicion 1 de la lista "Rojo", quedaría ['1', 'Rojo', '2', '3', '4', '5', 'MoureDev']

mipropialista[1] = "Azul"
print("Linea 59 -> ",mipropialista) #Chancamos la posicion 1 de la lista que contiene "Rojo" y la pasamos a "Azul", quedaria ['1', 'Azul', '2', '3', '4', '5', 'MoureDev']

mipropialista.remove("Azul")
print("Linea 62 -> ",mipropialista) #Eliminamos el elemento "Azul", quedaría #['1', '2', '3', '4', '5', 'MoureDev']

milista = [35, 24, 62, 52, 30, 30, 17]
print("Linea 65 -> ",milista) #[35, 24, 62, 52, 30, 30, 17]

milista.remove(30)
print("Linea 68 -> ",milista) #Se elimina un valor 30 de la lista, quedaría así la lista: [35, 24, 62, 52, 30, 17]

print("Linea 70 -> ",milista.pop()) #Con el pop se elimina el último elemento de la lista que tenemos, en este caso es 17
print("Linea 71 -> ",milista) #quedaría #[35, 24, 62, 52, 30]

my_pop_element = milista.pop(2)
print("Linea 74 -> ",my_pop_element) #62 #Despues del pop(2) se agarró y eliminó el antepenultimo elemento de la lista que en este caso fue 62
print("Linea 75 -> ",milista) #Quedó: [35, 24, 52, 30]

del milista[0] #35 #Otra manera de eliminar elementos de la lista en este caso con "del", lo ponemos en la posicion 0 y eliminarpa el valor 35
print("Linea 78 -> ",milista) #Quedó: [24, 52, 30]

# # Operaciones con listas

my_new_list = milista.copy()

milista.clear() #[] #Al hacer clear dejamos el array vacía, osea completamente limpio
print("Linea 85 -> ",milista) #[]
print("Linea 86 -> ",my_new_list) #[24, 52, 30]

my_new_list.reverse() #Pone en reversa la lista de [24, 52, 30]
print("Linea 89 -> ",my_new_list) #quedaría como: [30, 52, 24] 

my_new_list.sort() #Ordenacion de menor a mayor
print("Linea 92 -> ",my_new_list) #quedaría [24, 30, 52]

# # Sublistas

print("Linea 96 -> ",my_new_list[1:3])

# # Cambio de tipo

milista = "Hola Python"
print("Linea 101 -> ",milista)
print("Linea 102 -> ",type(milista))