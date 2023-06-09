# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=3239

### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print("linea 6 ->", my_original_list) #[0, 1, 2, 3, 4, 5, 6, 7]

my_range = range(8)
print("linea 9 ->",list(my_range)) #[0, 1, 2, 3, 4, 5, 6, 7]

# Definición

my_list = [i + 1 for i in range(8)]
print("linea 14 ->",my_list) #[1, 2, 3, 4, 5, 6, 7, 8]

my_list = [i * 2 for i in range(8)]
print("linea 17 ->",my_list) #[0, 2, 4, 6, 8, 10, 12, 14]

my_list = [i * i for i in range(8)]
print("linea 20 ->",my_list) #[0, 1, 4, 9, 16, 25, 36, 49]


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(8)]
print("linea 28 ->",my_list) #[5, 6, 7, 8, 9, 10, 11, 12]