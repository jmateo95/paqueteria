from pydantic import BaseModel

class VehiculoCreate(BaseModel):
    placa: str
    capacidad_lb: float
    costokm: float
    tipovehiculo_id: int
    sucursal_id: int

class VehiculoUpdate(BaseModel):
    placa: str = None
    capacidad_lb: float = None
    costokm: float = None
    tipovehiculo_id: int = None
    sucursal_id: int = None

    class Config:
        arbitrary_types_allowed = True
