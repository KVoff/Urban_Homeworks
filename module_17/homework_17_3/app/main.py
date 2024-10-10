from fastapi import FastAPI
from models import task
from models import user


app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Task manager"}


app.include_router(task.router)
app.include_router(user.router)
