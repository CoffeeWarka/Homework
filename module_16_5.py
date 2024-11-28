from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/')
async def req(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse('users.html',{'request':request, 'users': users})


@app.get('/user/{user_id}')
async def user_req(request: Request, user_id: int) -> templates.TemplateResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id]})


@app.get('/users')
async def all_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(user: User, username: str, age: int) -> User:
    if len(users) == 0:
        user.id = 1
    else:
        user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        del_user = users.pop(user_id - 1)
        return del_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")