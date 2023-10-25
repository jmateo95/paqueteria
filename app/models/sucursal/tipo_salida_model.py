from pydantic import BaseModel

class TipoSalidaCreate(BaseModel):
    nombre: str

class TipoSalidaUpdate(BaseModel):
    nombre: str = None

    class Config:
        arbitrary_types_allowed = True
