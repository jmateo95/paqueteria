from schema import ResponseSchema
from app.services.usuario_service import UsuarioService
from app.models.usuario_model import UsuarioCreate, UsuarioUpdate, UsuarioLogin
from config.config import settings
from config.auth import create_access_token, get_current_user_with_roles
from fastapi import Depends


class UsuarioController:
    def __init__(self):
        self.service = UsuarioService()

    
    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "SuperUser"]))):
        result = await self.service.get_all()
        return ResponseSchema(detail="", result=result)
    

    async def get_by_id(self, usuario_id: int):
        result = await self.service.get_by_id(usuario_id)
        return ResponseSchema(detail="", result=result)

    
    async def create(self, usuario: UsuarioCreate):
        await self.service.create(usuario)
        return ResponseSchema(detail="Usuario creado con éxito")
    

    async def update(self, usuario_id: int, usuario: UsuarioUpdate):
        await self.service.update(usuario_id, usuario)
        return ResponseSchema(detail="")


    async def delete(self, usuario_id: int):
        await self.service.delete(usuario_id)
        return ResponseSchema(detail="")


    async def login(self, credentials: UsuarioLogin):
        usuario = await self.service.login(credentials)
        if usuario:
            access_token = create_access_token(data={"sub": usuario.email, "rol": usuario.rol.nombre})
            return ResponseSchema(detail="Inicio de sesión exitoso", result=access_token)
        else:
            raise ResponseSchema(detail="Credenciales incorrectas")
        

usuario_controller = UsuarioController()
