from fastapi import FastAPI
'''
Запуск файла должен быть выполнен с указание имени файла
в данном случае: python3 -m uvicorn homework_16_1:app
'''

app = FastAPI()


@app.get("/")
async def get_main_page() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def get_admin_page() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def get_user_number(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def get_user_info(username: str = 'none', age: int = 0) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
