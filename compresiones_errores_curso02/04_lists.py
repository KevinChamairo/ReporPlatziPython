#Definimos un array vacio de numeros
'''
numbers = []
for element in range(1,11):
    numbers.append(element)

print("linea 6: ",numbers)

numbers_v2 = [element for element in range(1,11)]

print("linea 10: ",numbers_v2)
'''

numbers = []
for i in range(1,11):
    if i % 2 == 0:
        numbers.append(i * 2)
        
print(numbers)

numbers_v2 = [i * 2 for i in range(1,11) if i%2 == 0]
print(numbers_v2)

#mi solucion
x=int(input('Ingresa cantidad de longitud en "x": '))
y=int(input('Ingresa cantidad de altura en "y": '))
z=int(input('Ingresa cantidad de profundidad: '))
n=int(input('Ingresa numero limitante: '))

list=[[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n]

print(list)