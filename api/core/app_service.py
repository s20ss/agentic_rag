from .models import Application
from .db_init import engine
from sqlmodel import  Session,select
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
    def get_apps(offset,limit):
        with Session(engine) as session:
            apps = session.exec(select(Application).offset(offset).limit(limit)).all()
        return apps


