# main.py
from typing import Annotated
from fastapi import FastAPI,Query
from core.db_init import create_db_and_tables,SessionDep
from core.models import DatasetFile,Application,AppTool
from sqlmodel import select
from config import settings
from routes.file_router import file_router
from routes.app_router import app_router

app = FastAPI()


app.include_router(file_router)
app.include_router(app_router)

@app.on_event("startup")
def on_startup():
    print("Settings",settings.local_directory)
    create_db_and_tables()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

