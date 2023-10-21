from pydantic import BaseModel

class PuestoCreate(BaseModel):
    nombre: str
    descripcion: str
    salario_horario: float

class PuestoUpdate(BaseModel):
    nombre: str = None
    descripcion: str = None
    salario_horario: float = None

    class Config:
        arbitrary_types_allowed = True