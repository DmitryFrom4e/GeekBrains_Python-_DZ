def add_user(my_list, setup):
    print(f"Режим {setup}: добавление новой записи")
    my_list.append(input("Добавьте пользователя: ") + '\n')
    
def write_data(my_list):
    with open('DZ\8\data.txt', 'w', encoding='utf-8') as file:
        my_list[len(my_list) - 1].strip()
        file.writelines(my_list)
        
def edit_data(my_list, setup):
    text_in = input('Введите текст для поиска и замены: ')
    flag = False
    for i in range(len(my_list)):
        if text_in in my_list[i]:
            print(f"Режим {setup}: поиск и замена записи")
            text_out = input('Введите новый текст: ')
            my_list[i] = my_list[i].replace(text_in, text_out)
    if flag == False:
        print(f"Текст {text_in} в справочнике не обнаружен!")
    return my_list
        
        