# Backend Django

Python Version: 3.10.12

Django Version: 5.1.3

Django Rest Framework: 3.15.2

# Execução

1. Na raiz do projeto, criar um virtual environment usando venv:

   `python3 -m venv venv`

1. Ativar o virtual environment:

   `source venv/bin/activate`

1. Instalar as dependências:

   `pip install -r requirements.txt`

1. Executar o projeto em modo de desenvolvimento:

   `python3 manage.py runserver`

1. Acessar a porta do servidor:

   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Produção

Para executar em modo de produção:

`gunicorn server.wsgi`
