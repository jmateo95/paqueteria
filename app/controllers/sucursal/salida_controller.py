from schema import ResponseSchema
from app.services.sucursal.salida_service import SalidaService
from app.models.sucursal.salida_model import SalidaCreate, SalidaUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class SalidaController:
    def __init__(self):
        self.service = SalidaService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        salidas = await self.service.get_all()
        return ResponseSchema(detail="", result=salidas)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        salida = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=salida)

    async def create(self, salida: SalidaCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(salida)
        return ResponseSchema(detail="Salida creada con éxito")

    async def update(self, id: int, salida: SalidaUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(id, salida)
        return ResponseSchema(detail="Salida actualizada con éxito")

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Salida eliminada con éxito")
