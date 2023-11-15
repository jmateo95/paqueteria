from schema import ResponseSchema
from app.services.usuario.usuario_service import UsuarioService
from app.models.usuario.usuario_model import UsuarioCreate, UsuarioUpdate, UsuarioLogin
from config.auth import create_access_token, get_current_user_with_roles
from fastapi import Depends, Query


class UsuarioController:
    def __init__(self):
        self.service = UsuarioService()    

    async def get_users_by_filters(self, sucursal_id: int = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_users_by_filters(sucursal_id=sucursal_id, test=True)
        return ResponseSchema(detail="", result=result)

    async def create(self, usuario: UsuarioCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        usuario.test=True
        result = await self.service.create(usuario)
        return ResponseSchema(detail="Usuario creado con éxito", result=result) 

usuario_controller = UsuarioController()