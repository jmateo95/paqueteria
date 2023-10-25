from pydantic import BaseModel

class EstadoTrackingCreate(BaseModel):
    nombre: str
    descripcion: str

class EstadoTrackingUpdate(BaseModel):
    nombre: str = None
    descripcion: str = None

    class Config:
        arbitrary_types_allowed = True
