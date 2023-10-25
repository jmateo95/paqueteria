from schema import ResponseSchema
from app.services.paquete.paquete_service import PaqueteService
from app.models.paquete.paquete_model import PaqueteCreate, PaqueteUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class PaqueteController:
    def __init(self):
        self.service = PaqueteService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        paquetes = await self.service.get_all()
        return ResponseSchema(detail="", result=paquetes)

    async def get_by_id(self, paquete_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        paquete = await self.service.get_by_id(paquete_id)
        return ResponseSchema(detail="", result=paquete)

    async def create(self, paquete: PaqueteCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(paquete)
        return ResponseSchema(detail="Paquete creado con éxito")

    async def update(self, paquete_id: int, paquete: PaqueteUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(paquete_id, paquete)
        return ResponseSchema(detail="Paquete actualizado con éxito")

    async def delete(self, paquete_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(paquete_id)
        return ResponseSchema(detail="Paquete eliminado con éxito")
