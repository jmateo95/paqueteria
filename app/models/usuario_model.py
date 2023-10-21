from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    username: str
    email: str
    password: str
    horas: int
    rol_id: int
    sucursal_id: int
    puesto_id:int


class UsuarioUpdate(BaseModel):
    nombre: str
    username: str = None
    email: str = None
    password: str = None
    horas: int = None
    rol_id: int = None
    sucursal_id: int = None
    puesto_id:int = None


    class Config:
        # Permite que los campos sean opcionales
        arbitrary_types_allowed = True


class UsuarioLogin(BaseModel):
    email: str
    password: str