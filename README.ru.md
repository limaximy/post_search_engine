# Название

post_search_engine

***


# Описание

Позволяет находить людей выбранного пользователем возраста через лайки на постах в VK.

***


# Установка

```
git clone https://github.com/limaximy/post_search_engine.git
cd post_search_engine

python -m venv venv # создание виртуального окружения
source venv/bin/activate   # запуск venv на Linux / macOS
venv\Scripts\activate   # запуск venv на Windows
pip install -r requirements.txt # установка требуемых зависимостей
```

***


# Использование

## Создание токена

Получение токена описано в документации к VK API

Шифрование токена для работы в программе:
```
python encrypt.py
your_token
password
file_name
```

## Запуск приложения

```
uvicorn main:app --reload
```

Документация API будет доступна по адресу:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

***
