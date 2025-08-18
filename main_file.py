import check_input
from  vk_find import all_together


# Интерфейс программы
def select_logic():
    while True:
        print("Меню")
        print("1. Поиск человека")
        print("2. Вывод пользователей с неопределенным конечным соответствием")
        print("0. Выход")

        select = check_input.check_for_digit("Введите выбранный номер")
        if (select == 1):
            all_together()
            pass
        elif (select == 2):
            pass
        elif (select == 0):
            exit()
        else:
            print("Введенный вариант отсутствует")


if __name__ == '__main__':
    select_logic()
