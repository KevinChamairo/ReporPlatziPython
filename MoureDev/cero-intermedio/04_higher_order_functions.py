# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=10172

### Higher Order Functions ###

from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print("Linea 20 ->",sum_two_values_and_add_value(5, 2, sum_one)) #8
print("Linea 21 ->",sum_two_values_and_add_value(5, 2, sum_five)) #12

### Closures ###


def sum_ten():
    def add(value):
        return value + 10
    return add


# add_closure = sum_ten(1)
add_closure = sum_ten()
# print("Linea 33 ->",add_closure(5)) #16
print("Linea 34 ->",add_closure(5)) #15
# print("Linea 35 ->",(sum_ten(5))(1)) #16


def sum_ten2(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure2 = sum_ten2(1)
print("Linea 46 ->",add_closure2(5)) #16
print("Linea 47 ->",(sum_ten2(5))(1)) #16

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map


def multiply_two(number):
    return number * 2


print("Linea 60 ->",list(map(multiply_two, numbers)))
print("Linea 61 ->",list(map(lambda number: number * 2, numbers)))

# Filter


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print("Linea 72 ->",list(filter(filter_greater_than_ten, numbers)))
print("Linea 73 ->",list(filter(lambda number: number > 10, numbers)))

# Reduce


def sum_two_values(first_value, second_value):
    return first_value + second_value


print("Linea 82 ->",reduce(sum_two_values, numbers)) #[2, 5, 10, 21, 3, 30]
