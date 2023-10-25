from pydantic import BaseModel

class EstadoPaqueteCreate(BaseModel):
    nombre: str
    descripcion: str

class EstadoPaqueteUpdate(BaseModel):
    nombre: str = None
    descripcion: str = None

    class Config:
        arbitrary_types_allowed = True
