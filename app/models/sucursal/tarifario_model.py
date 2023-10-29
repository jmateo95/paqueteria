from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TarifarioCreate(BaseModel):
    ganancia_envio: float
    fecha:          Optional[datetime]= None

class Tarifario(BaseModel):
    fecha:          datetime
    ganancia_envio: float
    costo_lb:       float

class TarifarioUpdate(BaseModel):
    fecha:          datetime = None
    ganancia_envio: float = None
    costo_lb:       float = None

    class Config:
        arbitrary_types_allowed = True