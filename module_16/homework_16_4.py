from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List, Optional
'''
Запуск файла должен быть выполнен с указание имени файла
в данном случае: python3 -m uvicorn homework_16_4:app
'''

app = FastAPI()


class Users(BaseModel):
    id: Optional[int] = None
    username: str
    age: Optional[int] = None


users: List[Users] = []


@app.get('/')
def home_page() -> str:
    return 'Hello, check /docs'


@app.get('/users')
def get_users() -> List[Users]:
    return users


@app.post('/users')
def create_users(user: Users = Body()) -> Users:
    user.id = len(users) + 1  # id нового пользователя
    users.append(user)
    return user


@app.put("/users")
def update_user(
    user_id: int,
    username: str = Body(),
    age: int = Body()
) -> Users:
    try:
        user = users[user_id - 1]  # Индекс на 1 меньше
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> Users:
    try:
        user = users.pop(user_id - 1)  # Индекс на 1 меньше
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users")
def kill_all_users() -> str:
    users.clear()
    return "All users deleted!"
