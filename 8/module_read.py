def read_data():
    with open('DZ\8\data.txt', 'r', encoding='utf-8') as file:
        my_list = file.readlines()
        return my_list 
    
def print_data(my_list, setup):
    print(f"Режим {setup}: просмотр всего списка:")
    for i in my_list:
        print(i.strip())