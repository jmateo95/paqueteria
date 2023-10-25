from pydantic import BaseModel

class TipoGastoCreate(BaseModel):
    nombre: str

class TipoGastoUpdate(BaseModel):
    nombre: str = None

    class Config:
        arbitrary_types_allowed = True