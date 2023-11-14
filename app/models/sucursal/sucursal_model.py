from pydantic import BaseModel
from typing import Optional

class SucursalCreate(BaseModel):
    nombre: str
    direccion: str
    latitud: float
    longitud: float
    ciudad_id: int
    tipo_sucursal_id: int
    test: Optional[bool]= None

class SucursalUpdate(BaseModel):
    nombre: str = None
    direccion: str = None
    latitud: float = None
    longitud: float = None
    ciudad_id: int = None
    tipo_sucursal_id: int = None

    class Config:
        arbitrary_types_allowed = True