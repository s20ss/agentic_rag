from .models import Application
from .db_init import engine
from sqlmodel import  Session,select
from fastapi import HTTPException
class AppService():
    @staticmethod
    def create_app(name:str,description:str):
        application = Application(name=name,description=description)
        with Session(engine) as session:
            session.add(application)
            session.commit()
            session.refresh(application)
        return application
    
    @staticmethod
    def get_apps(offset:int,limit:int):
        with Session(engine) as session:
            apps = session.exec(select(Application).offset(offset).limit(limit)).all()
        return apps
    
    @staticmethod
    def get_app_by_id(id:int):
        with Session(engine) as session:
            app = session.get(Application,id)
        return app
    
    @staticmethod
    def delete_app(id:int):
        with Session(engine) as session:
            app = session.get(Application,id)
            if not app:
                raise HTTPException(status_code=404,detail="App Not Found")
            session.delete(app)
            session.commit()
        return app



