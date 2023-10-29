from pydantic import BaseModel

class PaqueteCotizar(BaseModel):
    sucursal_origen_id: int
    sucursal_destino_id: int
    peso: float

class PaqueteCreate(BaseModel):
    sucursal_origen_id: int
    sucursal_destino_id: int
    descripcion: str
    peso: float
    volumen: float
    remitente: str
    destinatario: str
    campo: str #Puede ser distancia o costo_lb


class Paquete(BaseModel):
    estado_paquete_id: int
    no_guia: str
    descripcion: str
    peso: float
    volumen: float
    remitente: str
    destinatario: str
    costo: float

class PaqueteUpdate(BaseModel):
    estado_paquete_id: int = None
    no_guia: str = None
    descripcion: str = None
    peso: float = None
    volumen: float = None
    remitente: str = None
    destinatario: str = None
    costo: float = None

    class Config:
        arbitrary_types_allowed = True
