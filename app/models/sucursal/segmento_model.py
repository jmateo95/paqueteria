from pydantic import BaseModel

class SegmentoCreate(BaseModel):
    sucursal_origen_id: int
    sucursal_destino_id: int
    descripcion: str
    distancia: float

class SegmentoUpdate(BaseModel):
    sucursal_origen_id: int = None
    sucursal_destino_id: int = None
    descripcion: str = None
    distancia: float = None

    class Config:
        arbitrary_types_allowed = True
