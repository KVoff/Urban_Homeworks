from fastapi import FastAPI, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional
'''
Запуск файла должен быть выполнен с указание имени файла
в данном случае: python3 -m uvicorn main:app
'''

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class Users(BaseModel):
    id: Optional[int] = None
    username: str
    age: Optional[int] = None


users_db: List[Users] = []


@app.get('/')
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        'users.html',
        {'request': request, 'users': users_db}
        )


@app.get('/users/{user_id}')
def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse(
            'users.html',
            {'request': request, 'user': users_db[user_id - 1]}
            )
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post('/users')
def create_users(user: Users = Body()) -> Users:
    user.id = len(users_db) + 1  # id нового пользователя начинается с 1
    users_db.append(user)
    return user


@app.put("/users")
def update_user(
    user_id: int,
    username: str = Body(),
    age: int = Body()
) -> Users:
    try:
        user = users_db[user_id - 1]  # Индекс на 1 меньше
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> Users:
    try:
        user = users_db.pop(user_id - 1)  # Индекс на 1 меньше
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")
