from .models import DatasetFile
from .db_init import engine
from sqlmodel import  Session
class FileService():
    @staticmethod
    def save_dataset_file(app_id:int,name:str,file_location:str):
        dataset_file = DatasetFile(app_id=app_id,name=name,file_location=file_location)
        with Session(engine) as session:
            session.add(dataset_file)
            session.commit()
            session.refresh(dataset_file)
        return dataset_file
        
    