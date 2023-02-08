# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
 
n = int(input('Введите число: '))
j = 1

list_fib = []
list_unfib = []

for i in range(0, n + 1):
    if i == 0 or i == 1:
        list_fib.append(i)
    else:
        list_fib.append(list_fib[i - 2] + list_fib[i - 1])   
print(list_fib)

for i in range(-len(list_fib), 0):
    if i == -len(list_fib) or i == -len(list_fib) + 1:
        list_unfib.append(list_fib[i])
    else:
        j += 1
        list_unfib.append(list_unfib[j - 2] - list_unfib[j - 1]) 

list_unfib.pop(0)
print(list_unfib) 
list_unfib.reverse()
list_out = list_unfib + list_fib
print(list_out)


    