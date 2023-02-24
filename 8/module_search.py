def search_data(my_list, setup):
    print(f"Режим {setup}: поиск по справочнику:")
    text = input('Введите текст для поиска: ')
    for elem in my_list:
        if text in elem:
            print(elem.strip())