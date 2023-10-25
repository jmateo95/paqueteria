from pydantic import BaseModel
from datetime import datetime

class TarifarioCreate(BaseModel):
    fecha: datetime
    ganancia_lb: float
    costo_lb_km: float
    sucursal_id: int

class TarifarioUpdate(BaseModel):
    fecha: datetime = None
    ganancia_lb: float = None
    costo_lb_km: float = None
    sucursal_id: int = None

    class Config:
        arbitrary_types_allowed = True