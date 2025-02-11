from typing import Annotated
from fastapi import APIRouter, File, UploadFile
from config import settings
import os
from core.app_service import AppService
from core.indexing_service import IndexingService
from core.retrieval_service import RetrievalService

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
    return apps


@app_router.get("/get_application_by_id/")
async def get_applications(app_id:int):
    app = AppService.get_app_by_id(id=app_id)
    print(app)
    return app


@app_router.delete("/get_application_by_id/")
async def get_applications(app_id:int):
    app = AppService.delete_app(id=app_id)
    print(app)
    return app

@app_router.get("/index_application/")
async def index_application(app_id:int):
    IndexingService.index_app(app_id=app_id)
    return None

@app_router.post("/search_application/")
async def search_application(app_id:int,query:str,top_k:int):
    results = RetrievalService.search_app(app_id=app_id,query=query,top_k=top_k)
    return results
