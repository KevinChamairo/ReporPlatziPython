#propiedades de conjuntos:
#Se pueden modificar
#No tienen un orden
#No permite duplicados

# no tiene un par key-value, así me doy cuenta que es un set, un conjunto.
set_countries = {'col', 'mex', 'bol'}
print("Linea 8 --->",set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print("Linea 12 --->",set_numbers)

# puede ser mixto. El set se ordena solo, lo importante es lo que tengo dentro.
set_types = {1, 'hola', False, 12.12}
print("Linea 16 --->",set_types)

# la podemos crear a partir de un string
set_from_string = set('hoola')
print("Linea 20 --->",set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print("Linea 23 --->",set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print("Linea 27 --->",set_numbers)
unique_numbers = list(set_numbers)
print("Linea 29 --->",unique_numbers)

# si yo pongo algo repetido, él me lo quita al imprimir
set_countries2 = {'col', 'mex', 'bol', 'col'}
print (set_countries2) # {'col', 'mex', 'bol'}

# la podemos crear a partir de una tupla
set_from_tuples = set (('abc','cbv','as','abc'))
print (set_from_tuples) # {'as', 'abc', 'cbv'}