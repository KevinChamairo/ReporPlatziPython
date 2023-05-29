items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print("Linea 17: ",items)
print("Linea 18: ",prices)
#IMPRIMEN:
# Linea 17:  [{'product': 'camisa', 'price': 100}, {'product': 'pantalones', 'price': 300}, {'product': 'pantalones 2', 'price': 200}]
# Linea 18:  [100, 300, 200]
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print("Linea 25: ",new_items)
#IMPRIME: Linea 25:  [{'product': 'camisa', 'price': 100, 'taxes': 19.0}, {'product': 'pantalones', 'price': 300, 'taxes': 57.0}, {'product': 'pantalones 2', 'price': 200, 'taxes': 38.0}]
print("Linea 26: ",items)
#IMPRIME: Linea 26:  [{'product': 'camisa', 'price': 100, 'taxes': 19.0}, {'product': 'pantalones', 'price': 300, 'taxes': 57.0}, {'product': 'pantalones 2', 'price': 200, 'taxes': 38.0}]

items =[
    {'product': 'shirt',
    'price':120},
    {'product': 'pants',
    'price':160},
    {'product': 'jacket',
    'price':205}
]

new_items = list(map( lambda x: x|{'tax': x['price']*0.19} ,items)) 

print(new_items)   
print(items)

#cree un nuevo array con el atributo copy() y listo, he visto que todos hicieron varias lineas extra de codigo, espero les funcione.
# items_cp = items.copy()
# print(items_cp)

