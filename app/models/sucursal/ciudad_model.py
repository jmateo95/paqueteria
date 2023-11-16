from pydantic import BaseModel
from typing import Optional

class CiudadCreate(BaseModel):
    nombre: str
    descripcion: str
    departamento: str
    test:  Optional[bool]= None

class CiudadUpdate(BaseModel):
    nombre: str = None
    descripcion: str = None
    departamento: str = None

    class Config:
        # Permite que los campos sean opcionales
        arbitrary_types_allowed = True