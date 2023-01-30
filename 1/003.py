# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num_square = int(input('Введите номер четверти: '))

if num_square == 1:
    print("x > 0; y > 0")
elif num_square == 2:
    print("x < 0; y > 0")
elif num_square == 3:
    print("x < 0; y < 0")
elif num_square == 4:
    print("x > 0; y < 0")
else:
    print("Неверный номер четверти")