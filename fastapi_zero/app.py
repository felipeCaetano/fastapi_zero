from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.get('/helloworld', status_code=HTTPStatus.OK)
def hello_world():
    return """
    <html>
    <head><title>Bem Vindo</title></head><body><h1>Olá, Mundo!</h1></body>
    </html>"""
