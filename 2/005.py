# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
import random
all = int(input('всего монеток: '))

resh = random.randint(0, all - 1)   #загуглил, -1 - чтобы как минимум 1 можно перевернуть)
gerb = all - resh
if gerb < resh:
    print("Перверни", gerb, "с гербом")
else:
    print("Перверни", gerb, "с решкой")