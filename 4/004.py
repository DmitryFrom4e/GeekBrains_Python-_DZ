# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

# тут я немного запутался... что такое нужно???
s = k = int(input('введите степень k: '))
string_x = ''
list_nums = []
for i in range(0, k):
    list_nums.append(random.randint(0, 101))

print(list_nums)

for i in list_nums:
    if i != 0:
        string_x += str(i) + " x ^ " + str(s)
        s -= 1
string_x += " = 0 "
print(string_x) 
    



