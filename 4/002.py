# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
    
N = int(input('введите число num: '))
my_list = []
simple = 2
while N > 1:
    if N % simple == 0:
        if my_list.count(simple) == 0:
            my_list.append(simple)
        N = N/simple
    else:
        simple += 1
print(my_list)

