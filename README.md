# Name

post_search_engine

***


# Description

It allows you to find people of the user's chosen age through likes on VK posts.

***


# Installation

```
git clone https://github.com/limaximy/post_search_engine.git
cd post_search_engine

python -m venv venv # создание виртуального окружения
source venv/bin/activate   # запуск venv на Linux / macOS
venv\Scripts\activate   # запуск venv на Windows
pip install -r requirements.txt # установка требуемых зависимостей
```

***


# Usage

## Creating a token

Getting a token is described in the VK API documentation

Encrypting the token to work in the program:
```
python encrypt.py
your_token
password
file_name
```

## Launching the app

```
uvicorn main:app --reload
```

The API documentation will be available at:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

***
