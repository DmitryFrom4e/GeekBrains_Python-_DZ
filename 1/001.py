# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_num = int(input('Введите номер дня недели: '))

if day_num >= 1 and day_num <= 5:
    print('нет')
elif day_num >= 6 and day_num <= 7:
    print('да')
else:
    print('Неверный номер дня недели')