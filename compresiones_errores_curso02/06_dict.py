import random
countries = ['col', 'mex', 'bol', 'pe']
population_v2 = { country: random.randint(1, 100)  for country in countries}
print("cuarto dictionary: ",population_v2)

result = { country: population for (country, population) in population_v2.items() 
          if population > 90}

print(result)


text = 'Hola, soy Nicolasu'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)

frecuencia = { c: text.count(c) for c in text if c in 'aeiou' }
print(frecuencia)

# def run():
#     text = "Hola a todos, esta es una cadena de texto de prueba."
#     print(text)
#     unique = { c: text.count(c) for c in text if c in 'aeiou' }
#     print(f"unique: {unique}")

# if __name__ == '__main__':
#     run()

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [number for number in numbers if number % 2 == 0]

print('v2 =>', even_numbers_v2)

#DIFERENCIAS ENTRE LIST-TUPLE y SET
#List Mutable-Ordenado-Indexing/Slicing-Duplicar elementos
#Tuple Ordenado-Indexing/Slicing-Duplicar elementos
#Set Mutable

a = {1,2}
b = {2,3}
print(a | b)

def sum(a = 1, b = 0):
  return a + b

print(sum(b=5))
