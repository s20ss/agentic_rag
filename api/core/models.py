from sqlmodel import Field, SQLModel

class Application(SQLModel, table=True):
    id: int  = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str = Field(default=None)
    

class DatasetFile(SQLModel,table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    summary: str = Field(default="")
    file_location: str = Field(default=None)
    app_id : int = Field(default=None, foreign_key="application.id")

class AppTool(SQLModel,table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    app_id: int = Field(default=None, foreign_key="application.id")
    
    

