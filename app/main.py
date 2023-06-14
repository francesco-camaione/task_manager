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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "src/"))
db = DbMiddleware()


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/create_user", response_class=PlainTextResponse)
def create_user(ksuid: int, email: str, pwdr: str, created_at=datetime.now()):
    db.create_user(ksuid, email, pwdr, created_at)
    return "user created"


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
