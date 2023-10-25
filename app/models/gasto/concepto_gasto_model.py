from pydantic import BaseModel

class ConceptoGastoCreate(BaseModel):
    nombre: str

class ConceptoGastoUpdate(BaseModel):
    nombre: str = None

    class Config:
        arbitrary_types_allowed = True
