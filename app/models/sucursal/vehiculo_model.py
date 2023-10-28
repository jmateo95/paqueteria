from pydantic import BaseModel

class VehiculoCreate(BaseModel):
    placa: str
    capacidad_lb: float
    costo_km: float
    tipo_vehiculo_id: int
    sucursal_id: int

class VehiculoUpdate(BaseModel):
    placa: str = None
    capacidad_lb: float = None
    costo_km: float = None
    tipo_vehiculo_id: int = None
    sucursal_id: int = None

    class Config:
        arbitrary_types_allowed = True
