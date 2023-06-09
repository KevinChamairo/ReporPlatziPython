# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print("Linea 10 -> ",type(my_dict)) #<class 'dict'>
print("Linea 11 -> ",type(my_other_dict)) #<class 'dict'>

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print("Linea 24 -> ",my_other_dict) #{'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}
print("Linea 25 -> ",my_dict) #{'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Python', 'Kotlin', 'Swift'}, 1: 1.77}

print("Linea 27 -> ",len(my_other_dict)) #4
print("Linea 28 -> ",len(my_dict)) #5

# Búsqueda

print("Linea 32 -> ",my_dict[1]) #1.77
print("Linea 33 -> ",my_dict["Nombre"]) #Brais

print("Linea 35 -> ","Moure" in my_dict) #False
print("Linea 36 -> ","Apellido" in my_dict) #True

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print("Linea 41 -> ",my_dict) #{'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Kotlin', 'Python', 'Swift'}, 1: 1.77, 'Calle': 'Calle MoureDev'}

# Actualización

# my_dict["Nombre"] = "Pedro"
my_dict["Nombre"] = "Pedro" #Chanca el valor de Brais por el de Pedro
print("Linea 47 -> ",my_dict["Nombre"]) #Pedro

# Eliminación

del my_dict["Calle"]
print("Linea 52 -> ",my_dict) #De {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Kotlin', 'Python', 'Swift'}, 1: 1.77, 'Calle': 'Calle MoureDev'}

#Pasa a {'Nombre': 'Pedro', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Swift', 'Python', 'Kotlin'}, 1: 1.77}

# Otras operaciones

print("Linea 58 -> ",my_dict.items()) #dict_items([('Nombre', 'Pedro'), ('Apellido', 'Moure'), ('Edad', 35), ('Lenguajes', {'Swift', 'Python', 'Kotlin'}), (1, 1.77)])
print("Linea 59 -> ",my_dict.keys()) #dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1])
print("Linea 60 -> ",my_dict.values()) #dict_values(['Pedro', 'Moure', 35, {'Swift', 'Python', 'Kotlin'}, 1.77])

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print("Linea 65 -> ",my_new_dict) #{'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print("Linea 67 -> ",(my_new_dict)) #{'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(my_dict)
print("Linea 69 -> ",(my_new_dict)) #{'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print("Linea 71 -> ",(my_new_dict)) #{'Nombre': 'MoureDev', 'Apellido': 'MoureDev', 'Edad': 'MoureDev', 'Lenguajes': 'MoureDev', 1: 'MoureDev'}

my_values = my_new_dict.values()
print("Linea 74 -> ",type(my_values)) #<class 'dict_values'>

print("Linea 76 -> ",my_new_dict.values()) #dict_values(['MoureDev', 'MoureDev', 'MoureDev', 'MoureDev', 'MoureDev'])
print("Linea 77 -> ",list(dict.fromkeys(list(my_new_dict.values())).keys())) #['MoureDev']
print("Linea 78 -> ",tuple(my_new_dict)) #('Nombre', 'Apellido', 'Edad', 'Lenguajes', 1)
print("Linea 79 -> ",set(my_new_dict)) #{'Lenguajes', 'Edad', 1, 'Nombre', 'Apellido'}