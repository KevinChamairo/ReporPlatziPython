x = 3.3
print("Linea 2 --->", x)

y = 1.1 + 2.2
print("Linea 5 --->", y)
print("Linea 6 --->", x == y)

y_str = format(y, ".2g")
print("Linea 9 --->", 'str =>', y_str)
print("Linea 10 --->", y_str == str(x))

print("Linea 12 --->", '*' * 10)

print("Linea 14 --->", y,x)

tolerance = 0.00001
print("Linea 17 --->", abs(x-y) < tolerance)