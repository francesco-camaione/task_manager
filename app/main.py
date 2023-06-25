import os
import uvicorn
import sys

from ksuid import ksuid as k_id
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from starlette import status

sys.path.append("/Users/france.cama/code/task_manager")
from middleware.dbMiddleware import DbMiddleware
from utils import utils

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "src/dist/"))
src = app.mount("/assets", StaticFiles(directory=os.path.join(BASE_DIR, "src/dist/assets")), name="src")
dbm = DbMiddleware()


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create_user", response_class=JSONResponse)
def create_user():
    ks = k_id()
    print("**ks: ", ks)
    response = dbm.create_user(ks, email="random", pswrd="random", created_at=utils.getSqlDatetime())
    return {"response": response}

@app.delete("/delete_user", response_class=JSONResponse)
def delete_user(ksuid: int):
    if dbm.is_auth(ksuid):
        dbm.delete_user(ksuid)
        return "User deleted"
    else:
        return RedirectResponse("/", status_code=status.HTTP_401_UNAUTHORIZED)

@app.post("/create_task", response_class=HTMLResponse)
def create_task(ksuid, id: int, description: str, priority: int):
    if dbm.is_auth(ksuid):
        return dbm.create_task(id, description, priority)
    else:
        return RedirectResponse("/", status_code=status.HTTP_401_UNAUTHORIZED)
    

@app.delete("/delete_task", response_class=JSONResponse)
def delete_task(ksuid, id: int):
    if dbm.is_auth(ksuid):
        dbm.delete_task(id)
        return "Task deleted"
    else:
        return RedirectResponse("/", status_code=status.HTTP_401_UNAUTHORIZED)

# if the file is runned directly, run uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
