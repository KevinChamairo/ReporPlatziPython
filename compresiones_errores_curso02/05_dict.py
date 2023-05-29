#El dict o dictionary tiene key: value
'''
dict = {}
for i in range(1, 5):
  dict[i] = i * 1

print("primer dictionary: ",dict)

dict_v2 = { i: i * 2 for i in range(1, 5)}
print("segundo dictionary: ",dict_v2)

import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1, 50)

print("tercer dictionary: ",population)

population_v2 = { country: random.randint(1, 100)  for country in countries}
print("cuarto dictionary: ",population_v2)
'''

#FORMA NUMERO 1
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

#Con el zip se comprimen dos listas a un Object, y con el list se pueden visualizar de la siguiente manera:
# [('nico',12),('zule',56),('santi',98)]
print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

#FORMA NUMERO 2
names2 = ['nico', 'zule', "santi"]
edades = [12,56,98]
new_dict2 = {names2[i]:edades[i] for i in range(len(names2))}
new_dict3 = {names2[i]:edades[i] for i in range(0,len(names2))}
print(new_dict2)
print(new_dict3)