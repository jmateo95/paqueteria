from pydantic import BaseModel
from datetime import datetime

class SalidaCreate(BaseModel):
    tipo_salida_id: int
    vehiculo_id: int
    segmento_id: int
    fecha_salida: datetime
    fecha_llegada: datetime
    comentario: str
    fecha_programada: datetime

class SalidaUpdate(BaseModel):
    tipo_salida_id: int = None
    vehiculo_id: int = None
    segmento_id: int = None
    fecha_salida: datetime = None
    fecha_llegada: datetime = None
    comentario: str = None
    fecha_programada: datetime = None

    class Config:
        arbitrary_types_allowed = True
