from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    username: str
    email: str
    password: str
    rol_id: int

class UsuarioUpdate(BaseModel):
    nombre: str
    username: str = None
    email: str = None
    password: str = None
    activo: bool = None

    class Config:
        # Permite que los campos sean opcionales
        arbitrary_types_allowed = True


class UsuarioLogin(BaseModel):
    email: str
    password: str