from fastapi import FastAPI
import uvicorn
from core import CoreObject
import additional_functions


app = FastAPI() # инициализация объекта для работы fastapi
core = CoreObject() # инициализация объекта главного класса

# Интерфейс для запуска функции поиска
@app.get("/launch", summary = "Поиск id", tags = ["Ручка 1"] )
def launch(source:str, password:str, token_file:str = "vk_token.myaw", version:float = 5.131, sex:int = 1, min_age:int = 16, max_age:int = 22,
           current_year:int = 2025, count:int = 1000, can_write_private_message:int = 1):

    core.config.set_token(token_file, password)
    core.config.set_version(version)
    core.config.set_sex(sex)
    core.config.set_min_age(min_age)
    core.config.set_max_age(max_age)
    core.config.set_current_year(current_year)
    core.config.set_count(count)
    core.config.set_can_write_private_message(can_write_private_message)
    owner_id, item_id = additional_functions.enter_source_and_take_owner_and_item_ids(source)
    core.all_ids_scan_and_record(owner_id, item_id)


# Интерфейс для получения данных из базы данных
@app.get("/take_ids", summary = "Получение id", tags = ["Ручка 2"])
def take_id(limit:int = 1000, shift:int = 0):
    return core.launch_select_id_from_position(limit, shift)


    
if __name__ == "__main__":
    uvicorn.run("main:app", reload = True) # запуск локального сервера с fastapi документацией