from pydantic import BaseModel

class CiudadCreate(BaseModel):
    nombre: str
    descripcion: str
    latitud: float
    longitud: float

class CiudadUpdate(BaseModel):
    nombre: str
    descripcion: str
    latitud: float
    longitud: float