from pydantic import BaseModel

class IngresoCreate(BaseModel):
    sucursal_id: int
    detalles: str
    monto: float
    fecha: str  # Asegúrate de procesar la fecha adecuadamente en tu lógica

class IngresoUpdate(BaseModel):
    sucursal_id: int = None
    detalles: str = None
    monto: float = None
    fecha: str = None  # Asegúrate de procesar la fecha adecuadamente en tu lógica

    class Config:
        arbitrary_types_allowed = True
