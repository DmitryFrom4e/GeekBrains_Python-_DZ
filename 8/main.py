# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import os
from module_read import read_data, print_data 
from module_write import add_user, write_data, edit_data
from module_search import search_data
from module_delete import delete_data

os.system('clear')

def menu(my_list):
    print('''\t------------Телефонный справочник-----------
      
      \tКоманды управления:
      \t\t>Просмотр всего списка: \t>1< 
      \t\t>Поиск по справочнику: \t\t>2<
      \t\t>Добавление новой записи: \t>3<
      \t\t>Поиск и замена записи: \t>4<
      \t\t>Поиск и удаление записи: \t>5<
      ''')
    setup = int(input('Введите команду для работы со справочником: '))
    if setup == 1:
        print_data(my_list, setup)
    elif setup == 2:
        search_data(my_list, setup)
    elif setup == 3:
        add_user(my_list, setup)
        write_data(my_list)
    elif setup == 4:
        my_list = edit_data(my_list, setup)
        write_data(my_list)
    elif setup ==5:
        my_list = delete_data(my_list, setup)
        write_data(my_list)
    menu(my_list)

def main():
    my_list = read_data()
    return my_list

my_list = []

if __name__ == '__main__':
    my_list = main()
    menu(my_list)
