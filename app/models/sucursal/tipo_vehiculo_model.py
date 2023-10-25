from pydantic import BaseModel

class TipoVehiculoCreate(BaseModel):
    nombre: str

class TipoVehiculoUpdate(BaseModel):
    nombre: str = None

    class Config:
        arbitrary_types_allowed = True
