def delete_data(my_list, setup):
    print(f"Режим {setup}: поиск и удаление записи")
    text_in = input('Введите текст для поиска и удаления: ')
    out_list = []
    flag = False
    for i in range(len(my_list)):
        if text_in not in my_list[i]:
            out_list.append(my_list[i])
            flag = True
    if flag == False:
        print(f"Текст {text_in} в справочнике не обнаружен!")
    out_list[len(out_list) - 1].strip()
    return out_list
        