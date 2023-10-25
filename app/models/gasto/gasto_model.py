from pydantic import BaseModel

class GastoCreate(BaseModel):
    sucursal_id: int
    tipo_gasto_id: int
    concepto_gasto_id: int
    detalles: str
    monto: float
    fecha: str  # Asegúrate de procesar la fecha adecuadamente en tu lógica

class GastoUpdate(BaseModel):
    sucursal_id: int = None
    tipo_gasto_id: int = None
    concepto_gasto_id: int = None
    detalles: str = None
    monto: float = None
    fecha: str = None  # Asegúrate de procesar la fecha adecuadamente en tu lógica

    class Config:
        arbitrary_types_allowed = True
