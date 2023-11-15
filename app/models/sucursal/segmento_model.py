from pydantic import BaseModel
from typing import Optional

class SegmentoCreate(BaseModel):
    sucursal_origen_id: int
    sucursal_destino_id: int
    descripcion: str
    distancia: float
    test:Optional[bool]= None


class SegmentoUpdate(BaseModel):
    sucursal_origen_id: int = None
    sucursal_destino_id: int = None
    descripcion: str = None
    distancia: float = None

    class Config:
        arbitrary_types_allowed = True
