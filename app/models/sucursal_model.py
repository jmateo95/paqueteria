from pydantic import BaseModel

class SucursalCreate(BaseModel):
    nombre: str
    direccion: str
    latitud: float
    longitud: float
    ciudad_id: int
    tiposucursal_id: int

class SucursalUpdate(BaseModel):
    nombre: str = None
    direccion: str = None
    latitud: float = None
    longitud: float = None
    ciudad_id: int = None
    tiposucursal_id: int = None

    class Config:
        arbitrary_types_allowed = True