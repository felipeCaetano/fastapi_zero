from http import HTTPStatus
from http.client import HTTPException

from fastapi import FastAPI

from fastapi_zero.schemas import Message, UserDB, UserSchema

app = FastAPI()
database = []


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserDB)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserDB)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserDB
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )
    return database.pop(user_id - 1)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.get('/helloworld', status_code=HTTPStatus.OK)
def hello_world():
    return """
    <html>
    <head><title>Bem Vindo</title></head><body><h1>Olá, Mundo!</h1></body>
    </html>"""
