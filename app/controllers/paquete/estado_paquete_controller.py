from schema import ResponseSchema
from app.services.paquete.estado_paquete_service import EstadoPaqueteService
from app.models.paquete.estado_paquete_model import EstadoPaqueteCreate, EstadoPaqueteUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class EstadoPaqueteController:
    def __init(self):
        self.service = EstadoPaqueteService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        estados_paquete = await self.service.get_all()
        return ResponseSchema(detail="", result=estados_paquete)

    async def get_by_id(self, estado_paquete_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        estado_paquete = await self.service.get_by_id(estado_paquete_id)
        return ResponseSchema(detail="", result=estado_paquete)

    async def create(self, estado_paquete: EstadoPaqueteCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(estado_paquete)
        return ResponseSchema(detail="Estado de Paquete creado con éxito")

    async def update(self, estado_paquete_id: int, estado_paquete: EstadoPaqueteUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(estado_paquete_id, estado_paquete)
        return ResponseSchema(detail="Estado de Paquete actualizado con éxito")

    async def delete(self, estado_paquete_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(estado_paquete_id)
        return ResponseSchema(detail="Estado de Paquete eliminado con éxito")
