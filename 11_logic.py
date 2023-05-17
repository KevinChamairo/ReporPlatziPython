# and
print('AND')
print('True and True =>', True and True)
print('True and True =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

# Otra manera
# num = int(input("Dime un numero: "))

print(stock >= 100 and stock <= 1000)

print('OR')
print('True or True =>', True or True)
print('True or True =>', True or False)
print('True or True =>', False or True)
print('True or True =>', False or False)

role = input('Digita el rol => ')
print(role == 'admin' or role == 'seller')