from pydantic import BaseModel
from datetime import datetime

class TrackingCreate(BaseModel):
    paquete_id: int
    sucursal_id: int
    estado_tracking_id: int
    salida_id: int
    fecha: datetime
    comentario: str

class TrackingUpdate(BaseModel):
    paquete_id: int = None
    sucursal_id: int = None
    estado_tracking_id: int = None
    salida_id: int = None
    fecha: datetime = None
    comentario: str = None

    class Config:
        arbitrary_types_allowed = True
