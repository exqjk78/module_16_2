from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def main_page():
    return 'Главная страница'

@app.get('/user/admin')
async def admin():
    return 'вы вошли как администратор'

@app.get('/user/{user_id}')
async def usern(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='78')):
    return f'вы вошли как пользователь № {user_id}'

@app.get('/user/{username}/{age}')
async def info(username: str = Path(min_length=5, max_length=20, description='Enter username', example='exqjk78')
               , age: int = Path(ge=18, le=120, description='Enter age', example='37')):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'