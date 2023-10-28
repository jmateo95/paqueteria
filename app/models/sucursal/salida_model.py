from pydantic import BaseModel
from datetime import datetime

class SalidaCreate(BaseModel):
    tipo_salida_id: int
    vehiculo_id: int
    segmento_id: int
    fecha_salida: datetime
    fecha_llegada: datetime
    fecha_programada: datetime
    comentario: str
    costo_lb: float
    capacidad_lb: float
    capacidad_reservada: float
    capacidad_ocupada: float

class SalidaUpdate(BaseModel):
    tipo_salida_id: int = None
    vehiculo_id: int = None
    segmento_id: int = None
    fecha_salida: datetime = None
    fecha_llegada: datetime = None
    fecha_programada: datetime = None
    comentario: str = None
    costo_lb: float = None
    capacidad_lb: float = None
    capacidad_reservada: float = None
    capacidad_ocupada: float = None

    class Config:
        arbitrary_types_allowed = True
