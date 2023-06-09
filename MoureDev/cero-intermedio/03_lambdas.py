# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=9145

### Lambdas ###

def sum_two_values(first_value, second_value): 
    return first_value + second_value


print("linea 9 ->",sum_two_values(2, 4)) #6


def multiply_values(first_value, second_value): 
    return first_value * second_value - 3


print("linea 16 ->",multiply_values(2, 4)) #5


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print("linea 23 ->",sum_three_values(5)(2, 4)) #11