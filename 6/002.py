# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

my_list = [-5, 9, 7, 8, 12, 45, -56, 45, 36, 67, 90, 100, 34, 23, -9]
min_index = int(input('задайте минимальное значение: '))
max_index = int(input('задайте максимальное значение: '))
for i in range(len(my_list)):
    if min_index <= my_list[i] <= max_index:
        print(i, end=" ")