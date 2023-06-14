import os
import uvicorn
import sys
from datetime import datetime

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse, PlainTextResponse
from starlette.templating import Jinja2Templates

sys.path.append("/Users/france.cama/code/task_manager")
from middleware.dbMiddleware import DbMiddleware
from utils import utils

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "src/"))
dbm = DbMiddleware()


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create_user", response_class=PlainTextResponse)
def create_user(ksuid: int, email: str, pswrd: str):
    sql_datetime = utils.getSqlDatetime()
    return dbm.create_user(ksuid, email, pswrd, sql_datetime)

@app.delete("/delete_user", response_class=PlainTextResponse)
def delete_user(ksuid: int):
    dbm.delete_user(ksuid)
    return "User deleted"

@app.post("/create_task", response_class=PlainTextResponse)
def create_task(id: int, description: str, priority: int):
    return dbm.create_task(id, description, priority)
    

@app.delete("/delete_task", response_class=PlainTextResponse)
def delete_task(id: int):
    dbm.delete_task(id)
    return "Task deleted"

# if the file is runned directly, run uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
