from pydantic import BaseModel

class TipoSucursalCreate(BaseModel):
    nombre: str

class TipoSucursalUpdate(BaseModel):
    nombre: str = None

    class Config:
        arbitrary_types_allowed = True