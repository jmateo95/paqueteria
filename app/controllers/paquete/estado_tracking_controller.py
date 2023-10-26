from schema import ResponseSchema
from app.services.paquete.estado_tracking_service import EstadoTrackingService
from app.models.paquete.estado_tracking_model import EstadoTrackingCreate, EstadoTrackingUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class EstadoTrackingController:
    def __init__(self):
        self.service = EstadoTrackingService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        estados_tracking = await self.service.get_all()
        return ResponseSchema(detail="", result=estados_tracking)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        estado_tracking = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=estado_tracking)

    async def create(self, estado_tracking: EstadoTrackingCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(estado_tracking)
        return ResponseSchema(detail="Estado de Tracking creado con éxito")

    async def update(self, id: int, estado_tracking: EstadoTrackingUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(id, estado_tracking)
        return ResponseSchema(detail="Estado de Tracking actualizado con éxito")

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Estado de Tracking eliminado con éxito")
