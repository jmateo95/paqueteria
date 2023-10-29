from schema import ResponseSchema
from app.services.paquete.paquete_service import PaqueteService
from app.models.paquete.paquete_model import PaqueteCreate, PaqueteUpdate, PaqueteCotizar
from config.auth import get_current_user_with_roles
from fastapi import Depends

class PaqueteController:
    def __init__(self):
        self.service = PaqueteService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        paquetes = await self.service.get_all()
        return ResponseSchema(detail="", result=paquetes)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        paquete = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=paquete)

    async def create(self, paquete: PaqueteCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        paquete = await self.service.create(paquete)
        return ResponseSchema(detail="Paquete creado con éxito", result=paquete)

    async def update(self, id: int, paquete: PaqueteUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        paquete = await self.service.update(id, paquete)
        return ResponseSchema(detail="Paquete actualizado con éxito", result=paquete)

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Paquete eliminado con éxito")

    async def cotizar(self, paquete: PaqueteCotizar, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        cotizacion=await self.service.cotizar(paquete)
        return ResponseSchema(detail="Paquete cotizado con éxito", result=cotizacion)