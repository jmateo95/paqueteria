from pydantic import BaseModel

class RolCreate(BaseModel):
    nombre: str
    descripcion: str

class RolUpdate(BaseModel):
    nombre: str = None
    descripcion: str = None

    class Config:
        arbitrary_types_allowed = True
