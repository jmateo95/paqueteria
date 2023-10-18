from pydantic import BaseModel

class CiudadCreate(BaseModel):
    nombre: str
    descripcion: str
    latitud: float
    longitud: float

class CiudadUpdate(BaseModel):
    nombre: str = None
    descripcion: str = None
    latitud: float = None
    longitud: float = None

    class Config:
        # Permite que los campos sean opcionales
        arbitrary_types_allowed = True