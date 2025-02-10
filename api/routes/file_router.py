from typing import Annotated
from fastapi import APIRouter, File, UploadFile
from config import settings
import os
from core.file_service import FileService

file_router = APIRouter()

@file_router.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
    app_id:int
):
    save_directory = settings.local_directory
    for file in files:
        file_location = os.path.join(save_directory, file.filename)
        with open(file_location, "wb+") as f:
            f.write(file.file.read())
        FileService.save_dataset_file(app_id=app_id,name=file.filename,file_location=file_location)
    
    return {"filenames": [file.filename for file in files]}