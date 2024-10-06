from fastapi import FastAPI, Path
from typing import Annotated
'''
Запуск файла должен быть выполнен с указание имени файла
в данном случае: python3 -m uvicorn homework_16_3:app
'''

app = FastAPI()

users = {'1': 'Name: Example, age: 18'}


@app.get('/')
async def home_page() -> str:
    return 'Hello, check /docs'


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/users/{username}/{age}')
async def post_users(
    username: Annotated[str, Path(
        min_length=5,
        max_length=20,
        description='Enter username',
        example='UrbanUser')],
    age: Annotated[int, Path(
        ge=18,
        le=120,
        description='Enter age',
        example='22')]
        ) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Name: {username}, age: {age}'
    return f'User {user_id} is registered'


@app.put('/users/{user_id}/{username}/{age}')
async def update_users(
    user_id: Annotated[int, Path(
        ge=1,
        le=100,
        description='Enter id',
        example='77')],
    username: Annotated[str, Path(
        min_length=5,
        max_length=20,
        description='Enter username',
        example='UrbanUser')],
    age: Annotated[int, Path(
        ge=18,
        le=120,
        description='Enter age',
        example='22')]
        ) -> str:
    users[str(user_id)] = f'Name: {username}, age: {age}'
    return f'User {user_id} has been updated'


@app.delete('/users/{user_id}')
async def delete_user(
    user_id: Annotated[int, Path(
        ge=1,
        le=100,
        description='Enter id',
        example='77')]
        ) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'


@app.delete('/')
async def delete_all_users() -> str:
    users.clear()
    return 'All users was deleted.'
