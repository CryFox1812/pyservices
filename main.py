from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app import Server


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
server = Server()
app.include_router(server.router)
