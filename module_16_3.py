from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1':'Имя: Example, возраст: 18'}


@app.get('/users')
async def all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='Kevin'),
                    age: int = Path(ge=18, le=120, description='Enter age', example=48)) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int = Path(ge=1, le=100, description='Enter User ID for update', example=48),
                      username: str = Path(min_length=5, max_length=20, description='Enter new username', example='Kevin'),
                    age: int = Path(ge=18, le=120, description='Enter new age', example=48)) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100, description='Enter User ID for delete', example=48)) -> str:
    str_id = str(user_id)
    users.pop(str_id)
    return f'User {user_id} has been deleted'