# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

in_list = [2, 3, 4, 5, 6]
out_list = []
mult = 0
    
len_list = len(in_list) if len(in_list) % 2 == 0 else len(in_list) + 1
    
for i in range(len_list // 2):
    mult = in_list[i] * in_list[len(in_list) - 1 - i]
    out_list.append(mult)
print(out_list)
