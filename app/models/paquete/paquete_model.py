from pydantic import BaseModel

class PaqueteCreate(BaseModel):
    segmento_id: int
    estado_paquete_id: int
    no_guia: str
    descripcion: str
    peso: float
    volumen: float
    remitente: str
    destinatario: str
    costo: float

class PaqueteUpdate(BaseModel):
    segmento_id: int = None
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
