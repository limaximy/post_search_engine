def data_year(data_stroka:str, current_year:int, min_age:int)->int:
    count_dot = 0
    year = ''
    for i in range(len(data_stroka)):
        if data_stroka[i] =='.':
            count_dot = count_dot + 1
    if count_dot == 2:
        for i in range(len(data_stroka)):
            if count_dot == 0:
                year = year + data_stroka[i]
            if data_stroka[i] == '.':
                count_dot = count_dot - 1
    if year == '':
        return current_year - (min_age + 1)
    return int(year)


def take_age(data_stroka:str, current_year:int, min_age:int)->int:
    if data_stroka == '' or data_stroka == None:
        return min_age + 1
    return current_year - data_year(data_stroka, current_year, min_age)


def enter_source_and_take_owner_and_item_ids(source_post:str):
    owner_id:str = ""
    item_id:str = ""
    flag = False
    while not flag:
        i = 0
        while source_post[i:i+4] != 'wall':
            i = i + 1
        i = i + 4

        j = i
        while source_post[j] != '_':
            j = j + 1

        owner_id = source_post[i:j]
        item_id = source_post[j+1:len(source_post)]
        print(f"owner_id={owner_id}, item_id={item_id}")
        if owner_id[1:].isdigit() and item_id.isdigit():
            if (owner_id[0] == '-') or owner_id[0].isdigit():
                flag = True
        else:
            print("Неверно введена ссылка")

    print(f"owner_id = {owner_id}")
    print(f"item_id = {item_id}")

    return owner_id, item_id # возвращает кортеж, а не список