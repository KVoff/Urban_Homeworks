from fastapi import FastAPI, Path
from typing import Annotated
'''
Запуск файла должен быть выполнен с указание имени файла
в данном случае python3 -m uvicorn lesson_1:app
'''

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {'message': 'Hello world'}


# вызов: http://127.0.0.1:8000/id?username=user&age=22
@app.get('/id')
# может работать со значениями по умолчанию
# async def id_paginator(username: str = 'Vasya', age: int = 12) -> dict:
async def id_paginator(username: str, age: int) -> dict:
    return {'User': username, 'age': age}


# вызов: http://127.0.0.1:8000/user/A/B
@app.get('/user/A/B')
async def tester() -> dict:
    return {'message': 'Hello, Tester'}


# вызов: http://127.0.0.1:8000/user/Vasya/Pupkin
@app.get('/user/{first_name}/{last_name}')
async def news(first_name: str, last_name: str) -> dict:
    return {'message': f'Hello, {first_name} {last_name}'}


# валидация данных
@app.get('/valid/{username}/{id}')
async def info_validate(
    username: Annotated[str, Path(
        min_length=3,
        max_length=15,
        description='Enter you username',
        example='clock')],
    id: int = Path(
        ge=0,
        le=100,
        description='Enter your id',
        example='99')
        ) -> dict:

    return {'message': f'Hello, {username}:{id}'}
