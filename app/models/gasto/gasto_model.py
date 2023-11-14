from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GastoCreate(BaseModel):
    sucursal_id: int
    tipo_gasto_id: int
    concepto_gasto_id: int
    detalles: str
    monto: float
    fecha: datetime
    test:  Optional[bool]= None

class GastoUpdate(BaseModel):
    sucursal_id: int = None
    tipo_gasto_id: int = None
    concepto_gasto_id: int = None
    detalles: str = None
    monto: float = None
    fecha: datetime = None

    class Config:
        arbitrary_types_allowed = True
