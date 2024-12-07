from fastapi import FastAPI
from app.routers import user, task

app = FastAPI()


@app.get('/')
def main_page():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)