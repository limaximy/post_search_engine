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

python -m venv venv # creating a virtual environment
source venv/bin/activate   # enable venv for Linux / macOS
venv\Scripts\activate   # enable venv for Windows
pip install -r requirements.txt # installation of necessary packages
```

***


# Usage

## Creating a token

Getting a token is described in the VK API documentation (i created the app here https://id.vk.com/about/business/go/ and used the Service Access Key)

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
