from decrypt import decrypt_file

TOKEN_FILE = "vk_token.myaw"
VK_API_VERSION = 5.131
CURRENT_YEAR = 2025

class SearchConfig:
    def __init__(self):
        self.token:bytes = bytes()
        self.version:float = -1
        self.sex:int = -1
        self.min_age:int = -1
        self.max_age:int = -1
        self.current_year:int = -1
        self.count:int = -1
        self.can_write_private_message:int = -1


    def set_token(self, token_file_name:str, password:str)->None:
        self.token = decrypt_file(token_file_name, password, False)


    def set_version(self, version:float)->None:
        self.version = version


    def set_sex(self, sex:int)->None:
        if sex != 0 and sex != 1:
            raise ValueError("Пол может быть только 0 или 1")
        self.sex = sex


    def set_min_age(self, min_age:int)->None:
        if min_age < 0:
            raise ValueError("Минимальный возраст не может быть отрицательным")
        self.min_age = min_age


    def set_max_age(self, max_age:int)->None:
        if max_age < 0:
            raise ValueError("Максимальный возраст не может быть отрицательным")
        self.max_age = max_age


    def set_current_year(self, current_year:int)->None:
        if current_year < 0:
            raise ValueError("Текущий год не может быть отрицательным")
        self.current_year = current_year


    def set_count(self, count:int)->None:
        if count > 1000 or count < 0:
            raise ValueError("Количество обрабатываемых запросов X должно быть в пределах 0 <= X <= 1000")
        self.count = count


    def set_can_write_private_message(self, can_write_private_message:int)->None:
        if can_write_private_message != 0 and can_write_private_message != 1:
            raise ValueError("Возможность писать приватные сообщения может быть либо 0, либо 1")
        self.can_write_private_message = can_write_private_message


    def set_default_settings(self, password)->None:
        self.set_token(TOKEN_FILE, password)
        self.set_version(VK_API_VERSION)
        self.set_sex(1)
        self.set_min_age(16)
        self.set_max_age(22)
        self.set_current_year(CURRENT_YEAR)
        self.set_count(1000)
        self.set_can_write_private_message(1)