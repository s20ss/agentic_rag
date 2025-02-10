from typing import Annotated
from fastapi import APIRouter, File, UploadFile
from config import settings
import os
from core.app_service import AppService

app_router = APIRouter()

@app_router.post("/create_application/")
async def create_upload_files(
    name:str,
    description:str
):
    app = AppService.create_app(name=name,description=description)
    return app

@app_router.get("/get_application/")
async def get_applications(offset:int,limit:int):
    apps = AppService.get_apps(offset=offset,limit=limit)
    print()
    return apps