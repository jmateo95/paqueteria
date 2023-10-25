from schema import ResponseSchema
from app.services.usuario.rol_service import RolService
from app.models.usuario.rol_model import RolCreate, RolUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class RolController:
    def __init__(self):
        self.service = RolService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.service.get_all()
        return ResponseSchema(detail="", result=roles)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        rol = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=rol)

    async def create(self, rol: RolCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(rol)
        return ResponseSchema(detail="Rol creado con éxito")

    async def update(self, id: int, rol: RolUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(id, rol)
        return ResponseSchema(detail="Rol actualizado con éxito")

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Rol eliminado con éxito")
