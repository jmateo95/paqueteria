from pydantic import BaseModel
from datetime import datetime

class IngresoCreate(BaseModel):
    sucursal_id: int
    detalles: str
    monto: float
    fecha: datetime  # Asegúrate de procesar la fecha adecuadamente en tu lógica

class IngresoUpdate(BaseModel):
    sucursal_id: int = None
    detalles: str = None
    monto: float = None
    fecha: datetime = None  # Asegúrate de procesar la fecha adecuadamente en tu lógica

    class Config:
        arbitrary_types_allowed = True
