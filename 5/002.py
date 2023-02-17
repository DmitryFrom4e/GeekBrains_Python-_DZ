# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# 1. Игрок1 поздоровался, назвал имя
# 2. Игрок2 поздоровался, назвал имя
#   - если имя Игрока2 - бот - играет ИИ
#   - если имя Игрока2 другое - играет человек

from random import randint
from goto import with_goto

def generate_lots():
    n = randint(1, 2)
    return (n % 2 == 0 and n) or n - 1

def init_game(current_step, k, money_box):
    while current_step < 3:         #игра в 2 хода
        user_take = print_act(str(players_list[k]))
        if k == 0:
            players_list[1].append(user_take)
            k += 2                 #меняем +1 индекс игрока, делающего следующий ход
        else: 
            players_list[3].append(user_take)
            k -= 2                  #меняем -1 индекс игрока, делающего следующий ход
        current_step += 1           #+1 ход

def print_act(user_name): #функция ""взятия"" конфет
    taken = 0
    # label .start
    if user_name.lower() != "бот":
        taken = input(f"{user_name}, возьмите конфеты (от 1 до 28): ")
        if int(taken) > 28:
            taken = 0
    else:
        taken = randint(1, 29)
        print(f"{user_name} взял {taken} конфет")
    # if int(taken) == 0 or not(taken.isdigit()):
    #     goto .start 
    return int(taken)    
    
def grab_all(k, in_list):               #распределяем выигрыш
    in_list[3 if k == 0 else 1].append(int(''.join(map(str,in_list[1 if k == 0 else 3]))))
    in_list[1 if k == 0 else 3] = []
    return in_list

def congrat_winner(k, in_list):
    text_congr = f"Победил {str(in_list[2 if k == 0 else 0])}, награда: {sum(in_list[3 if k == 0 else 1])})" 
    return text_congr

money_box = 250                         #общая копилка с конфетами
players_list = []                       #списки игроков
players_list.append(input("Введите имя Игрока1: "))
players_list.append([])                 #буфер для копилки игрока1
players_list.append(input("Введите имя Игрока2 (если имя 'бот' - игра с ИИ): "))
players_list.append([])                 #буфер для копилки игрока2
k = generate_lots()                     #рандомно номер индекса игрока, делающего первый ход
current_step = 1

init_game(current_step, k, money_box)   #начало игры
    
# перераспределяем копилки игроков между победителем-проигравшим
players_list = grab_all(k, players_list)
money_box -= sum(players_list[1]) + sum(players_list[3])
winner = congrat_winner(k, players_list)

print(winner)   #печатаем поздравление










    


