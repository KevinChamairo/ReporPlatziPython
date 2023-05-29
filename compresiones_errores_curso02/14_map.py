# MAP( )
# La función map () ejecuta una función especifica para cada 
# elemento en un iterable y el elemento se envía a la 
# función como un parámetro.

# Sintaxis.
# map(function, iterables)

# Con esto vamos hacer unos deliciosos tacos, para ello utilizáremos maps()

def ingredientes(a, b):
  return a + " es a " + b

menu = list(map(ingredientes, ('carne', 'maiz', 'aguacate'), ('molida', 'tacos', 'guacamole')))

print(list(menu))

#CLASE MAP
numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

numbers_v3 = map(lambda i: i * 2, numbers)

print("LINEA 26: ",numbers)
print("LINEA 27: ",numbers_v2)
print("LINEA 28: ",numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 16, 7]

print("LINEA 33: ",numbers_1)
print("LINEA 34: ",numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print("LINEA 36: ",result)